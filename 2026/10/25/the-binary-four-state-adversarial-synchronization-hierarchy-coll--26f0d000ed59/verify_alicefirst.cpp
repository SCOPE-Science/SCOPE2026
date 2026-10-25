// Exact two-letter adversarial synchronization census for three and four states.
// Transition tables enumerate all labeled ordered maps; no sampling is used.
#include <cstdio>
#include <cstdint>
#include <cassert>

int main() {
  for (int n = 3; n <= 4; ++n) {
    int pair[8][2] = {}, index[8][8], m = 0;
    for (int i = 0; i < 8; ++i)
      for (int j = 0; j < 8; ++j) index[i][j] = -1;
    for (int i = 0; i < n; ++i)
      for (int j = i + 1; j < n; ++j) {
        pair[m][0] = i; pair[m][1] = j;
        index[i][j] = index[j][i] = m++;
      }
    int total = 1;
    for (int i = 0; i < 2*n; ++i) total *= n;
    long long counts[8] = {};
    for (int key = 0; key < total; ++key) {
      int tab[2][8] = {}, tmp = key;
      for (int a = 0; a < 2; ++a)
        for (int q = 0; q < n; ++q) { tab[a][q] = tmp % n; tmp /= n; }
      int go[2][8] = {};
      for (int a = 0; a < 2; ++a)
        for (int p = 0; p < m; ++p) {
          int i = tab[a][pair[p][0]], j = tab[a][pair[p][1]];
          go[a][p] = (i == j) ? m : index[i][j];
        }
      // after[k][p] encodes all non-sink endpoints reachable from p
      // by adversarial words of length strictly smaller than k.
      unsigned after[8][8] = {};
      for (int p = 0; p < m; ++p) after[1][p] = 1u << p;
      for (int k = 2; k <= m; ++k)
        for (int p = 0; p < m; ++p) {
          unsigned u = after[k-1][p];
          for (int a = 0; a < 2; ++a) {
            int q = go[a][p];
            if (q < m) u |= after[k-1][q];
          }
          after[k][p] = u;
        }
      for (int k = 1; k <= m; ++k) {
        unsigned won = 0;
        // Alice chooses a letter, then Bob chooses any word of length < k.
        // Winning positions are the least fixed point of this attractor.
        while (true) {
          unsigned grown = won;
          for (int p = 0; p < m; ++p) if (!(won & (1u << p)))
            for (int a = 0; a < 2; ++a) {
              int q = go[a][p];
              if (q == m || !(after[k][q] & ~won)) {
                grown |= 1u << p; break;
              }
            }
          if (grown == won) break;
          won = grown;
        }
        counts[k] += (won == ((1u << m) - 1));
      }
    }
    printf("n=%d total=%d",n,total);
    for (int k = 1; k <= m; ++k) printf(" A%d=%lld",k,counts[k]);
    puts("");
    if (n==3) {
      assert(total == 729 && counts[1] == 549 && counts[2] == 381 && counts[3] == 381);
    } else {
      assert(total == 65536 && counts[1] == 51520 && counts[2] == 25360);
      for (int k = 3; k <= 6; ++k) assert(counts[k] == 22384);
    }
  }
  puts("ALICE_FIRST_VERIFY_OK");
}
