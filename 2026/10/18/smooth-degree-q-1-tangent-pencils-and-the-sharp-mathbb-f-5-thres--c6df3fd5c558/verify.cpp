#include <cstdio>
#include <vector>
#include <array>
#include <cstdint>
using namespace std;
constexpr int Q=5,N=31,M=10;
int mon[10][3],evals[N][M],diffs[N][3][M];
array<array<int,3>,N> pts;
int powmod(int a,int n){int x=1;for(int i=0;i<n;i++)x=x*a%Q;return x;}
void setup(){
 int k=0; for(int i=3;i>=0;i--)for(int j=3-i;j>=0;j--)mon[k][0]=i,mon[k][1]=j,mon[k++][2]=3-i-j;
 k=0;for(int x=0;x<Q;x++)for(int y=0;y<Q;y++)for(int z=0;z<Q;z++){
  if(!x&&!y&&!z)continue;
  int first=x?x:y?y:z; if(first!=1)continue;
  pts[k]={x,y,z};
  for(int m=0;m<M;m++){
   int e=powmod(x,mon[m][0])*powmod(y,mon[m][1])%Q*powmod(z,mon[m][2])%Q;
   evals[k][m]=e;
   for(int t=0;t<3;t++){
    int d=mon[m][t];if(!d){diffs[k][t][m]=0;continue;}
    diffs[k][t][m]=d*powmod(x,mon[m][0]-(t==0))%Q*powmod(y,mon[m][1]-(t==1))%Q*powmod(z,mon[m][2]-(t==2))%Q;
   }
  } k++;
 }if(k!=N)printf("BAD POINT COUNT %d\n",k);
}
int normline(int a,int b,int c){
 if(!a&&!b&&!c)return -1;
 int w=a?a:b?b:c;
 int inv=1;for(; inv<Q;inv++)if(w*inv%Q==1)break;
 a=a*inv%Q;b=b*inv%Q;c=c*inv%Q;
 for(int i=0;i<N;i++)if(pts[i][0]==a && pts[i][1]==b && pts[i][2]==c)return i;
 return -2;
}
int main(){
 setup();uint64_t lines[N];for(int j=0;j<N;j++){
  lines[j]=0;for(int i=0;i<N;i++)if((pts[i][0]*pts[j][0]+pts[i][1]*pts[j][1]+pts[i][2]*pts[j][2])%Q==0)lines[j]|=uint64_t(1)<<i;
 }
 // Enumerate every nonzero cubic up to scalar: its first nonzero coefficient is 1.
 int coeff[M];long long normalized=0,nonempty=0,covering=0;int hist[32]={0}; int maxcover=0; long long maxcount=0; int firstmax[10]={0};
 for(int first=0; first<M;first++){
  long long max=1;for(int i=first+1;i<M;i++)max*=Q;
  for(long long zz=0;zz<max;zz++){
   for(int k=0;k<M;k++)coeff[k]=0;
   coeff[first]=1;long long n=zz;
   for(int j=M-1;j>first;j--){coeff[j]=n%Q;n/=Q;}
   normalized++;
   int roots[N],sz=0;
   for(int i=0;i<N;i++){
    int f=0;for(int j=first;j<M;j++)f+=coeff[j]*evals[i][j];
    if(f%Q==0)roots[sz++]=i;
   }
   hist[sz]++;
   if(sz>0)nonempty++;
   uint64_t cov=0;
   for(int j=0;j<sz;j++){
    int p=roots[j],d[3]={};
    for(int t=0;t<3;t++){
     for(int k=first;k<M;k++)d[t]+=coeff[k]*diffs[p][t][k];
     d[t]%=Q;
    }
    int L=normline(d[0],d[1],d[2]);
    if(L>=0)cov |=lines[L];
   }
   int ccount=__builtin_popcountll(cov); if(ccount>maxcover){maxcover=ccount;maxcount=0;for(int jj=0;jj<M;jj++)firstmax[jj]=coeff[jj];}if(ccount==maxcover)maxcount++;
   if(cov == ((uint64_t(1)<<N)-1)){
    covering++;
    if(covering<15){printf("CUBIC_COVER ");for(int j=0;j<M;j++)printf("%d",coeff[j]);printf(" roots=%d\n",sz);}
   }
  }
 }
 printf("COUNTS normalized=%lld with_rational_point=%lld tangent_cover=%lld max_cover=%d max_count=%lld example=",normalized,nonempty,covering,maxcover,maxcount);for(int i=0;i<M;i++)printf("%d",firstmax[i]);printf("\n");
 for(int i=0;i<=N;i++)if(hist[i])printf("rootcount[%d]=%d\n",i,hist[i]);
 // Check the smooth quartic X^4+X^3Y+Y^3Z-Z^4 over F_5.
 // Every rational point lying on the curve contributes a tangent line.
 uint64_t quartic_cover=0;int quartic_points=0;
 for(int j=0;j<N;j++){
   int x=pts[j][0],y=pts[j][1],z=pts[j][2];
   int f=(powmod(x,4)+powmod(x,3)*y+powmod(y,3)*z-powmod(z,4))%Q;
   if((f+Q)%Q)continue;
   quartic_points++;
   int a=(4*powmod(x,3)+3*powmod(x,2)*y)%Q;
   int b=(powmod(x,3)+3*powmod(y,2)*z)%Q;
   int c=(powmod(y,3)-4*powmod(z,3)+4*Q)%Q;
   int l=normline(a,b,c);
   if(l<0){printf("ERROR: singular quartic rational point\n");return 1;}
   quartic_cover|=lines[l];
 }
 printf("QUARTIC rational_points=%d tangent_cover=%d\n", quartic_points, __builtin_popcountll(quartic_cover));
 if(normalized!=2441406LL||covering!=0||maxcover!=29||__builtin_popcountll(quartic_cover)!=N){puts("VERIFY_FAILED");return 1;}
 puts("VERIFY_OK: exhaustive 2441406 cubic classes, no tangent-filling cubic, and a tangent-filling quartic over F5");
}
