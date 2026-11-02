# Sharp weighted-variation stability of isotonic regression on rooted stars

## Finding
Let \(m\ge1\) be an integer. For strictly positive observation masses \(a_0,a_1,\ldots,a_m\), consider weighted least-squares regression onto the rooted-star order constraints \(z_0\le z_i\) for \(1\le i\le m\):
\[
P_a(y)=\operatorname*{argmin}_{z_0\le z_i\ (1\le i\le m)}\sum_{i=0}^{m}a_i(z_i-y_i)^2.
\]
For arbitrary strictly positive variation weights \(w_1,\ldots,w_m\), write \(W=\sum_{i=1}^{m}w_i\) and \(V_w(y)=\sum_{i=1}^{m}w_i|y_i-y_0|\). The exact global two-data constant is
\[
\boxed{\sup_{V_w(y-y')>0}\frac{V_w(P_a(y)-P_a(y'))}{V_w(y-y')}=K(a,w):=\max\left\{1,\max_{1\le i\le m}\frac{a_i(W-w_i)}{(a_0+a_i)w_i}\right\}.}
\]
The supremum is a maximum, realized by finite real input pairs. In particular, regression is nonexpansive in weighted edge variation exactly when \(a_i(W-w_i)\le(a_0+a_i)w_i\) for every leaf \(i\).

With all masses and weights equal to \(1\), the constant is \(\max\{1,(m-1)/2\}\). The first strict amplification occurs at four leaves. When the variation weights equal their corresponding leaf observation masses, \(w_i=a_i\), contraction is equivalent to \(\sum_{j=1}^{m}a_j\le a_0+2\min_{1\le i\le m}a_i\).

## Assumptions and scope
All inputs \(y,y'\) are arbitrary real vectors indexed by the root \(0\) and \(m\) incomparable leaves \(1,\ldots,m\); observation masses and variation weights are strictly positive. This is the rooted-star partial order, not the total order on the same number of vertices. The projection exists and is unique because its objective is strictly convex. Graph total variation is a seminorm with constants as kernel. Translation equivariance of the regression, \(P_a(y+c\mathbf1)=P_a(y)+c\mathbf1\), makes its two-data variation Lipschitz constant well-defined on the quotient by constants. Ratios are taken only over pairs for which the denominator is positive.

## Proof
**1. Exact pooled-root representation.** Fix data \(y\). For any prescribed root value \(t\), its optimally fitted leaf values are \(\max\{t,y_i\}\), because each leaf is constrained only to lie above the root. Consequently the unique fitted root minimizes
\[
\Phi_y(t)=a_0(t-y_0)^2+\sum_{i=1}^{m}a_i\bigl(\max\{t-y_i,0\}\bigr)^2.
\]
The function is strictly convex and coercive. On a region with a fixed *strict active set* \(S=\{i:y_i<t\}\), the first-order condition gives
\[
t=\frac{a_0y_0+\sum_{i\in S}a_i y_i}{A_S},\qquad A_S=a_0+\sum_{i\in S}a_i.
\]
Thus the projection is a continuous piecewise-affine map. All possible active sets can be used for an upper bound, even if a particular region is empty. Equalities at region boundaries are handled by continuity.

**2. Exact affine maps on edge gradients.** Put \(d_i=y_i-y_0\), and \(d'_i=(P_a(y))_i-(P_a(y))_0\). On a fixed region \(S\),
\[
d'_i=\begin{cases}0,&i\in S,\\[2pt]d_i-\dfrac{\sum_{j\in S}a_jd_j}{A_S},&i\notin S.\end{cases}
\]
Here \(V_w(y)=\sum_i w_i|d_i|\), so the induced norm of a linear map is the largest weighted absolute column sum. Its column indexed by an inactive leaf \(i\notin S\) has norm \(1\) and its column indexed by an active leaf \(i\in S\) has norm
\[
\frac{a_i}{w_i A_S}\sum_{k\notin S}w_k.
\]
When \(S\) is empty all columns have norm \(1\); when \(S\) is the full set all are zero. If \(i\in S\), then \(A_S\ge a_0+a_i\) and \(\sum_{k\notin S}w_k\le W-w_i\). Therefore every affine region has weighted variation operator norm at most \(K(a,w)\).

**3. Global two-input bound.** A straight segment connecting two arbitrary data vectors crosses only finitely many polyhedral active regions (or lies in common faces, where the affine formulas agree). Break it at region boundaries and use the triangle inequality, the preceding uniform affine bound, and homogeneity. Hence
\[
V_w(P_a(y)-P_a(y'))\le K(a,w)V_w(y-y')
\]
for every pair. Continuity covers degenerate segments on region boundaries. The same follows by integrating the almost-everywhere derivative along the segment.

**4. Sharpness and positive-denominator witnesses.** For the value \(1\), take data \(y_0=0\), \(y_j=3\) for every leaf, and perturb only one leaf upward by \(1/8\). Both vectors already obey strict constraints, so their projections equal themselves, and the variation ratio is \(1\).

For a specified leaf \(i\), take \(y_0=1\), \(y_i=0\), \(y_j=3\) for all \(j\ne i\). Let \(y'\) differ only by \(y'_i=y_i+1/8\). Both fitted roots pool with exactly leaf \(i\), because each root lies strictly between the corresponding value at \(i\) and the other leaves. The root changes by \(a_i/[8(a_0+a_i)]\); all other leaf outputs stay fixed, while the pooled leaf follows the root. Thus the output variation is \(a_i(W-w_i)/[8(a_0+a_i)]\), whereas the input variation of the difference is \(w_i/8\). The ratio equals precisely \(a_i(W-w_i)/[(a_0+a_i)w_i]\). Selecting a maximizing candidate proves equality in the boxed formula.

**5. Consequences.** Nonexpansivity is equivalent to all the candidate fractions being at most \(1\). Equal observation masses and unit edge weights give the candidate \((m-1)/2\). For \(w_i=a_i\), cancellation of the positive \(a_i\) reduces the condition to \(\sum_j a_j-a_i\le a_0+a_i\), or \(\sum_j a_j\le a_0+2a_i\), simultaneously for all \(i\), proving the stated minimum-mass criterion.

## Verification
The accompanying self-contained `check_star_isotonic.py` uses exact rational arithmetic. It independently enumerates candidate active faces and checks them against the sorted pooling algorithm; checks exact column norms of all active sets for randomized positive rational weights; tests two-input inequalities and sharp equality witnesses; and verifies the uniform and matched-mass specializations. A successful run prints `CHECKS_OK` and `TOTAL: 224239`. These checks are finite diagnostics; the complete proof for every finite \(m\) and all positive real weights is in the preceding argument. Reproduce with `python3 check_star_isotonic.py` (standard library only).

## Relationship to prior work
Classical isotonic regression is weighted Euclidean projection onto an order cone. Guyader, Jégou, Németh and Németh discuss regression and bounded variation for ordered sequences. A. B. Németh and S. Z. Németh study the coordinate-order isotonicity of general order-cone projections, explicitly including branching facets, but their order-preserving projection statement is not a quantitative graph-edge-variation stability estimate. Yang and Barber characterize seminorm contractivity for totally ordered isotonic regression; such results do not cover the star partial order or imply the weighted formula above. Punera and Ghosh study isotonic smoothing for hierarchical classification without the present sharp two-data variation modulus. This result concerns the *nonlinear difference* \(P_a(y)-P_a(y')\), not merely the variation of a single fitted output.

## Limitations
The formula applies to one rooted star, weighted quadratic isotonic loss, positive observation masses, positive edge variation weights, and real inputs. It does not classify arbitrary rooted trees, general partial orders, other losses, or nonlinear graph smoothers. The analytic proof establishes an operator constant but not statistical risk, convergence rates, or a claim about independent novelty verification. Equivalent formulae in older sensitivity analyses not located by the stated comparisons cannot be ruled out.

## References
1. A. Guyader, N. Jégou, A. B. Németh, and S. Z. Németh, *A Geometrical Approach to Iterative Isotone Regression*, arXiv:1211.3930v1 (first public 2012-11-16), https://arxiv.org/abs/1211.3930.
2. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458 (first public 2015-03-29), https://arxiv.org/abs/1503.08458.
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (first public 2017-06-06), https://arxiv.org/abs/1706.01852.
4. K. Punera and J. Ghosh, *Enhanced Hierarchical Classification via Isotonic Smoothing*, WWW 2008, https://www.ideal.ece.utexas.edu/papers/punera08_www.pdf.
