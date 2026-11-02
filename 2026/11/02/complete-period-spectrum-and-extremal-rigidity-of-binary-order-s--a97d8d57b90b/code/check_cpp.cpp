// Independent exhaustive edge-minimum enumeration of binary order-seven
// orientable necklaces.  C++17, no third-party libraries.
#include <bits/stdc++.h>
using namespace std;

constexpr int n = 7;
constexpr int vertex_mask = (1 << (n-1))-1;
int reversed_edge[1 << n], pair_number[1 << n];
uint64_t states = 0;
map<int,set<string>> words;
vector<int> edges;

string canonical(const string& s) {
    string best=s;
    for (int k=1; k<(int)s.size(); ++k) {
        string t=s.substr(k)+s.substr(0,k);
        if (t<best) best=t;
    }
    return best;
}

void explore(int root_vertex,int vertex,int smallest_edge,uint64_t used) {
    ++states;
    for (int b=0;b<2;++b) {
        int e=(vertex<<1)|b;
        if (e<smallest_edge || e==reversed_edge[e]) continue;
        uint64_t bit=uint64_t(1)<<pair_number[e];
        if (used&bit) continue;
        int next=e&vertex_mask;
        if (next==root_vertex) {
            // For a circular word, the final symbols of the visited
            // seven-bit windows form the cyclic word up to rotation.
            string w;
            for (int a:edges) w+=char('0'+(a&1));
            w+=char('0'+b);
            words[(int)w.size()].insert(canonical(w));
        }
        edges.push_back(e);
        explore(root_vertex,next,smallest_edge,used|bit);
        edges.pop_back();
    }
}

int main(int argc,char**argv) {
    if (argc!=2) {cerr<<"usage: check_cpp certificate_path\n";return 2;}
    for (int e=0;e<(1<<n);++e) {
        int r=0,t=e;
        for (int j=0;j<n;++j) {r=(r<<1)|(t&1);t>>=1;}
        reversed_edge[e]=r;
    }
    int id=0;
    for (int e=0;e<(1<<n);++e)
        if (e<reversed_edge[e]) {
            pair_number[e]=pair_number[reversed_edge[e]]=id++;
        }
    if (id!=56) return 3;
    for (int root=0;root<(1<<n);++root) {
        if (root==reversed_edge[root]) continue;
        edges.clear();edges.push_back(root);
        explore(root>>1,root&vertex_mask,root,uint64_t(1)<<pair_number[root]);
    }
    vector<string> known;
    ifstream fin(argv[1]);string item;
    while (getline(fin,item)) known.push_back(item);
    if (!fin.eof()) return 4;
    vector<string> computed(words[36].begin(),words[36].end());
    if (known!=computed) {cerr<<"certificate mismatch\n";return 5;}
    long total=0;
    for (auto& [length,ss]:words) total+=ss.size();
    if (total!=4788 || words.rbegin()->first!=36 || words[36].size()!=336)
        return 6;
    cout<<"CHECK_CPP_OK; states="<<states<<"; all_necklaces="<<total
        <<"; maximum_length=36; optimal_necklaces="<<words[36].size()<<"\n";
    cout<<"PERIOD_COUNTS=";
    bool first=true;
    for (auto& [length,ss]:words) {
        if(!first)cout<<",";first=false;
        cout<<length<<":"<<ss.size();
    }
    cout<<"\n";
    return 0;
}
