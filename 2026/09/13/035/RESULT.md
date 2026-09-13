# Green-function minimum on [0.4, 0.6] for the middle-third Cantor set exceeds 0.27

## Context

Let C be the middle-third Cantor set in [0, 1]. Its logarithmic equilibrium
measure mu, Robin constant V = I(mu), and logarithmic potential
U(x) = integral log(1/|x - y|) mu(dy) are standard objects of logarithmic
potential theory. The admitted target asked for a rigorous certified
two-sided enclosure proving m in [0.17, 0.27], where
m = min_{x in G} (V - U(x)) with G = [0.4, 0.6], or a rigorous certified
bound placing m strictly outside that interval. The interval G lies inside
the first removed open middle third (1/3, 2/3), so it is disjoint from C.

## Definitions

- C: middle-third Cantor set, compact, non-polar (Hausdorff dimension
  log 2 / log 3 > 0).
- mu: logarithmic equilibrium measure of C; V = I(mu) finite Robin constant.
- U(x): logarithmic potential with sign convention log(1/|x - y|).
- G = [0.4, 0.6] = [2/5, 3/5].
- m = min_{x in G} (V - U(x)), attained since V - U is continuous on G
  (dist(G, C) >= 1/15).
- g_C: Green function of C^c = C complement in C-hat with pole at infinity.
- E1 = [0, 1/3] union [2/3, 1], the level-one outer approximation, C subset E1.
- R(x) = 9x^2 - 9x + 1.

## Result

m >= (1/2) log((29 + 6 sqrt(6))/25) = g_{E1}(0.4) approx 0.2792011 > 0.27.

Hence m lies strictly above, and therefore strictly outside, the closed
interval [0.17, 0.27]. This resolves the TARGET via its second alternative
(rigorous certified bound strictly outside the interval) and disproves the
proposed enclosure.

## Proof / evidence

1. Green identity: C^c is connected, so g_C exists with pole at infinity and
   g_C(x) = V - U(x) for x off C, in particular on G. Thus m = min_G g_C.
2. Monotonicity: C subset E1 with both complements connected domains
   containing infinity gives C^c complement of E1 subset C^c complement of C,
   so g_C(x) >= g_{E1}(x) for x off E1, hence m >= min_G g_{E1}.
3. Exact outer Green function: R(x) + 1 = 9(x - 1/3)(x - 2/3), so
   E1 = R^{-1}([-1, 1]) (verified on [0,1] and off [0,1]; the complex
   extension uses that R^{-1}([-1,1]) intersect R = E1 and degree counting).
   By the degree-2 polynomial-preimage formula,
   g_{E1}(x) = (1/2) g_{[-1,1]}(R(x)) for x off E1, and for real w off
   [-1,1], g_{[-1,1]}(w) = log(|w| + sqrt(w^2 - 1)). On the gap (1/3, 2/3),
   g_{E1}(x) = (1/2) log(|R(x)| + sqrt(R(x)^2 - 1)).
   R is symmetric about 1/2, strictly decreasing on [1/3, 1/2], so
   min_G g_{E1} = g_{E1}(2/5) = g_{E1}(3/5).
4. Exact evaluation: R(2/5) = -29/25, R^2 - 1 = 216/625 = 36*6/625, so
   sqrt(R^2 - 1) = 6 sqrt(6)/25 and g_{E1}(2/5) = (1/2) log((29+6 sqrt6)/25).
5. Certified threshold: (1/2) log((29+6 sqrt6)/25) > 0.27 iff
   (29 + 6 sqrt6)/25 > exp(0.54). Exact rational chain: sqrt6 > 2449/1000
   (2449^2 = 5997601 < 6000000); exp(0.54) < 1.7161 via degree-7 Taylor sum
   S7 approx 1.7160066715 plus geometric remainder < 1.91e-7, so
   exp(0.54) < 1.7160068623 < 1.7161; bridge
   29 + 6(2.449) = 43.694 > 42.9025 = 25(1.7161) > 25 exp(0.54).
   All steps use integer/Fraction arithmetic only.

## Limitations

Certifies only the lower bound m > 0.27 (the disproving alternative). No
certified upper bound and no exact value of m are asserted; the bound is not
claimed sharp (uncertified pilot numerics suggest m approx 0.31-0.33).
Potential-theoretic ingredients (equilibrium existence/uniqueness, Green
identity, domain monotonicity, polynomial-preimage formula) are quoted as
standard textbook theorems, not re-proved.

## Reproducibility

Run `python3 output/artifacts/verify_bounds.py`: it checks the sqrt(6) bound,
the exp(0.54) Taylor-plus-remainder cap, the bridge inequality, and the exact
identities R(2/5) = -29/25 and R(2/5)^2 - 1 = 216/625, using Fraction
arithmetic only. Independent recomputation gives (29+6 sqrt6)/25 approx
1.7478775383 and half-log approx 0.2792011083.

## References

- T. Ransford, Potential Theory in the Complex Plane, Chapters 3-5
  (equilibrium measures, Green function, monotonicity, preimage formula).
- T. Ransford and J. Rostand, Computation of capacity, Math. Comp. 2007
  (Cantor capacity approx 0.220949102189507; global constant only).
- J. Liesen, O. Sete, M. M. S. Nasser, capacity computation series
  (2017, 2022, 2023): numerical methods and tables for Cantor capacity.
