# Global inverse reconstruction of metric stars from one geodesic-distance law

## Finding

Let \(T\) be a finite geodesic star with \(k\geq3\) arms having lengths \(a_1,\ldots,a_k>0\). Equip it with normalized one-dimensional length measure. If \(X,Y\) are independent samples, the *single scalar law* of \(D=d_T(X,Y)\) uniquely determines the isometry class of \(T\), for every positive arm-length vector including arbitrary ties and additive coincidences.

Write \(L=\sum_{i=1}^k a_i\), \(F(r)=\Pr(D\leq r)\), and let \(f\) be the continuous piecewise-linear density on nonnegative radii. Then

\[
L=\frac{2}{f(0+)},\qquad k(k-3)=L^2 f'(0+).
\]

The signed atomic measure given by the *distributional second derivative* of \(f\) is

\[
\nu=L^2f''=(4-2k)\sum_{i=1}^k\delta_{a_i}+2\sum_{1\leq i<j\leq k}\delta_{a_i+a_j}.
\]

The multiset of arm lengths is uniquely and constructively recoverable from \(\nu\), even when negative individual-arm atoms coincide with positive two-arm sum atoms and cancel or reverse sign.

## Assumptions and scope

The underlying object is a compact geodesic tree with exactly one vertex of degree \(k\geq3\), with \(k\) edges identified at their common center and strictly positive finite intrinsic lengths. Edge subdivisions at degree-two points are immaterial. Sample points independently from normalized arclength, so that the probability of choosing an arm is its length divided by \(L\). Distance is intrinsic shortest-path distance, not Euclidean distance in an embedding. Repeated arm lengths and exact relations such as \(a_i+a_j=a_h\) are admitted. Probability and derivatives refer to the exact distribution, not a finite sample or binned histogram. No assertion is made for arbitrary branched trees with multiple junctions, other sampling measures, or noisy data.

## Proof

For fixed \(r\geq0\), let \(t_+=\max(t,0)\). If both points lie on the same arm of length \(a_i\), their distance is the absolute difference of their arm coordinates. Its unnormalized density contribution is \(2(a_i-r)_+\). If points are on distinct arms \(i\) and \(j\), their distance equals the sum of the two nonnegative arm coordinates. Accounting for both orderings of the arms, the unnormalized density contribution is

\[
2\Big[r_+-(r-a_i)_+-(r-a_j)_++(r-a_i-a_j)_+\Big].
\]

Thus for \(r\geq0\) the exact density is

\[
L^2 f(r)=2\sum_{i=1}^k(a_i-r)_+
+2\sum_{1\leq i<j\leq k}\big[r_+-(r-a_i)_+-(r-a_j)_++(r-a_i-a_j)_+\big].
\tag{1}
\]

Every term is continuous and piecewise linear. On \(0<r<\min_i a_i\), the right side equals \(2L+k(k-3)r\). Hence \(f(0+)=2/L\) and \(L^2f'(0+)=k(k-3)\). As \(k\mapsto k(k-3)\) is strictly increasing on the integers \(k\geq3\), these observations uniquely recover \(L\) and \(k\).

The derivative of \((r-a)_+\) is a step function and its distributional second derivative on positive radii is \(\delta_a\). Differentiating (1) twice on the open half-line gives

\[
L^2f''=2\sum_i\delta_{a_i}-2(k-1)\sum_i\delta_{a_i}+2\sum_{i<j}\delta_{a_i+a_j}
=(4-2k)\sum_i\delta_{a_i}+2\sum_{i<j}\delta_{a_i+a_j}.
\tag{2}
\]

Here is an explicit inverse procedure. Start with the signed atomic measure \(\nu\) in (2) and an empty list \(B\) of recovered arms. At each stage, subtract from the current residual all *known* atomic effects contributed by lengths already recorded in \(B\) and their pairwise sums; equivalently, after recovering a new block, remove that block's negative single-arm impulses and all positive pair-sum impulses internal to that block or involving the previously recovered arms. Denote the resulting residual by \(\nu_B\). It contains precisely the negative single-arm impulses of not-yet-recovered arms and the positive pair-sum impulses having at least one not-yet-recovered arm.

If there is an unrecovered arm, let \(t>0\) be its smallest length and let \(m\geq1\) be the multiplicity of \(t\) among the unrecovered lengths. Every positive pair-sum impulse still present in \(\nu_B\) has location *strictly greater than* \(t\), since it contains an unrecovered length at least \(t\) and another strictly positive arm length. The smallest support point of \(\nu_B\) is therefore exactly \(t\), with signed mass \((4-2k)m<0\). Recover both \(t\) and \(m\). Remove \(m(4-2k)\delta_t\), remove \(2m\delta_{t+b}\) for each previous recorded arm \(b\in B\) counted with multiplicity, and remove \(m(m-1)\delta_{2t}\) for the \(\binom{m}{2}\) internal pairs. Add \(m\) copies of \(t\) to \(B\) and repeat. Induction shows the maintained residual invariant and recovers all \(k\) lengths in finitely many stages. Afterward the residual is zero. All decisions depend only on \(F\), proving unique reconstruction and the theorem.

A collision illustrates why reading off the negative atoms of the *original* measure is not enough: for nine arms of length \(1\) and one of length \(2\), the original signed mass at radius \(2\) is \(56>0\), despite the presence of an actual arm of length \(2\). After recovering and removing the nine shorter arms and their pairwise sums, the radius-\(2\) residual mass becomes negative and recovers the tenth arm.

## Verification

The standalone file `check_star.py` uses exact rational arithmetic to compute (1), the atomic measure (2), and the reconstruction algorithm. It checked \(368\) positive rational star configurations with \(3\leq k\leq14\), including repeated lengths and additive-collision cases. Each check verified exact recovery, exact density normalization, and the two small-radius coefficients. Four additional \(100\,000\)-pair simulations independently checked the predicted cumulative distribution against sampled geodesic distances, with maximum absolute discrepancies below \(0.004\). To reproduce, run `python check_star.py` with the Python standard library; no external data or software dependency is needed. Rational checks are finite consistency tests; the all-length theorem follows from the preceding proof, not from those checks.

## Relationship to prior work

Dey, Shi and Wang (2015, arXiv:1503.07414) study continuous metric graphs using *persistence-distortion* comparisons; that construction is a distinct invariant, not an inversion of the unconditioned distance histogram. Wei, Walteros and Batta (2019, DOI:10.1002/net.21919) provide general formulas for random-event distance distributions when a network and its edge lengths are supplied. Their work covers the *forward* computation and is not claimed as new here. Mémoli and Needham (arXiv:1810.09646, subsequently published as DOI:10.1111/sapm.12526) directly address inverse distance distributions and report a local-injectivity theorem for metric graphs. The present claim is the explicit *global, all-positive-arm-length* uniqueness and signed-atom peeling reconstruction for the one-junction star class, including ties and additive collisions. The full text of the last comparison source was not accessible in this assessment; its potential to contain an overlapping special theorem is a genuine residual bibliographic risk.

## Limitations

The reconstruction uses exact derivatives and exact atomic locations; it does not establish stability under noise, binning, or finite sampling. It is restricted to finite positive-length stars, not arbitrary metric graphs or multi-junction trees. No general graph-reconstruction theorem or general lower bound on sample complexity is asserted. The forward law is known in a more general setting; the claim of contribution is the all-parameters inverse theorem. Independent scholarly validation and an exhaustive historical-literature review have not been performed.

## References

1. T. K. Dey, D. Shi and Y. Wang, *Comparing Graphs via Persistence Distortion*, first public arXiv version 2015-03-25, arXiv:1503.07414; SoCG 2015, DOI:10.4230/LIPIcs.SOCG.2015.491.
2. N. Wei, J. L. Walteros and R. Batta, *On the Distance Between Random Events on a Network*, *Networks* 75 (2020), 203–231, first published 2019-11-27, DOI:10.1002/net.21919.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, first public arXiv version 2018-10-23, arXiv:1810.09646; *Studies in Applied Mathematics* 149 (2022), 943–1001, DOI:10.1111/sapm.12526.
