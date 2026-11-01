// Exhaustive labeled-state verification of three-color inhibitory dynamics
// on a complete-split graph. Independent of support-mask enumeration.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using State=vector<int>;

State advance_color(const State& x,int m){
  const int N=(int)x.size();
  State y(N);
  for(int i=0;i<N;++i){
    bool blinks=false;
    if(x[i]==2){
      for(int j=0;j<N;++j){
        if(j!=i && x[j]==1 && (i<m || j<m)) {blinks=true;break;}
      }
    }
    y[i]=(x[i]==2 && blinks) ? 2 : (x[i]+1)%3;
  }
  return y;
}
int first_sync(State x,int m){
  for(int t=0;t<=6;++t){
    bool all=true;
    for(int c:x) if(c!=x.front()){all=false;break;}
    if(all)return t;
    x=advance_color(x,m);
  }
  return 7;
}

array<int64_t,8> exact(int m,int n){
  int64_t U=(1LL<<m)-2, V=(1LL<<n)-2;
  int64_t R=1; for(int i=0;i<n;++i)R*=3;
  int64_t W=1; for(int i=0;i<m;++i)W*=3;
  int64_t v=W-3*(1LL<<m)+3;
  int64_t r=R-3*(1LL<<n)+3;
  return {3, (1LL<<n)*(U+1), R*(U+v)+(1LL<<n)*(U+1),
          (1LL<<n)*(U+1), V,
          U*(R-(1LL<<n)-1)+R-3,
          U*(R-(1LL<<(n+1))+1)+R-(1LL<<n)-1,
          r};
}
int main(){
  int64_t states=0;
  int cases=0;
  for(int m=1;m<=6;++m)for(int n=1;n<=7;++n){
    if(m+n>11)continue;
    int N=m+n;
    int64_t total=1;for(int i=0;i<N;++i)total*=3;
    array<int64_t,8> got{};
    for(int64_t word=0;word<total;++word){
      State x(N); auto z=word;
      for(int i=0;i<N;++i){x[i]=z%3;z/=3;}
      int t=first_sync(x,m);
      ++got[t];
      if(t==7){
        // Exceptional states are three-cyclic from time zero.
        State w=advance_color(advance_color(advance_color(x,m),m),m);
        assert(w==x);
        for(int i=0;i<m;++i)assert(x[i]==2);
        bool used[3]={false,false,false};
        for(int i=m;i<N;++i)used[x[i]]=true;
        assert(used[0]&&used[1]&&used[2]);
      }
    }
    if(got!=exact(m,n)){
      cerr<<"MISMATCH "<<m<<" "<<n<<"\n";
      return 1;
    }
    ++cases; states+=total;
  }
  cout<<"DIRECT_EXHAUSTIVE_OK: "<<cases<<" size pairs; "<<states<<" total labeled states; m+n<=11\n";
}
