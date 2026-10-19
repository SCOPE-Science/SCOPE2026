// Independent exact certificate: reduce the palindrome-covering cycle problem
// to an asymmetric Hamiltonian tour on mandatory de Bruijn edges.
// Compile: c++ -O2 -std=c++17 verify_overlap_tsp.cpp -o verify_tsp
// Run: ./verify_tsp
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

static bool pal(int x,int k){int y=x,r=0;for(int i=0;i<k;i++){r=(r<<1)|(y&1);y>>=1;}return r==x;}
static string bits(int x,int n){string s(n,'0');for(int i=n-1;i>=0;i--){s[i]=char('0'+(x&1));x>>=1;}return s;}
static string shortest_connector(const string& u,const string& v){
  const int m=u.size();
  for(int t=m;t>=0;t--)if(u.substr(m-t)==v.substr(0,t))return v.substr(t);
  throw runtime_error("unreachable");
}
static bool covers(const string& cyc,int k){
  vector<char> seen(1<<k,0);
  for(int i=0;i<(int)cyc.size();i++){
    int x=0;for(int j=0;j<k;j++)x=2*x+cyc[(i+j)%cyc.size()]-'0';
    if(pal(x,k))seen[x]=1;
  }
  for(int x=0;x<(1<<k);x++)if(pal(x,k)&&!seen[x])return false;
  return true;
}
int main(){const int expected[]={0,0,4,8,12,22,32,60,74};
for(int k=2;k<=8;k++){
 vector<string> p;
 for(int x=0;x<(1<<k);x++)if(pal(x,k))p.push_back(bits(x,k));
 const int m=p.size(),N=1<<m,INF=100000000;
 vector<string> head(m),tail(m);
 vector<vector<int>> cost(m,vector<int>(m));
 vector<vector<string>> connector(m,vector<string>(m));
 for(int i=0;i<m;i++){
  tail[i]=p[i].substr(0,k-1);head[i]=p[i].substr(1,k-1);
 }
 for(int i=0;i<m;i++)for(int j=0;j<m;j++){
  connector[i][j]=shortest_connector(head[i],tail[j]);
  cost[i][j]=1+(int)connector[i][j].size();
 }
 vector<int32_t> dp(N*m,INF),parent(N*m,-1);
 vector<unsigned long long> ways(N*m,0);
 dp[m]=0;ways[m]=1; // subset {0}, last=0 : index (1*m+0)
 for(int mask=1;mask<N;mask+=2){ // every considered subset contains the fixed edge 0
  for(int i=0;i<m;i++)if(mask&(1<<i)){
   int val=dp[mask*m+i];if(val>=INF)continue;
   for(int j=1;j<m;j++)if(!(mask&(1<<j))){
    int nmask=mask|(1<<j),pos=nmask*m+j;
    int v=val+cost[i][j];
    if(v<dp[pos]){dp[pos]=v;parent[pos]=i;ways[pos]=ways[mask*m+i];}
    else if(v==dp[pos])ways[pos]+=ways[mask*m+i];
   }
  }
 }
 int best=INF,last=-1; unsigned long long total_ways=0;
 for(int i=0;i<m;i++){
  int v=dp[(N-1)*m+i]+cost[i][0];
  if(v<best){best=v;last=i;total_ways=ways[(N-1)*m+i];}
  else if(v==best)total_ways+=ways[(N-1)*m+i];
 }
 const unsigned long long expectedTours[]={0,0,1,2,2,8,40,6272,768};
 if(best!=expected[k] || total_ways!=expectedTours[k])throw runtime_error("TSP result differs from expected");
 vector<int> route(m,-1);int mask=N-1;
 for(int t=m-1;t>=1;t--){route[t]=last;
   int j=parent[mask*m+last];mask^=1<<last;last=j;
 }
 route[0]=0;
 string cyc="0"; // mandatory edge 0^k already traversed
 for(int t=1;t<m;t++)cyc+=connector[route[t-1]][route[t]]+p[route[t]].substr(k-1);
 cyc+=connector[route[m-1]][route[0]];
 if((int)cyc.size()!=best || !covers(cyc,k))throw runtime_error("bad constructive tour");
 cout<<"k="<<k<<" exact="<<best<<" distinct_palindromes="<<m<<" optimal_tours="<<total_ways<<" cycle="<<cyc<<'\n';
}
cout<<"VERIFY_OK independent_overlap_TSP_k=2..8\n";
}
