# Short- versus Long-Root Zonotope Alexandrov–Fenchel Extremal Witnesses (C4/C5/C6 and F4)

## Context

The Alexandrov–Fenchel (AF) inequality states that for convex bodies
K, L, C_1, ..., C_{n-2} in R^n,

  V(K, L, C)^2 >= V(K, K, C) V(L, L, C),

where V denotes mixed volume and C = (C_1,...,C_{n-2}).
Characterizing its extremals (equality vs strict inequality) is a
long-standing open problem (Alexandrov 1937; Shenfeld–van Handel 2023;
Chan–Pak 2024 hardness). Concrete exact witnesses — pairs proved
non-homothetic with a certified strictly positive deficit — are
independently valuable data points. This record establishes such
witnesses for natural root-system zonotopes.

## Definitions

Work in R^n in Bourbaki coordinates with standard basis e_1,...,e_n.
For a finite generator multiset G, the (centrally symmetric) zonotope is

  Z(G) = sum_{g in G} [-g, g].

For n in {4,5,6}, let A = {e_i +/- e_j : i<j} (2*C(n,2) generators) and
B = {2e_i : 1<=i<=n} (n generators). Define:

  Z_n^s = Z(A)  (C_n short-root zonotope),
  Y_n^l = Z(B)  (C_n long-root zonotope; a coordinate cube [-2,2]^n up to the segment convention).

Reference tuple: C = (Z_n^s, ..., Z_n^s), n-2 copies.

For F4 in rank 4: short-root pairs are {+/-e_i} (4 pairs) plus
{(+/-1/2,...,...,+/-1/2) with first coordinate +1/2} (8 pairs);
long-root pairs are {+/-(e_i +/- e_j)} (12 pairs). Both zonotopes are
centrally symmetric about 0. Reference tuple C = (Zs, Zs).

## Result

For each n in {4,5,6}, Z_n^s and Y_n^l are not homothetic modulo
translation, and with C as above

  V(Z_n^s, Y_n^l, C)^2 - V(Z_n^s, Z_n^s, C) V(Y_n^l, Y_n^l, C)
      = 2^{2n} N / (n^2 (n-1)) > 0,

where N = (n-1) S1^2 - n S0 S2 is the positive integer:

  n=4: S0=636,  S1=1376,   S2=1632,    N=1528320;
  n=5: S0=15744, S1=30360,  S2=36480,  N=815212800;
  n=6: S0=470680, S1=839712, S2=1013280, N=663997432320.

Equivalently the mixed volumes are:
  n=4: V(Z,Z,C)=10176, V(Z,Y,C)=5504, V(Y,Y,C)=2176;
  n=5: V(Z,Z,C)=503808, V(Z,Y,C)=194304, V(Y,Y,C)=58368;
  n=6: V(Z,Z,C)=30123520, V(Z,Y,C)=8956928, V(Y,Y,C)=2161664.

The F4 short-vs-long pair likewise satisfies non-homotheticity and,
with C=(Zs,Zs),

  S0=159, S1=1032, S2=4680,
  N = 3 S1^2 - 4 S0 S2 = 218592 > 0,

hence strict AF deficit. Each pair is therefore an explicit
non-trivial extremal witness with exactly computed deficit.

## Proof / Evidence

Volume formula and reduction (exact). For zonotopes Z(G_1),...,Z(G_n),

  V(Z(G_1),...,Z(G_n)) = 2^n sum |det(g_1,...,g_n)|

over transversals (one generator from each body); this is the
polarization of vol(Z(G)) = 2^n sum_{|S|=n} |det G_S|.
With C=(Z,...,Z) (n-2 copies), define integer sums S0 (all n generators
from A), S1 (one B generator plus n-1 from A), S2 (two ordered distinct
B generators plus n-2 from A). Slot counting gives
V(Z,Z,C)=2^n S0, V(Z,Y,C)=2^n S1/n,
V(Y,Y,C)=2^n S2/(n(n-1)), and deficit sign = sign(N),
N=(n-1)S1^2-nS0S2. Diagonal b1=b2 terms have det 0 and are excluded.

Non-homotheticity (analytic). Both C_n bodies are 0-symmetric, so
Y=aZ+x forces x=0 and h_Y = a h_Z for support functions.
h_Z(e_1)=2(n-1), h_Y(e_1)=2, giving a=1/(n-1); in direction
u=(1,...,1), h_Z(u)=n(n-1), h_Y(u)=2n, giving a=2/(n-1), a
contradiction for every n>=2. For F4, exact Fraction arithmetic gives
h_Zs(e_1)=5 vs h_Zl(e_1)=6 (ratio 6/5) while in direction v=(1,1,0,0),
h_Zs(v)=6 vs h_Zl(v)=10 (ratio 5/3), contradiction.

Certified computation. output/artifacts/compute_cn.py evaluates all
integer determinants (float batched, rounded to nearest integer) with
tracked max deviation 1.78e-15 << 1/2 for every determinant in all
ranks, certifying exactness; independent exact Bareiss recomputation
matches the n=4 triple and n=5 S0, plus 300 randomized Bareiss-vs-float
spot checks per rank with zero mismatches (rerun:
python3 output/artifacts/compute_cn.py 4 5 6; n=6 enumerates
C(30,6)=593775 six-subsets plus augmented sums, minutes).
output/artifacts/compute_f4.py uses exact Fraction/Bareiss arithmetic
with denominator clearing, giving (159,1032,4680,218592).

## Limitations

The n=6 full enumeration uses float determinants with the rounding
certificate plus exact cross-checks rather than a fully exact Bareiss
rerun. The AF prefactors rest on the standard zonotope polarization
identity with the slot counting above. No generality beyond the stated
C_n and F4 root pairs is claimed.

## Reproducibility

Run `python3 output/artifacts/compute_cn.py 4 5 6` and
`python3 output/artifacts/compute_f4.py`; compare S0/S1/S2/N and the
maxdev certificate. Support-function values can be recomputed by hand
from h_{Z(G)}(u)=sum_g |<g,u>|.

## References

- A. D. Alexandrov, original AF inequality (1937).
- Y. Shenfeld & R. van Handel, The extremals of the AF inequality for
  convex polytopes, arXiv:2011.04059 / Acta Math. 231 (2023).
- S. H. Chan & I. Pak, Equality cases of the AF inequality are not in
  the polynomial hierarchy (2024).
- C. De Concini & C. Procesi, The zonotope of a root system,
  Transformation Groups 13 (2008), doi:10.1007/s00031-008-9031-z.
