/* Exhaustive original-axiom oracle for small complete height-two frames. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int valid(int p,int q, uint32_t r[]){
 const int n=p+q;
 for(int i=0;i<n;i++) {
  if(!(r[i]&(1u<<i)))return 0;
  for(int j=0;j<n;j++) if(r[i]&(1u<<j))if(r[j]&~r[i])return 0;
 }
 for(int i=0;i<p;i++)for(int j=p;j<n;j++)for(int v=0;v<n;v++){
  if(r[i]&(1u<<v)){
   int yes=0;
   for(int w=0;w<n;w++) if(r[j]&(1u<<w))if(w==v||(v<p&&w>=p)) yes=1;
   if(!yes)return 0;
  }
  if(r[j]&(1u<<v)){
   int yes=0;
   for(int w=0;w<n;w++)if(r[i]&(1u<<w))if(w==v||(w<p&&v>=p))yes=1;
   if(!yes)return 0;
  }
 }
 return 1;
}
static int nextperm(int *a,int n){int i=n-2;while(i>=0&&a[i]>=a[i+1])i--;if(i<0)return 0;int j=n-1;while(a[j]<=a[i])j--;int v=a[j];a[j]=a[i];a[i]=v;for(int l=i+1,r=n-1;l<r;l++,r--){v=a[l];a[l]=a[r];a[r]=v;}return 1;}
static unsigned encode(int n,const uint32_t*r){unsigned k=0;for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(r[i]&(1u<<j))k|=1u<<(i*n+j);return k;}
static unsigned canonical(int p,int q, uint32_t r[]){
 int n=p+q, a[6],b[6],sigma[6]; unsigned least=~0u;
 for(int i=0;i<p;i++)a[i]=i;
 do{
  for(int j=0;j<q;j++)b[j]=j;
  do{
   for(int i=0;i<p;i++)sigma[i]=a[i];
   for(int j=0;j<q;j++)sigma[p+j]=p+b[j];
   uint32_t out[6]={0};
   for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(r[i]&(1u<<j))out[sigma[i]]|=1u<<sigma[j];
   unsigned z=encode(n,out);if(z<least)least=z;
  }while(nextperm(b,q));
 }while(nextperm(a,p));
 return least;
}
static void go(int p,int q){
 const int n=p+q,K=n*(n-1);if(K>20){puts("MAX_EXCEEDED");exit(3);}
 uint8_t *mark=calloc(1u<<(n*n),1);if(!mark){puts("OOM");exit(3);}
 unsigned long long labelled=0,unlabelled=0;
 uint32_t r[6];
 for(unsigned k=0;k<(1u<<K);k++){
  for(int i=0;i<n;i++)r[i]=1u<<i;
  unsigned bits=k;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){if(bits&1u)r[i]|=1u<<j;bits>>=1;}
  if(!valid(p,q,r))continue;
  labelled++;
  unsigned c=canonical(p,q,r);
  if(!mark[c]){mark[c]=1;unlabelled++;}
 }
 free(mark);
 printf("EXHAUSTIVE %d %d %llu %llu\n",p,q,labelled,unlabelled);
}
int main(){go(2,2);go(2,3);go(3,2);puts("VERIFY_OK");}
