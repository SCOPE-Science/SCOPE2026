# Exact Steinberg spherical growth rates and golden-ratio minimal-growth witnesses for right-angled Coxeter groups on connected graphs with 4-6 vertices

## Context

Let $G$ be a finite simple connected graph with vertex set $S$, $|S|=n$, and
$W_G$ the right-angled Coxeter group with generators $s \in S$ of order 2
where $st=ts$ iff $st$ is an edge of $G$. Let
$W_G(t)=\sum_{w \in W_G} t^{\ell(w)}$ be the spherical growth series
($\ell$ = word length in $S$). Its exponential growth rate is
$\tau_G = 1/\rho_G$ where $\rho_G$ is the radius of convergence.
This work sits in the recognized Coxeter-growth program (Milnor-Wolf/Gromov
growth, Steinberg/Brink-Howlett rationality, Kellerhals-type minimal growth,
Perron/Salem arithmetic of rates, Terragni monotonicity and universal bound
$\approx 1.13$). Prior work proves type-level facts but publishes no uniform
replayable exact-rate table over the small connected-graph RACG strata, which
serves as test/benchmark data for minimal-growth, monotonicity, and
growth-series software.

## Definitions

- Spherical subset: for RACGs, $T \subseteq S$ is spherical iff $T$ is a
  clique of $G$, with finite-parabolic Poincare polynomial
  $W_T(u)=(1+u)^{|T|}$.
- Clique vector: $c_k$ = number of $k$-cliques of $G$ ($c_0=1$);
  $\omega$ = clique number.
- Steinberg denominator:
  $M_G(t)=\sum_{k=0}^{\omega}(-1)^k c_k t^k(1+t)^{\omega-k}\in\mathbb Z[t]$,
  $M_G(0)=1$, so $W_G(t)=(1+t)^{\omega}/M_G(t)$.
- Regimes: `finite` if $M_G\equiv 1$ (finite $W_G$); `subexponential` if
  $M_G(t)=(1-t)^k$ exactly for some $k\ge 1$ (only pole at $t=1$,
  $\tau_G=1$); `exponential` if $M_G$ has a root in $(0,1)$ and the smallest
  such root $r_G$ gives $\tau_G=1/r_G>1$.

## Result

For every connected graph $G$ with $4\le |G|\le 6$ (6 graphs at $n=4$,
21 at $n=5$, 112 at $n=6$):

- the growth series equals $(1+t)^{\omega(G)}/M_G(t)$ with the exact integer
  polynomial $M_G$ and clique data in the tables, and $\tau_G$ lies in the
  listed rigorous interval of width $\le 10^{-6}$ (in fact $\le 2\times
  10^{-11}$);
- among graphs with $\tau>1$, the per-stratum minimal exponential rate is
  the golden ratio $\varphi=(1+\sqrt5)/2\approx 1.6180339887$:
  - $n=4$: unique minimizer the paw (triangle with pendant edge; edges
    `01 02 03 12`), $M=1-t-t^2$; next rate $2.0$ (gap $0.382$);
  - $n=5$: exactly two tied minimizers, `n5-016` (edges
    `01 02 03 12 13 24 34`, $M=1-2t+t^3=(1-t)(1-t-t^2)$) and `n5-017`
    (edges `01 02 03 04 12 13 14 23`, $M=1-t-t^2$); next rate $\ge 2.0$;
  - $n=6$: exactly three tied minimizers, `n6-101`
    ($M=1-2t-t^2+2t^3+t^4=(t^2+t-1)^2$, double root at $\varphi^{-1}$),
    `n6-106` ($M=1-2t+t^3=(1-t)(1-t-t^2)$), `n6-108` ($M=1-t-t^2$);
    next rate $\ge 2.0$;
- rate-one graphs: one finite $K_n$ ($M\equiv 1$) per stratum; plus
  subexponential $M=(1-t)^k$ rows: two at $n=4$ (`n4-003`: $(1-t)^2$,
  `n4-004`: $1-t$), two at $n=5$ (`n5-018`: $1-2t+t^2$, `n5-019`: $1-t$),
  three at $n=6$ (`n6-107`: $(1-t)^3$, `n6-109`: $1-2t+t^2$, `n6-110`:
  $1-t$), each with $\tau=1.0/1.0$.
- Regime counts (finite/subexponential/exponential): 1/2/3 at $n=4$,
  1/2/18 at $n=5$, 1/3/108 at $n=6$.

## Proof / evidence

- Steinberg formula (Steinberg 1968; Davis Thm 17.1.9): with
  $c_k$ and $\omega$ as above,
  $1/W_G(t)=\sum_k(-1)^k c_k t^k/(1+t)^k=M_G(t)/(1+t)^\omega$.
  Pringsheim's theorem (nonnegative Taylor coefficients) gives radius =
  smallest positive real pole = smallest root of $M_G$ in $(0,1)$
  ($\tau=1$ if none).
- Computation: brute-force bitmask enumeration with exact permutation
  canonical representatives (counts 6/21/112); per graph brute-force clique
  vector, exact integer $M_G$, 12-term series check ($W_0=1$, nonnegative
  integers, matching recurrence); exact Sturm-sequence root count on
  $(0,1)$ over `Fraction` arithmetic; rigorous bisection enclosure of the
  smallest root (width $\le 10^{-12}$), hence $\tau=1/r$ intervals of width
  $\le 10^{-6}$; exact $(1-t)^k$ pre-test for subexponential rows.
- Independent replay `verify_census.py` (stdlib only): connectivity,
  canonical minimality, clique/$M$/series match, Sturm counts, interval
  containment and width, minimality statistic - PASS on all 139 rows.
- Auditor re-ran the verifier (PASS, exact witness sets) and an independent
  numpy-roots cross-check on all 139 rows (all exponential $\tau$ inside
  listed intervals; no non-exponential row has a root strictly inside
  $(0,1)$).
- Ties are exact by displayed factorization (common factor $1-t-t^2$;
  squared case $(t^2+t-1)^2$ still gives the radius by Pringsheim plus the
  positive series check). Minimality is certified by disjoint enclosures:
  every non-witness exponential row has recomputed interval lower bound
  $\ge 2.0 > 1.6180339890 \ge \varphi$.
- Boundary subtlety handled: 12 exponential rows have $M_G(1)=0$ but a
  smaller root in $(0,1)$ (e.g. `n5-012`: $M=(1-t)(1-2t)$, roots $1/2$
  and $1$, $\tau=2$); they are correctly exponential because the enclosure
  certifies the smallest root $<1$. Pure $(1-t)^k$ rows are subexponential.

## Limitations

- Graph enumeration uses brute-force canonicalization exact for $n\le 6$,
  not a general tool.
- Perron/Salem arithmetic of individual rates is not proved per graph
  (only numerical enclosures plus exact factors where stated).
- Word-length interpretation is spherical (standard generators), not
  geodesic length or Artin-group growth.
- Completeness (6/21/112 isomorphism types) rests on the committed
  bitmask-plus-permutation enumeration matching the classical sequence.

## Reproducibility

- Scripts (stdlib only): `artifacts/steinberg_census.py` (computation),
  `artifacts/verify_census.py` (independent replay).
- Tables: `artifacts/tables/table_n4.csv`, `table_n5.csv`, `table_n6.csv`
  with columns id, edges, m, clique, om, M, tau_lo, tau_hi, regime, w8.
- Run: `python3 artifacts/verify_census.py` (replays all 139 rows, prints
  PASS and the per-stratum phi-witness sets).

## References

- A. Kolpakov, A. Talambutsa, Spherical and geodesic growth rates of
  right-angled Coxeter and Artin groups are Perron numbers,
  arXiv:1809.09591. Type-level Perron theorem; no per-graph series/ranking.
- T. Terragni, On the growth of a Coxeter group, arXiv:1312.3437.
  Diagram-order monotonicity and universal lower bound $\approx 1.13$;
  general bound, not exact small-graph rates.
- T. Terragni, Data about hyperbolic Coxeter systems, arXiv:1503.08764.
  Poincare series/rates for prec-minimal hyperbolic systems (Magma);
  disjoint object class from the connected-graph RACG stratum.
- M. Davis, The Geometry and Topology of Coxeter Groups, Thm 17.1.9
  (Steinberg formula).
