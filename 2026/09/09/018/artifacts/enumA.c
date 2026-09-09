/* Engine A: max-insertion generating tree with specialized active-site tests.
   Usage: ./enumA 1324|1342|joint NMAX outprefix
   Writes <outprefix>_prof.csv and <outprefix>_trans.csv to stdout files.
   Perm values 1..m, gap g in 0..m means insert value m+1 at position g.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int CLS; /*0=1324 1=1342 2=joint*/
static int NMAX;
static long long prof[16][18];
static long long trans[16][18][18];

/* compute active gaps; returns k, fills act[] */
static int active_gaps(unsigned char *p, int m, int *act) {
    int forb[16] = {0};
    int g, i1, i2, i3;
    if (CLS == 0 || CLS == 2) {
        /* 1324: gap g forbidden iff prefix [0,g) contains a 132 triple.
           New max plays pattern-role 4 (last). */
        /* mark forbidden via min-end: compute has132[g] */
        for (g = 0; g <= m; g++) {
            int has = 0;
            for (i1 = 0; i1 < g && !has; i1++)
                for (i2 = i1 + 1; i2 < g && !has; i2++)
                    for (i3 = i2 + 1; i3 < g && !has; i3++) {
                        unsigned char a = p[i1], b = p[i2], c = p[i3];
                        if (a < c && c < b) has = 1; /* 132 */
                    }
            if (has) forb[g] = 1;
        }
    }
    if (CLS == 1 || CLS == 2) {
        /* 1342: gap g forbidden iff exists i1<i2<g<=i3 with p[i1]<p[i3]<p[i2].
           New max plays pattern-role 3. Use prefix minima + difference array. */
        int pmin[16];
        int diff[17] = {0};
        if (m > 0) {
            pmin[0] = 999;
            for (i2 = 1; i2 <= m; i2++) {
                int prev = p[i2 - 1];
                pmin[i2] = pmin[i2 - 1] < prev ? pmin[i2 - 1] : prev;
            }
            /* pmin[i2] = min of p[0..i2-1] */
            for (i2 = 0; i2 < m; i2++)
                for (i3 = i2 + 1; i3 < m; i3++) {
                    unsigned char b = p[i2], c = p[i3];
                    if (c < b && pmin[i2] < c) {
                        diff[i2 + 1]++; diff[i3 + 1]--;
                    }
                }
            int cur = 0;
            for (g = 0; g <= m; g++) { cur += diff[g]; if (cur > 0) forb[g] = 1; }
        }
    }
    int k = 0;
    for (g = 0; g <= m; g++) if (!forb[g]) act[k++] = g;
    return k;
}

static void dfs(unsigned char *p, int m) {
    int act[16], chact[16];
    int k = active_gaps(p, m, act);
    prof[m][k]++;
    if (m >= NMAX) return;
    unsigned char ch[16];
    for (int t = 0; t < k; t++) {
        int g = act[t];
        for (int i = 0; i < g; i++) ch[i] = p[i];
        ch[g] = (unsigned char)(m + 1);
        for (int i = g; i < m; i++) ch[i + 1] = p[i];
        int jk = active_gaps(ch, m + 1, chact);
        trans[m][k][jk]++;
        dfs(ch, m + 1);
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: enumA 1324|1342|joint NMAX outprefix\n"); return 1; }
    if (!strcmp(argv[1], "1324")) CLS = 0;
    else if (!strcmp(argv[1], "1342")) CLS = 1;
    else if (!strcmp(argv[1], "joint")) CLS = 2;
    else { fprintf(stderr, "bad class\n"); return 1; }
    NMAX = atoi(argv[2]);
    const char *pre = argv[3];
    unsigned char root[16] = {0};
    dfs(root, 0);
    char fn[256];
    snprintf(fn, sizeof fn, "%s_prof.csv", pre);
    FILE *f = fopen(fn, "w");
    fprintf(f, "n,k,count\n");
    for (int n = 0; n <= NMAX; n++)
        for (int k = 0; k <= n + 1; k++)
            if (prof[n][k]) fprintf(f, "%d,%d,%lld\n", n, k, prof[n][k]);
    fclose(f);
    snprintf(fn, sizeof fn, "%s_trans.csv", pre);
    f = fopen(fn, "w");
    fprintf(f, "m,k,j,count\n");
    for (int m = 0; m < NMAX; m++)
        for (int k = 0; k <= m + 1; k++)
            for (int j = 0; j <= m + 2; j++)
                if (trans[m][k][j]) fprintf(f, "%d,%d,%d,%lld\n", m, k, j, trans[m][k][j]);
    fclose(f);
    /* marginals to stderr */
    for (int n = 0; n <= NMAX; n++) {
        long long s = 0;
        for (int k = 0; k <= n + 1; k++) s += prof[n][k];
        fprintf(stderr, "A len=%d total=%lld\n", n, s);
    }
    return 0;
}
