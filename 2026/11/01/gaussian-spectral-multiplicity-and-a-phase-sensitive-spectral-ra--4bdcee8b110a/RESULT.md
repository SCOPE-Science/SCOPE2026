# Gaussian spectral multiplicity and a phase-sensitive spectral-radius boundary for Fock weighted compositions

## Finding

Let \(\mathcal F^2\) be the complex Bargmann–Fock space with squared norm
\[
\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z).
\]
Fix \(a,\tau\in\mathbb C\) with \(0<|a|<1\) and \(2|\tau|=1-|a|^2\), and put \(q=|a|^2\). Define \((Wf)(z)=e^{\tau z^2}f(az)\). The formula defines a bounded operator. There is a unitary map \(V:\mathcal F^2\to L^2(\mathbb R)\) for which
\[
V W^*W V^{-1}=M_m,\qquad m(x)=q^{-1/2}e^{-(1-q)x^2}.
\]
Consequently \(\sigma(W^*W)=\sigma_{\mathrm{ess}}(W^*W)=[0,q^{-1/2}]\), and this spectrum is purely absolutely continuous of multiplicity two on its interior. The pushforward of Lebesgue measure under \(m\) has density
\[
\frac{d\nu}{d\lambda}=\frac{1}{\sqrt{1-q}\,\lambda\sqrt{\log(q^{-1/2}/\lambda)}},\qquad 0<\lambda<q^{-1/2}.
\]
In particular \(\|W\|=\|W\|_{\mathrm{ess}}=q^{-1/4}\); neither \(W\) nor \(W^*W\) has a norming eigenvector.

The ordinary and essential spectral radii depend discontinuously on the *phase* of \(a\), although the entire singular-modulus spectral type above depends only on \(|a|\):

* If \(a\notin\mathbb R\), then \(W^2\) is Hilbert–Schmidt, \(\sigma(W)=\{0\}\cup\{a^n:n=0,1,2,\ldots\}\), \(r(W)=1\), and \(r_{\mathrm{ess}}(W)=0\). Every nonzero eigenvalue has geometric multiplicity one.
* If \(a\in\mathbb R\), then \(\|W^n\|=\|W^n\|_{\mathrm{ess}}=q^{-n/4}\) for every positive integer \(n\), so \(r(W)=r_{\mathrm{ess}}(W)=q^{-1/4}>1\), and \(W\) has no eigenvalues.

For \(0\le r<1\), the subcritical operators \((W_r f)(z)=e^{r\tau z^2}f(az)\) are Hilbert–Schmidt and converge strongly to \(W\) as \(r\uparrow1\), while
\[
\|W-W_r\|_{\mathrm{ess}}=q^{-1/4}\quad\text{for every }0\le r<1.
\]
Thus strong approximation across the endpoint preserves a positive, exactly known Calkin-norm gap.

## Assumptions and scope

The Hilbert space is the one-dimensional standard Gaussian Fock space over \(\mathbb C\). The exponent is exactly on the bounded/noncompact boundary \(2|\tau|=1-|a|^2\) with \(a\ne0\); neither an affine translation nor a linear exponential factor is included. Spectral multiplicity and absolute continuity refer to the self-adjoint operator \(W^*W\), not to the nonnormal operator \(W\). The essential spectrum is the Fredholm essential spectrum. The essential radius is the spectral radius of the image in the Calkin algebra.

## Proof

**1. Gaussian kernel and bounded extension.** For the Fock reproducing kernels \(K_w(z)=e^{z\overline w}\), their images under the displayed formula are \(WK_w(z)=\exp(\tau z^2+az\overline w)\), which lie in \(\mathcal F^2\) because \(2|\tau|<1\). The elementary complex Gaussian integral gives
\[
\langle WK_w,WK_z\rangle
= D^{-1/2}\exp\!\left(
 A z\overline w+Bz^2+\overline B\,\overline w^2\right),
\quad D=1-4|\tau|^2,\quad A=\frac{q}{D},\quad B=\frac{\tau\overline a^{\,2}}{D}.
\]
At the stated boundary, \(D=q(2-q)\), \(A=(2-q)^{-1}\), \(|B|=(1-q)/(2(2-q))\), and \(D^{-1/2}=q^{-1/2}/\sqrt{2-q}\). Choose the unitary Fock rotation \((R_\theta f)(z)=f(e^{i\theta}z)\) so that \(e^{2i\theta}B=-|B|\). The rotated kernel is therefore
\[
G(z,w)=\frac{q^{-1/2}}{\sqrt{2-q}}\exp\!\left(
\frac{z\overline w}{2-q}-\frac{1-q}{2(2-q)}(z^2+\overline w^2)\right).
\]

The unitary Segal–Bargmann transform \(\mathcal B:L^2(\mathbb R)\to\mathcal F^2\) is
\[
(\mathcal B h)(z)=\pi^{-1/4}\int_{\mathbb R}
 e^{-x^2/2+\sqrt2zx-z^2/2}h(x)\,dx.
\]
Completing the square shows that \(\mathcal B M_m\mathcal B^{-1}\), for the claimed \(m\), has exactly kernel \(G\). Thus, on the dense span of the \(K_w\), the quadratic form induced by \(W\) equals that of the bounded positive operator \(R_\theta^{-1}\mathcal B M_m\mathcal B^{-1}R_\theta\). This bounds \(W\), extends it uniquely to all of \(\mathcal F^2\), and proves the unitary equivalence with \(V=\mathcal B^{-1}R_\theta\). Point evaluation extends the original weighted-composition formula.

**2. Spectral type and essential norm.** The function \(m\) is continuous, positive, even, tends to zero at infinity, and is strictly decreasing on \((0,\infty)\). A nonzero multiplication operator by \(m\) on nonatomic \(L^2(\mathbb R)\) has essential range \([0,q^{-1/2}]\), has no eigenvalues, and is noncompact. The substitution \(\lambda=q^{-1/2}e^{-(1-q)x^2}\) gives the stated spectral-measure density and two inverse branches. Every scalar spectral measure is absolutely continuous. The Calkin norm satisfies \(\|W\|_{\mathrm{ess}}^2=\|W^*W\|_{\mathrm{ess}}=q^{-1/2}\); the ordinary norm follows identically. Equality in the multiplication norm would require an \(L^2\) function supported on \(\{0\}\), so the norm is not attained.

**3. Power-compact and non-power-compact phases.** Direct composition yields
\[
(W^n f)(z)=\exp\!\left(\tau\sum_{j=0}^{n-1}a^{2j}z^2\right)f(a^n z).
\]
For any \(b,c\in\mathbb C\) with \(0<|b|<1\), a direct Gaussian integration gives
\[
\|f\mapsto e^{cz^2}f(bz)\|_{\mathcal S_2}^2
=\bigl((1-|b|^2)^2-4|c|^2\bigr)^{-1/2}
\]
when \(2|c|<1-|b|^2\). If \(a\notin\mathbb R\), strict triangle inequality implies
\[
2|\tau(1+a^2)|=(1-q)|1+a^2|<(1-q)(1+q)=1-q^2,
\]
so \(W^2\) is Hilbert–Schmidt. Put \(\gamma=\tau/(1-a^2)\). Because \(|1-a^2|>1-q\), one has \(|\gamma|<1/2\), and all \(e^{\gamma z^2}z^n\) belong to \(\mathcal F^2\) and are eigenvectors of \(W\) with eigenvalues \(a^n\). Conversely, for any nonzero eigenvalue \(\lambda\), division by \(e^{\gamma z^2}\) reduces the eigenvalue equation to \(g(az)=\lambda g(z)\). Comparing Taylor coefficients forces \(\lambda=a^n\) and a one-dimensional eigenspace. Since \(W^2\) is compact, power-compact spectral theory rules out all other nonzero spectrum. The Calkin square vanishes and \(r_{\mathrm{ess}}(W)=0\).

If \(a\) is real, the same power formula has the critical parameter \(2|\tau\sum_{j=0}^{n-1}a^{2j}|=1-q^n\). Applying the first two steps with the new contraction \(a^n\) yields \(\|W^n\|=\|W^n\|_{\mathrm{ess}}=q^{-n/4}\); the spectral-radius formula and Calkin version follow by taking \(n\)-th roots. In this real case \(|\gamma|=1/2\). Every nonzero candidate eigenfunction would be \(e^{\gamma z^2}z^n\), none of which belongs to \(\mathcal F^2\); injectivity excludes zero as an eigenvalue.

**4. Strong but not norm convergence.** For \(r<1\), the strict inequality \(2r|\tau|<1-q\) and the Hilbert–Schmidt formula above prove compactness. For any \(f\in\mathcal F^2\), pointwise convergence is immediate. The integrable majorant
\[
|e^{r\tau z^2}f(az)|^2\le |f(az)|^2+|e^{\tau z^2}f(az)|^2
\]
holds since \(0\le r\le1\). Dominated convergence proves strong convergence. Since the difference of \(W\) and a compact operator has the same Calkin image as \(W\), its essential norm is exactly \(q^{-1/4}\). This also proves failure of operator-norm convergence.

## Verification

A standalone `verify_endpoint_gaussian.py` checks the rotated kernel against the Gaussian Segal–Bargmann multiplier kernel at random complex arguments and several parameters, the critical normalizations of real powers, the strict phase-gap inequalities, and an interior finite-section singular-value consistency calculation. Execute with `python verify_endpoint_gaussian.py` using Python 3, NumPy and SciPy installed. The current program reports 169 successful finite checks. These finite checks are ancillary to the analytic proof; they do not prove the infinite-dimensional spectrum or source novelty.

## Relationship to prior work

Barik, Sen and Paul (2026) characterize weighted-composition boundedness, compactness, Hilbert–Schmidt membership and estimate essential norms; the exact endpoint Calkin norm, continuous-modulus spectral type and phase-sensitive spectral-radius dichotomy are beyond the inspected claims. Sang and Zhao (2026) give a complex-symmetry classification and eigenvalue methods, including critical noncompact operators with compact squares; that qualitative mechanism is credited here, while the phase-blind *singular-modulus* multiplicity and exact real-versus-nonreal radii form the present statement. Le (2014) supplies classical boundedness/compactness characterization. Dong and Zhu (2025) prove complete geometric singular-value formulas for compact canonical Gaussian integral operators. Subcritical Gaussian weighted compositions can be reduced to that compact setting after scalar normalization: their compact singular-value theorem is **not** claimed as new here. At the critical endpoint the resulting canonical parameters escape their bounded family and the modulus has continuous rather than discrete spectrum. The exact endpoint statement is not contained in those inspected canonical theorems. Related general essential-norm bounds by Al-Rawashdeh (2015) were accessible at abstract level; exact applicability has residual priority risk.

## Limitations

The result concerns a centered quadratic exponential weight and scalar contraction in one complex dimension. It does not compute the full ordinary spectrum of \(W\) for real \(a\), only its spectral radius and lack of eigenvalues. The spectral multiplicity theorem is for \(W^*W\), not \(W\). Older general Gaussian operator theory could encode a reduction not explicitly present in the inspected weighted-composition literature; publication priority remains to be independently assessed. No independent mathematical audit has been performed.

## References

1. S. Barik, A. Sen, K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1 (first public 2026-07-19).
2. Y. Sang, L. Zhao, *A Characterization of Complex Symmetric Weighted Composition Operators on the Fock Space*, arXiv:2608.13832v1 (first public 2026-08-13).
3. X. Dong, K. Zhu, *Canonical integral operators on the Fock space II*, arXiv:2509.16672v1 (first public 2025-09-20).
4. T. Le, *Normal and isometric weighted composition operators on the Fock space*, Bulletin of the London Mathematical Society 46 (2014), 847–856, DOI:10.1112/blms/bdu046.
5. W. Al-Rawashdeh, *Essential norm of weighted composition operators on Bargmann-Fock spaces*, Advances in Inequalities and Applications (2015), article 6.
6. I. Chalendar, J. R. Partington, *Weighted composition operators on Fock spaces and their dynamics*, arXiv:1911.07254 (2019 preprint, 2023 publication).
