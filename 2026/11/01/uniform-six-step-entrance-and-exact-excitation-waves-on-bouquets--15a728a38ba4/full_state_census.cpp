#include <bits/stdc++.h>
using namespace std;
int main(){for(int k=1;k<=4;k++){
 int n=3*k+1, N=1; for(int i=0;i<n;i++)N*=3;
 vector<int> power(n);power[0]=1; for(int i=1;i<n;i++)power[i]=3*power[i-1];
 vector<vector<int>> ad(n);
 for(int p=0;p<k;p++){int a=3*p+1,b=a+1,c=a+2;for(auto [u,v]:vector<pair<int,int>>{{0,a},{a,b},{b,c},{c,0}}){ad[u].push_back(v);ad[v].push_back(u);}}
 vector<int> nxt(N);
 for(int s=0;s<N;s++){
  int digits[20];for(int v=0;v<n;v++)digits[v]=(s/power[v])%3;
  int t=0;
  for(int v=0;v<n;v++){
   int y=0;
   if(digits[v]==1)y=2;
   else if(digits[v]==0){for(int w:ad[v])if(digits[w]==1){y=1;break;}}
   t+=y*power[v];
  }
  nxt[s]=t;
 }
 vector<int> indeg(N),trans(N,-1),period(N,-1);
 for(int s=0;s<N;s++)indeg[nxt[s]]++;
 queue<int> q;for(int s=0;s<N;s++)if(!indeg[s])q.push(s);
 vector<int> topo;topo.reserve(N);
 while(!q.empty()){int v=q.front();q.pop();topo.push_back(v);if(--indeg[nxt[v]]==0)q.push(nxt[v]);}
 map<int,int> pcount;
 for(int s=0;s<N;s++)if(indeg[s]>0 && period[s]<0){
   int v=s,L=0;do{v=nxt[v];L++;}while(v!=s);
   v=s;do{period[v]=L;trans[v]=0;v=nxt[v];}while(v!=s);
   pcount[L]+=L;
 }
 int T=0;map<int,long long> basin;
 for(auto it=topo.rbegin();it!=topo.rend();++it){int v=*it;period[v]=period[nxt[v]];trans[v]=1+trans[nxt[v]];T=max(T,trans[v]);}
 for(int s=0;s<N;s++)basin[period[s]]++;
 cout<<"k="<<k<<" N="<<N<<" maxT="<<T<<" cycles:";for(auto [l,c]:pcount)cout<<" "<<l<<":"<<c/l;cout<<" basins:";for(auto [l,c]:basin)cout<<" "<<l<<":"<<c;cout<<"\n";
}}
