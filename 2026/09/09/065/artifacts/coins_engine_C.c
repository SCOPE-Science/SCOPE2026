// Engine C: independent recount — recursive DFS, descending child order,
// NO dedup (explores all 4 positions; duplicate subtrees allowed), byte-per-value
// converted to identical bitset layout. Guards against common-mode dedup bugs.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

static int64_t LO, BOUND;
static uint8_t *bits;
static uint64_t nodes_;

static inline void bitset_set(int64_t v) {
    uint64_t i = (uint64_t)(v - LO - 1);
    bits[i >> 3] |= (uint8_t)(1u << (i & 7));
}

static void dfs(int32_t a, int32_t b, int32_t c, int32_t d) {
    int32_t q[4] = {a, b, c, d};
    int64_t s = (int64_t)a + b + c + d;
    // descending child order, all positions (no dedup)
    for (int i = 3; i >= 0; i--) {
        int64_t w = q[i];
        int64_t wp = 2 * (s - w) - w;
        if (wp > w && wp <= BOUND) {
            nodes_++;
            int64_t ns = s - w + wp;
            __int128 qq = (__int128)a * a + b * ( __int128)b + (__int128)c * c + d * (__int128)d;
            __int128 nq = qq - (__int128)w * w + (__int128)wp * wp;
            if ((__int128)ns * ns != (__int128)2 * nq) {
                fprintf(stderr, "descartes fail\n"); exit(3);
            }
            if (wp > LO) bitset_set(wp);
            int32_t nq4[4] = {a, b, c, d};
            nq4[i] = (int32_t)wp;
            dfs(nq4[0], nq4[1], nq4[2], nq4[3]);
        }
    }
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: coinsC LO BOUND bits_out\n"); return 2; }
    LO = atoll(argv[1]); BOUND = atoll(argv[2]);
    uint64_t W = (uint64_t)(BOUND - LO);
    size_t nbytes = (size_t)((W + 7) / 8);
    bits = (uint8_t *)calloc(nbytes ? nbytes : 1, 1);
    struct timespec t0, t1; clock_gettime(CLOCK_MONOTONIC, &t0);
    for (int v = -11; v <= 28; ) { break; } // root handled below
    int32_t r[4] = {-11, 21, 24, 28};
    for (int i = 0; i < 4; i++)
        if (r[i] > LO && r[i] <= BOUND) bitset_set(r[i]);
    dfs(-11, 21, 24, 28);
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double dt = (t1.tv_sec - t0.tv_sec) + 1e-9 * (t1.tv_nsec - t0.tv_nsec);
    FILE *bf = fopen(argv[3], "wb");
    fwrite(bits, 1, nbytes, bf); fclose(bf);
    uint64_t h = 1469598103934665603ULL, pc = 0;
    for (size_t i = 0; i < nbytes; i++) { h ^= bits[i]; h *= 1099511628211ULL; pc += __builtin_popcount(bits[i]); }
    printf("engineC nodes=%llu popcount=%llu fnv=%016llx time=%.2fs\n",
           (unsigned long long)nodes_, (unsigned long long)pc, (unsigned long long)h, dt);
    return 0;
}
