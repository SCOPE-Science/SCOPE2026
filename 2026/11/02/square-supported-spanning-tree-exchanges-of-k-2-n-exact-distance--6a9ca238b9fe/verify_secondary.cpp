// Independently enumerate wildcard states and their local moves; verify graph distance statistics.
#include <bits/stdc++.h>
using namespace std;
int choose(int a,int b){if(b<0||b>a)return 0; int x=1;for(int i=1;i<=b;++i)x=x*(a-i+1)/i;return x;}
int main(){
 for(int n=2;n<=7;++n){
  vector<pair<int,vector<int>>> states;
  map<vector<int>,int> key;
  for(int j=0;j<n;++j) for(int m=0;m<(1<<(n-1));++m){
   vector<int> v(n);int z=0;
   for(int k=0;k<n;++k){if(k==j)v[k]=2;else v[k]=(m>>(z++))&1;}
   key[v]=states.size();states.push_back({j,v});
  }
  int N=states.size();vector<vector<int>> adj(N);
  for(int a=0;a<N;++a){
   auto v=states[a].second;
   for(int b=0;b<N;++b){
    if(a==b)continue;
    auto w=states[b].second;
    int starA=states[a].first,starB=states[b].first;
    bool possible=true;
    int flips=0;
    for(int k=0;k<n;++k){
     if(k==starA||k==starB)continue;
     if(v[k]!=w[k])++flips;
    }
    if(starA==starB){possible=(flips==1);}else{possible=(flips==0);}
    if(possible)adj[a].push_back(b);
   }
  }
  long long total=0;
  for(int a=0;a<N;++a){
   assert((int)adj[a].size()==3*(n-1));
   vector<int> dist(N,-1);queue<int> q;q.push(a);dist[a]=0;
   while(!q.empty()){int z=q.front();q.pop();for(int t:adj[z])if(dist[t]<0){dist[t]=dist[z]+1;q.push(t);}}
   for(int b=0;b<N;++b){
    auto v=states[a].second,w=states[b].second;
    int x=states[a].first,y=states[b].first;
    int expected=(x!=y);
    for(int k=0;k<n;++k)if(k!=x&&k!=y&&v[k]!=w[k])++expected;
    assert(dist[b]==expected);
    total+=dist[b];
   }
   for(int d=0;d<n;++d){int found=count(dist.begin(),dist.end(),d);int c=choose(n-1,d)+2*(n-1)*choose(n-2,d-1);assert(found==c);}
  }
  long long w=total/2;
  long long wanted=(long long)n*(n*n-1)*(1LL<<(2*n-4));assert(w==wanted);
  cout<<"SECONDARY_OK n="<<n<<" states="<<N<<" diameter="<<n-1<<" wiener="<<w<<"\n";
 }
 cout<<"SECONDARY_CERTIFICATE_OK\n";
}
