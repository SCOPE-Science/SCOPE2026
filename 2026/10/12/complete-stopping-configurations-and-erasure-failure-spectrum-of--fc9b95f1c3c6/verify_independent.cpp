// Direct exact enumeration of projective-plane incidence and erasure peeling.
#include <array>
#include <cassert>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
struct V {int x,y,z;};
V canon(V v){int a = v.x ? v.x : (v.y ? v.y : v.z); int k = a == 1 ? 1 : 2; return {v.x*k%3,v.y*k%3,v.z*k%3};}
bool equalv(V a,V b){return a.x==b.x&&a.y==b.y&&a.z==b.z;}
int pop(int x){return __builtin_popcount((unsigned)x);}
int main(){
 vector<V> p;
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  if(!x&&!y&&!z)continue; V v=canon({x,y,z});
  if(find_if(p.begin(),p.end(),[&](V w){return equalv(v,w);})==p.end())p.push_back(v);
 }
 assert(p.size()==13);
 array<int,13> rows{};
 for(int i=0;i<13;i++)for(int j=0;j<13;j++)
  if((p[i].x*p[j].x+p[i].y*p[j].y+p[i].z*p[j].z)%3==0)rows[i]|=1<<j;
 for(auto a:rows)assert(pop(a)==4);
 array<int,14> stopping{},failure{};
 int ps=0,pf=0;
 for(int mask=0;mask<(1<<13);mask++){
  bool stop=true;
  for(auto a:rows)if(pop(a&mask)==1)stop=false;
  if(stop){stopping[pop(mask)]++;ps++;}
  int rem=mask;
  while(rem){int one=0;
   for(auto a:rows){int z=rem&a;if(pop(z)==1){one=z;break;}}
   if(!one)break;rem^=one;
  }
  if(rem){failure[pop(mask)]++;pf++;}
 }
 assert(ps==769&&pf==3004);
 const int es[14]={1,0,0,0,0,0,78,0,117,247,234,78,13,1};
 const int ef[14]={0,0,0,0,0,0,78,546,1287,715,286,78,13,1};
 for(int j=0;j<14;j++)assert(stopping[j]==es[j]&&failure[j]==ef[j]);
 printf("VERIFY_CPP_OK all_8192_masks stopping=769 minimum_6=78 failure=3004\n");
 return 0;
}
