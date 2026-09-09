/* Antichain rank-profile enumerator for rank-selected Boolean slices.
 *
 * Poset P = { S subset of [N] : rmin <= |S| <= rmax }, inclusion order.
 * Enumerates ALL antichains by include/exclude backtracking over the NE
 * elements (grouped by rank), skipping elements already comparable to the
 * current antichain. Tabulates the rank-profile frequency table:
 *   profile (a_rmin,...,a_rmax) -> number of antichains with that profile
 * and stores one witness antichain per occurring profile cell.
 *
 * Usage: ./enum N rmin rmax outprefix
 * Outputs: <pre>_profiles.csv, <pre>_witnesses.csv, <pre>_summary.txt
 *
 * Deterministic: fixed element order (rank-major, ground-mask-minor), so
 * reruns reproduce the outputs bit-for-bit (FNV-1a hash logged in summary).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int N, RMIN, RMAX, NR, NE;
static uint64_t CMP[64];
static int ERANK[64], EMASK[64], LAYSIZE[64], DIM[8], STRIDE[8];
static uint64_t *TABLE, *WIT, *SIZEDIST;
static unsigned char *HASWIT;
static size_t NCELL;
static uint64_t TOTAL, MAXSIZE;

static int popcnt(int x) { int c = 0; while (x) { c += x & 1; x >>= 1; } return c; }

static void record_antichain(uint64_t chosen, int *cnt) {
    size_t idx = 0; int s = 0;
    for (int r = 0; r < NR; r++) { idx += (size_t)cnt[r] * (size_t)STRIDE[r]; s += cnt[r]; }
    if (!HASWIT[idx]) { WIT[idx] = chosen; HASWIT[idx] = 1; }
    TABLE[idx]++; SIZEDIST[s]++; TOTAL++;
    if ((uint64_t)s > MAXSIZE) MAXSIZE = (uint64_t)s;
}

static void rec(int i, uint64_t forb, uint64_t chosen, int *cnt) {
    while (i < NE && ((forb >> i) & 1ULL)) i++;
    if (i >= NE) { record_antichain(chosen, cnt); return; }
    rec(i + 1, forb, chosen, cnt);                       /* exclude i */
    cnt[ERANK[i] - RMIN]++;
    rec(i + 1, forb | CMP[i], chosen | (1ULL << i), cnt); /* include i */
    cnt[ERANK[i] - RMIN]--;
}

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: %s N rmin rmax outprefix\n", argv[0]); return 2; }
    N = atoi(argv[1]); RMIN = atoi(argv[2]); RMAX = atoi(argv[3]);
    const char *pre = argv[4];
    NR = RMAX - RMIN + 1;
    if (N < 1 || N > 6 || NR < 1 || NR > 6 || RMIN < 0 || RMAX > N) return 2;

    NE = 0;
    for (int r = RMIN; r <= RMAX; r++)
        for (int m = 0; m < (1 << N); m++)
            if (popcnt(m) == r) { ERANK[NE] = r; EMASK[NE] = m; NE++; }

    for (int r = 0; r < 64; r++) LAYSIZE[r] = 0;
    for (int i = 0; i < NE; i++) LAYSIZE[ERANK[i]]++;
    for (int i = 0; i < NE; i++) {
        uint64_t c = 0;
        for (int j = 0; j < NE; j++) {
            int a = EMASK[i], b = EMASK[j];
            if (((a & b) == a) || ((a & b) == b)) c |= (1ULL << j);
        }
        CMP[i] = c;
    }

    NCELL = 1;
    for (int r = 0; r < NR; r++) { DIM[r] = LAYSIZE[RMIN + r] + 1; STRIDE[r] = (int)NCELL; NCELL *= (size_t)DIM[r]; }
    TABLE = (uint64_t *)calloc(NCELL, sizeof(uint64_t));
    WIT = (uint64_t *)malloc(NCELL * sizeof(uint64_t));
    HASWIT = (unsigned char *)calloc(NCELL, 1);
    SIZEDIST = (uint64_t *)calloc((size_t)NE + 1, sizeof(uint64_t));
    if (!TABLE || !WIT || !HASWIT || !SIZEDIST) return 3;

    int cnt[8] = {0,0,0,0,0,0,0,0};
    rec(0, 0, 0, cnt);

    /* FNV-1a 64-bit hash over table + sizedist for bit-for-bit replay check */
    uint64_t h = 1469598103934665603ULL;
    for (size_t k = 0; k < NCELL; k++) {
        uint64_t v = TABLE[k];
        for (int b = 0; b < 8; b++) { h ^= (v & 0xFF); h *= 1099511628211ULL; v >>= 8; }
    }
    for (int s = 0; s <= NE; s++) {
        uint64_t v = SIZEDIST[s];
        for (int b = 0; b < 8; b++) { h ^= (v & 0xFF); h *= 1099511628211ULL; v >>= 8; }
    }
    h ^= TOTAL; h *= 1099511628211ULL;

    char fn[1024]; FILE *f;
    snprintf(fn, sizeof fn, "%s_profiles.csv", pre); f = fopen(fn, "w"); if (!f) return 4;
    for (int r = RMIN; r <= RMAX; r++) fprintf(f, "a%d%s", r, r < RMAX ? "," : "");
    fprintf(f, ",count\n");
    snprintf(fn, sizeof fn, "%s_witnesses.csv", pre);
    FILE *g = fopen(fn, "w"); if (!g) return 4;
    for (int r = RMIN; r <= RMAX; r++) fprintf(g, "a%d%s", r, r < RMAX ? "," : "");
    fprintf(g, ",count,chosen_hex,members\n");

    int cc[8] = {0,0,0,0,0,0,0,0};
    uint64_t nprof = 0, rowsum = 0;
    for (;;) {
        size_t idx = 0;
        for (int r = 0; r < NR; r++) idx += (size_t)cc[r] * (size_t)STRIDE[r];
        if (TABLE[idx] > 0) {
            nprof++; rowsum += TABLE[idx];
            for (int r = 0; r < NR; r++) fprintf(f, "%d%s", cc[r], r < NR - 1 ? "," : "");
            fprintf(f, ",%llu\n", (unsigned long long)TABLE[idx]);
            for (int r = 0; r < NR; r++) fprintf(g, "%d%s", cc[r], r < NR - 1 ? "," : "");
            fprintf(g, ",%llu,%llx,", (unsigned long long)TABLE[idx],
                    (unsigned long long)WIT[idx]);
            int first = 1;
            for (int j = 0; j < NE; j++)
                if ((WIT[idx] >> j) & 1ULL) { fprintf(g, "%s%d", first ? "" : " ", EMASK[j]); first = 0; }
            fprintf(g, "\n");
        }
        int r = 0;
        while (r < NR) { cc[r]++; if (cc[r] < DIM[r]) break; cc[r] = 0; r++; }
        if (r >= NR) break;
    }
    fclose(f); fclose(g);

    snprintf(fn, sizeof fn, "%s_summary.txt", pre); f = fopen(fn, "w"); if (!f) return 4;
    fprintf(f, "N=%d rmin=%d rmax=%d NE=%d\n", N, RMIN, RMAX, NE);
    fprintf(f, "laysizes:");
    for (int r = RMIN; r <= RMAX; r++) fprintf(f, " %d:%d", r, LAYSIZE[r]);
    fprintf(f, "\n");
    fprintf(f, "total=%llu\n", (unsigned long long)TOTAL);
    fprintf(f, "nprofiles=%llu\n", (unsigned long long)nprof);
    fprintf(f, "rowsum=%llu\n", (unsigned long long)rowsum);
    fprintf(f, "maxsize=%llu\n", (unsigned long long)MAXSIZE);
    fprintf(f, "fnv1a=%llx\n", (unsigned long long)h);
    fprintf(f, "sizedist:");
    for (int s = 0; s <= NE; s++) if (SIZEDIST[s]) fprintf(f, " %d:%llu", s, (unsigned long long)SIZEDIST[s]);
    fprintf(f, "\n");
    fclose(f);

    free(TABLE); free(WIT); free(HASWIT); free(SIZEDIST);
    return 0;
}
