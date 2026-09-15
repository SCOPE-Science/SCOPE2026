// Exact class-group exponent-5 test via ideal multiplication in an integral basis.
// R = maximal order: D odd: basis {1, w}, w=(1+s)/2; D even: basis {1, w}, w=s/2.
// Form (a,b,c) <-> ideal I = aZ + ((-b+s)/2)Z.
//   D odd: (-b+s)/2 = (-b-1)/2 + w  [since (1+s)/2*1: (-b+s)/2 = m + w with m=(-b-1)/2, integer as b odd]
//          I rows in (u,v): (a,0), (m,1).
//   D even: (-b+s)/2 = (-b/2) + w, b even: rows (a,0), (-b/2,1).
// Product I*J: 3 generators g1h1, g1h2+g2h1, g2h2 (g1g2=g2g1), each a product in R:
//   (u1+v1 w)(u2+v2 w) with w^2 = w + (D-1)/4 (D odd) or w^2 = D/4 (D even).
// HNF of 3x2 lattice -> (X0, 0; PX, G)... rows -> normal form (A,0),(B,1) [G must be 1
// for proper inputs]; ideal = AZ + ((B'+s)/2)Z with B' = -b3... convert back to form:
//   D odd: (B,1) means element B+w = B+(1+s)/2 = ((2B+1)+s)/2 -> b3 = -(2B+1).
//   D even: (B,1) means B + s/2 = (2B+s)/2 -> b3 = -2B.
// Then a3 = A, reduce. All exact (ll arithmetic; |D|<=2e5 fits easily).
// Usage: ./hnf D1 [D2 ...] (Di = |D|)
#include <stdio.h>
#include <stdlib.h>

typedef long long ll;

static ll llabs_(ll x) { return x < 0 ? -x : x; }
static ll gg(ll a, ll b) { a = llabs_(a); b = llabs_(b); while (b) { ll t = a % b; a = b; b = t; } return a; }

typedef struct { ll a, b, c; } Form;

// multiply in R: (u1+v1 w)(u2+v2 w). odd: w^2=w+(D-1)/4. even: w^2=D/4.
static void rmul(ll u1, ll v1, ll u2, ll v2, ll D, int odd, ll *u, ll *v) {
    if (odd) {
        ll t = (D - 1) / 4;
        *u = u1 * u2 + v1 * v2 * t;
        *v = u1 * v2 + v1 * u2 + v1 * v2;
    } else {
        ll t = D / 4;
        *u = u1 * u2 + v1 * v2 * t;
        *v = u1 * v2 + v1 * u2;
    }
}

static Form reducefD(ll a, ll b, ll D) {
    for (;;) {
        ll m = 2 * a;
        ll r = b % m;
        if (r < 0) r += m;
        if (r > a) r -= m;
        b = r;
        ll num = b * b - D;
        if (num % (4 * a) != 0) { fprintf(stderr, "reduce: bad disc a=%lld b=%lld D=%lld\n", a, b, D); exit(1); }
        ll c = num / (4 * a);
        if (a > c) { ll t = a; a = c; c = t; b = -b; continue; }
        if (a == c && b < 0) { b = -b; continue; }
        return (Form){a, b, c};
    }
}

static Form compose(Form f1, Form f2, ll D) {
    int odd = ((D % 2) + 2) % 2;
    ll a1 = f1.a, b1 = f1.b, a2 = f2.a, b2 = f2.b;
    ll g1u, g1v, g2u, g2v, h1u, h1v, h2u, h2v;
    if (odd) {
        g1u = a1; g1v = 0; g2u = (-b1 - 1) / 2; g2v = 1;
        h1u = a2; h1v = 0; h2u = (-b2 - 1) / 2; h2v = 1;
    } else {
        g1u = a1; g1v = 0; g2u = -b1 / 2; g2v = 1;
        h1u = a2; h1v = 0; h2u = -b2 / 2; h2v = 1;
    }
    ll U[4], V[4], u, v;
    rmul(g1u, g1v, h1u, h1v, D, odd, &u, &v); U[0] = u; V[0] = v;
    // four pairwise products as separate rows (g1h2 and g2h1 both needed even when equal)
    ll u1, v1, u2, v2;
    rmul(g1u, g1v, h2u, h2v, D, odd, &u1, &v1);
    rmul(g2u, g2v, h1u, h1v, D, odd, &u2, &v2);
    U[1] = u1; V[1] = v1;
    U[2] = u2; V[2] = v2;
    rmul(g2u, g2v, h2u, h2v, D, odd, &u, &v); U[3] = u; V[3] = v;
    // HNF of rows (U[i],V[i]): eliminate V
    ll x[4] = {U[0], U[1], U[2], U[3]}, y[4] = {V[0], V[1], V[2], V[3]};
    for (;;) {
        int p = -1, q = -1;
        for (int i = 0; i < 4; i++) if (y[i] != 0) { if (p < 0) p = i; else { q = i; break; } }
        if (q < 0) break;
        if (llabs_(y[p]) > llabs_(y[q])) { int t = p; p = q; q = t; }
        ll qq = y[q] / y[p];
        x[q] -= qq * x[p];
        y[q] -= qq * y[p];
    }
    int piv = -1;
    for (int i = 0; i < 4; i++) if (y[i] != 0) piv = i;
    if (piv < 0) { fprintf(stderr, "compose: rank collapse D=%lld\n", D); exit(1); }
    ll G = y[piv], PX = x[piv];
    if (G < 0) { G = -G; PX = -PX; }
    ll X0 = 0;
    for (int i = 0; i < 4; i++) {
        if (i == piv) continue;
        if (x[i] == 0 && y[i] == 0) continue;
        if (y[i] != 0) { fprintf(stderr, "compose: leftover pivot\n"); exit(1); }
        X0 = gg(X0, x[i]);
    }
    if (X0 == 0) {
        ll M = 0;
        for (int i = 0; i < 4; i++)
            for (int j = i + 1; j < 4; j++)
                M = gg(M, U[i] * V[j] - U[j] * V[i]);
        X0 = llabs_(M) / G;
    }
    if (X0 == 0) { fprintf(stderr, "compose: X0=0 D=%lld\n", D); exit(1); }
    X0 = llabs_(X0);
    PX %= X0; if (PX < 0) PX += X0;
    // divide by content (product may be imprimitive, e.g. P^2=(2)); norm = X0*G/c^2
    ll c0 = gg(gg(X0, PX), G);
    X0 /= c0; PX /= c0; G /= c0;
    if (G != 1) { fprintf(stderr, "compose: primitive G=%lld D=%lld\n", G, D); exit(1); }
    ll a3 = X0;
    ll b3 = odd ? -(2 * PX + 1) : -(2 * PX);
    // normalize b3 mod 2a3 (same class): b3 -> b3 mod 2a3 then reduce
    b3 %= (2 * a3); if (b3 <= -a3) b3 += 2 * a3; if (b3 > a3) b3 -= 2 * a3;
    return reducefD(a3, b3, D);
}

static int feq(Form f, Form g) { return f.a == g.a && f.b == g.b && f.c == g.c; }

int main(int argc, char *argv[]) {
    for (int ai = 1; ai < argc; ai++) {
        ll DD = atoll(argv[ai]);
        ll D = -DD;
        int odd = ((D % 2) + 2) % 2;
        ll bi = odd ? 1 : 0;
        Form ident = {1, bi, (bi * bi - D) / 4};
        Form *forms = malloc(1000000 * sizeof(Form));
        int h = 0;
        ll Amax = 0; while (3 * (Amax + 1) * (Amax + 1) <= DD) Amax++;
        Amax++;
        for (ll a = 1; a <= Amax; a++) {
            for (ll b = -a; b <= a; b++) {
                ll num = b * b - D;
                if (num % (4 * a) != 0) continue;
                ll c = num / (4 * a);
                if (c < a) continue;
                if ((llabs_(b) == a || a == c) && b < 0) continue;
                forms[h++] = (Form){a, b, c};
            }
        }
        int hasid = 0;
        for (int i = 0; i < h; i++) if (feq(forms[i], ident)) hasid = 1;
        int allexp5 = 1, n1 = 0, n5 = 0, nother = 0;
        for (int i = 0; i < h; i++) {
            Form f2 = compose(forms[i], forms[i], D);
            Form f4 = compose(f2, f2, D);
            Form f5 = compose(f4, forms[i], D);
            if (feq(f5, ident)) {
                if (feq(forms[i], ident)) n1++;
                else n5++;
            } else { allexp5 = 0; nother++; }
        }
        printf("D=%lld h=%d hasid=%d exp5forall=%d n_id=%d n_ord5=%d n_other=%d",
               D, h, hasid, allexp5, n1, n5, nother);
        if (h == 125 && allexp5 && hasid) printf("  <== (C5)^3 CONFIRMED");
        printf("\n");
        fflush(stdout);
        free(forms);
    }
    return 0;
}
