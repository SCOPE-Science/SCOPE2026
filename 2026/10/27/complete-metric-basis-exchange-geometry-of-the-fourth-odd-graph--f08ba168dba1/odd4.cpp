#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<int> triples; for(int m=0;m<(1<<7);m++) if(__builtin_popcount((unsigned)m)==3) triples.push_back(m);
 int N=triples.size();vector<vector<int>> adj(N),D(N,vector<int>(N,1000));
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)if(!(triples[i]&triples[j])){adj[i].push_back(j);adj[j].push_back(i);}
 for(int i=0;i<N;i++){queue<int>q;q.push(i);D[i][i]=0;while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(D[i][v]==1000){D[i][v]=D[i][u]+1;q.push(v);}}}
 cout<<"N="<<N<<" deg="<<adj[0].size()<<" diam="<<*max_element(D[0].begin(),D[0].end())<<endl;
 vector<array<uint64_t,10>> sep(N);
 int nPairs=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){for(int a=0;a<N;a++)if(D[a][i]!=D[a][j])sep[a][nPairs>>6]|=1ull<<(nPairs%64);nPairs++;}
 uint64_t full[10]; for(int t=0;t<10;t++)full[t]= t==9?((1ull<<(nPairs-9*64))-1):~0ull;
 vector<int> pick; uint64_t uncovered[10];copy(full,full+10,uncovered);
 long long count=0;
 function<void(int,int,int)>dfs=[&](int start,int left,int used){
  if(left==0){for(int t=0;t<10;t++)if(uncovered[t])return;count++; if(count<=5){cout<<"example:";for(auto a:pick)cout<<" "<<a;cout<<endl;}return;}
  for(int i=start;i<=N-left;i++){
   uint64_t old[10];memcpy(old,uncovered,sizeof old);for(int t=0;t<10;t++)uncovered[t]&=~sep[i][t];pick.push_back(i);dfs(i+1,left-1,used+1);pick.pop_back();memcpy(uncovered,old,sizeof old);
  }
 };
 for(int k=1;k<=9;k++){
  count=0;pick={0};for(int t=0;t<10;t++)uncovered[t]=full[t]&~sep[0][t];dfs(1,k-1,1);
  cout<<"k="<<k<<" sets_with_0="<<count<<" total="<<(count*35/k)<<endl;
  if(count)break;
 }
}
