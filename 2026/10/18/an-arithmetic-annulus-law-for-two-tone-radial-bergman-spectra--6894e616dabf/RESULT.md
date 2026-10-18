# An arithmetic annulus law for two-tone radial Bergman spectra

## Finding

Fix a real parameter \(\alpha>-1\), distinct positive numbers \(\beta,\gamma\), and \(c>0\). On the weighted analytic Bergman space \(A^2_\alpha(\mathbb D)\), let \(T_u\) be the Toeplitz operator with the bounded radial symbol
\[
u(z)=(1-|z|^2)^{i\beta}+c(1-|z|^2)^{i\gamma}.
\]
Write
\[
C_\alpha(t)=\frac{\Gamma(\alpha+1+it)}{\Gamma(\alpha+1)},\qquad
 a=|C_\alpha(\beta)|,\quad b=c|C_\alpha(\gamma)|.
\]
Then the essential spectrum has a sharp arithmetic dichotomy:

**Incommensurable frequencies.** If \(\beta/\gamma\notin\mathbb Q\), then
\[
\sigma_{\mathrm{ess}}(T_u)=\{\zeta\in\mathbb C:|a-b|\le|\zeta|\le a+b\}.
\]
Every point of the *filled annulus* occurs as a limit of Toeplitz eigenvalues. If \(a=b\), this is the full closed disk of radius \(2a\).

**Commensurable frequencies.** If \(\beta/\gamma=p/q\) in lowest positive terms and \(\omega=\beta/p=\gamma/q\), then
\[
\sigma_{\mathrm{ess}}(T_u)=
\left\{C_\alpha(\beta)e^{-ip\theta}+cC_\alpha(\gamma)e^{-iq\theta}:0\le\theta<2\pi\right\}.
\]
This is a compact, real-analytic parametrized curve of planar Lebesgue area zero. In both cases,
\[
\|T_u\|_{\mathrm{ess}}=a+b,\qquad
T_u\text{ is Fredholm}\iff a\ne b,
\]
and every Fredholm instance has index zero. For the unweighted Bergman space,
\[
|C_0(t)|=\sqrt{\frac{\pi t}{\sinh(\pi t)}}\qquad(t>0).
\]
Thus two bounded logarithmic radial oscillations provide an explicit, two-frequency family of operators with genuinely two-dimensional essential spectra, while commensuration collapses these spectra to curves.

## Assumptions and scope

The disk \(\mathbb D\) has normalized area measure \(dA=dx\,dy/\pi\). The space \(A^2_\alpha\) consists of analytic functions square-integrable for the probability measure \((\alpha+1)(1-|z|^2)^\alpha dA\). The symbol is interpreted via \(t^{i\xi}=\exp(i\xi\log t)\) for real \(\xi\) and \(0<t\le1\); it is measurable, bounded by \(1+c\), and need not have a boundary limit. The Toeplitz operator is \(T_uf=P_\alpha(uf)\), where \(P_\alpha\) is the orthogonal Bergman projection. The essential spectrum is the Fredholm essential spectrum. The theorem covers every fixed \(\alpha>-1\), \(\beta,\gamma>0\) with \(\beta\ne\gamma\), and \(c>0\). No assertion is made about arbitrary radial weights or nonradial symbols.

## Proof

**Step 1: Exact diagonalization.** The monomials are complete and mutually orthogonal in \(A^2_\alpha\), with
\[
\|z^n\|^2_\alpha=(\alpha+1)B(n+1,\alpha+1).
\]
As \(u\) is radial, different monomial degrees remain orthogonal after multiplication by \(u\). Consequently \(T_u\) is diagonal in the normalized monomial basis. For each real \(t>0\), the symbol \((1-|z|^2)^{it}\) has eigenvalue
\[
\begin{aligned}
\lambda_n(t)&=\frac{\int_0^1 x^n(1-x)^{\alpha+it}\,dx}{\int_0^1 x^n(1-x)^\alpha\,dx}\\
&=\frac{\Gamma(\alpha+1+it)}{\Gamma(\alpha+1)}
\frac{\Gamma(n+\alpha+2)}{\Gamma(n+\alpha+2+it)}.
\end{aligned}
\]
The eigenvalues of \(T_u\) are exactly \(\lambda_n=\lambda_n(\beta)+c\lambda_n(\gamma)\), for every integer \(n\ge0\). There is no finite-rank approximation in this identity.

**Step 2: Sharp boundary-moment asymptotics.** For fixed \(\alpha>-1\) and real \(t\), the gamma-ratio asymptotic gives
\[
\frac{\Gamma(n+\alpha+2)}{\Gamma(n+\alpha+2+it)}
=n^{-it}(1+O_{\alpha,t}(n^{-1})).
\]
Therefore, for the two fixed frequencies,
\[
\lambda_n=C_\alpha(\beta)e^{-i\beta\log n}
+cC_\alpha(\gamma)e^{-i\gamma\log n}+O(n^{-1})
\qquad(n\to\infty).
\]
The gamma function has no zeros, so \(a,b>0\). When \(\alpha=0\), the gamma reflection identity gives \(|\Gamma(1+it)|^2=\pi t/\sinh(\pi t)\).

**Step 3: Sampling a linear torus flow at logarithmic times.** The mesh
\[
\log(n+1)-\log n=\log(1+n^{-1})\longrightarrow0.
\]
Let \(F(s)=(e^{-i\beta s},e^{-i\gamma s})\) in \(\mathbb T^2\). Every accumulation point of \(F(\log n)\) lies in the closure of the positive continuous orbit. Conversely, take any target of that orbit closure. For rational \(\beta/\gamma\), the orbit is periodic, and for irrational \(\beta/\gamma\), Kronecker's theorem makes every positive tail dense in \(\mathbb T^2\). In either case there are times \(s_j\to\infty\) with \(F(s_j)\) tending to the target. Choosing integers \(n_j\) nearest to \(e^{s_j}\) gives \(\log n_j-s_j\to0\), hence \(F(\log n_j)\) has the same limit. Thus the sampled tail-cluster set equals the continuous orbit closure.

**Step 4: Exact geometry of the limit set.** In the commensurable case write \(\beta=p\omega\), \(\gamma=q\omega\) with coprime positive integers \(p,q\), so the orbit closure is \(\{(e^{-ip\theta},e^{-iq\theta}):\theta\in[0,2\pi]\}\). Its image under \((v,w)\mapsto C_\alpha(\beta)v+cC_\alpha(\gamma)w\) is exactly the claimed curve. Since this parametrization is smooth on a compact one-dimensional domain, its two-dimensional Lebesgue measure is zero.

In the incommensurable case the orbit closure is all of \(\mathbb T^2\). Its image is the Minkowski sum of centered circles of radii \(a\) and \(b\). The triangle and reverse-triangle inequalities give \(|a-b|\le|\zeta|\le a+b\). Conversely, the law of cosines realizes every intermediate radius, and a simultaneous common rotation realizes every argument. Hence the image is the entire closed annulus.

**Step 5: Essential spectrum, norm and Fredholm property.** For a bounded diagonal operator on an orthonormal basis, the Fredholm essential spectrum is exactly the cluster set of its eigenvalue sequence at indices tending to infinity: points outside that set have a uniformly bounded inverse on a cofinite tail, whereas points inside it admit weakly null unit approximate eigenvectors. The \(O(n^{-1})\) error from Step 2 does not change this cluster set. The displayed spectral formulas follow. The greatest modulus in each set equals \(a+b\): both free phases can be aligned in the irrational case, while in the rational case the relative phase \((p-q)\theta\) spans the circle because \(p\ne q\). The smallest modulus is \(|a-b|\) in either case, by aligning the two terms oppositely. Therefore zero belongs to the essential spectrum precisely when \(a=b\); equivalently, Fredholmness holds precisely for \(a\ne b\). A Fredholm diagonal operator has equal finite-dimensional kernel and cokernel, so its index is zero.

## Verification

The accompanying standalone \(verify.py\) checks five direct beta-moment integrals independently against the gamma quotient, five beta/gamma normalization identities, nine large-degree asymptotic instances, 123 annulus-radius constructions, and 93 rational-orbit periodicity identities. Running \(python verify.py\) prints `VERIFY_OK`. The all-degree theorem is proved by the gamma identity, the torus-density argument, and diagonal Fredholm theory; these finite computations are checks, not substitutes for those arguments.

## Relationship to prior work

Li and Wang's 2026 compactness theorem on radial weighted Bergman spaces characterizes compactness of bounded-symbol Toeplitz operators through boundary Berezin transforms, without giving the present two-tone essential-spectrum classification. Suárez (2007) proves a general characterization of radial Toeplitz eigenvalue sequences and exhibits arbitrary connected compact essential spectra for operators in the closure of radial Toeplitz operators; this does not prescribe the elementary symbols, attenuation radii or rational/irrational area dichotomy here. Maximenko and Pacheco (2025) establish diagonalization and logarithmic Lipschitz regularity of radial spectral sequences, but not this exact gamma-attenuated spectral geometry. Earlier work by Grudsky and Vasilevski (2001) establishes that radial Toeplitz essential spectra can have nonempty interior. The accessible abstract does not resolve whether that paper contains this specific two-frequency construction, which remains a historical-priority risk.

## Limitations

The theorem concerns the Fredholm essential spectrum, not an exact formula for the complete spectrum, which can also include finite-index eigenvalues. The arithmetic dichotomy concerns a precise two-tone symbol; it does not extend without further arguments to other bounded radial symbols. The proof is a self-review, not independent validation. The 2001 Grudsky–Vasilevski full text was not accessible during the comparison, so historical priority is qualified. The result does not strengthen the general compactness criterion or the general existence theorem for connected essential spectra.

## References

1. Y. Li and Z. Wang, *Compact Toeplitz operators on radial weighted Bergman spaces*, arXiv:2608.23733, first submitted 2026-08-24, https://arxiv.org/abs/2608.23733.
2. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, arXiv:0710.0797 (2007), https://arxiv.org/abs/0710.0797; Bull. Lond. Math. Soc. 40 (2008), 631–641.
3. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649 (2025), https://arxiv.org/html/2503.23649v1.
4. S. Grudsky and N. Vasilevski, *Bergman–Toeplitz operators: radial component influence*, Integral Equations Operator Theory 40 (2001), 16–33, https://doi.org/10.1007/BF01202952 (full-text comparison incomplete).
