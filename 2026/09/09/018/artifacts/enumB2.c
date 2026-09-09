/* Engine B2 (independent): max-insertion tree; active gaps decided by LOCALIZED
   brute force: for candidate child (parent + new max M=m+1 at gap g), every NEW
   forbidden occurrence must use position g (deleting g recovers the parent,
   which is avoiding by DFS induction). So enumerate all index triples from the
   other positions and test whether (triple + g) in positional order is order-
   isomorphic to a forbidden pattern. No incremental/prefix lemma is used;
   ranks are recomputed from scratch per quadruple. O(m^3) triples per gap.
   Usage: ./enumB2 1324|1342|joint NMAX outprefix
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int CLS;
static int NMAX;
static long long prof[16][18];
static long long trans[16][18][18];

/* test quadruple of values (v0,v1,v2,v3) in positional order against basis */
static int hits_basis(unsigned char v0, unsigned char v1, unsigned char v2, unsigned char v3) {
    unsigned char v[4] = {v0, v1, v2, v3};
    int r[4], i, j;
    for (i = 0; i < 4; i++) { r[i] = 0; for (j = 0; j < 4; j++) if (v[j] < v[i]) r[i]++; }
    if ((CLS == 0 || CLS == 2) && r[0] == 0 && r[1] == 2 && r[2] == 1 && r[3] == 3) return 1;
    if ((CLS == 1 || CLS == 2) && r[0] == 0 && r[1] == 2 && r[2] == 3 && r[3] == 1) return 1;
    return 0;
}

/* is gap g active for parent p[0..m)? build child values virtually */
static int gap_ok(unsigned char *p, int m, int g) {
    int M = m + 1;
    int a, b, c;
    /* positions in child: 0..m; value at g is M, else p shifted */
#define CVAL(pos) ((pos) < g ? p[(pos)] : ((pos) == g ? M : p[(pos)-1]))
    for (a = 0; a <= m; a++)
        for (b = a + 1; b <= m; b++)
            for (c = b + 1; c <= m; c++) {
                for (int d = c + 1; d <= m; d++) {
                    /* occurrences avoiding g live in the (avoiding) parent:
                       only quadruples using position g can be new */
                    if (a != g && b != g && c != g && d != g) continue;
                    if (hits_basis(CVAL(a), CVAL(b), CVAL(c), CVAL(d))) return 0;
                }
            }
#undef CVAL
    return 1;
}

static int node_k(unsigned char *p, int m) {
    int cnt = 0;
    for (int g = 0; g <= m; g++) if (gap_ok(p, m, g)) cnt++;
    return cnt;
}

static void dfs(unsigned char *p, int m) {
    int act[16], nk = 0;
    for (int g = 0; g <= m; g++) if (gap_ok(p, m, g)) act[nk++] = g;
    prof[m][nk]++;
    if (m >= NMAX) return;
    unsigned char ch[16];
    for (int t = 0; t < nk; t++) {
        int g = act[t];
        for (int i = 0; i < g; i++) ch[i] = p[i];
        ch[g] = (unsigned char)(m + 1);
        for (int i = g; i < m; i++) ch[i + 1] = p[i];
        int jk = node_k(ch, m + 1);
        trans[m][nk][jk]++;
        dfs(ch, m + 1);
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: enumB2 1324|1342|joint NMAX outprefix\n"); return 1; }
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
    for (int n = 0; n <= NMAX; n++) {
        long long s = 0;
        for (int k = 0; k <= n + 1; k++) s += prof[n][k];
        fprintf(stderr, "B2 len=%d total=%lld\n", n, s);
    }
    return 0;
}
