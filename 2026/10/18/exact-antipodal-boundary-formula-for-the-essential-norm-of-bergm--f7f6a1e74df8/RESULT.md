# Exact antipodal boundary formula for the essential norm of Bergman slant Toeplitz operators

## Finding
For the classical unweighted analytic Bergman space \(A^2(\mathbb D)\), let \(P:L^2(\mathbb D)\to A^2(\mathbb D)\) be the orthogonal Bergman projection. Define \(W\) first on analytic polynomials by \(Wz^{2n}=z^n\) and \(Wz^{2n+1}=0\) for integers \(n\ge0\). For a symbol \(\varphi\in C(\overline{\mathbb D})\), write \(B_\varphi=WP M_\varphi|_{A^2(\mathbb D)}\), and define its essential norm as \(\|B_\varphi\|_{\mathrm e}=\inf\{\|B_\varphi-K\|:K\text{ is compact}\}\).

The exact answer is
\[\boxed{\displaystyle \|B_\varphi\|_{\mathrm e}=\max_{|\zeta|=1}\sqrt{|\varphi(\zeta)|^2+|\varphi(-\zeta)|^2}.}\]
Consequently \(B_\varphi\) is compact exactly when \(\varphi|_{\partial\mathbb D}=0\). Examples: for \(\varphi(z)=1+z\), the essential norm is \(2\); for \(\varphi(z)=1+z^2\), it is \(2\sqrt2\). No factor of \(\sqrt2\) can be replaced by a naive uniform norm of \(\varphi\): antipodal values interfere in two independent input channels.

## Assumptions and scope
Use normalized planar area \(dA=\pi^{-1}\,dx\,dy\). The normalized Bergman monomial basis is \(e_n(z)=\sqrt{n+1}\,z^n\) for \(n\in\mathbb N_0\). The statement concerns the specific unnormalized-on-monomials slant map \(Wz^{2n}=z^n\), not other slant-shift normalization conventions. It holds for every complex-valued symbol continuous on the closed disk. No claim is made for arbitrary essentially bounded boundary functions, for non-continuous symbols, or for higher-order slant maps.

## Proof
**1. The slant map and its compact asymptote.** Its action on the orthonormal basis is
\[We_{2n}=\sqrt{\frac{2n+1}{n+1}}\,e_n,\qquad We_{2n+1}=0.\]
Thus \(W\) extends boundedly, with \(\|W\|=\sqrt2\). Let \(J\) denote the even-index decimator \(Je_{2n}=e_n\), \(Je_{2n+1}=0\). The diagonal coefficient difference tends to zero, so \(W-\sqrt2J\) is compact.

**2. Reduce a continuous symbol to its boundary.** If \(h\in C(\overline{\mathbb D})\) vanishes on the circle, then \(T_h=PM_h|_{A^2}\) is compact. Indeed, approximate \(h\) uniformly by \(h\) times a compactly supported radial cutoff. For a bounded symbol supported strictly inside the disk, the map \(A^2\to L^2\) given by multiplication is Hilbert--Schmidt: its squared Hilbert--Schmidt norm is \(\int |h(z)|^2(1-|z|^2)^{-2}dA(z)<\infty\). Composing with \(P\) preserves compactness. If two continuous symbols have the same boundary restriction, their Toeplitz operators, hence their slant Toeplitz operators, differ by a compact operator.

Trigonometric polynomials uniformly approximate any continuous function on the unit circle. For a boundary trigonometric polynomial \(p(e^{i\theta})=\sum_{k=-m}^{m}c_ke^{ik\theta}\), take the harmonic polynomial \(h(z)=c_0+\sum_{k=1}^m(c_kz^k+c_{-k}\overline z^{\,k})\). Then \(\varphi-h\) vanishes at the boundary and contributes only a compact operator. The limit from polynomials is in operator norm, because \(\|B_\varphi-B_\psi\|\le\|W\|\,\|\varphi-\psi\|_\infty\) for actual disk approximants; for boundary approximants choose their Poisson harmonic extensions, a contractive map in the uniform norm.

**3. A compact Laurent model.** Let \(S e_n=e_{n+1}\). Direct integration gives for \(k\ge1\)
\[T_{z^k}e_n=\sqrt{\frac{n+1}{n+k+1}}\,e_{n+k},\qquad T_{\overline z^{\,k}}e_n=\begin{cases}\sqrt{\frac{n-k+1}{n+1}}e_{n-k},&n\ge k,\\0,&n<k.\end{cases}\]
For each fixed \(k\), the weights tend to \(1\), whence \(T_{z^k}-S^k\) and \(T_{\overline z^{\,k}}-S^{*k}\) are compact. Thus \(B_h\) differs by a compact operator from \(\sqrt2J L_p\), where \(L_p=\sum_{k\ge0}c_kS^k+\sum_{k<0}c_kS^{*(-k)}\) is the finite Laurent Toeplitz matrix.

**4. Split the parity channels.** Identify the domain unitarily with \(\ell^2(\mathbb N_0)\oplus\ell^2(\mathbb N_0)\) by separating even- and odd-indexed coefficients. The row operator \(JL_p\) then has two unilateral Laurent Toeplitz blocks with respective Laurent symbols
\[a(\zeta)=\sum_{r\in\mathbb Z}c_{2r}\zeta^r,\qquad b(\zeta)=\sum_{r\in\mathbb Z}c_{2r+1}\zeta^{r+1}.\]
The entries crossing the origin follow the usual unilateral Toeplitz convention and introduce no asymptotic discrepancy. Its operator norm is bounded by the norm of the corresponding row of bilateral Laurent multipliers, i.e.
\[\|JL_p\|\le \max_{|\zeta|=1}\sqrt{|a(\zeta)|^2+|b(\zeta)|^2}.\]
For the reverse essential-norm bound, take unit vectors consisting of long finite plane-wave packets centered at indices tending to infinity, with two constant channel amplitudes proportional to the conjugate row \((\overline{a(\zeta)},\overline{b(\zeta)})\) at a chosen \(\zeta\). The packets converge weakly to zero while their image norms tend to \(\sqrt{|a(\zeta)|^2+|b(\zeta)|^2}\). Every compact operator sends them to zero. Taking the supremum gives the exact essential norm of the row. The same argument can be made directly with normalized Hardy reproducing kernels approaching that boundary point.

**5. The antipodal identity.** Choose \(\eta\in\partial\mathbb D\) with \(\zeta=\eta^2\). Then
\[p(\eta)=a(\zeta)+\eta\zeta^{-1}b(\zeta),\qquad p(-\eta)=a(\zeta)-\eta\zeta^{-1}b(\zeta).\]
By the parallelogram identity, \(|p(\eta)|^2+|p(-\eta)|^2=2(|a(\zeta)|^2+|b(\zeta)|^2)\). Combining steps 1--4 yields
\[\|B_h\|_{\mathrm e}=\max_{|\eta|=1}\sqrt{|p(\eta)|^2+|p(-\eta)|^2}.\]
Uniform approximation in Step 2 and the fact that essential norm is 1-Lipschitz in operator norm pass this exact equality to every \(\varphi\in C(\overline{\mathbb D})\). Finally, the displayed expression vanishes precisely when the boundary restriction vanishes, proving the compactness assertion.

## Verification
The standalone script `verify.py` checks exact finite basis coefficients for \(W\), \(T_{z^k}\), and \(T_{\overline z^{\,k}}\), parity-channel alignment, and the antipodal/parallelogram identity for several explicit Laurent polynomials. Reproduction: `python3 verify.py`. These finite identities support the concrete formulas; weakly-null packet and compactness arguments above, not finite computation, establish the infinite-dimensional essential-norm claim.

## Relationship to prior work
Cui--Li--Lu, arXiv:2610.09728v1 (first publicly available 2026-10-07), studies commutativity, finite-rank commutators, and zero products for slant Toeplitz operators with polyanalytic/harmonic symbols on Bergman space, using precisely the slant convention \(Wz^{2n}=z^n\). Its inspected statements do not supply the exact essential norm for arbitrary continuous symbols. Singh--Singh--Singh, arXiv:2507.06546v1, studies higher-order slant Bergman operators using a different normalized-basis slant map and discusses spectra and compactness; its inspected definitions and spectral section do not provide this quantitative antipodal Calkin norm. Classical Hardy/Laurent Toeplitz norm theory is a central ingredient, not claimed as new. The new statement is the explicit Bergman slant Calkin norm in terms of antipodal boundary values, with compact asymptotic reduction to a two-channel row operator.

## Limitations
This does not establish an essential spectrum formula, any Schatten singular-value asymptotics, or a result for general measurable symbols. The proof is self-contained modulo elementary Bergman kernel, Fourier approximation, and unilateral Toeplitz facts. An exhaustive survey of older slant Toeplitz literature was not possible; an unlocated equivalent polyphase Calkin formula remains an originality risk. Independent review has not been performed.

## References
1. P. Cui, R. Li, Y. Lu, *Commuting slant Toeplitz operators for polyanalytic and harmonic symbols*, arXiv:2610.09728v1 (first available 2026-10-07), https://arxiv.org/abs/2610.09728.
2. O. N. Singh, M. P. Singh, T. S. Singh, *Algebraic and Spectral properties of slant Toeplitz and slant little Hankel Operators on weighted Bergman Space*, arXiv:2507.06546v1 (2025), https://arxiv.org/abs/2507.06546.
3. M. C. Ho, *Properties of slant Toeplitz operators*, Indiana Univ. Math. J. 45 (1996), 843--862, doi:10.1512/iumj.1996.45.1973 (bibliographic lead; full text not reviewed).
