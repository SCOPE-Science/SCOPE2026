/* Exhaustive finite algebra certificate for three order-16 groups over F_2.
   Compile: cc -std=c99 -O2 -Wall -Wextra verify_binary.c -o verify_binary
   Run: ./verify_binary. No libraries are required. */
#include <stdint.h>
#include <stdio.h>
#include <string.h>

static int check(int action, int central_square, const int want[9]) {
    unsigned char product[16][16];
    int got[9] = {0};
    for (int i = 0; i < 16; ++i) {
        int a = i & 7, b = i >> 3;
        for (int j = 0; j < 16; ++j) {
            int d = j & 7, e = j >> 3;
            product[i][j] = (unsigned char)(
                ((a + (b ? action : 1)*d + central_square*b*e) & 7)
                + 8*(b^e));
        }
    }
    for (uint32_t bits = 0; bits < (1u << 16); ++bits) {
        unsigned char squared[16] = {0};
        for (int i = 0; i < 16; ++i) if ((bits >> i)&1u)
            for (int j = 0; j < 16; ++j) if ((bits >> j)&1u)
                squared[product[i][j]] ^= 1u;
        int zero = 1;
        for (int k = 0; k < 16; ++k) if (squared[k]) zero = 0;
        if (!zero) continue;
        uint16_t pivots[16] = {0};
        int rank = 0;
        for (int j = 0; j < 16; ++j) {
            uint16_t column = 0;
            for (int i = 0; i < 16; ++i) if ((bits >> i)&1u)
                column ^= (uint16_t)(1u << product[i][j]);
            for (int k = 15; k >= 0 && column; --k) if ((column >> k)&1u) {
                if (pivots[k]) column ^= pivots[k];
                else { pivots[k] = column; ++rank; break; }
            }
        }
        if (rank > 8) return 1;
        ++got[rank];
    }
    for (int i = 0; i <= 8; ++i) if (got[i] != want[i]) return 2;
    printf("action=%d central_square=%d:",action,central_square);
    for (int i = 0; i <= 8; ++i) if (got[i]) printf(" %d:%d",i,got[i]);
    puts("");
    return 0;
}
int main(void) {
    const int D[9] = {1,1,6,16,72,0,288,0,896};
    const int S[9] = {1,1,6,16,72,0,288,0,640};
    const int Q[9] = {1,1,6,16,72,0,288,0,384};
    int e1=check(7,0,D),e2=check(3,0,S),e3=check(7,4,Q);
    if (e1||e2||e3) {puts("FAIL");return 1;}
    puts("ORDER16_BINARY_RANK_PASS 3 complete 65536-element searches");
    return 0;
}
