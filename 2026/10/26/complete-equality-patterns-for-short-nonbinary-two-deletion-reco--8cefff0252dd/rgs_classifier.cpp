#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

static int n,N,a[12],peak;
static long long total,eligible; static int best;
static map<int,long long> multiplicity;
static vector<pair<string,int>> maximizing;

static inline int shadow(int *x, int t, uint32_t *out){
 int z=0;
 // n <= 6; generate subsequences by omission masks with exactly t bits
 for(int mask=0; mask < (1<<n); ++mask){
  if(__builtin_popcount((unsigned)mask)!=t) continue;
  uint32_t code=0;
  for(int i=0;i<n;i++) if((mask & (1<<i))==0) code=(code<<4)|(unsigned)x[i];
  out[z++]=code;
 }
 sort(out,out+z);
 return (int)(unique(out,out+z)-out);
}
static inline int common(uint32_t *x,int nx,uint32_t *y,int ny){
 int i=0,j=0,c=0;
 while(i<nx && j<ny){
  if(x[i]==y[j]) {++c;++i;++j;}
  else if(x[i]<y[j]) ++i; else ++j;
 }
 return c;
}
static void process(){
 ++total;
 uint32_t x1[32],y1[32],x2[32],y2[32];
 int nx1=shadow(a,1,x1),ny1=shadow(a+n,1,y1);
 if(common(x1,nx1,y1,ny1))return;
 ++eligible;
 int nx2=shadow(a,2,x2),ny2=shadow(a+n,2,y2);
 int c=common(x2,nx2,y2,ny2);
 if(c>best){best=c;multiplicity.clear();maximizing.clear();}
 if(c==best){
  int s=peak+1;
  multiplicity[s]++;
  string v;
  for(int i=0;i<N;i++)v+=char('0'+a[i]);
  maximizing.emplace_back(v,s);
 }
}
static void rgs(int pos,int maximum){
 if(pos==N){peak=maximum;process();return;}
 for(int v=0;v<=maximum+1;v++){
  a[pos]=v;rgs(pos+1,max(maximum,v));
 }
}
int main(){
 for(n=3;n<=6;n++){
  N=2*n;total=eligible=0;best=-1;peak=0;
  multiplicity.clear();maximizing.clear();
  a[0]=0;rgs(1,0);
  cout<<"N "<<n<<" BELL "<<total<<" ELIGIBLE "<<eligible<<" MAX "<<best<<" EXTREMAL_PATTERNS "<<maximizing.size()<<"\n";
  for(auto const &[s,count]:multiplicity)cout<<"SUPPORT "<<s<<" PATTERNS "<<count<<"\n";
  for(auto const &[v,s]:maximizing)cout<<"PATTERN "<<v.substr(0,n)<<" "<<v.substr(n)<<" SUPPORT "<<s<<"\n";
 }
}
