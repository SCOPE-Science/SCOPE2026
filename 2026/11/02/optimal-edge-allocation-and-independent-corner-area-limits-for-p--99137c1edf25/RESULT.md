# Optimal edge allocation and independent corner-area limits for polygonal boundary hulls

## Finding
Let \(P\) be a strictly convex Euclidean \(m\)-gon, \(m\ge3\), whose counterclockwise vertices are \(v_0,\ldots,v_{m-1}\). Indices are cyclic. Write \(e_i=v_{i+1}-v_i\), \(d_i=\tfrac12\det(e_{i-1},e_i)>0\), and \(A=\operatorname{area}(P)\). For each independent sample, select edge \(i\) with probability \(w_i>0\), \(\sum_i w_i=1\), and then select a point uniformly along that edge. Let \(K_n\) be the convex hull of \(n\) samples and \(\Delta_n=A-\operatorname{area}(K_n)\).

**Joint corner law and moments.** As \(n\to\infty\),
\[
n^2\Delta_n\ \Longrightarrow\ \sum_{i=0}^{m-1}\frac{d_i}{w_{i-1}w_i}E_i^-E_i^+,
\]
where all \(2m\) variables \(E_i^-,E_i^+\) are independent unit-mean exponentials. Every fixed positive integer moment converges. In particular,
\[
\lim_{n\to\infty}n^2\mathbb E\Delta_n=C_P(w):=\sum_i\frac{d_i}{w_{i-1}w_i},\qquad
\lim_{n\to\infty}n^4\operatorname{Var}(\Delta_n)=3\sum_i\left(\frac{d_i}{w_{i-1}w_i}\right)^2.
\]

**Explicit finite-sample approximation.** For every integer \(n\ge1\), let
\[
F_n(w)=\frac{1}{(n+1)(n+2)}\sum_i\frac{d_i}{w_{i-1}w_i}\bigl[1-(1-w_{i-1})^{n+2}-(1-w_i)^{n+2}+(1-w_{i-1}-w_i)^{n+2}\bigr].
\]
Then the following is a rigorous, explicit error bound:
\[
\left|\mathbb E\Delta_n-F_n(w)\right|\le\left(A+\sum_i d_i\right)\sum_j(1-w_j)^n.
\]
Thus the formula has exponentially small error at fixed strictly positive \(w\), beyond the exact rational leading normalization.

**Optimal allocation and parity rigidity.** The strictly convex function \(C_P(w)\) has a unique minimizer \(w^*\) in the positive probability simplex. It is characterized by one positive Lagrange multiplier \(\lambda\):
\[
(w_i^*)^2=\frac{d_i/w_{i-1}^*+d_{i+1}/w_{i+1}^*}{\lambda},\qquad \sum_i w_i^*=1.
\]
Equal edge probabilities \(w_i=1/m\) are optimal **if and only if** the sums \(d_i+d_{i+1}\) are constant. For odd \(m\) this is equivalent to all \(d_i\) being equal; for even \(m\) it is equivalent to the \(d_i\) alternating between two positive values. In particular, for a convex quadrilateral, equal edge probabilities are optimal **if and only if it is a parallelogram**. The unique optimal weights are invariant under invertible affine transformations of the polygon.

For every triangle, independently of its shape, the optimal leading mean area deficit is \(27A/n^2\); for every parallelogram it is \(32A/n^2\). In a rectangle of side lengths \(a,b\), replacing uniform arclength sampling with equal edge probabilities decreases the asymptotic expected missing area by the exact factor \((a+b)^2/(4ab)\), which can be arbitrarily large.

## Assumptions and scope
The polygon has exactly \(m\) genuine convex vertices and positive edge lengths; adjacent edges are never collinear. Samples are independent, and each chosen edge is sampled uniformly in the edge's affine coordinate. The fixed positive edge probabilities do not depend on \(n\). Polygon coordinates have their usual Euclidean area, but edge probabilities are dimensionless and may differ from proportions of total arclength. The limit concerns area deficit, not Hausdorff distance or interior sampling. All asymptotics hold for each fixed polygon and fixed positive weight vector; no claim of uniformity as weights approach zero is made.

## Proof
1. **Deterministic corner decomposition.** Let \(H_n\) be the event that every edge receives at least one sampled point. On each edge \(i\), define \(L_i\) as the least sampled normalized coordinate measured from \(v_i\) and \(R_i\) as the distance of the rightmost sampled point from \(v_{i+1}\), both in \([0,1]\). When an edge is empty, set both variables to \(1\); this convention only enters the bounded auxiliary expression below. On \(H_n\), the convex hull contains the segment between the extreme sampled points of each edge. Strict convexity makes the connecting segment across each original vertex a hull edge; the disjoint omitted regions are exactly the triangles formed by this vertex and its two neighboring extreme sampled points. Hence
\[
\Delta_n=\sum_i d_i R_{i-1}L_i\quad\text{on }H_n.
\]
Set \(B_n=\sum_i d_i R_{i-1}L_i\). Since \(0\le B_n\le\sum_i d_i\), \(0\le\Delta_n\le A\), and \(\Pr(H_n^c)\le\sum_j(1-w_j)^n\), the stated exponential error follows once \(\mathbb E B_n=F_n(w)\) is established.

2. **An exact order-statistic integral.** For normalized coordinates \(0\le s,t\le1\), the boundary intervals of lengths \(s\) and \(t\) adjoining vertex \(v_i\) on different edges carry probability masses \(w_{i-1}s\) and \(w_it\). They are disjoint. Therefore
\[
\Pr(R_{i-1}>s,L_i>t)=(1-w_{i-1}s-w_it)^n.
\]
Integrating this joint survival probability over the unit square and evaluating the two elementary antiderivatives yields
\[
\mathbb E(R_{i-1}L_i)=\frac{1-(1-w_{i-1})^{n+2}-(1-w_i)^{n+2}+(1-w_{i-1}-w_i)^{n+2}}{(n+1)(n+2)w_{i-1}w_i}.
\]
The displayed expression for \(F_n\) follows by summation. The positivity of \(1-w_{i-1}-w_i\) is guaranteed by \(m\ge3\) and all weights being positive.

3. **Poisson corner limits and moment convergence.** Under the scale change \(s\mapsto s/n\), each of the two endpoint intervals of edge \(i\) has probability mass \(w_i s/n\). For any finite collection of endpoint thresholds, the probability of avoiding the union of their eventually disjoint intervals is \((1-\sum_iw_i(s_i^-+s_i^+)/n)^n\), which tends to \(\exp[-\sum_iw_i(s_i^-+s_i^+)]\). This identifies all scaled endpoint distances jointly as independent exponentials with their respective edge rates. Every corner product then converges as stated; each original edge contributes two independent limiting endpoints. For every fixed power \(k>0\), \(\Pr(nL_i>t)\le\exp(-w_i t)\), with the analogous bound for \(R_i\) on the relevant range and zero beyond it. Thus the scaled endpoint distances have bounded moments of every order, their finite sums of products are uniformly integrable to every fixed order, and the exponentially rare event \(H_n^c\) contributes at most \(n^{2k}A^k\Pr(H_n^c)\to0\). This gives all positive integer moment limits. Since the product of two independent unit exponentials has mean \(1\) and variance \(3\), the mean and variance expressions follow.

4. **Convex optimization.** The Hessian of \((x,y)\mapsto 1/(xy)\) is positive definite on \((0,\infty)^2\): its diagonal entries are \(2/(x^3y)\) and \(2/(xy^3)\), and its determinant is \(3/(x^4y^4)>0\). Each \(d_i>0\), so \(C_P\) is strictly convex, and it diverges when any weight tends to zero. Its unique interior minimum therefore obeys the stated Lagrange equations. Evaluating the gradient at \(w_i=1/m\) gives \(-m^3(d_i+d_{i+1})\). The gradient is constant precisely when all adjacent sums agree. The recurrence \(d_{i+2}=d_i\) has constant solutions for odd cycle length and alternating solutions for even cycle length.

5. **Four-sided geometric rigidity and affine invariance.** For \(m=4\), the recurrence states \(d_0=d_2\) and \(d_1=d_3\). Put \(a=e_0\), \(b=e_1\), \(c=e_2\), \(e_3=-a-b-c\). The two determinant identities imply \(\det(a,c)=0\) and \(\det(a,b)=\det(b,c)\); since \(\det(a,b)>0\), they force \(c=-a\), then \(e_3=-b\). This is exactly the parallelogram condition. Conversely, every parallelogram has \(d_i=A/2\); every triangle has \(d_i=A\). The stated constants and rectangle ratio follow by substitution. An invertible affine map multiplies all \(d_i\) by its positive absolute determinant, so it leaves the minimizer and the normalized limiting law unchanged.

## Verification
The standalone `verify.py` uses only the Python standard library. Running `python verify.py` tests the exact corner decomposition against independent convex-hull computations on triangles, rectangles, irregular convex quadrilaterals and pentagons; checks the exact two-dimensional survival integral against a separately expanded finite polynomial; compares analytic gradients with centered finite differences; checks that nonparallelogram quadrilaterals admit a strict improvement over equal edge probabilities; and compares the limiting mean and variance with independent exponential-product samples. Its observed final line was `ALL_CHECKS_PASSED`. These finite checks supplement, but do not replace, the analytical arguments. All proof definitions and inputs are in this file and the accompanying script.

## Relationship to prior work
Reitzner, Schütt and Werner (arXiv:1911.05917, initially submitted November 14, 2019) develop random polytopes from uniform samples on polytope boundaries, establish volume-deficit orders, and analyze vertex-local contributions; the present geometric decomposition is consistent with that framework. Their inspected full text does not state the weighted, complete planar corner-area limit distribution, the edge-weight optimizer or its parity and parallelogram rigidity. Prochno, Schütt, Sonnleitner and Werner (arXiv:2404.02870, April 3, 2024) study Hausdorff approximation, a different error functional, under arclength-uniform boundary sampling. Earlier boundary-sampling and interior-sampling results provide context without directly supplying the stated edge-allocation classification. The order-statistic and convexity tools themselves are standard; the combined weighted law and geometric rigidity are the contribution assessed here.

## Limitations
The theorem concerns fixed finite-sided strictly convex polygons, independent samples, positive fixed per-edge probabilities, uniform conditional position on each selected edge and asymptotic minimization of expected missing area. It does not claim optimality for arbitrary nonuniform within-edge sampling densities, finite-sample exact minimizers, adaptive sampling, curved boundaries, higher-dimensional polytopes or Hausdorff loss. The exponentially accurate \(F_n\) is not asserted to be the exact expected deficit when an edge can remain unvisited. Exhaustive historical priority verification has not been performed.

## References
1. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917, first public version November 14, 2019; Discrete & Computational Geometry 69 (2023), 453–504. https://arxiv.org/abs/1911.05917 ; https://doi.org/10.1007/s00454-022-00460-2 .
2. J. Prochno, C. Schütt, M. Sonnleitner and E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870, first public version April 3, 2024. https://arxiv.org/html/2404.02870v1 .
3. R. Schneider, *Random approximation of convex sets*, Journal of Microscopy 151 (1988), 211–227, for the earlier general subject of random convex approximation.
