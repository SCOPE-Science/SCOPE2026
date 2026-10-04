#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

static uint32_t masks[28];
static uint8_t *closed_bits[28];

static inline int get_closed(int len, uint32_t x) {
    return (closed_bits[len][x >> 3] >> (x & 7u)) & 1u;
}

static inline void set_closed(int len, uint32_t x) {
    closed_bits[len][x >> 3] |= (uint8_t)(1u << (x & 7u));
}

static int closed_word(uint32_t x, int len) {
    if (len <= 1) return 1;
    for (int b = len - 1; b >= 1; --b) {
        uint32_t mask = masks[b];
        uint32_t prefix = x >> (len - b);
        uint32_t suffix = x & mask;
        if (prefix != suffix) continue;
        int occurrences = 0;
        for (int start = 0; start <= len - b; ++start) {
            uint32_t sub = (x >> (len - b - start)) & mask;
            if (sub == prefix) {
                ++occurrences;
                if (occurrences > 2) break;
            }
        }
        return occurrences == 2;
    }
    return 0;
}

static inline int bit_at(uint32_t x, int n, int i) {
    return (int)((x >> (n - 1 - i)) & 1u);
}

static int shortest_period(uint32_t x, int n) {
    for (int p = 1; p <= n; ++p) {
        int ok = 1;
        for (int i = p; i < n; ++i) {
            if (bit_at(x,n,i) != bit_at(x,n,i-p)) { ok = 0; break; }
        }
        if (ok) return p;
    }
    return n;
}

int main(void) {
    static const int expected_max[28] = {
        0,2,3,4,6,8,10,12,15,18,21,25,29,33,37,42,48,54,60,66,72,79,86,93,101,109,117,126
    };
    static const uint64_t expected_count[28] = {
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,128,72
    };

    masks[0] = 0;
    for (int i = 1; i <= 27; ++i) masks[i] = (1u << i) - 1u;

    for (int len = 1; len <= 27; ++len) {
        uint32_t lim = 1u << len;
        size_t bytes = ((size_t)lim + 7u) / 8u;
        closed_bits[len] = (uint8_t*)calloc(bytes, 1u);
        if (!closed_bits[len]) return 10;
        for (uint32_t x = 0; x < lim; ++x) {
            if (closed_word(x, len)) set_closed(len, x);
        }
    }

    uint8_t *prev = (uint8_t*)malloc(1u);
    if (!prev) return 11;
    prev[0] = 1; /* the empty factor */

    uint64_t period_hist[28][28];
    memset(period_hist, 0, sizeof(period_hist));

    for (int n = 1; n <= 27; ++n) {
        uint32_t lim = 1u << n;
        uint8_t *curr = (uint8_t*)malloc((size_t)lim);
        if (!curr) return 12;
        int maxv = -1;
        uint64_t maxcount = 0;

        for (uint32_t x = 0; x < lim; ++x) {
            int c = prev[x >> 1];
            for (int len = 1; len <= n; ++len) {
                uint32_t mask = masks[len];
                uint32_t suffix = x & mask;
                if (!get_closed(len, suffix)) continue;
                int seen_earlier = 0;
                for (int d = 1; d <= n - len; ++d) {
                    if (((x >> d) & mask) == suffix) { seen_earlier = 1; break; }
                }
                if (!seen_earlier) ++c;
            }
            if (c > 255) return 13;
            curr[x] = (uint8_t)c;
            if (c > maxv) { maxv = c; maxcount = 1; }
            else if (c == maxv) { ++maxcount; }
        }

        if (maxv != expected_max[n]) {
            fprintf(stderr, "max mismatch n=%d got=%d expected=%d\n", n, maxv, expected_max[n]);
            return 20;
        }
        if (n >= 25 && maxcount != expected_count[n]) {
            fprintf(stderr, "count mismatch n=%d got=%llu expected=%llu\n", n,
                    (unsigned long long)maxcount, (unsigned long long)expected_count[n]);
            return 21;
        }
        if (n >= 25) {
            for (uint32_t x = 0; x < lim; ++x) if (curr[x] == maxv) {
                int p = shortest_period(x,n);
                ++period_hist[n][p];
            }
        }

        free(prev);
        prev = curr;
    }

    if (period_hist[25][8] != 56) return 30;
    for (int p=1; p<=25; ++p) if (p != 8 && period_hist[25][p] != 0) return 31;
    if (period_hist[26][8] != 56 || period_hist[26][9] != 72) return 32;
    for (int p=1; p<=26; ++p) if (p != 8 && p != 9 && period_hist[26][p] != 0) return 33;
    if (period_hist[27][9] != 72) return 34;
    for (int p=1; p<=27; ++p) if (p != 9 && period_hist[27][p] != 0) return 35;

    free(prev);
    for (int len=1; len<=27; ++len) free(closed_bits[len]);

    puts("VERIFY_OK source_table_1_24=matched n25=109 count25=56 p25=8:56 n26=117 count26=128 p26=8:56,9:72 n27=126 count27=72 p27=9:72");
    return 0;
}
