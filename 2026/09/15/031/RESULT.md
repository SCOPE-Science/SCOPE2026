# Closed q-binomial expansion for the corner-weighted rectangle generating function

## Context
The target asked whether the Gamma-deformed corner-weighted sequence
A_k(l,m,z) over partitions fitting in an l x m rectangle is unimodal in k
for all l,m and real z>=1. Direct per-stratum attacks failed: the v=1
stratum is a wildly oscillating restricted divisor function and no
v-nondecreasing injection P_k -> P_{k+1} exists. The present result is the
complete enumerative content of the target object: a closed generating-function
identity that reduces the open unimodality question to staggered-centre
q-binomial sums. The full unimodality claim is explicitly not proved here.

## Definitions
Fix integers l,m>=1. Let P(l,m) be partitions with at most l parts each at
most m, P_k(l,m) those of size k, and v(alpha) the number of distinct positive
part sizes of alpha (equivalently the number of corners of its Young diagram).
For parameter z put w_v(z)=binomial(v+z-1,v)=Gamma(v+z)/(Gamma(v+1)Gamma(z))
with w_0=1, A_k(l,m,z)=sum_{alpha in P_k(l,m)} w_{v(alpha)}(z), and
F_{l,m,z}(q)=sum_{k=0}^{lm} A_k(l,m,z) q^k. Each A_k is a polynomial in z of
degree at most min(l,m). Let [n choose k]_q denote the Gaussian binomial
(0 if k<0 or k>n).

## Result
As a polynomial identity in z (hence for every complex z):
F_{l,m,z}(q) = sum_{i>=0} binomial(z-1,i) q^{i(i+1)/2} [m choose i]_q [m+l-i choose l-i]_q,
effectively over 0<=i<=min(l,m). By diagram conjugation, which preserves v,
the twin with l<->m holds simultaneously. Corollaries: at z=1 only i=0
survives, recovering the classical [m+l choose l]_q; at z=0 the sum collapses
to 1 (only the empty partition has v=0); at integer z=r>=1 all weights
binomial(r-1,i)>=0. The identity does not prove unimodality: summands
g_i(q)=q^{i(i+1)/2}[m choose i]_q[m+l-i choose l-i]_q are symmetric unimodal
about (lm+i)/2 with staggered centres, and positive staggered combinations
need not be unimodal.

## Proof / evidence
Lemma 1: with G(q,t)=sum_{alpha} t^{v(alpha)}q^{|alpha|},
G(q,t)=sum_{j=0}^l [u^j] prod_{n=1}^m (1-(1-t)uq^n)/(1-uq^n), by marking total
parts with u via multiplicities e_n and extracting total parts <=l.
Lemma 2: e_i(q,...,q^m)=q^{i(i+1)/2}[m choose i]_q by staircase shift;
h_j=q^j[m+j-1 choose j]_q with partial sums sum_{k<=L}h_k=[m+L choose L]_q by
subtracting 1 from each part. Hence G(q,t)=sum_i (t-1)^i g_i(q).
Lemma 3: L_z(t^v)=w_v(z) satisfies L_z[(1-t)^i]=(-1)^i binomial(z-1,i) as
polynomials in z, by writing the sum over a, using binomial(a+r-1,a)=(-1)^a
binomial(-r,a) at integer r>=1, applying Chu-Vandermonde, and extending by
polynomial agreement on all positive integers. Applying L_r termwise at
integer r gives (*); both sides are polynomials in z agreeing on all positive
integers, so (*) holds for all z. Verification: 35/35 definition-vs-formula
matches on (l,m) in {(1,3),(2,2),(2,3),(3,4),(4,4),(5,6),(6,6)} x
z in {1,2,3,1.5,2.5} with max error <1e-6, exact rational witness
A(3,4,3)=(1,3,6,12,18,24,28,28,25,19,12,6,3), independently recomputed exactly
by the auditor including half-integer z.

## Limitations
Proved: identity (*) and twin plus corollaries (i)-(iii). Computed but not
proved: unimodality of A_k on tested grids (l,m<=12, dense z); non-unimodality
of strata and of arbitrary staggered combinations (documented witnesses).
The full target unimodality for every l,m and real z>=1 remains open.

## Reproducibility
Enumerate partitions in the l x m box by recursion on part sizes, compute
v(alpha) as the number of distinct parts, form A_k with rising-factorial
weights, and compare against the q-binomial convolution using partition-in-box
counts for each Gaussian polynomial plus the q^{i(i+1)/2} shift; see
output/artifacts/verify.json.

## References
Kronenburg arXiv:2206.05062 (q-binomial sums); Melczer-Panova-Pemantle
arXiv:1805.08375 (rectangle asymptotics); Yee JCTA 2004 (finite
Andrews-Stanley refinement); Pak partition-bijections survey Sec 2.4;
Bridges arXiv:2004.12036; Ballantine-Beck-Merca-Sagan arXiv:2409.11268.
