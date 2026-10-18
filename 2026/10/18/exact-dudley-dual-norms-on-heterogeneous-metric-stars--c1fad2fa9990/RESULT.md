# Exact Dudley dual norms on heterogeneous metric stars

## Finding

Let \(S=\{o,v_1,\ldots,v_m\}\) be a finite real metric star, with \(m\ge1\), positive arm lengths \(\rho_i>0\), and distances \(d(o,v_i)=\rho_i\), \(d(v_i,v_j)=\rho_i+\rho_j\) for distinct leaves. For an arbitrary signed atomic measure
\[
\mu=\mu_0\delta_o+\sum_{i=1}^m\mu_i\delta_{v_i},\qquad M=\mu_0+\sum_{i=1}^m\mu_i,
\]
set \(I_+=\{i:\mu_i>0\}\) and \(I_-=\{i:\mu_i<0\}\), and put
\[
P(x)=\sum_{i\in I_+}\mu_i\min\{x,\rho_i\},\qquad
Q(y)=\sum_{i\in I_-}(-\mu_i)\min\{y,\rho_i\}.
\]
Define the two finite knot sets \(X=\{0\}\cup\{\rho_i:i\in I_+\}\) and \(Y=\{0\}\cup\{\rho_i:i\in I_-\}\). For the **sum-normalized** real bounded-Lipschitz norm \(\|f\|_{\mathrm{BL}}=\|f\|_\infty+\operatorname{Lip}(f)\), its signed-measure dual norm is exactly
\[
\boxed{\quad \|\mu\|_{\mathrm{BL}}^*=
\max\left\{|M|,\ \max_{x\in X,\,y\in Y}
\frac{M(y-x)+2P(x)+2Q(y)}{2+x+y}\right\}.\quad}
\]
Thus there are at most \(1+(|I_+|+1)(|I_-|+1)\) explicitly computable candidates, all involving only input arm lengths and signed masses. Every maximum is attained by an explicitly described function, including for measures with nonzero total mass. In addition, the norm can be computed **exactly in \(O(m\log m)\) real arithmetic operations and comparisons**, after sorting the positive and negative arm-length groups, by a one-dimensional piecewise-affine root calculation. Rational input gives a rational norm and rational attaining function.

## Assumptions and scope

There are finitely many *vertices*, not a continuum of points along each arm. The metric is the shortest-path metric restricted to this finite vertex set. Measures, potential values, and dual pairings are real, with **no total-mass-zero assumption**. Arms may have equal or unequal positive lengths; signed coefficients can vanish. The norm is a **sum**, not the maximum-normalized Fortet–Mourier norm. Computation costs count arithmetic operations and comparisons on exact real numbers, not bit-level complexity for arbitrary-length integer representations. Constants \(f\equiv\pm1\) have norm one, so \(\|\mu\|_{\mathrm{BL}}^*\ge|M|\).

## Proof

**1. Reduction to two cap variables.** For any \(f\) in the unit ball choose \(t\ge\operatorname{Lip}(f)\) and \(b\ge\|f\|_\infty\) with \(t,b\ge0\) and \(t+b=1\), and put \(c=f(o)\). The star metric makes the complete Lipschitz constraints equivalent to \(|f(v_i)-c|\le\rho_i t\) for every leaf: the leaf-to-leaf bounds then follow by the triangle inequality. Thus \(-b\le c\le b\), and each leaf lies in the independent interval
\[
[-b,b]\cap[c-\rho_i t,c+\rho_i t].
\]
For fixed \(t,b,c\), a maximizing leaf takes the largest allowable value if \(\mu_i>0\), the smallest if \(\mu_i<0\), and any allowable value otherwise. Consequently an optimal leaf is
\[
f(v_i)=\begin{cases}\min\{b,c+\rho_i t\},&\mu_i>0,\\
\max\{-b,c-\rho_i t\},&\mu_i<0,\\ c,&\mu_i=0.\end{cases}
\]
The case \(t=0\) forces every value to equal \(c\), where \(|c|\le1\), and gives optimum \(|M|\). For \(t>0\), set \(x=(b-c)/t\) and \(y=(b+c)/t\). Then \(x,y\ge0\) and
\[
t=\frac2{2+x+y},\qquad b=\frac{x+y}{2+x+y},\qquad c=\frac{y-x}{2+x+y}.
\]
Conversely every finite nonnegative pair \((x,y)\) gives a feasible triple and leaf potentials with norm at most one. The objective becomes exactly
\[
F(x,y)=\frac{M(y-x)+2P(x)+2Q(y)}{2+x+y}.
\]
Therefore \(\|\mu\|_{\mathrm{BL}}^*=\max\{|M|,\sup_{x,y\ge0}F(x,y)\}\).

**2. Finite-knot reduction.** On any interval between consecutive radii of positive-mass leaves, \(P(x)\) is affine. With \(y\) fixed, \(F(x,y)\) is a ratio of affine functions of \(x\), hence monotone or constant on that interval. It attains a maximum at an endpoint. Beyond the largest positive-leaf radius, \(P\) is constant, and the same argument puts the maximum at that last knot or at the limit \(-M\), which is already covered by \(|M|\). If \(I_+\) is empty the same argument applies starting at zero. Thus, up to an asymptotic value no larger than \(|M|\), \(x\) can be restricted to \(X\). Next, with \(x\) fixed at any such knot, the analogous argument for \(Q\) restricts \(y\) to \(Y\), with possible tail limit \(M\) again bounded by \(|M|\). This proves the stated finite maximum without an enumeration of the full ball's vertices. Finite candidates yield explicit attaining potentials by Step 1. When the maximizing branch is \(|M|\), the constant \(\operatorname{sgn}(M)\) attains it (and for \(M=0\), the zero potential suffices).

**3. An exact near-linear algorithm.** For \(r\ge|M|\) define
\[
\Phi_+(r)=\max_{x\ge0}\big\{2P(x)-(M+r)x\big\},\quad
\Phi_-(r)=\max_{y\ge0}\big\{2Q(y)-(r-M)y\big\},
\]
\[
G(r)=\Phi_+(r)+\Phi_-(r)-2r.
\]
By rearranging the inequality \(F(x,y)\le r\), one has
\[
\boxed{\quad r\ge\|\mu\|_{\mathrm{BL}}^*\ \Longleftrightarrow\
\ r\ge|M|\ \text{and}\ G(r)\le0.\quad}
\]
Because \(M+r\ge0\) and \(r-M\ge0\), both maxima in \(\Phi_\pm\) occur at zero or at the corresponding finite radii. The maxima are nonincreasing in \(r\), so \(G\) is continuous and strictly decreasing, with decrease at least \(2\) per unit increment. If \(G(|M|)\le0\), the answer is \(|M|\). Otherwise its unique zero in \((|M|,T]\), where \(T=\sum_{i=0}^m|\mu_i|\), is the dual norm; this interval contains a zero because the norm does not exceed total variation.

Sort and aggregate the positive-mass radii and, separately, the negative-mass radii. Each \(P\) and \(Q\) is increasing, concave, and affine between consecutive knots; on any such interval its slope is the total signed *positive weight* in arms whose radius is above the interval. Hence each \(\Phi\) is evaluable with a binary search in the decreasing list of tail masses, followed by one prefix-sum lookup. The only possible slope switches of \(G(r)\) occur at numbers
\[
r=2\,\bigl(\text{positive-mass tail sum}\bigr)-M
\quad\text{or}\quad
r=2\,\bigl(\text{negative-mass tail sum}\bigr)+M.
\]
There are at most \(2m\) such values. Sort those lying strictly inside \((|M|,T)\), append endpoints, and binary-search consecutive switch values that bracket the sign change. Since \(G\) is affine between switch values, one exact linear interpolation gives the root. Sorting takes \(O(m\log m)\) operations; the remaining binary searches and evaluations take \(O(\log^2m)\) operations, so the claimed overall bound follows. This procedure handles repeated radii and zero masses by aggregating equal knots and discarding zero groups. Its exact-rational implementation appears in `CHECK.py`.

## Verification

The two-dimensional reduction and piecewise-affine root argument prove the theorem for all finite positive arm lengths and real signed masses. The standalone exact-rational checker `CHECK.py` generated and passed 4,800 deterministic random cases plus 1,200 constructive attaining-potential checks, including repeated radii, vanishing coefficients, and both zero and nonzero total mass. In each case it compared the sorting/root computation with the independently implemented two-dimensional finite-knot maximum using Python rational fractions. The complementary `LP_CROSSCHECK.py` directly formulates the primal bounded-Lipschitz linear program, without using either the knot or root reductions. With SciPy's HiGHS solver installed it passed 2,100 deterministic primal-LP comparisons on sizes one through seven, with separate zero-total-mass cases; 1,050 further exact special-case checks passed. Numerical LP agreement is corroboration, not a proof of the stated all-size theorem. For example, with three leaves, \((\rho_1,\rho_2,\rho_3)=(1,4,2)\) and coefficients \((\mu_0,\mu_1,\mu_2,\mu_3)=(0,2,-3,1)\), the formula gives exactly \(30/7\). For a nonzero-total-mass example, radii \((1/2,3,5)\) and coefficients \((1,1,-2,2)\) give exactly \(40/11\), strictly greater than the total mass \(2\).

## Relationship to prior work

Hille and Theewis, arXiv:2206.12234, Section 6, Lemma 6.1 and equation (39), give a finite-dimensional linear-programming representation for Dudley norms on *arbitrary* finite metrics. This certainly computes each special case indirectly, but it does not contain the present heterogeneous-star finite-knot identity, its two independent mass-cap reductions, or the near-linear exact sorting/root algorithm. Their arXiv:2305.08500 studies norming and extreme functions for general bounded-Lipschitz balls; its theorems do not provide this exact support formula. The published result *Exact Dudley norms and mass-imbalance thresholds on equiradial stars* determines a sharper two-branch specialization when **all arms are equal and the measure has zero total mass**; that restricted regime is explicitly prior art rather than a novelty claim. Earlier calculations for the maximum-normalized Fortet–Mourier norm are for a different Banach norm and need not determine the sum-normalized answer. The new assertion is a closed form with an exact near-linear evaluation algorithm for *arbitrarily heterogeneous* positive arm lengths and all signed masses, not a claim that computing a general finite linear program is novel.

## Limitations

This is a real finite-vertex result: it does not classify arbitrary metric trees, infinitely many arms, measures supported in edge interiors, complex-valued test functions, or bit complexity. No assertion is made that general bounded-Lipschitz dual optimization lacked earlier algorithms. Bibliographic searches and full-text comparisons cannot eliminate an unindexed equivalent formula or a stronger independently derived sorting method. The algorithm is exact in an arithmetic/comparison model; finite tests alone cannot establish its universal correctness.

## References

1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1 (first public 15 May 2023), Sections 1, 5, 6, https://arxiv.org/abs/2305.08500.
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234v2 (originally public 24 June 2022), especially Section 6, https://arxiv.org/abs/2206.12234.
3. *Exact Dudley norms and mass-imbalance thresholds on equiradial stars*, published published-finding corpus record 2026/10/11/SCOPE-exact-dudley-norms-and-mass-imbalance-thresholds-on-equiradial-s--ecc3b6450a54, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-dudley-norms-and-mass-imbalance-thresholds-on-equiradial-s--ecc3b6450a54.
4. B. K. Sriperumbudur, K. Fukumizu, A. Gretton, B. Schölkopf, and G. R. G. Lanckriet, *On the empirical estimation of integral probability metrics*, Electronic Journal of Statistics 6 (2012), 1550–1599, DOI:10.1214/12-EJS722 (general empirical linear-programming background; full text not independently inspected).
