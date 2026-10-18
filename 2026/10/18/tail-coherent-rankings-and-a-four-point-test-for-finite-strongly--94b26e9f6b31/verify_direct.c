#include <stdio.h>
#include <stdlib.h>
#define N 4
static int cand[N][24][1<<N], nc[N], f[N][1<<N];
static long long count,checked;
void gen(int w,int mask,int idx,int* a){
 if(mask==(1<<N)){
  for(int q=0;q<(1<<N);q++) cand[w][nc[w]][q]=a[q];
  nc[w]++;return;
 }
 if(mask==0||((mask>>w)&1)){a[mask]=w;gen(w,mask+1,idx,a);}
 else for(int x=0;x<N;x++)if((mask>>x)&1){a[mask]=x;gen(w,mask+1,idx,a);}
}
int dense(void){
 for(int w=0;w<N;w++)for(int A=1;A<(1<<N);A++){
  int u=f[w][A];
  for(int C=A;C;C=(C-1)&A) if(f[w][C]!=f[u][C]) return 0;
 }
 return 1;
}
void rec(int w){
 if(w==N){checked++;if(dense())count++;return;}
 for(int j=0;j<nc[w];j++){for(int A=0;A<(1<<N);A++)f[w][A]=cand[w][j][A];rec(w+1);}
}
int main(){for(int w=0;w<N;w++){int a[1<<N];gen(w,0,0,a);printf("%d ",nc[w]);}rec(0);printf("\nraw=%lld dense=%lld\n",checked,count);}
