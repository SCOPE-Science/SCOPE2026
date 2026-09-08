/* From-scratch Sprague-Grundy DP for 5-digit octal games.
 * Usage: ./octal_dp DIGITS N OUTFILE [BFILE]
 *   DIGITS: e.g. 13337 ; N: max heap ; OUTFILE: "n G(n)" lines for n=0..N
 *   BFILE (optional): OEIS b-file "n value" lines for n>=1, used ONLY as
 *     consistency gate over n<=min(N, b-file range); mismatches -> FAIL exit.
 * Rules: digit dk (k=1..5): bit0(1): n==k -> reachable 0; bit1(2): n>k ->
 *   reachable G(n-k); bit2(4): n>k -> reachable G(a)^G(b) for a+b=n-k,a,b>=1.
 * G(0)=0.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SEEN_SIZE 65536

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s DIGITS N OUTFILE [BFILE]\n", argv[0]); return 2; }
    const char *digits = argv[1];
    if (strlen(digits) != 5) { fprintf(stderr, "DIGITS must have length 5\n"); return 2; }
    int d[6];
    for (int k = 1; k <= 5; k++) {
        if (digits[k-1] < '0' || digits[k-1] > '7') { fprintf(stderr, "bad digit\n"); return 2; }
        d[k] = digits[k-1] - '0';
    }
    long N = atol(argv[2]);
    if (N < 1 || N > 1000000) { fprintf(stderr, "bad N\n"); return 2; }

    int *G = (int*)malloc((N+1) * sizeof(int));
    int *seen = (int*)calloc(SEEN_SIZE, sizeof(int));
    if (!G || !seen) { fprintf(stderr, "oom\n"); return 2; }
    G[0] = 0;
    int cur = 0;
    int maxv = 0;
    for (long n = 1; n <= N; n++) {
        cur++;
        if (cur == 2000000000) { memset(seen, 0, SEEN_SIZE*sizeof(int)); cur = 1; }
        for (int k = 1; k <= 5; k++) {
            if (n < k) continue;
            if (n == k) {
                if (d[k] & 1) seen[0] = cur;
                continue;
            }
            if (d[k] & 2) {
                int v = G[n-k];
                if (v < SEEN_SIZE) seen[v] = cur;
                else { fprintf(stderr, "single value overflow at n=%ld\n", n); return 3; }
            }
            if (d[k] & 4) {
                long m = n - k;
                for (long a = 1; a <= m - 1; a++) {
                    long b = m - a;
                    if (a > b) break;
                    int v = G[a] ^ G[(size_t)b];
                    if (v < SEEN_SIZE) seen[v] = cur;
                    else { fprintf(stderr, "xor value overflow at n=%ld\n", n); return 3; }
                }
            }
        }
        int mex = 0;
        while (mex < SEEN_SIZE && seen[mex] == cur) mex++;
        if (mex >= SEEN_SIZE) { fprintf(stderr, "mex overflow at n=%ld\n", n); return 3; }
        G[n] = mex;
        if (mex > maxv) maxv = mex;
    }

    if (argc >= 5) {
        FILE *bf = fopen(argv[4], "r");
        if (!bf) { fprintf(stderr, "cannot open BFILE\n"); return 2; }
        long n; int v; long checked = 0, lastn = 0;
        while (fscanf(bf, "%ld %d", &n, &v) == 2) {
            if (n >= 1 && n <= N) {
                if (G[n] != v) {
                    fprintf(stderr, "GATE FAIL at n=%ld: dp=%d bfile=%d\n", n, G[n], v);
                    fclose(bf); return 1;
                }
                checked++; lastn = n;
            }
        }
        fclose(bf);
        printf("gate: PASS (%ld values checked through n=%ld)\n", checked, lastn);
    }

    FILE *f = fopen(argv[3], "w");
    if (!f) { fprintf(stderr, "cannot open OUTFILE\n"); return 2; }
    for (long n = 0; n <= N; n++) fprintf(f, "%ld %d\n", n, G[n]);
    fclose(f);
    printf("game .%s N=%ld done, max nimber=%d\n", digits, N, maxv);
    free(G); free(seen);
    return 0;
}
