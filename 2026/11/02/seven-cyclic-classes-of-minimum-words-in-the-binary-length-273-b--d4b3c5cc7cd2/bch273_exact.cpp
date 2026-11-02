#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
constexpr uint32_t POLY=0x10ff, TOP=0x1000, N=273;
uint32_t mul(uint32_t a,uint32_t b){uint32_t z=0;while(b){if(b&1)z^=a;b>>=1;a<<=1;if(a&TOP)a^=POLY;}return z;}
uint32_t power(uint32_t a,unsigned k){uint32_t z=1;while(k){if(k&1)z=mul(z,a);a=mul(a,a);k>>=1;}return z;}
using Five=array<int,5>;
Five normalize(Five a){Five best={N,N,N,N,N};for(int r=0;r<(int)N;r++){Five b=a;for(int &j:b)j=(j+r)%N;sort(b.begin(),b.end());if(b<best)best=b;}return best;}
int main(){
 const uint32_t generator=11;
 if(power(generator,4095)!=1)throw runtime_error("order");
 for(int p:{3,5,7,13})if(power(generator,4095/p)==1)throw runtime_error("not primitive");
 uint32_t beta=power(generator,15);
 vector<uint32_t> h(N),cubes(N);h[0]=1;
 for(int i=1;i<(int)N;i++)h[i]=mul(h[i-1],beta);
 if(mul(h[N-1],beta)!=1 || set<uint32_t>(h.begin(),h.end()).size()!=N)throw runtime_error("not order 273");
 for(int i=0;i<(int)N;i++)cubes[i]=power(h[i],3);
 map<pair<uint32_t,uint32_t>,vector<pair<int,int>>> pairs;
 for(int i=1;i<(int)N;i++)for(int j=i+1;j<(int)N;j++)pairs[{h[i]^h[j],cubes[i]^cubes[j]}].push_back({i,j});
 if(pairs.size()!=36856)throw runtime_error("pair collision");
 int matches=0;set<Five> anchored;
 for(const auto &[key, first]:pairs){
   const auto it=pairs.find({key.first^1U,key.second^1U});
   if(it==pairs.end())continue;
   for(const auto &[i,j]:first)for(const auto &[k,l]:it->second){
     if(i==k||i==l||j==k||j==l)continue;
     matches++;
     Five a={0,i,j,k,l};sort(a.begin(),a.end());
     uint32_t x=0,y=0;for(int v:a){x^=h[v];y^=cubes[v];}
     if(x||y)throw runtime_error("wrong zero");
     anchored.insert(a);
   }
 }
 if(matches!=210||anchored.size()!=35)throw runtime_error("anchored mismatch");
 set<Five> reps;for(Five a:anchored)reps.insert(normalize(a));
 const set<Five> expected={{{0,1,64,97,202},{0,2,128,131,194},{0,4,115,256,262},{0,8,230,239,251},{0,13,78,104,234},{0,16,187,205,229},{0,32,101,137,185}}};
 if(reps!=expected)throw runtime_error("representative mismatch");
 set<Five> all;
 for(Five a:reps)for(int r=0;r<(int)N;r++){for(int &v:a)v=(v+r)%N;sort(a.begin(),a.end());all.insert(a);for(int &v:a)v=(v-r+N)%N;sort(a.begin(),a.end());}
 if(all.size()!=1911)throw runtime_error("orbit size mismatch");
 for(Five a:all){uint32_t x=0,y=0;for(int i:a){x^=h[i];y^=cubes[i];}if(x||y)throw runtime_error("incorrect orbit");}
 cout<<"BCH273_CPP_OK GF=4096 PAIRS=36856 MATCHES=210 ANCHORED=35 ORBITS=7 WORDS=1911\n";
 for(Five a:reps){for(int v:a)cout<<v<<' ';cout<<'\n';}
}
