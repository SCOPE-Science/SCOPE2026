/* Route B: lexicographic next_permutation; chained-comparison occurrence
 * search per base (shared across patterns); rectangle point-count shading
 * test (no occurrence skip: occurrence points lie on region boundary);
 * quadruples descending.
 * Usage: ./enumB -> prints per-pattern counts for n=1..10.
 * Same frozen window W as Route A; deliberately different code paths.
 */
#include <stdio.h>

static int cellc[8] = {0, 0, 1, 2, 0, 0, 1, 2};
static int cellr[8] = {0, 1, 1, 2, 0, 1, 1, 2};
static long counts[8][11];
static long classical[2][11];
static int occA[300][4], noccA;
static int occB[300][4], noccB;

static void find_occ(int *t, int n) {
    noccA = 0; noccB = 0;
    for (int i4 = n - 1; i4 >= 3; i4--)
        for (int i3 = i4 - 1; i3 >= 2; i3--)
            for (int i2 = i3 - 1; i2 >= 1; i2--)
                for (int i1 = i2 - 1; i1 >= 0; i1--) {
                    int a = t[i1], b = t[i2], c = t[i3], d = t[i4];
                    if (a < c && c < b && b < d) {
                        occA[noccA][0] = i1; occA[noccA][1] = i2;
                        occA[noccA][2] = i3; occA[noccA][3] = i4;
                        noccA++;
                    } else if (b < a && a < d && d < c) {
                        occB[noccB][0] = i1; occB[noccB][1] = i2;
                        occB[noccB][2] = i3; occB[noccB][3] = i4;
                        noccB++;
                    }
                }
}

/* descending bubble sort of 4 values -> ascending S; rectangle point count */
static int shade_free(int cc, int cr, int n, int *t,
                      int i1, int i2, int i3, int i4,
                      int a, int b, int c, int d) {
    int I[4] = {i1, i2, i3, i4};
    int v[4] = {a, b, c, d};
    for (int x = 0; x < 3; x++)
        for (int y = 0; y < 3 - x; y++)
            if (v[y] < v[y + 1]) {
                int tmp = v[y]; v[y] = v[y + 1]; v[y + 1] = tmp;
            }
    int S[4] = {v[3], v[2], v[1], v[0]};
    int xlo = (cc == 0) ? -1 : I[cc - 1];
    int xhi = (cc == 4) ? n : I[cc];
    int ylo = (cr == 0) ? -1 : S[cr - 1];
    int yhi = (cr == 4) ? n : S[cr];
    int cnt = 0;
    for (int j = 0; j < n; j++)
        if (xlo < j && j < xhi && ylo < t[j] && t[j] < yhi)
            cnt++;
    return cnt == 0;
}

static int next_perm(int *t, int n) {
    int i = n - 2;
    while (i >= 0 && t[i] > t[i + 1]) i--;
    if (i < 0) return 0;
    int j = n - 1;
    while (t[j] < t[i]) j--;
    int tmp = t[i]; t[i] = t[j]; t[j] = tmp;
    int lo = i + 1, hi = n - 1;
    while (lo < hi) {
        tmp = t[lo]; t[lo] = t[hi]; t[hi] = tmp;
        lo++; hi--;
    }
    return 1;
}

int main(void) {
    int t[10];
    for (int n = 1; n <= 10; n++) {
        for (int j = 0; j < n; j++) t[j] = j;
        do {
            find_occ(t, n);
            for (int m = 0; m < 8; m++) {
                int hit = 0;
                int (*occ)[4] = (m < 4) ? occA : occB;
                int nocc = (m < 4) ? noccA : noccB;
                for (int q = 0; q < nocc; q++) {
                    int i1 = occ[q][0], i2 = occ[q][1];
                    int i3 = occ[q][2], i4 = occ[q][3];
                    if (shade_free(cellc[m], cellr[m], n, t, i1, i2, i3, i4,
                                   t[i1], t[i2], t[i3], t[i4])) {
                        hit = 1; break;
                    }
                }
                if (!hit) counts[m][n]++;
            }
            if (noccA == 0) classical[0][n]++;
            if (noccB == 0) classical[1][n]++;
        } while (next_perm(t, n));
        fprintf(stderr, "B: n=%d done\n", n);
    }
    for (int m = 0; m < 8; m++) {
        printf("MESH_B M%d", m);
        for (int n = 1; n <= 10; n++) printf(" %ld", counts[m][n]);
        printf("\n");
    }
    printf("CLASS_B B0");
    for (int n = 1; n <= 10; n++) printf(" %ld", classical[0][n]);
    printf("\n");
    printf("CLASS_B B1");
    for (int n = 1; n <= 10; n++) printf(" %ld", classical[1][n]);
    printf("\n");
    return 0;
}
