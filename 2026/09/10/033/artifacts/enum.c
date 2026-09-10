/* Max-insertion enumeration of U=Av(2413,3142), C1=Av(+123654), C2=Av(+321654).
   Incremental checks using the new maximum element (value m+1 at slot j).
   - Separable child check: only 4-sets through j can be new 2413/3142. O(m^2).
   - T-filters: max of T (value 6 at index 3 in both) must be the new max. O(m).
   DFS from level-7 seeds, OpenMP parallel over seeds.
   Usage: ./enum N [only1|only2|all]  (N = max depth; class-restricted DFS prunes
   to C1/C2 subtrees for deeper counts)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifdef _OPENMP
#include <omp.h>
#endif

static int NMAX;
static long long cntU[32], cnt1[32], cnt2[32];
// first symmetric-difference witnesses per level
static int wit12[32][32], wit21[32][32]; // wit12[m] = first perm in C1\C2 at level m
static int have12[32], have21[32];

/* check child a[0..m] (len m+1), new max at j, parent was separable.
   return 1 if child avoids 2413 & 3142. */
static inline int sep_ok(const int *a, int m, int j) {
    int i1, i3, i4;
    // 2413: i1<j<i3<i4, a[i3]<a[i1]<a[i4]. suffix max over (j..m]
    // sufmax[k] = max_{i in [k,m]} a[i]
    int suf[32];
    suf[m] = a[m];
    for (int k = m - 1; k > j; k--) suf[k] = a[k] > suf[k+1] ? a[k] : suf[k+1];
    for (i1 = 0; i1 < j; i1++) {
        for (i3 = j + 1; i3 <= m; i3++) {
            if (a[i3] < a[i1] && (i3 + 1 > m ? -1 : suf[i3+1]) > a[i1]) return 0;
        }
    }
    // 3142: i1<i2<j<i4, a[i2]<a[i4]<a[i1]. prefmax[i2]=max_{i1<i2} a[i1]
    int pre = a[0];
    for (int i2 = 1; i2 < j; i2++) {
        if (a[i2-1] > pre) pre = a[i2-1];
        for (i4 = j + 1; i4 <= m; i4++) {
            if (a[i2] < a[i4] && a[i4] < pre) return 0;
        }
    }
    // note i2=0: no i1<0, skip (loop starts at 1). Correct.
    return 1;
}

/* New occurrence of T through new max at j. T1=123654: inc triple before j,
   dec pair after j. T2=321654: dec triple before j, dec pair after j.
   (Unused draft removed; scans below are the tested versions.) */

/* Exact incremental T-hit test (validated logic):
   Child b[0..m], new global max at slot j. A new T1=123654 (resp. T2=321654)
   occurrence through j exists iff: inc-triple (resp. dec-triple) at indices
   < j plus dec-pair at indices > j with max(triple) < min(pair).
   Compute t1min = min possible max-value of a 123-triple in b[0..j);
   t2min = min possible max-value of a 321-triple in b[0..j);
   p2max = max possible min-value of a 21-pair in b(j..m].
   New hits: h1 = (t1min < p2max), h2 = (t2min < p2max). O(m^2). */
static inline void thit(const int *b, int m, int j, int *h1, int *h2) {
    const int INF = 1000000;
    int t1min = INF, t2min = INF, p2max = -1;
    if (j >= 3) {
        // inc-triple min-max: for each middle i2, need smaller before + larger after
        for (int i2 = 1; i2 < j; i2++) {
            int pre = 0;
            for (int i1 = 0; i1 < i2; i1++)
                if (b[i1] < b[i2]) { pre = 1; break; }
            if (!pre) continue;
            for (int i3 = i2 + 1; i3 < j; i3++)
                if (b[i3] > b[i2] && b[i3] < t1min) t1min = b[i3];
        }
        // dec-triple min-max: max of triple is its first element; minimize it
        for (int i1 = 0; i1 < j; i1++) {
            if (b[i1] >= t2min) continue; // cannot improve
            int found = 0;
            for (int i2 = i1 + 1; i2 < j && !found; i2++) {
                if (b[i2] >= b[i1]) continue;
                for (int i3 = i2 + 1; i3 < j; i3++) {
                    if (b[i3] < b[i2]) { found = 1; break; }
                }
            }
            if (found && b[i1] < t2min) t2min = b[i1];
        }
    }
    if (j + 2 <= m) {
        for (int k1 = j + 1; k1 < m; k1++) {
            int pmax = -1;
            for (int k2 = k1 + 1; k2 <= m; k2++)
                if (b[k2] < b[k1] && b[k2] > pmax) pmax = b[k2];
            if (pmax > p2max) p2max = pmax;
        }
    }
    *h1 = (t1min < p2max);
    *h2 = (t2min < p2max);
}

static int MODE; // 0=all, 1=only C1 subtree, 2=only C2 subtree

static void dfs(int *a, int m, int t1, int t2) {
    // a[0..m-1] current perm of length m; count it
#pragma omp atomic
    cntU[m]++;
    if (!t1) {
#pragma omp atomic
        cnt1[m]++;
    }
    if (!t2) {
#pragma omp atomic
        cnt2[m]++;
    }
    if (m >= NMAX) return;
    if (MODE == 1 && t1) return;
    if (MODE == 2 && t2) return;
    // record witnesses
    if ((!t1 && t2 && !have12[m]) || (!t2 && t1 && !have21[m])) {
#pragma omp critical
        {
            if (!t1 && t2 && !have12[m]) {
                have12[m] = 1;
                for (int i = 0; i < m; i++) wit12[m][i] = a[i];
            }
            if (!t2 && t1 && !have21[m]) {
                have21[m] = 1;
                for (int i = 0; i < m; i++) wit21[m][i] = a[i];
            }
        }
    }
    int b[32];
    for (int j = 0; j <= m; j++) {
        for (int i = 0; i < j; i++) b[i] = a[i];
        b[j] = m + 1;
        for (int i = j; i < m; i++) b[i+1] = a[i];
        if (!sep_ok(b, m, j)) continue;
        int n1 = t1, n2 = t2;
        if (!n1 || !n2) {
            int h1 = 0, h2 = 0;
            thit(b, m, j, &h1, &h2);
            if (h1) n1 = 1;
            if (h2) n2 = 1;
        }
        if (MODE == 1 && n1) continue;
        if (MODE == 2 && n2) continue;
        dfs(b, m + 1, n1, n2);
    }
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: enum N [all|only1|only2]\n"); return 1; }
    NMAX = atoi(argv[1]);
    MODE = 0;
    if (argc >= 3) {
        if (!strcmp(argv[2], "only1")) MODE = 1;
        if (!strcmp(argv[2], "only2")) MODE = 2;
    }
    // build seeds to length 7
    static int seeds[2000][8];
    int nseeds = 1;
    seeds[0][0] = 0; // len 0
    int lens[2000]; lens[0] = 0;
    int tmp[32];
    for (int m = 0; m < 7; m++) {
        int nn = 0;
        static int ns[50000][8];
        for (int s = 0; s < nseeds; s++) {
            int *a = seeds[s];
            for (int j = 0; j <= m; j++) {
                for (int i = 0; i < j; i++) tmp[i] = a[i];
                tmp[j] = m + 1;
                for (int i = j; i < m; i++) tmp[i+1] = a[i];
                if (!sep_ok(tmp, m, j)) continue;
                for (int i = 0; i <= m; i++) ns[nn][i] = tmp[i];
                lens[nn] = m + 1;
                nn++;
            }
        }
        nseeds = nn;
        for (int s = 0; s < nseeds; s++)
            for (int i = 0; i < 8; i++) seeds[s][i] = ns[s][i];
    }
    printf("seeds at len 7: %d\n", nseeds);
    fflush(stdout);
#pragma omp parallel
    {
        int loc[32];
#pragma omp for schedule(dynamic)
        for (int s = 0; s < nseeds; s++) {
            for (int i = 0; i < 7; i++) loc[i] = seeds[s][i];
            // t1/t2 flags at len 7: brute force check small perms directly
            int t1 = 0, t2 = 0;
            // 6-subsets of 7 elements
            for (int skip = 0; skip < 7 && (!t1 || !t2); skip++) {
                int p[6], q = 0;
                for (int i = 0; i < 7; i++) if (i != skip) p[q++] = loc[i];
                // standardize
                int r[6];
                for (int i = 0; i < 6; i++) {
                    int c = 1;
                    for (int k = 0; k < 6; k++) if (p[k] < p[i]) c++;
                    r[i] = c;
                }
                if (r[0]==1&&r[1]==2&&r[2]==3&&r[3]==6&&r[4]==5&&r[5]==4) t1=1;
                if (r[0]==3&&r[1]==2&&r[2]==1&&r[3]==6&&r[4]==5&&r[5]==4) t2=1;
            }
            dfs(loc, 7, t1, t2);
        }
    }
    // merge: counts accumulated with atomics? Use critical — instead use reduction via atomic updates
    printf("N, U, C1, C2\n");
    for (int m = 0; m <= NMAX; m++)
        printf("%d %lld %lld %lld\n", m, cntU[m], cnt1[m], cnt2[m]);
    for (int m = 0; m <= NMAX; m++) {
        if (have12[m]) {
            printf("WIT12[%d]:", m);
            for (int i = 0; i < m; i++) printf(" %d", wit12[m][i]);
            printf("\n");
        }
        if (have21[m]) {
            printf("WIT21[%d]:", m);
            for (int i = 0; i < m; i++) printf(" %d", wit21[m][i]);
            printf("\n");
        }
    }
    return 0;
}
