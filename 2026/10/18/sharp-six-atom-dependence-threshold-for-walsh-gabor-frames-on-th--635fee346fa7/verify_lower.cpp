#include <cstdio>
#include <cstdint>
#include <array>
#include <algorithm>
constexpr int N=8, Q=64;
constexpr int64_t P=1000003;
static int64_t aa[8][5];
int64_t pw(int64_t a,int64_t e){int64_t r=1;while(e){if(e&1)r=r*a%P;a=a*a%P;e>>=1;}return r;}
int rank5(const int32_t g[8],const int idx[5]){
 for(int t=0;t<8;t++)for(int j=0;j<5;j++){
  int x=idx[j]>>3,y=idx[j]&7;
  int z=__builtin_parity(unsigned(t&y))?-g[t^x]:g[t^x];
  aa[t][j]=z<0?int64_t(z)+P:z;
 }
 int rank=0;
 for(int j=0;j<5;j++){
  int h=rank;while(h<8 && aa[h][j]==0)h++;
  if(h==8)continue;
  for(int u=j;u<5;u++)std::swap(aa[h][u],aa[rank][u]);
  int64_t inv=pw(aa[rank][j],P-2);
  for(int k=rank+1;k<8;k++){
   if(!aa[k][j])continue;
   int64_t mult=aa[k][j]*inv%P;
   for(int u=j+1;u<5;u++){
    aa[k][u]=(aa[k][u]-mult*aa[rank][u]%P+P)%P;
   }
   aa[k][j]=0;
  }
  rank++;if(rank==5)break;
 }
 return rank;
}
int main(){
 for (int64_t divisor=2; divisor*divisor<=P; ++divisor) {
  if (P % divisor==0) {
   printf("FAIL: modulus not prime\n");
   return 3;
  }
 }
 int32_t g[8]={31,47,61,73,89,107,127,149};
 int ids[5]={0,0,0,0,0};
 int64_t cnt=0,bad=0;
 for(int a=1;a<61;a++)for(int b=a+1;b<62;b++)for(int c=b+1;c<63;c++)for(int d=c+1;d<64;d++){
  ids[1]=a;ids[2]=b;ids[3]=c;ids[4]=d;cnt++;
  if(rank5(g,ids)<5){
   if(bad<8)printf("FAIL set=(0,%d,%d,%d,%d)\n",a,b,c,d);
   bad++;
  }
 }
 printf("checked=%lld bad=%lld g=31,47,61,73,89,107,127,149 p=%lld\n",(long long)cnt,(long long)bad,(long long)P);
 return bad?2:0;
}
