/* Exact full census for reciprocal adjacent-sum permutations. C11, unsigned 64-bit arithmetic. */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static int n,p[16];
static uint64_t L,wt[32],cycle_count,line_count;
static uint64_t gcd64(uint64_t a,uint64_t b){while(b){uint64_t t=a%b;a=b;b=t;}return a;}
static void circle_dfs(int d,int prev,uint32_t used,uint64_t sum){
    if(d==n){
        if(p[1]<prev && sum+wt[prev+1]==L)cycle_count++;
        return;
    }
    for(int x=2;x<=n;x++)if(!(used&(1u<<x))){
        p[d]=x;
        circle_dfs(d+1,x,used|(1u<<x),sum+wt[prev+x]);
    }
}
static void line_dfs(int d,int prev,uint32_t used,uint64_t sum){
    if(d==n){if(p[0]<prev && sum==L)line_count++;return;}
    for(int x=1;x<=n;x++)if(!(used&(1u<<x))){
        p[d]=x;
        line_dfs(d+1,x,used|(1u<<x),sum+(d?wt[prev+x]:0));
    }
}
int main(void){
  static const uint64_t expected_circle[14]={0,0,0,0,0,0,0,0,2,5,6,38,79,224};
  static const uint64_t expected_line[13]={0,0,0,0,0,0,0,1,8,22,98,844,3831};
  static const uint64_t expected_l[14]={0,0,0,60,420,2520,27720,360360,360360,12252240,232792560,232792560,5354228880ULL,26771144400ULL};
  for(n=3;n<=13;n++){
    L=1;
    for(int d=3;d<=2*n-1;d++)L=(L/gcd64(L,(uint64_t)d))*(uint64_t)d;
    if(L!=expected_l[n]){fprintf(stderr,"LCM_FAIL %d\n",n);return 2;}
    for(int d=3;d<=2*n-1;d++)wt[d]=L/(uint64_t)d;
    /* Maximum of n positive summands is below n*L/3 < 2^64 for n <= 13. */
    if((uint64_t)n*(L/3+1)>=UINT64_MAX/2){return 3;}
    p[0]=1; cycle_count=0;
    circle_dfs(1,1,1u<<1,0);
    if(cycle_count!=expected_circle[n]){
      fprintf(stderr,"CIRCLE_FAIL %d %llu\n",n,(unsigned long long)cycle_count);return 4;
    }
    if(n<=12){
       line_count=0;line_dfs(0,0,0,0);
       if(line_count!=expected_line[n]){
         fprintf(stderr,"LINE_FAIL %d %llu\n",n,(unsigned long long)line_count);return 5;
       }
    }
    printf("n=%d circle=%llu",n,(unsigned long long)cycle_count);
    if(n<=12)printf(" line=%llu",(unsigned long long)line_count);
    printf(" L=%llu\n",(unsigned long long)L);
  }
  puts("VERIFY_OK");return 0;
}
