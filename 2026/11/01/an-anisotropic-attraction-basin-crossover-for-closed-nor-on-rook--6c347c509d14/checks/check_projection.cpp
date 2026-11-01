// Independent matrix-projection enumeration of self-inclusive NOR dynamics.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
using ull=unsigned long long;
ull rectangle(int a,int b,int rows,int cols){
  ull s=0;
  for(int i=0;i<a;i++)for(int j=0;j<b;j++)
    if((rows>>i&1)&&(cols>>j&1))s|=1ULL<<(i*b+j);
  return s;
}
int ones(int mask){return __builtin_popcount((unsigned)mask);}
long long choose(int n,int k){
  long long ans=1; for(int j=1;j<=k;j++)ans=ans*(n-j+1)/j; return ans;
}
long long occupancy(int r,int c){
  long long ans=0;
  for(int i=0;i<=r;i++)for(int j=0;j<=c;j++){
    long long z=choose(r,i)*choose(c,j)*(1LL<<((r-i)*(c-j)));
    ans+=((i+j)&1)?-z:z;
  }
  return ans;
}
void test(int a,int b){
  const int N=a*b;
  assert(N<=20);
  ull lim=1ULL<<N;
  map<pair<ull,ull>,long long> basins;
  long long periodic=0;
  for(ull s=0;s<lim;s++){
    int R=0,C=0;
    for(int i=0;i<a;i++)for(int j=0;j<b;j++)
      if(s>>(i*b+j)&1){R|=(1<<i); C|=(1<<j);}
    ull f=rectangle(a,b,((1<<a)-1)^R,((1<<b)-1)^C);
    int R1=0,C1=0;
    for(int i=0;i<a;i++)for(int j=0;j<b;j++)
      if(f>>(i*b+j)&1){R1|=1<<i;C1|=1<<j;}
    ull f2=rectangle(a,b,((1<<a)-1)^R1,((1<<b)-1)^C1);
    assert(f!=f2);
    int R2=0,C2=0;
    for(int i=0;i<a;i++)for(int j=0;j<b;j++)
      if(f2>>(i*b+j)&1){R2|=1<<i;C2|=1<<j;}
    ull f3=rectangle(a,b,((1<<a)-1)^R2,((1<<b)-1)^C2);
    assert(f3==f);
    if(s==f || s==f2)periodic++;
    basins[minmax(f,f2)]++;
  }
  long long cycles=1LL + ((1LL<<a)-2)*((1LL<<b)-2)/2;
  assert((long long)basins.size()==cycles);
  ull full=lim-1;
  long long B=1;
  for(int r=1;r<=a;r++)for(int c=1;c<=b;c++)
     if(r==a || c==b) B+=choose(a,r)*choose(b,c)*occupancy(r,c);
  assert(basins.at({0,full})==B);
  for(auto &entry:basins){
    if(entry.first==make_pair(0ULL,full))continue;
    int R=0,C=0;
    ull s=entry.first.first;
    for(int i=0;i<a;i++)for(int j=0;j<b;j++)
      if(s>>(i*b+j)&1){R|=1<<i;C|=1<<j;}
    long long expected=occupancy(ones(R),ones(C))+occupancy(a-ones(R),b-ones(C));
    assert(entry.second==expected);
  }
  assert(periodic==2*cycles);
  long long total=0; for(const auto &entry:basins)total+=entry.second;
  assert(total==(long long)lim);
  cout<<a<<"x"<<b<<" "<<lim<<" states; "<<cycles<<" cycles; "<<B<<" central; "<<periodic<<" periodic\n";
}
int main(){
  vector<pair<int,int>> dims={{2,2},{2,3},{2,4},{2,9},{3,3},{3,4},{3,5},{3,6},{4,4},{4,5}};
  ull count=0;
  for(auto [a,b]:dims){test(a,b); count+=1ULL<<(a*b);}
  cout<<"PROJECTION_OK total_states "<<count<<"\n";
}
