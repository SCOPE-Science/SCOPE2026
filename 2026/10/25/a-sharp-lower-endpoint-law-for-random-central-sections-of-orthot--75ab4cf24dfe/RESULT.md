# A sharp lower-endpoint law for random central sections of orthotopes

## Finding

Let \(n\ge 3\) and let
\[
B=\prod_{i=1}^{n}[-a_i,a_i]\subset\mathbb R^n,
\qquad a_1>a_2\ge\cdots\ge a_n>0.
\]
Let \(H\) be a Haar-uniform hyperplane through the origin, and write
\[
D_H=\operatorname{diam}(B\cap H),\qquad
R_0=\left(\sum_{i=2}^{n}a_i^2\right)^{1/2},\qquad D_0=2R_0.
\]
Then \(D_0\) is the minimum possible central-section diameter, and the lower-tail probability has the exact endpoint asymptotic
\[
\boxed{
\mathbb P(D_H\le D_0+\varepsilon)
=\frac{2^{n-1}\Gamma(n/2)}{(n-1)!\,\pi^{n/2}}
\frac{\left(\sum_{i=2}^{n}a_i^2\right)^{(n-1)/4}}{\prod_{i=2}^{n}a_i}
\varepsilon^{(n-1)/2}\bigl(1+O_B(\varepsilon)\bigr)
}\]
as \(\varepsilon\downarrow0\). The leading coefficient is independent of the unique longest half-length \(a_1\); the assumption \(a_1>a_2\) creates the isolated minimizing orientation and a positive gap to all other edge directions.

## Assumptions and scope

The box is centered and has positive half-lengths ordered as above. Hyperplanes are sampled by choosing a uniform normal on \(S^{n-1}\); opposite normals represent the same hyperplane and give the same probability. The claim is for fixed \(B\) as \(\varepsilon\to0^+\), with the error constant allowed to depend on \(B\). It does not cover tied longest axes.

## Proof

Put \(R(H)=\max\{\|x\|_2:x\in B\cap H\}\). Since \(B\cap H\) is centrally symmetric, \(D_H=2R(H)\). For a generic hyperplane, each section vertex lies on a box edge. A vertex on an edge parallel to coordinate \(i\) has squared norm at least \(\sum_{j\ne i}a_j^2\), so
\[
R(H)^2\ge \min_i\sum_{j\ne i}a_j^2=R_0^2.
\]
The coordinate hyperplane \(H_0=\{x_1=0\}\) attains equality, proving the minimum \(D_0=2R_0\).

Let \(u=(u_1,\ldots,u_n)\) be a unit normal and set
\[
S(u)=\sum_{j=2}^{n}a_j|u_j|,\qquad \delta=a_1^2-a_2^2>0.
\]
Any section vertex on an edge parallel to coordinate \(i\ge2\) has squared norm at least
\[
\sum_{j\ne i}a_j^2\ge R_0^2+\delta.
\]
Consequently, for all sufficiently small \(\varepsilon>0\), the event \(D_H\le D_0+\varepsilon\) forces every section vertex onto an edge parallel to the first coordinate. This forces \(S(u)\le a_1|u_1|\): otherwise, holding the first coordinate at a fixed endpoint and flipping the signs of the remaining coordinates along a cube-edge path changes the sign of \(u\cdot x\), so some non-first-coordinate edge crosses \(H\).

When \(S(u)<a_1|u_1|\), every first-coordinate edge crosses \(H\), no other edge direction crosses it, and the largest absolute first coordinate of a section vertex is \(S(u)/|u_1|\). Therefore
\[
R(H)^2=R_0^2+\left(\frac{S(u)}{|u_1|}\right)^2.
\]
Conversely, the same identity and edge pattern hold whenever \(S(u)/|u_1|\) is sufficiently small. Since
\[
2\sqrt{R_0^2+t^2}\le 2R_0+\varepsilon
\quad\Longleftrightarrow\quad
 t\le \tau_\varepsilon:=\sqrt{R_0\varepsilon+\varepsilon^2/4},
\]
the small-tail event is exactly \(S(u)/|u_1|\le\tau_\varepsilon\) for sufficiently small \(\varepsilon\).

Use projective coordinates \(y_j=u_j/u_1\), \(2\le j\le n\), near each of the two poles \(\pm e_1\). In either chart, the spherical area element is
\[
(1+\|y\|_2^2)^{-n/2}\,dy,
\]
and the event becomes the weighted cross-polytope
\[
L_{\tau}=\left\{y\in\mathbb R^{n-1}:\sum_{j=2}^{n}a_j|y_j|\le\tau\right\},
\qquad \tau=\tau_\varepsilon.
\]
Its Euclidean volume is exactly
\[
\operatorname{Vol}_{n-1}(L_\tau)=
\frac{2^{n-1}\tau^{n-1}}{(n-1)!\prod_{j=2}^{n}a_j}.
\]
Throughout \(L_\tau\), one has \(\|y\|_2=O_B(\tau)\); hence the integral of the spherical density over this set equals its Euclidean volume times \(1+O_B(\tau^2)\). Both pole charts contribute equally. Dividing their combined area by \(|S^{n-1}|=2\pi^{n/2}/\Gamma(n/2)\) gives
\[
\mathbb P(D_H\le D_0+\varepsilon)
=\frac{2^{n-1}\Gamma(n/2)}{(n-1)!\pi^{n/2}\prod_{j=2}^{n}a_j}
\tau_\varepsilon^{n-1}\bigl(1+O_B(\tau_\varepsilon^2)\bigr).
\]
Finally, \(\tau_\varepsilon^{n-1}=R_0^{(n-1)/2}\varepsilon^{(n-1)/2}(1+O_B(\varepsilon))\) and \(\tau_\varepsilon^2=O_B(\varepsilon)\), which yields the stated formula.

## Verification

The proof reduces the local event to a weighted \(\ell_1\)-ball in a projective normal-coordinate chart; its volume is evaluated exactly. The standalone script `verify.py` uses rational arithmetic to check representative edge-intersection cases in dimension three, verifies the positive gap away from the dominant-edge cone, and checks the dimension-three simplification of the coefficient. These finite checks are consistency checks, not substitutes for the analytic proof.

## Relationship to prior work

The recent preprint *On random diameters of convex bodies* studies random-section diameters through high-probability bounds and applications to \(p\)-ellipsoids. The accessible abstract motivates the random-diameter question but does not state this exact lower-endpoint expansion. Other nearby results concern section vertex counts, section polygon type, random widths, or diameters of cross-polytope sections; those are different statistics or bodies and do not imply the displayed coefficient. The full text of the recent preprint was not available for direct comparison during this review, so this remains a stated literature risk rather than a claim that the paper has been exhaustively ruled out.

## Limitations

The result is local at the minimum and assumes a unique longest half-length. When two or more longest half-lengths tie, the minimizing normals are no longer isolated to a single antipodal pair and the leading coefficient/exponent may change. The formula does not give the full distribution of \(D_H\) away from \(D_0\). The closest recent paper's abstract was inspected, but its full text was not; an independent literature audit should revisit that comparison.

## References

1. O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, “On random diameters of convex bodies,” arXiv:2609.24131v1, first posted 2026-09-21. https://arxiv.org/abs/2609.24131.
2. G. Ambrus, “Critical central sections of the cube,” arXiv:2107.14778, 2021. https://arxiv.org/abs/2107.14778.
3. H. König and A. Koldobsky, “On the maximal perimeter of sections of the cube,” arXiv:1806.08659, 2018. https://arxiv.org/abs/1806.08659.
