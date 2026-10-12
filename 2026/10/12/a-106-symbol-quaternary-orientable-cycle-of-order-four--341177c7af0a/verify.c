/* Independent literal factor-pair verification for a cyclic four-letter word. */
#include <assert.h>
#include <stdio.h>
#include <string.h>
int main(void) {
  FILE *f = fopen("witness.txt", "r");
  if (!f) { perror("witness.txt"); return 2; }
  char word[256] = {0};
  if (fscanf(f,"%255s",word) != 1) return 2;
  fclose(f);
  int n = (int)strlen(word);
  assert(n == 106);
  for (int i = 0; i < n; ++i) assert(word[i] >= '0' && word[i] <= '3');
  for (int i = 0; i < n; ++i) {
    int a[4];
    for (int t = 0; t < 4; ++t) a[t] = word[(i+t)%n]-'0';
    assert(a[0] != a[3] || a[1] != a[2]);
    for (int j = 0; j < i; ++j) {
      int fwd=1, rev=1;
      for (int t = 0; t < 4; ++t) {
        int b = word[(j+t)%n]-'0';
        if (a[t] != b) fwd=0;
        if (a[3-t] != b) rev=0;
      }
      assert(!fwd && !rev);
    }
  }
  puts("VERIFY_OK cyclic_length=106 all_5565_factor_pairs_distinct_under_reversal");
  return 0;
}
