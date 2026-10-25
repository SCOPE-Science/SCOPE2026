#include <iostream>
#include <vector>
#include <array>
#include <iomanip>
#include <stdint.h>
#include <algorithm>
using namespace std;
static bool is_subseq(int small,int ns,int big,int nb){
  int i=0;
  for(int j=0;j<nb;j++)if(i<ns && ((small>>(ns-1-i))&1)==((big>>(nb-1-j))&1))i++;
  return i==ns;
}
vector<uint32_t> rows(int n,bool ins){
  int m=n+(ins?2:-2),N=1<<n,M=1<<m;
  vector<uint32_t> a(M,0);
  for(int y=0;y<M;y++)for(int x=0;x<N;x++)if(ins?is_subseq(x,n,y,m):is_subseq(y,m,x,n))a[y]|=(uint32_t(1)<<x);
  return a;
}
struct Counts {uint64_t count=0,first=0;vector<uint64_t> list;};
Counts census(const vector<uint32_t>&a,int n,int k){
 int N=1<<n; Counts c;
 uint64_t s=(1ULL<<k)-1,limit=1ULL<<N;
 while(s<limit){
  bool valid=true;
  for(auto row:a)if(__builtin_popcount((uint32_t)s & row)>2){valid=false;break;}
  if(valid){if(!c.count)c.first=s; c.count++;if(N<=32 && k<=6)c.list.push_back(s);}
  uint64_t t=s&-s, u=s+t;
  if(!u || u>=limit) break;
  s=u|(((s^u)>>2)/t);
 }
 return c;
}
string words(uint64_t mask,int n){
 string res="";for(int i=0;i<(1<<n);i++)if(mask>>i&1){if(res.size())res+=",";for(int j=n-1;j>=0;j--)res+=((i>>j&1)?'1':'0');}return res;
}
int main(){
 for(int n=2;n<=5;n++)for(bool ins:{false,true}){
  auto a=rows(n,ins);int kmax= n==2?3:n==3?4:n==4?5:(ins?7:5);
  cerr <<"n="<<n<<" "<<(ins?"ins":"del")<<" rows="<<a.size()<<"\n";
  for(int k=1;k<=kmax;k++){
   Counts c=census(a,n,k);
   cout<<"n="<<n<<" op="<<(ins?"ins":"del")<<" k="<<k<<" count="<<c.count;
   if(c.count)cout<<" first="<<words(c.first,n);
   cout<<"\n";
  }
 }
}
