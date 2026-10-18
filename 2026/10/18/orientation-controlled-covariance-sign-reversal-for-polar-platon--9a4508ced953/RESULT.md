# Orientation-controlled covariance sign reversal for polar Platonic widths

## Finding
Let \(Q=[-1,1]^3\), \(O_0=\operatorname{conv}\{\pm e_i:1\le i\le3\}\), and \(O_1=\operatorname{conv}\{\pm r_i:1\le i\le3\}\), where
\[
r_1=(2,-1,2)/3,\qquad r_2=(2,2,-1)/3,\qquad r_3=(-1,2,2)/3.
\]
The three \(r_i\) are orthonormal and positively oriented; this is a rotation by \(60^\circ\) around the body diagonal \((1,1,1)\). For a Haar-uniform \(U\in S^2\), use the *same* direction \(U\) to evaluate each pair of widths, where \(w_K(u)=h_K(u)+h_K(-u)\). Put \(\theta=\arctan(1/(2\sqrt2))=\arccos(2\sqrt2/3)\). Then
\[
\operatorname{Cov}(w_Q(U),w_{O_0}(U))
=\frac43-\frac{9\sqrt2}{2}+\frac{\sqrt2(8+9\theta)}\pi
=-0.05253921785439\ldots<0,
\]
whereas
\[
\operatorname{Cov}(w_Q(U),w_{O_1}(U))
=\frac{22}9-\frac{9\sqrt2}2+
\frac{8+4\sqrt2/3+(9\sqrt2-16/3)\theta}{\pi}
=0.02707153969993\ldots>0.
\]
Thus a natural, fixed \(60^\circ\) relative rotation reverses the sign of same-direction width covariance between polar Platonic solids.

## Assumptions and scope
The width convention gives \(w_Q(u)=2\sum_{i=1}^3|u_i|\) and \(w_{O_j}(u)=2\max_k|r_k^{(j)}\cdot u|\), with \(r_k^{(0)}=e_k\). Haar means normalized spherical area \(d\omega/(4\pi)\), not independent normals for the two widths. The displayed signs concern precisely the aligned and specified rotated octahedra, not all relative rotations. Scaling either body by a positive factor scales both covariances by its product with the other scale and does not change their signs.

## Proof
Write \(S(u)=\sum_i|u_i|\), \(M_0(u)=\max_i|u_i|\), and \(M_1(u)=\max_i|r_i\cdot u|\). The covariances equal \(4\operatorname{Cov}(S(U),M_j(U))\). Direct marginal spherical integration and the classical octahedral mean-width calculation yield
\[
\mathbb ES=\frac32,\qquad
\mathbb EM_0=\mathbb EM_1=\frac{3\sqrt2}{2\pi}\arccos(1/3)
=\frac{3\sqrt2}{2\pi}(\pi/2-\theta).
\]
For aligned axes, partition the sphere into signed octants and the six choices of maximizing absolute coordinate. The chart \(u=(1,p,q)/\sqrt{1+p^2+q^2}\), \(0\le p,q\le1\), has spherical Jacobian \((1+p^2+q^2)^{-3/2}\). Hence
\[
\mathbb E(SM_0)=\frac6\pi\int_0^1\!\int_0^1
\frac{1+p+q}{(1+p^2+q^2)^{5/2}}\,dp\,dq
=\frac13+\frac{2\sqrt2}\pi.
\]
Here the elementary integrals of the constant and \(p\) terms are, respectively, \(\pi/18+1/(3\sqrt3)\) and \(1/(3\sqrt2)-1/(6\sqrt3)\), with the \(q\) term equal to the latter by symmetry.

For the rotated axes, form the spherical chambers defined by the eight sign orthants of \(u\) and the six signed candidate winners \(\pm r_j\). Each chamber is the intersection of the halfspaces \(\sigma_i u_i\ge0\) and \((t r_j\mp r_k)\cdot u\ge0\) for every \(k\). Their boundary rays are cross products of the integer defining normals, filtered by the full inequality system. This is a finite *exact* enumeration (the accompanying `CHECK.py` reconstructs it). Exactly 24 nonempty two-dimensional chambers result, grouped as follows. Here \(b=t r_j\), \(c=\sigma\), \(\Omega\) is the spherical area of a chamber, and \(E\) is the edge correction in the integral identity below.

| Kind | Number | Vertices | \(b\cdot c\) | \(\Omega\) | \(E\) |
| --- | ---: | ---: | ---: | --- | --- |
| A | 6 | 3 | \(1\) | \(\pi/6\) | \(4/9\) |
| B | 12 | 3 | \(1/3\) | \(\theta-\pi/12\) | \(1/9+\sqrt2/18-2\sqrt3/27\) |
| C | 6 | 5 | \(5/3\) | \(2\pi/3-2\theta\) | \(2/3+\sqrt2/9+4\sqrt3/27\) |

To evaluate these cells without numerical spherical quadrature, for any spherical geodesic polygon \(P\) with boundary edges \(e\), outward tangent unit normals \(m_e\), unit endpoints \(a_e,z_e\), and edge length \(\ell_e\), the spherical Laplacian and divergence theorem give the *exact* bilinear identity
\[
\int_P(b\cdot u)(c\cdot u)\,d\omega
=\frac{b\cdot c}{3}\,\Omega(P)
-\frac16\sum_e\left[(m_e\cdot b)(c\cdot V_e)
+(m_e\cdot c)(b\cdot V_e)\right],
\qquad V_e=\tan(\ell_e/2)(a_e+z_e).
\]
Indeed \(\Delta_{S^2}[(b\cdot u)(c\cdot u)-(b\cdot c)/3]\) equals \(-6\) times that bracket, while integration of \(u\) along a great-circle arc equals \(V_e\). The edge-normal inner products give the areas by spherical Gauss--Bonnet. The exact algebraic boundary terms sum to the table's \(E\)-values; the verifier checks each chamber directly from its exact ray coordinates and normals.

Summing \((b\cdot c)\Omega/3+E\) across the three kinds produces
\[
\int_{S^2}S(u)M_1(u)\,d\omega
=8+\frac{4\sqrt2}{3}+\frac{22\pi}{9}-\frac{16\theta}{3}.
\]
Therefore
\[
\mathbb E(SM_1)=\frac{11}{18}+\frac{2+\sqrt2/3}{\pi}
-\frac{4\theta}{3\pi}.
\]
Subtracting \(\mathbb ES\,\mathbb EM_j\), then multiplying by four, gives both displayed covariance formulas.

To establish the signs without relying on floating-point values, bound \(\sqrt2\) between the rationals \(141421356237/10^{11}\) and \(141421356238/10^{11}\); use \(\pi=16\arctan(1/5)-4\arctan(1/239)\) and \(\theta=\arctan(1/(2\sqrt2))\), bounding each arctangent by consecutive alternating Taylor partial sums (14 and 15 terms). Pure rational outward-interval arithmetic then gives
\[
-0.052539217903<\operatorname{Cov}(w_Q,w_{O_0})<-0.052539217813,
\qquad 0.027071539660<\operatorname{Cov}(w_Q,w_{O_1})<0.027071539726.
\]
These enclosures are certified by the included checker using rational fractions.

## Verification
Run `python CHECK.py` with Python 3, SymPy, and NumPy. It independently constructs 24 spherical cone chambers from all 48 sign/winner possibilities, certifies their exact integer boundary intersections, checks the cyclic ray orientations using exact determinants, verifies the three chamber multiplicities, areas and exact algebraic edge corrections, and produces a pure-rational certificate of both signs. Expected terminator: `VERIFY_OK`. The few floating-point operations in the checker only propose the cyclic order of exact rays and print decimals; they do not certify the inequalities, chamber measures, algebraic integrals, or covariance signs.

## Relationship to prior work
Finch's studies of regular-polyhedron widths (arXiv:1110.0671 and arXiv:1112.0499) give one-solid mean widths and marginal moments. Kabluchko, Litvak and Zaporozhets (arXiv:1511.08479) obtain single-body projection-length moments, including the regular cube and cross-polytope. Their marginal moments do not determine the *same-direction cross moment* of differently oriented bodies. Standard support-function/Minkowski-sum identities can encode a cross term formally, but they do not give these evaluated orientation-dependent covariance formulas and signs. The assessment concerns this exact polar pair and the specified two orientations.

## Limitations
No claim is made that either orientation maximizes or minimizes covariance over all rotations, nor that the correlation sign has a single phase transition in rotation angle. The chamber-certificate method is elementary but involves exact algebraic arithmetic; the source code is supplied to make every finite case reproducible. The result has not received independent mathematical audit or definitive historical-priority confirmation; broad mixed-moment identities and unindexed older work remain residual priority risks.

## References
1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first public version 2011-10-04. https://arxiv.org/abs/1110.0671
2. S. R. Finch, *Mean Width of a Regular Cross-Polytope*, arXiv:1112.0499, first public version 2011-12-02. https://arxiv.org/abs/1112.0499
3. Z. Kabluchko, A. E. Litvak and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, first public version 2015-11-26. https://arxiv.org/abs/1511.08479
