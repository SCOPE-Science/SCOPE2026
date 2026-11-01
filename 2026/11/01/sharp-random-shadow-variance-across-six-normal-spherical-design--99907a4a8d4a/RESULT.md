# Sharp random-shadow variance across six-normal spherical-design polytopes

## Finding

Let \(X=\{x_1,\ldots,x_6\}\subset\mathbb S^2\) be six **distinct** nodes forming an equal-weight spherical \(2\)-design. Associate the convex polyhedron \(P_X\) having outward normals \(x_i\) and six facet areas \(2\pi/3\). Define its brightness in a unit viewing direction \(v\) by \(B_X(v)=\operatorname{area}_2(\operatorname{proj}_{v^\perp}P_X)\). For \(V\) uniformly distributed on the sphere, \(\mathbb EB_X(V)=\pi\).

Every such six-normal design is congruent, up to permutation, to exactly one family member with twist angle \(0\le\phi\le\pi/3\):
\[
 x_j^+=(\sqrt{2/3}\cos(2\pi j/3),\sqrt{2/3}\sin(2\pi j/3),1/\sqrt3),
 \quad x_j^-=(\sqrt{2/3}\cos(\phi+2\pi j/3),\sqrt{2/3}\sin(\phi+2\pi j/3),-1/\sqrt3),
\quad j=0,1,2.
\]
Put \(t_j(\phi)=[2\cos(\phi+2\pi j/3)-1]/3\) and \(H(t)=\sqrt{1-t^2}+t\arcsin(t)\). Then the **exact** variance of the random planar shadow area is
\[
 \boxed{\operatorname{Var}[B_X(V)]
 =\frac{\pi}{9}\left(8+4\sum_{j=0}^{2}H(t_j(\phi))-7\pi\right).}
\]
This is strictly increasing on \([0,\pi/3]\). Its sharp range is
\[
 \boxed{\frac{\pi}{9}\left[8+\frac43\left(2\sqrt2+2\sqrt5+\arcsin(1/3)+4\arcsin(2/3)\right)-7\pi\right]
 \le \operatorname{Var}[B_X(V)]\le \frac{\pi}{9}(16-5\pi).}
\]
The bounds are approximately \(0.030694143418\) and \(0.101940050221\). Equality on the left occurs only for \(\phi=0\), the aligned two-triangle normal design (whose Minkowski realization is a triangular bipyramid). Equality on the right occurs only for \(\phi=\pi/3\), when the six normals form three opposite pairs and the Minkowski polyhedron is a cube. Congruence and translation do not affect the shadow variance.

## Assumptions and scope

A six-node spherical \(2\)-design is equivalent to the exact identities \(\sum_{i=1}^6x_i=0\) and \(\sum_{i=1}^6x_ix_i^T=2I_3\). These conditions imply that the positive discrete measure \(\frac{2\pi}{3}\sum_i\delta_{x_i}\) has zero first moment and nondegenerate three-dimensional support, hence it is the surface-area measure of a unique convex body up to translation by Minkowski's theorem. Each node is distinct, so its surface-area atom corresponds to one facet. The variances use normalized Haar probability on \(\mathbb S^2\), and the measured shadow is ordinary Euclidean area. No arbitrary scaling is allowed: each facet has area \(2\pi/3\), giving total surface area \(4\pi\).

## Proof

**1. Six-node classification.** Let \(U\) be the \(6\times3\) matrix with rows \(x_i\). The design equations read \(U^TU=2I_3\) and \(U^T\mathbf1=0\). Consequently
\[
 Q=I_6-\tfrac12UU^T-\tfrac16\mathbf1\mathbf1^T
\]
is an orthogonal rank-two projection, with all six diagonal entries equal to \(1/3\). Choose a real \(6\times2\) matrix \(W\) with \(WW^T=Q\) and \(W^TW=I_2\). Its rows have equal length \(1/\sqrt3\), so the complex numbers \(z_i=\sqrt3(W_{i1}+\mathrm iW_{i2})\) have modulus one. Orthogonality to \(\mathbf1\) gives \(\sum_i z_i=0\), while \(W^TW=I_2\) gives \(\sum_i z_i^2=0\). The first two elementary symmetric coefficients of the monic polynomial with roots \(z_i\) therefore vanish. Because all roots are on the unit circle, the reciprocal-conjugate identity forces the next-to-highest and next-to-next-to-highest coefficients to vanish too. Thus the polynomial has the form \(z^6-cz^3+d\); its multiset of roots consists of two equilateral triples, including possible repeated roots.

For indices belonging to either triple, the rows of \(W\) make mutual angles \(2\pi/3\). Since \(\tfrac12UU^T=I_6-Q-\tfrac16\mathbf1\mathbf1^T\), the corresponding original three rows of \(U\) are mutually orthogonal unit vectors. The two triples of original rows have sums that are equal and opposite (by \(U^T\mathbf1=0\)). Each sum has norm \(\sqrt3\). Taking their normalized first sum as the vertical axis makes every upper vector have vertical coordinate \(1/\sqrt3\), every lower vector \(-1/\sqrt3\), and both horizontal triples equilateral at radius \(\sqrt{2/3}\). Relabeling and an orthogonal symmetry put the relative rotation in \([0,\pi/3]\). This proves the canonical family without assuming that it is combinatorially a cube at an endpoint.

**2. Projection-area covariance.** Cauchy's projection formula applied to these equal-area facets is
\[
 B_X(v)=\frac12\sum_{i=1}^6\frac{2\pi}{3}|x_i\cdot v|=\frac\pi3\sum_{i=1}^6|x_i\cdot v|.
\]
For fixed unit \(x\), \(\mathbb E|x\cdot V|=1/2\). For unit \(x,y\) with \(x\cdot y=t\), spherical polar integration in their span gives the elementary exact integral
\[
 \mathbb E[|x\cdot V|\,|y\cdot V|]
 =\frac{2}{3\pi}\left(\sqrt{1-t^2}+t\arcsin t\right)=\frac{2}{3\pi}H(t).
\]
There are six within-triple unordered pairs, each with \(t=0\), and nine cross-triple unordered pairs, with each of the three distinct dot products \(t_0,t_1,t_2\) repeated three times. Expanding the square of the brightness formula, using \(\mathbb E(x\cdot V)^2=1/3\) and subtracting \(\pi^2\), produces the stated exact variance.

**3. Strict monotonicity.** Put \(s_j=t_j^2\) and \(h(s)=H(\sqrt{s})\) for \(0\le s\le1\). The function \(H\) is even and differentiable, with \(H'(t)=\arcsin t\). For \(0<s<1\), direct differentiation yields
\[
 h''(s)=\frac{\sqrt{s}/\sqrt{1-s}-\arcsin\sqrt{s}}{4s^{3/2}}>0.
\]
The strict sign follows because \(g(t)=t/\sqrt{1-t^2}-\arcsin(t)\) vanishes at zero and has derivative \(g'(t)=t^2/(1-t^2)^{3/2}>0\) for \(0<t<1\).

For \(0<\phi<\pi/3\), the following strict inequalities hold:
\[
 -t_1>-t_2>t_0>0,\qquad t_0^2+t_1^2+t_2^2=1.
\]
The square \(t_1^2\) strictly increases with \(\phi\); \(t_0^2\) strictly decreases. Hence the sorted vector \((t_1^2,t_2^2,t_0^2)\) strictly increases in the majorization preorder: its largest coordinate, and the sum of its two largest coordinates, both increase, while the total remains one. Strict convexity of \(h\) and Karamata's inequality show that \(\sum_jh(t_j^2)\), and therefore the variance, strictly increase. Continuity includes both endpoints.

**4. Endpoints.** At \(\phi=0\), the cross-dot products are \((1/3,-2/3,-2/3)\). At \(\phi=\pi/3\), they are \((0,-1,0)\). Substitution into \(H\) yields precisely the displayed constants. Strict monotonicity and the canonical parameter classification give both equality characterizations.

## Verification

The accompanying self-contained file `verify_brightness.py` recomputes the dot products, first and second design moments, and endpoint constants; uses independent spherical midpoint quadrature to compare the predicted variance at five twists; and checks the relevant parameter ordering on 299 interior points. Execute with `python3 verify_brightness.py` (Python standard library only). Its successful execution printed `PASS` and the numerical endpoints above. Numerical quadrature is **not** a proof of the continuum monotonicity; that step is the strict-convexity and majorization argument in the preceding section.

## Relationship to prior work

Congpei An's *Minkowski Polytopes of Spherical Designs* (arXiv:2608.11570, first submitted 2026-08-12) establishes the equal-area Minkowski realization for general spherical designs, surface tensor exactness, and bounds for brightness as a function of design strength; it does not determine the present exact six-normal orientation variance or its sharp dependence on the twist parameter. An's *Exact Finite Integral Geometry* (arXiv:2609.05869) supplies a general theory of directional cosine kernels, but not this extremal six-normal variance classification. Previously recorded calculations give the one-parameter classification and volume of the six-normal Minkowski family; they do not give this orientation-variance functional or its extrema. A published mathematical record gives exact random-shadow variances for the individual Platonic solids, thus in particular the cube endpoint, which is **not** separately claimed here. The novel assertion is the complete sharp variance envelope over **all** six-node spherical \(2\)-design Minkowski polytopes, including a strict order along the entire family and the non-Platonic minimizing shape.

## Limitations

The theorem does not cover unequal facet areas, more than six design nodes, higher ambient dimensions, or other random projection statistics. The classification of six-node designs and the cube endpoint overlap existing literature; the contribution is the specific complete brightness-variance extremal theorem. Historical works not fully accessible might contain an equivalent calculation, so mathematical-priority claims remain open to independent scrutiny. No independently audited verification is represented.

## References

- Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570 (first submitted 2026-08-12), https://arxiv.org/abs/2608.11570.
- Congpei An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869 (submitted 2026-09-05), https://arxiv.org/abs/2609.05869.
- *Exact orientation-variance spectrum of Platonic shadow areas*, published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-orientation-variance-spectrum-of-platonic-shadow-areas--76ed33fc3859.
- Classical Cauchy projection formula, Minkowski surface-area-measure existence theorem, and strict Karamata inequality (standard background).
