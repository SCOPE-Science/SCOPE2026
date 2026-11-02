#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <stdexcept>

// Independently enumerates labelled configurations of matched-deleted bicliques.
// Two shores contain n vertices each; index i is not adjacent to index i+n.
static uint32_t transition(uint32_t state, int n) {
    int x[16];
    uint32_t z = state;
    int a1 = 0, b1 = 0;
    for (int i=0;i<2*n;++i) {
        x[i] = z % 3;
        z /= 3;
        if (x[i] == 1) (i<n ? a1 : b1)++;
    }
    uint32_t result = 0, pow = 1;
    for (int i=0;i<2*n;++i) {
        int old = x[i];
        int match = i<n ? i+n : i-n;
        int neighbors_blinking = (i<n ? b1 : a1) - (x[match]==1);
        int fresh = (old == 2 && neighbors_blinking > 0) ? 2 : (old+1)%3;
        result += pow * fresh;
        pow *= 3;
    }
    return result;
}

static uint64_t b4_formula(int n) {
    uint64_t p4=1, p2=1;
    for(int i=0;i<n;++i) {p4*=4; p2*=2;}
    int64_t v = (int64_t)((n*n+7*n+16)*p4/8)
      -(int64_t)((n*n+5*n+8)*p2)
      -n*(n-1)*(n-2)*(n-3)+4*n*(n-1)+8;
    return (uint64_t)v;
}

int main() {
    for(int n=2;n<=7;++n) {
        uint32_t N=1;
        for (int k=0;k<2*n;++k) N*=3;
        std::vector<uint32_t> nxt(N), marker(N,0), index(N,0);
        std::vector<uint8_t> period(N,0), tau(N,0);
        for (uint32_t x=0;x<N;++x) nxt[x]=transition(x,n);
        std::vector<uint32_t> path;
        path.reserve(256);
        uint32_t tag=0;
        for (uint32_t start=0;start<N;++start) {
            if (period[start]) continue;
            ++tag; path.clear();
            uint32_t x=start;
            while(period[x]==0 && marker[x]!=tag) {
                marker[x]=tag;
                index[x]=(uint32_t)path.size();
                path.push_back(x);
                x=nxt[x];
            }
            if (period[x]==0) {
                uint32_t r=index[x];
                uint32_t cyc=(uint32_t)path.size()-r;
                if (cyc>255) throw std::runtime_error("cycle overflows period storage");
                for(uint32_t j=r;j<path.size();++j) {
                    period[path[j]]=(uint8_t)cyc; tau[path[j]]=0;
                }
                path.resize(r);
            }
            for(size_t j=path.size();j-->0;) {
                uint32_t y=path[j], f=nxt[y];
                period[y]=period[f];
                tau[y]=uint8_t(tau[f]+1);
            }
        }
        std::map<int,uint64_t> basin,recurrent;
        int max_tau=0;
        for(uint32_t x=0;x<N;++x) {
            int p=period[x],t=tau[x];
            basin[p]++;
            if(t==0) recurrent[p]++;
            max_tau=std::max(t,max_tau);
        }
        uint64_t total=0;
        for(auto [p,k]:basin) total+=k;
        if(total!=N) throw std::runtime_error("basin sum disagrees");
        if(n==2) {
            if(max_tau!=3 || basin!=std::map<int,uint64_t>{{3,81}})
                throw std::runtime_error("n=2 mismatch");
        } else if(n==3) {
            if(max_tau!=9 || basin!=std::map<int,uint64_t>{{3,585},{18,144}} || recurrent[18]!=72)
                throw std::runtime_error("n=3 mismatch");
        } else {
            uint64_t b4=b4_formula(n);
            uint64_t r4=2;
            for(int j=0;j<n;++j)r4*=4;
            uint64_t p2=1;
            for(int j=0;j<n;++j)p2*=2;
            r4 -= (4*n+8)*p2;
            r4 += n*(n-1)*(n-2)*(n-3)+8*n+8;
            if(basin!=std::map<int,uint64_t>{{3,N-b4},{4,b4}} || recurrent[4]!=r4 || max_tau!=(n==4?9:13))
                throw std::runtime_error("n>=4 mismatch");
        }
        std::cout << "n="<<n<<" labelled_states="<<N<<" max_entry="<<max_tau;
        for(auto [p,k]:basin) std::cout<<" basin_"<<p<<"="<<k;
        for(auto [p,k]:recurrent) std::cout<<" recurrent_"<<p<<"="<<k;
        std::cout<<"\n";
    }
    std::cout<<"INDEPENDENT_VERTEX_CHECK_OK\n";
}
