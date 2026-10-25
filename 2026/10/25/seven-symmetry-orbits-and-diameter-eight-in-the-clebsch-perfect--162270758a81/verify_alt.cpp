// Independent exhaustive verifier: a different matching and flip representation.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_alt.cpp -o verify_alt
// Run: ./verify_alt
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
static const int N = 16;
static const int gen[5]={1,2,4,8,15};
struct Edge { int u,v; };
vector<Edge> edges;
int edge_idx[16][16];
vector<uint64_t> matchbits;

void recurse(unsigned freebits, uint64_t chosen) {
    if (freebits==0) {matchbits.push_back(chosen);return;}
    int a=__builtin_ctz(freebits);
    unsigned rest=freebits & ~(1u<<a);
    for (int s:gen) {
        int b=a^s;
        if (rest & (1u<<b)) {
            int pos=edge_idx[a][b];
            assert(pos>=0);
            recurse(rest & ~(1u<<b),chosen | (1ULL<<pos));
        }
    }
}
int main() {
    for (auto &row:edge_idx) for(int &v:row)v=-1;
    for(int i=0;i<N;++i)for(int j=i+1;j<N;++j){
        int x=i^j;
        if(find(begin(gen),end(gen),x)!=end(gen)){
            int id=int(edges.size()); edges.push_back({i,j});
            edge_idx[i][j]=edge_idx[j][i]=id;
        }
    }
    assert(edges.size()==40);
    recurse((1u<<N)-1,0);
    sort(matchbits.begin(),matchbits.end());
    assert(unique(matchbits.begin(),matchbits.end())==matchbits.end());
    assert(matchbits.size()==705);
    vector<vector<int>> adj(705);
    // All unordered pairs: a 4-edge symmetric difference of perfect matchings
    // must itself be a single alternating quadrilateral.
    for(int a=0;a<705;++a)for(int b=a+1;b<705;++b){
        uint64_t sym=matchbits[a]^matchbits[b];
        if(__builtin_popcountll(sym)==4){
            adj[a].push_back(b);adj[b].push_back(a);
        }
    }
    map<int,int> degree, ecc, lengths;
    long long edgecount=0;
    for(auto &v:adj){degree[int(v.size())]++;edgecount+=v.size();}
    assert(edgecount==4320);
    assert((degree==map<int,int>{{4,200},{6,360},{8,60},{10,80},{16,5}}));
    for(int src=0;src<705;++src){
        vector<int> dist(705,-1);queue<int> q;
        q.push(src);dist[src]=0;
        while(!q.empty()){
            int x=q.front();q.pop();
            for(int y:adj[x])if(dist[y]==-1){dist[y]=dist[x]+1;q.push(y);}
        }
        assert(all_of(dist.begin(),dist.end(),[](int x){return x>=0;}));
        ecc[*max_element(dist.begin(),dist.end())]++;
        for(int y=src+1;y<705;++y)lengths[dist[y]]++;
    }
    assert((ecc==map<int,int>{{7,5},{8,700}}));
    assert((lengths==map<int,int>{{1,2160},{2,8040},{3,22360},{4,45160},
                                 {5,64800},{6,61920},{7,34880},{8,8840}}));
    cout<<"INDEPENDENT_OK vertices=705 edges=2160 radius=7 diameter=8\n";
    cout<<"ALL_VERIFY_OK\n";
}
