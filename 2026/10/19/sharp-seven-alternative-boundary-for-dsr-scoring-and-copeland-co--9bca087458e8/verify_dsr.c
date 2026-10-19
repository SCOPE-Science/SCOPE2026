/* Exhaustive integer verification of the tournament DSR/Copeland boundary.
   Build: cc -std=c99 -O3 -Wall -Wextra verify_dsr.c -o verify_dsr
   Run: ./verify_dsr
   All 2^(n(n-1)/2) labeled tournaments are visited at each order 2..7.
*/
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

static int evaluate(int n, uint64_t mask, int dsr[7], int cop[7]) {
    int win[7][7] = {{0}};
    int bit = 0;
    for (int i = 0; i < n; i++)
        for (int j = i+1; j < n; j++, bit++) {
            if ((mask >> bit) & 1) win[i][j] = 1;
            else win[j][i] = 1;
        }
    for (int i = 0; i < n; i++) {
        cop[i] = dsr[i] = 0;
        for (int j = 0; j < n; j++) cop[i] += win[i][j];
    }
    for (int z = 0; z < n; z++) {
        int u[7], d[7], nu = 0, nd = 0;
        for (int i = 0; i < n; i++) {
            if (win[i][z]) u[nu++] = i;
            if (win[z][i]) d[nd++] = i;
        }
        /* The no-outneighbor clause is line 5 of Algorithm 2. */
        if (nd == 0) {
            for (int k = 0; k < nu; k++) dsr[u[k]]++;
            continue;
        }
        /* For tournaments, relation >= is just > for distinct vertices.
           C2 tests every member of U union {z} beats some element of D;
           C3 tests at least one U member beats every member of D. */
        int c2 = 1, c3 = 0;
        for (int k = 0; k < nu; k++) {
            int some = 0, all = 1, x = u[k];
            for (int h = 0; h < nd; h++) {
                some |= win[x][d[h]];
                all &= win[x][d[h]];
            }
            c2 &= some;
            c3 |= all;
        }
        /* The additional z member always beats every member of D. */
        if (!c2 && !c3) continue;
        for (int k = 0; k <= nu; k++) {
            int x = (k == nu ? z : u[k]);
            dsr[x] += (x != z);
            for (int h = 0; h < nd; h++) dsr[x] += win[x][d[h]];
        }
    }
    int maxs = -1, maxc = -1, bad = 0, common = 0;
    for (int x = 0; x < n; x++) {
        if (dsr[x] > maxs) maxs = dsr[x];
        if (cop[x] > maxc) maxc = cop[x];
    }
    for (int x = 0; x < n; x++) {
        if (dsr[x] == maxs && cop[x] < maxc) bad = 1;
        if (dsr[x] == maxs && cop[x] == maxc) common = 1;
    }
    return bad ? (common ? 1 : 2) : 0;
}

int main(void) {
    int dsr[7], cop[7];
    for (int n = 2; n <= 7; n++) {
        uint64_t limit = UINT64_C(1) << (n*(n-1)/2);
        uint64_t failures = 0, disjoint = 0, first = UINT64_MAX;
        for (uint64_t mask = 0; mask < limit; mask++) {
            int status = evaluate(n,mask,dsr,cop);
            if (status) {
                failures++;
                if (status == 2) disjoint++;
                if (first == UINT64_MAX) first = mask;
            }
        }
        printf("n=%d total=%llu noncontainment=%llu disjoint=%llu\n",
            n, (unsigned long long)limit, (unsigned long long)failures,
            (unsigned long long)disjoint);
        if ((n < 7 && failures != 0) ||
            (n == 7 && (failures != 5040 || disjoint != 0))) return 2;
        if (n == 7) {
            evaluate(n, UINT64_C(1324), dsr, cop);
            printf("witness_mask=1324 copeland:");
            for (int i = 0; i < n; i++) printf(" %d",cop[i]);
            printf(" dsr:");
            for (int i = 0; i < n; i++) printf(" %d",dsr[i]);
            printf(" first_noncontainment_mask=%llu\n", (unsigned long long)first);
            const int expected_c[] = {3,3,2,2,2,5,4};
            const int expected_s[] = {6,3,2,4,5,14,14};
            for (int i=0;i<n;i++) if (cop[i]!=expected_c[i] || dsr[i]!=expected_s[i]) return 3;
        }
    }
    puts("VERIFY_OK");
    return 0;
}
