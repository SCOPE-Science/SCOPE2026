# Sharp seasonal sorting boundary and three-season reversal for common-equilibrium Hassell recruitment

## Finding

Fix a shared positive equilibrium \(K>0\), a Hassell exponent \(p>0\), and a positive seasonal density-feedback strength \(a\). Define the recruitment map
\[
H_a(x)=x\left(\frac{1+aK}{1+ax}\right)^p,\qquad x>0.
\]
The classical Hassell growth multiplier is \((1+aK)^p\). For every \(0<a<b\) and \(x>0\) with \(x\ne K\),
\[
\operatorname{sgn}\bigl(H_b(H_a(x))-H_a(H_b(x))\bigr)=\operatorname{sgn}(p-1).
\]
At \(p=1\), all these maps commute identically. For \(0<p<1\), the **descending-strength** schedule maximizes the final abundance among every permutation of an arbitrary finite multiset of seasons, and the ascending-strength schedule minimizes it, for any initial \(x>0\) away from \(K\). For \(p>1\), an **ascending-strength** schedule maximizes, and descending minimizes, on \(0<x<K\) whenever all seasonal strengths satisfy \(a(p-1)K\le1\). In each ordered case, strict inequality holds versus any genuinely different ordering of unequal strengths.

This last bound is sharp as a universal three-season sorting guarantee. If \(p>1\), \(0<a<b<c\), and \(c(p-1)K>1\), then for every starting value \(x<K\) sufficiently close to \(K\),
\[
H_c(H_b(H_a(x)))<H_c(H_a(H_b(x))).
\]
Thus the ascending arrangement loses to a schedule swapping its first two seasons; no two-season case can exhibit that failure, since its universal exchange sign never changes.

## Assumptions and scope

The model is a deterministic positive scalar discrete-time Hassell recruitment map, with shared positive equilibrium \(K\) and shared exponent \(p\). Seasonal strengths are positive, with no upper restriction except where the monotonicity-dependent multi-season result explicitly imposes one. A schedule is a composition of the listed season maps, each applied exactly once in its specified temporal order. An ``optimal schedule'' means largest final population for a fixed initial population after those finitely many updates, *not* a long-run growth objective. When comparing permutations, relabelings of equal strengths are identified. The model makes no claim about the ecological desirability of maximizing abundance.

## Proof

**Pairwise exchange.** Put \(L_a=(1+aK)^p\) and
\[
D_{a,b}(x)=1+ax+\frac{b L_a x}{(1+ax)^{p-1}}.
\]
Direct substitution, retaining all positive denominators, yields
\[
H_b(H_a(x))=\frac{L_aL_b x}{D_{a,b}(x)^p}.
\]
For \(0<a<b\), the difference of swapped denominators is \(D_{b,a}(x)-D_{a,b}(x)=xG(x)\), where
\[
G(x)=b-a+\frac{a(1+bK)^p}{(1+bx)^{p-1}}-\frac{b(1+aK)^p}{(1+ax)^{p-1}}.
\]
It obeys \(G(K)=0\) and
\[
G'(x)=-(p-1)ab\left[\left(\frac{1+bK}{1+bx}\right)^p-\left(\frac{1+aK}{1+ax}\right)^p\right].
\]
For \(x<K\), the expression \((1+tK)/(1+tx)\) is strictly increasing in \(t>0\); for \(x>K\) it is strictly decreasing. Hence if \(p>1\), \(G\) decreases toward zero on \((0,K)\) and increases away from zero on \((K,\infty)\); thus \(G(x)>0\) on both intervals. If \(0<p<1\) the signs are reversed. The common numerator in the two compositions is positive, and raising positive denominators to \(p>0\) preserves their order; the sign assertion follows. At \(p=1\), \(G\equiv0\), so the maps commute.

**Global permutations below the scramble boundary.** Direct differentiation gives
\[
H_a'(x)=\frac{H_a(x)}{x(1+ax)}\bigl[1+(1-p)ax\bigr].
\]
For \(0<p<1\), every map is strictly increasing throughout \((0,\infty)\), so swapping any adjacent inverted strengths according to the pairwise sign strictly improves the final output, with every subsequent map preserving that comparison. No intermediate iterate reaches \(K\) from an input other than \(K\), because an increasing map fixes \(K\) and is injective. Repeated adjacent swaps yield the descending maximum and ascending minimum.

For \(p>1\) and \(a(p-1)K\le1\), each map is strictly increasing on \([0,K)\), nondecreasing on \([0,K]\), sends \(0\) to \(0\) and \(K\) to \(K\), and hence preserves the interval \([0,K]\). All intermediate positive iterates from \(x<K\) remain strictly below \(K\); adjacent-exchange improvements therefore survive every subsequent map and give the opposite sorting order. At \(p=1\), compositions are independent of the permutation.

**Sharp failure at three seasons.** For \(p>1\) and \(c(p-1)K>1\), the derivative at the shared equilibrium is
\[
H_c'(K)=\frac{1-(p-1)cK}{1+cK}<0.
\]
By continuity, \(H_c\) is strictly decreasing in a neighborhood of \(K\). The pairwise exchange already proved ensures \(H_b(H_a(x))>H_a(H_b(x))\) for every \(x<K\). As \(x\uparrow K\), both expressions tend to \(K\); applying the decreasing \(H_c\) reverses their order for all sufficiently near-equilibrium \(x<K\). The weak inequality \(c(p-1)K\le1\) therefore cannot be extended to any larger universal bound for three distinct strengths. Two seasons obey the exchange sign for every positive initial value and every strength pair, so three are minimal for this sorting failure.

**Exact witness.** With \(p=2\), \(K=1\), strengths \((1/2,1,2)\), and initial value \(x=1/2\), direct rational arithmetic gives the ascending final value \(29953800/29691601\), while interchanging the first two strengths gives \(246402/243049\), larger by exactly \(35828733402/7216513931449>0\). All maps and fractions are positive.

## Verification

Run `python3 verify.py` with Python 3.10+ (standard library only). It evaluates 11,444 sampled pairwise and four-season permutation comparisons with deterministic random seed, checks exact commuting behavior numerically at \(p=1\), and replays the fully rational three-season witness using `fractions.Fraction`. Expected final status: `PASS: 11444 sampled pair and permutation comparisons, plus exact-rational witness`. These finite checks verify implementation and the witness but are **not** the proof of the quantified inequalities, which is analytical above.

## Relationship to prior work

Hassell (1975) introduced the underlying density-feedback family and studied equilibria and population stability, not the present finite-horizon ordering phase diagram. Jaggi and Joshi (2001) studied the stabilizing effects of spatial density variation in Ricker and Hassell maps, not the effect of temporal permutation at a common equilibrium. Elaydi and Sacker (2005) studied nonautonomous Beverton–Holt equations, their periodic solutions and averages; the \(p=1\) common-equilibrium commuting case here is consistent with this general setting but is not claimed as a novel equation. The novelty proposed here is the **combined strict exchange law for finite \(p\)**, its arbitrary-season sorting consequences, and the sharp **three-season failure threshold** at the Hassell monotonicity boundary, not the use of adjacent exchanges as a general proof method. Published-record and prior-result searches yielded no direct statement implying this complete classification; absence from search is not a priority proof.

## Limitations

The sharp counterexample tests guaranteed sorting and does not characterize the globally optimal permutation in every overcompensatory regime. The upper strength condition pertains to inputs below the common equilibrium and to finite-horizon optimization. Different equilibria, different exponents, negative/zero parameters, ecological noise, harvesting, and objectives based on multi-year stationary cycles are not covered. Priority remains provisional: no exhaustive historical survey of all period-map rearrangement theorems or inaccessible publisher-only material was possible.

## References

1. M. P. Hassell (1975), “Density-dependence in single-species populations,” *Journal of Animal Ecology* **44**, 283–295, doi:10.2307/3863. A lawful public manuscript reproduction was read, including the recruitment equation and stability discussion.
2. S. Jaggi and A. Joshi (2001), “Incorporating spatial variation in density enhances the stability of simple population dynamics models,” *Journal of Theoretical Biology* **209**, 249–255, doi:10.1006/jtbi.2000.2260, publication date 2001-03-21 (PubMed PMID 11401466). Abstract and repository catalog inspected; public full PDF access was unsuccessful.
3. S. Elaydi and R. J. Sacker (2005), “Nonautonomous Beverton–Holt equations and the Cushing–Henson conjectures,” *Journal of Difference Equations and Applications*, doi:10.1080/10236190412331335418. Open HTML copy of the complete paper inspected.
