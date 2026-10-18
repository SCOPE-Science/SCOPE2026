/* Exact checks for a matrix square-zero count over a four-dimensional commutative algebra.
   Compile: cc -O3 -std=c11 -Wall -Wextra verify.c -o verify && ./verify */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#define MAXEL 81
static unsigned char addtab[MAXEL][MAXEL], multab[MAXEL][MAXEL];
static int q,lim;
static int mod(int a) {int r=a%q;return r<0?r+q:r;}
static void precompute(int field){
 q=field;lim=q*q*q*q;
 for(int a=0;a<lim;a++)for(int b=0;b<lim;b++){
   int x[4],y[4], aa=a,bb=b;
   for(int i=0;i<4;i++){x[i]=aa%q;aa/=q;y[i]=bb%q;bb/=q;}
   int c[4]={mod(x[0]+y[0]),mod(x[1]+y[1]),mod(x[2]+y[2]),mod(x[3]+y[3])};
   int d[4]={mod(x[0]*y[0]),mod(x[0]*y[1]+x[1]*y[0]),mod(x[0]*y[2]+x[2]*y[0]),mod(x[0]*y[3]+x[3]*y[0]+x[1]*y[2]+x[2]*y[1])};
   addtab[a][b]=(unsigned char)(c[0]+q*c[1]+q*q*c[2]+q*q*q*c[3]);
   multab[a][b]=(unsigned char)(d[0]+q*d[1]+q*q*d[2]+q*q*q*d[3]);
 }
}
static uint64_t predicted(int qq){uint64_t t=qq,t2=t*t,t3=t2*t,t4=t2*t2,t5=t4*t,t6=t3*t3,t7=t6*t,t8=t4*t4,t9=t8*t;
 if(qq%2)return t9+4*t8-2*t7-3*t6+t5;
 return t9*t+t9+t8-t7-t6;
}
static uint64_t direct(void){
 uint64_t total=0;
 for(int a=0;a<lim;a++) for(int d=0;d<lim;d++){
  int s=addtab[a][d], a2=multab[a][a], d2=multab[d][d];
  for(int b=0;b<lim;b++){
   if(multab[s][b])continue;
   for(int c=0;c<lim;c++){
    if(multab[s][c])continue;
    int bc=multab[b][c];
    if(addtab[a2][bc]==0 && addtab[d2][bc]==0)total++;
   }
  }
 }
 return total;
}
static uint64_t anticommuting_count(void){
 uint64_t n=0;
 for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++)
  for(int e=0;e<q;e++)for(int f=0;f<q;f++)for(int g=0;g<q;g++)for(int h=0;h<q;h++){
   if(mod(2*a*e+b*g+f*c)==0 && mod(a*f+b*h+e*b+f*d)==0 &&
      mod(c*e+d*g+g*a+h*c)==0 && mod(c*f+d*h+g*b+h*d)==0)n++;
  }
 return n;
}
int main(void){
 for(int field=2;field<=3;field++){
  precompute(field);uint64_t act=direct(),exp=predicted(field);
  printf("FULL q=%d: observed=%llu expected=%llu\n",field,(unsigned long long)act,(unsigned long long)exp);
  if(act!=exp)return 1;
 }
 for(int field=2;field<=7;field++){
  q=field;
  /* Anticommuting test only over primes; omit composite moduli. */
  if(field==4||field==6)continue;
  uint64_t act=anticommuting_count();
  uint64_t t=field,t2=t*t,t3=t2*t,t4=t2*t2,t5=t4*t;
  uint64_t exp= field==2? t5*t+t5-t3 : t5+3*t4-2*t3-2*t2+t;
  printf("ANTI q=%d: observed=%llu expected=%llu\n",field,(unsigned long long)act,(unsigned long long)exp);
  if(act!=exp)return 2;
 }
 puts("VERIFY_OK");return 0;
}
