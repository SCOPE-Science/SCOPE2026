// Exact cyclotomic zero-pattern census on the prime-field parabola; public scientific checker.
// Compile: g++ -std=c++17 -O3 verify_p11.cpp -o verify_p11
#include <array>
#include <set>
#include <cstdio>
#include <cstdint>
#include <algorithm>
#include <iostream>
using namespace std;
constexpr int p=11;
using Cyc=array<int16_t,p>;
struct Seed {int e[3][4][2];};
const int reps[6][5]={{0,1,2,3,4},{0,1,2,3,5},{0,1,2,3,6},{0,1,2,3,7},{0,1,2,4,5},{0,1,2,4,7}};
const int repsz[6]={55,110,110,55,110,22};
int rem(int a){a%=p;return a<0?a+p:a;}
void determinant(Cyc &out,const Seed &s,int omit){
 int keep[3],k=0;for(int j=0;j<4;j++)if(j!=omit)keep[k++]=j;
 // Six permutations, each product of three binomials with eight terms.
 static const int perm[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
 static const int parity[6]={1,-1,-1,1,1,-1};
 out.fill(0);
 for(int n=0;n<6;n++)for(int mask=0;mask<8;mask++){
  int ex=0,sgn=parity[n];
  for(int i=0;i<3;i++){
   int c=keep[perm[n][i]],choice=(mask>>i)&1;
   ex+=s.e[i][c][choice];
   if(choice)sgn=-sgn;
  }
  out[rem(ex)]+=sgn;
 }
 if(omit&1)for(auto &v:out)v=-v;
}
int main(){
 // Exhaustive verification that the six representatives partition all 462 supports.
 int actualsz[6]={0};int allsupports=0;
 for(int x0=0;x0<7;x0++)for(int x1=x0+1;x1<8;x1++)
 for(int x2=x1+1;x2<9;x2++)for(int x3=x2+1;x3<10;x3++)
 for(int x4=x3+1;x4<11;x4++){
  int xs[5]={x0,x1,x2,x3,x4};int hit=-1;
  for(int o=0;o<6;o++){
   bool in=false;
   for(int u=1;u<11 && !in;u++)for(int v=0;v<11 && !in;v++){
    int tr[5];for(int j=0;j<5;j++)tr[j]=rem(u*reps[o][j]+v);
    sort(tr,tr+5);
    in=equal(tr,tr+5,xs);
   }
   if(in){if(hit>=0){fprintf(stderr,"Overlapping support orbits!\n");return 3;}hit=o;}
  }
  if(hit<0){fprintf(stderr,"Missing support orbit!\n");return 4;}
  actualsz[hit]++;allsupports++;
 }
 if(allsupports!=462){fprintf(stderr,"Wrong support number!\n");return 5;}
 for(int o=0;o<6;o++)if(actualsz[o]!=repsz[o]){fprintf(stderr,"Wrong orbit size!\n");return 6;}
 long long final_total=0;
 for(int oi=0;oi<6;oi++){
  const int *X=reps[oi];
  int expo[121][5];
  for(int a=0;a<p;a++)for(int b=0;b<p;b++)for(int j=0;j<5;j++)expo[a*p+b][j]=rem(a*X[j]*X[j]+b*X[j]);
  int e[121][4][2];
  for(int r=0;r<121;r++)for(int j=0;j<4;j++){e[r][j][0]=expo[r][j];e[r][j][1]=expo[r][4];}
  long long rank_drop=0,noncollinear_drop=0,nonfull=0,full=0,six_seeds=0;
  set<array<uint8_t,6>> exact_zero_sets;
  int max_zeros=0;
  Seed s;
  for(int a=1;a<119;a++)for(int b=a+1;b<120;b++)for(int c=b+1;c<121;c++){
   const int idx[3]={a,b,c};
   for(int t=0;t<3;t++)for(int j=0;j<4;j++)for(int u=0;u<2;u++)s.e[t][j][u]=e[idx[t]][j][u];
   Cyc coeff[5];bool rank4=false,fullsupport=true;
   for(int j=0;j<4;j++){
    determinant(coeff[j],s,j);
    for(int k=0;k<p;k++)if(coeff[j][k])rank4=true;
   }
   if(!rank4){
    rank_drop++;
    int aa=a/p,ab=a%p,ba=b/p,bb=b%p,ca=c/p,cb=c%p;
    if(rem(aa*bb-ba*ab)||rem(aa*cb-ca*ab))noncollinear_drop++;
    continue;
   }
   coeff[4].fill(0);
   for(int j=0;j<4;j++)for(int k=0;k<p;k++)coeff[4][k]-=coeff[j][k];
   for(int j=0;j<5;j++){bool nz=false;for(int k=0;k<p;k++)if(coeff[j][k])nz=true;if(!nz)fullsupport=false;}
   if(!fullsupport){nonfull++;continue;}
   full++;
   array<uint8_t,6> z{};int count=0;
   for(int r=0;r<121;r++){
    int16_t v[p]={0};
    for(int j=0;j<5;j++){
     int sh=expo[r][j];
     for(int k=0;k<p;k++)v[(k+sh)%p]+=coeff[j][k];
    }
    bool iszero=true;for(int k=0;k<p;k++)if(v[k]){iszero=false;break;}
    if(iszero){if(count<6)z[count]=r;count++;}
   }
   if(count>max_zeros)max_zeros=count;
   if(count==6){six_seeds++;exact_zero_sets.insert(z);}
  }
  long long n0=exact_zero_sets.size();
  if((n0*121)%6){fprintf(stderr,"Nonintegral orbit count!\n");return 2;}
  if(noncollinear_drop){fprintf(stderr,"Non-collinear rank loss!\n");return 7;}
  long long per_support=n0*121/6;
  final_total+=per_support*repsz[oi];
  printf("orbit=%d support=(%d,%d,%d,%d,%d) orbit_supports=%d rankdrop=%lld noncollinear_rankdrop=%lld nonfull=%lld full=%lld seeds6=%lld zero_origin_rays=%lld rays_per_support=%lld max_zeros=%d\n",oi,X[0],X[1],X[2],X[3],X[4],repsz[oi],rank_drop,noncollinear_drop,nonfull,full,six_seeds,n0,per_support,max_zeros);
 }
 if(final_total!=532400){fprintf(stderr,"Unexpected census total!\n");return 8;}
 printf("VERIFY_OK exact cyclotomic census: 462 supports; six affine orbits; 532400 sharp projective rays\n");
 printf("TOTAL_PROJECTIVE_RAYS=%lld\n",final_total);
}
