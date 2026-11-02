// Independent base-eight enumeration and direct state-set breadth-first search.
// Compile: c++ -std=c++17 -O2 crosscheck.cpp -o crosscheck && ./crosscheck
#include <iostream>
#include <array>
#include <algorithm>
#include <map>
#include <vector>
#include <cassert>
using namespace std;
int main(){
 const int n=8,all=(1<<n)-1;
 long long accepted=0,nosync=0,compatible=0;map<int,int> hist;
 for(int code=0;code<(1<<24);code++){
  int b[n],k=code,mask=0;
  for(int i=0;i<n;i++){b[i]=k&7;k>>=3;mask|=1<<b[i];}
  if(mask!=254)continue;accepted++;
  auto permquot=[&](int d){int outs[8],used=0;fill(outs,outs+d,-1);
   for(int i=0;i<n;i++){int j=b[i]%d;if(outs[i%d]>=0&&outs[i%d]!=j)return false;outs[i%d]=j;}
   for(int r=0;r<d;r++)used|=1<<outs[r];return __builtin_popcount((unsigned)used)==d;};
  bool invariant=permquot(2)||permquot(4);compatible+=invariant;
  // Transition obtained by applying symbols to each member of the set;
  // unlike verify.cpp this does not use subset-transition precomputation.
  auto action=[&](int s,bool letter){int t=0;
   for(int j=0;j<n;j++)if(s&(1<<j))t|=1<<(letter?b[j]:(j+1)%n);
   return t;};
  array<int,256> dist;dist.fill(-1);
  int Q[256],head=0,tail=1;Q[0]=all;dist[all]=0;int threshold=0;
  while(head<tail){int s=Q[head++];
   if((s&(s-1))==0){threshold=dist[s];break;}
   for(bool letter:{false,true}){int t=action(s,letter);
    if(dist[t]<0){dist[t]=dist[s]+1;Q[tail++]=t;}}
  }
  hist[threshold]++;nosync+=(threshold==0);
  if((threshold==0)!=invariant){cerr<<"MISCLASSIFICATION "<<code<<"\n";return 2;}
 }
 assert(accepted==141120&&nosync==1856&&compatible==1856);
 assert(hist.at(49)==1&&hist.at(44)==1&&hist.at(43)==1);
 cout<<"threshold,classes\n";for(auto [k,v]:hist)cout<<k<<","<<v<<"\n";
 cout<<"CROSSCHECK_OK\n";
}
