# Exact reflected mixed-volume profile and flat minimum for triangular bipyramids

## Finding
Let \(K\subset\mathbb R^3\) be a full-dimensional convex triangular bipyramid with a base triangle \(\Delta=\operatorname{conv}(v_0,v_1,v_2)\) and two apices on opposite sides of its plane. The apex segment intersects \(\operatorname{relint}\Delta\) at
\[
p=\lambda_0v_0+\lambda_1v_1+\lambda_2v_2,\qquad
\lambda_i>0,\quad \lambda_0+\lambda_1+\lambda_2=1.
\]
Let the perpendicular apex heights be \(h_+>0\) and \(h_->0\), and write \(\alpha=h_+/(h_++h_-)\), \(\beta=1-\alpha\). For real \(z\), define \((z)_+=\max\{z,0\}\). The **complete affine-invariant reflected mixed-volume profile** is
\[
\boxed{\frac{V_3(K,K,-K)}{\operatorname{vol}_3(K)}
=2+\sum_{i=0}^2\big[(\lambda_i-\alpha)_++(\lambda_i-\beta)_+\big].}
\tag{1}
\]
Consequently, the exact difference-body volume profile is
\[
\boxed{\frac{\operatorname{vol}_3(K-K)}{\operatorname{vol}_3(K)}
=14+6\sum_{i=0}^2\big[(\lambda_i-\alpha)_++(\lambda_i-\beta)_+\big].}
\tag{2}
\]
For each fixed apex-height fraction \(0<\alpha<1\), the minimum of the ratio in (1), allowing all interior barycentric intersections, is
\[
\boxed{2+\big(1-3\min\{\alpha,1-\alpha\}\big)_+.}
\tag{3}
\]
The global minimum of (1) is \(2\), equivalently a difference-body ratio of \(14\). It is attained **if and only if**
\[
\boxed{\frac13\le\alpha\le\frac23\quad\text{and}\quad
\lambda_i\le\min\{\alpha,1-\alpha\}\ \text{for }i=0,1,2.}
\tag{4}
\]
At a balanced apex split, \(\alpha=\beta=1/2\), this is the positive-area barycentric region \(\max_i\lambda_i\le1/2\): the exact minimum is **not isolated in affine moduli**. The precise possible ranges of the ratios in (1) and (2) over nondegenerate bipyramids are \([2,3)\) and \([14,20)\), respectively.

## Assumptions and scope
A convex triangular bipyramid has precisely five vertices and six triangular facets. The equatorial triangle and the two nonadjacent apices determine the intrinsic affine data \(\alpha\in(0,1)\) and \(\lambda_i>0\) with sum one, up to permuting base vertices and interchanging apices. Here \(\operatorname{vol}_3\) is Euclidean Lebesgue volume; the reflected Minkowski mixed volume is normalized by
\[
\operatorname{vol}_3(A+tB)
=\operatorname{vol}_3(A)+3tV_3(A,A,B)+3t^2V_3(A,B,B)+t^3\operatorname{vol}_3(B),\qquad t\ge0.
\]
The ratios are invariant under invertible affine transformations and translation. The apex segment must meet the *relative interior* of the equatorial triangle; degenerate triangular faces or zero heights are excluded. There is no claim concerning square pyramids, general five-vertex convex hulls, or higher-dimensional bipyramids.

## Proof
**1. Affine normalization.** Map the equatorial triangle to \(v_0=(0,0,0)\), \(v_1=(1,0,0)\), \(v_2=(0,1,0)\). A shear parallel to its plane makes the apices
\[
a_+=(s,t,h),\qquad a_-=(s,t,-k),\qquad
s,t>0,\quad s+t<1,\quad h,k>0.
\]
Then \(\lambda_0=1-s-t\), \(\lambda_1=s\), \(\lambda_2=t\), \(L=h+k\), \(\alpha=h/L\), \(\beta=k/L\). Splitting at the equatorial triangle gives
\[
\operatorname{vol}_3(K)=\frac{h+k}{6}=\frac L6.
\tag{5}
\]

**2. All six facet supports.** For a triangular facet, let \(N\) denote the outward area vector of *twice* its area, so \(N=2\operatorname{area}(F)u_F\). Write \(h_{-K}(N)=\max_{x\in-K}\langle N,x\rangle=-\min_{x\in K}\langle N,x\rangle\). The two facets meeting each equatorial edge have the following outward area vectors and reflected supports:

| Equatorial edge and apex | Outward area vector \(N\) | Reflected support \(h_{-K}(N)\) |
|---|---|---|
| \(v_0v_1,a_+\) | \((0,-h,t)\) | \(\max\{h,Lt\}\) |
| \(v_0v_1,a_-\) | \((0,-k,-t)\) | \(\max\{k,Lt\}\) |
| \(v_0v_2,a_+\) | \((-h,0,s)\) | \(\max\{h,Ls\}\) |
| \(v_0v_2,a_-\) | \((-k,0,-s)\) | \(\max\{k,Ls\}\) |
| \(v_1v_2,a_+\) | \((h,h,\lambda_0)\) | \((L\lambda_0-h)_+\) |
| \(v_1v_2,a_-\) | \((k,k,-\lambda_0)\) | \((L\lambda_0-k)_+\) |

These values follow by checking the five vertices of \(K\); for instance, at \(N=(0,-h,t)\), the negative of the smallest vertex scalar product equals \(\max\{h,Lt\}\). The six listed triangular faces are exhaustive because the two apex tetrahedra meet only along the interior equatorial triangle.

**3. The mixed-volume identity.** The polytope first mixed-volume formula gives
\[
3V_3(K,K,-K)=\int_{S^2}h_{-K}(u)\,dS_K(u)
=\sum_F \operatorname{area}(F)h_{-K}(u_F)
=\frac12\sum_Fh_{-K}(N_F).
\]
Consequently \(V_3(K,K,-K)=\frac16\sum_Fh_{-K}(N_F)\). Replace \(\max\{h,L\lambda_i\}\) by \(h+L(\lambda_i-\alpha)_+\), and similarly for \(k\). Summing the table yields
\[
\sum_Fh_{-K}(N_F)=L\left(2+\sum_{i=0}^2[(\lambda_i-\alpha)_++(\lambda_i-\beta)_+]\right).
\]
Dividing by (5) proves (1). Reflection and symmetry of mixed volume imply \(V_3(K,-K,-K)=V_3(K,K,-K)\). Polarizing the difference body \(K-K=K+(-K)\) therefore gives
\[
\operatorname{vol}_3(K-K)=2\operatorname{vol}_3(K)+6V_3(K,K,-K),
\]
which proves (2).

**4. Sharp fixed-height minimum.** By convexity of \(x\mapsto(x-c)_+\), Jensen's inequality with \(\sum_i\lambda_i=1\) gives, separately for \(c=\alpha,\beta\),
\[
\sum_{i=0}^2(\lambda_i-c)_+\ge3(1/3-c)_+.
\]
Equality in the combined bound occurs at \(\lambda_0=\lambda_1=\lambda_2=1/3\), so the bound is attained. Since \(\alpha+\beta=1\), at most one of \(\alpha,\beta\) can be below \(1/3\), yielding (3). If \(\alpha<1/3\), the complete fixed-height minimizing set is \(\lambda_i\ge\alpha\) for all \(i\); these conditions automatically imply \(\lambda_i<\beta\). For \(\alpha>2/3\), the analogous condition is \(\lambda_i\ge\beta\) for all \(i\). For \(1/3\le\alpha\le2/3\), equation (1) equals \(2\) exactly when all six positive parts vanish, which is (4). Hence (4) describes *all* global minimizers.

**5. Strict upper endpoint and full range.** For \(0<c<1\) and \(\lambda_i>0\) summing to one, \(\sum_i(\lambda_i-c)_+<1-c\): if one index is active, its value is strictly below one; if at least two are active, subtracting at least \(2c\) from a sum at most one gives a strict bound. Taking \(c=\alpha\) and \(\beta\) in (1) yields strictly less than \(2+(1-\alpha)+(1-\beta)=3\). Conversely, for any fixed \(0<\alpha<1\), take \(\lambda_0=1-2\varepsilon\), \(\lambda_1=\lambda_2=\varepsilon\) and \(\varepsilon\downarrow0\). The ratio tends to \(3\), while each positive \(\varepsilon\) gives a nondegenerate bipyramid. Connectedness of the parameter domain and continuity of (1), together with (4), prove every value in \([2,3)\) occurs, and (2) gives \([14,20)\).

## Verification
The standalone `verify_bipyramid.py` uses exact rational numbers for the six facet-support calculations and an independent \(3\)-dimensional convex-hull triangulation of all pairwise vertex differences, with exact rational tetrahedral determinants for the resulting volume. It tests \(247\) rational parameter instances, including equality, height imbalance, nonuniform barycentric weights, and crossing thresholds, returning `BIPYRAMID_GODBERSEN_VERIFY_OK cases=247 exact_facet=247 exact_hull=247`. Numerical hull triangulation determines combinatorial faces, while each reported simplex volume is evaluated with exact rational arithmetic. Its finite checks supplement rather than establish the general theorem, which is proved in steps 1–5.

## Relationship to prior work
Kotrbatý and Mouamine (July 2026) prove the universal Godbersen inequality and polytope equality characterization, and Fryš–Kotrbatý–Mouamine–Wang (October 2026) give the general equality theorem and a higher-order extension. Their universal inequality is \(V_3(K,K,-K)\le3\operatorname{vol}_3(K)\), with equality exactly for tetrahedra, but does not imply the detailed formula (1), the sharp internal minimum, or the positive-dimensional plateau of distinct non-simplex affine shapes.

The available full published mathematical record *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* computes the family obtained by cutting a vertex from a simplex with a **parallel** hyperplane: that family has a pair of homothetic simplex cross sections and is not the present triangular bipyramid, which has two apices joined through a triangle and six triangular facets. Its coefficient formula does not specialize to (1). A two-dimensional reflected-mixed-area result for quadrilaterals likewise does not state a three-dimensional five-vertex formula. These object, parameter and implication differences matter; matching only the word “Godbersen” would not establish novelty or coverage.

## Limitations
This is an exact classification only within convex triangular bipyramids, not within all three-dimensional convex bodies, all five-vertex polytopes, or arbitrary multi-apex polytopes. The upper endpoint occurs only as a degeneration, not on a genuine five-vertex body. The global lower endpoint is internal to this shape family and **not** a new universal lower bound: the general Brunn–Minkowski difference-body bound can be smaller. The finite tests are not exhaustive proofs. Historical priority cannot be certified by finite database searches; older or unindexed explicit mixed-volume calculations for triangular bipyramids remain a residual risk.

## References
1. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers–Shephard inequality*, arXiv:2607.20387v1, first public 22 July 2026; Theorem 1.1 and Section 3.
2. O. Friedland, E. Putterman and M. Szusterman, *Equality case in the Kotrbatý–Mouamine inequality*, arXiv:2610.04527v1, first public 3 October 2026.
3. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-Order Godbersen Inequality and a Characterization of Simplices via the Face Lattice*, arXiv:2610.06806v1, first public 5 October 2026, especially Theorem 1.2.
4. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations*, published mathematical record, published-finding corpus identifier `2026/10/11/SCOPE-exact-godbersen-mixed-volume-profile-for-one-vertex-simplex-trun--dda979276949`, `RESULT.md`.
5. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik **8** (1957), 220–233, classical background.
