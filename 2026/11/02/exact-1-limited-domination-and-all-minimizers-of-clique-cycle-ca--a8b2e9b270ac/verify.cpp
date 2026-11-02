// Independent finite checks of one-limited domination on K_m square C_n.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
// Standard C++17 only. All graph labels are vertices (column, row).
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

static pair<int,long long> predicted(int m, int n) {
  const int q=n/4, r=n%4;
  const int h=2*q+(r==3);
  const int minset=m*(n-h);
  long long count=(r==0?4:(r==2?1LL*n*n/4:n));
  if(m==3 && (n==3 || n==6)) count+=3;
  return {minset,count};
}

// All-subset search on the original labelled graph: does not use any
// clique-column reduction or binary-word characterization.
static pair<int,long long> direct(int m,int n) {
  const int N=m*n;
  if(N>24) throw runtime_error("direct experiment too large");
  vector<uint32_t> adj(N,0);
  for(int j=0;j<n;j++) for(int i=0;i<m;i++) {
    const int v=j*m+i;
    for(int k=0;k<m;k++) if(i!=k) adj[v]|=uint32_t(1)<<(j*m+k);
    adj[v]|=uint32_t(1)<<(((j+1)%n)*m+i);
    adj[v]|=uint32_t(1)<<(((j+n-1)%n)*m+i);
  }
  int best=N+1;long long count=0;
  const uint32_t whole=(uint32_t(1)<<N)-1;
  for(uint32_t mask=0;mask<=whole;mask++) {
    const int size=__builtin_popcount(mask);
    if(size>best) continue;
    bool good=true;
    for(int v=0;v<N;v++) {
      const uint32_t outside=adj[v]&(whole^mask);
      if(mask&(uint32_t(1)<<v)) {
        if(__builtin_popcount(outside)>1) {good=false;break;}
      } else if((adj[v]&mask)==0) {good=false;break;}
    }
    if(!good) continue;
    if(size<best) {best=size;count=0;}
    ++count;
  }
  return {best,count};
}

// Independent cyclic dynamic programming over every locally allowed column
// occupancy, including singleton labels; it uses direct neighbor conditions.
static bool omitted(int typ,int row,int m) {
  return typ==m+1 || (typ>=1 && typ<=m && typ==row+1);
}
static int omitted_count(int typ,int m) {
  return typ==m+1?m:(typ==0?0:1);
}
static bool allowed(int left,int center,int right,int m) {
  const int s=omitted_count(center,m);
  for(int i=0;i<m;i++) {
    const bool out=omitted(center,i,m);
    const int h=int(omitted(left,i,m))+int(omitted(right,i,m));
    if(out) {
      if(s==m && h==2) return false;
    } else if(s+h>1) return false;
  }
  return true;
}
static pair<int,long long> column_dp(int m,int n) {
  const int Q=m+2;
  int best=-1;long long ways=0;
  using State=pair<int,int>;
  using Value=pair<int,long long>;
  for(int a=0;a<Q;a++)for(int b=0;b<Q;b++) {
    map<State,Value> dp;
    dp[{a,b}]={omitted_count(a,m)+omitted_count(b,m),1};
    for(int k=2;k<n;k++) {
      map<State,Value> ndp;
      for(const auto& e:dp) {
        const int x=e.first.first,y=e.first.second;
        for(int c=0;c<Q;c++) if(allowed(x,y,c,m)) {
          const int w=e.second.first+omitted_count(c,m);
          const State t={y,c};
          auto it=ndp.find(t);
          if(it==ndp.end() || w>it->second.first) ndp[t]={w,e.second.second};
          else if(w==it->second.first) it->second.second+=e.second.second;
        }
      }
      dp.swap(ndp);
    }
    for(const auto& e:dp) {
      const int x=e.first.first,y=e.first.second;
      if(!allowed(x,y,a,m) || !allowed(y,a,b,m))continue;
      const int w=e.second.first;
      if(w>best) {best=w;ways=e.second.second;}
      else if(w==best) ways+=e.second.second;
    }
  }
  return {m*n-best,ways};
}

int main() {
  int direct_cases=0;
  for(auto p: vector<pair<int,int>>{{3,3},{3,4},{3,5},{3,6},
                                     {4,3},{4,4},{4,5},{4,6},
                                     {5,3},{5,4}}) {
    const auto got=direct(p.first,p.second);
    const auto expected=predicted(p.first,p.second);
    if(got!=expected) {
      cerr<<"DIRECT_MISMATCH "<<p.first<<" "<<p.second<<"\n";
      return 1;
    }
    direct_cases++;
  }
  cout<<"DIRECT_ORIGINAL_GRAPH_EXHAUSTIVE_OK "<<direct_cases<<" CASES\n";
  int dp_cases=0;
  for(int m=3;m<=8;m++) for(int n=3;n<=34;n++) {
    const auto got=column_dp(m,n);
    const auto expected=predicted(m,n);
    if(got!=expected) {
      cerr<<"COLUMN_DP_MISMATCH "<<m<<" "<<n<<" "
          <<got.first<<" "<<got.second<<" vs "
          <<expected.first<<" "<<expected.second<<"\n";
      return 1;
    }
    dp_cases++;
  }
  cout<<"COLUMN_PATTERN_DP_OK "<<dp_cases<<" CASES\n";
  // The general product bound does not force equality on arbitrary bases:
  // K_3 square K_{1,3} admits the eight-vertex chosen set consisting of
  // the first two clique rows in all four base columns.
  cout<<"VERIFY_OK\n";
  return 0;
}
