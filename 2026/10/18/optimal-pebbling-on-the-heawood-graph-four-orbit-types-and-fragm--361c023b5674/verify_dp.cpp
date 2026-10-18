// Exact recursive pebbling-state dynamic program for the Fano-incidence graph.
// Compile: c++ -O2 -std=c++17 verify_dp.cpp -o verify_dp && ./verify_dp
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

static array<vector<int>,14> edges;
static unordered_map<uint64_t,uint16_t> cache;
static vector<uint64_t> solutions;
static long long candidates=0;
static const uint16_t ALL=(1u<<14)-1;

uint16_t reachable(uint64_t state) {
    auto it=cache.find(state);
    if(it!=cache.end()) return it->second;
    uint16_t out=0;
    for(int u=0;u<14;u++) if((state>>(4*u))&15u) out|=uint16_t(1u<<u);
    for(int u=0;u<14;u++) if(((state>>(4*u))&15u)>=2)
        for(int v:edges[u]) out|=reachable(state-(uint64_t(2)<<(4*u))+(uint64_t(1)<<(4*v)));
    cache[state]=out;
    return out;
}

void distribute(int index, int remaining, uint64_t state) {
    if(index==13) {
        candidates++;
        uint64_t complete=state+(uint64_t(remaining)<<(4*index));
        if(reachable(complete)==ALL) solutions.push_back(complete);
        return;
    }
    for(int m=0;m<=remaining;m++) distribute(index+1,remaining-m,state+(uint64_t(m)<<(4*index)));
}

int level(uint64_t s,int i) { return (s>>(4*i))&15u; }

vector<int> graphdist(int r) {
    vector<int> ds(14,-1);ds[r]=0;
    queue<int> q;q.push(r);
    while(!q.empty()) {int v=q.front();q.pop();for(int w:edges[v])
        if(ds[w]<0){ds[w]=ds[v]+1;q.push(w);}}
    return ds;
}

bool geometric(uint64_t s, const vector<vector<int>>& ds) {
    vector<int> vs; vector<int> weight(5);
    for(int i=0;i<14;i++) if(level(s,i)) {vs.push_back(i);if(level(s,i)<=4) weight[level(s,i)]++;}
    if(vs.size()==2 && weight[4]==1 && weight[2]==1){
        int u=level(s,vs[0])==4?vs[0]:vs[1];
        int v=level(s,vs[0])==2?vs[0]:vs[1];
        return ds[u][v]==1 || ds[u][v]==3;
    }
    if(vs.size()==2 && weight[3]==2)return ds[vs[0]][vs[1]]==1;
    if(vs.size()==3 && weight[4]==1 && weight[1]==2){
        bool same_side=true;
        for(int v:vs) if((v<7)!=(vs[0]<7)) same_side=false;
        if(!same_side) return false;
        if(vs[0]<7){
            for(int j=7;j<14;j++) {
                bool ok=true;for(int v:vs) if(ds[v][j]!=1)ok=false;
                if(ok)return true;
            }
        }else{
            for(int p=0;p<7;p++){
                bool ok=true;for(int v:vs)if(ds[v][p]!=1)ok=false;
                if(ok)return true;
            }
        }
    }
    return false;
}

int main() {
    for(int j=0;j<7;j++)for(int d:{0,1,3}){
        int p=(j+d)%7;
        edges[p].push_back(7+j);
        edges[7+j].push_back(p);
    }
    for(int i=0;i<14;i++)assert(edges[i].size()==3);
    vector<vector<int>> ds;
    for(int i=0;i<14;i++){
        ds.push_back(graphdist(i));
        for(int j=0;j<14;j++)assert(ds.back()[j]>=0 && ds.back()[j]<=3);
    }
    cache.reserve(45000);
    const int expect_candidates[]={1,14,105,560,2380,8568,27132};
    for(int k=0;k<=6;k++) {
        solutions.clear();candidates=0;
        distribute(0,k,0);
        assert(candidates==expect_candidates[k]);
        if(k<6)assert(solutions.empty());
        if(k==6)assert(solutions.size()==161);
    }
    set<uint64_t> optimal(solutions.begin(),solutions.end());
    assert(optimal.size()==161);
    map<array<int,4>,int> types;
    for(uint64_t s:solutions) {
        assert(geometric(s,ds));
        array<int,4> typ{};for(int u=0;u<14;u++)if(level(s,u))typ[level(s,u)-1]++;
        types[typ]++;
    }
    assert(types.size()==3);
    int n42=0,n33=0,n411=0;
    for(auto const& [t,num]:types){
        if(t[3]==1 && t[1]==1) {assert(num==98);n42=num;}
        else if(t[2]==2){assert(num==21);n33=num;}
        else if(t[3]==1 && t[0]==2){assert(num==42);n411=num;}
        else assert(false);
    }
    // Check every geometrically described six-pebble distribution, not just the valid ones.
    candidates=0;
    for(int k=6;k<=6;k++){
        // By enumerating all positions with the same generator, the equality follows
        // from the 161 successful states and the formula's independently counted size.
        int geo_count=0;
        // Enumerate 6 pebble placement vectors by rank using an iterative stars-and-bars expansion.
        vector<array<int,14>> todo(1);todo[0].fill(0);
        for(int rep=0;rep<6;rep++){
            vector<array<int,14>> nxt;
            set<array<int,14>> unique;
            for(const auto& s:todo)for(int i=0;i<14;i++){
                auto q=s;q[i]++;
                unique.insert(q);
            }
            nxt.assign(unique.begin(),unique.end());todo.swap(nxt);
        }
        assert(todo.size()==27132);
        for(const auto& q:todo) {
            uint64_t s=0;for(int i=0;i<14;i++)s|=uint64_t(q[i])<<(4*i);
            if(geometric(s,ds)){
                geo_count++;
                assert(optimal.count(s));
            }
        }
        assert(geo_count==161);
    }
    map<uint64_t,int> id;
    for(int i=0;i<(int)solutions.size();i++)id[solutions[i]]=i;
    set<pair<int,int>> transitions,nonlocal;
    for(int i=0;i<(int)solutions.size();i++){
        uint64_t s=solutions[i];
        for(int u=0;u<14;u++)if(level(s,u))for(int v=0;v<14;v++)if(u!=v){
            uint64_t t=s-(1ull<<(4*u))+(1ull<<(4*v));
            auto f=id.find(t);
            if(f!=id.end() && i<f->second){
                nonlocal.emplace(i,f->second);
                for(int w:edges[u])if(w==v)transitions.emplace(i,f->second);
            }
        }
    }
    assert(transitions.size()==42 && transitions==nonlocal);
    vector<set<int>> nbr(161);
    for(auto [a,b]:transitions){nbr[a].insert(b);nbr[b].insert(a);}
    map<int,int> degrees;
    for(const auto& s:nbr)degrees[(int)s.size()]++;
    assert(degrees[0]==98 && degrees[1]==42 && degrees[2]==21);
    set<int> unseen;for(int i=0;i<161;i++)unseen.insert(i);
    map<int,int> comps;
    while(!unseen.empty()){
        int r=*unseen.begin();unseen.erase(r);
        vector<int> q={r};
        for(size_t a=0;a<q.size();a++)for(int t:nbr[q[a]])if(unseen.erase(t))q.push_back(t);
        comps[(int)q.size()]++;
        if(q.size()==3){int degs=0;for(int t:q)degs+=(int)nbr[t].size();assert(degs==4);}
    }
    assert(comps[1]==98 && comps[3]==21 && comps.size()==2);
    cout<<"{\"graph\":\"Fano incidence graph via cyclic difference set\",\"candidate_counts\":[1,14,105,560,2380,8568,27132],\"optimal_counts\":[0,0,0,0,0,0,161],\"types\":{\"4+2\":"<<n42<<",\"3+3\":"<<n33<<",\"4+1+1\":"<<n411<<"},\"reconfiguration\":{\"edges\":"<<transitions.size()<<",\"isolated\":"<<comps[1]<<",\"three_vertex_paths\":"<<comps[3]<<",\"same_when_nonlocal_moves_allowed\":true},\"pebbling_states_checked\":"<<cache.size()<<"}\n";
}
