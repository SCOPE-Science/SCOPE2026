/* Finite-field reproduction of the prescribed Jordan-product fiber formula.
 * Build: cc -O2 -std=c11 -Wall -Wextra verify.c -o verify && ./verify
 */
#include <stdint.h>
#include <stdio.h>
#include <string.h>

static int add(int a,int b,int q) {return q==4?(a^b):((a+b)%q);}
static int sub(int a,int b,int q) {return q==4?(a^b):((a-b+q)%q);}
static int mul(int a,int b,int q) {
    static const int m4[4][4]={{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};
    return q==4?m4[a][b]:(a*b)%q;
}
static int inv(int a,int q) {
    if(q==4) {static const int i4[4]={0,1,3,2};return i4[a];}
    for(int i=1;i<q;i++) if(mul(a,i,q)==1) return i;
    return 0;
}
static int64_t pw(int q,int n) {int64_t v=1;while(n--)v*=q;return v;}
static int rank_and_consistency(const int R[3][6],const int t[3],int q,int *ok) {
    int A[3][7];
    for(int i=0;i<3;i++){
        for(int j=0;j<6;j++)A[i][j]=R[i][j];
        A[i][6]=t[i];
    }
    int r=0;
    for(int col=0;col<6&&r<3;col++){
        int pivot=r;
        while(pivot<3&&!A[pivot][col])pivot++;
        if(pivot==3)continue;
        if(pivot!=r) for(int j=0;j<7;j++){
            int v=A[pivot][j];A[pivot][j]=A[r][j];A[r][j]=v;
        }
        int k=inv(A[r][col],q);
        for(int j=col;j<7;j++)A[r][j]=mul(k,A[r][j],q);
        for(int i=0;i<3;i++) if(i!=r && A[i][col]){
            int factor=A[i][col];
            for(int j=col;j<7;j++)A[i][j]=sub(A[i][j],mul(factor,A[r][j],q),q);
        }
        r++;
    }
    *ok=1;
    for(int i=r;i<3;i++)if(A[i][6]) *ok=0;
    return r;
}
static int check_q(int q){
    int64_t hist[343]={0};
    const int T=q*q*q;
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int d=0;d<q;d++)
    for(int e=0;e<q;e++)for(int f=0;f<q;f++){
        const int R[3][6]={{d,0,0,a,0,0},{0,0,0,f,0,d},{e,f,0,0,a,b}};
        for(int u=0;u<q;u++)for(int v=0;v<q;v++)for(int w=0;w<q;w++){
            const int target[3]={u,v,w};
            int ok=0;
            int r=rank_and_consistency(R,target,q,&ok);
            if(ok) hist[(u*q+v)*q+w]+=pw(q,7-r);
        }
    }
    int64_t total=0;
    for(int u=0;u<q;u++)for(int v=0;v<q;v++)for(int w=0;w<q;w++){
        const int index=(u*q+v)*q+w;
        int64_t expected=(u||v)?pw(q,7)*(q*q-1):
          (w?2*pw(q,7)*(q*q-1):pw(q,7)*(2*q*q+q-2));
        if(hist[index]!=expected){
            printf("FAIL q=%d target=(%d,%d,%d) actual=%lld expected=%lld\n",
              q,u,v,w,(long long)hist[index],(long long)expected);return 0;
        }
        total+=hist[index];
    }
    if(total!=pw(q,12)){printf("FAIL total q=%d\n",q);return 0;}
    if(q<=4){
        int64_t brute[64]={0};
        for(int ix=0;ix<q*q*q*q*q*q;ix++){
            int xc[6],z=ix;
            for(int i=0;i<6;i++){xc[i]=z%q;z/=q;}
            for(int iy=0;iy<q*q*q*q*q*q;iy++){
                int yc[6];z=iy;
                for(int i=0;i<6;i++){yc[i]=z%q;z/=q;}
                const int u=add(mul(xc[0],yc[3],q),mul(yc[0],xc[3],q),q);
                const int v=add(mul(xc[3],yc[5],q),mul(yc[3],xc[5],q),q);
                const int w=add(add(mul(xc[0],yc[4],q),mul(xc[1],yc[5],q),q),
                                add(mul(yc[0],xc[4],q),mul(yc[1],xc[5],q),q),q);
                brute[(u*q+v)*q+w]++;
            }
        }
        for(int i=0;i<T;i++)if(brute[i]!=hist[i]){
            printf("FAIL independent direct check q=%d index=%d\n",q,i);return 0;
        }
    }
    printf("PASS q=%d, target_count=%d, all %lld ordered pairs, direct=%s\n",
       q,T,(long long)total,q<=4?"yes":"rank-only");
    return 1;
}
int main(void){
    for(int q=2;q<=7;q++) if(q!=6 && !check_q(q))return 1;
    puts("VERIFY_OK_NILTRIANGULAR_JORDAN_FIBERS");
    return 0;
}
