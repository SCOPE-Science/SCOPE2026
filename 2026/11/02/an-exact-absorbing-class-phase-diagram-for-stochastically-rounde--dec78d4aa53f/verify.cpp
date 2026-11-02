#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>

// Integer-exact directed-support census for one-step stochastic rounding of
// f(x)=4x(1-x) on {0,1/N,...,1}. No random sampling or floating arithmetic.
int main(int argc, char** argv) {
    int limit = 65536;
    int start = 2;
    if (argc >= 2) limit = std::stoi(argv[1]);
    if (argc >= 3) start = std::stoi(argv[2]);
    if (limit < 2 || limit > 65536 || start < 2 || start > limit) throw std::invalid_argument("limit");
    std::vector<int> head(limit+1), from(2*(limit+1)), next(2*(limit+1));
    std::vector<int> dist(limit+1), queue(limit+1);
    int globalMax = 0, atN = 0;
    std::uint64_t totalStates = 0, totalEdges = 0;
    for (int N=start; N<=limit; ++N) {
        std::fill(head.begin(),head.begin()+N+1,-1);
        std::fill(dist.begin(),dist.begin()+N+1,-1);
        int ec = 0;
        for (int j=0; j<=N; ++j) {
            std::uint64_t num = 4ULL*static_cast<std::uint64_t>(j)*static_cast<std::uint64_t>(N-j);
            int lo = static_cast<int>(num / N);
            int hi = static_cast<int>((num + N - 1) / N);
            if (lo < 0 || hi > N || hi-lo>1) throw std::runtime_error("bounds");
            from[ec]=j; next[ec]=head[lo]; head[lo]=ec++;
            if (hi!=lo) {from[ec]=j;next[ec]=head[hi];head[hi]=ec++;}
        }
        totalStates+=static_cast<std::uint64_t>(N)+1;
        totalEdges+=ec;
        int first=0,last=1;
        queue[0]=0;dist[0]=0;
        int dmax=0;
        while(first<last){
            int v=queue[first++];
            for(int e=head[v];e!=-1;e=next[e]){
                int j=from[e];
                if(dist[j]==-1){dist[j]=dist[v]+1;dmax=std::max(dmax,dist[j]);queue[last++]=j;}
            }
        }
        int missing=0;
        for(int j=0;j<=N;++j){
            bool expected=(N%4==0 && (j==N/4 || j==3*N/4));
            bool actual=dist[j]==-1;
            if(actual!=expected){
                std::cerr<<"FAIL N="<<N<<" j="<<j<<" actual="<<actual<<" expected="<<expected<<"\n";
                return 1;
            }
            if(actual)++missing;
        }
        if(missing!=(N%4==0?2:0))throw std::runtime_error("count");
        if(dmax>globalMax){globalMax=dmax;atN=N;}
        if(N==255 || N==256 || N==65535 || N==65536){
           std::cout<<"N="<<N<<" states="<<N+1<<" edges="<<ec<<" missing="<<missing<<" max_path="<<dmax<<"\n";
        }
    }
    std::cout<<"PASS grids="<<limit-start+1<<" total_states="<<totalStates<<" total_edges="<<totalEdges<<" global_max_shortest_path="<<globalMax<<" first_at_N="<<atN<<"\n";
}
