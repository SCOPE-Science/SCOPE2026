// Independent Johnson-pair checker: masks, direct neighbor generation, and BFS.
// C++17; compile: g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main(){
 for(int n=3;n<=8;n++){
  vector<int> pairs;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)pairs.push_back((1<<a)|(1<<b));
  int q=(int)pairs.size(), N=q*(q-1);
  vector<pair<int,int>> states;
  vector<vector<int>> pos(q,vector<int>(q,-1));
  for(int a=0;a<q;a++)for(int b=0;b<q;b++)if(a!=b){
   pos[a][b]=(int)states.size();states.emplace_back(a,b);
  }
  assert((int)states.size()==N);
  vector<vector<int>> adj(N);
  for(int s=0;s<N;s++){
   auto [a,b]=states[s];
   for(int i=0;i<q;i++){
    if(i!=b && __builtin_popcount((unsigned)(pairs[i]&pairs[a]))==1)
     adj[s].push_back(pos[i][b]);
    if(i!=a && __builtin_popcount((unsigned)(pairs[i]&pairs[b]))==1)
     adj[s].push_back(pos[a][i]);
   }
   sort(adj[s].begin(),adj[s].end());
   assert(unique(adj[s].begin(),adj[s].end())==adj[s].end());
   int common=__builtin_popcount((unsigned)(pairs[a]&pairs[b]));
   assert((int)adj[s].size()== (common==1 ?4*n-10:4*n-8));
  }
  long long distance_sum=0;
  long long hist[5]={0,0,0,0,0};
  int diameter=0;
  for(int s=0;s<N;s++){
   vector<int> ds(N,-1);
   queue<int> qu;ds[s]=0;qu.push(s);
   while(!qu.empty()){
    int u=qu.front();qu.pop();
    for(int v:adj[u])if(ds[v]<0){ds[v]=ds[u]+1;qu.push(v);}
   }
   auto [a,b]=states[s];
   for(int t=0;t<N;t++){
    assert(ds[t]>=0);
    auto [c,d]=states[t];
    int lower=(2-__builtin_popcount((unsigned)(pairs[a]&pairs[c])))+
              (2-__builtin_popcount((unsigned)(pairs[b]&pairs[d])));
    int penalty=(a==d && b==c && __builtin_popcount((unsigned)(pairs[a]&pairs[b]))==1);
    if(ds[t]!=lower+penalty){cerr<<"Mismatch n="<<n<<" from="<<s<<" to="<<t<<endl;return 1;}
    distance_sum+=ds[t];
    assert(ds[t]<=4);hist[ds[t]]++;
    diameter=max(diameter,ds[t]);
   }
  }
  long long Q=q;
  long long exact=Q*((Q-1)*(Q-1)*(n-1)*(n-2)+(n-2));
  long long k=2*(n-2),r=Q-1-k;
  long long target[5]={Q*(Q-1),2*Q*k*(Q-2),Q*(Q-2)*(k*k+2*r),
                        Q*k*(2*(Q-2)*r+1),Q*r*((Q-2)*r+1)};
  for(int d=0;d<5;d++)assert(hist[d]==target[d]);
  assert(distance_sum==2*exact);
  assert(diameter==(n==3?3:4));
  cout<<"ALTERNATIVE_PASS n="<<n<<" states="<<N<<" wiener="<<exact<<" diameter="<<diameter<<"\n";
 }
 cout<<"ALTERNATIVE_CROWN_CERTIFICATE_OK\n";
}
