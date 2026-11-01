// Independent direct vertex-neighbor XOR enumeration for one-corner punctured rook graphs.
#include <cstdint>
#include <map>
#include <cassert>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;
uint32_t step(uint32_t x,const vector<uint32_t>& masks){
 uint32_t y=0;
 for(size_t i=0;i<masks.size();i++) y|=uint32_t(__builtin_parity(x&masks[i]))<<i;
 return y;
}
int main(){
 uint64_t total=0; int cases=0;
 for(int a=2;a<=8;a++) for(int b=2;b<=8;b++){
  int E=a*b-1;if(E>17)continue;
  vector<pair<int,int>> v;
  for(int i=0;i<a;i++)for(int j=0;j<b;j++)if(i!=a-1 || j!=b-1)v.emplace_back(i,j);
  vector<uint32_t> masks(E,0);
  for(int i=0;i<E;i++)for(int j=0;j<E;j++)
    if((v[i].first==v[j].first)!=(v[i].second==v[j].second))masks[i]|=1u<<j;
  map<pair<int,int>,uint64_t> got,want;
  for(uint32_t x=0;x<(1u<<E);x++){
   uint32_t path[9];path[0]=x;
   for(int t=1;t<9;t++)path[t]=step(path[t-1],masks);
   int entry=-1,period=-1;
   for(int t=0;t<=5;t++){
    if(path[t]==path[t+1]){entry=t;period=1;break;}
    if(path[t]==path[t+2]){entry=t;period=2;break;}
   }
   assert(entry>=0);
   got[{period,entry}]++;
  }
  uint64_t Q=1ULL<<E;
  if((a&1) && (b&1)){
   int d=a+b-2;
   uint64_t layers[2]={1ULL<<d,Q-(1ULL<<d)};
   for(int t=0;t<=1;t++){
    want[{1,t}]=layers[t]/2;
    want[{2,t}]=layers[t]/2;
   }
  }else if(!(a&1)&&!(b&1)){
   int r=a+b-2;
   want[{1,0}]=1;want[{1,1}]=(1ULL<<(E-r))-1;
   want[{1,2}]=(1ULL<<(E-1))-(1ULL<<(E-r));
   want[{1,3}]=Q-(1ULL<<(E-1));
  }else{
   int s=(a%2==0)?a:b,o=(a%2==1)?a:b;
   int d=s-2;int r[6]={E,o+s-1,s+1,s,s-1,s-2};
   uint64_t prev=1ULL<<d;
   want[{1,0}]=prev;
   for(int t=1;t<=5;t++){
    uint64_t cum=1ULL<<(E-r[t]+d);
    want[{1,t}]=cum-prev;prev=cum;
   }
  }
  for(auto [k,n]:got)assert(want[k]==n);
  for(auto [k,n]:want)assert(got[k]==n);
  total+=(1u<<E);cases++;
 }
 cout<<"PASS punctured-rook independent exhaustive direct C++: "<<cases<<" graph sizes, "<<total<<" labelled binary states\n";
}
