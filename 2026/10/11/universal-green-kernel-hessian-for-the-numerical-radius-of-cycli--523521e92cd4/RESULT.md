# Universal Green-kernel Hessian for the numerical radius of cyclic shifts on \(\ell_p\)

## Finding
For every integer \(n\ge2\), exponent \(1<p<\infty\), and real weight perturbation \(h=(h_0,\ldots,h_{n-1})\in\mathbb R^n\), let \(T_\varepsilon\) act on real or complex \(\ell_p^n\) by
\[
(T_\varepsilon x)_j=(1+\varepsilon h_j)x_{j+1},\qquad j\pmod n,
\]
for sufficiently small real \(\varepsilon\) that all weights remain positive. Write \(\bar h=n^{-1}\sum_jh_j\), \(h^\circ=h-\bar h\mathbf1\), and \(L=2I-S-S^{-1}\), the cycle graph Laplacian with \((Sx)_j=x_{j+1}\) and the convention that its two parallel directed edges are counted when \(n=2\). Let \(L^+\) be the Moore--Penrose inverse, zero on constants.

The spatial numerical radius has the exact second-order expansion
\[
\boxed{v_p(T_\varepsilon)=1+\bar h\varepsilon+
\frac{\varepsilon^2}{2n}\left[\frac{p^2}{p-1}\langle h^\circ,L^+h^\circ\rangle-\|h^\circ\|_2^2\right]
+O_{p,n,h}(|\varepsilon|^3).}
\]
The maximizing coordinate-modulus power profile is uniquely determined and real analytic near \(\varepsilon=0\). The quadratic coefficient is nonnegative, and for nonconstant perturbations is strictly positive except at \(p=2\) in even dimension with \(h^\circ\) alternating between two opposite values. In particular, for two perturbations having equal means and equal centered Euclidean norms, their leading numerical-radius difference is governed entirely by their difference in cycle Green energies, with a positive coefficient independent of the arrangement and a common dependence on \(p\).

For example, with \(n=4\), set \(h^{\mathrm{grp}}=(1,1,0,0)\) and \(h^{\mathrm{alt}}=(1,0,1,0)\). Then, for every \(1<p<\infty\),
\[
v_p(T_{\varepsilon,h^{\mathrm{grp}}})-v_p(T_{\varepsilon,h^{\mathrm{alt}}})
=\frac{p^2}{32(p-1)}\varepsilon^2+O_p(|\varepsilon|^3)>0
\]
for all sufficiently small nonzero \(\varepsilon\).

## Assumptions and scope
The field may be \(\mathbb R\) or \(\mathbb C\). The spatial numerical radius on a smooth \(\ell_p\) space is
\[
v_p(T)=\sup_{\|x\|_p=1}\left|\sum_{j=0}^{n-1}|x_j|^{p-2}\overline{x_j}(Tx)_j\right|.
\]
At zero coordinates the displayed duality-map summand is interpreted as zero. All assertions fix finite \(n\), fixed \(p\), and fixed finite real \(h\) before \(\varepsilon\to0\). The constants implicit in the remainder may depend on these data; they are not uniform as \(p\) approaches an endpoint or \(n\to\infty\). The real/complex statement concerns the supremum and the uniquely determined positive mass profile, not uniqueness of complex maximizing phases.

## Proof
**Reduction to a simplex.** For positive weights, the triangle inequality and the choice of nonnegative real coordinates show, with \(\alpha=(p-1)/p\), \(\beta=1/p\), that
\[
v_p(T_\varepsilon)=\max_{u_j\ge0,\ \sum_j u_j=1}
\Phi_\varepsilon(u),\qquad
\Phi_\varepsilon(u)=\sum_{j=0}^{n-1}(1+\varepsilon h_j)u_j^\alpha u_{j+1}^\beta,
\]
where \(u_j=|x_j|^p\). This reduction is valid over both scalar fields. At zero perturbation, weighted arithmetic--geometric mean yields \(u_j^\alpha u_{j+1}^\beta\le\alpha u_j+\beta u_{j+1}\), hence \(\Phi_0(u)\le1\). Equality forces \(u_j=u_{j+1}\) for all \(j\), so the unique maximizing mass is \(u_*=(1/n)\mathbf1\).

**Uniform localization and differentiability.** Compactness of the closed probability simplex and uniqueness of \(u_*\) imply every global maximizer of \(\Phi_\varepsilon\) converges to \(u_*\) as \(\varepsilon\to0\); in particular it lies in the interior for small \(\varepsilon\). On the tangent hyperplane \(\{\xi:\sum_j\xi_j=0\}\), the Hessian of \(\Phi_0\) at \(u_*\) is \(-n\alpha\beta L\). The graph is connected, so this is negative definite on that hyperplane. The analytic implicit-function theorem gives a unique analytic critical profile near \(u_*\), and the localization argument makes it the unique global maximizer for sufficiently small \(\varepsilon\).

**Expansion and maximization.** Write \(u_j=n^{-1}+\varepsilon\xi_j+O(\varepsilon^2)\) with \(\sum_j\xi_j=0\). A direct Taylor expansion gives
\[
\Phi_\varepsilon(u)=1+\bar h\varepsilon+\varepsilon^2
\left[\langle b,\xi\rangle-\frac{n\alpha\beta}{2}\langle\xi,L\xi\rangle\right]+O(|\varepsilon|^3),
\]
where \(b_j=\alpha h_j+\beta h_{j-1}\). Taking the gradient within the tangent hyperplane yields
\[
\xi=\frac1{n\alpha\beta}L^+b^\circ,
\qquad b^\circ=b-\bar h\mathbf1.
\]
The quadratic objective at its maximum equals \(\langle b^\circ,L^+b^\circ\rangle/(2n\alpha\beta)\). Since \(b^\circ=(\alpha I+\beta S^{-1})h^\circ\), these circulant operators commute with \(L^+\), and
\[
(\alpha I+\beta S)(\alpha I+\beta S^{-1})
=I-\alpha\beta L.
\]
Thus \(\langle b^\circ,L^+b^\circ\rangle=\langle h^\circ,L^+h^\circ\rangle-\alpha\beta\|h^\circ\|_2^2\). Substitution and \(1/(\alpha\beta)=p^2/(p-1)\) give the asserted coefficient. Analyticity supplies the claimed cubic remainder.

**Positivity, boundary, and arrangement.** On the mean-zero subspace, the eigenvalues of \(L\) are \(\lambda_k=4\sin^2(\pi k/n)\), \(k=1,\ldots,n-1\). Writing \(h^\circ\) in the corresponding orthogonal Fourier modes, the quadratic bracket is a sum of \((p^2/((p-1)\lambda_k)-1)\) times nonnegative squared mode amplitudes. Here \(p^2/(p-1)=4+(p-2)^2/(p-1)\ge4\ge\lambda_k\). Equality for a nonconstant perturbation requires \(p=2\), even \(n\), and support solely on the alternating mode \(k=n/2\). For the displayed four-cycle patterns, \(\|h^\circ\|_2^2=1\) for both, while their Green energies are \(1/2\) and \(1/4\); the difference of coefficients is \(p^2/(32(p-1))\). Its strict positivity implies the local inequality for sufficiently small nonzero \(\varepsilon\).

## Verification
The accompanying standalone `verify.py` implements the cycle Green operator by solving the regularized Laplacian linear system, independently computes the simplex maximization using constrained optimization, and compares the Hilbert special case with the top eigenvalue of the symmetrized shift. It checks the explicit four-cycle energy values, the quadratic coefficient and its arrangement difference, multiple dimensions and exponents, and both signs of sufficiently small perturbations. Run with `python verify.py` using Python 3 with NumPy and SciPy installed. Passing finite numerical checks is a reproducibility supplement and not a proof of the universal statement, which is supplied above.

## Relationship to prior work
Chang and Wang (2012) characterize weight permutations maximizing numerical radius for cyclic weighted matrices in the Hilbert setting. Their original 2012 text formulates the problem on a complex Hilbert space and does not state the \(\ell_p\)-dependent Green-kernel second variation. Chien and Sheu (2013) calculate and compare numerical radii of certain Hilbert-space weighted shift matrices and operators, principally noncyclic weighted shifts. The present formula treats local simultaneous perturbations of every positive weight on a cyclic shift on real or complex \(\ell_p^n\), providing an explicitly mode-resolved Hessian and a common arrangement ordering valid beyond the Hilbert exponent. The Hilbert part is a special perturbative consequence of standard Perron eigenvalue theory and is not claimed separately as novel.

## Limitations
The theorem concerns positive weights near a common strictly positive baseline, finite cycles, and exponents strictly between one and infinity. It is a local second-order expansion, not a global rearrangement theorem for arbitrary weights. Complex maximizing phases are not asserted unique. The older Hilbert literature can encode the \(p=2\) specialization by familiar eigenvalue perturbation; potential alternative historical formulations of the general \(\ell_p\) expansion are a residual bibliographic risk. Independent external mathematical and bibliographic validation has not been performed.

## References
1. C.-T. Chang and K.-Z. Wang, “Maximizing numerical radii of weighted shifts under weight permutations,” *Journal of Mathematical Analysis and Applications* 394 (2012), 592–602, doi:10.1016/j.jmaa.2012.04.039. Earliest verified online availability: 30 April 2012.
2. M.-T. Chien and H.-A. Sheu, “The numerical radii of weighted shift matrices and operators,” *Operators and Matrices* 7 (2013), 197–204, doi:10.7153/oam-07-11. Open full text: https://files.ele-math.com/articles/oam-07-11.pdf.
