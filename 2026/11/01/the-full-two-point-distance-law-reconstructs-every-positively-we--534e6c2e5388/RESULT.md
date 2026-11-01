# The full two-point distance law reconstructs every positively weighted metric star

## Finding
Let \(k\ge3\), let \(a_1,\ldots,a_k>0\), and form the intrinsic metric star by identifying the zero endpoints of intervals of these lengths. Write \(L=\sum_i a_i\). Choose two points independently from the normalized arclength measure and let \(D\) denote their shortest-path distance. **The probability law of \(D\), without any arm labels or knowledge of \(k\) or \(L\), uniquely determines \(k\), \(L\), and the complete multiset \(\{a_1,\ldots,a_k\}\), including all multiplicities.** Consequently it determines the metric star up to isometry.

The distribution has a continuous piecewise-linear density, with \(t_+=\max\{t,0\}\) and \(t\ge0\),
\[
f(t)=\frac2L+\frac{k(k-3)}{L^2}t-\frac{2(k-2)}{L^2}\sum_{i=1}^k(t-a_i)_++\frac2{L^2}\sum_{i<j}(t-a_i-a_j)_+.
\]
The density is zero past the diameter \(\max_{i<j}(a_i+a_j)\). The reconstruction is constructive even when a single-arm breakpoint is canceled by a sum of two other arm lengths.

The degree threshold is sharp: a star with only one or two arms is isometric to an interval. All positive splits of the same total interval length have the identical two-point distance distribution.

## Assumptions and scope
An arm is a copy of \([0,a_i]\), with zero identified across arms; degree-two subdivision vertices are not additional arms. Points are sampled with density \(1/L\) against total intrinsic one-dimensional arclength, independently. The term \(\delta_x\) is a unit point mass at \(x\); derivatives of piecewise-linear functions are interpreted distributionally on \((0,\infty)\). The theorem is exact for every finite integer \(k\ge3\), every positive real length vector (including repeated or incommensurable lengths), and the complete population law. It makes no claim about uniqueness among arbitrary nonstar graphs or reconstruction from finitely many noisy observations.

## Proof
**1. Exact conditional distance density.** Both points on the same arm of length \(a_i\) contribute \(2(a_i-t)_+/L^2\) to the unconditional density, using the two orders of point coordinates. Points on distinct arms \(i,j\) have distance equal to the sum of their positive radial coordinates. Integrating along the line \(x+y=t\) in \([0,a_i]\times[0,a_j]\) and taking both ordered arm assignments gives
\[
\frac2{L^2}\left[t_+-(t-a_i)_+-(t-a_j)_++(t-a_i-a_j)_+\right].
\]
Summing the same-arm and cross-arm terms gives the density and, on using \((a-t)_+=a-t+(t-a)_+\), yields the displayed spline formula. The conditional components integrate to their sampling probabilities, so \(f\) integrates to one. In particular, \(f\) is continuous and vanishes beyond the diameter.

**2. Recover total length and number of arms.** Since all \(a_i\) are strictly positive, there is an interval \(0<t<\min_i a_i\) on which all positive-part terms vanish. Therefore
\[
f(0+)=\frac2L,\qquad f'(0+)=\frac{k(k-3)}{L^2}.
\]
Thus \(L=2/f(0+)\). Among integers \(k\ge3\), the map \(k\mapsto k(k-3)\) is strictly increasing (its values start \(0,4,10,18,\ldots\)), so \(k\) is uniquely recovered from \(L^2 f'(0+)\). This also separates stars with degree at least three from intervals, whose initial derivative is negative.

**3. Signed atomic curvature.** On the open half-line \((0,\infty)\), the second distributional derivative satisfies
\[
\mu:=L^2 f''=-2(k-2)\sum_i\delta_{a_i}+2\sum_{i<j}\delta_{a_i+a_j}.
\]
All coefficients are exact, and atoms may cancel. Observe that only the arm multiset, not an ordering, enters \(\mu\).

**4. Complete inversion with canceled atoms.** Maintain a recovered submultiset \(B\) of arm lengths, initially empty. From \(\mu\), subtract its known contributions: the negative singleton atoms for each arm in \(B\) and the positive pair-sum atoms for all unordered *distinct indexed arms* both in \(B\). Call the resulting signed atomic measure \(\mu_B\). If arms remain unrecovered, let \(a\) be their smallest length and let \(m\) be its multiplicity among the unrecovered arms. Every positive pair-sum atom still present in \(\mu_B\) involves at least one unrecovered arm and lies strictly above \(a\), because every other length is positive. Every unrecovered negative singleton atom lies at or above \(a\). Thus the **smallest nonzero atom of \(\mu_B\)** occurs at \(a\), with mass precisely \(-2(k-2)m\). Read \(a,m\), append \(m\) copies of \(a\) to \(B\), subtract their singleton and newly known pair contributions, and repeat. After finitely many steps exactly \(k\) arm lengths are recovered. This procedure works even when some original atom of \(\mu\) vanished through cancellations, because the canceled known contributions are removed before the next step.

If two positive-length star models have the same distance law, steps 2--4 recover the same \(k\), \(L\), and multiset of lengths from that law. Their intrinsic metric stars are therefore isometric, proving the claim.

**5. The sharp exception.** For one or two positive arms the underlying metric graph is an interval of length \(L\). The distance between two independent arclength-uniform points then has density \(2(L-t)_+/L^2\), independent of how an interval is split into two arms. This proves that the branching assumption is necessary for recovery of a distinguished arm list.

## Verification
The standalone `verify.py` independently evaluates the density in two algebraically distinct ways: by direct same-arm and pairwise-convolution integrations, and by the simplified spline. It compares the resulting exact rational values across \(k=3,\ldots,10\), random positive rational lengths, and test distances; it independently forms the signed atomic measure and performs the multiplicity-aware inversion. It also checks exact normalization for selected cases, the interval exception, and the nontrivial cancellation \((1,2,3)\) at \(t=3\). Run `python3 verify.py` using Python 3 standard library. The completed run returned `VERIFY_OK 77483 exact independent density identities, inverse reconstructions and normalization checks`. The finite tests are corroboration only; the proof above establishes the universal statement.

## Relationship to prior work
Wei, Walteros and Batta derive general forward probability distributions for distances between random events on **arbitrary weighted networks**. Consequently, the forward distance-density calculation, even with this particularly simple spline specialization, is **not claimed as new**. The distinct finding is the inverse statement: the unlabeled two-point distribution uniquely determines every positive arm length, including under exact cancellation, by an explicit signed-curvature peeling argument. Their published full manuscript describes a forward computational framework (Theorems 4 and 5 already give general densities and piecewise linearity), not an inverse identifiability theorem for unknown star metrics.

Dover and Özaydın study homeomorphism and homotopy types of configurations of separated points on metric graphs; Li and Özaydın later develop persistent homological models of restricted two-point configurations on metric stars. Such filtered homotopy/persistence data may determine arm lengths, but it is a different, richer invariant than the single **probability measure** of distance; no inference from their topological results to two-point-distance-law reconstruction is presumed. Garijo, Márquez and Silveira and Baptista, Kennedy and Mugnolo study **mean** distances on weighted metric graphs. Their mean results do not determine the full law or the individual lengths. In particular, the earlier mean/variance classifications for weighted stars do not supply the present full inverse law.

## Limitations
The theorem assumes the number of positive arms is finite and at least three, independent and normalized-arclength-uniform sampling, and exact knowledge of the entire distance distribution. Reconstruction can be poorly conditioned near canceling breakpoints or nearly coincident arm lengths; no stability rate or finite-sample statistical guarantee is proved. The general forward density formula is prior work, and existence of an earlier unindexed inverse characterization cannot be excluded solely from literature searches. Independent validation has not been performed.

## References
1. J. Dover and M. Özaydın, *Homeomorphism and Homotopy Types of Restricted Configuration Spaces of Metric Graphs*, arXiv:1301.5693 (first posted 2013-01-24), https://arxiv.org/abs/1301.5693.
2. N. Wei, J. L. Walteros, and R. Batta, *On the Distance Between Random Events on a Network*, *Networks* 75 (2020), 203–231 (first publicly published 2019-11-27), https://doi.org/10.1002/net.21919; especially §§3, 5, 8, 12.
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, *Results in Mathematics* 78 (2023), 139, https://doi.org/10.1007/s00025-023-01902-w.
4. L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean Distance on Metric Graphs*, *Journal of Geometric Analysis* 34 (2024), 137, https://doi.org/10.1007/s12220-024-01574-0.
5. W. Li and M. Özaydın, *Persistent Combinatorial Model of the Restricted Second Configuration Space of Metric Star Graphs*, arXiv:2603.00914v1 (first publicly posted 2026-03-01), https://arxiv.org/html/2603.00914v1.
