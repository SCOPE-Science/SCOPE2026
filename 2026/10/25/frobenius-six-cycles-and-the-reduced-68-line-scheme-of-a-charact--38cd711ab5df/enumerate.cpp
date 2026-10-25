#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <array>
#include <string>
using namespace std;
int Q,P; vector<unsigned char> M, Sq, Cub, Fourth;
inline int mul(int a,int b){return M[a*Q+b];}
inline int FF(const array<int,4>& x){
  // lambda=1
  int a=x[0],b=x[1],c=x[2],d=x[3];
  return mul(mul(a,Sq[b]),c)^Fourth[b]^mul(b,Cub[c])^mul(Cub[a],d)^mul(mul(a,c),Sq[d]);
}
inline array<int,4> addt(const array<int,4>& A,const array<int,4>& B,int t){
 return {A[0]^mul(t,B[0]),A[1]^mul(t,B[1]),A[2]^mul(t,B[2]),A[3]^mul(t,B[3])};
}
int main(int argc,char** argv){
 if(argc<3){puts("q poly");return 1;}
 Q=atoi(argv[1]); P=strtol(argv[2],0,0); if(Q<4){puts("q>=4 needed");return 1;}
 M.resize(Q*Q);Sq.resize(Q);Cub.resize(Q);Fourth.resize(Q);
 for(int x=0;x<Q;x++)for(int y=0;y<Q;y++){
  int a=x,b=y,r=0;while(b){if(b&1)r^=a;b>>=1;a<<=1;if(a&Q)a^=P;}
  M[x*Q+y]=r;
 }
 for(int a=0;a<Q;a++){Sq[a]=mul(a,a);Cub[a]=mul(Sq[a],a);Fourth[a]=mul(Sq[a],Sq[a]);}
 uint64_t count=0, pcount[6]={}, tried=0; int no=0;
 for(int p=0;p<3;p++)for(int r=p+1;r<4;r++,no++){
  vector<pair<int,int>> frees;array<int,4>A{},B{};A[p]=1;B[r]=1;
  for(int j=p+1;j<4;j++)if(j!=r)frees.push_back({0,j});
  for(int j=r+1;j<4;j++)frees.push_back({1,j});
  int k=(int)frees.size();uint64_t total=1;for(int i=0;i<k;i++)total*=Q;
  for(uint64_t z=0;z<total;z++){
   uint64_t u=z;
   for(auto [row,col]:frees){int a=u%Q;u/=Q;if(row==0)A[col]=a;else B[col]=a;}
   tried++;
   if(FF(A))continue;
   if(FF(B))continue;
   if(FF(addt(A,B,1)))continue;
   if(FF(addt(A,B,2)))continue;
   if(FF(addt(A,B,3)))continue;
   ++count;++pcount[no];
   printf("LINE %d %d %d %d %d %d %d %d %d %d\n",p,r,A[0],A[1],A[2],A[3],B[0],B[1],B[2],B[3]);
  }
 }
 fprintf(stderr,"SUMMARY q=%d poly=%d tried=%llu lines=%llu charts=%llu,%llu,%llu,%llu,%llu,%llu\n",Q,P,(unsigned long long)tried,(unsigned long long)count,(unsigned long long)pcount[0],(unsigned long long)pcount[1],(unsigned long long)pcount[2],(unsigned long long)pcount[3],(unsigned long long)pcount[4],(unsigned long long)pcount[5]);
}
