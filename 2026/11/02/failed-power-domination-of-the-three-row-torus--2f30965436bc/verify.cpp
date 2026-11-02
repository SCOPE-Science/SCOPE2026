// Exact tests for failed power domination on C_3 box C_n.
// Build: c++ -std=c++17 -O2 torus_verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static vector<uint64_t> neighborhood(int n) {
    vector<uint64_t> adj(3*n);
    for(int j=0;j<n;j++)for(int r=0;r<3;r++){
        int v=3*j+r;
        for(int q=0;q<3;q++)if(q!=r)adj[v]|=1ULL<<(3*j+q);
        adj[v]|=1ULL<<(3*((j+1)%n)+r);
        adj[v]|=1ULL<<(3*((j+n-1)%n)+r);
    }
    return adj;
}
static bool dominates(uint64_t S, int n, const vector<uint64_t>& adj){
    uint64_t all=(1ULL<<(3*n))-1;
    uint64_t seen=S;
    for(int v=0;v<3*n;v++)if((S>>v)&1ULL)seen|=adj[v];
    while(seen!=all){
        uint64_t added=0;
        for(int v=0;v<3*n;v++)if((seen>>v)&1ULL){
            uint64_t missing=adj[v]&~seen;
            if(missing && (missing&(missing-1))==0)added|=missing;
        }
        if(!added)return false;
        seen|=added;
    }
    return true;
}
static uint64_t witness(int n){
    uint64_t S=0;
    for(int j=0;j<=n-2;j+=2)S|=1ULL<<(3*j);
    return S;
}
int main(){
    for(int n=3;n<=7;n++){
        auto adj=neighborhood(n);
        int best=-1;
        uint64_t number=0;
        for(uint64_t S=0;S<(1ULL<<(3*n));S++){
            if(!dominates(S,n,adj)){
                int w=__builtin_popcountll(S);
                if(w>best){best=w;number=1;}
                else if(w==best)number++;
            }
        }
        assert(best==n/2);
        assert(!dominates(witness(n),n,adj));
        assert(__builtin_popcountll(witness(n))==n/2);
        cout<<"EXHAUSTIVE n="<<n<<" max="<<best<<" optimal_sets="<<number<<"\n";
    }
    for(int n=3;n<=20;n++){
        auto adj=neighborhood(n);
        assert(!dominates(witness(n),n,adj));
        if(n<=13){
            for(int j=0;j<n;j++){
                // Three sensors in one triangle necessarily dominate.
                assert(dominates(7ULL<<(3*j),n,adj));
                for(int d=1;d<=3;d++){
                    int k=(j+d)%n;
                    if(k==j)continue;
                    // All row subsets of the two selected triangles.
                    for(int A=1;A<=3;A++)for(int B=1;B<=3;B++){
                        for(int maskA=1;maskA<8;maskA++)if(__builtin_popcount(maskA)==A)
                        for(int maskB=1;maskB<8;maskB++)if(__builtin_popcount(maskB)==B){
                            if(d>=A+B)continue;
                            uint64_t S=((uint64_t)maskA<<(3*j))|((uint64_t)maskB<<(3*k));
                            assert(dominates(S,n,adj));
                        }
                    }
                }
            }
        }
    }
    cout<<"VERIFY_OK\n";
}
