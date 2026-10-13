#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static const int G[9][43] = {
    {1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1},
    {0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0},
    {0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1},
    {0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0},
    {0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,1,1},
    {0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,1,0,1},
    {0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1},
    {0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,1},
    {0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1}
};
static uint64_t words[512];
static unsigned long long hist[10][44], expect[10][44], countd[10];
static const unsigned long long expected_counts[10] = {0ULL,511ULL,43435ULL,788035ULL,3309747ULL,3309747ULL,788035ULL,43435ULL,511ULL,1ULL};

static void process_pivots(int d, int *piv){
    int isP[9]={0}; for(int i=0;i<d;i++) isP[piv[i]]=1;
    int fi[81],fc[81],F=0;
    for(int i=0;i<d;i++) for(int c=piv[i]+1;c<9;c++) if(!isP[c]){fi[F]=i;fc[F]=c;F++;}
    uint64_t total=1ULL<<F;
    for(uint64_t mask=0;mask<total;mask++){
        unsigned basis[9]={0};
        for(int i=0;i<d;i++) basis[i]=1U<<piv[i];
        for(int z=0;z<F;z++) if((mask>>z)&1ULL) basis[fi[z]]|=1U<<fc[z];
        uint64_t supp=0; for(int i=0;i<d;i++) supp|=words[basis[i]];
        int wt=__builtin_popcountll(supp); hist[d][wt]++; countd[d]++;
    }
}
static void recpiv(int d,int idx,int start,int *piv){
    if(idx==d){process_pivots(d,piv);return;}
    for(int p=start;p<=9-(d-idx);p++){piv[idx]=p;recpiv(d,idx+1,p+1,piv);}
}
static int rank9(void){
    uint64_t A[9]={0};
    for(int i=0;i<9;i++) for(int j=0;j<43;j++) if(G[i][j]) A[i]|=1ULL<<j;
    int r=0; for(int c=0;c<43;c++){int p=-1;for(int i=r;i<9;i++)if((A[i]>>c)&1ULL){p=i;break;}if(p<0)continue;uint64_t t=A[r];A[r]=A[p];A[p]=t;for(int i=0;i<9;i++)if(i!=r&&((A[i]>>c)&1ULL))A[i]^=A[r];r++;if(r==9)break;}
    return r;
}
int main(void){
    expect[1][16]=24ULL;
    expect[1][18]=95ULL;
    expect[1][20]=123ULL;
    expect[1][22]=107ULL;
    expect[1][24]=91ULL;
    expect[1][26]=45ULL;
    expect[1][28]=17ULL;
    expect[1][30]=9ULL;
    expect[2][24]=20ULL;
    expect[2][26]=670ULL;
    expect[2][28]=4148ULL;
    expect[2][30]=9178ULL;
    expect[2][32]=12131ULL;
    expect[2][34]=10238ULL;
    expect[2][36]=5220ULL;
    expect[2][38]=1638ULL;
    expect[2][40]=188ULL;
    expect[2][42]=4ULL;
    expect[3][29]=4ULL;
    expect[3][30]=73ULL;
    expect[3][31]=656ULL;
    expect[3][32]=3608ULL;
    expect[3][33]=13350ULL;
    expect[3][34]=33822ULL;
    expect[3][35]=65820ULL;
    expect[3][36]=103542ULL;
    expect[3][37]=135384ULL;
    expect[3][38]=146345ULL;
    expect[3][39]=127984ULL;
    expect[3][40]=90629ULL;
    expect[3][41]=47854ULL;
    expect[3][42]=16288ULL;
    expect[3][43]=2676ULL;
    expect[4][33]=9ULL;
    expect[4][34]=271ULL;
    expect[4][35]=3070ULL;
    expect[4][36]=21524ULL;
    expect[4][37]=90746ULL;
    expect[4][38]=252224ULL;
    expect[4][39]=514084ULL;
    expect[4][40]=769511ULL;
    expect[4][41]=840741ULL;
    expect[4][42]=604137ULL;
    expect[4][43]=213430ULL;
    expect[5][36]=28ULL;
    expect[5][37]=757ULL;
    expect[5][38]=11682ULL;
    expect[5][39]=84161ULL;
    expect[5][40]=326127ULL;
    expect[5][41]=796191ULL;
    expect[5][42]=1207110ULL;
    expect[5][43]=883691ULL;
    expect[6][38]=8ULL;
    expect[6][39]=468ULL;
    expect[6][40]=11271ULL;
    expect[6][41]=77980ULL;
    expect[6][42]=272500ULL;
    expect[6][43]=425808ULL;
    expect[7][40]=7ULL;
    expect[7][41]=882ULL;
    expect[7][42]=9180ULL;
    expect[7][43]=33366ULL;
    expect[8][42]=43ULL;
    expect[8][43]=468ULL;
    expect[9][43]=1ULL;
    if(rank9()!=9){puts("FAIL rank");return 1;}
    uint64_t rowbits[9]={0};
    for(int i=0;i<9;i++) for(int j=0;j<43;j++) if(G[i][j]) rowbits[i]|=1ULL<<j;
    for(int i=0;i<9;i++) for(int j=0;j<9;j++) if(__builtin_parityll(rowbits[i]&rowbits[j])){puts("FAIL Gram");return 1;}
    for(int u=0;u<512;u++){uint64_t z=0;for(int i=0;i<9;i++)if((u>>i)&1)z^=rowbits[i];words[u]=z;}
    unsigned long long wh[44]={0};for(int u=0;u<512;u++)wh[__builtin_popcountll(words[u])]++;
    unsigned long long wexp[44]={0};wexp[0]=1;wexp[16]=24;wexp[18]=95;wexp[20]=123;wexp[22]=107;wexp[24]=91;wexp[26]=45;wexp[28]=17;wexp[30]=9;
    for(int w=0;w<=43;w++)if(wh[w]!=wexp[w]){printf("FAIL weight %d\n",w);return 1;}
    for(int d=1;d<=9;d++){int piv[9];recpiv(d,0,0,piv);if(countd[d]!=expected_counts[d]){printf("FAIL count d=%d\n",d);return 1;}for(int w=0;w<=43;w++)if(hist[d][w]!=expect[d][w]){printf("FAIL spectrum d=%d w=%d got=%llu exp=%llu\n",d,w,hist[d][w],expect[d][w]);return 1;}}
    int col[43];for(int c=0;c<43;c++){int v=0;for(int i=0;i<9;i++)v|=G[i][c]<<i;if(v==0){puts("FAIL zero column");return 1;}col[c]=v;}
    for(int a=0;a<43;a++)for(int b=a+1;b<43;b++)if(col[a]==col[b]){puts("FAIL duplicate column");return 1;}
    int found[7][3];int nf=0;for(int a=0;a<43;a++)for(int b=a+1;b<43;b++)for(int c=b+1;c<43;c++)if((col[a]^col[b]^col[c])==0){if(nf>=7){puts("FAIL too many triples");return 1;}found[nf][0]=a+1;found[nf][1]=b+1;found[nf][2]=c+1;nf++;}
    int exptri[7][3]={ {6,20,35}, {11,24,41}, {12,31,36}, {13,31,41}, {14,31,35}, {15,27,36}, {34,41,43} };
    if(nf!=7){printf("FAIL triple count %d\n",nf);return 1;}
    for(int t=0;t<7;t++)for(int j=0;j<3;j++)if(found[t][j]!=exptri[t][j]){puts("FAIL triple list");return 1;}
    puts("VERIFY_OK");return 0;
}
