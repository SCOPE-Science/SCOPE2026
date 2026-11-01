// Standalone verification of the primitive-four GH orbit formula on rook graphs.
// No external libraries beyond the C++17 standard library.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
struct RookGH {
 int a,b,n;vector<int> pw,neighbor;
 RookGH(int ra,int cb):a(ra),b(cb),n(a*b),pw(n+1,1),neighbor(n,0){
  if(n>20)throw runtime_error("bit-mask verification supports at most 20 cells");
  for(int i=1;i<=n;i++)pw[i]=pw[i-1]*3;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j&&(i/b==j/b||i%b==j%b))neighbor[i]|=(1<<j);
 }
 int next(int state)const{
  int v=state,excited=0;
  for(int i=0;i<n;i++){if(v%3==1)excited|=1<<i;v/=3;}
  int ans=0;v=state;
  for(int i=0;i<n;i++){
   int s=v%3;v/=3;
   int out=(s==1?2:(s==2?0:((excited&neighbor[i])?1:0)));
   ans+=out*pw[i];
  }
  return ans;
 }
 bool primitive4(int x)const{
  int y=next(x),z=next(y),w=next(z),u=next(w);
  return u==x&&z!=x;
 }
 int phase_to_state(const vector<int>&phase)const{
  int st=0;
  for(int i=0;i<n;i++)st+=(phase[i]==0?1:(phase[i]==3?2:0))*pw[i];
  return st;
 }
 set<int> construct_periodic4()const{
  set<int> result;
  for(int R=1;R<(1<<a)-1;R++)for(int C=1;C<(1<<b)-1;C++)
   for(int p=0;p<4;p++)for(int eps:{-1,1}){
    vector<int>phase(n);
    for(int r=0;r<a;r++)for(int c=0;c<b;c++){
     bool rb=(R>>r)&1, cb=(C>>c)&1;
     int val=(!rb&&!cb)?p:(!rb&&cb)?p+eps:(rb&&!cb)?p-eps:p+2;
     phase[r*b+c]=(val%4+4)%4;
    }
    int st=phase_to_state(phase);
    if(!primitive4(st))throw runtime_error("constructed state not primitive four");
    result.insert(st);
   }
  const uint64_t expected=2ull*((1ull<<a)-2)*((1ull<<b)-2);
  if(result.size()!=expected)throw runtime_error("construction duplicate count mismatch");
  return result;
 }
};
int main(){
 vector<pair<int,int>> samples={{2,2},{2,3},{2,4},{2,5},{2,6},{2,7},{3,3},{3,4},{3,5}};
 uint64_t examined=0;
 for(auto [a,b]:samples){
  RookGH g(a,b);
  set<int> made=g.construct_periodic4();
  uint64_t found=0;
  for(int x=0;x<g.pw[g.n];x++){
   bool brute=g.primitive4(x);
   bool predicted=made.count(x)!=0;
   if(brute!=predicted){cerr<<"DISAGREEMENT a="<<a<<" b="<<b<<" x="<<x<<"\n";return 1;}
   if(brute)found++;
  }
  examined+=g.pw[g.n];
  cout<<"a="<<a<<" b="<<b<<" states="<<g.pw[g.n]
      <<" period_four_states="<<found<<" primitive_orbits="<<(found/4)
      <<" formula="<<(((1ull<<a)-2)*((1ull<<b)-2)/2)<<" OK\n";
 }
 cout<<"COMPLETE: "<<examined<<" initial configurations, independent rectangle construction matches brute-force F^4 test.\n";
}
