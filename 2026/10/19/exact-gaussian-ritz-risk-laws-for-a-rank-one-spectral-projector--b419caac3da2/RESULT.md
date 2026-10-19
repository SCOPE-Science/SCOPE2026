# Exact Gaussian Ritz risk laws for a rank-one spectral projector

## Finding

Let \(n\ge m+1\ge3\), let \(v\in\mathbb C^n\) be a unit vector, and let \(\mathcal W\subset\mathbb C^n\) be any \(m\)-dimensional subspace with \(0<\theta:=\angle(v,\mathcal W)<\pi/2\). Set \(A=I-vv^*\), \(\alpha=\sin^2\theta\), and \(k=m-1\). Draw \(\Omega\in\mathbb C^{n\times m}\) with independent standard circular complex-normal entries, and compute the generalized eigenpairs of the square Petrov--Galerkin pencil \(\Omega^*(A-\mu I)W\), where \(W\) is any orthonormal basis of \(\mathcal W\).

Almost surely, the pencil has eigenvalue \(1\) with multiplicity \(m-1\) and exactly one other eigenvalue \(\mu\). For an eigenvector \(y\) corresponding to \(\mu\), define the **refined randomized Ritz value** \(\rho=(Wy)^*A(Wy)/\|Wy\|^2\). The complete marginal laws are

\[
\mu\ \overset{\mathrm d}=\ \alpha+\sqrt{\alpha(1-\alpha)}\,Z,
\quad f_Z(z)=\frac{1}{\pi(1+|z|^2)^2}\quad (z\in\mathbb C),
\]

\[
\rho\ \overset{\mathrm d}=\ \frac{\alpha}{\alpha+(1-\alpha)U},
\qquad U\sim\operatorname{Beta}(1,k).
\]

Consequently, for \(\alpha\le t<1\), the **exact** refined-value distribution and its mean are

\[
\Pr\{\rho\le t\}=\left(\frac{t-\alpha}{(1-\alpha)t}\right)^k,
\]

\[
\mathbb E\rho
=\frac{k\alpha}{(1-\alpha)^k}
\left[\log\frac1\alpha-\sum_{j=1}^{k-1}\frac{(1-\alpha)^j}{j}\right].
\]

The distribution function is \(0\) below \(\alpha\) and \(1\) at or above \(1\); the sum is empty for \(k=1\). For every \(p\in(0,2)\),

\[
\mathbb E|\mu-\alpha|^p
=[\alpha(1-\alpha)]^{p/2}
\Gamma(1+p/2)\Gamma(1-p/2),
\]

whereas this centered moment is infinite for every \(p\ge2\). In particular, \(\mathbb E\mu=\alpha\) exists but \(\mathbb E|\mu|^2=\infty\) for every \(0<\alpha<1\).

For fixed \(m\) as \(\alpha\downarrow0\), writing \(H_0=0\) and \(H_j=\sum_{r=1}^j 1/r\),

\[
\mathbb E\rho
=k\alpha\bigl(\log(1/\alpha)-H_{k-1}\bigr)
+O_m\bigl(\alpha^2\log(1/\alpha)\bigr).
\]

The ordinary (deterministic) Rayleigh--Ritz approximation to the zero eigenvalue in the **same** trial subspace is exactly \(\alpha\). Thus the expected refined randomized approximation loses an unbounded factor \(\sim k\log(1/\alpha)\) compared with the deterministic Ritz value, despite convergence of individual sketches at the usual quadratic order with high probability.

There is also a sharp joint dimension--angle law. For \(k=m-1\to\infty\), \(\alpha_m\to0\), and \(k\alpha_m\to\tau\in(0,\infty)\),

\[
\rho_m\ \Rightarrow\ \frac{\tau}{\tau+E},
\qquad E\sim\operatorname{Exp}(1).
\]

If \(k\alpha_m\to0\), then \(\rho_m\to0\) in probability; if \(k\alpha_m\to\infty\), then \(\rho_m\to1\) in probability. More generally, under \(\alpha_m\to0\), convergence \(\rho_m\to0\) in probability (equivalently, in mean) holds **if and only if** \((m-1)\alpha_m\to0\). The positive finite-\(\tau\) limit has mean \(\tau e^\tau E_1(\tau)\), where \(E_1(\tau)=\int_\tau^\infty e^{-u}\,du/u\).

## Assumptions and scope

All random variables and linear-algebra operations are over \(\mathbb C\), and the Gaussian entries have independent real and imaginary parts each of variance \(1/2\). A single square Gaussian test pencil is used, without oversampling, clipping, or regularization. The target eigenvalue \(0\) of the rank-one-complement projector \(A=I-vv^*\) is simple; its other eigenvalue is \(1\) with multiplicity \(n-1\). The target Ritz branch is defined as the eigenvalue distinct from the persistent eigenvalue \(1\), not by a possibly ambiguous nearest-value sorting rule. Every \(m\)-dimensional trial space with the stated angle is included, and the ambient dimension \(n\) can be arbitrarily larger than \(m\). Statements at the excluded endpoints \(\alpha=0,1\) are not asserted by continuity of eigenpair multiplicities.

## Proof

**1. Canonical basis and randomized kernel.** Normalize the projection of \(v\) onto \(\mathcal W\) and extend it to an orthonormal basis of \(\mathcal W\). Unitary invariance then permits coordinates in which \(v=e_1\), \(w_1=ce_1+se_{m+1}\), \(w_j=e_j\) for \(2\le j\le m\), where \(s=\sqrt\alpha\) and \(c=\sqrt{1-\alpha}\). The matrix is \(A=\operatorname{diag}(0,1,\ldots,1)\). Only the first \(m+1\) rows of \(\Omega\) affect the pencil. Their conjugate transpose has a one-dimensional kernel almost surely; by unitary invariance this kernel line is distributed as the span of \(h=(h_1,\ldots,h_{m+1})\), whose coordinates are independent standard circular complex Gaussians. This is a distributional representation of the random kernel, not an assertion that \(h\) is independent of the pencil.

**2. Exact eigenpair.** For the branch \(\mu\ne1\), write its trial vector as \(x=w_1+\sum_{j=2}^m z_je_j\). The condition \(\Omega^*(A-\mu I)x=0\) is equivalent to \((A-\mu I)x\) belonging to the kernel line of the restricted sketch. Equating coordinates gives

\[
 z_j=s\frac{h_j}{h_{m+1}}\quad(2\le j\le m),
\qquad
 \mu=\frac{s h_1}{s h_1-c h_{m+1}}.
\]

The denominators vanish with probability zero. The other \(m-1\) trial directions are exact eigenvectors of \(A\) with eigenvalue \(1\), so this accounts for all eigenvalues, with the claimed multiplicities almost surely.

**3. Complex Cauchy law.** Set \(V=sh_1-ch_{m+1}\) and \(\Xi=ch_1+sh_{m+1}\). They are independent standard circular complex Gaussians, and \(h_1=sV+c\Xi\). Therefore \(\mu=\alpha+sc\,\Xi/V\). A change of variables \((V,\Xi)\mapsto(V,Z=\Xi/V)\), whose real Jacobian is \(|V|^2\), gives \(f_Z(z)=1/[\pi(1+|z|^2)^2]\). Polar integration yields the displayed gamma-product moments for \(p<2\) and divergence for \(p\ge2\). Rotational symmetry plus integrability establishes \(\mathbb E\mu=\alpha\).

**4. Refined-value beta law.** Let \(X=\sum_{j=2}^m|h_j|^2\sim\operatorname{Gamma}(k,1)\) and \(Y=|h_{m+1}|^2\sim\operatorname{Gamma}(1,1)\), independently. Since \(\|x\|^2=1+\alpha X/Y\) and \(x^*Ax=\alpha+\alpha X/Y\),

\[
\rho=\frac{\alpha(X+Y)}{Y+\alpha X}
=\frac{\alpha}{\alpha+(1-\alpha)U},
\qquad U=\frac{Y}{X+Y}\sim\operatorname{Beta}(1,k).
\]

The beta cumulative distribution \(\Pr\{U\le u\}=1-(1-u)^k\) gives the claimed \(\rho\) distribution by a decreasing transformation. Integrating the beta density and substituting \(t=1-u\) gives

\[
\mathbb E\rho=k\alpha\int_0^1\frac{t^{k-1}}{1-(1-\alpha)t}\,dt,
\]

which evaluates exactly to the finite-sum expression. Expanding at fixed \(k\) proves the logarithmic term and harmonic-number constant. In canonical coordinates the ordinary compressed matrix \(W^*AW\) is \(\operatorname{diag}(\alpha,1,\ldots,1)\); hence its smallest Ritz value is \(\alpha\).

**5. Joint dimensional limit and necessity.** For \(U_k\sim\operatorname{Beta}(1,k)\), \(\Pr\{kU_k>t\}=(1-t/k)^k\to e^{-t}\) for each fixed \(t\ge0\), so \(kU_k\Rightarrow E\sim\operatorname{Exp}(1)\). Since \(\rho_k=k\alpha_k/[k\alpha_k+(1-\alpha_k)kU_k]\), the three stated limit regimes follow. To see necessity for consistency, the exact median is \(\alpha_k/[1-(1-\alpha_k)2^{-1/k}]\); along any subsequence with \(k\alpha_k\) bounded away from zero, these medians stay bounded away from zero. Finally, boundedness \(0\le\rho_k\le1\) makes convergence in probability to zero equivalent to convergence of the mean to zero.

## Verification

The standalone standard-library script `VERIFY.py` checks the Petrov--Galerkin eigenpair identities against independently drawn Gaussian test matrices, tests the beta CDF and mean by Monte Carlo and numerical quadrature, and checks the fixed-dimensional and joint-dimensional asymptotics. Its reported checks are finite numerical corroboration; the analytic proof above supplies the exact distributional statements. Replay with `python VERIFY.py`.

## Relationship to prior work

Shao's randomized Rayleigh--Ritz (RRR) method uses a square Gaussian Petrov--Galerkin pencil, followed by Rayleigh-quotient refinement. Its 2026 analysis establishes high-probability linear eigenvector and quadratic Hermitian refined-value accuracy, together with a square-Gaussian \(\delta^{-1/2}\) tail scale. The present theorem instead computes the entire eigenvalue and refined-value distributions on **all** trial subspaces of a natural projector class and identifies a sharp logarithmic expected-risk loss and dimension--angle consistency threshold. Those exact statements are not obtained by replacing a probabilistic upper bound with equality. Nakatsukasa and Tropp's earlier sketched Rayleigh--Ritz framework typically uses an oversampled subspace embedding; its general residual comparisons do not yield these square-pencil distributional laws. Classical beta--gamma and Gaussian-ratio identities are used as explicit steps in the proof and are not claimed as new probability distributions in themselves.

## Limitations

The theorem concerns an exact rank-one-complement Hermitian projector, circular complex Gaussian sketches, the eigenvalue branch distinct from \(1\), and the specified Rayleigh-quotient refinement. It does not assert identical distributions for arbitrary Hermitian spectra, real Gaussian sketches, oversampled or regularized pencils, floating-point sorting rules, or independent repetitions and robust aggregations. The unrefined Ritz values may be complex even though \(A\) is Hermitian. The marginal laws do not imply that \(\mu\) and \(\rho\) are independent. Bibliographic noncoverage is subject to ordinary unindexed-source risk; no external independent validation is asserted.

## References

1. N. Shao, *Stabilizing the Rayleigh--Ritz procedure by randomization*, arXiv:2604.01037v3 (2026), first publicly submitted 1 April 2026, https://arxiv.org/html/2604.01037v3; especially Algorithm 1, Theorems 2--3, and Section 5.3.
2. Y. Nakatsukasa and J. A. Tropp, *Fast & Accurate Randomized Algorithms for Linear Systems and Eigenvalue Problems*, arXiv:2111.00113v2 (2022), https://arxiv.org/html/2111.00113v2; see Section 6 for the sketched eigenvalue method and Section 6.8 for the Hermitian case. Journal version: *SIAM J. Matrix Anal. Appl.* 45 (2024), 1183--1214.
