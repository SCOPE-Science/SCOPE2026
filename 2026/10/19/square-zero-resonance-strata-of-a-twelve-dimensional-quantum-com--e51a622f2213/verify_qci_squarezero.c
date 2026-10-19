/* Exhaustive independent associative-algebra multiplication check.
   Quantum complete intersection: x^3=y^4=0, yx=t xy.
   Coordinates enumerate all degree 2 and degree 3 parts; higher degrees are free. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static int mult(int a, int b, int q, int ext) {
  if (!ext) return (a*b)%q;
  /* GF(4), alpha^2=alpha+1, bit-coded */
  int r=0; for(int k=0;k<2;k++)if((b>>k)&1)r^=a<<k;
  if(r&8)r^=0xC;
  if(r&4)r^=0x7;
  return r;
}
static int add(int a,int b,int q,int ext){return ext?a^b:(a+b)%q;}
static int field_pow(int a,int e,int q,int ext){int r=1;for(int i=0;i<e;i++)r=mult(r,a,q,ext);return r;}
static int sqrzero(const int *a,int t,int q,int ext){
  const int ii[6]={2,1,0,2,1,0}, jj[6]={0,1,2,1,2,3};
  int out[3]={0};
  for(int r=0;r<6;r++)for(int s=0;s<6;s++){
    if(ii[r]+ii[s]>2||jj[r]+jj[s]>3)continue;
    int I=ii[r]+ii[s],J=jj[r]+jj[s];
    int idx = (I==2&&J==2)?0:(I==1&&J==3)?1:(I==2&&J==3)?2:-1;
    if(idx<0){fprintf(stderr,"unexpected term %d %d\n",I,J);exit(7);}
    int z=mult(mult(a[r],a[s],q,ext),field_pow(t,jj[r]*ii[s],q,ext),q,ext);
    out[idx]=add(out[idx],z,q,ext);
  }
  return !(out[0]||out[1]||out[2]);
}
static long long predicted(int q,int t,int ext){
 int one=1, c1=add(one,field_pow(t,4,q,ext),q,ext);
 int c2=add(one,field_pow(t,2,q,ext),q,ext);
 int c3=add(one,field_pow(t,6,q,ext),q,ext);
 long long base=0, z=0;
 if(!c2 && c1 && !ext && q%2==1){base=(long long)q*q;z=q;}
 else if(!c1 && c2){base=(long long)q*q;z=q;}
 else if(!c1&&!c2){base=(long long)q*q;z=(!c3?q*q:q);}
 else {base=2*q-1;z=!c3?q:1;}
 long long q5=1;for(int i=0;i<5;i++)q5*=q;
 return q5*(base+(q-1)*z);
}
static void test(int q,int t,int ext){
 int x[6],total=1;for(int i=0;i<6;i++)total*=q;
 long long count=0;
 for(int m=0;m<total;m++){
  int v=m;
  for(int i=0;i<6;i++){x[i]=v%q;v/=q;}
  count+=sqrzero(x,t,q,ext);
 }
 long long free=1;for(int i=0;i<3;i++)free*=q;
 long long got=count*free,exp=predicted(q,t,ext);
 printf("q=%d parameter=%d ext=%d core=%lld solutions=%lld expected=%lld %s\n",q,t,ext,count,got,exp,got==exp?"PASS":"FAIL");
 if(got!=exp)exit(1);
}
int main(){
 test(2,1,0);
 test(3,1,0); test(3,2,0);
 test(4,2,1); test(4,3,1); test(4,1,1);
 for(int t=1;t<5;t++)test(5,t,0);
 test(13,2,0); /* 12th root: lambda^6=-1, lambda^2 != -1 */
 test(13,5,0); /* lambda^2=-1 */
 test(17,2,0); /* lambda^4=-1 */
 puts("VERIFY_OK");return 0;
}
