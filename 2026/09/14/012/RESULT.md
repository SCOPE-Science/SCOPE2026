# E_{4,4}(|x^2-1/4|) on [-1,1] exceeds 0.02: certified lower bound 0.025 (DISPROOF)

## Context
Let f2(x)=|x^2-1/4| on [-1,1], with interior cusps at x=-1/2 and x=1/2.
Let E_{4,4}(f2) be the real rational minimax error over r=p/q with
deg p,deg q <= 4 and q nonzero on [-1,1].
The admitted target asks whether E_{4,4}(f2) <= 0.02.
Approximation theory (Newman, Stahl) studies root-exponential rational
approximation of cusp functions such as |x|, but gives no finite exact
value for this two-cusp object at type (4,4).

## Definitions
- t=x^2 in [0,1]; g(t)=|t-1/4|.
- R(x)=P(t)/Q(t) with P(t)=0.279088-2.074492t+4.253844t^2,
  Q(t)=1-1.309050t+3.719230t^2. R is even, hence type-(4,4) in x.
- rho=0.025=1/40; threshold 0.02.
- Nodes: -1,-0.856,-0.622,-0.5,-0.369,0,0.369,0.5,0.622,0.856,1.

## Result
The target claim is FALSE. In fact E_{4,4}(f2) >= 0.025 > 0.02.
The error e=f2-R strictly alternates in sign (+,-,+,-,+,-,+,-,+,-,+)
across the 11 ordered nodes with |e|>0.025 at every node (|e|~0.02909).
Since m+n+2=10 points suffice for type (4,4), the rational
de la Vallee Poussin theorem forces every real type-(4,4) rational to
have uniform error at least 0.025.

## Proof / evidence
1. Q positivity: Q is quadratic in t with discriminant
1.30905^2-4*3.71923<0 and Q(0)=1>0; vertex t*~0.176 in (0,1) with
minimum ~0.8848>0. Hence Q>0 on [0,1] and R is pole-free on [-1,1].
2. Node identities: exact rational arithmetic (Python fractions) gives,
e.g. e(0)=-909/31250=-0.029088, e(+/-1/2)=-210642/7241515~-0.0290881,
e(+/-1)=19839/682036~+0.0290879, and six further exact fractions, all
with |e|>1/40 and alternating signs; verified by output/artifacts/verify_cert.py.
3. Rational de la Vallee Poussin theorem: if r in R_{m,n} alternates with
amplitude >=rho on N=m+n+2 nodes and some s in R_{m,n} had error <rho,
then s-r=(uq-pv)/(vq) would have >=m+n+1 distinct zeros while uq-pv has
degree <=m+n, forcing s=r and contradicting ||f-s||<rho. Hence E_{m,n}>=rho.
With m=n=4, N=10 needed and 11 exhibited, E_{4,4}(f2)>=0.025.
Numerical Remez/DE searches suggest E44~0.0291 (R nearly optimal) but are
supporting evidence only, not part of the proof.

## Limitations
Certified bound is 0.025, not the numerically indicated true value ~0.0291.
Pinpointing the exact minimax value (defect analysis, full alternation
characterization) is not attempted. Resolves only the 0.02 threshold, not
neighboring thresholds in (0.025,0.029).

## Reproducibility
Run `python3 output/artifacts/verify_cert.py` (stdlib only, exact
fractions.Fraction arithmetic). Prints Qmin and all 11 node errors.

## References
- Rational de la Vallee Poussin theorem (proved in full in DRAFT).
- S.-I. Filip, Y. Nakatsukasa, L. N. Trefethen, B. Beckermann, Rational
  minimax approximation via adaptive barycentric representations (2018).
- R. S. Varga, A. Ruttan, A. D. Carpenter, best uniform rational
  approximation of |x| tables; Chebfun RationalAbsx example (different
  object |x|, no |x^2-1/4| threshold).
