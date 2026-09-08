#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <omp.h>

static int rowmasks[35];
static int nrowmasks;
static inline int pc(int x){ return __builtin_popcount((unsigned)x); }

static inline int ryser_perm(const int *r){
    long s = 0;
    for(int S=1; S<128; S++){
        int bits = pc(S);
        long prod = 1;
        for(int i=0;i<7;i++){
            int c = pc(r[i] & S);
            if(c==0){ prod=0; break; }
            prod *= c;
        }
        if(bits & 1) s -= prod; else s += prod;
    }
    return (int)(-s);
}

int main(){
    nrowmasks=0;
    for(int m=0;m<128;m++) if(pc(m)==3) rowmasks[nrowmasks++]=m;
    int R0 = 7; // 0b0000111 canonical first row
    long long tc[35]; memset(tc,0,sizeof(tc));
    int lmin[35]; int lwit[35][7]; static long long lh[35][200];
    for(int i=0;i<35;i++){ lmin[i]=1000000; }

#pragma omp parallel for schedule(dynamic)
    for(int i1=0;i1<35;i1++){
        int rows[7]; rows[0]=R0; rows[1]=rowmasks[i1];
        int colsum[7]; for(int j=0;j<7;j++) colsum[j]=((R0>>j)&1)+((rowmasks[i1]>>j)&1);
        int ok0=1; for(int j=0;j<7;j++) if(colsum[j]>3) ok0=0;
        long long mycount=0; int mymin=1000000; int mywit[7]={0};
        long long myh[200]; memset(myh,0,sizeof(myh));
        if(ok0){
            int ch[7]; ch[0]=R0; ch[1]=rowmasks[i1];
            int ptr[8]; for(int d=0;d<8;d++) ptr[d]=0;
            int depth=2; ptr[2]=0;
            while(depth>=2){
                if(depth==7){
                    int ok=1;
                    for(int j=0;j<7;j++) if(colsum[j]!=3){ok=0;break;}
                    if(ok){
                        int p = ryser_perm(rows);
                        mycount++;
                        if(p<200) myh[p]++;
                        if(p<mymin){mymin=p; memcpy(mywit,rows,sizeof(rows));}
                    }
                    depth--; if(depth>=2){ int m=ch[depth]; for(int j=0;j<7;j++) colsum[j]-=((m>>j)&1); ptr[depth]++; }
                    continue;
                }
                if(ptr[depth]>=35){
                    ptr[depth]=0; depth--;
                    if(depth>=2){ int m=ch[depth]; for(int j=0;j<7;j++) colsum[j]-=((m>>j)&1); ptr[depth]++; }
                    continue;
                }
                int m = rowmasks[ptr[depth]];
                int rem = 6 - depth;
                int ok=1;
                for(int j=0;j<7;j++){ int b=(m>>j)&1; if(colsum[j]+b>3){ok=0;break;} if(colsum[j]+b+rem<3){ok=0;break;} }
                if(!ok){ ptr[depth]++; continue; }
                ch[depth]=m; rows[depth]=m;
                for(int j=0;j<7;j++) colsum[j]+=((m>>j)&1);
                depth++; if(depth<7) ptr[depth]=0;
            }
        }
        tc[i1]=mycount; lmin[i1]=mymin; memcpy(lwit[i1],mywit,sizeof(mywit)); memcpy(lh[i1],myh,sizeof(myh));
#pragma omp critical
        { printf("row1 %d mask %d done count %lld min %d\n", i1, rowmasks[i1], mycount, mymin); fflush(stdout); }
    }
    long long sub=0; for(int i=0;i<35;i++) sub+=tc[i];
    printf("SUBTOTAL(row0 fixed) %lld  TOTAL(x35) %lld\n", sub, sub*35);
    int gm=1000000; int gi=0;
    long long gh[200]; memset(gh,0,sizeof(gh));
    for(int i=0;i<35;i++){ for(int p=0;p<200;p++) gh[p]+=lh[i][p]; if(lmin[i]<gm){gm=lmin[i];gi=i;} }
    printf("MIN %d from row1 %d\n", gm, gi);
    printf("WIT: "); for(int r=0;r<7;r++) printf("%d ", lwit[gi][r]); printf("\n");
    printf("HIST-SUB:\n");
    for(int p=0;p<200;p++) if(gh[p]) printf("%d:%lld (sub, x35=%lld)\n", p, gh[p], gh[p]*35);
    return 0;
}
