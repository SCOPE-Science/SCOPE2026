# Antipodal atomic Fock Toeplitz spectra have a sharp majorization reversal

## Finding

Let \(d\ge1\), \(\alpha>0\), and \(a\in\mathbb C^d\setminus\{0\}\). For arbitrary positive masses \(m_+,m_->0\), put \(\mu=m_+\delta_a+m_-\delta_{-a}\). Let \(T_\mu^{\mathrm h}\) and \(T_\mu^{\mathrm{ph}}\) be the positive Toeplitz operators induced by \(\mu\), respectively on the holomorphic and pluriharmonic Gaussian Fock Hilbert spaces with Gaussian scale \(\alpha\). Set

\[
t=\frac{\|a\|^2}{\alpha},\qquad u=e^{-t},\qquad D=2-u,\qquad t_*=\log(2+\sqrt3).
\]

Both operators have exactly two positive eigenvalues. If their eigenvalue lists (padded by zeros) are denoted by \(\lambda^\downarrow\), their *normalized spectral majorization* satisfies the sharp trichotomy

\[
\begin{cases}
\lambda^\downarrow(T_\mu^{\mathrm h})\succ\lambda^\downarrow(T_\mu^{\mathrm{ph}}/D),&0<t<t_*,\\
\lambda^\downarrow(T_\mu^{\mathrm h})=\lambda^\downarrow(T_\mu^{\mathrm{ph}}/D),&t=t_*,\\
\lambda^\downarrow(T_\mu^{\mathrm{ph}}/D)\succ\lambda^\downarrow(T_\mu^{\mathrm h}),&t>t_*.
\end{cases}
\]

Here \(x\succ y\) means that their total sums agree and each leading partial sum of \(x\) is at least that of \(y\); the strict cases have a strict first partial-sum inequality. In particular, for **every** real \(p>1\), the strict Schatten comparison \(\|T_\mu^{\mathrm{ph}}\|_{S_p}<D\|T_\mu^{\mathrm h}\|_{S_p}\) holds below \(t_*\), whereas the inequality reverses above \(t_*\). For **every** \(0<p<1\), the corresponding inequalities reverse again. At \(p=1\) there is equality for all \(t>0\). At \(t=t_*\), \(T_\mu^{\mathrm{ph}}/D\) and \(T_\mu^{\mathrm h}\) have the same nonzero spectrum for all positive masses, and all their Schatten norms and unitarily invariant ideal norms coincide. The same majorization comparison applies to the operator norm, strictly away from \(t_*\).

The threshold is independent of the two masses, of dimension, and of Schatten exponent. At the degenerate endpoint \(a=0\), both point masses merge into one; the two operators then agree, and the strict trichotomy does not apply.

## Assumptions and scope

The Gaussian holomorphic Fock Hilbert space \(F_\alpha^2(\mathbb C^d)\) is normalized by the probability measure \((\pi\alpha)^{-d}e^{-\|z\|^2/\alpha}\,dV(z)\). Its reproducing kernel is

\[
K_{\mathrm h}(z,w)=\exp(z\cdot\overline w/\alpha).
\]

The pluriharmonic space is the closed complex Hilbert subspace of square-integrable functions of the form \(g+\overline h\) with \(g,h\) entire, \(h(0)=0\), with the norm inherited from the Gaussian \(L^2\) space. Its kernel is

\[
K_{\mathrm{ph}}(z,w)=K_{\mathrm h}(z,w)+\overline{K_{\mathrm h}(z,w)}-1.
\]

For either space \(H\), its positive Toeplitz operator is defined by the finite positive form

\[
\langle T_\mu^H f,g\rangle_H=\sum_{\varepsilon\in\{-1,1\}}m_{\varepsilon}\,e^{-t}\,f(\varepsilon a)\,\overline{g(\varepsilon a)}.
\]

Here \(m_{+1}=m_+\) and \(m_{-1}=m_-\). The Schatten quasi-norm for \(0<p<1\) is understood as \((\sum_j s_j(T)^p)^{1/p}\). All claims are for exactly two distinct antipodal atoms of strictly positive masses and the stated Gaussian normalization.

## Proof

For either reproducing-kernel Hilbert space, introduce the weighted evaluation map

\[
E_Hf=\bigl(\sqrt{m_+}e^{-t/2}f(a),\sqrt{m_-}e^{-t/2}f(-a)\bigr).
\]

Then \(T_\mu^H=E_H^*E_H\), and the nonzero eigenvalues, including multiplicity, equal those of the positive Gram matrix \(E_HE_H^*\). The kernel formulas above give, with \(q=u(2u-1)\),

\[
G_{\mathrm h}=\begin{pmatrix}m_+&\sqrt{m_+m_-}\,u^2\\\sqrt{m_+m_-}\,u^2&m_-\end{pmatrix},
\qquad
G_{\mathrm{ph}}=\begin{pmatrix}Dm_+&\sqrt{m_+m_-}\,q\\\sqrt{m_+m_-}\,q&Dm_-\end{pmatrix}.
\]

The two strictly positive eigenvalues are, writing \(s=m_++m_-\) and \(\Delta=m_+-m_-\),

\[
\lambda_\pm(T_\mu^{\mathrm h})=\frac{s\pm\sqrt{\Delta^2+4m_+m_-u^4}}2,
\]

\[
\lambda_\pm(T_\mu^{\mathrm{ph}})=\frac{Ds\pm\sqrt{D^2\Delta^2+4m_+m_-q^2}}2.
\]

Their positivity follows from \(1-u^4>0\) and \(D^2-q^2=4(1-u^2)(1-u+u^2)>0\), respectively. The normalized matrices \(G_{\mathrm h}\) and \(G_{\mathrm{ph}}/D\) have the same trace \(s\), whereas their determinant difference is exactly

\[
\det G_{\mathrm h}-\det(G_{\mathrm{ph}}/D)
=m_+m_-\left(\frac{q^2}{D^2}-u^4\right)
=\frac{m_+m_-u^2(1-u^2)}{(2-u)^2}(u^2-4u+1).
\]

Because \(0<u<1\), the last factor has exactly one zero in the allowed interval, namely \(u_*=2-\sqrt3\), corresponding to \(t_*=\log(2+\sqrt3)\). It is negative when \(0<t<t_*\), and positive when \(t>t_*\). For two positive eigenvalues with fixed sum, smaller determinant means larger largest eigenvalue and thus strict majorization. This proves all three cases, including sharpness and mass independence.

The scalar function \(x\mapsto x^p\) is strictly convex on \((0,\infty)\) for \(p>1\), strictly concave for \(0<p<1\), and linear for \(p=1\). Two-coordinate majorization therefore gives all stated strict Schatten directions and trace equality; leading-eigenvalue comparison gives the operator-norm direction. At the unique positive threshold, \(q=-Du^2\), so \(G_{\mathrm{ph}}/D\) is conjugate to \(G_{\mathrm h}\) by the diagonal unitary \(\operatorname{diag}(1,-1)\). This independently proves full eigenvalue equality there, not merely trace equality.

## Verification

The algebraic determinant factorization, the two required positivity identities, and direct numerical eigenvalue comparisons were independently checked using the included `CHECK.py` program. Run `python CHECK.py` with Python 3, NumPy, and SymPy installed. The checker reports three exact symbolic identities and 1,296 finite spectral/Schatten diagnostics across radii, positive mass ratios, and exponents on both sides of the transition, including the critical radius. These checks are supporting diagnostics; the analytic matrix calculation and majorization argument prove the universal statement.

## Relationship to prior work

Looi's arXiv:2608.13550v1 (August 13, 2026), Theorem 1.1 and Corollary 1.2, prove general optimal but radius-independent holomorphic/pluriharmonic Schatten and symmetric-ideal norm comparisons; Proposition 6.1 gives an exact trace identity, and Proposition 6.2 uses a *single* point mass and circle measures to establish sharp constants. The one-point formula determines the natural normalization \(D\), but does not state how the spectra of *two* positive atoms compare after this normalization. The present complete two-atom majorization trichotomy is a different question. Jaguzović and Vujadinović, arXiv:2605.23256v1 (May 22, 2026), establish boundedness, compactness, and trace-class properties of positive pluriharmonic Fock Toeplitz forms, not the antipodal two-point crossover. Fulsche, arXiv:1901.02644v1 (January 9, 2019), investigates quantization and essential spectra for other symbol classes, not positive two-atom spectral majorization.

## Limitations

This result does not optimize the norm ratio over all positive measures on a sphere or ball and does not classify two arbitrary non-antipodal positions, three or more atoms, or signed measures. Its strict comparisons require both masses positive and the locations distinct. The threshold is a direct, exact consequence of the two known reproducing kernels and finite-dimensional spectral algebra; claims of independent publication priority remain subject to external review.

## References

1. S. Looi, *Positive Toeplitz operators on pluriharmonic Fock spaces: Schatten class criteria, sharp norm comparisons, and generalized weights*, arXiv:2608.13550v1 (2026), Sections 1–2, 4–6, https://arxiv.org/abs/2608.13550.
2. V. Jaguzović and Đ. Vujadinović, *Toeplitz operators on pluriharmonic Fock spaces*, arXiv:2605.23256v1 (2026), Sections 2–3, https://arxiv.org/abs/2605.23256.
3. R. Fulsche, *Toeplitz operators on pluriharmonic function spaces: deformation quantization and spectral theory*, arXiv:1901.02644v1 (2019), Sections 2–5, https://arxiv.org/abs/1901.02644.
4. K. Fan, *Maximum properties and inequalities for the eigenvalues of completely continuous operators*, Proc. Natl. Acad. Sci. USA 37 (1951), 760–766, https://doi.org/10.1073/pnas.37.11.760.
