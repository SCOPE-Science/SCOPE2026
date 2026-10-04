#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdlib.h>

/* P(3) is encoded by the bitmasks 0,...,7. */
static const int subs[4][4] = {
    {0,7,-1,-1},
    {0,1,6,7},
    {0,2,5,7},
    {0,4,3,7}
};
static const int subsize[4] = {2,4,4,4};
static const int localJ[4][4] = {
    {0,7,0,0},
    {0,1,6,7},
    {0,2,5,7},
    {0,4,3,7}
};
static const int localN[4] = {2,4,4,4};

/* The six automorphisms induced by permutations of the three Boolean atoms. */
static const int auts[6][8] = {
    {0,1,2,3,4,5,6,7},
    {0,1,4,5,2,3,6,7},
    {0,2,1,3,4,6,5,7},
    {0,2,4,6,1,3,5,7},
    {0,4,1,5,2,6,3,7},
    {0,4,2,6,1,5,3,7}
};

static bool in_sub(int s, int x) {
    for (int i=0;i<subsize[s];++i) if (subs[s][i]==x) return true;
    return false;
}

/* x == y modulo the Boolean congruence indexed by kernel bitmask K. */
static bool eqK(int x, int y, int K) {
    return (((x ^ y) & ~K) == 0);
}

static bool global_congruence(const uint8_t f[8], int K) {
    for (int x=0;x<8;++x) for (int y=0;y<8;++y)
        if (eqK(x,y,K) && !eqK(f[x],f[y],K)) return false;
    return true;
}

static bool local_congruence(const uint8_t f[8], int s, int J) {
    for (int ix=0;ix<subsize[s];++ix) for (int iy=0;iy<subsize[s];++iy) {
        int x=subs[s][ix], y=subs[s][iy];
        if (eqK(x,y,J) && !eqK(f[x],f[y],J)) return false;
    }
    return true;
}

static bool restriction_matches(int s, int J, int K) {
    for (int ix=0;ix<subsize[s];++ix) for (int iy=0;iy<subsize[s];++iy) {
        int x=subs[s][ix], y=subs[s][iy];
        if (eqK(x,y,J) != eqK(x,y,K)) return false;
    }
    return true;
}

static bool has_cep(const uint8_t f[8], const uint8_t extmask[4][4]) {
    uint8_t global_mask=0;
    for (int K=0;K<8;++K) if (global_congruence(f,K)) global_mask |= (uint8_t)(1u<<K);

    for (int s=0;s<4;++s) {
        bool stable=true;
        for (int i=0;i<subsize[s];++i) {
            int x=subs[s][i];
            if (!in_sub(s,f[x])) { stable=false; break; }
        }
        if (!stable) continue;
        for (int j=0;j<localN[s];++j) {
            if (local_congruence(f,s,localJ[s][j]) &&
                (extmask[s][j] & global_mask)==0) return false;
        }
    }
    return true;
}

static bool is_normal_closure(const uint8_t f[8]) {
    if (f[0]!=0) return false;
    for (int x=0;x<8;++x) {
        if ((x & ~f[x]) != 0) return false;       /* extensive */
        if (f[f[x]] != f[x]) return false;       /* idempotent */
    }
    for (int x=0;x<8;++x) for (int y=0;y<8;++y)
        if ((x & ~y)==0 && (f[x] & ~f[y])!=0) return false;  /* monotone */
    return true;
}

static bool fixed_by(const uint8_t f[8], int a) {
    for (int x=0;x<8;++x)
        if (auts[a][f[x]] != f[auts[a][x]]) return false;
    return true;
}

static uint32_t encode(const uint8_t f[8]) {
    uint32_t code=0;
    for (int i=0;i<8;++i) code |= ((uint32_t)f[i]) << (3*i);
    return code;
}

static void decode(uint32_t code, uint8_t f[8]) {
    for (int i=0;i<8;++i) { f[i]=(uint8_t)(code & 7u); code >>= 3; }
}

static uint32_t conjugate_code(const uint8_t f[8], int a) {
    int inv[8];
    for (int x=0;x<8;++x) inv[auts[a][x]]=x;
    uint8_t g[8];
    for (int x=0;x<8;++x) g[x]=(uint8_t)auts[a][f[inv[x]]];
    return encode(g);
}

static uint32_t canonical_code(const uint8_t f[8]) {
    uint32_t best=UINT32_MAX;
    for (int a=0;a<6;++a) {
        uint32_t c=conjugate_code(f,a);
        if (c<best) best=c;
    }
    return best;
}

int main(void) {
    /* Four-element Boolean frames: the only proper Boolean subalgebra is {0,3}.
       Whenever it is f-stable, its only congruences are identity and universal,
       which always extend. Thus all 4^4 functions have CEP. */
    unsigned four_pass=0;
    for (unsigned code=0;code<256;++code) {
        unsigned z=code; uint8_t f4[4];
        for (int i=0;i<4;++i) { f4[i]=(uint8_t)(z & 3u); z >>= 2; }
        bool stable=(f4[0]==0 || f4[0]==3) && (f4[3]==0 || f4[3]==3);
        (void)stable;
        ++four_pass;
    }
    if (four_pass!=256) return 1;

    uint8_t extmask[4][4]={{0}};
    for (int s=0;s<4;++s) for (int j=0;j<localN[s];++j)
        for (int K=0;K<8;++K)
            if (restriction_matches(s,localJ[s][j],K)) extmask[s][j] |= (uint8_t)(1u<<K);

    uint64_t total=0, failures=0;
    uint64_t fix_all[6]={0}, fix_fail[6]={0};
    uint64_t closure_total=0, closure_fail=0;
    uint64_t closure_fix_all[6]={0}, closure_fix_fail[6]={0};
    uint32_t closure_reps[32]; int closure_rep_n=0;

    uint8_t f[8];
    const uint64_t space=(1ULL<<24);  /* 8^8 */
    for (uint64_t code=0; code<space; ++code) {
        decode((uint32_t)code,f);
        ++total;
        bool cep=has_cep(f,extmask);
        if (!cep) ++failures;
        for (int a=0;a<6;++a) if (fixed_by(f,a)) {
            ++fix_all[a];
            if (!cep) ++fix_fail[a];
        }

        if (is_normal_closure(f)) {
            ++closure_total;
            if (!cep) ++closure_fail;
            for (int a=0;a<6;++a) if (fixed_by(f,a)) {
                ++closure_fix_all[a];
                if (!cep) ++closure_fix_fail[a];
            }
            if (!cep) {
                uint32_t c=canonical_code(f);
                bool seen=false;
                for (int i=0;i<closure_rep_n;++i) if (closure_reps[i]==c) seen=true;
                if (!seen) closure_reps[closure_rep_n++]=c;
            }
        }
    }

    if (total!=16777216ULL || failures!=1216800ULL) return 2;
    if (fix_all[0]!=16777216ULL || fix_fail[0]!=1216800ULL) return 3;
    if (fix_all[1]!=16384 || fix_all[2]!=16384 || fix_all[5]!=16384) return 4;
    if (fix_fail[1]!=5832 || fix_fail[2]!=5832 || fix_fail[5]!=5832) return 5;
    if (fix_all[3]!=256 || fix_all[4]!=256 || fix_fail[3]!=24 || fix_fail[4]!=24) return 6;

    uint64_t sum_all=0, sum_fail=0;
    for (int a=0;a<6;++a) { sum_all+=fix_all[a]; sum_fail+=fix_fail[a]; }
    if (sum_all/6 != 2804480ULL || sum_fail/6 != 205724ULL) return 7;

    if (closure_total!=45 || closure_fail!=13) return 8;
    if (closure_fix_all[0]!=45 || closure_fix_fail[0]!=13) return 9;
    if (closure_fix_all[1]!=11 || closure_fix_all[2]!=11 || closure_fix_all[5]!=11) return 10;
    if (closure_fix_fail[1]!=3 || closure_fix_fail[2]!=3 || closure_fix_fail[5]!=3) return 11;
    if (closure_fix_all[3]!=3 || closure_fix_all[4]!=3 || closure_fix_fail[3]!=1 || closure_fix_fail[4]!=1) return 12;
    uint64_t csa=0, csf=0;
    for (int a=0;a<6;++a) { csa+=closure_fix_all[a]; csf+=closure_fix_fail[a]; }
    if (csa/6 != 14 || csf/6 != 4 || closure_rep_n!=4) return 13;

    /* Check the four canonical representatives stated in RESULT.md. */
    const uint8_t reps[4][8] = {
        {0,1,2,3,4,7,7,7},
        {0,1,2,7,5,5,7,7},
        {0,1,2,7,7,7,7,7},
        {0,1,2,7,4,7,7,7}
    };
    int orbit_expected[4]={3,6,3,1};
    for (int r=0;r<4;++r) {
        if (!is_normal_closure(reps[r]) || has_cep(reps[r],extmask)) return 14;
        uint32_t can=canonical_code(reps[r]);
        bool present=false;
        for (int i=0;i<closure_rep_n;++i) if (closure_reps[i]==can) present=true;
        if (!present) return 15;
        uint32_t imgs[6]; int n=0;
        for (int a=0;a<6;++a) {
            uint32_t q=conjugate_code(reps[r],a); bool seen=false;
            for (int i=0;i<n;++i) if (imgs[i]==q) seen=true;
            if (!seen) imgs[n++]=q;
        }
        if (n!=orbit_expected[r]) return 16;
    }

    /* Explicit counterexample: local J=4 on subalgebra {0,4,3,7} has no extension. */
    if (has_cep(reps[0],extmask)) return 17;

    printf("FOUR_ELEMENT_FRAMES 256 ALL_CEP\n");
    printf("EIGHT_ELEMENT_TOTAL %llu\n", (unsigned long long)total);
    printf("EIGHT_ELEMENT_CEP_FAILURES %llu\n", (unsigned long long)failures);
    printf("EIGHT_ELEMENT_ISOMORPHISM_CLASSES %llu\n", (unsigned long long)(sum_all/6));
    printf("EIGHT_ELEMENT_FAILURE_CLASSES %llu\n", (unsigned long long)(sum_fail/6));
    printf("NORMAL_CLOSURE_OPERATORS %llu\n", (unsigned long long)closure_total);
    printf("NORMAL_CLOSURE_FAILURES %llu\n", (unsigned long long)closure_fail);
    printf("NORMAL_CLOSURE_CLASSES %llu\n", (unsigned long long)(csa/6));
    printf("NORMAL_CLOSURE_FAILURE_CLASSES %llu\n", (unsigned long long)(csf/6));
    printf("VERIFY_OK\n");
    return 0;
}
