#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

#define MAXN 7
#define MAXSUB (1<<MAXN)
#define MAXPERM 5040

static int pairidx[MAXN][MAXN];
static int perms[MAXPERM][MAXN];
static int nperm=0;

static void make_pairidx(int n){
    int k=0;
    for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) pairidx[i][j]=k++;
}

static void genperm_rec(int n,int d,int used,int *p){
    if(d==n){
        for(int i=0;i<n;i++) perms[nperm][i]=p[i];
        nperm++;
        return;
    }
    for(int x=0;x<n;x++) if(!(used&(1<<x))){
        p[d]=x;
        genperm_rec(n,d+1,used|(1<<x),p);
    }
}

static inline int beats(uint32_t t,int a,int b){
    int i=a<b?a:b, j=a<b?b:a;
    int bit=(t>>pairidx[i][j])&1u;
    return a<b ? bit : !bit;
}

static uint32_t uncovered(uint32_t t,int n){
    uint32_t out[MAXN]={0};
    for(int a=0;a<n;a++) for(int b=0;b<n;b++)
        if(a!=b && beats(t,a,b)) out[a]|=1u<<b;

    uint32_t U=0;
    for(int x=0;x<n;x++){
        int covered=0;
        for(int y=0;y<n;y++) if(y!=x && ((out[y]>>x)&1u)){
            if((out[x] & ~out[y])==0){
                covered=1;
                break;
            }
        }
        if(!covered) U|=1u<<x;
    }
    return U;
}

static uint32_t banks(uint32_t t,int n){
    unsigned char trans[MAXSUB]={0};
    signed char top[MAXSUB];
    int lim=1<<n;
    trans[0]=1; top[0]=-1;

    for(int S=1;S<lim;S++){
        trans[S]=0; top[S]=-1;
        for(int x=0;x<n;x++) if((S>>x)&1){
            int R=S^(1<<x);
            if(!trans[R]) continue;
            int ok=1;
            for(int y=0;y<n;y++) if((R>>y)&1){
                if(!beats(t,x,y)){ ok=0; break; }
            }
            if(ok){
                trans[S]=1;
                top[S]=x;
                break;
            }
        }
    }

    uint32_t B=0;
    for(int S=1;S<lim;S++) if(trans[S]){
        int maximal=1;
        for(int x=0;x<n;x++) if(!((S>>x)&1)){
            if(trans[S|(1<<x)]){
                maximal=0;
                break;
            }
        }
        if(maximal) B|=1u<<top[S];
    }
    return B;
}

static uint32_t relabel7(uint32_t t,int *p){
    uint32_t u=0;
    for(int a=0;a<7;a++) for(int b=a+1;b<7;b++){
        int winner=beats(t,a,b)?a:b;
        int loser=(winner==a)?b:a;
        int A=p[winner], B=p[loser];
        int i=A<B?A:B, j=A<B?B:A;
        if(A<B) u|=1u<<pairidx[i][j];
    }
    return u;
}

static uint32_t canonical7(uint32_t t){
    uint32_t best=0xffffffffu;
    for(int k=0;k<nperm;k++){
        uint32_t u=relabel7(t,perms[k]);
        if(u<best) best=u;
    }
    return best;
}

typedef struct { uint32_t c; uint32_t count; } Entry;
static int cmpentry(const void *aa,const void *bb){
    uint32_t a=((const Entry*)aa)->c, b=((const Entry*)bb)->c;
    return a<b?-1:a>b?1:0;
}

int main(void){
    uint32_t diff_by_n[8]={0};

    for(int n=1;n<=7;n++){
        make_pairidx(n);
        uint32_t total=1u<<(n*(n-1)/2);
        uint32_t diff=0;

        uint64_t size_hist[8][8]={{0}};
        Entry *arr=NULL;
        uint32_t narr=0;

        if(n==7){
            nperm=0;
            int p[7];
            genperm_rec(7,0,0,p);
            arr=(Entry*)malloc((size_t)total*sizeof(Entry));
            if(!arr) return 2;
        }

        for(uint32_t t=0;t<total;t++){
            uint32_t U=uncovered(t,n);
            uint32_t B=banks(t,n);

            if((B & ~U)!=0){
                fprintf(stderr,"Banks-not-subset failure n=%d t=%u\n",n,t);
                return 3;
            }

            int bs=__builtin_popcount(B);
            int us=__builtin_popcount(U);
            size_hist[bs][us]++;

            if(B!=U){
                diff++;
                if(n==7){
                    arr[narr].c=canonical7(t);
                    arr[narr].count=1;
                    narr++;
                }
            }
        }

        diff_by_n[n]=diff;
        printf("N %d TOTAL %u DIFF %u\n",n,total,diff);

        if(n<=6 && diff!=0){
            fprintf(stderr,"unexpected pre-7 disparity\n");
            return 4;
        }

        if(n==7){
            if(diff!=13440){
                fprintf(stderr,"unexpected n=7 diff count\n");
                return 5;
            }

            uint64_t expected[8][8]={{0}};
            expected[1][1]=229376;
            expected[3][3]=402640;
            expected[3][4]=1680;
            expected[4][4]=525840;
            expected[4][5]=5040;
            expected[5][5]=486528;
            expected[5][6]=5040;
            expected[6][6]=330960;
            expected[6][7]=1680;
            expected[7][7]=108368;

            for(int i=0;i<8;i++) for(int j=0;j<8;j++){
                if(size_hist[i][j]!=expected[i][j]){
                    fprintf(stderr,"hist mismatch %d %d got %llu exp %llu\n",
                        i,j,(unsigned long long)size_hist[i][j],
                        (unsigned long long)expected[i][j]);
                    return 6;
                }
                if(size_hist[i][j])
                    printf("H %d %d %llu\n",i,j,(unsigned long long)size_hist[i][j]);
            }

            qsort(arr,narr,sizeof(Entry),cmpentry);
            uint32_t canons[4]={4642,4705,9387,11371};
            uint32_t orbit[4]={5040,5040,1680,1680};
            int ci=0;
            for(uint32_t i=0;i<narr;){
                uint32_t j=i+1;
                while(j<narr && arr[j].c==arr[i].c) j++;
                printf("C %u %u\n",arr[i].c,j-i);
                if(ci>=4 || arr[i].c!=canons[ci] || j-i!=orbit[ci]){
                    fprintf(stderr,"canonical class mismatch\n");
                    return 7;
                }
                ci++;
                i=j;
            }
            if(ci!=4){
                fprintf(stderr,"unexpected number of isomorphism classes\n");
                return 8;
            }
            free(arr);
        }
    }

    if(diff_by_n[1]||diff_by_n[2]||diff_by_n[3]||diff_by_n[4]||diff_by_n[5]||diff_by_n[6]||diff_by_n[7]!=13440)
        return 9;

    puts("VERIFY_OK");
    puts("FIRST_DISPARITY_ORDER 7");
    puts("N7_DIFFERENT 13440 / 2097152 = 105 / 16384");
    puts("N7_CLASSES 4");
    puts("N7_STRICT_SIZE_PAIRS (3,4):1680 (4,5):5040 (5,6):5040 (6,7):1680");
    return 0;
}
