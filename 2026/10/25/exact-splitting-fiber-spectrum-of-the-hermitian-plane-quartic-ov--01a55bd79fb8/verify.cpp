// Exact projective incidence computation for the Hermitian quartic over F_{3^6}.
// F_{3^6}=F_3[t]/(t^6+t+2), elements base-three encoded 0..728.
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
constexpr int Q=729, Q2=Q*Q, NL=Q2+Q+1;
using I=uint16_t;
vector<I> ADD(Q*Q), MUL(Q*Q);
I INV[Q], NEG[Q], POW3[Q], POW4[Q];
inline I ad(int a,int b){return ADD[a*Q+b];}
inline I mu(int a,int b){return MUL[a*Q+b];}
inline I ne(int a){return NEG[a];}
inline I su(int a,int b){return ad(a,ne(b));}
inline I dv(int a,int b){return mu(a,INV[b]);}
I powe(int a,int e){I r=1;while(e){if(e&1)r=mu(r,a);a=mu(a,a);e>>=1;}return r;}
void makefield(){
 int d[Q][6]={};for(int x=0;x<Q;x++){int y=x;for(int j=0;j<6;j++){d[x][j]=y%3;y/=3;}}
 for(int x=0;x<Q;x++)for(int y=0;y<Q;y++){
  int v=0,p=1;
  for(int j=0;j<6;j++){v+=((d[x][j]+d[y][j])%3)*p;p*=3;}
  ADD[x*Q+y]=v;
  int c[11]={};for(int i=0;i<6;i++)for(int j=0;j<6;j++)c[i+j]+=d[x][i]*d[y][j];
  // t^6 = 1+2t
  for(int j=10;j>=6;j--){c[j-6]+=c[j];c[j-5]+=2*c[j];}
  v=0;p=1;for(int j=0;j<6;j++){v+=(c[j]%3)*p;p*=3;}
  MUL[x*Q+y]=v;
 }
 for(int a=0;a<Q;a++){int c=a,n=0,p=1;for(int j=0;j<6;j++){n+=((3-c%3)%3)*p;c/=3;p*=3;}NEG[a]=n;}
 for(int a=1;a<Q;a++)INV[a]=powe(a,Q-2);
 for(int a=0;a<Q;a++){POW3[a]=powe(a,3);POW4[a]=powe(a,4);}
}
// projective line with equation Ax+By+Cz=0. Normalize leftmost nonzero coefficient.
inline int lineid(int A,int B,int C){
 if(A){int i=INV[A];return mu(B,i)*Q+mu(C,i);}
 if(B)return Q2+dv(C,B);
 assert(C);return NL-1;
}
inline void pointcurve(vector<pair<I,I>>& pts,vector<uint8_t>& onC){
 vector<vector<I>> roots(Q);
 for(int y=0;y<Q;y++)roots[ad(POW3[y],y)].push_back(y);
 for(int x=0;x<Q;x++)for(auto y:roots[POW4[x]]){
  pts.emplace_back(x,y);
  onC[x*Q+y]=1;
 }
 onC[NL-1]=1;
}
int main(){
 makefield();
 for(int a=1;a<Q;a++)assert(mu(a,INV[a])==1);
 for(int a=0;a<Q;a++)assert(ad(POW3[a],a)==ad(mu(mu(a,a),a),a));
 vector<pair<I,I>> affine;
 vector<uint8_t> onC(NL,0);
 pointcurve(affine,onC);
 assert(affine.size()==891);
 printf("FIELD 3^6 polynomial=t^6+t+2; CURVE %zu\n",affine.size()+1);
 vector<uint8_t> incidence(NL,0),paircounts(NL,0);
 for(auto [x,y]:affine){
  // all 729 nonvertical lines y=m*x+b through (x,y), plus vertical line x=x0
  for(int m=0;m<Q;m++){
   int A=ne(m),B=1,C=su(mu(m,x),y);
   int lid=lineid(A,B,C);
   incidence[lid]++;
  }
  incidence[lineid(1,0,ne(x))]++;
 }
 // Infinity (0:1:0) lies on all verticals and the line at infinity.
 for(int x=0;x<Q;x++)incidence[lineid(1,0,ne(x))]++;
 incidence[NL-1]++;
 map<int,int> curve_intersections;
 for(auto a:incidence){assert(a<=4);curve_intersections[a]++;assert(a==0||a==1||a==2||a==4);}
 printf("LINES incidence values:");for(auto [a,n]:curve_intersections)printf(" (%d,%d)",a,n);puts("");
 // Independent recovery of line incidence from all pairs of curve points.
 for(int i=0;i<(int)affine.size();i++){
  auto [x,y]=affine[i];
  paircounts[lineid(1,0,ne(x))]++;
  for(int j=i+1;j<(int)affine.size();j++){
   auto [u,v]=affine[j];
   int A=su(y,v),B=su(u,x),C=su(mu(x,v),mu(y,u));
   paircounts[lineid(A,B,C)]++;
  }
 }
 for(int l=0;l<NL;l++){
  int n=incidence[l];
  assert((int)paircounts[l]==n*(n-1)/2);
 }
 vector<int> count(NL,0);
 int n4=0;
 for(int lid=0;lid<NL;lid++)if(incidence[lid]==4){
  n4++;
  int A,B,C;
  if(lid<Q2){A=1;B=lid/Q;C=lid%Q;}
  else if(lid<Q2+Q){A=0;B=1;C=lid-Q2;}
  else {A=0;B=0;C=1;}
  if(B){
   int binv=INV[B];
   for(int x=0;x<Q;x++){
    int y=mu(ne(ad(mu(A,x),C)),binv);
    count[x*Q+y]++;
   }
   count[Q2+mu(ne(A),binv)]++;
  }else if(A){
   int x=mu(ne(C),INV[A]);
   for(int y=0;y<Q;y++)count[x*Q+y]++;
   count[NL-1]++;
  }else{
   for(int y=0;y<Q;y++)count[Q2+y]++;
   count[NL-1]++;
  }
 }
 map<int,int> spectrum_ext,spectrum_curve;
 int minout=999,maxout=0,uncovered=0;
 for(int p=0;p<NL;p++){
  if(onC[p])spectrum_curve[count[p]]++;
  else {spectrum_ext[count[p]]++;minout=min(minout,count[p]);maxout=max(maxout,count[p]);if(!count[p])uncovered++;}
 }
 // The fixed locus of ninth-power Frobenius is the subplane PG(2,9).
 int nsub=0,nsubcurve=0,nsubext=0;
 for(int x=0;x<Q;x++)if(powe(x,9)==x){
  for(int y=0;y<Q;y++)if(powe(y,9)==y){
   int id=x*Q+y;nsub++;
   if(onC[id]){nsubcurve++;assert(count[id]==297);}
   else {nsubext++;assert(count[id]==222);}
  }
  int id=Q2+x;nsub++;
  if(onC[id]){nsubcurve++;assert(count[id]==297);}
  else {nsubext++;assert(count[id]==222);}
 }
 nsub++;nsubcurve++;assert(count[NL-1]==297);
 assert(nsub==91 && nsubcurve==28 && nsubext==63);
 assert(spectrum_ext[222]==nsubext);
 printf("SUBFIELD_PG2_F9 all=%d curve=%d exterior=%d (exterior four-secant multiplicity 222)\n",nsub,nsubcurve,nsubext);
 printf("FOUR_SECANT_LINES %d\n",n4);
 printf("SPECTRUM_EXTERIOR min=%d max=%d uncovered=%d\n",minout,maxout,uncovered);
 for(auto [v,n]:spectrum_ext)printf(" EX %d %d\n",v,n);
 for(auto [v,n]:spectrum_curve)printf(" CURVE %d %d\n",v,n);
 long long incidences=0;for(int p=0;p<NL;p++)incidences+=count[p];
 assert(incidences==1ll*n4*(Q+1));
 int total=0;for(auto [v,n]:spectrum_ext)total+=n;assert(total==NL-892);
 puts("VERIFY_OK");
}
