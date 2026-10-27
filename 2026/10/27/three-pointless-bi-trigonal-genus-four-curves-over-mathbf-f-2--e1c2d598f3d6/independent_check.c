#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
const int mod[7]={0,3,7,11,19,37,67};
static inline int mul(int a,int b,int d){int r=0; while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&(1<<d))a^=mod[d];}return r;}
static inline int power(int a,int n,int d){int v=1;while(n--)v=mul(v,a,d);return v;}
static int test_sing(int m,int d){int q=1<<d;
for(int chart=0;chart<4;chart++)for(int x=0;x<q;x++)for(int y=0;y<q;y++){
 int F=0,Fx=0,Fy=0;for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(m&(1<<(4*i+j))){int ex=(chart&1)?3-i:i;int ey=(chart&2)?3-j:j;F^=mul(power(x,ex,d),power(y,ey,d),d);if(ex&1)Fx^=mul(power(x,ex-1,d),power(y,ey,d),d);if(ey&1)Fy^=mul(power(x,ex,d),power(y,ey-1,d),d);}
 if(!(F|Fx|Fy))return 1;}
return 0;}
int main(){int count=0,singular[7]={0};for(int m=0;m<(1<<16);m++){int empty=1;for(int x=0;x<3&&empty;x++)for(int y=0;y<3&&empty;y++){int v=0;for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(m&(1<<(4*i+j))){int v1=x==0 ? i==0 : x==1? 1 :i==3;int v2=y==0 ?j==0 : y==1?1:j==3; v^=(v1&v2);}if(!v)empty=0;}if(!empty)continue;
int bad=0;for(int d=1;d<=6&&!bad;d++){if(test_sing(m,d)){bad=1;singular[d]++;}}
if(!bad){count++;printf("%04x\n",m);}}
fprintf(stderr,"smooth (no singular through degree6)=%d; first-degrees:",count);for(int d=1;d<=6;d++)fprintf(stderr," %d:%d",d,singular[d]);fputc('\n',stderr);return 0;}
