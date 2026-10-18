# One-dimensional Schwartz universality for finite doubly positive Gram data

## Finding
Fix integers \(d,n\ge1\). Let \(f:\mathbb R^d\to\mathbb R\) be a normalized, pointwise nonnegative, positive-definite **generalized trigonometric polynomial**, meaning
\[
f(x)=\sum_{\ell=1}^{M}a_\ell e^{i\langle\lambda_\ell,x\rangle},\qquad a_\ell>0,\quad \sum_\ell a_\ell=1,
\]
with finitely many distinct \(\lambda_\ell\in\mathbb R^d\), and with the additional hypothesis \(f(x)\ge0\) for every \(x\). (The reality condition is part of the hypothesis; frequencies need not be integer or commensurable.) Write \(\mathcal G_n(f)\) for all real matrices
\[
G_f(x_1,\ldots,x_n)=[f(x_j-x_k)]_{j,k=1}^n,\qquad x_j\in\mathbb R^d.
\]
There is a **full-Lebesgue-measure dense \(G_\delta\)** set of directions \(v\in\mathbb R^d\) such that the one-variable window \(h_v(t)=f(tv)\) is again a normalized pointwise nonnegative positive-definite generalized trigonometric polynomial and
\[
\boxed{\overline{\mathcal G_n(h_v)}=\overline{\mathcal G_n(f)}\quad\text{for every integer }n\ge1.}
\]
Indeed, the same generic direction works **simultaneously for every finite sample size**. **Smooth dimension-collapse strengthening.** More strongly, for every such sample matrix \(G_f(x_1,\ldots,x_n)\) and every \(\varepsilon>0\) there exist points \(t_1,\ldots,t_n\in\mathbb R\) and a one-variable **strictly positive, even, real-entire Schwartz function** \(g:\mathbb R\to(0,\infty)\), normalized by \(g(0)=1\), which is positive definite, whose Fourier transform is a **strictly positive entire finite Gaussian mixture**, and for which
\[
\boxed{\max_{j,k}|g(t_j-t_k)-f(x_j-x_k)|<\varepsilon.}
\]
Thus every strict finite-Gram obstruction in the original class also occurs for a one-dimensional Schwartz kernel with no Fourier spectral zeros. The generic-line equality above is the key intermediate assertion.

## Assumptions and scope
Both conclusions concern entrywise approximation (hence also convergence in any finite-dimensional matrix norm); neither identifies the sampling points or claims exact equality of individual matrices. The word *generalized* permits arbitrary real frequencies, so \(h_v\) may be quasiperiodic rather than periodic. It is crucial that the Fourier spectrum of \(f\) be finite. No such all-function claim is made for general continuous positive-positive-definite functions with arbitrary spectral measures. The direction may depend on \(f\) but does not depend on \(n\) or the sample points.

## Proof
Set
\[
\Phi(x)=(e^{i\langle\lambda_1,x\rangle},\ldots,e^{i\langle\lambda_M,x\rangle})\in\mathbb T^M
\]
and let \(H=\overline{\Phi(\mathbb R^d)}\). For \(m=(m_1,\ldots,m_M)\in\mathbb Z^M\), the torus character \(\chi_m(z)=\prod_\ell z_\ell^{m_\ell}\) is trivial on \(H\) if and only if
\[
\sum_{\ell=1}^{M}m_\ell\lambda_\ell=0.
\]
The same character is trivial on \(H_v=\overline{\Phi(\mathbb Rv)}\) if and only if \(\langle\sum_\ell m_\ell\lambda_\ell,v\rangle=0\). Choose \(v\) outside the countable union of proper hyperplanes
\[
\bigcup_{\substack{m\in\mathbb Z^M\\\sum_\ell m_\ell\lambda_\ell\ne0}}
\left\{v:\left\langle\sum_\ell m_\ell\lambda_\ell,v\right\rangle=0\right\}.
\]
Such directions form a dense \(G_\delta\) of full Lebesgue measure. Their two annihilator sets coincide. The character-separation form of Kronecker's theorem for closed subgroups of a finite torus now yields \(H_v=H\).

Fix any \(x_1,\ldots,x_n\in\mathbb R^d\) and \(\delta>0\). By \(H_v=H\), choose \(t_1,\ldots,t_n\in\mathbb R\) such that
\[
\max_{j,\ell}\left|e^{it_j\langle\lambda_\ell,v\rangle}-e^{i\langle\lambda_\ell,x_j\rangle}\right|<\delta.
\]
All these phase factors have modulus one; hence their quotients obey
\[
\left|e^{i(t_j-t_k)\langle\lambda_\ell,v\rangle}-e^{i\langle\lambda_\ell,x_j-x_k\rangle}\right|<2\delta.
\]
Multiplying by the nonnegative weights \(a_\ell\), summing, and using \(\sum a_\ell=1\) shows
\[
\max_{j,k}|h_v(t_j-t_k)-f(x_j-x_k)|\le2\delta.
\]
Thus every matrix in \(\mathcal G_n(f)\) is in \(\overline{\mathcal G_n(h_v)}\). The reverse inclusion holds without a closure because every line sample \(t_jv\) is a sample in \(\mathbb R^d\). This proves the displayed equality, with no dependence of the choice of \(v\) on \(n\).

The restriction retains finite support and positive Fourier weights (so is positive definite by direct summation of rank-one character kernels), normalization \(h_v(0)=1\), reality, and global pointwise nonnegativity. For the class-wide assertion, extend any one-variable \(h\) to \(\mathbb R^d\) by \(F(x)=h(x_1)\), providing the reverse inclusion of the union of Gram sets. Finally, any continuous real function of a fixed-size Gram matrix has identical infimum and supremum over the corresponding equal compact closures.

For the stronger smooth assertion, retain the generic direction and sampling numbers already chosen. For \(\alpha,\tau>0\), set
\[
g_{\alpha,\tau}(t)=e^{-\tau t^2}\frac{h_v(t)+\alpha}{1+\alpha}.
\]
Both factors are positive definite, hence their product is positive definite; moreover \(g_{\alpha,\tau}(0)=1\), \(g_{\alpha,\tau}(t)>0\) for every real \(t\), and the function is even and real entire. All derivatives of \(h_v\) are bounded (finite exponential sum), so the Gaussian factor makes \(g_{\alpha,\tau}\) Schwartz. Writing \(\beta_\ell=\langle\lambda_\ell,v\rangle\), its Fourier transform under \(\widehat g(\omega)=\int_{\mathbb R}g(t)e^{-i\omega t}dt\) is
\[
\widehat g_{\alpha,\tau}(\omega)
=\frac{\sqrt{\pi/\tau}}{1+\alpha}
\left(\alpha e^{-\omega^2/(4\tau)}+
\sum_{\ell=1}^{M}a_\ell e^{-(\omega-\beta_\ell)^2/(4\tau)}\right)>0
\quad (\omega\in\mathbb R).
\]
It is entire as a function of \(\omega\). The bounds \( |h_v(t)|\le1\), \( |(h_v(t)+\alpha)/(1+\alpha)-h_v(t)|\le2\alpha\), and \(0\le1-e^{-\tau u^2}\le\tau u^2\) give, for \(D=\max_{j,k}|t_j-t_k|\),
\[
\max_{j,k}|g_{\alpha,\tau}(t_j-t_k)-f(x_j-x_k)|
\le2\delta+2\alpha+\tau D^2.
\]
Choose \(\delta\), then \(\alpha\), then \(\tau\) in that order, making this less than the prescribed \(\varepsilon\). A strictly negative quadratic-form defect remains negative by continuity.

## Verification
The proof is analytic. The key nonstandard step is the explicit annihilator comparison for every integer character, followed by the standard torus character-separation theorem. The bound \(2\delta\) checks the exact sample-to-Gram implication. A supplementary checker `VERIFY.py` additionally tests Gaussian smoothing and uses
\[
f(x,y)=\tfrac14(1+\cos x)(1+\cos y),\qquad v=(1,\sqrt2),
\]
with four points \((0,0),(\pi,0),(0,\pi),(\pi,\pi)\), whose original Gram matrix is the identity. Increasing finite searches over a one-dimensional dense orbit approximate this Gram matrix and test normalization and the error bound; positivity and positive definiteness follow analytically from the Fourier coefficients. These finite tests cannot prove torus orbit density.

## Relationship to prior work
Hinrichs and Vybíral's *On positive positive-definite functions and Bochner's Theorem* (2010 preprint, later journal article) introduces the Gram-matrix inequality for normalized doubly positive functions and supplies equivalent formulations. Vybíral's September 18, 2026 preprint reports a strict eight-point violation using a seven-variable trigonometric polynomial. The present theorem is a **generic-line finite-Gram closure equivalence**, not another rederivation of that numerical witness. Applied to a verified strict seven-dimensional witness, it gives a nonperiodic, one-variable strict witness with the same sample size and arbitrarily close deficit; in particular the reported gap of \(-1/10\) could be approached arbitrarily closely. The newer preprint's **abstract** was accessible, but its full text was not; a one-dimensional argument elsewhere in that paper remains a historical-priority risk. Kronecker's torus theorem is a classical, explicitly credited component of the method.

## Limitations
Equality is of closures, not individual matrix realizations. No uniform quantitative bound is given for the sizes of the one-dimensional sampling locations or the Gaussian smoothing scale, and there is no assertion for strictly periodic integer-frequency polynomials or general continuous positive-positive-definite kernels with non-atomic spectral measure. The dimension-collapse and Gaussian-regularization theorem does not independently certify the numerical assertions in Vybíral's separate seven-dimensional example. Novelty is therefore qualified by the incomplete full-text comparison; independent mathematical review has not been performed.

## References
1. A. Hinrichs and J. Vybíral, *On positive positive-definite functions and Bochner's Theorem*, preprint dated September 3, 2010. https://people.fjfi.cvut.cz/vybirja2/publ/Vybiral19.pdf
2. J. Vybíral, *An explicit counterexample to the Hinrichs--Vybiral conjecture*, arXiv:2609.21733, first posted September 18, 2026. https://arxiv.org/abs/2609.21733
3. Kronecker's approximation theorem, character/annihilator description for closed subgroups of finite tori; classical theorem, used as background rather than claimed new.
