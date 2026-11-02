// Two independent exhaustive methods for the 24-site model (2^24 configurations).
// Compile: c++ -O3 -std=c++17 census_independent.cpp -o census && ./census
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
  constexpr int D=3,L=8,N=D*L,WIDTH=(1<<N); array<uint32_t,N> nb{};
  vector<pair<int,int>> edges;
  for(int i=0;i<D;i++)for(int s=0;s<L;s++){
    int u=i*L+s;
    for(int j=i+1;j<D;j++)edges.emplace_back(u,j*L+s);
    for(int j=0;j<D;j++)if(i!=j && s<(s^(1<<j)))edges.emplace_back(u,i*L+(s^(1<<j)));
  }
  if(edges.size()!=48) return 10;
  for(auto [a,b]:edges){nb[a]|=1u<<b;nb[b]|=1u<<a;}
  for(int v=0;v<N;v++)if(__builtin_popcount(nb[v])!=4)return 11;
  array<int,N+1> top1,top2;
  top1.fill(-1);top2.fill(-1);
  array<uint64_t,N+1> cnt1{},cnt2{};
  // Method A: Gray sequence, update cut by flipping one spin.
  uint32_t mask=0;int k=0,cut=0;
  for(uint32_t t=0;t<WIDTH;t++){
    if(t){int v=__builtin_ctz(t);bool old=(mask>>v)&1;int q=__builtin_popcount(mask&nb[v]);int oldCross=old?4-q:q;
      cut+=4-2*oldCross;k+=old?-1:1;mask^=1u<<v;}
    if(cut>top1[k]){top1[k]=cut;cnt1[k]=1;} else if(cut==top1[k])++cnt1[k];
  }
  // Method B: direct low-bit recurrence for induced-edge count, not Gray updates.
  vector<uint8_t> internal(WIDTH); // max 48 fits
  for(uint32_t s=0;s<WIDTH;s++){
    if(s){int v=__builtin_ctz(s);uint32_t prev=s&(s-1);internal[s]=internal[prev]+__builtin_popcount(prev&nb[v]);}
    int n=__builtin_popcount(s),value=4*n-2*internal[s];
    if(value>top2[n]){top2[n]=value;cnt2[n]=1;}else if(value==top2[n])++cnt2[n];
  }
  uint64_t total=0;
  for(int n=0;n<=N;n++){
    int r=min(n,N-n),q=r/L;int expected=2*(D-1-q)*r+L*q*(q+1);
    if(top1[n]!=top2[n]||cnt1[n]!=cnt2[n]||top1[n]!=expected)return 20+n;
    cout<<n<<" "<<top1[n]<<" "<<cnt1[n]<<"\n";
    total+=cnt1[n];
  }
  if(total<=0)return 99;
  cout<<"all 25 sectors, both exhaustive methods and formula agree\n";
}
