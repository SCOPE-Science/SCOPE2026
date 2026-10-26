/* Independent enumeration of five-variable binary cubic forms with no squarefree monomials.
   The five generators are four adjacent basis swaps and one elementary basis addition. */
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define LIMIT (1u<<25)
static uint8_t *visited;
static uint32_t *stack;
static inline unsigned parity(unsigned a){return __builtin_parity(a);}
static int rank5(uint32_t code){
 unsigned rr[5],rk=0;
 for(int i=0;i<5;i++)rr[i]=(code>>(5*i))&31u;
 for(int j=0;j<5;j++){
  int pivot=-1;
  for(int i=rk;i<5;i++)if((rr[i]>>j)&1u){pivot=i;break;}
  if(pivot<0)continue;
  unsigned t=rr[rk];rr[rk]=rr[pivot];rr[pivot]=t;
  for(int i=rk+1;i<5;i++)if((rr[i]>>j)&1u)rr[i]^=rr[rk];
  rk++;
 }
 return rk==5;
}
static uint32_t move_matrix(uint32_t a,int generator){
 unsigned R[5];
 for(int i=0;i<5;i++)R[i]=(a>>(5*i))&31u;
 if(generator<4){
   int s=generator, t=s+1;
   unsigned tmp=R[s];R[s]=R[t];R[t]=tmp;
   for(int i=0;i<5;i++){
     unsigned p=(R[i]>>s)&1u,q=(R[i]>>t)&1u;
     R[i] ^= (p^q)*((1u<<s)|(1u<<t));
   }
 }else{
   // Congruence by I+E_{0,1}; column 1 += column 0, then row 1 += row 0.
   for(int i=0;i<5;i++)if(R[i]&1u)R[i]^=2u;
   R[1]^=R[0];
 }
 uint32_t b=0;
 for(int i=0;i<5;i++)b|=R[i]<<(5*i);
 return b;
}
static int count_points(uint32_t a){
 int ct=0;
 for(int x=1;x<32;x++){
  int v=0;
  for(int i=0;i<5;i++){
   if(x&(1<<i))v^=parity(((a>>(i*5))&31u)&(unsigned)x);
  }
  ct+=v==0;
 }
 return ct;
}
int main(void){
 visited=calloc(LIMIT,1);
 stack=malloc(10000000u*sizeof(uint32_t));
 if(!visited||!stack)return 2;
 unsigned long long total=0;
 int classes=0;
 for(uint32_t initial=0;initial<LIMIT;initial++){
  if(visited[initial]||!rank5(initial))continue;
  uint32_t head=0,tail=1;
  stack[0]=initial;visited[initial]=1;
  while(head<tail){
   uint32_t x=stack[head++];
   for(int i=0;i<5;i++){
    uint32_t y=move_matrix(x,i);
    if(visited[y])continue;
    if(tail>=9999360u)return 3;
    visited[y]=1;stack[tail++]=y;
   }
  }
  printf("class=%d rep=%u members=%u points=%d\n",++classes,initial,tail,count_points(initial));
  total+=tail;
 }
 printf("TOTAL=%llu CLASSES=%d\n",total,classes);
 free(visited);free(stack);
 return total==9999360u && classes==13?0:5;
}
