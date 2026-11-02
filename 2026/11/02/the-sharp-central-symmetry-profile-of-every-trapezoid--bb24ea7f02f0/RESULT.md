# The sharp central-symmetry profile of every trapezoid

## Finding

For a planar convex body \(T\) define its Kovner–Besicovitch point-symmetry ratio by
\[
\kappa(T)=\frac{1}{\operatorname{area}(T)}\max_{c\in\mathbb R^2}\operatorname{area}\bigl(T\cap(2c-T)\bigr).
\]
Every centrally symmetric subset with center \(c\) is contained in this intersection, so the definition also gives the largest centrally symmetric subset's area fraction.

**Theorem.** Let \(T\) be a nondegenerate convex trapezoid with two parallel sides of positive lengths \(B\ge b\), and put \(t=b/B\in(0,1]\). Then
\[
\boxed{\kappa(T)=\begin{cases}\frac{2}{3(1-t^2)},&0<t\le\frac13,\\[3pt]\frac{1+3t}{2(1+t)},&\frac13\le t\le1.\end{cases}}
\]
There is precisely one maximizing center. After an affine normalization to
\[
T_t=\operatorname{conv}\{(-1,0),(1,0),(t,1),(-t,1)\},
\]
that center is
\[
\boxed{c_t=\begin{cases}\left(0,\frac{1}{3(1-t)}\right),&0<t\le\frac13,\\[3pt]\left(0,\frac12\right),&\frac13\le t\le1.\end{cases}}
\]
The profile is strictly increasing on \((0,1]\), is \(C^1\) at \(t=1/3\), but its right minus left second derivative there equals \(-27/8\). The ratio therefore uniquely identifies \(t\). At \(t\downarrow0\), the inverse has sharp Hölder exponent \(1/2\).

## Assumptions and scope

The figure is a full-dimensional Euclidean trapezoid, meaning a convex quadrilateral with at least one pair of parallel opposite sides. The longer and shorter parallel base lengths are positive; \(t=1\) includes parallelograms. If both pairs of opposite sides are parallel, either pair gives \(t=1\). This is an affine-invariant problem: affine maps preserve ratios of parallel collinear segment lengths, central symmetry, intersection, and relative area. Every nondegenerate trapezoid is affinely equivalent to the displayed \(T_t\). Centers in the theorem are *points*, not axes of symmetry. At the boundary \(t=0\), \(T_t\) degenerates from a quadrilateral to a triangle, and the limiting formulas still make sense, but only \(t>0\) belongs to the stated trapezoid class.

## Proof

**1. Affine reduction and slices.** Make the parallel bases horizontal at heights \(z=0\) and \(z=1\), center their respective midpoints by an affine shear, and scale their half-lengths to \(1\) and \(t\). Put \(q=1-t\in[0,1)\). The horizontal section of \(T_t\) at height \(z\in[0,1]\) is the interval \([-r(z),r(z)]\), with \(r(z)=1-qz\). Its total area is \(1+t\).

**2. Optimal horizontal coordinate.** Fix a candidate symmetry center \((x,y)\). At height \(z\), the intersection \(T_t\cap(2(x,y)-T_t)\) is the intersection of \([-r(z),r(z)]\) with \([2x-r(2y-z),2x+r(2y-z)]\); both are empty outside their respective height supports. The overlap length is at most \(2\min\{r(z),r(2y-z)\}\), and equality for almost every relevant \(z\) is attained at \(x=0\). If \(y\notin(0,1)\), the intersection has zero area, while choices \(y\in(0,1)\) produce positive area. For each such \(y\), at the central height \(z=y\) the two intervals have equal positive radii. If \(x\ne0\), their overlap is then strictly smaller than the upper bound and remains so for \(z\) in a positive-measure neighborhood. Therefore every global maximizing center has \(x=0\), uniquely in that coordinate.

**3. Exact one-variable area.** For \(0<y<1\) write \(m=\min\{y,1-y\}\). The common vertical support is \([y-m,y+m]\). Since \(r\) decreases, the smaller of \(r(z)\) and \(r(2y-z)\) equals \(1-q(y+|z-y|)\). Thus
\[
A_t(y)=\operatorname{area}\bigl(T_t\cap(2(0,y)-T_t)\bigr)
=\int_{y-m}^{y+m}2\bigl(1-q(y+|z-y|)\bigr)\,dz
=4m(1-qy)-2qm^2.
\]
Splitting at \(y=1/2\) gives the exact quadratic branches
\[
A_t(y)=\begin{cases}4y-6qy^2,&0\le y\le1/2,\\[3pt]4t(1-y)+2q(1-y)^2,&1/2\le y\le1.\end{cases}
\]
On the upper half \(A_t\) is strictly decreasing (including \(t=1\)). On the lower half it is strictly concave if \(t<1\), with unconstrained maximizer \(y_0=1/(3q)\), which lies in \([0,1/2]\) exactly when \(t\le1/3\). For \(t>1/3\), its lower-half maximum is at \(y=1/2\). If \(t=1\), the lower branch is \(4y\), also uniquely maximized at \(1/2\). These observations prove the stated unique maximizing center. Substitution gives
\[
\max_y A_t(y)=\begin{cases}\frac{2}{3(1-t)},&0<t\le1/3,\\[3pt]\frac{1+3t}{2},&1/3\le t\le1.\end{cases}
\]
Division by \(\operatorname{area}(T_t)=1+t\) proves the two-branch ratio.

**4. Phase, inversion, and conditioning.** On the first branch
\(\kappa'(t)=4t/[3(1-t^2)^2]>0\); on the second \(\kappa'(t)=1/(1+t)^2>0\). Both first derivatives equal \(9/16\) at \(t=1/3\). Their one-sided second derivatives there are \(81/32\) and \(-27/32\), giving the jump \(-27/8\). If a measured ratio is \(k\), the unique recovered base ratio is
\[
\boxed{t=\begin{cases}\sqrt{1-\frac{2}{3k}},&\frac23\le k\le\frac34,\\[3pt]\frac{2k-1}{3-2k},&\frac34\le k\le1.\end{cases}}
\]
The lower endpoint is the triangular limit and the upper endpoint is attained exactly by parallelograms. Since \(\kappa(t)-2/3=(2/3)t^2+O(t^4)\) as \(t\downarrow0\), no inverse Hölder exponent larger than \(1/2\) can hold uniformly up to the triangular endpoint; the displayed inverse attains exponent \(1/2\) there. Away from this endpoint the inverse is locally Lipschitz.

## Verification

The accompanying standalone `checker.py` uses exact rational polygon clipping of the intersection of the normalized trapezoid and its point reflection, independently of the slice integral. It checks 845 rational center/shape configurations in several aspect-ratio classes, including the transition and parallelogram. Symbolic calculations check both optimal-value branches, the transition derivatives, inverse formulas, and the sharp endpoint expansion. Execute `python checker.py` with Python 3 and SymPy installed (the optional `requirements.txt` lists the dependency); successful output ends in `ALL_CHECKS_PASSED`. Finite grids are consistency tests, not a substitute for the proof above.

## Relationship to prior work

The classical Kovner–Besicovitch theorem gives the universal planar convex-body point-symmetry bound \(2/3\), with triangles as limiting extremizers; that theorem is not claimed here. Goenka, Moore, Sun, and White's 2023 work investigates *axial* symmetry ratios and folding for convex bodies; it describes the point-symmetric antecedent but does not state the present trapezoid-specific two-branch profile. Generic maximum-translation-overlap algorithms (including the 2025 work of Chan and Hair and an earlier 1998 algorithm) can calculate maximal overlaps for fixed polygon inputs, but the novelty claim is the uniform symbolic affine classification, uniqueness, exact phase threshold, and conditioning—not generic computability of an instance. A previous published geometric study may still contain an equivalent specialized formula; historical priority is provisional.

## Limitations

This is a two-dimensional, exact-geometry result for genuine convex trapezoids, not a full classification of arbitrary quadrilaterals. Identifiability is for the affine base-ratio parameter, not absolute size or Euclidean angles. The ratio assumes exact optimal overlap, and no statistical/noisy-measurement estimator is analyzed. Generic polygon-overlap algorithms provide computational coverage of individual instances. Full text of the foundational 1998 algorithmic paper and a relevant specialized symmetry reference could not be obtained; their potential historical coverage remains a priority risk. No independent audit has been performed.

## References

1. R. Goenka, K. Moore, W. R. Sun, and E. P. White, *On Axial Symmetry in Convex Bodies*, arXiv:2309.12597 (first publicly posted 2023-09-22), https://arxiv.org/abs/2309.12597 .
2. T. M. Chan and I. Hair, *A Linear Time Algorithm for the Maximum Overlap of Two Convex Polygons Under Translation*, arXiv:2504.18352 (2025), https://arxiv.org/abs/2504.18352 .
3. M. de Berg and collaborators, *Computing maximum overlap of two convex polygons under translation*, 1998, DOI:10.1007/PL00005845 . Full text not inspected.
4. G. Tóth, *Measures of Symmetry for Convex Sets and Stability*, Springer, 2015, DOI:10.1007/978-3-319-23733-6 . Full text not inspected.
