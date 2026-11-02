#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
 for(int k=1;k<=6;k++) {
  int n=2+2*k;
  vector<vector<int>> neighbors(n);
  auto edge=[&](int a,int b){ neighbors[a].push_back(b);neighbors[b].push_back(a); };
  edge(0,1);
  for(int i=0;i<k;i++) {int a=2+2*i,b=a+1; edge(0,a);edge(a,b);edge(b,1);}
  vector<uint32_t> pow3(n+1,1);
  for(int i=1;i<=n;i++) pow3[i]=pow3[i-1]*3;
  const uint32_t N=pow3[n];
  vector<uint32_t> succ(N);
  vector<uint8_t> mark(N,0), period(N,0), depth(N,0);
  for(uint32_t x=0;x<N;x++) {
    int state[16];
    for(int i=0;i<n;i++) state[i]=(x/pow3[i])%3;
    uint32_t y=0;
    for(int i=0;i<n;i++) {
      int val=state[i] ? (state[i]+1)%3 : 0;
      if(state[i]==0) for(int j:neighbors[i]) if(state[j]==1) {val=1;break;}
      y+=val*pow3[i];
    }
    succ[x]=y;
  }
  map<int,uint64_t> cycle_count, basin_count;
  uint64_t max_t=0;
  vector<uint32_t> chain;
  chain.reserve(256);
  for(uint32_t st=0;st<N;st++) {
    if(mark[st]!=0)continue;
    uint32_t x=st; chain.clear();
    while(mark[x]==0) {mark[x]=1;chain.push_back(x);x=succ[x];}
    if(mark[x]==1) {
      uint32_t p=x;int cyc_len=0;
      do {cyc_len++;p=succ[p];} while(p!=x);
      p=x;
      do {mark[p]=2;period[p]=cyc_len;depth[p]=0;p=succ[p];} while(p!=x);
      cycle_count[cyc_len]++;
    }
    for(auto it=chain.rbegin();it!=chain.rend();++it) {
      uint32_t v=*it;
      if(mark[v]!=2) {
        uint32_t nxt=succ[v];
        assert(mark[nxt]==2);
        mark[v]=2;period[v]=period[nxt];
        depth[v]=depth[nxt]+1;
      }
      basin_count[period[v]]++;
      if(depth[v]>max_t)max_t=depth[v];
    }
  }
  uint64_t p3=k>=1 ? [] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=3;return r;}(k):0;
  uint64_t p2=[] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=2;return r;}(k);
  uint64_t p6=[] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=6;return r;}(k);
  uint64_t p7=[] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=7;return r;}(k);
  uint64_t p8=[] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=8;return r;}(k);
  uint64_t p9=[] (int k) {uint64_t r=1;for(int i=0;i<k;i++)r*=9;return r;}(k);
  uint64_t q3=p3-2*p2+1;
  uint64_t q4=2*p2-2;
  assert(cycle_count[1]==1 && cycle_count[3]==q3 && cycle_count[4]==q4);
  assert(cycle_count.size()==3);
  assert(basin_count[1]==3*p7+6*p6);
  assert(basin_count[3]==3*(p9-2*p8+p7));
  assert(basin_count[4]==6*(p9+p8-p7-p6));
  assert(max_t==(k==1?4:5));
  cout<<"k="<<k<<" states="<<N<<" Q1="<<cycle_count[1]<<" Q3="<<cycle_count[3]
      <<" Q4="<<cycle_count[4]<<" B1="<<basin_count[1]<<" B3="<<basin_count[3]
      <<" B4="<<basin_count[4]<<" T="<<max_t<<" PASS\n";
 }
}
