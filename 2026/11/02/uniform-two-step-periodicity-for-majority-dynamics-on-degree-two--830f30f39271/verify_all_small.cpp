// Exhaustive labelled base graphs of maximum degree two; no external dependencies.
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
#include <cstdlib>
using namespace std;

static uint32_t evolve(uint32_t s, const vector<uint32_t>& nbr, int N) {
    uint32_t result = 0;
    for (int i=0;i<N;++i) {
        int count = __builtin_popcount(s & nbr[i]);
        int degree = __builtin_popcount(nbr[i]);
        int bit = (s>>i)&1;
        int next = (count*2>degree) ? 1 : ((count*2<degree) ? 0 : bit);
        result |= ((uint32_t) next)<<i;
    }
    return result;
}
int main() {
    for (int n=1;n<=6;++n) {
        vector<pair<int,int>> e;
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)e.emplace_back(i,j);
        uint64_t allowed=0, configurations=0, attaining_two=0;
        for(uint32_t mask=0;mask<(1u<<e.size());++mask) {
            vector<int> degree(n,0);
            vector<uint32_t> adj(2*n,0);
            for(int k=0;k<(int)e.size();++k) if(mask&(1u<<k)) {
                auto [u,v] = e[k]; degree[u]++;degree[v]++;
                adj[u] |= 1u<<v; adj[v] |= 1u<<u;
            }
            bool good=true;
            for(int x:degree)if(x>2)good=false;
            if(!good)continue;
            for(int i=0;i<n;++i) {
                adj[i] |= 1u<<(i+n);
                adj[i+n] |= 1u<<i;
            }
            ++allowed;
            for(uint32_t s=0;s<(1u<<(2*n));++s) {
                uint32_t s1=evolve(s,adj,2*n);
                uint32_t s2=evolve(s1,adj,2*n);
                uint32_t s3=evolve(s2,adj,2*n);
                uint32_t s4=evolve(s3,adj,2*n);
                if(s4!=s2) {cerr<<"FAIL n="<<n<<" mask="<<mask<<" state="<<s<<"\n";return 1;}
                configurations++;
                if(s2!=s && s3!=s1)attaining_two++;
            }
        }
        cout<<"n="<<n<<" admissible_labelled_graphs="<<allowed
            <<" checked_states="<<configurations
            <<" entry_exactly_two="<<attaining_two<<"\n";
    }
    cout<<"VERIFY_OK\n";
}
