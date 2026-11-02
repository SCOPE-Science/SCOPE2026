// Independent exhaustive verification of the fence linear-extension theorem.
// Compile: c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int N,allmask,best;
int predmask[16],place[16];
uint64_t total, minimizers;
unordered_set<uint64_t> optimum;

void explore(int taken,int depth,int last,int legal_moves, uint64_t packed){
    if(depth==N){
        total++;
        if(legal_moves<best){best=legal_moves;minimizers=0;optimum.clear();}
        if(legal_moves==best){minimizers++;optimum.insert(packed);}
        return;
    }
    for(int v=0;v<N;v++){
        if((taken&(1<<v))!=0)continue;
        if((predmask[v]&taken)!=predmask[v])continue;
        int add=(depth>0 && abs(last-v)!=1)?1:0;
        place[depth]=v;
        explore(taken|(1<<v),depth+1,v,legal_moves+add,
                packed|((uint64_t)v<<(4*depth)));
    }
}

uint64_t swapped(uint64_t code,int i){
    const uint64_t mask=15ULL;
    uint64_t a=(code>>(4*i))&mask, b=(code>>(4*(i+1)))&mask;
    code&=~((mask<<(4*i))|(mask<<(4*(i+1))));
    return code|(a<<(4*(i+1)))|(b<<(4*i));
}

void verify(int n){
    N=n; total=0; minimizers=0; best=999; optimum.clear();
    for(int i=0;i<n;i++)predmask[i]=0;
    for(int i=0;i<n-1;i++){
        // Even labels (zero-based odd indices) are peaks and follow both neighbours.
        if(i%2==0) predmask[i+1]|=1<<i;
        else predmask[i]|=1<<(i+1);
    }
    explore(0,0,-10,0,0);
    int expected=(n+1)/2-1;
    uint64_t desired=n%2 ? (1ULL<<((n-1)/2)) : 1;
    if(best!=expected||minimizers!=desired||optimum.size()!=desired){
        cerr<<"BAD_MINIMUM "<<n<<' '<<best<<' '<<minimizers<<' '<<desired<<"\n";exit(1);
    }
    uint64_t sum=0;
    for(auto code:optimum){
        int near=0;
        for(int i=0;i<n-1;i++)if(optimum.count(swapped(code,i)))near++;
        if(near!=(n%2?1:0)){cerr<<"BAD_INDUCED_DEGREE "<<n<<"\n";exit(1);}
        sum+=near;
    }
    uint64_t edges=sum/2;
    if(edges!=(n%2 ? (1ULL<<((n-3)/2)) : 0)){
        cerr<<"BAD_INDUCED_EDGES "<<n<<"\n";exit(1);
    }
    cout<<"n="<<n<<" enumerated="<<total<<" min_degree="<<best
        <<" min_count="<<minimizers<<" induced_edges="<<edges<<"\n";
}
int main(){
    for(int n=3;n<=13;n++)verify(n);
    cout<<"INDEPENDENT_FENCE_PASS\n";
}
