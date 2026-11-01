#include <iostream>
#include <vector>
#include <cstdint>
#include <stdexcept>

// Independent microscopic verification for synchronous parallel chip-firing.
// Fan F_n is a hub (vertex 0) joined to the path 1,...,n.
static std::vector<int> step(const std::vector<int>& c,
                             const std::vector<std::vector<int>>& adj) {
    const int s=(int)c.size();
    std::vector<int> out(c);
    for(int v=0;v<s;++v) {
        if(c[v] >= (int)adj[v].size()) {
            out[v]-=(int)adj[v].size();
            for(int w:adj[v])++out[w];
        }
    }
    return out;
}
int main() {
    for(int n=2;n<=8;++n) {
        const int s=n+1;
        std::vector<std::vector<int>> adj(s);
        auto edge=[&](int u,int v){adj[u].push_back(v);adj[v].push_back(u);};
        for(int i=1;i<=n;++i)edge(0,i);
        for(int i=1;i<n;++i)edge(i,i+1);
        std::vector<int> radix(s);uint64_t total=1;
        for(int i=0;i<s;++i){radix[i]=2*(int)adj[i].size();total*=radix[i];}
        uint64_t states=0;
        std::vector<int> c(s,0);
        for(uint64_t idx=0;idx<total;++idx) {
            auto a=step(c,adj), b=step(a,adj);
            if(b==c && a!=c) ++states;
            for(int i=0;i<s;++i) {if(++c[i]<radix[i]) break; c[i]=0;}
        }
        if(states%2!=0)throw std::runtime_error("non-even periodic count");
        std::cout<<"n="<<n<<" scanned="<<total<<" primitive_states="<<states
                 <<" orbits="<<(states/2)<<'\n';
    }
}
