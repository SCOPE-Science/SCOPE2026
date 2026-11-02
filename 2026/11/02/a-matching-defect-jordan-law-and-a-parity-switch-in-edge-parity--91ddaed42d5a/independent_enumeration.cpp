// Exact state enumeration for binary neighbor-parity dynamics on line graphs.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
static U step(U x,const vector<U>& nei){
 U y=0;
 for(size_t e=0;e<nei.size();++e){
  if(__builtin_parityll(x&nei[e])) y|=U(1)<<e;
 }
 return y;
}
static U pow2(int j){return U(1)<<j;}
int main(){
 unsigned long long cases=0,states=0;
 for(int n=3;n<=7;++n)for(int k=0;k<=n/2;++k){
  set<pair<int,int>> absent;
  for(int i=0;i<k;++i) absent.insert({2*i,2*i+1});
  vector<pair<int,int>> edges;
  for(int u=0;u<n;++u)for(int v=u+1;v<n;++v)
   if(!absent.count({u,v}))edges.push_back({u,v});
  int E=int(edges.size());
  vector<U> nei(E);
  for(int e=0;e<E;++e)for(int f=0;f<E;++f)if(e!=f){
   auto [u,v]=edges[e];auto [a,b]=edges[f];
   if(u==a||u==b||v==a||v==b)nei[e]|=U(1)<<f;
  }
  unsigned long long counts[5][3]={};
  for(U x=0;x<pow2(E);++x){
    ++states;
    U y=step(x,nei),z=step(y,nei),w=step(z,nei);
    if(n%2){
      assert(w==y);
      int t=(z==x)?0:1;
      int p=(z==y)?1:2;
      ++counts[t][p];
    }else{
      assert(w==0);
      int t=x==0?0:y==0?1:z==0?2:3;
      ++counts[t][1];
    }
  }
  if(n%2){
    int r=n-1;
    U expectedFixed=pow2(E-k), expectedOsc=pow2(E)-expectedFixed;
    U fixedRecur=pow2(r-k),oscRecur=pow2(r)-fixedRecur;
    assert(counts[0][1]==fixedRecur && counts[0][2]==oscRecur);
    assert(counts[1][1]+counts[0][1]==expectedFixed);
    assert(counts[1][2]+counts[0][2]==expectedOsc);
  }else{
    int m=n/2, r1=n-2;
    int r2=k<m?k:m-1-(m%2==0);
    U expected[4]={1,pow2(E-r1)-1,pow2(E-r2)-pow2(E-r1),pow2(E)-pow2(E-r2)};
    for(int t=0;t<4;++t) assert(counts[t][1]==expected[t]);
  }
  ++cases;
  cout << "n="<<n<<" k="<<k<<" edge_states="<<E<<" all="<<pow2(E);
  if(n%2) cout<<" fixed_basin="<<counts[0][1]+counts[1][1]
                <<" two_basin="<<counts[0][2]+counts[1][2];
  else cout<<" zero_time_counts="<<counts[0][1]<<","<<counts[1][1]
           <<","<<counts[2][1]<<","<<counts[3][1];
  cout<<" OK\n";
 }
 cout<<"ALL_TESTS_PASS graph_cases="<<cases<<" initial_states="<<states<<"\n";
}
