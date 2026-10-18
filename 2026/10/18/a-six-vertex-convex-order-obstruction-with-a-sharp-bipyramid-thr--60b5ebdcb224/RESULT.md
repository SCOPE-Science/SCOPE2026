# A six-vertex convex-order obstruction with a sharp bipyramid threshold

## Finding

A rectangular bipyramid in \(\mathbb R^3\) with just six vertices can have **smaller surface-average than volume-average for a convex function**, even though the respective centroids coincide. In the explicit family below, the convex quadratic \(f(x,y,z)=x^2\) reverses the usual Jensen-type volume-to-boundary comparison precisely for \(t>\sqrt{161}\). The vertex count is globally minimal among centrally symmetric three-dimensional polytopes.

## Assumptions and scope

For each real \(t>0\), set
\[
K_t=\operatorname{conv}\{(\pm t,0,\pm1),(0,\pm t,0)\}.
\]
Here the first displayed set consists of the four independent sign choices; the second comprises two points. This is a nondegenerate rectangular bipyramid, with the rectangle in the plane \(y=0\) and two apices on the \(y\)-axis. Let \(X_t\) be uniform with respect to three-dimensional Lebesgue volume and let \(Y_t\) be uniform with respect to two-dimensional Euclidean Hausdorff surface measure. Central symmetry gives \(\mathbb E X_t=\mathbb E Y_t=0\). The fixed convex function is \(f(x,y,z)=x^2\).

We make no assertion that every convex function reverses the inequality: one convex quadratic suffices to disprove convex-order dominance.

## Proof

**Volume mean.** A slice with \(y=\pm ts\), where \(0\le s\le1\), is the rectangle \(|x|\le t(1-s)\), \(|z|\le1-s\). Its area is \(4t(1-s)^2\). On that rectangle the conditional expectation of \(x^2\) is \(t^2(1-s)^2/3\). Integrating over the two signs yields
\[
\mathbb E f(X_t)=\frac{t^2}{3}\frac{\int_0^1(1-s)^4\,ds}{\int_0^1(1-s)^2\,ds}=\frac{t^2}{5}.
\]

**Surface mean.** The bipyramid has eight triangular faces. Four lie over the two base edges parallel to the \(x\)-axis; each has area \(t\sqrt{t^2+1}\). Their three \(x\)-coordinates at the vertices are \(-t,t,0\), so their face-average of \(x^2\) is \(t^2/6\). Four lie over base edges parallel to the \(z\)-axis; each has area \(t\sqrt2\). Their three \(x\)-coordinates are either \(t,t,0\) or \(-t,-t,0\), giving face-average \(t^2/2\). These averages follow from the standard barycentric second moments on a triangle: if the vertex values of an affine scalar coordinate are \(a,b,c\), its squared mean is \(((a+b+c)^2+a^2+b^2+c^2)/12\).

Area weighting now yields
\[
\mathbb E f(Y_t)
=\frac{4t\sqrt{t^2+1}\,(t^2/6)+4t\sqrt2\,(t^2/2)}{4t\sqrt{t^2+1}+4t\sqrt2}
=\frac{t^2(\sqrt{t^2+1}+3\sqrt2)}{6(\sqrt{t^2+1}+\sqrt2)}.
\]
Subtracting the volume mean gives the exact identity
\[
\mathbb E f(Y_t)-\mathbb E f(X_t)=
\frac{t^2(9\sqrt2-\sqrt{t^2+1})}{30(\sqrt{t^2+1}+\sqrt2)}.
\]
The denominator is strictly positive. Its numerator is negative exactly when \(\sqrt{t^2+1}>9\sqrt2\), or equivalently \(t^2>161\). Equality occurs at \(t=\sqrt{161}\). In particular, the six vertices of \(K_{13}\) have integer coordinates and yield a strict reversal.

**Sharp vertex complexity.** Every full-dimensional centrally symmetric three-dimensional polytope has at least three linearly independent antipodal vertex pairs, hence at least six vertices. Each \(K_t\) has precisely six vertices and full dimension. The lower bound is therefore attained by the obstruction above, so the vertex count is smallest possible in the centrally symmetric polytope class.

## Verification

The formulas were independently checked by direct triangular-face integration and volume-slice integration. Numerical evaluation gives \(\mathbb E f(Y_{13})=33.67898021143848\), while \(\mathbb E f(X_{13})=33.8\). The signed difference is about \(-0.12101978856\). Substituting \(t=\sqrt{161}\) into the exact expression gives zero, and substituting \(t=12\) gives a positive value. Finite numeric checks corroborate but do not replace the all-parameter algebraic proof.

## Relationship to prior work

Pasteczka's *Jensen-type geometric shapes* (2018) formulates the comparison between uniform volume and uniform boundary integrals for every convex function, emphasizes equality of their centroids as a necessary condition, and establishes positive cases including parallelotopes and certain tangential polytopes. Tokmachev (2026) proves convex-order domination for planar bodies with coincident centroids and for circumscribed polytopes whose insphere center equals both centroids. These theorems do **not** cover this three-dimensional, non-tangential bipyramid family. Shen (2026) studies counterexamples in a different mean-distance problem and gives a separate, nonsymmetric six-vertex-type construction. Lotnikov (2026) proves that pairwise mean-distance inequalities can fail for centrally symmetric bodies in dimensions at least three; that broader existence result means no first-counterexample claim is made here. The present statement instead supplies a transparent quadratic witness, a globally minimum symmetric vertex count, and an exact transition in one fixed explicit family.

## Limitations

The threshold is for the fixed family \(K_t\) and the one chosen convex function \(x^2\); it is **not** a classification of all six-vertex polytopes or of all convex functions. Some related 2026 full texts could only be inspected in part or through their explicit abstracts, leaving residual priority risk. This is an internally checked proof, not an independently audited or externally certified result.

## References

1. P. Pasteczka, *Jensen-type geometric shapes*, arXiv:1804.03688 (2018).
2. A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1 (first public 2026-07-09).
3. E. Shen, *Zaporozhets-Tarasov Conjecture on Mean Distances*, arXiv:2608.06470v1 (2026).
4. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848v1 (2026).
5. S. Steinerberger, *The Hermite-Hadamard Inequality in Higher Dimensions*, arXiv:1808.07794 (2018).
