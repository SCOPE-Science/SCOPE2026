// Independent finite zero-forcing enumeration for even helm graphs.
// Build: c++ -std=c++17 -O2 check_cpp.cpp -o check_cpp && ./check_cpp
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using U = std::uint64_t;
static int n;
static std::vector<U> nb;
static bool color_all(U s){
 const U full=(U(1)<<(2*n+1))-1;
 while(s!=full){
  U newer=0;
  for(int i=0;i<2*n+1;i++)if(s&(U(1)<<i)){
    U white=nb[i]&~s;
    if(white && (white&(white-1))==0)newer|=white;
  }
  if(!newer)return false;
  s|=newer;
 }
 return true;
}
static void make_helm(){
 nb.assign(2*n+1,0);
 auto join=[](int a,int b){ nb[a]|=U(1)<<b;nb[b]|=U(1)<<a;};
 for(int i=0;i<n;i++){
  join(0,i+1);join(i+1,((i+1)%n)+1);join(i+1,n+i+1);
 }
}
static bool combinatorial_criterion(U s){
 std::vector<int> where,kind;
 for(int i=0;i<n;i++){
  int a=(s>>i)&1,b=(s>>((i+1)%n))&1;
  if(a==b){where.push_back(i);kind.push_back(a);}
 }
 int d=(int)where.size();if(d<4)return false;
 int count[2]={0,0};int distance[2]={-1,-1};
 for(int i=0;i<d;i++)if(kind[i]==kind[(i+1)%d]){
  int t=kind[i];count[t]++;distance[t]=(where[(i+1)%d]-where[i]+n)%n;
 }
 return count[0]==1 && count[1]==1 && distance[0]==1 && distance[1]==1;
}
int main(){
 for(n=6;n<=20;n+=2){
  make_helm();int k=n/2;std::uint64_t cnt=0;
  U S=(U(1)<<k)-1;U limit=U(1)<<n;
  while(S<limit){
   U leafmask=S<<(n+1);
   bool direct=color_all(leafmask);
   bool criterion=combinatorial_criterion(S);
   assert(direct==criterion);
   if(direct)cnt++;
   U low=S&-S,next=S+low;
   S=(((S^next)>>2)/low)|next;
  }
  std::uint64_t expect=(n==6)?6:(std::uint64_t)k*k*(U(1)<<(k-4));
  assert(cnt==expect);
  std::cout<<"n="<<n<<" states="<<cnt<<" expected="<<expect<<" criterion_ok=yes\n";
 }
 std::cout<<"CPP_VERIFY_OK\n";
}
