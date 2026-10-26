#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
static const int poly[]={0,0x3,0x7,0xb,0x13,0x25,0x43,0x83,0x11b,0x203,0x409,0x805,0x1009};
static int mult(int a,int b,int m,int irr){int z=0,top=1<<m;while(b){if(b&1)z^=a;b>>=1;a<<=1;if(a&top)a^=irr;}return z;}
int main(int argc,char**argv){int max=argc>1?atoi(argv[1]):12;for(int m=1;m<=max;m++){int q=1<<m,*cub=calloc(q,sizeof(int)),*chi=calloc(q,sizeof(int));
for(int a=0;a<q;a++){cub[a]=mult(mult(a,a,m,poly[m]),a,m,poly[m]);int tr=0,b=a;for(int i=0;i<m;i++){tr^=b;b=mult(b,b,m,poly[m]);}if(tr!=0&&tr!=1){fprintf(stderr,"invalid trace %d\n",tr);return 1;}chi[a]=1-2*tr;}
long long S=0;for(int y=0;y<q;y++){int y3=cub[y];for(int z=0;z<q;z++) S+=chi[y ^ mult(y3,z,m,poly[m]) ^ cub[z]];}
long long nx=(long long)q*q+q+1+S;
int s= ((m%2)==0?2:0)+((m%3)==0?6:0)+((m%6)==0?6:0); // 2 + 3+3 +6 orbit lengths
long long ny=nx+(long long)q*s;
long long trace=ny-1-(long long)q*q;
if((trace%q)!=0){fprintf(stderr,"nondivisible n%d trace%lld q%d\n",m,trace,q);return 1;}
printf("m=%d q=%d S=%lld X=%lld singular_rational=%d Y=%lld trH2=%lld normalized_trace=%lld\n",m,q,S,nx,s,ny,trace,trace/q);
free(cub);free(chi);}
return 0;}
