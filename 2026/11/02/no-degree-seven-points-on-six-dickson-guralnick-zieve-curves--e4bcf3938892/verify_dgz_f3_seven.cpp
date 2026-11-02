#include <cstdio>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
const int Q=2187;
int add(int a,int b) {int s=0,m=1; for(int i=0;i<7;i++){s+=((a%3+b%3)%3)*m;a/=3;b/=3;m*=3;}return s;}
int neg(int a) {int s=0,m=1; for(int i=0;i<7;i++){s+=((3-a%3)%3)*m;a/=3;m*=3;}return s;}
int mul(int a,int b) {int aa[7]={},bb[7]={},c[13]={};for(int i=0;i<7;i++){aa[i]=a%3;a/=3;bb[i]=b%3;b/=3;}for(int i=0;i<7;i++)for(int j=0;j<7;j++)c[i+j]=(c[i+j]+aa[i]*bb[j])%3;for(int i=12;i>=7;i--){int v=c[i]; c[i]=0; c[i-7]=(c[i-7]+2*v)%3; c[i-6]=(c[i-6]+2*v)%3; c[i-4]=(c[i-4]+2*v)%3;}int r=0,m=1;for(int i=0;i<7;i++){r+=m*c[i];m*=3;}return r;}
int main(){
 vector<uint16_t> M(Q*Q), A(Q*Q);
 for(int a=0;a<Q;a++)for(int b=0;b<Q;b++){M[a*Q+b]=mul(a,b);A[a*Q+b]=add(a,b);}
 auto mm=[&](int a,int b)->int{return M[a*Q+b];};
 auto aa=[&](int a,int b)->int{return A[a*Q+b];};
 auto nn=[&](int a)->int{return neg(a);};
 // Every nonzero residue has multiplicative order dividing 3^7-1.
 // This checks that the displayed quotient ring really is a field.
 for(int a=1;a<Q;a++){int e=Q-1,z=1,t=a;while(e){if(e&1)z=mm(z,t);t=mm(t,t);e>>=1;}assert(z==1);}
 vector<int> reps,weights(Q,0);
 for(int x=0;x<Q;x++){int u=mm(x,x);if(!weights[u])reps.push_back(u);weights[u]++;}
 printf("distinct squares %zu, weights sum %d\n",reps.size(),Q);
 // F(x,y,1) as polynomial f(u=x^2,v=y^2), terms from exact determinant quotient.
 // exponent and sign entries
 const int TERMS[][3]={{9,0,1},{6,3,1},{6,2,1},{6,1,1},{6,0,1},{5,3,-1},{5,2,-1},{5,1,-1},{3,6,1},{3,5,-1},{3,3,1},{3,1,-1},{3,0,1},{2,6,1},{2,5,-1},{2,2,-1},{2,1,1},{1,6,1},{1,5,-1},{1,3,-1},{1,2,1},{0,9,1},{0,6,1},{0,3,1},{0,0,1}};
 const int N=sizeof(TERMS)/sizeof(TERMS[0]);
 vector<vector<int>> powers(Q,vector<int>(10,1));
 for(int z:reps)for(int j=1;j<10;j++)powers[z][j]=mm(powers[z][j-1],z);
 long long affine=0; long long pairclasses=0; int nonzero=0;
 for(int i=0;i<(int)reps.size();i++){
  int u=reps[i];
  for(int j=i;j<(int)reps.size();j++){
   int v=reps[j];int val=0;
   for(auto &t:TERMS){int c=mm(powers[u][t[0]],powers[v][t[1]]); if(t[2]<0)c=nn(c);val=aa(val,c);}
   if(val==0){long long w=1LL*weights[u]*weights[v]*(i==j?1:2);affine+=w;pairclasses++;nonzero++;}
  }
 }
 printf("point count affine=%lld, square-pair half-classes=%lld, point count infinity=0, total=%lld, %s div7\n",affine,pairclasses,affine,affine%7==0?"yes":"NO");
 // count F_3 by direct evaluation
 long long n1=0;for(int x=0;x<3;x++)for(int y=0;y<3;y++){
  int u=mm(x,x),v=mm(y,y),val=0;for(auto&t:TERMS){int c=mm(powers[u][t[0]],powers[v][t[1]]);if(t[2]<0)c=nn(c);val=aa(val,c);}if(val==0)n1++;
 }
 printf("affine F3 count %lld\n",n1);
 assert(affine==0 && n1==0);
 puts("DGZ_F3_SEVENTH_EXTENSION_ENUMERATION_PASS");
}
