/* Route A: recursive prefix-DFS; rank-counting occurrence search per base
 * (shared across the 4 patterns of that base); half-open interval shading
 * scan with occurrence skip; quadruples ascending.
 * Usage: ./enumA -> prints per-pattern counts for n=1..10.
 * Window W frozen in WORKLOG §1. Single shaded cell per pattern.
 */
#include <stdio.h>

static int cellc[8] = {0, 0, 1, 2, 0, 0, 1, 2};
static int cellr[8] = {0, 1, 1, 2, 0, 1, 1, 2};
static int N;
static int perm[10];
static int used[10];
static long counts[8][11];
static long classical[2][11];
/* occurrence lists: packed (i1,i2,i3,i4) bytes */
static int occA[300][4], noccA;
static int occB[300][4], noccB;

static void find_occ(int *t, int n) {
    noccA = 0; noccB = 0;
    for (int i1 = 0; i1 < n; i1++)
        for (int i2 = i1 + 1; i2 < n; i2++)
            for (int i3 = i2 + 1; i3 < n; i3++)
                for (int i4 = i3 + 1; i4 < n; i4++) {
                    int a = t[i1], b = t[i2], c = t[i3], d = t[i4];
                    int ra = (a > b) + (a > c) + (a > d);
                    int rb = (b > a) + (b > c) + (b > d);
                    int rc = (c > a) + (c > b) + (c > d);
                    int rd = 6 - ra - rb - rc;
                    if (ra == 0 && rb == 2 && rc == 1 && rd == 3) {
                        occA[noccA][0] = i1; occA[noccA][1] = i2;
                        occA[noccA][2] = i3; occA[noccA][3] = i4;
                        noccA++;
                    } else if (ra == 1 && rb == 0 && rc == 3 && rd == 2) {
                        occB[noccB][0] = i1; occB[noccB][1] = i2;
                        occB[noccB][2] = i3; occB[noccB][3] = i4;
                        noccB++;
                    }
                }
}

/* shading test for occurrence (i's, values a..d) with value-sort via insertion sort */
static int shade_free(int cc, int cr, int n, int *t,
                      int i1, int i2, int i3, int i4,
                      int a, int b, int c, int d) {
    int I[4] = {i1, i2, i3, i4};
    int S[4] = {a, b, c, d};
    for (int k = 1; k < 4; k++) {
        int key = S[k], l = k - 1;
        while (l >= 0 && S[l] > key) { S[l + 1] = S[l]; l--; }
        S[l + 1] = key;
    }
    int xlo = (cc == 0) ? -1 : I[cc - 1];
    int xhi = (cc == 4) ? n : I[cc];
    int ylo = (cr == 0) ? -1 : S[cr - 1];
    int yhi = (cr == 4) ? n : S[cr];
    for (int j = xlo + 1; j <= xhi - 1; j++) {
        if (j == i1 || j == i2 || j == i3 || j == i4) continue;
        if (t[j] > ylo && t[j] < yhi) return 0;
    }
    return 1;
}

static void dfs(int pos) {
    if (pos == N) {
        find_occ(perm, N);
        if (noccA == 0) {
            for (int m = 0; m < 4; m++) counts[m][N]++;
        } else {
            for (int m = 0; m < 4; m++) {
                int hit = 0;
                for (int q = 0; q < noccA; q++) {
                    int i1 = occA[q][0], i2 = occA[q][1];
                    int i3 = occA[q][2], i4 = occA[q][3];
                    if (shade_free(cellc[m], cellr[m], N, perm, i1, i2, i3, i4,
                                   perm[i1], perm[i2], perm[i3], perm[i4])) {
                        hit = 1; break;
                    }
                }
                if (!hit) counts[m][N]++;
            }
        }
        if (noccB == 0) {
            for (int m = 4; m < 8; m++) counts[m][N]++;
        } else {
            for (int m = 4; m < 8; m++) {
                int hit = 0;
                for (int q = 0; q < noccB; q++) {
                    int i1 = occB[q][0], i2 = occB[q][1];
                    int i3 = occB[q][2], i4 = occB[q][3];
                    if (shade_free(cellc[m], cellr[m], N, perm, i1, i2, i3, i4,
                                   perm[i1], perm[i2], perm[i3], perm[i4])) {
                        hit = 1; break;
                    }
                }
                if (!hit) counts[m][N]++;
            }
        }
        if (noccA == 0) classical[0][N]++;
        if (noccB == 0) classical[1][N]++;
        return;
    }
    for (int v = 0; v < N; v++) {
        if (!used[v]) {
            used[v] = 1;
            perm[pos] = v;
            dfs(pos + 1);
            used[v] = 0;
        }
    }
}

int main(void) {
    for (int n = 1; n <= 10; n++) {
        N = n;
        for (int v = 0; v < n; v++) used[v] = 0;
        dfs(0);
        fprintf(stderr, "A: n=%d done\n", n);
    }
    for (int m = 0; m < 8; m++) {
        printf("MESH_A M%d", m);
        for (int n = 1; n <= 10; n++) printf(" %ld", counts[m][n]);
        printf("\n");
    }
    printf("CLASS_A B0");
    for (int n = 1; n <= 10; n++) printf(" %ld", classical[0][n]);
    printf("\n");
    printf("CLASS_A B1");
    for (int n = 1; n <= 10; n++) printf(" %ld", classical[1][n]);
    printf("\n");
    return 0;
}
