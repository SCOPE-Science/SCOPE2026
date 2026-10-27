// Exhaustive vertex-level check, independently updating all labelled vertices.
// All graph edges are reconstructed from the three shore labels; no quotient
// states or finite-certificate transition maps are used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

uint64_t step(uint64_t packed,const vector<int> &part,int count_vertices){
 vector<int> state(count_vertices);
 uint64_t temp=packed;
 for(int i=0;i<count_vertices;++i){state[i]=temp%3;temp/=3;}
 int counts[3][3]={{0}};
 for(int i=0;i<count_vertices;++i)++counts[part[i]][state[i]];
 uint64_t answer=0,mul=1;
 for(int i=0;i<count_vertices;++i){
  int successor=(state[i]+1)%3;
  int excited=0;
  for(int j=0;j<3;++j)if(j!=part[i])excited+=counts[j][successor];
  int nxt=excited>=2?successor:state[i];
  answer+=mul*nxt;mul*=3;
 }
 return answer;
}
void inspect(int a,int b,int c,map<int,uint64_t> expect){
 int total=a+b+c;
 vector<int> part(total);
 for(int i=a;i<a+b;++i)part[i]=1;
 for(int i=a+b;i<total;++i)part[i]=2;
 uint64_t bound=1;for(int i=0;i<total;++i)bound*=3;
 map<int,uint64_t> periodic;
 int worst=0;
 for(uint64_t x=0;x<bound;++x){
  array<uint64_t,22> seq{};seq[0]=x;
  for(int j=1;j<22;++j)seq[j]=step(seq[j-1],part,total);
  assert(seq[9]==seq[21]);
  int entry=-1,period=-1;
  for(int t=0;t<=9;++t)if(seq[t]==seq[t+12]){entry=t;break;}
  assert(entry>=0);
  for(int p:{1,2,3,4,6,12})if(seq[entry]==seq[entry+p]){period=p;break;}
  assert(period>0);
  worst=max(worst,entry);
  if(entry==0)++periodic[period];
 }
 for(int p:{4,6,12})assert(periodic[p]==expect[p]);
 cout<<"DIRECT "<<a<<","<<b<<","<<c<<" size="<<bound<<" maxpre="<<worst<<" recurrent:";
 for(auto [p,v]:periodic)cout<<" "<<p<<"="<<v;
 cout<<"\n";
}
int main(){
 inspect(1,4,4,{{12,648}});
 inspect(2,2,2,{{6,48}});
 inspect(2,2,4,{{4,144}});
 inspect(2,4,4,{{12,1296}});
 inspect(3,4,4,{{12,1296}});
 inspect(5,3,2,{});
 cout<<"DIRECT_VERTICES_OK\n";
}
