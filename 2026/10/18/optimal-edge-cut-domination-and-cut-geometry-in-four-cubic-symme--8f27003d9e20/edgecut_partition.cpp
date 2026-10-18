// Independent cut-first exhaustive enumeration. No external libraries.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
struct Graph {int n; vector<pair<int,int>> e;};
Graph make(int typ){Graph a; if(typ==0){a.n=14;for(int j=0;j<7;j++) for(int d:{0,1,3})a.e.emplace_back((j+d)%7,7+j);} if(typ==1){a.n=16;for(int j=0;j<8;j++){a.e.emplace_back(j,(j+1)%8);a.e.emplace_back(8+j,8+(j+3)%8);a.e.emplace_back(j,8+j);}}if(typ==2){a.n=18; for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int slope=0;slope<3;slope++)a.e.emplace_back(x*3+y,9+slope*3+(y-slope*x+9)%3);}if(typ==3){a.n=20;for(int j=0;j<10;j++){a.e.emplace_back(j,(j+1)%10);a.e.emplace_back(10+j,10+(j+3)%10);a.e.emplace_back(j,10+j);}}return a;}
bool dom(const Graph&g,uint64_t f){unsigned covered=0;int i=0;for(auto[u,v]:g.e){if(f>>i&1) covered|=1U<<u | 1U<<v; i++;}for(auto[u,v]:g.e)if(!(covered>>u&1) && !(covered>>v&1))return false;return true;}
void combine(const Graph&g,const vector<int>&rest,int start,int r,uint64_t mask,set<uint64_t>&out){if(!r){if(dom(g,mask))out.insert(mask);return;}if((int)rest.size()-start<r)return;for(int i=start;i<=(int)rest.size()-r;i++)combine(g,rest,i+1,r-1,mask|(1ULL<<rest[i]),out);}
set<uint64_t> check(const Graph&g,int k){int m=g.e.size();set<uint64_t>result;int universe=(1<<g.n)-1; for(int subset=1;subset<universe;subset+=2){uint64_t delta=0;int cnt=0;for(int i=0;i<m;i++){auto[u,v]=g.e[i];if(((subset>>u)&1)!=((subset>>v)&1)){delta|=1ULL<<i;cnt++;}}if(cnt>k)continue;vector<int> other;for(int i=0;i<m;i++)if(!(delta>>i&1))other.push_back(i);combine(g,other,0,k-cnt,delta,result);}return result;}
int main(){string names[]={"Heawood","MobiusKantor","Pappus","Desargues"};int sizes[]={6,6,7,6};for(int t=0;t<4;t++){Graph g=make(t);auto sm=check(g,sizes[t]-1),ss=check(g,sizes[t]);cout<<names[t]<<" count_previous="<<sm.size()<<" count_min="<<ss.size()<<"\n";cout<<"SETS";for(auto bits:ss)cout<<" "<<bits;cout<<"\n";}}
