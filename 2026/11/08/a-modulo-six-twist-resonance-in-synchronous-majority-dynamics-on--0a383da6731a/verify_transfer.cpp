// Independent exact transfer matrix for majority periodic constraints on cyclic ladders.
// This does not evolve configurations: it counts cyclic space-time words directly.
// Build: g++ -O3 -std=c++17 verify_transfer.cpp -o verify_transfer
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static uint64_t lucas(int n){uint64_t a=2,b=1;for(int i=0;i<n;i++){auto c=a+b;a=b;b=c;}return a;}
static int eps(int n){const int e[6]={2,1,-1,-2,-1,1};return e[n%6];}
static int delta(int n){const int d[3]={2,-1,-1};return d[n%3];}
static int maj(int a,int b,int c){return (a+b+c>=2);}
static int bits(int col,int l,int time,int order){return (col>>(l+2*time))&1;}
static int swapcol(int col,int order){
 int ret=0;
 for(int t=0;t<order;t++)for(int l=0;l<2;l++)ret|=bits(col,l,t,order)<<(1-l+2*t);
 return ret;
}
static bool local(int left,int center,int right,int order,int kind){
 for(int l=0;l<2;l++)for(int t=0;t<order;t++){
  int z=maj(bits(left,l,t,order),bits(right,l,t,order),bits(center,1-l,t,order));
  int expected=kind==0?bits(center,l,0,order):kind==1?(1-bits(center,l,0,order)):bits(center,l,1-t,order);
  if(z!=expected)return false;
 }
 return true;
}
static uint64_t trace_word(int n,int twist,int kind){
 int order=kind==2?2:1, alpha=order==2?16:4, nodes=alpha*alpha;
 vector<vector<int>> edges(nodes);
 for(int a=0;a<alpha;a++)for(int b=0;b<alpha;b++)for(int c=0;c<alpha;c++){
  if(local(a,b,c,order,kind))edges[a*alpha+b].push_back(b*alpha+c);
 }
 vector<uint64_t> curr(nodes),next(nodes);
 uint64_t total=0;
 for(int start=0;start<nodes;start++){
  fill(curr.begin(),curr.end(),0);curr[start]=1;
  for(int step=0;step<n;step++){
   fill(next.begin(),next.end(),0);
   for(int j=0;j<nodes;j++)if(curr[j])for(int k:edges[j])next[k]+=curr[j];
   curr.swap(next);
  }
  int a=start/alpha,b=start%alpha;
  int target=twist?swapcol(a,order)*alpha+swapcol(b,order):start;
  total+=curr[target];
 }
 return total;
}
int main(){
 for(int n=3;n<=22;n++)for(int twist=0;twist<=1;twist++){
  uint64_t f=trace_word(n,twist,0),q=trace_word(n,twist,1),p=trace_word(n,twist,2);
  uint64_t ff=lucas(n)+eps(n)+2*(twist==0);
  uint64_t qq=lucas(n)+(twist?-delta(n):delta(n))+2*(n%2==0);
  uint64_t pp;
  if((n+twist)%2==0)pp=ff*ff;
  else pp=lucas(2*n)+eps(2*n)+2;
  if(f!=ff||q!=qq||p!=pp){cerr<<"FAIL n="<<n<<" twist="<<twist<<" trace="<<f<<","<<q<<","<<p<<" predicted="<<ff<<","<<qq<<","<<pp<<"\n";return 1;}
  cout<<"n="<<n<<" twist="<<twist<<" fixed="<<f<<" fixed_two="<<p<<" fullflip="<<q<<" OK\n";
 }
 cout<<"PASS independent exact transfer 40 instances\n";
}
