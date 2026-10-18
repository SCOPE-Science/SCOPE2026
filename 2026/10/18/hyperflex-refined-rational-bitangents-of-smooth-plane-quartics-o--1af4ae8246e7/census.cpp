#include <cstdio>
#include <vector>
#include <array>
#include <map>
#include <tuple>
#include <algorithm>
#include <cstdint>
#include <cstring>
#include <string>
#include <chrono>
#include "tables.hpp"
using namespace std;
constexpr int P3_15=14348907;
int POW3[16];
struct Term {unsigned char i,j,v;};
vector<Term> TERMS[4];
void init() {
 POW3[0]=1; for(int k=1;k<=15;k++)POW3[k]=POW3[k-1]*3;
 for (int g=0;g<4;g++)for(int i=0;i<15;i++)for(int j=0;j<15;j++)if(GM[g][i][j])TERMS[g].push_back(Term{(unsigned char)i,(unsigned char)j,(unsigned char)GM[g][i][j]});
}
inline void decode(int n,uint8_t a[15]) {for(int i=0;i<15;i++){a[i]=n%3;n/=3;}}
inline int encode(uint8_t a[15]) {int n=0;for(int i=0;i<15;i++)n+=POW3[i]*a[i];return n;}
inline int normalize_encode(int a[15]) {
 int factor=1;
 for(int i=0;i<15;i++){a[i]%=3;if(a[i]<0)a[i]+=3;if(a[i]){if(a[i]==2)factor=2;break;}}
 int n=0;for(int i=0;i<15;i++)n+=POW3[i]*(a[i]*factor%3);
 return n;
}
inline int apply(int code,int g) {
 uint8_t a[15];decode(code,a);
 int b[15]={};
 for(const Term & t:TERMS[g]) b[t.j]+=a[t.i]*t.v;
 return normalize_encode(b);
}
int num_bitangents(int code,int &nproper,int &nhyper) {
 uint8_t a[15];decode(code,a);
 nproper=nhyper=0;
 for(int l=0;l<13;l++){
  int b[5]={};
  for(int i=0;i<15;i++)if(a[i])for(int j=0;j<5;j++)b[j]+=a[i]*RESTR[l][i][j];
  int factor=1;
  for(int j=0;j<5;j++){
   b[j]%=3;
   if(b[j]){if(b[j]==2)factor=2;break;}
  }
  for(int j=0;j<5;j++)b[j]=(b[j]*factor)%3;
  bool matched=false;
  for(int i=0;i<9 && !matched;i++){
   bool eq=true;for(int j=0;j<5;j++)if(b[j]!=PROPER[i][j]){eq=false;break;}
   if(eq){nproper++;matched=true;}
  }
  for(int i=0;i<4 && !matched;i++){
   bool eq=true;for(int j=0;j<5;j++)if(b[j]!=HYPER[i][j]){eq=false;break;}
   if(eq){nhyper++;matched=true;}
  }
 }
 return nproper+nhyper;
}
int rank_check(int code) {
 uint8_t coef[15];decode(code,coef);
 uint8_t A[36][45]={};
 for(int c=0;c<45;c++)for(int k=0;k<RANK_NUM[c];k++){
  int i=RANK_I[c][k],r=RANK_R[c][k];
  A[r][c]=(A[r][c]+coef[i]*RANK_V[c][k])%3;
 }
 int rank=0;
 for(int col=0;col<45 && rank<36;col++){
  int piv=rank;while(piv<36 && A[piv][col]==0)piv++;
  if(piv>=36)continue;
  if(piv!=rank)for(int c=col;c<45;c++)swap(A[piv][c],A[rank][c]);
  if(A[rank][col]==2)for(int c=col;c<45;c++)A[rank][c]=(2*A[rank][c])%3;
  for(int r=rank+1;r<36;r++){
   int fact=A[r][col];if(!fact)continue;
   for(int c=col;c<45;c++)A[r][c]=(A[r][c]+3-fact*A[rank][c]%3)%3;
  }
  rank++;
 }
 return rank;
}
int num_rational(int code){
 uint8_t a[15];decode(code,a);int nr=0;
 for(int i=0;i<13;i++){
  int s=0;
  for(int m=0;m<15;m++){
   int t=1;for(int j=0;j<3;j++)for(int k=0;k<MONOMS[m][j];k++)t=t*POINTS[i][j]%3;
   s+=t*a[m];
  }
  if(s%3==0)nr++;
 }
 return nr;
}
int main(){
 init();
 FILE *out=fopen("orbits.csv","w");
 if(!out){perror("open");return 2;}
 fprintf(out,"code,size,smooth,bitangent_proper,hyperflex,rational_points\n");
 vector<uint8_t> seen(P3_15,0);vector<int> q;
 long long count=0,norbits=0,smooth_count=0,smooth_orbits=0;
 map<pair<int,int>,long long> W, WO;map<int,long long> maxreps;
 int max_proper=-1,max_all=-1;
 auto t0=chrono::steady_clock::now();
 for(int seed=1;seed<P3_15;seed++){
  if(seen[seed])continue;
  uint8_t cf[15];decode(seed,cf);
  uint8_t first=0;for(int i=0;i<15;i++)if(cf[i]){first=cf[i];break;}
  if(first!=1)continue;
  q.clear();q.push_back(seed);seen[seed]=1;
  for(size_t k=0;k<q.size();k++)for(int g=0;g<4;g++){
   int target=apply(q[k],g);
   if(!seen[target]){seen[target]=1;q.push_back(target);}
  }
  int orbit=q.size();count+=orbit;norbits++;
  int rank=rank_check(seed),pr=-1,h=-1,rational=-1;
  if(rank==36){
   num_bitangents(seed,pr,h);rational=num_rational(seed);
   smooth_count+=orbit;smooth_orbits++;W[{pr,h}]+=orbit;WO[{pr,h}]++;
   if(pr>max_proper){max_proper=pr;maxreps.clear();}
   if(pr==max_proper)maxreps[seed]=orbit;
   max_all=max(max_all,pr+h);
  }
  fprintf(out,"%d,%d,%d,%d,%d,%d\n",seed,orbit,rank==36,pr,h,rational);
  if(norbits%200==0){auto t=chrono::duration<double>(chrono::steady_clock::now()-t0).count();fprintf(stderr,"orbits=%lld forms=%lld smooth=%lld time=%.2fs\n",norbits,count,smooth_count,t);fflush(stderr);}
 }
 fclose(out);
 printf("orbits=%lld forms=%lld smooth_orbits=%lld smooth_forms=%lld max_proper=%d max_all=%d\n",norbits,count,smooth_orbits,smooth_count,max_proper,max_all);
 for(auto &kv:W)printf("bitangents proper=%d hyperflex=%d forms=%lld orbits=%lld\n",kv.first.first,kv.first.second,kv.second,WO[kv.first]);
 for(auto &kv:maxreps)printf("maximum_rep code=%d orbit=%lld\n",kv.first,kv.second);
}
