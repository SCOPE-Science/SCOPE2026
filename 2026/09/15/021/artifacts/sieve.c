// Sieve class numbers of imaginary quadratic fundamental discriminants |D|<=B.
// Counts reduced forms (a,b,c): |b|<=a<=c, b^2-4ac=-D, with normalization
// (if |b|==a or a==c then b>=0). Weight per (a,|b|,c): 1 if |b| in {0,a} or
// c==a, else 2. Only fundamental D counted.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char *argv[]) {
    long B = atol(argv[1]);
    char *sqf = malloc(B + 1);
    memset(sqf, 1, B + 1);
    sqf[0] = 0;
    long sq = (long)sqrt((double)B) + 1;
    char *isp = malloc(sq + 1);
    memset(isp, 1, sq + 1);
    for (long p = 2; p * p <= sq; p++) if (isp[p])
        for (long q = p * p; q <= sq; q += p) isp[q] = 0;
    for (long p = 2; p <= sq; p++) if (isp[p]) {
        long p2 = p * p;
        for (long m = p2; m <= B; m += p2) sqf[m] = 0;
    }
    int *cnt = calloc(B + 1, sizeof(int));
    long Amax = (long)sqrt(B / 3.0) + 1;
#pragma omp parallel for schedule(dynamic, 8)
    for (long a = 1; a <= Amax; a++) {
        for (long bb = 0; bb <= a; bb++) {
            long cmax = (bb * bb + B) / (4 * a);
            for (long c = a; c <= cmax; c++) {
                long D = 4 * a * c - bb * bb;
                if (D < 1 || D > B) continue;
                int r = D & 3;
                int fund = 0;
                if (r == 3) fund = sqf[D];
                else if (r == 0) { long q = D / 4; fund = sqf[q] && ((q & 3) != 3); }
                if (!fund) continue;
                int w = (bb == 0 || bb == a || c == a) ? 1 : 2;
#pragma omp atomic
                cnt[D] += w;
            }
        }
    }
    long nfund = 0, nhit = 0;
    for (long D = 1; D <= B; D++) {
        int r = D & 3, fund = 0;
        if (r == 3) fund = sqf[D];
        else if (r == 0) { long q = D / 4; fund = sqf[q] && ((q & 3) != 3); }
        if (!fund) continue;
        nfund++;
        if (cnt[D] == 125) { printf("HIT %ld\n", D); nhit++; }
    }
    fprintf(stderr, "B=%ld fundamentals=%ld hits(h=125)=%ld\n", B, nfund, nhit);
    // calibration spot checks
    long cal[] = {3, 4, 7, 8, 11, 15, 19, 20, 23, 24, 31, 39, 47, 163};
    for (int i = 0; i < 14; i++) fprintf(stderr, "h(-%ld)=%d\n", cal[i], cnt[cal[i]]);
    return 0;
}
