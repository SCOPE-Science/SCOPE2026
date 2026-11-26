# Saturated parallel-edge bundles reverse loop covariance in regular configuration multigraphs

## Finding

Let integers \(n\ge3\) and \(d\ge2\) satisfy \(nd\) even. Pair the \(nd\) distinguishable half-edges uniformly, with \(d\) half-edges at each of \(n\) labeled vertices. Let \(L\) count loops, and let \(M_{uv}\) count edges between distinct vertices \(u,v\). For \(2\le r\le d\), define
\[
P_r=\sum_{u<v}\binom{M_{uv}}r,\qquad
p_r=\prod_{j=0}^{r-1}\frac{1}{nd-(2j+1)},\qquad
B_r=\binom n2\binom dr^2 r!.
\]
The extension to **higher bundles \(3\le r\le d\)** gives the exact finite-size covariance
\[
\boxed{\operatorname{Cov}(L,P_r)=B_rp_r\,\frac{r\{2d-r-1-nd(d-r)\}}{(nd-1)(nd-2r-1)}.}
\]
It is strictly negative for \(3\le r<d\) and strictly positive for \(r=d\ge3\). Thus the reversal occurs exactly when the bundle exhausts both endpoints. In the saturated case the bundle is a two-vertex component. The formula also holds at \(r=2\), but that case, including the positive sign at \(d=2\) and negative sign for \(d\ge3\), is prior work [4,5]. It is included to show the full spectrum, not as a new result.

For fixed \(d,r\), along admissible \(n\to\infty\), the formula yields
\[
\operatorname{Cov}(L,P_r)\sim
-\frac{r(d-r)\binom dr^2r!}{2d^{r+1}}\,n^{1-r}\qquad(2\le r<d),
\]
\[
\operatorname{Cov}(L,P_d)\sim \frac{d!(d-1)}{2d^{d+1}}\,n^{-d}.
\]
The positive saturated contribution decays faster than the negative unsaturated contributions. At \(r=2\) the rates also follow from the prior exact formula.

## Assumptions and scope

All half-edge pairings have equal probability; vertex-labeled multigraphs with the same degree sequence need not be equally likely. Loops count as single edges and contribute two to the degree. The statistic \(P_r\) counts \(r\)-subsets of parallel non-loop edges, not just vertex pairs with at least \(r\) edges. Under the hypotheses above, \(nd-2r-1>0\). If instead \(n=2\) and \(r=d\), then \(L\) and \(P_d\) cannot both be positive, and both have positive means, so their covariance is strictly negative.

## Proof

A specified set of \(r\) disjoint matched half-edge pairs has probability \(p_r\): after revealing \(j\) such pairs there are \(nd-2j-1\) possible partners for the next specified half-edge. For each unordered vertex pair there are \(\binom dr^2r!\) elementary bundle events, corresponding to choosing the half-edges at each endpoint and pairing them by a bijection. The indicators sum to \(P_r\), even when more than \(r\) parallel edges are present. Hence \(\mathbb E P_r=B_rp_r\). Counting possible same-vertex pairs likewise gives \(\mathbb E L=n\binom d2/(nd-1)\).

Condition on any one elementary bundle event. The remaining \(nd-2r\) half-edges are paired uniformly. The residual degrees are \(d-r\) at the two endpoints and \(d\) elsewhere. Thus the conditional number of eligible same-vertex pairs is
\[
(n-2)\binom d2+2\binom{d-r}2=n\binom d2-r(2d-r-1).
\]
Each residual same-vertex pair is matched with probability \(1/(nd-2r-1)\). The conditional loop expectation is independent of the choice of bundle event. Summing over those events gives
\[
\frac{\mathbb E[LP_r]}{\mathbb E P_r}
=\frac{n\binom d2-r(2d-r-1)}{nd-2r-1}.
\]
Subtracting \(\mathbb E L\) and multiplying by \(B_rp_r\) gives the covariance. At saturation the bracket in its numerator is \(d-1>0\). Otherwise \(nd(d-r)\ge3d>2d-r-1\), giving the strict negative sign. In probabilistic terms, a saturated bundle removes the endpoints altogether and raises the expected loop count on the remaining uniformly paired regular graph relative to the original expectation; an unsaturated bundle leaves two partially depleted vertices, for which the reduction in the number of eligible loop pairs dominates.

For fixed \(d,r\), \(B_r\sim n^2\binom dr^2r!/2\) and \(p_r\sim (nd)^{-r}\). The rational factor in the covariance is asymptotic to \(-r(d-r)/(dn)\) for \(r<d\), and to \((d-1)/(dn^2)\) for \(r=d\). This proves both rates.

## Verification

The accompanying `verify.py` can be run with Python 3 and the standard library. It directly enumerates every matching for the listed cases with at most twelve half-edges and compares exact rational covariances for every \(2\le r\le d\). It checks additional signs for admissible \(2\le n<50\), \(2\le d<15\), and exercises the excluded two-vertex saturated case. These checks corroborate the proof but do not replace it.

## Relationship to prior work

Angel, van der Hofstad, and Holmgren [1] study loops and the pair statistic \(P_2\), with Poisson approximations. Janson [2] uses factorial moments for loop and parallel-pair counts, and [3] records exact probabilities of prescribed disjoint pairs. The Poisson-scale statements do not give the finite corrections here. More directly, [4] gives an exact all-degree-sequence covariance for \(L\) and \(P_2\), including its regular degree sign classification; specializing to a regular sequence gives exactly the \(r=2\) slice above. The distinct same-date record [5] also treats that pair statistic, with no claim here about within-day order. Neither pair-statistic identity determines the joint moments for \(r\ge3\). The contribution is the finite higher-bundle covariance and the saturation threshold and rate for those bundles, derived using the standard prescribed-pair probabilities.

## Limitations

The formula concerns uniform half-edge pairings under a regular degree sequence. It does not assert a sign threshold for irregular degree sequences or for a different sampling law. A covariance sign alone does not prove independence, association, or a stochastic ordering. The inspected prior sources do not establish historical priority beyond their stated results.

## References

1. O. Angel, R. van der Hofstad, and C. Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172, equations (1.2), (1.6), and §3.
2. S. Janson, *The probability that a random multigraph is simple*, arXiv:math/0609802, §7, particularly Theorem 7.1 and Remark 7.2.
3. S. Janson, *Random graphs with given vertex degrees and switchings*, arXiv:1901.09744, equation (5.8).
4. *A sharp degree-two covariance reversal for loop and parallel-pair counts*, Resultary record `2026/10/18/SCOPE-a-sharp-degree-two-covariance-reversal-for-loop-and-parallel-pai--3cf215ef6662`.
5. *A finite-size sign reversal between loops and parallel-edge pairs*, Resultary record `2026/10/26/SCOPE-a-finite-size-sign-reversal-between-loops-and-parallel-edge-pair--8bb0aaf4e210`.
