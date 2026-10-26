/* Standalone exhaustive certificate for the degree-26 seven-factor onset.
   Compile: cc -O2 -std=c11 -Wall -Wextra verify.c -o verify && ./verify
   Polynomials over F_2 use little-endian coefficient bit masks. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static int degree(uint32_t a) { int d=-1; while(a){a>>=1;d++;}return d; }
static uint32_t rem(uint32_t a,uint32_t b) {
 int db=degree(b); if(db<0) exit(3);
 while(a && degree(a)>=db) a^=b << (degree(a)-db);
 return a;
}
static int irreducible(uint32_t f){
 int d=degree(f);
 if(d<1 || !(f&1)) return 0;
 for(int j=1;j<=d/2;j++) for(uint32_t g=(1u<<j);g<(1u<<(j+1));g++) if(rem(f,g)==0)return 0;
 return 1;
}
static uint32_t mul(uint32_t a,uint32_t b){uint32_t c=0;while(b){if(b&1)c^=a;a<<=1;b>>=1;}return c;}
static uint32_t candidates[2][100]; static int ncan[2];
static void put(int d,uint32_t f){int j=d-25;if(degree(f)!=d||j<0||j>1)abort();for(int k=0;k<ncan[j];k++)if(candidates[j][k]==f)abort();candidates[j][ncan[j]++]=f;}
static uint8_t *seen;
static int target_degree;
static uint32_t witness_poly=123935485u, count_witness;
static uint32_t witness_word;
static int witness_recorded;
static void dfs(int k,uint32_t prev,uint32_t cur,uint32_t word){
 if(k==target_degree){
  if(degree(cur)!=target_degree) abort();
  seen[cur^(1u<<target_degree)]=1;
  if(cur==witness_poly){count_witness++;if(!witness_recorded){witness_word=word;witness_recorded=1;}}
  return;
 }
 dfs(k+1,cur,(cur<<1)^prev,word);
 dfs(k+1,cur,(cur<<1)^cur^prev,word | (1u<<k));
}
static void enumerate(int d){
 target_degree=d;
 seen=calloc((size_t)1u<<d,1);if(!seen){perror("calloc");exit(2);}
 count_witness=0;witness_recorded=0;
 dfs(1,1,2,0); dfs(1,1,3,1);
 int hits=0;
 for(int k=0;k<ncan[d-25];k++){
  uint32_t f=candidates[d-25][k];
  if(seen[f^(1u<<d)]){hits++; printf("positive_degree_%d: %u\n",d,f);if(d!=26||f!=witness_poly)abort();}
 }
 printf("degree_%d_candidates=%d positive=%d\n",d,ncan[d-25],hits);
 if((d==25&&hits!=0)||(d==26&&hits!=1))abort();
 if(d==26){printf("witness_word_mask=%u witness_multiplicity=%u\n",witness_word,count_witness);if(count_witness!=128)abort();}
 free(seen);
}
int main(void){
 uint32_t p2=7, p3a=11,p3b=13,deg4[3],deg5[6],deg6[9];
 int n4=0,n5=0,n6=0;
 for(int d=2;d<=6;d++){
  int count=0;
  for(uint32_t f=(1u<<d);f<(1u<<(d+1));f++)if(irreducible(f)){
   count++;if(d==4)deg4[n4++]=f;if(d==5)deg5[n5++]=f;if(d==6)deg6[n6++]=f;
  }
  printf("irreducibles_degree_%d=%d\n",d,count);
  if(count!=(d==2?1:d==3?2:d==4?3:d==5?6:9))abort();
 }
 uint32_t bas=mul(mul(p2,p3a),p3b);
 uint32_t full4=bas;
 for(int i=0;i<3;i++)full4=mul(full4,deg4[i]);
 for(int j=0;j<6;j++){
  uint32_t f=mul(full4,deg5[j]);put(25,f);put(26,mul(f,2));put(26,mul(f,3));
 }
 for(int j=0;j<9;j++)put(26,mul(full4,deg6[j]));
 for(int omit=0;omit<3;omit++){
  uint32_t f=bas;
  for(int i=0;i<3;i++)if(i!=omit)f=mul(f,deg4[i]);
  for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)put(26,mul(mul(f,deg5[a]),deg5[b]));
 }
 if(ncan[0]!=6||ncan[1]!=66)abort();
 enumerate(25);enumerate(26);
 puts("VERIFY_OK");return 0;
}
