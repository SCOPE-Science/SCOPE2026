// Independent exhaustive test on the original 32-vertex 5-cube.
// No Clebsch-graph construction or 4-cycle classification is used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
int main() {
    constexpr int N=32,K=8;
    array<uint32_t,N> open_nb{};
    for (int x=0; x<N; ++x)
        for (int bit=0;bit<5;++bit) open_nb[x] |= 1u<<(x^(1<<bit));
    vector<uint32_t> good;
    array<int,K> a{};
    iota(a.begin(),a.end(),0);
    uint64_t tested=0;
    for (;;) {
        uint32_t covered=0,mask=0;
        for(int x:a){covered |= open_nb[x];mask |= 1u<<x;}
        if(covered==UINT32_MAX)good.push_back(mask);
        ++tested;
        int j=K-1;
        while(j>=0 && a[j]==N-K+j)--j;
        if(j<0)break;
        ++a[j];
        for(int k=j+1;k<K;++k)a[k]=a[k-1]+1;
    }
    assert(tested==10518300);
    assert(good.size()==1600);
    unordered_map<uint32_t,int> index;
    for(int i=0;i<(int)good.size();++i)index.emplace(good[i],i);
    vector<vector<int>> adj(good.size());
    for(int i=0;i<(int)good.size();++i){
        uint32_t s=good[i];
        for(int u=0;u<N;++u)if(s&(1u<<u))
            for(int v=u+1;v<N;++v)if(s&(1u<<v))
                for(int x=0;x<N;++x)if(!(s&(1u<<x)))
                    for(int y=x+1;y<N;++y)if(!(s&(1u<<y))){
                        uint32_t next=(s^(1u<<u)^(1u<<v))|(1u<<x)|(1u<<y);
                        auto p=index.find(next);
                        if(p!=index.end())adj[i].push_back(p->second);
                    }
    }
    long long ordered_edges=0;
    for(auto &v:adj){
        sort(v.begin(),v.end());
        assert(unique(v.begin(),v.end())==v.end());
        assert(v.size()==24);
        ordered_edges+=v.size();
    }
    assert(ordered_edges/2==19200);
    // All one-vertex swaps are absent. Check every candidate directly.
    for(uint32_t s: good)
        for(int u=0;u<N;++u)if(s&(1u<<u))
            for(int v=0;v<N;++v)if(!(s&(1u<<v)))
                assert(index.find((s^(1u<<u))|(1u<<v))==index.end());
    // Every distance profile checked by direct BFS, without symmetry assumptions.
    for(int root=0;root<(int)good.size();++root){
        vector<int> dist(good.size(),-1);
        queue<int> q; q.push(root);dist[root]=0;
        array<int,5> hist{};
        while(!q.empty()){
            int x=q.front();q.pop();
            assert(dist[x]>=0&&dist[x]<=4);
            ++hist[dist[x]];
            for(int y:adj[x])if(dist[y]<0){dist[y]=dist[x]+1;q.push(y);}
        }
        assert((hist==array<int,5>{1,24,198,648,729}));
    }
    cout<<"DIRECT_Q5_ALL_8_SUBSETS_ALL_REPLACEMENTS_PASS\n";
    cout<<"tested=10518300 optimum_sets=1600 one_swap_edges=0 two_swap_edges=19200\n";
    cout<<"all_vertex_distance_profile=1,24,198,648,729\n";
}
