// Exact finite check for a degree-controlled bipartite matching-capacity statement.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify_matching_capacity.cpp -o verify_matching_capacity
// Run: ./verify_matching_capacity
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;

static int maximum_matching(const vector<int> &rows, int alive, int m){
  const int n=(int)rows.size();
  vector<vector<int>> memo(n+1,vector<int>(1<<m,-1));
  function<int(int,int)> go=[&](int i,int used)->int{
    if(i==n)return 0;
    int &r=memo[i][used];if(r!=-1)return r;
    r=go(i+1,used); int avail=rows[i]&alive&(~used);
    while(avail){int b=avail&(-avail);avail-=b;r=max(r,1+go(i+1,used|b));}
    return r;
  };
  return go(0,0);
}
static bool connected(const vector<int>& rows,int m){
  int n=(int)rows.size(); if(n==0)return false;
  int plants=1,polls=0;
  for(int iter=0;iter<n+m;iter++){
    for(int i=0;i<n;i++)if(plants&(1<<i))polls|=rows[i];
    for(int i=0;i<n;i++)if(rows[i]&polls)plants|=1<<i;
  }
  return plants==(1<<n)-1 && polls==(1<<m)-1;
}
static vector<int> signature(const vector<int>& rows,int m){
  vector<int> d,e(m,0);for(int r:rows){d.push_back(__builtin_popcount((unsigned)r));for(int j=0;j<m;j++)e[j]+=((r>>j)&1);}
  sort(d.begin(),d.end());sort(e.begin(),e.end());d.push_back(-1);d.insert(d.end(),e.begin(),e.end());return d;
}
static vector<int> counts(const vector<int> &rows,int m){
  vector<int> a(m+1,0);
  for(int alive=0;alive<(1<<m);alive++)a[__builtin_popcount((unsigned)alive)]+=maximum_matching(rows,alive,m);
  return a;
}
static vector<int> decode_rows(int mask,int n,int m){
  vector<int> rows(n);for(int i=0;i<n;i++)rows[i]=(mask>>(i*m))&((1<<m)-1);return rows;
}
static int pairs_seen=0, connected_seen=0;
static void check_lower_bound(){
  for(int n=1;n<=7;n++)for(int m=1;n+m<=8;m++){
    if(n*m>20)throw runtime_error("Unexpected size");
    map<vector<int>,set<vector<int>>> signatures;
    int local=0;
    for(int mask=0;mask<(1<<(n*m));mask++){
      auto rows=decode_rows(mask,n,m);
      bool no_isolated=true;for(int r:rows)if(!r)no_isolated=false;
      if(!no_isolated||!connected(rows,m))continue;
      signatures[signature(rows,m)].insert(counts(rows,m));
      local++;connected_seen++;
    }
    for(const auto &it:signatures){
      const auto &v=it.second;
      for(auto a=v.begin();a!=v.end();a++)for(auto b=next(a);b!=v.end();b++){
        pairs_seen++;
        int s=0;
        for(int k=0;k<=m;k++){
          int diff=(*a)[k]-(*b)[k];int t=(diff>0)-(diff<0);
          if(t!=0 && s!=0 && t!=s)throw runtime_error("Mixed coefficient signs below nine vertices");
          if(t!=0)s=t;
        }
      }
    }
    cout<<"lower_bound_size="<<n<<"+"<<m<<" connected_labeled="<<local<<" degree_signatures="<<signatures.size()<<"\n";
  }
}
static void check_witness(){
  vector<int> A={29,7,2,1}, B={23,14,1,1};
  assert(connected(A,5)&&connected(B,5));
  assert(signature(A,5)==signature(B,5));
  vector<int> a=counts(A,5),b=counts(B,5);
  assert((a==vector<int>{0,5,19,27,17,4}));
  assert((b==vector<int>{0,5,20,26,14,3}));
  // Independent pure enumeration of all injective plant-pollinator assignments.
  auto exhaustive=[&](const vector<int>&rows,int alive){
    int best=0;function<void(int,int,int)> rec=[&](int i,int used,int got){
      if(i==(int)rows.size()){best=max(best,got);return;}
      rec(i+1,used,got);for(int j=0;j<5;j++)if((alive>>j&1)&&(rows[i]>>j&1)&&!(used>>j&1))rec(i+1,used|(1<<j),got+1);
    };rec(0,0,0);return best;
  };
  for(int s=0;s<32;s++){
    if(exhaustive(A,s)!=maximum_matching(A,s,5)||exhaustive(B,s)!=maximum_matching(B,s,5))
      throw runtime_error("Witness algorithm disagreement");
  }
  // Expand sum_k (a_k-b_k)*(1-q)^k*q^(5-k) by integer binomial coefficients.
  int choose[6][6]={{0}};
  for(int i=0;i<=5;i++){choose[i][0]=choose[i][i]=1;for(int j=1;j<i;j++)choose[i][j]=choose[i-1][j-1]+choose[i-1][j];}
  vector<int> polynomial(6,0);
  for(int k=0;k<=5;k++)for(int t=0;t<=k;t++)
    polynomial[5-k+t]+=(a[k]-b[k])*choose[k][t]*((t%2)?-1:1);
  assert((polynomial==vector<int>{1,-2,-1,4,-2,0}));
  // (1-q)^2 (1-2q^2), positive below q=1/sqrt(2), negative above.
  cout<<"witness_A=29,7,2,1; witness_B=23,14,1,1\n";
  cout<<"witness_coefficient_A=0,5,19,27,17,4\n";
  cout<<"witness_coefficient_B=0,5,20,26,14,3\n";
  cout<<"difference_polynomial=1,-2,-1,4,-2,0\n";
}
int main(){check_lower_bound();check_witness();cout<<"PASS connected_labeled="<<connected_seen<<" degree_profile_coefficient_pairs="<<pairs_seen<<"\n";}
