#include <cstdio>
#include <cstdint>
long long hist[10]={};long long n=0;int q=3,N=27;int e[27];
void dfs(int v,uint32_t used,int depth,int hits){
 if(depth==N){
  if(v==0){int last=e[N-1],first=e[0];int h=hits+ (last/9 == first%3 && (last/3)%3==last%3);
  hist[h]++;n++;
  }
  return;
 }
 int a=v/q,b=v%q;
 for(int c=0;c<q;c++){
  int id=v*q+c;
  if((used>>id)&1)continue;
  e[depth]=id;
  int hit=0;
  if(depth>0){int p=e[depth-1];hit=(p/9 ==c && (p/3)%3==p%3);}
  dfs(b*q+c,used|(1u<<id),depth+1,hits+hit);
 }
}
int main(){e[0]=0;dfs(0,1,1,0);printf("n %lld\n",n);for(int i=0;i<10;i++)printf("%d %lld\n",i,hist[i]);}
