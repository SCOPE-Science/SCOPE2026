# Certified class-number census for real quadratic Q(sqrt(d)), 201 <= d <= 350 squarefree

## Context
Real-quadratic class numbers connect Minkowski finiteness to Cohen-Lenstra
heuristics, but bounded-d strata beyond textbook d < 200 tables lack a single
citable bundle with numbers, non-principality certificates, and
regulator/period data plus rerunnable code. The interval 201-350 is the first
full post-textbook block where the Minkowski bound M(D)=sqrt(D)/2 stays below
18.63 (only primes p <= 17), so every non-principality claim rechecks by a
short norm-equation / rho-chain check, while regulators already span an order
of magnitude and the class-number distribution becomes nontrivial.

## Definitions
For squarefree d, K=Q(sqrt(d)), discriminant D=d if d=1 mod 4 else D=4d,
M(D)=sqrt(D)/2. l(d) is the continued-fraction period of sqrt(d).
The maximal-order fundamental unit is written eps_d=(x+y sqrt(d))/2 with
x=y mod 2 when D=d, else y even; N(eps_d)=+-1; regulator R_d=log(eps_d).
Narrow classes are rho-cycles of reduced indefinite forms of discriminant D;
K is the narrow class of a principal ideal of negative norm when N=+1, and
ordinary classes are narrow classes modulo K (h=h+ if N=-1 else h+/2).

## Result
For all 91 squarefree d in [201,350]:

- Class numbers and structures: h=1 on 38 fields; h=2 (C2) on 34;
  h=3 (C3) on 6 (223,229,254,257,321,326); h=4 on 10 (C4 on
  219,274,291,322,323; C2xC2 on 210,231,255,290,330); h=6 (C6) on 235,346;
  h=8 (C8) on 226.
- For each of the 53 fields with h>1, an explicit prime ideal of norm
  p <= M(D) is given as a prime form (p,b,c) plus its exact rho-reduction
  chain into a certified nonprincipal narrow cycle outside {C0,CK}.
- Periods, maximal-order units, and regulators are tabulated (40 digits in
  artifact). Extremal witnesses are unique on the interval and both at
  d=331: longest period l=34 and largest regulator
  R=36.25638320432540082048..., eps=2785589801443970+153109862634573 sqrt(331)
  (norm +1). Regulator maximality is proved by exact integer comparison of
  all 91 units; runner-up is d=334 (R=32.47999...), gap 3.776.
  Minimum regulator is 2.703575... at d=221. Maximum class number is h=8
  at d=226 despite minimal period l=1.
- Correction: R~=47.21 at d=277 in the topic brief is the non-maximal-order
  norm+1 unit (convergent n=41, p=159150073798980475849); the true field
  regulator is R_277=7.8682544119... with eps=(2613+157 sqrt(277))/2 of
  norm -1. The minimal order unit (n=20) has regulator 23.6047... (3x).

## Proof / evidence
Exact-integer pipeline in pure Python (stdlib + numpy for sums + mpmath only
for digit strings): squarefree sieve; CF by (m,d,a) recurrence; maximal-order
unit from convergents n<2l with N=+-1 and N=+-4 odd half-units, exact minimum,
Legendre check 8y<x+y sqrt(d), exhaustive search to 4l plus growth
certificate v_{4l-1}>2 eps0; reduced-form enumeration (|a|,|b|<=isqrt(D),
exact reduced predicate), rho permutation, disjoint even-length cycles,
unique a=1 and a=-1 forms; K-form from (x+sqrt(d)) resp. ((x+sqrt(d))/2) of
negative norm with two-alpha agreement and CK==C0 iff N=-1; Kronecker
splitting and prime forms (p,b,c) rho-reduced to cycles, nonprincipal iff
outside {C0,CK}; Dirichlet composition of coprime-a forms plus rho reduction
with per-field identity, K^2=C0, inverse, associativity spot, and
well-definedness checks; ordinary group as quotient by K (h<=8, orders
determine structure). Independent verifier re-derives everything from the
CSV/JSON with no shared functions (6 check groups PASS). Analytic
class-number formula h*R=sqrt(D)/2*L(1,chi_D) via vectorized sums to N=1e6
with rigorous D/N tail bound agrees on 91/91 (worst gap/bound 0.035; wrong h
by >=1.5x would exceed bound by ~50x). LMFDB spot checks match: 2.2.904.1
(h=8, R=3.40230664548), 2.2.277.1 (h=1, R=7.86825441198), 2.2.1324.1 (h=1,
R=36.2563832043, narrow C2).

## Limitations
Finite computation, not a new theoretical theorem; background theorems
(Minkowski generation, cycles=narrow classes, K-quotient, composition,
class-number formula) are textbook. No PARI bnfcertify in sandbox; replaced
by formula check plus from-scratch verifier. Regulator digits beyond ~15 rely
on mpmath; ordering uses exact integers only. Order-regulator factor wording
(6x vs 3x for norm+1 vs minimal unit at d=277) should be read as norm+1
comparison.

## Reproducibility
Run `python3 verify.py` inside the artifact directory (stock Python + numpy +
mpmath); it re-derives CF/units/cycles/K/h, verifies all 53 witness chains,
recomputes h>=4 structures, proves extrema exactly, and spot-checks the
formula at N=2e5 in minutes. Full pipeline scripts and CSV/JSON are in
output/artifacts/.

## References
- Amir-He-Lee-Oliver-Sultanow, Machine Learning Class Numbers of Real
  Quadratic Fields, arXiv:2209.09283 (predictive, no proofs).
- Bernardini, Class number of real quadratic fields of explicit
  discriminant, arXiv:2412.06351 (sparse family, exceptions).
- Kopp-Lagarias, Unit-generated orders I, arXiv:2512.11311 (orders, not
  interval maximal orders).
- Lamzouri, Large moments and extreme values, arXiv:1609.01630 (asymptotic).
- Cherubini-Fazzari-Granville-Kala-Yatsyna, Consecutive real quadratic
  fields with large class numbers (existence, not census).
- PARI/GP headquarters, https://pari.math.u-bordeaux.fr/ (tool baseline).
- LMFDB 2.2.904.1, 2.2.277.1, 2.2.1324.1 (single-field bare values).
