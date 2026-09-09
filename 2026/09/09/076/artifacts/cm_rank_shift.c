// Independent exact-rational + independent double-check utilities are in Python;
// this is the same C kernel recompiled with a coordinate shift to get a
// SECOND independent specialization of the target (guards against any
// artifact-specific fluke). Shift passed as argv[4].
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#ifdef _OPENMP
#include <omp.h>
#endif

#define P 251

static uint8_t MULT[P*P];
static int INV[P];
static int modpow(int a,int e){ long r=1,b=a; while(e){ if(e&1)r=r*b%P; b=b*b%P; e>>=1;} return (int)r; }

int main(int argc, char**argv){
  int d = argc>1? atoi(argv[1]) : 136;
  int m = argc>2? atoi(argv[2]) : 43;
  int npts = argc>3? atoi(argv[3]) : 10;
  int SH = argc>4? atoi(argv[4]) : 100;
  int px[32], py[32];
  int xs[10]={0,1,2,3,4,5,6,7,8,9};
  int ys[10]={0,2,5,11,7,13,17,23,29,31};
  for(int t=0;t<npts;t++){ px[t]=(xs[t%10]+SH)%P; py[t]=(ys[t%10]+2*SH)%P; }
  // distinctness check mod P
  for(int a=0;a<npts;a++) for(int b=a+1;b<npts;b++)
    if(px[a]==px[b]&&py[a]==py[b]){ printf("POINT COLLISION\n"); return 2; }
  int C=0; for(int i=0;i<=d;i++) for(int j=0;j<=d-i;j++) C++;
  int mm=m-1;
  int per=0; for(int a=0;a<=mm;a++) for(int b=0;b<=mm-a;b++) per++;
  long R=(long)per*npts;
  printf("d=%d m=%d npts=%d shift=%d C=%d per=%d R=%ld P=%d\n",d,m,npts,SH,C,per,R,P);
  for(int a=0;a<P;a++) for(int b=0;b<P;b++) MULT[a*P+b]=(uint8_t)((a*b)%P);
  for(int a=1;a<P;a++) INV[a]=modpow(a,P-2);
  int *mi=(int*)malloc(C*sizeof(int)), *mj=(int*)malloc(C*sizeof(int));
  int c=0; for(int i=0;i<=d;i++) for(int j=0;j<=d-i;j++){ mi[c]=i; mj[c]=j; c++; }
  int *pwx = (int*)malloc(npts*(d+1)*sizeof(int));
  int *pwy = (int*)malloc(npts*(d+1)*sizeof(int));
  for(int t=0;t<npts;t++){
    pwx[t*(d+1)+0]=1; for(int e=1;e<=d;e++) pwx[t*(d+1)+e]=(pwx[t*(d+1)+e-1]*px[t])%P;
    pwy[t*(d+1)+0]=1; for(int e=1;e<=d;e++) pwy[t*(d+1)+e]=(pwy[t*(d+1)+e-1]*py[t])%P;
  }
  int *ff=(int*)malloc((d+1)*(m)*sizeof(int));
  for(int e=0;e<=d;e++) for(int a=0;a<=m;a++){
    if(a>e){ ff[e*(m)+a]=0; continue; }
    long v=1; for(int k=e-a+1;k<=e;k++) v=v*k%P; ff[e*(m)+a]=(int)v;
  }
  size_t nC=(size_t)C;
  uint8_t *A=(uint8_t*)malloc((size_t)R*nC);
  if(!A){ printf("OOM\n"); return 1; }
  uint8_t **rows=(uint8_t**)malloc(R*sizeof(uint8_t*));
  for(long r=0;r<R;r++) rows[r]=A+r*nC;
#pragma omp parallel for schedule(static)
  for(long r=0;r<R;r++){
    int t=r/per, s=r%per;
    int a=0,b=s;
    int ss=s;
    for(int aa=0;aa<=mm;aa++){ int cnt=(mm-aa)+1; if(ss<cnt){ a=aa; b=ss; break; } ss-=cnt; }
    uint8_t *row=rows[r];
    int *pwx_t=pwx+t*(d+1), *pwy_t=pwy+t*(d+1);
    for(int cc=0;cc<C;cc++){
      int i=mi[cc], j=mj[cc];
      if(i<a||j<b){ row[cc]=0; continue; }
      int v=(int)((long)ff[i*(m)+a]*ff[j*(m)+b]%P);
      v=(int)((long)v*pwx_t[i-a]%P);
      v=(int)((long)v*pwy_t[j-b]%P);
      row[cc]=(uint8_t)v;
    }
  }
  printf("build done\n"); fflush(stdout);
  int piv=0;
  double w0=omp_get_wtime();
  for(int k=0;k<C;k++){
    int pr=-1;
    for(long i=k;i<R;i++) if(rows[i][k]){ pr=(int)i; break; }
    if(pr<0){ continue; }
    if(pr!=k){ uint8_t *tmp=rows[k]; rows[k]=rows[pr]; rows[pr]=tmp; }
    uint8_t *Rk=rows[k];
    int inv=INV[Rk[k]];
    if(inv!=1){
      uint8_t *Mi=MULT+inv*P;
#pragma omp parallel for schedule(static)
      for(int j=k;j<C;j++) Rk[j]=Mi[Rk[j]];
    }
    Rk=rows[k];
#pragma omp parallel for schedule(static)
    for(long i=k+1;i<R;i++){
      uint8_t *Ri=rows[i];
      int f=Ri[k];
      if(!f) continue;
      uint8_t *Mf=MULT+f*P;
      for(int j=k+1;j<C;j++){
        int v=(int)Ri[j]-(int)Mf[Rk[j]];
        if(v<0) v+=P;
        Ri[j]=(uint8_t)v;
      }
      Ri[k]=0;
    }
    piv++;
    if((k+1)%1000==0||k+1==C){ printf("  col %d/%d piv=%d elapsed=%.1fs\n",k+1,C,piv,omp_get_wtime()-w0); fflush(stdout); }
  }
  printf("PIVOTS=%d C=%d R=%ld => %s\n",piv,C,R,(piv==C?"FULL COLUMN RANK: SYSTEM EMPTY":"RANK DEFICIENT"));
  return 0;
}
