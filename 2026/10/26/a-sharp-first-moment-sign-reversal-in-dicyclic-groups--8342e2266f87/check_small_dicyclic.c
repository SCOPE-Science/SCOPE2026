/* Exhaustive group-table cross-check for Dic_n, 2 <= n <= 6.
 * Compile: cc -O2 -std=c11 check_small_dicyclic.c -o check_small_dicyclic
 * Run: ./check_small_dicyclic
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>

static int product(int x, int y, int n) {
  const int m = 2*n, i = x%m, j = y%m;
  const int b = x/m, c = y/m;
  int e = (i + (b ? -j : j) + ((b && c) ? n : 0) + 2*m) % m;
  return e + (b ^ c)*m;
}
static int cardinality(uint64_t mask) {return __builtin_popcountll(mask);}
int main(void) {
  const uint64_t want_pos[] = {0,0,16,354,3920,48060,462790};
  const uint64_t want_neg[] = {0,0,48,588,8536,92200,1036332};
  const int64_t want_m1[] = {0,0,-32,-156,-5376,-47280,-779184};
  for(int n=2; n<=6; n++) {
    int k = 4*n;
    int table[24][24], inverse[24], quotient[24][24];
    for(int i=0;i<k;i++) for(int j=0;j<k;j++) table[i][j]=product(i,j,n);
    for(int i=0;i<k;i++) {
      inverse[i]=-1;
      for(int j=0;j<k;j++) if(table[i][j]==0 && table[j][i]==0) {
        if(inverse[i]!=-1) return 2;
        inverse[i]=j;
      }
      if(inverse[i]<0) return 3;
    }
    for(int i=0;i<k;i++) for(int j=0;j<k;j++) quotient[i][j]=table[i][inverse[j]];
    for(int i=0;i<k;i++) for(int j=0;j<k;j++) for(int z=0;z<k;z++)
      if(table[table[i][j]][z]!=table[i][table[j][z]]) return 4;
    uint64_t pos=0,neg=0,zero=0;
    int64_t moment=0;
    for(uint64_t subset=0; subset<(UINT64_C(1)<<k); subset++) {
      uint64_t P=0,Q=0;
      for(uint64_t xs=subset;xs;xs&=xs-1) {
        int i=__builtin_ctzll(xs);
        for(uint64_t ys=subset;ys;ys&=ys-1) {
          int j=__builtin_ctzll(ys);
          P|=UINT64_C(1)<<table[i][j];
          Q|=UINT64_C(1)<<quotient[i][j];
        }
      }
      int d=cardinality(P)-cardinality(Q);
      if(d>0)pos++;else if(d<0)neg++;else zero++;
      moment+=d;
    }
    if(pos!=want_pos[n] || neg!=want_neg[n] || moment!=want_m1[n] ||
       pos+neg+zero!=(UINT64_C(1)<<k)) return 5;
    printf("GROUP_OK n=%d order=%d MPTQ=%" PRIu64 " MQTP=%" PRIu64
           " BAL=%" PRIu64 " M1=%" PRId64 "\n",n,k,pos,neg,zero,moment);
  }
  return 0;
}
