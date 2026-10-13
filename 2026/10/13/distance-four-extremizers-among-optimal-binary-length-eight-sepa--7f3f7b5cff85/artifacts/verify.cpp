#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
static int wt(int x){ return __builtin_popcount((unsigned)x); }
static bool separates(int a,int b,int c){
  int t[3]={a,b,c};
  for(int k=0;k<3;k++){
    int z=t[k],x=t[(k+1)%3],y=t[(k+2)%3];
    if(( ((~(x^y))&255) & (z^x) )==0) return false;
  }
  return true;
}
static vector<int> words; static vector<vector<uint64_t>> adj; static vector<int> chosen; static long long n0=0;
static bool edge(int i,int j){return (adj[i][j>>6]>>(j&63))&1ULL;}
static void enumerate(vector<int> cand){
  if(chosen.size()==9){ ++n0; return; }
  if(chosen.size()+cand.size()<9) return;
  for(int ii=0;ii<(int)cand.size();++ii){
    int v=cand[ii]; vector<int> nxt;
    for(int jj=ii+1;jj<(int)cand.size();++jj){
      int u=cand[jj]; if(!edge(v,u)) continue; bool ok=true;
      for(int r:chosen) if(!separates(words[r],words[v],words[u])){ok=false;break;}
      if(ok) nxt.push_back(u);
    }
    chosen.push_back(v); enumerate(nxt); chosen.pop_back();
  }
}
static bool valid(const vector<int>& C){
  for(int i=0;i<(int)C.size();++i) for(int j=i+1;j<(int)C.size();++j) if(wt(C[i]^C[j])<4) return false;
  for(int i=0;i<(int)C.size();++i) for(int j=i+1;j<(int)C.size();++j) for(int k=j+1;k<(int)C.size();++k)
    if(!separates(C[i],C[j],C[k])) return false;
  return true;
}
static int permute_bits(int x,const array<int,8>& p){ int y=0; for(int i=0;i<8;++i) if(x&(1<<i)) y|=1<<p[i]; return y; }
static long long stabilizer(const vector<int>& C){
  array<int,8> p={0,1,2,3,4,5,6,7}; set<int> S(C.begin(),C.end()); long long s=0;
  do{
    vector<int> P; for(int x:C) P.push_back(permute_bits(x,p));
    for(int t:C){ bool ok=true; for(int y:P) if(!S.count(y^t)){ok=false;break;} if(ok) ++s; }
  }while(next_permutation(p.begin(),p.end()));
  return s;
}
static map<pair<int,int>,int> distance_hist(const vector<int>& C){map<pair<int,int>,int> h; for(int i=0;i<10;i++){int a=0,b=0; for(int j=0;j<10;j++)if(i!=j){int d=wt(C[i]^C[j]); if(d==4)a++; if(d==6)b++;} h[{a,b}]++;} return h;}
int main(){
  for(int x=1;x<256;++x) if(wt(x)>=4) words.push_back(x);
  int n=words.size(), B=(n+63)/64; adj.assign(n,vector<uint64_t>(B));
  for(int i=0;i<n;++i) for(int j=i+1;j<n;++j) if(wt(words[i]^words[j])>=4 && separates(0,words[i],words[j])){
    adj[i][j>>6]|=1ULL<<(j&63); adj[j][i>>6]|=1ULL<<(i&63);
  }
  vector<int> cand(n); iota(cand.begin(),cand.end(),0); enumerate(cand);
  if(n0!=46200) return 2;
  long long labeled=n0*256/10; if(labeled!=1182720) return 3;
  vector<vector<int>> R={
    {0,15,51,60,85,90,150,153,225,238},
    {0,15,51,60,85,106,150,169,216,228},
    {0,15,51,60,85,106,150,169,216,231}
  };
  vector<long long> st,orb;
  for(auto &C:R){ if(!valid(C)) return 4; long long s=stabilizer(C); st.push_back(s); orb.push_back(10321920LL/s); }
  if(st!=vector<long long>({48,32,16})) return 5;
  if(orb!=vector<long long>({215040,322560,645120})) return 6;
  if(orb[0]+orb[1]+orb[2]!=labeled) return 7;
  auto h0=distance_hist(R[0]), h1=distance_hist(R[1]), h2=distance_hist(R[2]);
  if(h0==h1 || h0==h2 || h1==h2) return 8;
  cout<<"VERIFY_OK d4_containing_zero="<<n0<<" d4_labeled="<<labeled
      <<" orbit_sizes="<<orb[0]<<","<<orb[1]<<","<<orb[2]
      <<" stabilizers="<<st[0]<<","<<st[1]<<","<<st[2]<<" group=10321920\n";
}
