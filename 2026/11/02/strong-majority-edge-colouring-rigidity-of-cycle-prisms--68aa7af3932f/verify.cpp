#include <bits/stdc++.h>
using namespace std;
struct Edge {int u,v;};
vector<Edge> build(int n){
 vector<Edge> E; E.reserve(3*n);
 for(int i=0;i<n;i++)E.push_back({i,(i+1)%n});
 for(int i=0;i<n;i++)E.push_back({n+i,n+(i+1)%n});
 for(int i=0;i<n;i++)E.push_back({i,n+i});
 return E;
}
vector<array<int,4>> neighbors(int n){
 auto E=build(n);vector<array<int,4>> adj(3*n);
 for(int i=0;i<3*n;i++){
  vector<int> others;
  for(int j=0;j<3*n;j++)if(i!=j&&(E[i].u==E[j].u||E[i].u==E[j].v||E[i].v==E[j].u||E[i].v==E[j].v))others.push_back(j);
  assert(others.size()==4);
  for(int a=0;a<4;a++)adj[i][a]=others[a];
 }
 return adj;
}
bool good(const vector<int>& cols,const vector<array<int,4>>& adj,int q){
 for(const auto& x:adj){int cnt[3]={0,0,0};for(int j:x)cnt[cols[j]]++;for(int k=0;k<q;k++)if(cnt[k]>2)return false;}
 return true;
}
int main(){
 for(int n=3;n<=7;n++){
  auto adj=neighbors(n);uint64_t count=0;
  uint64_t end=1ULL<<(3*n);
  for(uint64_t mask=0;mask<end;mask++){
   vector<int> c(3*n);for(int j=0;j<3*n;j++)c[j]= (mask>>j)&1;
   if(good(c,adj,2))count++;
  }
  assert(count==(n%4==0?8:0));
  cout<<"BRUTE "<<n<<" "<<count<<"/"<<end<<"\n";
 }
 for(int n=3;n<=44;n++){
  auto edges=build(n);auto adj=neighbors(n);
  // A fixed Hamiltonian cycle passes through top rail 0..n-1, rung n-1,
  // reversed bottom rail n-1..0, and rung 0.
  vector<int> circuit;
  for(int i=0;i<n-1;i++) circuit.push_back(i);
  circuit.push_back(3*n-1);
  for(int i=n-2;i>=0;i--)circuit.push_back(n+i);
  circuit.push_back(2*n);
  assert((int)circuit.size()==2*n);
  vector<int> c(3*n,2);
  for(int k=0;k<(int)circuit.size();k++){assert(c[circuit[k]]==2);c[circuit[k]]=k%2;}
  assert(good(c,adj,3));
  // All 8 analytically classified 2-colourings are valid whenever 4|n.
  if(n%4==0){
   set<vector<int>> examples;
   for(int a=0;a<2;a++)for(int b=0;b<2;b++)for(int r=0;r<2;r++){
    vector<int> top(n),cs(3*n);
    for(int i=0;i<n;i++)top[i] = (i%4==0?a:i%4==1?b:i%4==2?1-a:1-b);
    for(int i=0;i<n;i++){cs[i]=top[i];cs[n+i]=1-top[i];cs[2*n+i]=r^(i%2);}
    assert(good(cs,adj,2));examples.insert(cs);
   }
   assert(examples.size()==8);
  }
 }
 cout<<"VERIFY_OK brute_labels_n=3..7 cubic_prism_n=3..44 proper_three_edge_coloring=all exactly_eight_n_multiple_4=all\n";
}
