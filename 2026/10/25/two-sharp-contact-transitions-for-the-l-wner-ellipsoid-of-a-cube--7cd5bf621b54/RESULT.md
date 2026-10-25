# Two sharp contact transitions for the Löwner ellipsoid of a cube with one axial spike

## Finding

Let \(d\ge2\) be an integer, let \(h>1\), and let
\[
C_d=[-1,1]^d,\qquad K_{d,h}=\operatorname{conv}\bigl(C_d\cup\{he_1\}\bigr)\subset\mathbb R^d.
\]
The unique least-volume ellipsoid containing \(K_{d,h}\), among all translated and rotated full-dimensional ellipsoids, is
\[
E_{d,h}=\left\{x:\frac{(x_1-c)^2}{a^2}+\sum_{j=2}^{d}\frac{x_j^2}{b^2}\le1\right\},
\]
with exactly the following three regimes:
\[
\boxed{\begin{array}{c|c|c|c}
\text{parameter}&c&a^2&b^2\\ \hline
1<h\le\sqrt d&0&d&d\\
\sqrt d\le h\le d&0&h^2&\dfrac{(d-1)h^2}{h^2-1}\\
h\ge d&\dfrac{h-d}{d+1}&\dfrac{d^2(h+1)^2}{(d+1)^2}&\dfrac{d^2}{d+1}
\end{array}}
\]
The entries match at the shared endpoints. Both thresholds are sharp. For \(1<h<\sqrt d\), the contact set is exactly the \(2^d\) cube vertices; at \(h=\sqrt d\) the apex joins them; for \(\sqrt d<h\le d\), the apex and all cube vertices contact; for \(h>d\), exactly the apex and the \(2^{d-1}\) vertices in the opposite face \(x_1=-1\) contact. At \(h=d\), the positive-face corners still touch but become inactive in a nonnegative optimality certificate.

The exact volume is
\[
\operatorname{vol}_d(E_{d,h})=\kappa_d a b^{d-1},\qquad
\kappa_d=\frac{\pi^{d/2}}{\Gamma(d/2+1)}.
\]
In particular, beyond the second threshold the transverse semiaxis \(b=d/\sqrt{d+1}\) is independent of \(h\), while the axial semiaxis grows linearly.

There is also a sharp dimension-scale volume transition. If \(h_d>1\) and \(h_d/\sqrt d\to\tau\in[0,\infty)\), then
\[
\lim_{d\to\infty}\frac{\operatorname{vol}_d(E_{d,h_d})}{\kappa_d d^{d/2}}
=\begin{cases}1,&0\le\tau\le1,\\
\tau\exp\!\bigl((\tau^{-2}-1)/2\bigr),&\tau>1.
\end{cases}
\]

## Assumptions and scope

All distances, volumes and orthogonality are Euclidean. The body is the convex hull of the standard cube and exactly one point on a coordinate axis at \(h>1\). The cube is full-dimensional for all stated dimensions, and the competing ellipsoids may have arbitrary centers and orientations. The semiaxes \(a,b\) are positive lengths, not inverse-quadratic coefficients. The asserted contact set means \(K_{d,h}\cap\partial E_{d,h}\), not the contact points with the supporting halfspaces of the polytope. No restriction to axially symmetric competitors is assumed in the optimality proof.

## Proof

**1. Construct a containing ellipsoid and classify equality.** Every point of \(K_{d,h}\) is a convex combination of the cube vertices \((\varepsilon_1,\ldots,\varepsilon_d)\), with \(\varepsilon_i\in\{-1,1\}\), and the apex \(he_1\). Since the displayed ellipsoid is convex, it suffices to check these finitely many points. For the first regime, the defining quadratic form is \(\|x\|_2^2/d\), which equals \(1\) on each cube vertex and equals \(h^2/d\le1\) at the apex. In the middle regime the corner value is exactly
\[
\frac1{h^2}+\frac{d-1}{b^2}=\frac1{h^2}+\frac{h^2-1}{h^2}=1,
\]
and the apex has value \(1\). In the last regime, \(a=h-c\) and
\[
\frac{(-1-c)^2}{a^2}=\frac1{d^2},\qquad
\frac{d-1}{b^2}=\frac{d^2-1}{d^2}.
\]
Thus the apex and all opposite-face corners attain equality. The corners with first coordinate \(+1\) have strictly smaller quadratic value when \(h>d\), because \(c>0\) implies \((1-c)^2<(1+c)^2\). The ellipsoid is strictly convex, so a nontrivial convex combination of distinct generating points cannot furnish another boundary contact. This proves containment and the complete asserted contact sets, including endpoint cases.

**2. Establish a global optimality lemma.** Suppose \(S\subseteq B_2^d\) contains unit vectors supporting a probability distribution \(\nu\) with
\[
\mathbb E_\nu Z=0,\qquad \mathbb E_\nu ZZ^{\mathsf T}=I_d/d.
\]
Every ellipsoid \(F=w+TB_2^d\), where \(T\) is symmetric positive definite, containing \(S\) satisfies
\[
1\ge\mathbb E_\nu\|T^{-1}(Z-w)\|_2^2
=\frac1d\operatorname{tr}(T^{-2})+w^{\mathsf T}T^{-2}w.
\]
Consequently \(\operatorname{tr}(T^{-2})\le d\); arithmetic–geometric mean for its positive eigenvalues yields \(\det(T)^{-2/d}\le\operatorname{tr}(T^{-2})/d\le1\), hence \(\det T\ge1\). Equality forces \(w=0\) and \(T=I_d\). Therefore the unit ball is the unique least-volume ellipsoid containing any body inside it that contains this isotropic contact distribution. An affine change of coordinates transfers the conclusion to any candidate ellipsoid.

**3. Produce the isotropic contact distribution in all regimes.** Work in original coordinates and write \(A=\operatorname{diag}(a,b,\ldots,b)\). It is enough to place probability on contact points \(X\) such that
\[
\mathbb E X=ce_1,\qquad
\operatorname{Cov}(X)=A^2/d;
\]
then \(Z=A^{-1}(X-ce_1)\) meets the lemma's hypotheses.

In the first regime, take the uniform distribution on all cube vertices. It has mean zero and covariance \(I_d=A^2/d\).

In the middle regime, give the apex probability
\[
\lambda=\frac{h^2-d}{d(h^2-1)}
\]
and give total probability \(1-\lambda\) to the cube vertices. Conditional on a cube vertex, make coordinates \(2,\ldots,d\) independent fair signs, and make the first-coordinate sign have mean \(-\beta\), where
\[
\beta=\frac{h^2-d}{(d-1)h}.
\]
The inequalities \(0\le\lambda<1\) and \(0\le\beta\le1\) hold exactly throughout \(\sqrt d\le h\le d\); the latter upper bound is equivalent to \((h-d)(h+1)\le0\). Directly,
\[
\lambda h-(1-\lambda)\beta=0,
\quad \lambda h^2+(1-\lambda)=\frac{h^2}{d},
\quad 1-\lambda=\frac{b^2}{d}.
\]
Every mixed covariance is zero, since the transverse signs are independent and centered. The mean and full covariance therefore have the required values.

In the last regime, give the apex weight \(1/(d+1)\) and uniformly distribute the remaining weight \(d/(d+1)\) among the opposite-face corners \((-1,\varepsilon_2,\ldots,\varepsilon_d)\). The first-coordinate mean and variance are
\[
\frac{h-d}{d+1}=c,\qquad
\frac{d(h+1)^2}{(d+1)^2}=\frac{a^2}{d},
\]
and each transverse variance equals \(d/(d+1)=b^2/d\), with all cross-covariances zero. Thus the same contact lemma proves global minimum volume and uniqueness in all three regimes. At the thresholds, the adjacent formulas coincide and at least one displayed distribution remains valid.

**4. The dimension-scale limit.** Divide the semiaxis volume product by \(d^{d/2}\). If \(h_d/\sqrt d\to\tau<1\), eventually the first regime applies and the ratio is \(1\). If \(\tau>1\), eventually the middle regime applies and the ratio is
\[
\frac{h_d}{\sqrt d}\left(\frac{1-d^{-1}}{1-h_d^{-2}}\right)^{(d-1)/2}
\longrightarrow\tau\exp\bigl((\tau^{-2}-1)/2\bigr).
\]
For \(\tau=1\), either branch gives limit \(1\), using the same expression when above the first threshold and continuity of its logarithm. These cases prove the limiting formula, including \(\tau=0\).

## Verification

The standalone standard-library script `verify.py` uses exact rational arithmetic for \(50{,}022\) dimension/parameter configurations through dimension \(100\). It checks every distinct corner-orbit containment value, apex containment, endpoint equality, screening, nonnegative weight ranges, and the exact first- and second-moment identities behind the global certificate. It also checks \(4{,}200\) independently sampled high-dimensional cube vertices numerically. Execute `python3 verify.py` in the extracted package directory. The expected report begins with `PASS exact rational configurations 50022`. These finite checks support but do not replace the universal proof above.

## Relationship to prior work

Güler and Gürtuna (2007) establish general John–Löwner contact and symmetry machinery and explicitly treat ellipsoid slabs, truncated second-order cones and cylinders. Their methods justify using isotropic contact measures, but their stated special bodies have spherical or ellipsoidal cross-sections, unlike a cube plus one axial exterior vertex; the two exact thresholds and opposite-face screening are not their listed formulas. A published treatment of John ellipsoids of **capped hypercubes** concerns a cube intersected with a diagonal halfspace, which is an intersection and inscribed-ellipsoid problem rather than the present convex-hull and circumscribed-ellipsoid problem. Published treatments of **isocanted cubes** and **rank-selected Boolean polytopes** supply other sharp Löwner contact-orbit transitions; their parameterized vertex sets do not contain a continuously moving exterior axial point. Standard minimum-volume-ellipsoid/optimal-design duality yields a general optimization formulation, not the explicit all-dimensional, two-threshold profile here.

## Limitations

The classification is for one point moving along an axis normal to a cube face. It does not address off-axis outliers, multiple outliers, weighted Euclidean metrics outside affine normalization, or general convex bodies. Historical priority in older optimal-design or computational-geometry literature cannot be conclusively established from the inspected sources. The rational verifier does not certify untested parameter values or infinite dimension ranges; those are covered only by the analytic argument.

## References

1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707v1, first public 2007-09-05; https://arxiv.org/abs/0709.0707 and https://optimization-online.org/2007/09/1771/ . Sections 2, 4, 6 and 8.
2. *Three-phase John ellipsoid of a capped hypercube*, published research record, 2026-10-11, identifier `9b8726b32127`.
3. *Parity-sharp Löwner contact transitions and pole avoidance for isocanted cubes*, published research record, 2026-10-11, identifier `c0498570052b`.
4. *Exact Löwner ellipsoids of arbitrary rank-selected Boolean polytopes*, published research record, 2026-10-11, identifier `3c04f47dc8c3`.
5. A. C. Atkinson, *Optimal Design*, Wiley StatsRef, published 2015; https://doi.org/10.1002/9781118445112.stat04090.pub2 . General D-optimality background only.
