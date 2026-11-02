// Independent exhaustive maximum-clique computation for binary cross-bifix-free codes.
// Compile: c++ -O3 -std=c++17 verify_independent.cpp -o verify_independent
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int n,d,M,W,best;
vector<string> words;
vector<vector<uint64_t>> adj;
int bit(const vector<uint64_t>&a){for(int j=0;j<W;j++)if(a[j])return j*64+__builtin_ctzll(a[j]);return -1;}
void clearbit(vector<uint64_t>&a,int k){a[k/64]&=~(1ULL<<(k%64));}
bool has(const vector<uint64_t>&a){for(auto v:a)if(v)return true;return false;}
void expand(vector<uint64_t> P,int cnt){
 if(!has(P)){if(cnt>best)best=cnt;return;}
 vector<int> order,bound;auto R=P;int col=0;
 while(has(R)){
  col++;auto Q=R;
  while(has(Q)){
   int v=bit(Q);clearbit(R,v);clearbit(Q,v);
   for(int j=0;j<W;j++)Q[j]&=~adj[v][j];
   order.push_back(v);bound.push_back(col);
  }
 }
 for(int k=int(order.size())-1;k>=0;k--){
  if(cnt+bound[k]<=best)return;
  int v=order[k];auto child=P;
  for(int j=0;j<W;j++)child[j]&=adj[v][j];
  expand(child,cnt+1);clearbit(P,v);
 }
}
bool unbordered(const string&s){for(int k=1;k<(int)s.size();k++)if(s.substr(0,k)==s.substr(s.size()-k))return false;return true;}
bool possible(const string&a,const string&b,int dist){
 int h=0;for(int i=0;i<(int)a.size();i++)h+=(a[i]!=b[i]);if(h<dist)return false;
 for(int k=1;k<(int)a.size();k++)if(a.substr(0,k)==b.substr(b.size()-k)||b.substr(0,k)==a.substr(a.size()-k))return false;
 return true;
}
int run(int len,int mindist){
 n=len;d=mindist;words.clear();
 for(int x=0;x<(1<<n);x++){
  string s(n,'0');for(int j=0;j<n;j++)if(x&(1<<(n-1-j)))s[j]='1';
  if(s.front()=='0'&&s.back()=='1'&&unbordered(s))words.push_back(s);
 }
 M=int(words.size());W=(M+63)/64;adj.assign(M,vector<uint64_t>(W));
 for(int i=0;i<M;i++)for(int j=i+1;j<M;j++)if(possible(words[i],words[j],d)){
  adj[i][j/64]|=1ULL<<(j%64);adj[j][i/64]|=1ULL<<(i%64);
 }
 vector<uint64_t>P(W,~0ULL);if(M%64)P.back()=(1ULL<<(M%64))-1;
 best=0;expand(P,0);return best;
}
int main(){for(int n=2;n<=11;n++)for(int d=2;d<=n;d++)cout<<n<<","<<d<<","<<run(n,d)<<"\n";}
