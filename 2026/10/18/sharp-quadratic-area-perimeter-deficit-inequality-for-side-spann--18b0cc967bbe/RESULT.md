# Sharp quadratic area–perimeter deficit inequality for side-spanning inscribed polygons

## Finding

Let \(K\) be any nondegenerate convex Euclidean polygon with \(m\ge3\) genuine vertices and interior angles \(\theta_i\in(0,\pi)\). Let \(S\subseteq\partial K\) be finite and meet the relative interior of **every** side, and set \(H=\operatorname{conv}S\). Write \(\Delta_P=P(K)-P(H)\ge0\) and \(\Delta_A=A(K)-A(H)\ge0\). Define
\[
\kappa_i=\frac{\sin\theta_i}{8[1-\sin(\theta_i/2)]^2},\qquad
C(K)=\left(\sum_{i=1}^{m}\kappa_i^{-1}\right)^{-1}.
\]
Then
\[
\boxed{\Delta_A\ge C(K)\,\Delta_P^2.}
\]
The constant \(C(K)>0\) is **optimal for each fixed polygon** and depends only on the interior angles. The inequality admits equality with \(\Delta_P>0\) for explicit nondegenerate side-spanning configurations, not merely in a limiting degeneration. All nontrivial equality configurations are classified below. An **exact nonnegative stability decomposition** separates imbalance of the two corner cuts from dispersion of the perimeter loss across corners.

## Assumptions and scope

Angles are Euclidean interior angles and adjacent collinear edges are merged. For every vertex \(v_i\), let \(x_i\ge0\) and \(y_i\ge0\) be the distances from that vertex to the nearest points of \(S\) on its preceding and following sides. The side-spanning condition makes each distance less than its side length. Put
\[
\begin{aligned}
 d_i&=\sqrt{x_i^2+y_i^2-2x_iy_i\cos\theta_i},\\
 u_i&=x_i+y_i-d_i,\qquad v_i=\tfrac12x_iy_i\sin\theta_i,\\
 s_i&=\sin(\theta_i/2),\qquad c_i=\cos(\theta_i/2),\\
 z_i&=\begin{cases}d_i/(x_i+y_i),&x_i+y_i>0,\\1,&x_i+y_i=0.\end{cases}
\end{aligned}
\]
For this class of inscribed hulls, \(\Delta_P=\sum_i u_i\) and \(\Delta_A=\sum_i v_i\) exactly. If \(H=K\), equality holds trivially. Otherwise, equality holds **if and only if** every corner has balanced positive cuts \(x_i=y_i>0\) and the numbers \(\kappa_i u_i\) are identical across all corners; equivalently \(x_i=y_i=t[1-\sin(\theta_i/2)]/\sin\theta_i\) for a common \(t>0\), subject to the obvious side-length feasibility inequalities \(x_i+y_{i+1}\le\ell_i\) (cyclic indices). The equality construction below ensures strict feasibility.

## Proof

**1. Exact corner losses.** On every side, the extreme boundary samples are exposed support points of \(H\). Their side segments connect via chords joining the nearest samples across each polygon vertex. Every removed corner is a triangle, and the removed corner triangles have disjoint interiors. The cosine rule and triangle area formula give
\[
\Delta_P=\sum_i\bigl(x_i+y_i-d_i\bigr)=\sum_i u_i,
\qquad \Delta_A=\frac12\sum_i x_iy_i\sin\theta_i=\sum_i v_i.
\]
These are finite exact identities, with no sampling distribution or asymptotic argument.

**2. Sharp single-corner inequality.** Fix one interior angle \(\theta\), and suppress its index. When \(x,y>0\), write \(p=x+y\), \(s=\sin(\theta/2)\), \(c=\cos(\theta/2)\), and \(z=d/p\). Then \(s\le z<1\), since
\[
z^2=s^2+c^2\frac{(x-y)^2}{(x+y)^2},
\]
and the ratio of removed corner area to squared perimeter shortening is
\[
\frac{v}{u^2}
=\frac{\sin\theta}{8c^2}\frac{1+z}{1-z}
\ge\frac{\sin\theta}{8(1-s)^2}=\kappa(\theta).
\]
Strict monotonicity of \((1+z)/(1-z)\) proves equality exactly when \(z=s\), equivalently \(x=y>0\). If \(xy=0\), both \(u\) and \(v\) vanish and the non-strict inequality remains valid.

The corner inequality has an **exact slack**. Direct subtraction of the two ratios, using \(z^2-s^2=c^2(x-y)^2/(x+y)^2\), gives
\[
\boxed{v-\kappa(\theta)u^2
=\frac{\sin\theta}{4}\,\frac{(x-y)^2(1-z)}{(z+s)(1-s)}\ge0.}
\]
At \(x+y=0\), both sides are zero under the stated convention \(z=1\). This identity is valid also when one gap vanishes.

**3. Optimal global inequality and stability.** Set \(r_i=\kappa_i^{-1}>0\), \(R=\sum_i r_i\), and \(C=R^{-1}\). Weighted Cauchy–Schwarz implies
\[
\sum_i\kappa_i u_i^2=\sum_i r_i(\kappa_i u_i)^2
\ge \frac{(\sum_i u_i)^2}{\sum_i r_i}=C\Delta_P^2.
\]
Combining with Step 2 proves the theorem. More precisely, the variance identity for the positive weights \(r_i\) gives the exact decomposition
\[
\boxed{\begin{aligned}
\Delta_A-C\Delta_P^2
={}&\sum_{i=1}^{m}\frac{\sin\theta_i}{4}
\frac{(x_i-y_i)^2(1-z_i)}{(z_i+s_i)(1-s_i)}\\
&+\sum_{i=1}^{m}\kappa_i^{-1}
\bigl(\kappa_i u_i-C\Delta_P\bigr)^2.
\end{aligned}}
\]
Thus both the cut-balance and the weighted corner-loss dispersion must vanish at equality. For \(\Delta_P>0\), the second sum forces every \(u_i=C\Delta_P/\kappa_i>0\); the first then forces all \(x_i=y_i>0\). Since \(u_i=2x_i(1-s_i)\), common \(\kappa_i u_i\) gives the equality parameterization in the assumptions.

**4. Sharpness and attainment.** Choose any \(t>0\) so small that
\[
t\left(\frac{1-s_i}{\sin\theta_i}
+\frac{1-s_{i+1}}{\sin\theta_{i+1}}\right)<\ell_i
\qquad\text{for every side }i.
\]
This is possible because there are finitely many positive side lengths and interior angles. Mark on each of the two rays from \(v_i\) the distance \(x_i=y_i=t(1-s_i)/\sin\theta_i\); include these marks in \(S\). Every side contains its two distinct prescribed marks, so the hull is side-spanning. At each corner, the marks balance and satisfy
\[
\kappa_i u_i=\kappa_i\cdot 2t(1-s_i)^2/\sin\theta_i=t/4,
\]
independent of \(i\). Both nonnegative terms in the stability identity vanish, with \(\Delta_P>0\). Consequently \(C(K)\) cannot be increased for that polygon, and the equality classification is complete.

## Verification

The standalone standard-library file `check.py` independently computes hull areas and perimeters, compares them with the exact corner decomposition, checks the sharp inequality and the two-term stability identity, and constructs equality configurations on multiple nonregular convex polygons. In the completed diagnostic run, 1,800 random configurations passed the analytic/numeric comparisons; finite checks illustrate rather than prove the theorem. Steps 1–4 are the rigorous proof for every admissible polygon and configuration.

## Relationship to prior work

Reitzner, Schütt and Werner (first circulated 2019) study expected combinatorial quantities and volume deficits for boundary-random approximants of polytopes. Prochno, Schütt, Sonnleitner and Werner (first circulated 2024) study the Hausdorff error of boundary-random approximants. These works motivate quantitative finite inscribed-polygon approximation but their examined principal statements do not give an angle-specific, **best possible finite-configuration comparison of simultaneous area and perimeter deficits**, nor its exact two-mechanism equality and stability law. Polygonal isoperimetric-deficit estimates generally compare each polygon with an optimal shape rather than comparing a fixed outer polygon with every side-spanning inner hull. The present theorem concerns the latter distinct geometric object and is deterministic: it also applies sample-by-sample to any random-boundary model on the event that every side is visited.

## Limitations

The side-spanning hypothesis is essential to the exact corner decomposition: allowing a missing side can create larger regions not represented by its two neighboring corner triangles. The constant depends on every angle and is not claimed to be uniformly bounded away from zero over polygons with arbitrarily sharp vertices. No theorem is asserted for arbitrary interior-point hulls, curved boundaries, or higher dimensions. The equality configurations require the side-length feasibility inequalities; sufficiently small positive common scale always realizes them. No exhaustive historical uniqueness or independent mathematical audit is claimed.

## References

1. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public 14 November 2019), Discrete & Computational Geometry 69 (2023), 453–504. https://arxiv.org/abs/1911.05917
2. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first public 3 April 2024), Mathematische Annalen 392 (2025), 4525–4542. https://arxiv.org/abs/2404.02870
3. E. Indrei, *A sharp lower bound on the polygonal isoperimetric deficit*, arXiv:1502.05978 (first public 20 February 2015). https://arxiv.org/abs/1502.05978
