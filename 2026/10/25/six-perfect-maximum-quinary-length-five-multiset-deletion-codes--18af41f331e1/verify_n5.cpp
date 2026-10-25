#include <bits/stdc++.h>
using namespace std;using U=unsigned __int128;
constexpr int Q=5,N=5,T=26;vector<array<int,Q>> V;U nearH[126];U bit(int i){return (U)1<<i;}
int low(U x){return x<((U)1<<64)?__builtin_ctzll((unsigned long long)x):64+__builtin_ctzll((unsigned long long)(x>>64));}
int pc(U x){return __builtin_popcountll((unsigned long long)x)+__builtin_popcountll((unsigned long long)(x>>64));}
unsigned long long nodes=0,leaves=0;vector<int> cur;vector<vector<int>> sols;
void search(U cand){
 nodes++;
 if((int)cur.size()==T){sols.push_back(cur);return;}
 if((int)cur.size()+pc(cand)<T)return;
 vector<int> order,col;
 U rem=cand;int color=0;
 while(rem){
  color++;U free=rem;
  while(free){int v=low(free);U bv=bit(v);order.push_back(v);col.push_back(color);rem&=~bv;free&=~bv;free&=~nearH[v];}
 }
 for(int i=(int)order.size()-1;i>=0;i--){
  if((int)cur.size()+col[i]<T) return;
  int v=order[i];cur.push_back(v);search(cand&nearH[v]);cur.pop_back();cand&=~bit(v);
 }
}
void gen(int j,int rem,array<int,Q> a){if(j==Q-1){a[j]=rem;V.push_back(a);return;}for(int z=0;z<=rem;z++){a[j]=z;gen(j+1,rem-z,a);}}
int main(){array<int,Q> a={};gen(0,N,a);if(V.size()!=126)return 2;for(int i=0;i<126;i++)for(int j=0;j<126;j++){if(i==j)continue;int d=0;for(int k=0;k<Q;k++)d+=abs(V[i][k]-V[j][k]);if(d!=2)nearH[i]|=bit(j);}
 U all=((U)1<<126)-1;auto t=chrono::steady_clock::now();search(all);double secs=chrono::duration<double>(chrono::steady_clock::now()-t).count();cout<<"V="<<V.size()<<" nodes="<<nodes<<" solutions="<<sols.size()<<" secs="<<secs<<"\n";for(auto &s:sols){sort(s.begin(),s.end());for(int v:s)cout<<v<<',';cout<<'\n';}return 0;
}
