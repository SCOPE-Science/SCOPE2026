# Exact Haar diameter law for central sections of the regular octahedron

## Finding

Let \(O=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\), and choose a two-dimensional linear subspace \(E\) with normalized Haar measure on the Grassmannian. Denote the Euclidean diameter of the central planar section by \(D(E)=\operatorname{diam}_2(O\cap E)\). Its distribution has support exactly \([\sqrt2,2]\) and has no atoms.

For \(0\le t\le1\), introduce the decreasing threshold
\[
d(t)=\frac{2\sqrt{1+t^2}}{1+t}
\]
and the explicitly positive expression
\[
\begin{aligned}
N(t)={}&\sqrt{3(1+2t^2)(2+t^2)}
 +(1+2t)\sqrt{2+t^2}\\
 &+\sqrt3(1+t+t^2)+(2+t)\sqrt{1+2t^2}.
\end{aligned}
\]
The exact distribution law is
\[
\boxed{\mathbb P\{D(E)\le d(t)\}=\frac{24}{\pi}\arctan\frac{(1-t)^2}{N(t)}\quad(0\le t\le1).}
\]
In particular, this formula gives the full cumulative distribution function. For \(\sqrt2\le d\le2\), set
\[
r=d/2,\qquad t(d)=\frac{1-r^2}{r^2+\sqrt{2r^2-1}}.
\]
Then \(\mathbb P\{D(E)\le d\}=24\pi^{-1}\arctan((1-t(d))^2/N(t(d)))\). The cumulative distribution is zero below \(\sqrt2\) and one above \(2\).

## Assumptions and scope

The octahedron is normalized to have vertices \(\pm e_1,\pm e_2,\pm e_3\), and Euclidean diameter uses the ambient Euclidean norm. The subspace is linear, passes through the origin, and is sampled by Haar probability rather than by a random affine offset. Its unoriented unit normal can be represented as a uniform vector \(n\) on \(S^2\). All probability statements refer to this distribution. The exact formula is restricted to this three-dimensional polytope and two-dimensional central sections; no higher-dimensional or arbitrary-body conclusion is asserted.

## Proof

**1. Reduction to a great-circle minimum.** The section \(O\cap E\) is centrally symmetric. On every ray with Euclidean-unit direction \(u\in E\cap S^2\), its radial extent equals \(\|u\|_1^{-1}\), where \(\|u\|_1=|u_1|+|u_2|+|u_3|\). Therefore
\[
D(E)=\frac2{\displaystyle\min_{u\in E\cap S^2}\|u\|_1}.
\]
Assume temporarily that all three coordinates of \(n\) are nonzero. The three coordinate great circles divide \(E\cap S^2\) into finitely many arcs on each of which the signs of the coordinates of \(u\) are fixed. On each open arc, \(\|u\|_1=\varepsilon\cdot u\) for a fixed sign vector \(\varepsilon\in\{\pm1\}^3\). As a function of the angle along that circle, this is a sinusoid. An interior critical point with positive value is necessarily its local maximum; the local minimum of a sinusoid is negative, whereas \(\|u\|_1>0\). Consequently the global minimum occurs when at least one coordinate of \(u\) is zero. Degenerate normals follow by continuity.

**2. Exact deterministic section diameter.** Suppose \(u_i=0\) and the other coordinate indices are \(j,k\). The equation \(n\cdot u=0\) forces \((u_j,u_k)\) to be parallel to \((n_k,-n_j)\). After Euclidean normalization, the reciprocal of \(\|u\|_1\) at this direction is
\[
\frac{\sqrt{n_j^2+n_k^2}}{|n_j|+|n_k|}.
\]
It follows that the section radius is the maximum of this expression over the three coordinate pairs. Write the ordered absolute normal coordinates as \(0\le a\le b\le c\), with \(c>0\). The function
\[
f(s)=\frac{\sqrt{1+s^2}}{1+s}\quad (0\le s\le1)
\]
has derivative \(f'(s)=(s-1)/((1+s)^2\sqrt{1+s^2})\le0\). The most unequal pair \((a,c)\) therefore maximizes the radius, and hence
\[
\boxed{D(E)=2\frac{\sqrt{a^2+c^2}}{a+c}=d(a/c).}
\]
The same formula remains valid for normals with zero or repeated absolute coordinates by continuity. Thus \(D(E)\in[\sqrt2,2]\), and both endpoints are limits of values on open sets of normals.

**3. The spherical event.** Put \(T=a/c\). The function \(d(t)\) is strictly decreasing for \(0\le t<1\), so
\[
\mathbb P\{D(E)\le d(t)\}=\mathbb P\{T\ge t\}.
\]
The absolute value of a uniform spherical normal is uniformly distributed on the positive octant, whose spherical area is \(\pi/2\). Divide that octant into the six congruent sectors determined by the six orderings of its three coordinates. In the sector \(0\le x\le y\le z\), the condition \(T\ge t\) becomes \(x\ge tz\). Its intersection with the unit sphere is precisely the geodesic triangle spanned by the three positive rays
\[
A=(1,1,1),\qquad B=(t,t,1),\qquad C=(t,1,1).
\]
The six sectors agree in spherical area and their boundaries have measure zero. If \(\Omega(t)\) is the solid angle of that one triangle, then \(\mathbb P\{T\ge t\}=6\Omega(t)/(\pi/2)=12\Omega(t)/\pi\).

**4. Exact evaluation of the solid angle.** The standard solid-angle identity for three rays \(U,V,W\) spanning a triangle on the unit sphere is
\[
\Omega=2\arctan\frac{|\det(U,V,W)|}{\|U\|_2\|V\|_2\|W\|_2+(U\cdot V)\|W\|_2+(V\cdot W)\|U\|_2+(W\cdot U)\|V\|_2},
\]
with the positive branch when all ray pairs make acute angles. This identity is the classical spherical-triangle solid-angle formula of van Oosterom and Strackee; it can also be checked by spherical excess and the spherical cosine rule. For our rays, direct calculation gives
\[
\begin{gathered}
|\det(A,B,C)|=(1-t)^2,\quad
\|A\|_2=\sqrt3,\quad\|B\|_2=\sqrt{1+2t^2},\quad\|C\|_2=\sqrt{2+t^2},\\
A\cdot B=1+2t,\quad B\cdot C=1+t+t^2,\quad C\cdot A=2+t.
\end{gathered}
\]
Substitution yields \(\Omega(t)=2\arctan((1-t)^2/N(t))\). The factor \(12/\pi\) from the six sectors proves the displayed probability law.

**5. Inversion and endpoints.** Solving \(r=\sqrt{1+t^2}/(1+t)\) for \(0\le t\le1\) gives \(t=(1-r^2)/(r^2+\sqrt{2r^2-1})\) whenever \(1/\sqrt2\le r\le1\). This establishes the stated cumulative distribution. The formula at \(t=0\) equals one, since the spherical region is the entire octant, while at \(t=1\) it equals zero, since only the eight body-diagonal normals remain. The normal sphere has no atoms, and level sets of the continuous coordinate ratio \(a/c\) have spherical area zero. Therefore the diameter law has no atoms, including at its endpoints.

## Verification

The standalone `verify.py` program uses only the Python standard library. It tests the exact coordinate-pair maximum for 215 nonzero integer triples by rational arithmetic, compares the spherical-triangle expression against an independent spherical-excess calculation, and compares the distribution against a second integral representation using independent half-normal order statistics:
\[
\mathbb P\{T\ge t\}=3\int_0^\infty\sqrt{\frac2\pi}\,e^{-z^2/2}\left[\operatorname{erf}\frac{z}{\sqrt2}-\operatorname{erf}\frac{tz}{\sqrt2}\right]^2\,dz.
\]
It additionally checks 22,000 Gaussian normal triples and compares 180,000 sampled normals to the predicted event probabilities. Reproduction: run `python3 verify.py` from the directory containing this file; successful completion prints `VERIFY_OK`. The universal theorem is proved by the preceding exact geometric argument; finite computations and numerical integration are supporting checks only.

## Relationship to prior work

Guédon, Litvak, Tatarko, and Vritsiou study random diameters of general convex bodies and provide nonasymptotic upper and lower bounds, including bounds for random sections of \(\ell_1\) balls. In the specialized three-dimensional Haar-plane case, the present identity supplies the complete probability distribution rather than bounds up to constants. Hmadi and Liakopoulos derive inequalities for the inradius of random projections of cubes and explain the polar relation between cube projections and cross-polytope sections. In the present normalization, polarity gives the equivalent formulation \(r(P_E[-1,1]^3)=1/(D(E)/2)\), but their published estimates do not determine this exact law. Gluskin and Ostrover discuss diameters of random octahedron sections in substantially different dimensions and a different Grassmannian model, without giving this finite three-dimensional cumulative distribution. The spherical solid-angle evaluation uses the established van Oosterom–Strackee identity.

The inradius of the projection of the *octahedron* is a different statistic: its polar is a *cube section*. The present statistic is the diameter of an *octahedron section*, equivalently the reciprocal inradius of a *cube projection*. Interchanging section and projection and interchanging cube and octahedron are not innocuous, and neither statistic alone determines the other.

## Limitations

No claim is made about noncentral affine sections, higher-dimensional sections, arbitrary weights on the coordinates, or other distributions of orientations. The cited literature supplies mathematical motivation and comparisons, not external validation of this specific distribution. An equivalent elementary formula may be present in unindexed geometric-probability or coordinate-ratio literature. The independent mathematical audit remains unperformed.

## References

- O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On random diameters of convex bodies*, arXiv:2609.24131v1 (first posted September 21, 2026), especially introduction and Section 3. https://arxiv.org/pdf/2609.24131
- A. Hmadi and D.-M. Liakopoulos, *Negative moments of the support function and applications to isotropic convex bodies*, arXiv:2609.27757v1, especially Theorem 1.3, Section 3, and Appendix A. https://arxiv.org/html/2609.27757v1
- E. D. Gluskin and Y. Ostrover, *A remark on projections of the rotated cube to complex lines*, arXiv:1604.04927v1 (2016), especially Theorem 1.1 and Remark 1.3. https://arxiv.org/pdf/1604.04927
- A. van Oosterom and J. Strackee, *The solid angle of a plane triangle*, IEEE Transactions on Biomedical Engineering 30(2) (1983), 125–126. DOI: 10.1109/TBME.1983.325207.
