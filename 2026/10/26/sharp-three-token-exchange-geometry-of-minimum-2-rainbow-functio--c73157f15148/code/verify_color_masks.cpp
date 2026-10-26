// Exhaustive validation for 2-rainbow domination on the 4-dimensional cube.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
 array<unsigned,16> neighbor{};
 for(int v=0;v<16;v++)for(int bit=0;bit<4;bit++)neighbor[v]|=1u<<(v^(1<<bit));
 array<vector<unsigned>,8> choices;
 for(unsigned s=0;s<(1u<<16);s++){
  int c=__builtin_popcount(s);
  if(c<=7)choices[c].push_back(s);
 }
 array<unsigned long long,8> counts{};
 vector<uint32_t> opt;
 for(int weight=0;weight<=7;weight++)for(int aweight=0;aweight<=weight;aweight++){
  for(unsigned a:choices[aweight])for(unsigned b:choices[weight-aweight]){
   unsigned empty=(~(a|b))&0xffffu;
   bool good=true;
   for(int v=0;v<16;v++)if((empty>>v)&1u){
     if(!(neighbor[v]&a)||!(neighbor[v]&b)){good=false;break;}
   }
   if(good){counts[weight]++;if(weight==7)opt.push_back(a|(b<<16));}
  }
 }
 const array<unsigned long long,8> expected={0,0,0,0,0,0,0,320};
 assert(counts==expected);
 assert(opt.size()==320);
 sort(opt.begin(),opt.end());
 assert(unique(opt.begin(),opt.end())==opt.end());
 array<unsigned long long,8> hist{};
 vector<vector<int>> g(opt.size());
 for(int i=0;i<(int)opt.size();i++)for(int j=i+1;j<(int)opt.size();j++){
  int d=__builtin_popcount(opt[i]^opt[j])/2;
  assert(d>=3&&d<=7);
  hist[d]++;
  if(d==3){g[i].push_back(j);g[j].push_back(i);}
 }
 assert(hist[3]==4320&&hist[4]==1440&&hist[5]==22080&&hist[6]==11520&&hist[7]==11680);
 for(auto &r:g)assert(r.size()==27);
 array<int,16> center{};
 for(int start=0;start<(int)opt.size();start++){
  vector<int> dist(opt.size(),-1);
  queue<int> Q;Q.push(start);dist[start]=0;
  while(!Q.empty()){
   int v=Q.front();Q.pop();
   for(int w:g[v])if(dist[w]<0){dist[w]=dist[v]+1;Q.push(w);}
  }
  int mx=0;
  for(int d:dist){assert(d>=0);mx=max(mx,d);}
  assert(mx==3);
 }
 array<int,3> overlap{};
 for(auto x:opt){
  unsigned a=x&0xffffu,b=x>>16;
  int j=__builtin_popcount(a&b);
  assert(j<=1);
  overlap[j]++;
  assert((__builtin_popcount(a)==3&&__builtin_popcount(b)==4)||
         (__builtin_popcount(a)==4&&__builtin_popcount(b)==3));
 }
 assert(overlap[0]==192&&overlap[1]==128);
 cout<<"feasible_by_weight_0_through_7 [0, 0, 0, 0, 0, 0, 0, 320]\n";
 cout<<"optimal_count 320; overlap_distribution 0:192 1:128\n";
 cout<<"token_distance_histogram 3:4320 4:1440 5:22080 6:11520 7:11680\n";
 cout<<"distance_three_graph vertices 320 edges 4320 degree 27 connected yes radius 3 diameter 3\n";
}
