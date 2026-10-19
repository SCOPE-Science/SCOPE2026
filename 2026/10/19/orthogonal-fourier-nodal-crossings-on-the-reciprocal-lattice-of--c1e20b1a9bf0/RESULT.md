# Orthogonal Fourier nodal crossings on the reciprocal lattice of a regular hexagon

## Finding
Let \(H\subset\mathbb R^2\) be the centered regular hexagon of circumradius one, and write
\[
F(\xi)=\int_H e^{-2\pi i\xi\cdot X}\,dX.
\]
Let \(\Lambda\) be the hexagonal tiling lattice of \(H\), and let \(\Lambda^*\) be its Euclidean reciprocal lattice (with the Fourier convention above). All nonzero points of \(\Lambda^*\) are Fourier zeros. Exactly the points of an index-three sublattice, except for three lines through the origin, are nondegenerate zeros of exact Taylor order two; each is an ordinary crossing of exactly two real-analytic nodal arcs meeting at a right angle. All remaining nonzero reciprocal-lattice Fourier zeros are regular simple zeros.

More explicitly, put
\[
A=\begin{pmatrix}1&1/2\\0&\sqrt3/2\end{pmatrix},\quad
M=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\quad
\xi_{k,\ell}=A^{-T}M^{-T}\binom{k}{\ell},\quad(k,\ell)\in\mathbb Z^2\setminus\{(0,0)\}.
\]
Set \(s=\xi\cdot Ae_1\), \(t=\xi\cdot Ae_2\). At \(\xi_{k,\ell}\), these equal \(s=(2k+\ell)/3\) and \(t=(k+2\ell)/3\). A double crossing occurs **if and only if** \(s,t\in\mathbb Z\) and \(st(s-t)\ne0\). In that case, writing \(m=s\), \(n=t\), \(\xi_0=(m,(2n-m)/\sqrt3)\), and \(h=(h_x,h_y)\), one has
\[
F(\xi_0+h)=\frac{3\sqrt3}{8mn(m-n)}
\operatorname{Re}\left[(\xi_{0,x}+i\xi_{0,y})(h_x+ih_y)^2\right]
+O_{\xi_0}(|h|^3).
\]
If \(\theta=\arg(\xi_{0,x}+i\xi_{0,y})\), the two tangent-line directions are
\[
\varphi=\frac\pi4-\frac\theta2\pmod{\pi/2}.
\]
In particular, the reciprocal zero at \(\xi_0=(1,\sqrt3)\) has nodal tangents at angles \(15^\circ\) and \(105^\circ\).

In disks of Euclidean radius \(R\), the number of nonzero reciprocal-lattice zero nodes and the number of orthogonal quadratic crossings satisfy, respectively,
\[
N_{\mathrm{dual}}(R)=\frac{3\sqrt3\pi}{2}R^2+O(R+1),\qquad
N_{\mathrm{cross}}(R)=\frac{\sqrt3\pi}{2}R^2+O(R+1).
\]
Thus exactly one third of reciprocal-lattice zero nodes are orthogonal quadratic crossings in the density limit.

## Assumptions and scope
The domain is precisely \(H=A H_0\), where \(H_0=\{(u,v)\in\mathbb R^2:|u|\le1,\ |v|\le1,\ |u+v|\le1\}\). It has area \(3\sqrt3/2\), and \(H+(AM)\mathbb Z^2\) tiles the plane up to null boundaries. The Fourier transform is *unnormalized*, with exponential \(e^{-2\pi i\xi\cdot X}\); the reciprocal lattice is \(\Lambda^*=(AM)^{-T}\mathbb Z^2\). Counts refer exclusively to the **distinct nonzero reciprocal-lattice points**, not to all zeros of \(F\), which may lie elsewhere. The order of a zero means the degree of its first nonzero real-analytic Taylor jet. The right-angle assertion concerns the Euclidean metric and the regular hexagon; general affine distortions preserve crossings but need not preserve this angle.

## Proof
**1. Exact transform and lattice zeros.** For \(s=\xi\cdot Ae_1\), \(t=\xi\cdot Ae_2\), integration over \(H_0\) uses the two vertical sections
\[
-1\le u\le0:\ -1-u\le v\le1;\qquad
0\le u\le1:\ -1\le v\le1-u.
\]
Integrating first in \(v\) and then in \(u\) gives, initially when \(st(s-t)\ne0\),
\[
F(\xi)=\frac{\sqrt3}{2}\frac{N(s,t)}{2\pi^2st(s-t)},\quad
N(s,t)=(s-t)\cos(2\pi(s-t))+t\cos(2\pi t)-s\cos(2\pi s).
\]
The integral ensures that apparent poles are removable. The tiling lattice has matrix \(AM\), and its Fourier-orthogonality property already implies \(F(\xi)=0\) for nonzero \(\xi\in\Lambda^*\). It also follows directly: all three of \(s,t,s-t\) are integers when \(k\equiv\ell\pmod3\), so \(N=0\) away from denominator zeros. Otherwise their three cosine values equal \(-1/2\), again forcing \(N=0\); continuity covers the remaining axial points.

**2. Quadratic nodes.** At integer \((s,t)=(m,n)\) with \(mn(m-n)\ne0\), direct differentiation gives \(N=0\), \(\nabla N=0\), and
\[
D^2N(m,n)=4\pi^2\begin{pmatrix}n&m-n\\m-n&-m\end{pmatrix},\qquad
\det D^2N=-16\pi^4(m^2-mn+n^2)<0.
\]
The first nonzero Taylor term after division by the nonzero denominator is
\[
\frac{n(\delta s)^2+2(m-n)\delta s\,\delta t-m(\delta t)^2}{mn(m-n)}.
\]
Here \(\delta s=h_x\), \(\delta t=(h_x+\sqrt3h_y)/2\); multiplying by \(\det A=\sqrt3/2\) yields precisely the physical-coordinate quadratic formula in the finding. That quadratic form is a nonzero scalar times the real part of a rotated complex square. It is harmonic, has a nondegenerate indefinite Hessian, and its two null lines are orthogonal, with the stated half-angle directions. By the real-analytic Morse lemma, the full zero set in a sufficiently small neighborhood comprises **exactly two** embedded real-analytic nodal arcs crossing transversely along these lines. Hence the order is exactly two and there are no hidden additional arcs at these points.

**3. Other dual points are simple.** If \(m,n\in\mathbb Z\) with at least one of \(m,n,m-n\) equal to zero but not both \(m=n=0\), the continuously extended transform in oblique coordinates has the following linear jets (up to the common nonzero factor \(\sqrt3/2\)):
\[
\begin{array}{ll}
(s,t)=(0,n):&(-\delta s+2\delta t)/n,\\
(s,t)=(m,0):&(2\delta s-\delta t)/m,\\
(s,t)=(m,m):&(\delta s+\delta t)/m.
\end{array}
\]
Each is nonzero. If \(k\not\equiv\ell\pmod3\), all of \(s,t,s-t\) are nonintegers and all their cosines equal \(-1/2\). Differentiating \(N\), using the sine values \(\pm\sqrt3/2\), gives
\[
\nabla_{s,t}N(s,t)=\pm\pi\sqrt3\,(2s-t,\,2t-s).
\]
This vector cannot vanish except at \(s=t=0\), excluded for this coset. Because \(st(s-t)\ne0\) here, the transform has a nonzero first derivative. The real-analytic implicit-function theorem makes the local zero set one smooth analytic arc in every such case.

**4. Exact density.** The dual lattice has covolume \(|\det(AM)|^{-1}=2/(3\sqrt3)\), hence its Euclidean point density is \(3\sqrt3/2\). The integer sublattice \(s,t\in\mathbb Z\) has index three because its integer labels satisfy \(k\equiv\ell\pmod3\). The excluded lines \(s=0\), \(t=0\), and \(s=t\) contribute at most \(O(R+1)\) points in a disk. Standard lattice-point estimates for disks yield both quadratic counts and their one-third ratio.

## Verification
The independent numerical route integrates the polygonal indicator directly, rather than deriving values by evaluating the cosine quotient. A reproducible standalone program, `check_hexagon.py`, verifies the symbolic Hessian and its physical trace, compares three generic transform values with direct high-precision quadrature, checks seven reciprocal zeros by quadrature, compares five quadratic jets with direct integration, and verifies exact trigonometric zero/gradient identities at all 288 nonorigin reciprocal points with \(-8\le k,\ell\le8\). Run `python check_hexagon.py` with Python, SymPy, and mpmath. Its captured output is in `checks.txt`. Finite numerical tests do not establish the all-index classification; the proof above is analytic.

## Relationship to prior work
The polygonal-aperture integral and its edge-wave formulations are longstanding; see Huang–Christian–McDonald. The hexagonal tiling and reciprocal-lattice Fourier orthogonality follow from general spectral-domain theory and are explicitly developed for hexagons by Li–Sun–Xu and for root lattices by Li–Xu. These works account for the known zero **locations**. The present statement is restricted to the local Taylor orders, Euclidean orthogonal-crossing jets, tangent half-angle law, and one-third census at these known locations. A contemporary convex-body Fourier-zero study concentrates on the first positive Fourier zero and affine deformations, a distinct invariant. The 2011–12 geometric multivariate-sinc paper by Ye–Entezari is relevant to hexagonal cardinal functions but was not available in full text during comparison.

## Limitations
No classification is asserted for zeros outside the reciprocal lattice. No assertion of orthogonality is made for nonregular affine images. Literature precedence cannot be ruled out for unindexed optical or interpolation literature; the Ye–Entezari full text was not inspected.

## References
1. J. G. Huang, J. M. Christian, and G. S. McDonald, *Fresnel diffraction and fractal patterns from polygonal apertures*, J. Opt. Soc. Am. A 23 (2006), 2768–2774, DOI 10.1364/JOSAA.23.002768. The manuscript states “posted June 20, 2006”; author-accessible PDF: https://www.salfordphysics.com/gsmcdonald/32_JOSAA_v23_p2768_2006.pdf.
2. H. Li, J. Sun, and Y. Xu, *Discrete Fourier analysis, cubature and interpolation on a hexagon and a triangle*, arXiv:0712.3093, first posted December 19, 2007, https://arxiv.org/abs/0712.3093.
3. H. Li and Y. Xu, *Discrete Fourier analysis on fundamental domain of \(A_d\) lattice and on simplex in \(d\)-variable*, arXiv:0809.1079, first posted September 5, 2008, https://arxiv.org/abs/0809.1079.
4. J. Gómez-Serrano, M. Levitin, D. Platt, and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517, https://arxiv.org/abs/2609.10517.
5. J. Ye and A. Entezari, *A geometric construction of multivariate sinc functions*, IEEE Trans. Image Process., DOI 10.1109/TIP.2011.2162421 (metadata/abstract comparison only).
