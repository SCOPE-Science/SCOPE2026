#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <map>
#include <ctime>
#include "heawood_aut.h"
using namespace std;
int colors[14],allowed[7], K=4; long long tot=0,good=0, nontriv=0;
unordered_set<unsigned> canonical;
unsigned canon(const int *c){ int m[4]={-1,-1,-1,-1},next=0;unsigned key=0;for(int i=0;i<14;i++){if(m[c[i]]<0)m[c[i]]=next++;key|=(m[c[i]]<<(2*i));}return key;}
void dfs(int j){
 if(j==7){
  tot++;
  bool sym=false;
  for(int p=1;p<336;p++){
   int i=0;for(;i<14;i++)if(colors[i]!=colors[perms[p][i]])break;
   if(i==14){sym=true;break;}
  }
  if(!sym){good++;canonical.insert(canon(colors));}
  else nontriv++;
  return;
 }
 int opts=allowed[j];while(opts){int c=__builtin_ctz((unsigned)opts);opts&=opts-1;colors[7+j]=c;dfs(j+1);}
}
int main(int argc,char**argv){if(argc>1)K=atoi(argv[1]);clock_t t=clock(); int maxpt=1;for(int i=0;i<7;i++)maxpt*=K;
 for(int mask=0;mask<maxpt;mask++){
  int v=mask;for(int i=0;i<7;i++){colors[i]=v%K;v/=K;}
  bool ok=true;
  for(int j=0;j<7;j++){
   allowed[j]=(1<<K)-1;
   for(int p:ln[j])allowed[j]&=~(1<<colors[p]);
   if(!allowed[j]){ok=false;break;}
  }
  if(ok)dfs(0);
 }
 cerr<<"k="<<K<<" proper="<<tot<<" nontriv="<<nontriv<<" distinguishing="<<good<<" canonical="<<canonical.size()<<" runtime="<<double(clock()-t)/CLOCKS_PER_SEC<<"\n";
 map<int,int> orbit_count; map<int,int> orb_sizes;
 while(!canonical.empty()){
  unsigned k=*canonical.begin();int c[14];for(int i=0;i<14;i++)c[i]=(k>>(2*i))&3;
  unordered_set<unsigned> orbit;
  for(int p=0;p<336;p++){int d[14];for(int i=0;i<14;i++)d[i]=c[perms[p][i]];orbit.insert(canon(d));}
  orbit_count[orbit.size()]++;
  for(unsigned x:orbit){if(!canonical.erase(x)){cerr<<"ERROR missing orbit element!\n";return 1;}}
 }
 for(auto [size,num]:orbit_count)cerr<<"orbit_size="<<size<<" multiplicity="<<num<<"\n";
 if(K==3 && (tot!=2106 || good!=0 || !orbit_count.empty()))return 2;
 if(K==4 && (tot!=719052 || good!=328608 || orbit_count!=map<int,int>{{56,1},{84,1},{112,1},{168,16},{336,32}}))return 3;
 if(K==3 || K==4)cerr<<"VERIFY_OK exact_palette_count="<<K<<"\n";
}
