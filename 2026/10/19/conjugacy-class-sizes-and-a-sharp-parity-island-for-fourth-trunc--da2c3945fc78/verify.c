/* Independent finite-field check of the stated conjugacy rank distribution.
   Only a C11 compiler is required: cc -O2 -std=c11 verify.c -o verify && ./verify
   For p=2,3,5 we examine every ordered tuple of 8 low-degree coordinates.
   Four length-three coordinates are central and multiply all element counts
   by p^4. The 8x8 matrix is constructed directly from path multiplication. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static int prime, inverses[8];
static int reduce(int mat[8][8]) {
    int rank=0;
    for (int j=0;j<8;j++) {
        int pivot=rank;
        while (pivot<8 && mat[pivot][j]==0) pivot++;
        if (pivot==8) continue;
        for(int k=j;k<8;k++) {
            int tmp=mat[rank][k]; mat[rank][k]=mat[pivot][k];mat[pivot][k]=tmp;
        }
        int inv=inverses[mat[rank][j]];
        for(int k=j;k<8;k++) mat[rank][k]=mat[rank][k]*inv%prime;
        for(int row=rank+1;row<8;row++){
            int c=mat[row][j];
            if(!c)continue;
            for(int k=j;k<8;k++) mat[row][k]=(mat[row][k]+prime*prime-c*mat[rank][k])%prime;
        }
        if(++rank==8)break;
    }
    return rank;
}
static int adjoint_rank(const int a[4],const int b[4]) {
    int mat[8][8]={0};
    for(int i=0;i<4;i++){
        mat[i][(i+1)%4]=(mat[i][(i+1)%4]+a[i])%prime;
        mat[i][i]=(mat[i][i]+prime-a[(i+1)%4])%prime;
        mat[i+4][(i+2)%4]=(mat[i+4][(i+2)%4]+b[i])%prime;
        mat[i+4][i]=(mat[i+4][i]+prime-b[(i+1)%4])%prime;
        mat[i+4][4+(i+1)%4]=(mat[i+4][4+(i+1)%4]+a[i])%prime;
        mat[i+4][4+i]=(mat[i+4][4+i]+prime-a[(i+2)%4])%prime;
    }
    return reduce(mat);
}
static long long power(int a,int e){long long p=1;while(e--)p*=a;return p;}
static void check(int q){
    prime=q;
    for(int i=1;i<q;i++)for(int j=1;j<q;j++)if(i*j%q==1)inverses[i]=j;
    long long elements[9]={0},limit=power(q,8);
    for(long long z=0;z<limit;z++){
        long long x=z;int a[4],b[4];
        for(int i=0;i<4;i++){a[i]=(int)(x%q);x/=q;}
        for(int i=0;i<4;i++){b[i]=(int)(x%q);x/=q;}
        int rank=adjoint_rank(a,b);
        if(rank<0||rank>8){fprintf(stderr,"invalid rank\n");exit(1);}
        elements[rank]++;
    }
    long long expected[9]={0};
    expected[0]=1;
    expected[2]=(q-1)*(long long)(q+1)*(q+1);
    expected[4]=q*(long long)(q-1)*(q-1)*(q+1)+2*power(q,4)*(q*q-1);
    expected[6]=power(q,4)*power(q*q-1,2);
    for(int r=0;r<9;r++){
        if(elements[r]!=expected[r]){
            fprintf(stderr,"FAIL: q=%d rank=%d got=%lld expected=%lld\n",
                    q,r,elements[r],expected[r]);exit(1);
        }
    }
    long long total_classes=0;
    for(int r=0;r<9;r++){
        if(!expected[r])continue;
        long long denominator=power(q,r);
        long long elements_with_central=expected[r]*power(q,4);
        if(elements_with_central%denominator){fprintf(stderr,"nonintegral class count\n");exit(1);}
        total_classes+=elements_with_central/denominator;
    }
    if(total_classes!=3*power(q,6)+power(q,5)-power(q,4)-2*power(q,3)-power(q,2)+q){
        fprintf(stderr,"class total mismatch\n");exit(1);
    }
    printf("q=%d: low-coordinate rank counts: %lld %lld %lld %lld; classes=%lld\n",
            q,elements[0],elements[2],elements[4],elements[6],total_classes);
}
int main(void){check(2);check(3);check(5);puts("VERIFY_OK");return 0;}
