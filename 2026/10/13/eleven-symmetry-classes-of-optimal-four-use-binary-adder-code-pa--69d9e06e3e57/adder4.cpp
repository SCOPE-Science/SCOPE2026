#include <bits/stdc++.h>
using namespace std;
int key[16][16],full=1<<16;int best=0;map<pair<int,int>,long long> combos; vector<pair<int,int>> witnesses;
int mis(const int conf[16],int mask){
 if(!mask)return 0;
 int v=__builtin_ctz((unsigned)mask);
 int without=mask & ~(1<<v);
 return max(mis(conf,without),1+mis(conf,without &~conf[v]));
}
int main(){
 for(int a=0;a<16;a++)for(int b=0;b<16;b++){int k=0,scale=1;for(int i=0;i<4;i++){int t=((a>>i)&1)-((b>>i)&1);k+=(t+1)*scale;scale*=3;}key[a][b]=k;}
 for(int A=1;A<65536;A+=2){
  bitset<81> diff;for(int a=0;a<16;a++)if(A>>a&1)for(int b=0;b<16;b++)if((A>>b&1)&&a!=b)diff.set(key[a][b]);
  int conflict[16]={};for(int a=0;a<16;a++)for(int b=0;b<16;b++)if(a!=b&&diff[key[a][b]])conflict[a]|=1<<b;
  int m=mis(conflict,65535),p=__builtin_popcount((unsigned)A)*m;
  if(p>best){best=p;witnesses.clear();cerr<<"best "<<best<<" A "<<A<<" size "<<__builtin_popcount((unsigned)A)<<" B "<<m<<"\n";}
  if(p==best)witnesses.push_back({A,m});
  combos[{__builtin_popcount((unsigned)A),m}]++;
 }
 cout<<"MAX "<<best<<" witnesses_A_with0 "<<witnesses.size()<<"\n";for(auto &[ab,bmax]:witnesses)cout<<ab<<" "<<__builtin_popcount((unsigned)ab)<<" "<<bmax<<"\n";
}
