// Coins packing Descartes-tree enumerator (engines A/B: opposite child order).
// Root (-11,21,24,28). Child rule: w' = 2*(sum-w)-w; child iff w'>w, w'<=BOUND.
// Marks birth curvatures in (LO,BOUND] into a bitset. Per-node Descartes check.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef struct { int32_t q[4]; int64_t sum, sq; int next; } Frame;

static int64_t LO, BOUND;
static uint8_t *bits;
static uint64_t nodes_, marks_;
static int64_t minmark_;

static inline void bitset_set(int64_t v) {
    uint64_t i = (uint64_t)(v - LO - 1);
    bits[i >> 3] |= (uint8_t)(1u << (i & 7));
}

int main(int argc, char **argv) {
    // usage: coins LO BOUND order bits_out [find_target]
    if (argc < 5) { fprintf(stderr, "usage: coins LO BOUND order bits_out [find]\n"); return 2; }
    LO = atoll(argv[1]); BOUND = atoll(argv[2]);
    int order = atoi(argv[3]); // 0: child index asc, 1: desc
    const char *out = argv[4];
    int64_t find = (argc > 5) ? atoll(argv[5]) : -1;
    uint64_t W = (uint64_t)(BOUND - LO);
    size_t nbytes = (size_t)((W + 7) / 8);
    bits = (uint8_t *)calloc(nbytes ? nbytes : 1, 1);
    if (!bits) { fprintf(stderr, "oom bits\n"); return 1; }

    size_t cap = 1 << 20;
    Frame *st = (Frame *)malloc(cap * sizeof(Frame));
    if (!st) { fprintf(stderr, "oom stack\n"); return 1; }
    size_t top = 0;
    // root
    st[0].q[0] = -11; st[0].q[1] = 21; st[0].q[2] = 24; st[0].q[3] = 28;
    st[0].sum = 62; st[0].sq = 121 + 441 + 576 + 784; st[0].next = 0;
    if (st[0].sum * st[0].sum != 2 * st[0].sq) { fprintf(stderr, "root descartes fail\n"); return 1; }
    for (int i = 0; i < 4; i++) {
        int64_t v = st[0].q[i];
        if (v > LO && v <= BOUND) { bitset_set(v); marks_++; if (v < minmark_ || marks_ == 1) minmark_ = v; }
    }
    if (find > 0) minmark_ = INT64_MAX;
    struct timespec t0, t1; clock_gettime(CLOCK_MONOTONIC, &t0);
    long found_depth = -1;
    while (top < (size_t)-1) {
        Frame *f = &st[top];
        if (f->next < 4) {
            int k = f->next++;
            int i = order ? (3 - k) : k;
            int32_t w = f->q[i];
            int dup = 0;
            for (int j = 0; j < i; j++) if (f->q[j] == w) { dup = 1; break; }
            if (dup) continue;
            int64_t rest = f->sum - w;
            int64_t wp = 2 * rest - w;
            if (wp > w && wp <= BOUND) {
                nodes_++;
                if (find > 0 && wp == find) { found_depth = (long)top + 1; break; }
                if (wp > LO) { bitset_set(wp); marks_++; if (wp < minmark_) minmark_ = wp; }
                if (top + 1 >= cap) {
                    cap *= 2;
                    Frame *ns = (Frame *)realloc(st, cap * sizeof(Frame));
                    if (!ns) { fprintf(stderr, "oom grow\n"); return 1; }
                    st = ns; f = &st[top];
                }
                Frame *c = &st[top + 1];
                c->q[0] = f->q[0]; c->q[1] = f->q[1]; c->q[2] = f->q[2]; c->q[3] = f->q[3];
                c->q[i] = (int32_t)wp;
                c->sum = rest + wp;
                c->sq = f->sq - (int64_t)w * w + wp * wp;
                __int128 lhs = (__int128)c->sum * c->sum;
                __int128 rhs = (__int128)2 * c->sq;
                if (lhs != rhs) { fprintf(stderr, "descartes fail at node %llu\n", (unsigned long long)nodes_); return 3; }
                c->next = 0;
                top++;
            }
        } else {
            if (top == 0) break;
            top--;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &t1);
    double dt = (t1.tv_sec - t0.tv_sec) + 1e-9 * (t1.tv_nsec - t0.tv_nsec);
    if (find > 0) {
        printf("FIND %lld depth=%ld nodes=%llu time=%.2fs\n", (long long)find, found_depth,
               (unsigned long long)nodes_, dt);
        if (found_depth >= 0) {
            // reconstruct chain: replay stack contents (frames 0..top) + target birth
            FILE *cf = fopen(out, "w");
            if (cf) {
                for (size_t d = 0; d <= top; d++)
                    fprintf(cf, "%zu: (%d,%d,%d,%d) sum=%lld\n", d, st[d].q[0], st[d].q[1],
                            st[d].q[2], st[d].q[3], (long long)st[d].sum);
                // birth quad = parent with target filled at the found slot; recompute slot
                Frame *f = &st[top];
                for (int k = 0; k < 4; k++) {
                    int i = order ? (3 - k) : k;
                    int32_t w = f->q[i];
                    int dup = 0;
                    for (int j = 0; j < i; j++) if (f->q[j] == w) { dup = 1; break; }
                    if (dup) continue;
                    int64_t wp = 2 * (f->sum - w) - w;
                    if (wp > w && wp <= BOUND && wp == find) {
                        fprintf(cf, "birth: replace pos %d (%d -> %lld)\n", i, w, (long long)wp);
                        fprintf(cf, "birth_quad: (%d,%d,%d,%d)\n",
                                i == 0 ? (int)find : f->q[0], i == 1 ? (int)find : f->q[1],
                                i == 2 ? (int)find : f->q[2], i == 3 ? (int)find : f->q[3]);
                        break;
                    }
                }
                fclose(cf);
            }
        }
        return 0;
    }
    FILE *bf = fopen(out, "wb");
    if (!bf) { fprintf(stderr, "cannot open out\n"); return 1; }
    if (nbytes) fwrite(bits, 1, nbytes, bf);
    fclose(bf);
    // fnv hash + popcount
    uint64_t h = 1469598103934665603ULL, pc = 0;
    for (size_t i = 0; i < nbytes; i++) { h ^= bits[i]; h *= 1099511628211ULL; pc += __builtin_popcount(bits[i]); }
    printf("LO=%lld BOUND=%lld order=%d nodes=%llu marks=%llu minmark=%lld popcount=%llu fnv=%016llx time=%.2fs\n",
           (long long)LO, (long long)BOUND, order, (unsigned long long)nodes_,
           (unsigned long long)marks_, (long long)minmark_, (unsigned long long)pc,
           (unsigned long long)h, dt);
    return 0;
}
