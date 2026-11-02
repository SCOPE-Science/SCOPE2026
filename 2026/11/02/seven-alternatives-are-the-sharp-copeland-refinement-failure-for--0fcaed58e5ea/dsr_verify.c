/* Exact finite census for Hou's 2024 DSR score on tournaments.
   C99 standard library only.  Compile: cc -O2 -std=c99 dsr_verify.c -o dsr_verify
   Run: ./dsr_verify  (enumerates all labeled tournaments up to seven vertices).
   For i<j, a set bit at index (i,j) signifies i beats j; an unset bit
   signifies j beats i.  Vertex identifiers are 0,...,n-1. */
#include <stdio.h>
#include <stdint.h>
#include <string.h>

static int idx[7][7];
static unsigned char orbit[1u << 21];
static int perm[7], used[7];
static uint32_t witness_mask = 1324u;
static unsigned int orbit_size = 0;

static int beat(uint32_t code, int a, int b) {
    if (a == b) return 0;
    unsigned k = (unsigned)idx[a][b];
    return (a < b) ? (int)((code >> k) & 1u)
                   : (int)(1u ^ ((code >> k) & 1u));
}

/* Implements equations (6)-(9) for strict tournaments: beta/gamma
   conditions reduce to a single predecessor beating all successors,
   or every predecessor beating at least one successor. */
static void score(int n, uint32_t code, int dsr[7], int cop[7]) {
    memset(dsr, 0, 7 * sizeof(int));
    memset(cop, 0, 7 * sizeof(int));
    for (int a = 0; a < n; a++)
        for (int b = 0; b < n; b++) cop[a] += beat(code, a, b);

    for (int z = 0; z < n; z++) {
        int U[7], B[7], nu=0, nb=0;
        for (int x = 0; x < n; x++) {
            if (beat(code, x, z)) U[nu++] = x;
            if (beat(code, z, x)) B[nb++] = x;
        }
        if (nb == 0) {
            for (int j = 0; j < nu; j++) dsr[U[j]]++;
            continue;
        }
        int all_pred_some = 1, some_pred_all = 0;
        for (int j = 0; j < nu; j++) {
            int x = U[j], some = 0, all = 1;
            for (int k = 0; k < nb; k++) {
                if (beat(code, x, B[k])) some = 1;
                else all = 0;
            }
            if (!some) all_pred_some = 0;
            if (all) some_pred_all = 1;
        }
        /* z beats every vertex in B, so beta(U U {z},B)>0 automatically.
           When U is empty, gamma is positive, as required for a CW. */
        if (all_pred_some || some_pred_all) {
            dsr[z] += nb;
            for (int j = 0; j < nu; j++) {
                int x = U[j];
                dsr[x] += 1;
                for (int k = 0; k < nb; k++)
                    dsr[x] += beat(code, x, B[k]);
            }
        }
    }
}

static int bad(int n, uint32_t code) {
    int dsr[7], cop[7], max_dsr=-1, max_cop=-1;
    score(n, code, dsr, cop);
    for (int i=0; i<n; i++) {
        if (dsr[i] > max_dsr) max_dsr=dsr[i];
        if (cop[i] > max_cop) max_cop=cop[i];
    }
    for (int i=0; i<n; i++)
        if (dsr[i]==max_dsr && cop[i]<max_cop) return 1;
    return 0;
}

static void permutations(int k) {
    if (k==7) {
        uint32_t code=0;
        for(int i=0;i<7;i++) for(int j=i+1;j<7;j++) {
            int win=beat(witness_mask,i,j)?perm[i]:perm[j];
            int lose=beat(witness_mask,i,j)?perm[j]:perm[i];
            if(win<lose) code |= 1u << idx[win][lose];
        }
        if(!orbit[code]) {orbit[code]=1;orbit_size++;}
        return;
    }
    for(int i=0;i<7;i++) if(!used[i]) {
        used[i]=1;perm[k]=i;permutations(k+1);used[i]=0;
    }
}
static void init_idx(int n) {
    int k=0;
    for (int i=0;i<n;i++) for(int j=i+1;j<n;j++) {
        idx[i][j]=idx[j][i]=k++;
    }
}
int main(void) {
    init_idx(4);
    /* Reference example: four-vertex tournament in Hou's Table 7. */
    { int d[7],c[7];score(4,59u,d,c);
      const int ref[4]={3,4,1,0};
      for(int i=0;i<4;i++) if(d[i]!=ref[i]) return 4;
    }
    init_idx(7);
    permutations(0);
    printf("orbit_size=%u\n",orbit_size);
    if(orbit_size!=5040u) return 5;
    for (int n=2; n<=7; n++) {
        init_idx(n);
        const uint32_t total=1u << (n*(n-1)/2);
        uint32_t bad_count=0, in_orbit=0;
        for(uint32_t m=0; m<total; m++) if(bad(n,m)) {
            bad_count++;
            if(n==7) {
                if(!orbit[m]) {
                    fprintf(stderr,"extra exception: %u\n",m);
                    return 6;
                }
                in_orbit++;
            }
        }
        printf("n=%d total=%u exceptions=%u\n",n,total,bad_count);
        if(n<7 && bad_count!=0) return 7;
        if(n==7 && (bad_count!=5040u || in_orbit!=orbit_size))return 8;
    }
    init_idx(7);
    {int d[7],c[7];score(7,witness_mask,d,c);
     printf("witness=%u\nDSR:",witness_mask);
     for(int i=0;i<7;i++)printf(" %d",d[i]);
     printf("\nCopeland:");
     for(int i=0;i<7;i++)printf(" %d",c[i]);
     printf("\n");
    }
    return 0;
}
