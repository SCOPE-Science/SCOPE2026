// Independent construction from cyclic binary matchings, with actual graph checks.
// The two exceptional matching masks are built from alternating rim edges.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct Check {
 int n; vector<pair<int,int>> edges; map<pair<int,int>,int> eid;
 Check(int N):n(N) {
  auto add=[&](int a,int b){if(a>b)swap(a,b);if(!eid.count({a,b})){int i=edges.size();eid[{a,b}]=i;edges.push_back({a,b});}};
  for(int j=0;j<n;j++)add(j,j+n);
  for(int j=0;j<n-1;j++){add(j,j+1);add(j+n,j+n+1);}
  add(n-1,n);add(2*n-1,0);
 }
 U bit(int a,int b){if(a>b)swap(a,b);auto it=eid.find({a,b});if(it==eid.end())throw runtime_error("missing edge");return U(1)<<it->second;}
 vector<U> states() {
  vector<U> v;
  for(int z=0;z<(1<<n);z++){
   if((z&(z<<1))||(z&1 && z&(1<<(n-1))))continue;
   U M=0;
   for(int i=0;i<n;i++)if(z>>i&1){
    int j=(i+1)%n;
    if(j==0)M|=bit(n-1,n)|bit(2*n-1,0);
    else M|=bit(i,j)|bit(n+i,n+j);
   }
   for(int i=0;i<n;i++)if(!(z>>i&1)&&!(z>>((i+n-1)%n)&1))M|=bit(i,n+i);
   v.push_back(M);
  }
  if(n%2){
   U a=0,b=0;
   for(int i=0;i<n;i++){a|=bit(2*i,2*i+1); b|=bit((2*i+1)%(2*n),(2*i+2)%(2*n));}
   v.push_back(a);v.push_back(b);
  }
  set<U> uniq(v.begin(),v.end());if(uniq.size()!=v.size())throw runtime_error("duplicates");
  for(U M:v){
   vector<int> d(2*n);
   for(int k=0;k<(int)edges.size();k++)if(M>>k&1){auto [a,b]=edges[k];d[a]++;d[b]++;}
   for(int q:d)if(q!=1)throw runtime_error("not perfect");
  }
  return v;
 }
 // Return the length if the full symmetric difference is one alternating cycle; else 0.
 int fliplen(U M,U N){
  U x=M^N;if(!x)return 0;
  vector<vector<int>> adj(2*n);int e=0;
  for(int i=0;i<(int)edges.size();i++)if(x>>i&1){auto [a,b]=edges[i];adj[a].push_back(b);adj[b].push_back(a);e++;}
  int st=-1;
  for(int i=0;i<2*n;i++){
   if(adj[i].size()!=0 && adj[i].size()!=2)throw runtime_error("bad symmetric difference");
   if(adj[i].size())st=i;
  }
  vector<char> seen(2*n,0);queue<int> q;q.push(st);seen[st]=1;int reached=0;
  while(!q.empty()){int a=q.front();q.pop();reached++;for(int b:adj[a])if(!seen[b]){seen[b]=1;q.push(b);}}
  return reached==e?e:0;
 }
 vector<int> ccs(vector<vector<int>>& adj){
  vector<char> seen(adj.size()); vector<int> sizes;
  for(int i=0;i<(int)adj.size();i++)if(!seen[i]){
   int cnt=0;queue<int> q;q.push(i);seen[i]=1;
   while(!q.empty()){int a=q.front();q.pop();cnt++;for(int b:adj[a])if(!seen[b]){seen[b]=1;q.push(b);}}
   sizes.push_back(cnt);
  }
  sort(sizes.begin(),sizes.end());return sizes;
 }
 void run(){
  auto v=states();int N=v.size();
  int lucas=0;for(int x=0;x<(1<<n);x++)if(!(x&(x<<1))&&!(x&1&&x&(1<<(n-1))))lucas++;
  if(N!=lucas+2*(n%2))throw runtime_error("count wrong");
  vector<vector<int>> four(N), upto(N);
  map<int,int> degrees;
  long long e4=0;int smallest=INT_MAX, neighbors_at_threshold=0;
  int a=(n%2?N-2:-1),b=N-1;
  for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
   int l=fliplen(v[i],v[j]);
   if(!l)continue;
   if(l==4){four[i].push_back(j);four[j].push_back(i);e4++;}
   if(l<=(n%2?n+1:4)){upto[i].push_back(j);upto[j].push_back(i);}
   if(n%2&&(i==a||i==b||j==a||j==b)){smallest=min(smallest,l);if(l==n+1)neighbors_at_threshold++;}
  }
  long long f0=0,f1=1;
  for(int i=0;i<n-1;i++){long long q=f0+f1;f0=f1;f1=q;}
  if(e4!=n*f0)throw runtime_error("edge formula");
  auto cc4=ccs(four), cct=ccs(upto);
  if(cct!=vector<int>{N})throw runtime_error("threshold not connected");
  if(cc4!=(n%2?vector<int>{1,1,lucas}:vector<int>{lucas}))throw runtime_error("4-flip components");
  if(n%2 && (smallest!=n+1||neighbors_at_threshold!=2*n))throw runtime_error("odd barrier");
  for(auto &z:four)degrees[z.size()]++;
  // Generate expected degrees separately directly from allowed cyclic strings.
  map<int,int> pred;
  for(int z=0;z<(1<<n);z++){
   if(z&(z<<1)|| (z&1&&z&(1<<(n-1))))continue;
   int degree=0;
   for(int i=0;i<n;i++){
    int y=z^(1<<i);
    if(!(y&(y<<1))&& !(y&1&&y&(1<<(n-1))))degree++;
   }
   pred[degree]++;
  }
  if(n%2)pred[0]+=2;
  if(pred!=degrees)throw runtime_error("degree law");
  cout<<"ALT_PASS "<<n<<" states="<<N<<" edges="<<e4<<" components="<<cc4.size()<<" min_odd_cycle="<<(n%2?smallest:0)<<"\n";
 }
};
int main(){for(int n=4;n<=12;n++)Check(n).run();cout<<"ALT_ALL_PASS\n";}
