// Independent finite certificate: the generalized Petersen representation GP(10,3).
// Compile with: c++ -O2 -std=c++17 verify_gp.cpp -o verify_gp
#include <array>
#include <cassert>
#include <iostream>
using namespace std;
struct DSU {
  array<int,20> p, size;
  DSU() { for(int i=0;i<20;++i) p[i]=i,size[i]=1; }
  int root(int x) {while(x!=p[x]) x=p[x]=p[p[x]]; return x;}
  bool join(int a,int b) {a=root(a); b=root(b); if(a==b)return false;
    if(size[a]<size[b]) swap(a,b); p[b]=a; size[a]+=size[b];return true;}
};
int main() {
  array<array<int,2>,30> E{}; int t=0;
  for(int i=0;i<10;++i) {
    E[t++]={i,(i+1)%10}; E[t++]={i,i+10}; E[t++]={10+i,10+(i+3)%10};
  }
  assert(t==30);
  array<int,7> pass{};
  int independent=0, adjacent=0, checked=0;
  for(int mask=0;mask<(1<<20);++mask) {
    int k=__builtin_popcount((unsigned)mask);
    if(k>6)continue;
    ++checked;
    DSU D; bool forest=true;
    for(const auto& e:E) {
      if((mask&(1<<e[0]))||(mask&(1<<e[1])))continue;
      if(!D.join(e[0],e[1])) {forest=false;break;}
    }
    if(!forest)continue;
    ++pass[k];
    if(k==6) {
      int e_s=0;
      for(const auto& e:E) if((mask&(1<<e[0]))&&(mask&(1<<e[1])))++e_s;
      assert(e_s<=1);
      if(e_s==0)++independent;
      else ++adjacent;
    }
  }
  assert(checked==60460); // sum_{k=0}^{6} binom(20,k)
  for(int k=0;k<6;++k)assert(pass[k]==0);
  assert(pass[6]==2860 && independent==760 && adjacent==2100);
  cout<<"VERIFY_GP_OK candidates_0_through_6="<<checked
      <<" optimum_size=6 optimum_sets="<<pass[6]
      <<" edgeless_deletions="<<independent<<" one_edge_deletions="<<adjacent<<"\n";
}
