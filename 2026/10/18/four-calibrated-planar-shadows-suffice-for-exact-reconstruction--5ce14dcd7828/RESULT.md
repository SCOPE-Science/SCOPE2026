# Four calibrated planar shadows suffice for exact reconstruction in the threefold-projection class

## Finding
Consider the class of full-dimensional convex bodies \(K\subset\mathbb R^3\) for which **every** orthogonal projection onto a plane has threefold rotational symmetry after a translation of that planar projection. A calibrated view specifies the plane, an oriented orthonormal basis of the plane, and the projected body **up to translation only**; independent in-plane rotations are not discarded.

**Theorem (sharp number of views).** Four suitably chosen calibrated planar shadows uniquely determine any such \(K\) up to a single spatial translation. The same holds for almost every four-tuple of planes (with respect to product Haar measure). No three calibrated planar shadows suffice uniformly over this class: for every prescribed triple of planes, infinitely many pairwise non-translation-equivalent smooth strictly convex bodies have identical three shadows up to separate in-plane translations. The minimal number of views is therefore exactly **four**.

The recovery has an **explicit rational certificate**, needs only seven real third-harmonic measurements from the four shadows, and is Lipschitz stable for the displayed configuration. Write the support function, after removing translation, as
\[
 h_K(u)=r+\sum_{j=1}^7 a_jH_j(u),\qquad r>0,\quad u\in S^2,
\]
where \(H_j\) are the seven homogeneous harmonic cubics specified below and \(r\) is the mean support on any calibrated projection circle. For the seven measurements \(m=(C_1,D_1,C_2,D_2,C_3,D_3,C_4)\) from the four fixed views below, \(a=V^{-1}m\), with
\[
 \det V=\frac{625}{6912}\ne0,\qquad
 \|a-a'\|_\infty\le\frac{164}{5}\|m-m'\|_\infty.
\]
Consequently, with the translations removed, the Hausdorff distance between the bodies is at most
\[
 |r-r'|+\frac{2296}{5}\|m-m'\|_\infty.
\]
These numerical stability coefficients are sufficient, not claimed optimal.

## Assumptions and scope
The ambient Euclidean coordinate frame is fixed. A planar shadow means the **entire orthogonal projection as a convex set**, known up to **planar translation**, and measured in its prescribed orthonormal frame. In particular, its first support-function Fourier mode is discarded, but its third-harmonic phase relative to the frame is retained. The theorem does not assert reconstruction from brightness (projection *area*) alone, unregistered planar rotations, noisy unknown orientations, or a finite number of arbitrary uncalibrated silhouettes.

For an oriented orthonormal plane frame \((e,f)\), parametrize \(u(\theta)=e\cos\theta+f\sin\theta\). Its shadow has a support function of the form
\[
 p_{e,f}(\theta)=r+U\cos\theta+W\sin\theta
 +C_{e,f}\cos3\theta+D_{e,f}\sin3\theta.
\]
The coefficients \(C_{e,f},D_{e,f}\) and the common mean \(r\) are invariant under translating the shadow. They can be extracted by integration against the corresponding trigonometric functions. Let \(r_2=x^2+y^2+z^2\) and use the **ordered** real harmonic-cubic basis
\[
\begin{aligned}
H_1&=z(5z^2-3r_2), &H_2&=x(5z^2-r_2), &H_3&=y(5z^2-r_2),\\
H_4&=z(x^2-y^2), &H_5&=xyz, &H_6&=x(x^2-3y^2),\\
H_7&=y(3x^2-y^2).
\end{aligned}
\]
Every such polynomial is harmonic and their restrictions form a basis of the seven-dimensional real degree-three spherical-harmonic space.

## Proof
**1. Identifying the finite-dimensional geometric class.** The basic harmonic-projection method and the nonzero equatorial-frequency lemma are established by Myroshnychenko, Ryabogin, and Saroglou [1, Sections 4.4–4.7]. The threefold symmetry hypothesis means that on every great circle the support function has Fourier frequencies only in \(\{0,\pm1,\pm3,\pm6,\pm9,\ldots\}\): the first harmonic accounts for the allowable planar translation. This is a linear, rotation-invariant condition. Each ambient spherical-harmonic projection preserves it, by averaging the rotated function against the irreducible character. For any even degree \(\ell\ge2\), a nonzero \(\ell\)-harmonic has a nonzero equatorial Fourier mode \(2\) on some great circle, contradicting this condition. For every odd degree \(\ell\ge5\), the same source lemma supplies a nonzero forbidden mode \(5\). The only possible ambient degrees are therefore \(0,1,3\). Continuity upgrades the resulting \(L^2\) harmonic identity to a pointwise identity. Degrees \(0\) and \(1\) give \(r\) and a global translation, and degree \(3\) gives the stated seven-dimensional component. This structural reduction is credited as a consequence of the established spherical-harmonic machinery, **not claimed as the new result**. Conversely, any sufficiently small perturbation \(1+\varepsilon H\), for \(H\) harmonic cubic, defines a smooth strictly convex constant-width body: its curvature-radius form is \(I+\varepsilon(\nabla^2_SH+HI)\), positive definite for sufficiently small \(|\varepsilon|\). Its projections have only modes \(0,1,3\), hence the required symmetry.

**2. Exact linear measurement formula.** For any homogeneous real cubic \(H\), put \(w=e-if\in\mathbb C^3\). Substituting
\[
 u(\theta)=\frac12\bigl(we^{i\theta}+\overline w e^{-i\theta}\bigr)
\]
shows that the coefficient of \(e^{3i\theta}\) in \(H(u(\theta))\) equals \(H(w)/8\). Consequently,
\[
 C_{e,f}-iD_{e,f}=\frac14 H(e-if).
\]
The formula is valid for all the basis harmonics and requires no curvature approximation. Since their means and first harmonics are orthogonal to the third mode, it gives the entire measurement map for the translation-equivalence class.

**3. Seven-measurement rational reconstruction.** Choose the four oriented plane frames
\[
\begin{aligned}
(e_1,f_1)&=((1,0,0),(0,1,0)),\\
(e_2,f_2)&=((1,0,0),(0,0,1)),\\
(e_3,f_3)&=((0,0,-1),(0,1,0)),\\
(e_4,f_4)&=((1,2,-2)/3,(2,1,2)/3).
\end{aligned}
\]
Every pair is exactly orthonormal. Take \(C_i=C_{e_i,f_i}\), \(D_i=D_{e_i,f_i}\) and \(m=(C_1,D_1,C_2,D_2,C_3,D_3,C_4)^\mathsf T\). By Step 2, \(m=Va\) for
\[
V=\begin{pmatrix}
0&0&0&0&0&1&0\\
0&0&0&0&0&0&1\\
0&-5/4&0&0&0&1/4&0\\
-5/4&0&0&1/4&0&0&0\\
-5/4&0&0&-1/4&0&0&0\\
0&0&5/4&0&0&0&1/4\\
20/27&20/27&10/27&1/9&-5/54&1/27&-8/27
\end{pmatrix}.
\]
Exact rational elimination gives \(\det V=625/6912\), so these seven scalar Fourier coefficients suffice. For complete explicit inversion, with \(a=(a_1,\ldots,a_7)^\mathsf T\),
\[
\begin{aligned}
a_1&=-2(D_2+C_3)/5,\\
a_2&=(C_1-4C_2)/5,\\
a_3&=(-D_1+4D_3)/5,\\
a_4&=2(D_2-C_3),\\
a_5&=2C_1-4D_1-\tfrac{32}{5}C_2-\tfrac45D_2-\tfrac{28}{5}C_3+\tfrac{16}{5}D_3-\tfrac{54}{5}C_4,\\
a_6&=C_1,\qquad a_7=D_1.
\end{aligned}
\]
The remaining eighth scalar datum \(D_4\) is redundant and provides a consistency check for exact data. The common radius \(r\) is the angular mean of any shadow support function, and thus the full support function is recovered up to its global linear term.

**4. Generic four-view sufficiency.** The determinant of any selected seven-by-seven measurement minor is a real-analytic polynomial function of the four oriented orthonormal frames. It is nonzero for the configuration in Step 3, so the set where that particular minor vanishes is a proper real-analytic subset of the connected manifold \(SO(3)^4\), hence Haar-null and nowhere dense. Changing the orthonormal basis within an individual plane merely applies an invertible planar rotation of angle three to \((C_i,D_i)\). Thus full rank is a property of the four planes, and generic four-tuples of unoriented planes also work.

**5. Sharp necessity of four views.** Fix any three projection planes and their frames. The third-harmonic data define a linear map from a real seven-dimensional space to at most six real coordinates. Its kernel contains a nonzero harmonic cubic \(H\). For all sufficiently small \(\varepsilon\), the bodies with supports \(1+\varepsilon H(u)\) are smooth and strictly convex, but the third-harmonic coefficients of all three chosen shadows are zero and their means are one. Thus each chosen shadow is, up to its own translation, the unit disk, for an entire nontrivial interval of \(\varepsilon\). These bodies are not spatial translates of one another because the cubic components differ. This proves failure for **every** three-plane choice and exact minimality of four.

**6. Stability.** Exact inversion of \(V\) shows \(\|V^{-1}\|_{\ell_\infty\to\ell_\infty}=164/5\), yielding the coefficient bound. The individual harmonics have sphere sup norms at most \((2,4,4,1,1,1,1)\), whose sum is \(14\). Therefore, after choosing representatives with zero global linear component,
\[
\|h_K-h_{K'}\|_{L^\infty(S^2)}\le|r-r'|+14\cdot\frac{164}{5}\|m-m'\|_\infty.
\]
For compact convex sets the support-function supremum equals Hausdorff distance, proving the claimed geometric estimate.

## Verification
The embedded standalone \(\texttt{verify.py}\) recomputes each harmonic's Laplacian, checks the exact four orthonormal frames, derives each matrix entry by expanding the cubic restriction into powers of cosine and sine, and independently checks those entries via complex null-frame evaluation. Exact rational elimination checks the printed matrix, determinant, rank, inverse, and operator norm. Its output is \(\texttt{VERIFY\_OK}\). The checks verify finite algebraic certificates; the infinitely-many-plane and genericity assertions follow from Steps 1, 4, and 5, not finite enumeration.

## Relationship to prior work
Myroshnychenko, Ryabogin, and Saroglou [1] establish rotational-projection rigidity for fourfold or higher symmetry and construct non-ball threefold examples. Their Sections 4–5 provide the harmonic tools and the cubic restriction identity used in Step 1; the finite calibrated-view count, the exact four-plane rank certificate, and minimality are not stated in the inspected full source. The general harmonic restriction background in [2] and finite-band spherical-harmonic sampling in [3] concern broader harmonic representation and point-sampling schemes; neither identified statement directly supplies the present minimal **translated-shadow / third-circle-Fourier** measurement design. The related explicit cubic-family convexity and brightness calculations [4–6] concern particular one-dimensional cubic families and projected **areas**, not recovery of arbitrary seven-dimensional cubic-harmonic shapes.

## Limitations
The hypotheses require **every** plane to have threefold-symmetric projection, but recovery uses only four selected planes. The frame orientation and phase are calibrated. If planar rotations as well as translations are forgotten, this proof does not establish four-view sufficiency. The bound \(164/5\) is exact for the specified seven-coordinate inversion in the chosen basis, not a universally optimal noise-amplification constant or a claim about stochastic noise. The result makes no assertion about all convex bodies, higher-dimensional analogues, or recovery from projection areas alone. Although the checked sources do not establish the four-view theorem, an equivalent earlier finite-harmonic sampling scheme in unindexed literature remains a priority risk; novelty is not independently certified.

## References
1. S. Myroshnychenko, D. Ryabogin and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first public 2026-09-23, https://arxiv.org/abs/2609.27192.
2. H. Groemer, *Geometric Applications of Fourier Series and Spherical Harmonics*, Cambridge University Press, 1996/2009.
3. Z. Khalid, R. A. Kennedy and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, 2014.
4. *Sharp convexity threshold for the cubic constant-width support family*, mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-convexity-threshold-for-the-cubic-constant-width-support-f--b3681da24cdc.
5. *Exact brightness profile of the cubic threefold-projection exception*, mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-brightness-profile-of-the-cubic-threefold-projection-excep--a6ac80c263be.
6. *Exact projection-body volume and random-brightness law for axial cubic bodies*, mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-projection-body-volume-and-random-brightness-law-for-axial--718163d68e7d.
