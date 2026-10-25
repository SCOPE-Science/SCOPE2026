/* Reproducible exhaustive finite-field incidence count; only mathematical data. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#define MAXP 350
#define MAXMASK 15
struct mon {int i,j,k;};
struct mon mon[18];int nm=0;
struct mon all5[21],all2[6],all1[3],all3[10],all4[15];
int nall5=0,nall2=0,nall1=0,nall3=0,nall4=0;
uint32_t basis[70][21];int divisor_total=0;
void init_degrees(){for(int d=1;d<=5;d++)for(int i=0;i<=d;i++)for(int j=0;j<=d-i;j++){
 struct mon x={i,j,d-i-j};
 if(d==1)all1[nall1++]=x;else if(d==2)all2[nall2++]=x;else if(d==3)all3[nall3++]=x;else if(d==4)all4[nall4++]=x;else all5[nall5++]=x;
}}
int full_id(int i,int j,int k){for(int t=0;t<21;t++)if(all5[t].i==i&&all5[t].j==j&&all5[t].k==k)return t;return -1;}
void basis_insert(uint32_t *b,uint32_t x){for(int j=20;j>=0;j--)if((x>>j)&1){if(b[j])x^=b[j];else{b[j]=x;break;}}}
void prepare_divisors(){init_degrees();for(int d=1;d<=2;d++){
 struct mon *mons=d==1?all1:all2;int nd=d==1?3:6;struct mon *quo=d==1?all4:all3;int nq=d==1?15:10;
 for(int g=1;g<(1<<nd);g++){
 uint32_t *b=basis[divisor_total++];
 for(int t=0;t<nq;t++){uint32_t x=0;for(int j=0;j<nd;j++)if((g>>j)&1){int p=full_id(mons[j].i+quo[t].i,mons[j].j+quo[t].j,mons[j].k+quo[t].k);x^=(uint32_t)1<<p;}basis_insert(b,x);}
 }
 }if(divisor_total!=70){fprintf(stderr,"bad divisors %d\n",divisor_total);exit(4);}}
int reducible(uint32_t m){uint32_t f=0;for(int t=0;t<nm;t++)if((m>>t)&1)f ^= (uint32_t)1<<full_id(mon[t].i,mon[t].j,mon[t].k);
 for(int d=0;d<divisor_total;d++){
 uint32_t r=f;for(int j=20;j>=0;j--)if((r>>j)&1 && basis[d][j])r ^= basis[d][j];
 if(!r)return 1;
 }return 0;}

struct point {uint32_t eq[MAXMASK];int ne,n;};
struct point p[MAXP]; int np=0;
int irr[6]={0,3,7,11,19,37};
int mul[32][32],qsize;
int gf_mul(int a,int b,int n){int v=0,q=1<<n; while(b){if(b&1)v^=a; b>>=1; a<<=1; if(a&q)a^=irr[n];}return v;}
void makemul(int n){qsize=1<<n;for(int i=0;i<qsize;i++)for(int j=0;j<qsize;j++)mul[i][j]=gf_mul(i,j,n);}
int fpow(int a,int k){int r=1;while(k--){r=mul[r][a];}return r;}
int orb_len(int a,int b,int n){int q=1<<n, a0=a,b0=b; int d=0; do{a=mul[a][a];b=mul[b][b];d++;if(d>n){fprintf(stderr,"bad Frobenius orbit\n");exit(5);}}while(a!=a0||b!=b0);return d;}
int is_min(int a,int b,int n){int aa=a,bb=b, q=1<<n, key=a*q+b;for(int i=1;i<n;i++){aa=mul[aa][aa];bb=mul[bb][bb];if(aa*q+bb<key)return 0;}return 1;}
void putpoint(int x,int y,int z,int n){if(np>=MAXP){fprintf(stderr,"point capacity exceeded\n");exit(2);}struct point *v=&p[np];memset(v,0,sizeof(*v));v->n=n;v->ne=3*n;
for(int h=0;h<nm;h++){
 int i=mon[h].i,j=mon[h].j,k=mon[h].k;
 int dx=(i&1)?mul[mul[fpow(x,i-1)][fpow(y,j)]][fpow(z,k)]:0;
 int dy=(j&1)?mul[mul[fpow(x,i)][fpow(y,j-1)]][fpow(z,k)]:0;
 int dz=(k&1)?mul[mul[fpow(x,i)][fpow(y,j)]][fpow(z,k-1)]:0;
 for(int bit=0;bit<n;bit++){
   if((dx>>bit)&1)v->eq[bit]|=1u<<h;
   if((dy>>bit)&1)v->eq[n+bit]|=1u<<h;
   if((dz>>bit)&1)v->eq[2*n+bit]|=1u<<h;
 }
}np++;
}
void generate(){for(int n=1;n<=5;n++){makemul(n);int q=qsize;int before=np;
 for(int a=0;a<q;a++)for(int b=0;b<q;b++)if(orb_len(a,b,n)==n && is_min(a,b,n))putpoint(1,a,b,n);
 for(int b=0;b<q;b++)if(orb_len(1,b,n)==n && is_min(1,b,n))putpoint(0,1,b,n);
 /* center [0:0:1] is singular by hypothesis, so omit */
 printf("degree %d closed points: %d\n",n,np-before);
} }
int idx(int a,int b,int c){for(int i=0;i<nm;i++)if(mon[i].i==a&&mon[i].j==b&&mon[i].k==c)return i;return -1;}
int term(uint32_t mask,int a,int b,int c){int id=idx(a,b,c);return id>=0 && ((mask>>id)&1);}
int parity(uint32_t x){return __builtin_parity(x);}
int type(uint32_t m){int a=term(m,2,0,3), b=term(m,1,1,3),c=term(m,0,2,3);if(b)return (a&&c)?2:1;
 if(a+c==0)return 0;
 int v=0;
 if(a&&c){for(int i=0;i<=3;i++)v^=term(m,i,3-i,2);}
 else if(a)v=term(m,0,3,2);
 else v=term(m,3,0,2);
 return v?3:0;
}
int residual(uint32_t m,int ux,int uy){int v=0;for(int h=0;h<nm;h++)if((m>>h)&1){int i=mon[h].i,j=mon[h].j;if((!i||ux)&&(!j||uy))v^=1<<(i+j-2);}return v;}
int fiber_type(int v){int z=((v&1)==0)+((v&8)==0)+(__builtin_parity((unsigned)v)==0); // rational roots
 if(z==0)return 0; // irreducible cubic
 if(z==3)return 4; // three simple
 if(z==2)return 3; // 2+1 with double root
 if(v==1||v==8||v==15)return 2; // triple rational root
 return 1; // rational simple + irreducible quadratic
}
int rational_fiber(uint32_t m,int ux,int uy){int k=fiber_type(residual(m,ux,uy));int cnt[5]={0,1,1,2,3};return cnt[k];}
int issing(uint32_t m,struct point *v){for(int j=0;j<v->ne;j++)if(parity(m & v->eq[j]))return 0;return 1;}
int main(){for(int i=0;i<=5;i++)for(int j=0;j<=5-i;j++){int k=5-i-j;if(k==5 || (i==1&&j==0&&k==4) || (i==0&&j==1&&k==4))continue;mon[nm++]=(struct mon){i,j,k};}if(nm!=18){fprintf(stderr,"bad nm %d\n",nm);return 1;}generate();prepare_divisors();int initial=np;
 int profiles[4][5][5][5]={0}, ram_count[4][4]={0};int rejected[6]={0}, red[4]={0},qualified[4]={0}, counts[4][10]={0},fiber[4][4][4][4]={0},accepted=0;
 for(uint32_t m=0;m<(1u<<18);m++){
 int t=type(m);if(!t)continue;qualified[t]++;
 int fail=0;for(int k=0;k<np;k++){
   if(issing(m,&p[k])){fail=p[k].n;break;}
 }
 if(fail){rejected[fail]++;continue;}
 if(reducible(m)){red[t]++;continue;}
 accepted++;int a=rational_fiber(m,1,0),b=rational_fiber(m,0,1),c=rational_fiber(m,1,1),N=a+b+c;
 int v[3]={a,b,c};for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(v[j]<v[i]){int h=v[j];v[j]=v[i];v[i]=h;}
 counts[t][N]++;fiber[t][v[0]][v[1]][v[2]]++;
 int w[3]={fiber_type(residual(m,1,0)),fiber_type(residual(m,0,1)),fiber_type(residual(m,1,1))};
 int rr=0;for(int i=0;i<3;i++)rr+=(w[i]==2||w[i]==3);for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(w[j]<w[i]){int tmp=w[j];w[j]=w[i];w[i]=tmp;}ram_count[t][rr]++;profiles[t][w[0]][w[1]][w[2]]++;
 }
 printf("remaining reducible type 1 2 3: %d %d %d\n",red[1],red[2],red[3]);
 printf("candidate by local type split,nonsplit,cusp: %d %d %d\n",qualified[1],qualified[2],qualified[3]);
 printf("rejected by first singular degree 1..5: %d %d %d %d %d\n",rejected[1],rejected[2],rejected[3],rejected[4],rejected[5]);
 printf("total accepted fixed center: %d; global forms: %d; weighted moduli: %d/24 = %.6f\n",accepted,accepted*7,accepted,accepted/24.0);
 for(int t=1;t<=3;t++) {printf("type %d count-by-rational-points:",t);for(int i=0;i<10;i++)if(counts[t][i])printf(" %d:%d",i,counts[t][i]);printf("\n");for(int i=0;i<4;i++)for(int j=i;j<4;j++)for(int k=j;k<4;k++)if(fiber[t][i][j][k])printf("fiber %d %d-%d-%d %d\n",t,i,j,k,fiber[t][i][j][k]);}
 printf("all rational-fiber splitting profiles; types I3=0, LQ=1, L3=2, L2L=3, LLL=4\n");
 for(int t=1;t<=3;t++){
 printf("rational ramified base-fiber counts for source type %d: %d %d %d %d\n",t,ram_count[t][0],ram_count[t][1],ram_count[t][2],ram_count[t][3]);
 for(int i=0;i<5;i++)for(int j=i;j<5;j++)for(int k=j;k<5;k++)if(profiles[t][i][j][k])printf("profile %d %d %d %d count %d\n",t,i,j,k,profiles[t][i][j][k]);
 }
 return 0;
}
