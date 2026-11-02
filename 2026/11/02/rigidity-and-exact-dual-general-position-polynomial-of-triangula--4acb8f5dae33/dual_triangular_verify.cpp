// Standalone exhaustive distance-definition check for dual general-position sets in L(K_n).
// Compile: g++ -O3 -std=c++17 dual_triangular_verify.cpp -o dual_triangular_verify
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
using namespace std;
static bool is_star(uint32_t mask,const vector<array<int,2>>& e,int n){
  for(int a=0;a<n;++a){
    uint32_t S=0;
    for(int j=0;j<(int)e.size();++j) if(e[j][0]==a||e[j][1]==a) S|=uint32_t(1)<<j;
    if(mask==S) return true;
  }
  return false;
}
static bool is_triangle(uint32_t mask,const vector<array<int,2>>& e,int n){
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c){
    uint32_t S=0;
    for(int j=0;j<(int)e.size();++j){
      auto [u,v]=e[j];
      if((u==a||u==b||u==c)&&(v==a||v==b||v==c))S|=uint32_t(1)<<j;
    }
    if(mask==S)return true;
  }
  return false;
}
int main(){
 for(int n=3;n<=7;++n){
  vector<array<int,2>> edges;
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)edges.push_back({a,b});
  int N=(int)edges.size();
  vector<vector<int>> dist(N,vector<int>(N,1000));
  for(int i=0;i<N;++i)for(int j=0;j<N;++j){
   if(i==j)dist[i][j]=0;
   else if(edges[i][0]==edges[j][0]||edges[i][0]==edges[j][1]||edges[i][1]==edges[j][0]||edges[i][1]==edges[j][1])dist[i][j]=1;
  }
  for(int k=0;k<N;++k)for(int i=0;i<N;++i)for(int j=0;j<N;++j)
   dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
  vector<vector<uint32_t>> bad(N);
  for(int w=0;w<N;++w)for(int i=0;i<N;++i)for(int j=i+1;j<N;++j){
   if(w!=i&&w!=j&&dist[i][j]==dist[i][w]+dist[w][j])
    bad[w].push_back((uint32_t(1)<<i)|(uint32_t(1)<<j));
  }
  uint32_t total=uint32_t(1)<<N;
  uint64_t counts[22]={};
  for(uint32_t m=0;m<total;++m){
   bool ok=true;uint32_t sel=m;
   while(sel&&ok){
    int w=__builtin_ctz(sel);sel&=sel-1;
    for(uint32_t p:bad[w]){
      uint32_t v=m&p;
      if(v==0||v==p){ok=false;break;}
    }
   }
   if(!ok)continue;
   bool expected=m==0||(n==3)||(is_star(m,edges,n))||(n==4&&is_triangle(m,edges,n));
   if(!expected){cerr<<"Unexpected admissible configuration n="<<n<<" mask="<<m<<"\n";return 2;}
   counts[__builtin_popcount(m)]++;
  }
  uint64_t sum=0;for(auto x:counts)sum+=x;
  uint64_t expected=(n==3?8:(n==4?9:1+n));
  if(sum!=expected){cerr<<"Bad total n="<<n<<" got="<<sum<<" expected="<<expected<<"\n";return 3;}
  cout<<"n="<<n<<" V="<<N<<" candidate_subsets="<<total<<" admissible="<<sum<<" coefficient_by_size=";
  for(int k=0;k<=N;++k)if(counts[k])cout<<k<<":"<<counts[k]<<" ";
  cout<<"\n";
 }
 cout<<"VERIFY_OK\n";
}
