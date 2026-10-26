# Saturated parallel-edge bundles reverse loop covariance in regular configuration graphs

## Finding

Let integers \(n\geq 3\) and \(d\geq 2\) satisfy \(nd\) even. Form the \(d\)-regular configuration-model multigraph by uniformly pairing the \(nd\) distinguishable half-edges, grouped into \(n\) labeled vertices with \(d\) half-edges each. Write \(L\) for its total number of loops; a loop consumes two half-edges at one vertex. Let \(M_{uv}\) be the number of non-loop edges between distinct vertices \(u,v\). For every integer \(2\leq r\leq d\), put
\[
P_r=\sum_{1\leq u<v\leq n}\binom{M_{uv}}r.
\]
Thus \(P_r\) counts unordered bundles of \(r\) parallel edges, with multiplicity if more than \(r\) edges connect the same pair. Define
\[
p_r=\prod_{j=0}^{r-1}\frac{1}{nd-(2j+1)},\qquad B_r=\binom n2\binom dr^2r!.
\]
Then, **for every permitted \(n,d,r\)**,
\[
\boxed{\operatorname{Cov}(L,P_r)
= B_rp_r\,\frac{r\{2d-r-1-nd(d-r)\}}{(nd-1)(nd-2r-1)}.}
\]
Consequently \(\operatorname{Cov}(L,P_r)<0\) for every \(2\leq r<d\), but \(\operatorname{Cov}(L,P_d)>0\). In particular, for \(d=2\) the ordinary double-edge count has positive covariance with loops, whereas for every \(d\geq3\) it has negative covariance. The sign switch occurs **exactly at saturation** of the two endpoint degrees, for all admissible \(n,d\), not merely in a large-graph limit.

At fixed \(d\), along admissible \(n\to\infty\), the exact rates are
\[
\operatorname{Cov}(L,P_r)
\sim -\frac{r(d-r)\binom dr^2r!}{2d^{r+1}}\,n^{1-r}
\quad(2\le r<d),
\]
\[
\operatorname{Cov}(L,P_d)
\sim \frac{d!(d-1)}{2d^{d+1}}\,n^{-d}.
\]
The positive covariance is a much smaller finite-size correction than the negative unsaturated terms.

## Assumptions and scope

All underlying half-edge pairings have equal probability. The generated multigraph is not uniform over vertex-labeled multigraphs with the same degree sequence. Loops are counted as single edges and have degree contribution two; \(P_r\) counts \(r\)-subsets of parallel non-loop edges, not just pairs of vertices having at least \(r\) edges. The hypotheses \(n\ge3\), \(d\ge2\), \(nd\) even, and \(2\le r\le d\) are essential to the displayed theorem; the factor \(nd-2r-1\) is then positive. In the excluded two-vertex saturated case \(n=2,r=d\), the events \(L>0\) and \(P_d>0\) are incompatible, and their covariance is strictly negative.

## Proof

A specified collection of \(r\) disjoint matched half-edge pairs appears with probability \(p_r\): reveal its pairs sequentially, and note that after \(j\) pairs there are \(nd-2j-1\) possible partners for the next exposed half-edge. For a fixed unordered pair of vertices, the number of elementary \(r\)-bundle events is \(\binom dr^2r!\), because one chooses \(r\) half-edges from each endpoint and a bijection. Summing indicators yields
\[
\mathbb E P_r=B_rp_r>0.
\]
Similarly, \(\mathbb E L=n\binom d2/(nd-1)\).

Condition on any elementary \(r\)-bundle event. Exactly \(r\) half-edges at each of its two endpoints are already paired across, and all remaining \(nd-2r\) half-edges are still paired uniformly. The number of eligible same-vertex half-edge pairs among them is
\[
(n-2)\binom d2+2\binom{d-r}2
=n\binom d2-r(2d-r-1).
\]
Every eligible pair is joined with probability \(1/(nd-2r-1)\). Hence the conditional expected number of loops is the same for every elementary bundle event, and indicator summation gives the exact size-biased identity
\[
\frac{\mathbb E[LP_r]}{\mathbb E P_r}
=\frac{n\binom d2-r(2d-r-1)}{nd-2r-1}.
\]
Subtracting \(\mathbb E L\) and simplifying,
\[
\frac{\operatorname{Cov}(L,P_r)}{\mathbb E P_r}
=\frac{r[2d-r-1-nd(d-r)]}{(nd-1)(nd-2r-1)}.
\]
This proves the formula without an approximation.

If \(r=d\), the numerator bracket equals \(d-1>0\). If \(r\le d-1\), then \(d-r\ge1\) and \(nd(d-r)\ge3d>2d-r-1\), making it strictly negative. All other factors are positive. Finally, for fixed \(d,r\), use \(B_r\sim n^2\binom dr^2r!/2\), \(p_r\sim (nd)^{-r}\), and expand the final rational factor. For \(r<d\) its leading term is \(-r(d-r)/(dn)\); for \(r=d\), it is \((d-1)/(dn^2)\). These yield the two asymptotic constants.

## Verification

The accompanying `verify.py` enumerates every pairing for \((n,d)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,4),(4,2),(4,3),(5,2),(6,2)\), checks the exact covariance for every \(2\leq r\leq d\), and tests the predicted sign across all admissible \(2\leq n<50\), \(2\leq d<15\). It uses rational arithmetic throughout and reports `VERIFY_OK`. The two-vertex cases are boundary checks, not part of the claimed theorem. The proof above covers all admissible parameters; enumeration does not replace that proof.

## Relationship to prior work

The configuration model and the pairing probability for prescribed disjoint edges are standard. Angel, van der Hofstad, and Holmgren (2016), particularly their equations (1.2), (1.6), and (3.1), study loop counts and the double-edge pair statistic, with asymptotic independent-Poisson limits; these are credited rather than claimed here. Janson (2019), Sections 3–5 (especially (5.8)), analyzes configuration-model multigraphs and multiple-edge defects using exact prescribed-pair probabilities and switchings. The present statement isolates the **entire multiplicity-indexed mixed covariance spectrum** for regular degrees, including the finite-order reversal at \(r=d\), plus its different orders of decay. These claims are not stated in the inspected portions of those papers. Chodrow (2019) studies a different, uniformly weighted multigraph model and an expected adjacency matrix; its sampling law must not be conflated with uniform pairing.

## Limitations

This result concerns the regular stub-pairing configuration model, not an arbitrary prescribed degree sequence, a simple graph conditioned on no loops, or a uniformly weighted vertex-labeled multigraph. Its sign result does not imply association or independence of the random variables. The multiplicity-saturated positive effect is of order \(n^{-d}\), so it is invisible to leading Poisson approximations. A broad historical literature exists on factorial moments of random pairings; while the inspected sources do not state the exact all-\(r\) covariance sign transition, historical priority cannot be certified by a finite literature search. No independent mathematical audit is claimed.

## References

1. S. Janson, *Random graphs with given vertex degrees and switchings*, arXiv:1901.09744 (first public version 2019-01-28), especially Sections 3–5 and equation (5.8). https://arxiv.org/abs/1901.09744
2. O. Angel, R. van der Hofstad, and C. Holmgren, *Limit laws for self-loops and multiple edges in the configuration model*, arXiv:1603.07172 (first public version 2016-03-23), especially equations (1.2), (1.6), and (3.1). https://arxiv.org/abs/1603.07172
3. P. S. Chodrow, *Moments of Uniform Random Multigraphs with Fixed Degree Sequences*, arXiv:1909.09037 (first public version 2019-09-19). https://arxiv.org/abs/1909.09037
