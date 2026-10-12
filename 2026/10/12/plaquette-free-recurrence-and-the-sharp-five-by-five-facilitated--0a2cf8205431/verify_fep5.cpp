// Exact finite-state verifier for the directional facilitated exclusion process
// on the 5-by-5 periodic square lattice. Public-domain mathematical code.
// Build: g++ -O3 -std=c++17 verify_fep5.cpp -o verify_fep5
// Run:   ./verify_fep5
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

struct Move { uint32_t facilitator, source, destination; };
static vector<Move> make_moves() {
    vector<Move> moves;
    constexpr int n = 5;
    constexpr int dr[4] = {1,-1,0,0};
    constexpr int dc[4] = {0,0,1,-1};
    for(int r=0;r<n;++r) for(int c=0;c<n;++c)
        for(int t=0;t<4;++t) {
            int fr=(r-dr[t]+n)%n, fc=(c-dc[t]+n)%n;
            int rr=(r+dr[t]+n)%n, cc=(c+dc[t]+n)%n;
            moves.push_back({1u<<(fr*n+fc),1u<<(r*n+c),1u<<(rr*n+cc)});
        }
    assert(moves.size()==100);
    return moves;
}
static vector<uint32_t> make_plaquettes() {
    vector<uint32_t> boxes;
    for(int r=0;r<5;++r)for(int c=0;c<5;++c) {
        uint32_t box=0;
        for(int dr=0;dr<2;++dr)for(int dc=0;dc<2;++dc)
            box|=1u<<(((r+dr)%5)*5+(c+dc)%5);
        boxes.push_back(box);
    }
    return boxes;
}
static vector<uint32_t> make_masks(int h,vector<int32_t>& index) {
    vector<uint32_t> masks;
    uint32_t x=(1u<<h)-1u;
    while(x<(1u<<25)) {
        index[x]=static_cast<int32_t>(masks.size());
        masks.push_back(x);
        const uint32_t y=x&-x;
        const uint32_t z=x+y;
        if(z==0)break;
        x=z|(((x^z)>>2)/y);
    }
    return masks;
}
static int next_id(uint32_t vacancy, const Move &m, bool reverse,
                   const vector<int32_t>& index) {
    // Vacancy-mask forward move: 110 -> 101 on (facilitator,source,destination).
    // Its predecessor test is 101 in the POST-state; the original 110 is reconstructed.
    if(!reverse) {
        if(!(vacancy&m.destination) || (vacancy&(m.facilitator|m.source)))return -1;
    } else {
        if(!(vacancy&m.source) || (vacancy&(m.facilitator|m.destination)))return -1;
    }
    return index[vacancy ^ m.source ^ m.destination];
}
struct Frame { int id; uint8_t next_move; };
struct Outcome {
    int h; size_t vertices,edges,components,terminal_components,recurrent_states;
    vector<int> terminal_sizes;
};
static Outcome evaluate(int h, const vector<Move>& moves, const vector<uint32_t>& plaquettes) {
    vector<int32_t> index(1u<<25,-1);
    auto masks=make_masks(h,index);
    const int n=static_cast<int>(masks.size());
    vector<uint8_t> visited(n,0);
    vector<int> finish; finish.reserve(n);
    vector<Frame> st; st.reserve(n);
    size_t edges=0;
    // First pass: explicit-stack forward DFS; order vertices by exit time.
    for(int root=0;root<n;++root) if(!visited[root]) {
        visited[root]=1;
        st.push_back({root,0});
        while(!st.empty()) {
            Frame &top=st.back();
            if(top.next_move==moves.size()) {
                finish.push_back(top.id);
                st.pop_back();
                continue;
            }
            const Move& move=moves[top.next_move++];
            int neighbor=next_id(masks[top.id],move,false,index);
            if(neighbor<0)continue;
            ++edges;
            if(!visited[neighbor]) {
                visited[neighbor]=1;
                st.push_back({neighbor,0});
            }
        }
    }
    if(finish.size()!=masks.size())throw runtime_error("incomplete forward exploration");
    // Second pass: reverse DFS in reverse exit order; Kosaraju SCC labels.
    vector<int> label(n,-1),sz;
    vector<int> q; q.reserve(n);
    for(auto it=finish.rbegin();it!=finish.rend();++it) {
        int root=*it;
        if(label[root]!=-1)continue;
        int cid=static_cast<int>(sz.size());
        sz.push_back(0);
        q.push_back(root);
        label[root]=cid;
        while(!q.empty()) {
            int u=q.back();q.pop_back();++sz[cid];
            for(const Move& move:moves) {
                int predecessor=next_id(masks[u],move,true,index);
                if(predecessor>=0 && label[predecessor]==-1) {
                    label[predecessor]=cid;
                    q.push_back(predecessor);
                }
            }
        }
    }
    vector<uint8_t> terminal(sz.size(),1);
    for(int u=0;u<n;++u) for(const Move& move:moves) {
        int v=next_id(masks[u],move,false,index);
        if(v>=0 && label[u]!=label[v])terminal[label[u]]=0;
    }
    // Verify the actual recurrent-set membership, not just its cardinality.
    // A configuration is predicted recurrent exactly when no 2x2 plaquette is empty.
    size_t plaquette_free=0;
    for(int u=0;u<n;++u) {
        bool contains_empty_box=false;
        for(uint32_t box:plaquettes)
            if((masks[u]&box)==box) {contains_empty_box=true;break;}
        bool should_recur=!contains_empty_box;
        if(should_recur)++plaquette_free;
        if(bool(terminal[label[u]])!=should_recur)
            throw runtime_error("recurrent-set / plaquette-free disagreement");
    }
    Outcome result{h,static_cast<size_t>(n),edges,sz.size(),0,0,{}};
    for(size_t i=0;i<sz.size();++i)if(terminal[i]) {
        ++result.terminal_components;
        result.recurrent_states+=sz[i];
        result.terminal_sizes.push_back(sz[i]);
    }
    sort(result.terminal_sizes.begin(),result.terminal_sizes.end());
    if(result.recurrent_states!=plaquette_free)
        throw runtime_error("plaquette-free count mismatch");
    return result;
}
int main() {
    try {
        auto moves=make_moves();
        auto plaquettes=make_plaquettes();
        const array<array<size_t,5>,8> expected{{
           {{25,100,1,1,25}},
           {{300,2200,1,1,300}},
           {{2300,23100,1,1,2300}},
           {{12650,154000,26,1,12625}},
           {{53130,731500,26,1,52605}},
           {{177100,2633400,76,1,171900}},
           {{480700,7461300,126,1,448450}},
           {{1081575,17054400,426,1,941450}}
        }};
        for(int h=1;h<=8;++h) {
            auto r=evaluate(h,moves,plaquettes);
            auto e=expected[h-1];
            cout << "holes=" << h << " states=" << r.vertices << " edges=" << r.edges
                 << " scc=" << r.components << " terminal=" << r.terminal_components
                 << " recurrent=" << r.recurrent_states << '\n';
            if(r.vertices!=e[0] || r.edges!=e[1] || r.components!=e[2] ||
               r.terminal_components!=e[3] || r.recurrent_states!=e[4] ||
               r.terminal_sizes!=vector<int>{static_cast<int>(e[4])})
                throw runtime_error("count mismatch");
        }
        cout << "VERIFY_OK eight high-density sectors and plaquette-free characterization" << endl;
    } catch(const exception& e) {
        cerr << "VERIFICATION_FAILED: " << e.what() << endl;
        return 1;
    }
    return 0;
}
