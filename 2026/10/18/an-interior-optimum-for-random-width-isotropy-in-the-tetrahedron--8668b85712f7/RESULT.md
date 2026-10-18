# An interior optimum for random-width isotropy in the tetrahedron–octahedron truncation family

## Finding
Let \(T\) be the regular tetrahedron with vertices \(v_0=(1,1,1)\), \(v_1=(1,-1,-1)\), \(v_2=(-1,1,-1)\), \(v_3=(-1,-1,1)\). For every \(0\le t\le1/2\), form its equal edge truncation
\[
K_t=\operatorname{conv}\{(1-t)v_i+t v_j:0\le i,j\le3,\ i\ne j\}.
\]
At \(t=0\) this is \(T\), at \(t=1/3\) the regular truncated tetrahedron, and at \(t=1/2\) a regular octahedron. For a uniformly distributed \(U\in\mathbb S^2\), let \(W_t(U)\) be the Euclidean width of \(K_t\) in direction \(U\). Its scale-invariant squared coefficient of variation is
\[
\mathcal R(t)=\frac{\operatorname{Var}(W_t(U))}{(\mathbb E W_t(U))^2}.
\]
The unique minimizer of \(\mathcal R\) on the entire interval is an interior, non-Archimedean truncation \(t_*\). Write \(c=1-2t\),
\[
\alpha=\frac{3\sqrt2}{\pi}\arctan\frac1{\sqrt2},\qquad
\beta=\frac3{\sqrt2}-2\alpha,
\]
\[
A=\frac13+\frac2{\pi\sqrt3},\quad B=\frac2{\pi\sqrt3},\quad
C=\frac13+\frac2\pi-\frac4{\pi\sqrt3}.
\]
Then, for all \(t\in[0,1/2]\),
\[
\boxed{\mathcal R(t)=\frac{A+2Bc+Cc^2}{(\alpha+\beta c)^2}-1},\qquad
\boxed{t_*=\frac12\left(1-\frac{\beta A-\alpha B}{\alpha C-\beta B}\right)}.
\]
In particular \(0.195313965128<t_*<0.195313965398\), whereas the regular truncated tetrahedron occurs at \(t=1/3\). The minimum of \(\mathcal R\) is approximately \(0.001657728216\). The mean and second moment of width are, exactly,
\[
\mathbb EW_t=2(\alpha+\beta c),\qquad
\mathbb EW_t^2=4(A+2Bc+Cc^2).
\]
There is also an independent sharp transition in the minimum directional width:
\[
\min_{\|u\|=1}W_t(u)=2\min\left\{1,\frac{2-2t}{\sqrt3}\right\},
\quad
\max_{\|u\|=1}W_t(u)=2\sqrt{1+(1-2t)^2}.
\]
The minimizing directions switch from coordinate axes to body diagonals at \(t=(2-\sqrt3)/2\); at the transition both classes minimize.

## Assumptions and scope
All widths are lengths of one-dimensional orthogonal projections. The random direction has the rotation-invariant probability law on \(\mathbb S^2\); no shape scaling is assumed, since the coefficient of variation is invariant under positive homotheties. The initial four vertices are specified exactly. The truncation parameter ranges over the *entire closed interval* \([0,1/2]\), including both degenerate-to-a-vertex-set endpoints of the displayed vertex formula. Here \(\mathbb E W_t^2\) means \(\mathbb E[(W_t)^2]\), not \((\mathbb EW_t)^2\).

## Proof
**1. Exact directional identity.** For a unit vector \(u\), set \(M\ge m\ge s\ge0\) to be the decreasing rearrangement of \((|u_1|,|u_2|,|u_3|)\). The width of a tetrahedron is invariant under the tetrahedral orthogonal group and sign reversal of the direction, hence under all coordinate sign changes and permutations. We can assume \(u=(M,m,s)\). The four dot products \(d_i=\langle u,v_i\rangle\) are then ordered
\[
M+m+s\ge M-m-s\ge -M+m-s\ge -M-m+s.
\]
Because \(0\le t\le 1/2\), maximizing \((1-t)d_i+td_j\) over distinct indices chooses the largest two \(d_i\) in this order; minimizing chooses the smallest two. Thus
\[
W_t(u)=(1-t)(d_{(1)}-d_{(4)})+t(d_{(2)}-d_{(3)})
=\boxed{2\bigl(M+(1-2t)m\bigr)}.
\]
This identity includes all coincident-dot-product and endpoint cases by continuity.

**2. Five spherical order-statistic moments.** Set \(\alpha=\mathbb EM\), \(\beta=\mathbb Em\), \(A=\mathbb EM^2\), \(B=\mathbb E(Mm)\), \(C=\mathbb Em^2\). By the 48 congruent ordered signed-coordinate chambers, one chamber has the spherical parametrization
\[
u=(\cos\theta,\sin\theta\cos\phi,\sin\theta\sin\phi),\quad
0\le\phi\le\frac\pi4,\quad 0\le\theta\le\theta_0(\phi)=\arctan(\sec\phi).
\]
The expectation is \(12/\pi\) times integration against \(\sin\theta\,d\theta\,d\phi\) on that chamber. In particular,
\[
\alpha=\frac6\pi\int_0^{\pi/4}\frac{d\phi}{1+\cos^2\phi}
=\frac{3\sqrt2}{\pi}\arctan\frac1{\sqrt2},
\]
\[
B=\frac4\pi\int_0^{\pi/4}\frac{\cos\phi\,d\phi}{(1+\cos^2\phi)^{3/2}}=\frac2{\pi\sqrt3},
\]
\[
A=\frac4\pi\int_0^{\pi/4}\left[1-\frac{\cos^3\phi}{(1+\cos^2\phi)^{3/2}}\right]d\phi
=\frac13+\frac2{\pi\sqrt3}.
\]
Similarly, elementary integration of the other two chamber moments gives
\[
\beta=\frac6\pi\int_0^{\pi/4}\cos\phi
\left(\theta_0-\frac{\cos\phi}{1+\cos^2\phi}\right)d\phi
=\frac3{\sqrt2}-2\alpha,
\]
\[
C=\frac{12}\pi\int_0^{\pi/4}\cos^2\phi
\left(\frac23-\frac{\cos\phi}{\sqrt{1+\cos^2\phi}}
+\frac{\cos^3\phi}{3(1+\cos^2\phi)^{3/2}}\right)d\phi
=\frac13+\frac2\pi-\frac4{\pi\sqrt3}.
\]
For verification of the last two elementary evaluations, put \(z=\sin\phi\) and use \(\theta_0=\arctan(1/\sqrt{1-z^2})\). The integrals reduce to primitives of \((2-z^2)^{-1/2}\), \((2-z^2)^{-3/2}\), and \((2-z^2)^{1/2}\), evaluated at \(0\) and \(1/\sqrt2\). This supplies the stated five exact moments without statistical approximation.

**3. Unique coefficient-of-variation minimum.** Applying the pointwise identity and moments gives the displayed \(\mathcal R\). Differentiation yields
\[
\frac{d\mathcal R}{dc}=
\frac{2\{(\alpha B-\beta A)+(\alpha C-\beta B)c\}}
{(\alpha+\beta c)^3}.
\]
Write \(D=\alpha C-\beta B\) and \(E=\beta A-\alpha B\). Both are strictly positive, as is \(D-E\); exact rational interval bounds, using Machin's formula for \(\pi\), integer square-root enclosures, and alternating arctangent series, certify
\[
0.026518167598<D<0.026518167605,\quad
0.016159430665<E<0.016159430675,\quad
0.010358736923<D-E<0.010358736940.
\]
Consequently \(d\mathcal R/dc\) has a single sign change from negative to positive at \(c_*=E/D\in(0,1)\), proving unique global minimization. Since \(c=1-2t\) is a bijection from \([0,1/2]\) to \([1,0]\), this proves the asserted \(t_*\). The rational enclosure checker included with this note independently verifies all three strict signs and gives the stated certified bounds on \(t_*\).

**4. Exact directional extrema.** For ordered \(M\ge m\ge s\ge0\) on the unit sphere, Cauchy–Schwarz gives \(M+cm\le\sqrt{1+c^2}\), with equality at the ordered direction proportional to \((1,c,0)\), proving the maximum. On the spherical triangle of ordered nonnegative triples the positive linear functional \(M+cm\) cannot attain a minimum in an open geodesic arc: normalized chord interpolation strictly increases the value above the smaller endpoint value. Thus it is minimized at one of the triangle's vertices \((1,0,0)\), \((1,1,0)/\sqrt2\), or \((1,1,1)/\sqrt3\). Their values are \(1\), \((1+c)/\sqrt2\), and \((1+c)/\sqrt3\). The middle never minimizes; the other two exchange order at \(c=\sqrt3-1\). Positive signs/permutations yield all equality directions, with the endpoint equalities interpreted in the evident limiting sense.

## Verification
The included self-contained Python checker `verify_truncation_width.py` reruns exact rational enclosures for all three strict signs in the minimizer proof; it independently enumerates all twelve vertices for 18,000 random direction/truncation pairs; numerically integrates the five spherical chamber moments; compares global extremum formulas against 40,000 independently enumerated directions; and tests a grid of 10,001 coefficient-of-variation values. The exact analytical derivation, not finite sampling, proves the identity and all-parameter extremum. As a further cross-check, at \(t=0\) the mean-square width divided by the tetrahedron's squared side length \(8\) is exactly
\[
\frac{A+2B+C}{2}=\frac13+\frac{3+\sqrt3}{3\pi},
\]
matching the regular tetrahedron's mean-square width reported by Finch (2011).

## Relationship to prior work
The tetrahedron-to-octahedron equal-truncation family is the object considered in Damasceno, Engel, and Glotzer (2011) for hard-particle assembly and packing. Finch (2011) explicitly evaluates the mean-square width of the untruncated regular tetrahedron, agreeing with the endpoint of the present formula. Kabluchko, Litvak, and Zaporozhets (2015) establish width moments and probabilistic equivalences for regular simplices, cubes, and crosspolytopes. Those endpoint and generic tools do not themselves state the mixed ordered-coordinate moment \(\mathbb E(Mm)\), the full one-parameter truncated family profile, or its unique interior coefficient-of-variation optimum. This is a claim-specific distinction, not a declaration of exhaustive historical priority.

## Limitations
The extremal claim concerns exactly the displayed equal-edge truncations and **squared coefficient of variation** of *one-dimensional directional width* under uniform rotations. It is not a theorem for all tetrahedral perturbations, arbitrary polyhedra, area/perimeter of shadows, random affine sections, or anisotropic directional laws. The published truncation-family paper was accessible only through its abstract; unnoticed full-text work remains a specific priority risk. The scientific and arithmetic checks are not independent external validation.

## References
- P. F. Damasceno, M. Engel, and S. C. Glotzer, *Crystalline Assemblies and Densest Packings of a Family of Truncated Tetrahedra and the Role of Directional Entropic Forces*, arXiv:1109.1323, initial version 6 September 2011, https://arxiv.org/abs/1109.1323.
- S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, initial version 4 October 2011, https://arxiv.org/abs/1110.0671.
- Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, initial version 26 November 2015, https://arxiv.org/abs/1511.08479.
