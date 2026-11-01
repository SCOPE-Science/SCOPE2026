#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

// Direct graph-neighborhood implementation; no reduction to the petal-count formula.
static uint64_t step(uint64_t state, int n, int m) {
    int N=1+n*m;
    static int cached_n=-1,cached_m=-1;
    static vector<vector<int>> adj;
    if (n!=cached_n || m!=cached_m) {
        cached_n=n;cached_m=m;
        adj.assign(N,{});
        for (int i=0; i<n; ++i) {
            for (int j=0; j<m; ++j) {
                int a=1+i*m+j;
                adj[0].push_back(a);
                adj[a].push_back(0);
                for(int k=0;k<m;++k)if(k!=j)adj[a].push_back(1+i*m+k);
            }
        }
    }
    uint64_t result=0;
    for(int a=0;a<N;++a){
        int cnt=0;
        for(int b:adj[a])cnt+=(state>>b)&1ULL;
        bool value=(2*cnt>static_cast<int>(adj[a].size())) ||
          (2*cnt==static_cast<int>(adj[a].size()) && ((state>>a)&1ULL));
        if(value)result|=1ULL<<a;
    }
    return result;
}

static uint64_t binom(int n,int k) {
    uint64_t v=1;
    for(int i=1;i<=k;++i)v=v*(n-i+1)/i;
    return v;
}
static void verify(int n, int m) {
    assert(n%2==1&&n>=3&&m%2==0&&m>=4);
    int N=1+n*m; assert(N<=25);
    uint64_t u=(1ULL<<(m-1))-binom(m,m/2)/2;
    uint64_t v=(1ULL<<(m-1))+binom(m,m/2)/2;
    vector<uint64_t> basin(1<<n,0);
    bool sharp=false;
    for (uint64_t s=0;s<(1ULL<<N);++s) {
        uint64_t first=step(s,n,m), second=step(first,n,m), third=step(second,n,m);
        if(second!=third){cerr<<"Failed eventual fixation\n";abort();}
        sharp|=(first!=second);
        int P=0;
        for(int i=0;i<n;++i) {
            bool bit=(second>>(1+i*m))&1ULL;
            for(int j=1;j<m;++j)assert(((second>>(1+i*m+j))&1ULL)==bit);
            P|=static_cast<int>(bit)<<i;
        }
        assert((second&1ULL)==static_cast<uint64_t>(2*__builtin_popcount(static_cast<unsigned int>(P))>n));
        ++basin[P];
    }
    auto power=[](uint64_t x,int e){uint64_t y=1;while(e--)y*=x;return y;};
    uint64_t total=0;
    for(int P=0;P<(1<<n);++P){
        int p=__builtin_popcount(static_cast<unsigned int>(P));
        uint64_t want=power(u,p)*power(v,n-p)+power(v,p)*power(u,n-p);
        if(basin[P]!=want){cerr<<"Wrong basin "<<P<<" got "<<basin[P]<<" want "<<want<<"\n";abort();}
        total+=basin[P];
    }
    assert(total==(1ULL<<N) && sharp);
    auto mm=minmax_element(basin.begin(),basin.end());
    cout<<"PASS n="<<n<<", m="<<m<<": states="<<(1ULL<<N)
        <<", fixed="<<(1<<n)<<", basin_min="<<*mm.first
        <<", basin_max="<<*mm.second<<", sharp_two="<<sharp<<"\n";
}
int main(){verify(3,4);verify(5,4);verify(3,6);}
