# Complete volumetric convexification spline for cross-polytope vertex translates

## Finding

For every integer \(d\ge2\), let
\[
C_d=\{x\in\mathbb R^d:\|x\|_1\le1\},\qquad
V_d=\{\pm e_1,\ldots,\pm e_d\},\qquad
U_{d,t}=V_d+tC_d\quad(t\ge0).
\]
Because \(\operatorname{conv}(U_{d,t})=(1+t)C_d\), its **volumetric convexification deficit** is
\[
H_d(t)=\operatorname{vol}_d\big((1+t)C_d\setminus U_{d,t}\big),\qquad
v_d=\operatorname{vol}_d(C_d)=\frac{2^d}{d!}.
\]
Write \(a_+=\max\{a,0\}\). The complete exact answer, valid for **all** \(d\ge2\) and \(t\ge0\), is
\[
\boxed{\frac{H_d(t)}{v_d}=\begin{cases}
(1+t)^d-2dt^d,&0\le t\le1,\\[2mm]
2(-1)^d\displaystyle\sum_{j=3}^{d}\frac{(-1)^j\binom dj}{j-2}
(j-1-t)_+^d,&t\ge1.
\end{cases}}
\]
The second sum is empty for \(d=2\); both branches agree at \(t=1\). In particular, \(H_d(t)>0\) exactly when \(0\le t<d-1\), and the exact convexification threshold is \(t=d-1\). For \(d\ge3\), the **last nonzero chamber** is especially simple:
\[
H_d(t)=\frac{2^{d+1}}{d!(d-2)}(d-1-t)^d,
\qquad d-2\le t\le d-1.
\]

The volume profile is a polynomial spline with a strict regularity hierarchy. It is \(C^{d-2}\) at the first knot \(t=1\), but not \(C^{d-1}\), with the exact derivative jump
\[
H_d^{(d-1)}(1^+)-H_d^{(d-1)}(1^-)=2^d d(d-1).
\]
At each subsequent integer knot \(k\in\{2,\ldots,d-1\}\), it is \(C^{d-1}\), but not \(C^d\), with jump
\[
H_d^{(d)}(k^+)-H_d^{(d)}(k^-)
=\frac{2^{d+1}(-1)^k}{k-1}\binom d{k+1}\ne0.
\]
The second assertion is vacuous when \(d=2\). Away from these knots, \(H_d\) is polynomial, including the identically zero tail.

For illustration, in dimension three:
\[
H_3(t)=\frac43\begin{cases}
(1+t)^3-6t^3,&0\le t\le1,\\
2(2-t)^3,&1\le t\le2,\\
0,&t\ge2.
\end{cases}
\]

## Assumptions and scope

The dimension \(d\) is an integer at least two. Volume means ordinary \(d\)-dimensional Lebesgue measure; \(t\) is real and nonnegative. The \(2d\) components of \(U_{d,t}\) are closed translates of a homothetic copy of the *same* coordinate cross-polytope. Their union need not be convex. This theorem concerns missing **volume**, not Euclidean Hausdorff distance or arbitrary convexifying bodies. Boundary sets have zero Lebesgue measure and do not affect the formulas.

## Proof

**1. Exact distance and hole condition.** Set \(s=\sum_i|x_i|\) and \(M=\max_i|x_i|\). For each coordinate \(i\), choosing the nearer signed vertex gives
\[
\min_{\varepsilon\in\{-1,1\}}\|x-\varepsilon e_i\|_1
=s-|x_i|+\big||x_i|-1\big|
=s+1-2\min\{|x_i|,1\}.
\]
Taking the minimum over \(i\) yields
\[
\min_{v\in V_d}\|x-v\|_1=s+1-2\min\{M,1\}.\tag{1}
\]
For \(t\ge1\), inside the enclosing cross-polytope \(s\le t+1\), a point is uncovered precisely when
\[
s>t-1,\qquad |x_i|<h_t(s):=\frac{s+1-t}{2}\quad\text{for all }i.\tag{2}
\]
Indeed, \(h_t(s)\le1\) in the enclosing cross-polytope, so (1) is equivalent to (2). In the closed first orthant, the absolute values are ordinary coordinates.

**2. Elementary low-scale branch.** The \(2d\) vertex centers are pairwise separated by \(\ell_1\)-distance at least two. For \(0\le t\le1\), the interiors of their radius-\(t\) cross-polytopes are pairwise disjoint. Each has volume \(v_dt^d\), while the enclosing body has volume \(v_d(1+t)^d\). Consequently,
\[
H_d(t)=v_d\big((1+t)^d-2dt^d\big),\quad0\le t\le1.\tag{3}
\]
Touching at \(t=1\) causes no volume ambiguity.

**3. Slice formula with all positive-part boundaries accounted for.** For \(t\ge1\), fix \(s\in[t-1,t+1]\). The \((d-1)\)-dimensional simplex slice \(\{x_i\ge0:\sum_i x_i=s\}\), written with the standard coarea normalization, has differential volume \(s^{d-1}\,ds/(d-1)!\). The slice satisfying \(x_i<h_t(s)\) for all \(i\) has differential volume, by inclusion-exclusion over the upper bounds,
\[
\frac{ds}{(d-1)!}\sum_{j=0}^{d}(-1)^j\binom dj
\big(s-jh_t(s)\big)_+^{d-1}.\tag{4}
\]
There are \(2^d\) sign orthants. Since \(s-jh_t(s)=(1-j/2)s+j(t-1)/2\), integration of (4) gives
\[
\begin{aligned}
\frac{H_d(t)}{v_d}
={}&(t+1)^d-(t-1)^d-2d\big(t^d-(t-1)^d\big)\\
&+2d\binom d2(t-1)^{d-1}\\
&+2\sum_{j=3}^{d}\frac{(-1)^j\binom dj}{j-2}
\big((t-1)^d-(t+1-j)_+^d\big).
\end{aligned}\tag{5}
\]
Here the \(j=0\) integral is \(((t+1)^d-(t-1)^d)/d\), the \(j=1\) integral is \(2(t^d-(t-1)^d)/d\), and the \(j=2\) integral is \(2(t-1)^{d-1}\). For \(j\ge3\), the affine positive part decreases as \(s\) increases and has integral \(2\big((t-1)^d-(t+1-j)_+^d\big)/[d(j-2)]\). Thus (5) treats every moving cutoff exactly.

**4. Sharp threshold, and polynomial cancellation.** For every \(x\in(1+t)C_d\), if \(M\ge1\), formula (1) gives \(\min_v\|x-v\|_1=s-1\le t\). If \(M<1\), then \(M\ge s/d\), whence
\[
\min_v\|x-v\|_1\le1+s\big(1-2/d\big)
\le1+(t+1)\big(1-2/d\big)\le t
\]
provided \(t\ge d-1\); the last inequality is equivalent to \(t\ge d-1\) for \(d>2\), and holds for \(d=2,t\ge1\). Thus \(U_{d,t}=(1+t)C_d\) for \(t\ge d-1\). Conversely, if \(t<d-1\), the point \(x=((1+t)/d,\ldots,(1+t)/d)\) on a positive facet has all coordinates below one and violates the covering criterion strictly: \(\min_v\|x-v\|_1-t=2(d-1-t)/d>0\). By continuity, a full-dimensional neighborhood inside the enclosing body is uncovered, so \(H_d(t)>0\).

For \(t\ge d-1\) all quantities \((t+1-j)_+\) in (5) can be replaced by their untruncated polynomial arguments, and the left side is identically zero. Therefore the resulting ordinary polynomial in \(t\), which vanishes on an infinite interval, vanishes identically. Subtracting this zero polynomial from (5) yields
\[
\frac{H_d(t)}{v_d}
=2\sum_{j=3}^{d}\frac{(-1)^j\binom dj}{j-2}
\big((t+1-j)^d-(t+1-j)_+^d\big).
\]
For each \(j\), the bracket is \((-1)^d(j-1-t)_+^d\). This proves the compact spline formula for every \(t\ge1\). If \(d=2\) the sum is empty, consistently with the threshold one.

**5. Final chamber and all derivative jumps.** If \(d\ge3\) and \(d-2\le t<d-1\), only the term \(j=d\) survives, giving the last-chamber formula. For \(1<t<2\), comparison of (5) with the polynomial continuation of (3) leaves a term \(2d\binom d2(t-1)^{d-1}\) and terms divisible by \((t-1)^d\). Multiplying its \((d-1)\)-st derivative by \(v_d=2^d/d!\) gives the stated jump \(2^dd(d-1)\); all lower derivatives match. At \(k\in\{2,\ldots,d-1\}\), only the summand \(j=k+1\) changes polynomial form. Differentiating \((k-t)_+^d\) shows that the \(d\)-th right-minus-left derivative jump is
\[
-v_d\,2(-1)^d\frac{(-1)^{k+1}\binom d{k+1}}{k-1}(-1)^dd!
=\frac{2^{d+1}(-1)^k}{k-1}\binom d{k+1}.
\]
Lower derivatives agree. Every displayed jump is nonzero, proving the asserted sharp regularity classification.

## Verification

The standalone file `verification/volume_spline_verifier.py` uses only Python's standard library and exact rational arithmetic. Running `python3 verification/volume_spline_verifier.py` checks the compact expression against an **independently coded** integration of the positive-part simplex slices at 594 rational parameter points across dimensions 2 through 12. It also checks positivity and vanishing, near-threshold chamber identities, and direct distance-to-every-center membership in 5,404 coordinate test cases. One execution produced `PASS` with 6,905 diagnostic checks.

The proof above establishes the theorem for all integers \(d\ge2\) and all real \(t\ge0\). Finite diagnostic tests are supplementary, not a substitute for the integral identity or the polynomial argument.

## Relationship to prior work

Meyer (2026) studies when adding a dilated convex body makes a compact set convex, and proves general criteria in terms of exposed-set covering conditions. The present result specializes to the coordinate cross-polytope's vertices but **adds a complete all-dimensional missing-volume law and its exact regularity transitions**, not provided by those general criteria. Artstein-Avidan, Falah and Slomka (2024) introduce vertex-generated polytopes and the equivalent \(\lambda\)-parameter perspective; the convexification threshold itself is closely related to their general theory, so **no novelty is claimed merely for knowing when convexification eventually occurs**. The 2026 work of van Hintum concerns Hausdorff deficits of iterated Minkowski averages, a different operation and quantity. Related exact volume splines for Hadamard truncations and lattice octahedral covering concern different sets; matching spline form alone does not imply their formulas cover (or are covered by) this result.

## Limitations

This result does not address general polytopes, anisotropic translate radii, arbitrary centers, Euclidean Hausdorff distance, or full homotopy classification of holes. Historical priority of the volume formula is not conclusively established: specialized older formulas for unions of \(\ell_1\)-balls may use a different terminology and could be unindexed. No independent mathematical audit has been performed.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation* (first public preprint 2026-10-19), arXiv:2610.26744, https://arxiv.org/abs/2610.26744.
2. Shiri Artstein-Avidan, Tomer Falah, Boaz A. Slomka, *Vertex generated polytopes* (first public preprint 2024-07-30), arXiv:2407.20604, https://arxiv.org/abs/2407.20604.
3. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition* (2026-06-09), arXiv:2606.10815, https://arxiv.org/abs/2606.10815.
