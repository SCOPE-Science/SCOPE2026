// Independent direct order-ideal and minimal-complement enumeration.
// Build: c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <map>
#include <utility>
using namespace std;
int main(){
 for(int n=3;n<=6;++n){
  vector<pair<int,int>> edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  int m=edges.size(), N=n+m;
  vector<uint32_t> all;
  for(uint32_t mask=0;mask<(1u<<N);++mask){
   bool valid=true;
   for(int k=0;k<m;++k){
    if(!(mask&(1u<<(n+k))))continue;
    auto [u,v]=edges[k];
    if(!(mask&(1u<<u)) || !(mask&(1u<<v))){valid=false;break;}
   }
   if(valid)all.push_back(mask);
  }
  unordered_map<uint32_t,int> ids;
  ids.reserve(all.size()*2);
  for(int i=0;i<(int)all.size();i++) ids.emplace(all[i],i);
  vector<int> succ(all.size());
  vector<char> incoming(all.size(),0), visited(all.size(),0);
  for(int i=0;i<(int)all.size();i++){
   uint32_t x=all[i],mincomp=0;
   for(int v=0;v<n;++v) if(!(x&(1u<<v))) mincomp|=1u<<v;
   for(int k=0;k<m;++k){
    if(x&(1u<<(n+k)))continue;
    auto [u,v]=edges[k];
    if((x&(1u<<u))&&(x&(1u<<v)))mincomp|=1u<<(n+k);
   }
   uint32_t ideal=mincomp;
   for(int k=0;k<m;++k)if(ideal&(1u<<(n+k))){
    auto [u,v]=edges[k];ideal|=(1u<<u)|(1u<<v);
   }
   auto it=ids.find(ideal);
   if(it==ids.end()){cerr<<"MISSING_IMAGE\n";return 2;}
   succ[i]=it->second;
   assert(!incoming[succ[i]]);incoming[succ[i]]=1;
  }
  map<int,int> count;
  for(int i=0;i<(int)all.size();i++)if(!visited[i]){
   int j=i,len=0;
   do{assert(!visited[j]);visited[j]=1;j=succ[j];++len;}while(j!=i);
   count[len]++;
  }
  if(n==3)assert((count==map<int,int>({{3,1},{5,3}})));
  if(n==4)assert((count==map<int,int>({{2,9},{3,1},{5,4},{8,9}})));
  if(n==5)assert((count==map<int,int>({{2,256},{3,1},{5,5},{6,45},{8,80}})));
  if(n==6)assert((count==map<int,int>({{2,11065},{3,1},{5,6},{6,1671},{8,985}})));
  cout<<"DIRECT_OK n="<<n<<" ideals="<<all.size()<<" cycles=";
  for(auto [p,c]:count)cout<<p<<":"<<c<<" ";
  cout<<"\n";
 }
 cout<<"INDEPENDENT_VERIFY_OK\n";
}
