/* Min weight of GF3-row space of a 36x36 (0,1)-design matrix.
   Steps: row-reduce mod 3 to find rank r and basis (r x 36); if r != 18 report;
   else systematic + MITM as in minweight.c (generalized to r=18 basis). */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif
#define N 36
#define H 9
#define NPOW 19683
static inline void pack36(const uint8_t *v, uint64_t *lo, uint64_t *hi) {
    uint64_t l=0,h=0;
    for (int i=0;i<N;i++){ if(v[i]&1) l|=(1ULL<<i); if(v[i]&2) h|=(1ULL<<i); }
    *lo=l; *hi=h;
}
int main(int argc, char **argv) {
    if (argc<2){fprintf(stderr,"usage: %s design36.txt\n",argv[0]);return 2;}
    uint8_t D[N][N];
    FILE *f=fopen(argv[1],"r"); if(!f){perror("open");return 1;}
    for(int i=0;i<N;i++)for(int j=0;j<N;j++){int x;if(fscanf(f,"%d",&x)!=1){fprintf(stderr,"parse fail\n");return 1;}D[i][j]=((x%3)+3)%3;}
    fclose(f);
    // RREF to get rank + basis rows (row space basis = nonzero RREF rows)
    uint8_t R[N][N]; memcpy(R,D,sizeof(R));
    int pivcol[N]; int row=0;
    for(int col=0;col<N && row<N;col++){
        int sel=-1; for(int i=row;i<N;i++) if(R[i][col]){sel=i;break;}
        if(sel<0)continue;
        if(sel!=row){for(int j=0;j<N;j++){uint8_t t=R[sel][j];R[sel][j]=R[row][j];R[row][j]=t;}}
        if(R[row][col]==2)for(int j=0;j<N;j++)R[row][j]=(R[row][j]*2)%3;
        for(int i=0;i<N;i++){if(i!=row&&R[i][col]){uint8_t f2=R[i][col];for(int j=0;j<N;j++)R[i][j]=(R[i][j]+3-f2*R[row][j]%3)%3;}}
        pivcol[row]=col;row++;
    }
    int r=row;
    printf("RANK %d\n",r);
    if(r!=18)return 0;
    uint8_t B[18][N];
    for(int i=0;i<18;i++)memcpy(B[i],R[i],N);
    // systematic on B
    int isp[N]; memset(isp,0,sizeof(isp));
    for(int i=0;i<18;i++)isp[pivcol[i]]=1;
    int P[N];int p=0;
    for(int i=0;i<18;i++)P[p++]=pivcol[i];
    for(int j=0;j<N;j++)if(!isp[j])P[p++]=j;
    uint8_t Gs[18][N];
    for(int k=0;k<18;k++){int col=P[k];int rf=-1;for(int i=0;i<18;i++)if(R[i][col]==1){rf=i;break;}if(rf<0){printf("internal\n");return 1;}for(int j=0;j<N;j++)Gs[k][j]=R[rf][P[j]];}
    for(int i=0;i<18;i++)for(int j=0;j<18;j++){if(Gs[i][j]!=(i==j)){printf("not systematic\n");return 1;}}
    uint8_t A[18][N-18];
    for(int i=0;i<18;i++)for(int j=0;j<N-18;j++)A[i][j]=Gs[i][18+j];
    static uint64_t L1lo[NPOW],L1hi[NPOW],L2lo[NPOW],L2hi[NPOW];
    static uint8_t pw[NPOW][H];
    for(int i=0;i<NPOW;i++){int t=i;for(int j=0;j<H;j++){pw[i][j]=t%3;t/=3;}}
    for(int i=0;i<NPOW;i++){
        uint8_t v[N];memset(v,0,sizeof(v));
        for(int j=0;j<H;j++)v[j]=pw[i][j];
        for(int j=0;j<N-18;j++){int s=0;for(int q=0;q<H;q++)s+=pw[i][q]*A[q][j];v[18+j]=s%3;}
        pack36(v,&L1lo[i],&L1hi[i]);
    }
    for(int i=0;i<NPOW;i++){
        uint8_t v[N];memset(v,0,sizeof(v));
        for(int j=0;j<H;j++)v[H+j]=pw[i][j];
        for(int j=0;j<N-18;j++){int s=0;for(int q=0;q<H;q++)s+=pw[i][q]*A[H+q][j];v[18+j]=s%3;}
        pack36(v,&L2lo[i],&L2hi[i]);
    }
    long minw=N+1;
#pragma omp parallel for schedule(static) reduction(min:minw)
    for(int i=0;i<NPOW;i++){
        uint64_t a0=L1lo[i],a1=L1hi[i];
        for(int j=0;j<NPOW;j++){
            uint64_t b0=L2lo[j],b1=L2hi[j];
            uint64_t bit0=a0^b0,c1=a0&b0,bit1=a1^b1^c1,bit2=(a1&b1)|(c1&(a1^b1));
            uint64_t three=bit1&bit0&~bit2;
            uint64_t slo=(bit0&~three)|bit2,shi=bit1&~three;
            long w=__builtin_popcountll(slo|shi);
            if(w==0)continue;
            if(w<minw)minw=w;
        }
    }
    printf("MINWEIGHT %ld\n",minw);
    return 0;
}
