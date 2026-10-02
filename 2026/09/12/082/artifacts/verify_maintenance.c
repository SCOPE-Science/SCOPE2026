/* Exhaustive distance-three exclusion and explicit distance-six witnesses. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#define MASK ((UINT64_C(1)<<18)-1)
typedef uint64_t U;
typedef struct{U key;int i,j,k,a,b,c;} Triple;
static U add(U a,U b){U al=a&MASK,ah=a>>18,bl=b&MASK,bh=b>>18,az=MASK^(al|ah),bz=MASK^(bl|bh);return ((az&bl)|(al&bz)|(ah&bh))|(((az&bh)|(ah&bz)|(al&bl))<<18);}
static U neg(U a){return (a>>18)|((a&MASK)<<18);}
static void need(int ok,const char* m){if(!ok){fprintf(stderr,"%s\n",m);exit(1);}}
static int compare(const void* a,const void* b){U x=((const Triple*)a)->key,y=((const Triple*)b)->key;return (x>y)-(x<y);}
static int disjoint(Triple a,Triple b){int x[3]={a.i,a.j,a.k},y[3]={b.i,b.j,b.k};for(int i=0;i<3;i++)for(int j=0;j<3;j++)if(x[i]==y[j])return 0;return 1;}
int main(void){
  int total;need(scanf("%d",&total)==1&&total==1458,"matrix count");
  Triple* triples=malloc(57120*sizeof(Triple));need(triples!=NULL,"allocation");
  for(int f=0;f<total;f++){
    char name[200];int M[36][36],B[36][36];U col[36]={0};
    need(scanf("%199s",name)==1,"matrix name");
    for(int i=0;i<36;i++)for(int j=0;j<36;j++){need(scanf("%d",&M[i][j])==1,"truncated");need(M[i][j]==0||M[i][j]==1,"not binary");B[i][j]=M[i][j];}
    for(int i=0;i<36;i++){
      int row=0,column=0;for(int j=0;j<36;j++){row+=M[i][j];column+=M[j][i];}need(row==15&&column==15,"row/column sum");
      for(int j=0;j<36;j++){int r=0,c=0;for(int k=0;k<36;k++){r+=M[i][k]*M[j][k];c+=M[k][i]*M[k][j];}need(r==(i==j?15:6)&&c==(i==j?15:6),"design Gram identity");}
    }
    int rank=0;
    for(int c=0;c<36;c++){
      int p=rank;while(p<36&&!B[p][c])p++;if(p==36)continue;
      for(int j=0;j<36;j++){int t=B[p][j];B[p][j]=B[rank][j];B[rank][j]=t;}
      if(B[rank][c]==2)for(int j=0;j<36;j++)B[rank][j]=2*B[rank][j]%3;
      for(int i=0;i<36;i++)if(i!=rank){int v=B[i][c];for(int j=0;j<36;j++)B[i][j]=(B[i][j]-v*B[rank][j]+6)%3;}rank++;
    }
    need(rank==18,"rank not 18");
    for(int j=0;j<36;j++)for(int i=0;i<18;i++)if(B[i][j])col[j]|=UINT64_C(1)<<(i+(B[i][j]==2?18:0));
    /* Self-orthogonality and half dimension imply C=kernel(B), and every
       codeword has weight 0 mod 3. Check all weight-three words, up to sign. */
    for(int i=0;i<36;i++)for(int j=i+1;j<36;j++)for(int k=j+1;k<36;k++)for(int b=1;b<=2;b++)for(int c=1;c<=2;c++)need(add(add(col[i],b==1?col[j]:neg(col[j])),c==1?col[k]:neg(col[k]))!=0,"weight-three word");
    int size=0;
    for(int i=0;i<36;i++)for(int j=i+1;j<36;j++)for(int k=j+1;k<36;k++)for(int a=1;a<=2;a++)for(int b=1;b<=2;b++)for(int c=1;c<=2;c++){
      U key=add(add(a==1?col[i]:neg(col[i]),b==1?col[j]:neg(col[j])),c==1?col[k]:neg(col[k]));triples[size++]=(Triple){key,i,j,k,a,b,c};
    }
    need(size==57120,"triple count");qsort(triples,size,sizeof(Triple),compare);
    int found=0;Triple left={0},right={0};
    for(int lo=0;lo<size&&!found;){int hi=lo+1;while(hi<size&&triples[hi].key==triples[lo].key)hi++;for(int a=lo;a<hi&&!found;a++)for(int b=a+1;b<hi;b++)if(disjoint(triples[a],triples[b])){left=triples[a];right=triples[b];found=1;break;}lo=hi;}
    need(found,"no weight-six witness");int word[36]={0};word[left.i]=left.a;word[left.j]=left.b;word[left.k]=left.c;word[right.i]=3-right.a;word[right.j]=3-right.b;word[right.k]=3-right.c;
    int weight=0;for(int j=0;j<36;j++)weight+=(word[j]!=0);need(weight==6,"weight mismatch");
    for(int i=0;i<36;i++){int s=0;for(int j=0;j<36;j++)s+=M[i][j]*word[j];need(s%3==0,"witness syndrome");}
    printf("%s RANK 18 MINWEIGHT 6 WITNESS",name);for(int j=0;j<36;j++)if(word[j])printf(" %d:%d",j,word[j]);puts("");
  }
  free(triples);puts("VERIFY_OK: all 1458 design identities, ranks, weight-three exclusions and explicit weight-six witnesses");return 0;
}
