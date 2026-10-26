# Sharp disk concentration and spectral-gap resonances in the first true-polyanalytic Fock space

## Finding
Let \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) on \(\mathbb C\), and let \(\mathcal H_1\) be the closed span of \(\Phi_0(z)=\bar z\) and \(\Phi_n(z)=(z^n\bar z-nz^{n-1})/\sqrt{n!}\) for all integers \(n\ge1\). Its elements constitute the first excited, or true order-two, polyanalytic Fock space. For every real \(x>0\), let \(T_x=P_1\mathbf1_{\{|z|^2\le x\}}\vert_{\mathcal H_1}\), where \(P_1\) is orthogonal projection in \(L^2(\gamma)\) onto \(\mathcal H_1\).

The exact sharp disk-concentration coefficient, equal to the operator norm of \(T_x\), is
\[
C(x)=\sup_{0\ne F\in\mathcal H_1}\frac{\displaystyle\int_{|z|^2\le x}|F(z)|^2\,d\gamma(z)}{\displaystyle\int_{\mathbb C}|F(z)|^2\,d\gamma(z)}
=\begin{cases}
1-e^{-x}(1+x^2),&0<x<1,\\
1-2/e,&x=1,\\
1-e^{-x}(1+x),&x>1.
\end{cases}
\]
The complete maximizing subspace \(E(x)\) is \(\mathbb C\Phi_1\) for \(0<x<1\); \(\operatorname{span}\{\Phi_0,\Phi_1,\Phi_2\}\) at \(x=1\); and \(\mathbb C\Phi_0\) for \(x>1\). In particular, the critical disk has an exactly three-dimensional maximizing eigenspace.

For every \(x>0\) there is also a sharp positive *spectral-gap stability law*
\[
C(x)\|F\|_{L^2(\gamma)}^2-\int_{|z|^2\le x}|F|^2\,d\gamma
\ge g(x)\,\operatorname{dist}_{L^2(\gamma)}(F,E(x))^2,\qquad F\in\mathcal H_1,
\]
where the greatest possible constant is
\[
g(x)=\begin{cases}
\tfrac12 e^{-x}x(1-x)(2-x),&0<x<1,\\
1/(3e),&x=1,\\
\tfrac12e^{-x}x^2(x-1),&1<x<2,\\
2e^{-2},&x=2,\\
e^{-x}x(x-1),&x>2.
\end{cases}
\]
The second-highest *distinct* eigenspace is \(\mathbb C\Phi_2\) if \(0<x<1\) or \(1<x<2\), \(\mathbb C\Phi_3\) at \(x=1\), \(\operatorname{span}\{\Phi_1,\Phi_2,\Phi_3\}\) at \(x=2\), and \(\mathbb C\Phi_1\) for \(x>2\). In every case equality in the stability law holds precisely for vectors in the sum of the maximizing and second-highest eigenspaces.

## Assumptions and scope
The normalization and radial disk are exactly as written. The squared radius \(x\) is dimensionless; under the standard short-time Fourier transform with normalized first Hermite window \(h_1\) and phase-space measure \(du\,dv\), \(x=\pi R^2\) for the centered disk of radius \(R\). The polyanalytic Bargmann transform identifies the norm quotient above with squared \(L^2\) concentration of \(V_{h_1}f\) on that disk. Only one Landau level is included (not the direct sum of all lower levels). All disk radii \(x>0\), all nonzero complex-valued \(F\in\mathcal H_1\), and all eigenvalue indices \(n\ge0\) are covered.

## Proof
**1. Diagonalization and normalization.** For \(n\ge1\), the functions \(\Phi_n\) have angular frequency \(n-1\), while \(\Phi_0\) has frequency \(-1\). Gaussian radial moments give \(\int_0^\infty e^{-t}t^{n-1}(n-t)^2\,dt=n!\); for \(n=0\), \(\int_0^\infty e^{-t}t\,dt=1\). Distinct angular frequencies are orthogonal, and the complex-Hermite basis is complete in the true order-two Fock space (see References). Thus \(T_x\) is compact, positive and diagonal in this basis, with
\[
\lambda_0(x)=1-e^{-x}(1+x),\qquad
\lambda_n(x)=\frac1{n!}\int_0^x e^{-t}t^{n-1}(n-t)^2\,dt\quad(n\ge1).
\]
Integrating each polynomial term yields, for every \(n\ge0\),
\[
\lambda_n(x)=1-e^{-x}Q_n(x),\quad
Q_n(x)=\sum_{j=0}^{n-1}\frac{x^j}{j!}+(1-n)\frac{x^n}{n!}+\frac{x^{n+1}}{n!}.
\]
The sum is empty when \(n=0\). All eigenvalues strictly lie in \((0,1)\) for finite \(x>0\), and \(\lambda_n(x)\to0\) as \(n\to\infty\) by factorial domination of fixed-disk integrals. Thus the supremum is attained at some eigenindex.

**2. Adjacent-index signs.** Direct subtraction yields the exact identity
\[
\lambda_{n+1}(x)-\lambda_n(x)
=-\frac{e^{-x}x^n}{(n+1)!}(x-n)(x-n-1),\qquad n\ge0.
\]
Hence the sequence decreases at indices \(n<x-1\), increases at a single index \(x-1<n<x\) when such an integer exists, and then decreases strictly at every index \(n>x\). At \(x=1\), \(\lambda_0=\lambda_1=\lambda_2\), and at \(x=2\), \(\lambda_1=\lambda_2=\lambda_3\). The formula alone does not exclude a larger remote tail peak, so this comparison is addressed next.

**3. Half-mass exclusion of the remote peak.** For each integer \(n\ge1\), write \(f_n(t)=e^{-t}t^n/n!\). By integration by parts, \(\lambda_n(n)=\int_0^n f_n(t)\,dt\). For \(0<s<n\),
\[
\log\frac{f_n(n+s)}{f_n(n-s)}
=2n\left[\operatorname{artanh}(s/n)-s/n\right]>0.
\]
Consequently the mass on \((n,2n)\) strictly exceeds that on \((0,n)\); the remaining mass past \(2n\) is positive. Since \(\int_0^\infty f_n=1\), necessarily \(\lambda_n(n)<1/2\). Because \(\lambda_n\) increases with \(x\), we obtain
\[
\lambda_n(x)<1/2\qquad\text{whenever }n\ge1\text{ and }x\le n.
\]
At \(x=2\), \(\lambda_0(2)=1-3e^{-2}>1/2\), since \(e^2>6\); hence \(\lambda_0(x)>1/2\) for all \(x\ge2\). At \(x=3\), \(\lambda_1(3)=1-10e^{-3}>1/2\), since \(e^3>20\); hence \(\lambda_1(x)>1/2\) for \(x\ge3\). Both strict exponential comparisons follow immediately from finite positive Taylor sums, so no decimal estimates are used.

**4. Exact leading and runner-up spectral positions.** For \(0<x<1\) the adjacent signs show \(\lambda_1>\lambda_2>\lambda_3>\cdots\) and \(\lambda_1>\lambda_0\), and a separate direct comparison gives \(\lambda_2>\lambda_0\). At \(x=1\), the first three eigenvalues tie, with \(\lambda_3\) strictly maximal among the rest. For \(1<x<2\), the signs give \(\lambda_2>\lambda_1\), \(\lambda_2>\lambda_3>\cdots\), whereas \(\lambda_0>\lambda_2\). The two needed direct comparisons are
\[
\lambda_2-\lambda_0=-\tfrac12e^{-x}x^2(x-1),\qquad
\lambda_1-\lambda_3=\tfrac16e^{-x}x(x-2)(x^2-3).
\]
For \(2<x<3\), \(\lambda_0>\lambda_1>\lambda_2\), and the second formula ensures \(\lambda_1>\lambda_3\); all later eigenvalues are below \(\lambda_3\) by the adjacent signs. For \(x\ge3\), use \(\lambda_1(x)>1/2\) to exclude every index \(n\ge\lceil x\rceil\) by step 3, while step 2 shows \(\lambda_1\) dominates every index \(2\le n\le\lfloor x\rfloor\). At integer endpoints, zero adjacent differences cause the stated ties but no additional larger indices. Likewise for \(x\ge2\), \(\lambda_0>1/2\) excludes all indices \(n\ge\lceil x\rceil\), and step 2 covers all smaller indices. These deductions give the maximizing and next-distinct eigenspaces for *every* \(x>0\), not merely sampled radii.

**5. Coefficients and sharpness of stability.** The explicit formulas give \(\lambda_1=1-e^{-x}(1+x^2)\); the differences between the largest and next-distinct eigenvalues yield \(g(x)\) in the displayed five cases. Writing \(F=\sum_{n\ge0}c_n\Phi_n\), Parseval gives
\[
C(x)\|F\|^2-\langle T_xF,F\rangle
=\sum_{n\ge0}(C(x)-\lambda_n(x))|c_n|^2.
\]
The zero coefficients in this diagonal deficit are precisely the maximizing eigenspace; every other coefficient is at least \(g(x)>0\). Equality holds if and only if no coefficient outside the top two distinct eigenspaces occurs. A unit vector in the second eigenspace attains equality, proving that \(g(x)\) cannot be increased. This completes both the norm and stability claims.

## Verification
The complete argument is analytic and covers infinitely many modes. An independently runnable dependency-free rational-arithmetic script `verify.py` checks the adjacent-difference polynomial identity for 501 indices, the critical algebraic comparisons and transition ties, and the exact ordering of 81 candidate modes at 17 rational radii. Run `python3 verify.py` from the package directory. Output is recorded in `CHECKS.txt`. The finite computations are supplementary; they do not substitute for step 3 or the global spectral exclusions of step 4.

## Relationship to prior work
Abreu and Speckbacher (2018, arXiv:1808.02258v1, Sections 4–5) prove local reproducing identities and Hermite-window large-sieve inequalities. In Section 5 the explicitly sharp centered-disk concentration formula is stated for the *Gaussian* window. Their disk orthogonality identity for arbitrary Hermite levels supplies the diagonal framework, not the present optimization over the first excited level and its exact second spectral gap. Maximenko and Tellería-Romero (2019, arXiv:1905.00978, Section 6, Proposition 6.3) give eigenvalue integrals for arbitrary radial Toeplitz symbols in true polyanalytic Fock spaces; the full section was examined, including the characteristic-disk symbols in Proposition 6.6. Its results do not specify the maximizing disk eigenindex, critical three-way transition or sharp gap. The Gaussian-window radial localization theorem originating with Daubechies (1988), and treated by Knutsen (2020), has a different window and spectrum. Nicola–Tilli (2022) optimize Gaussian-window localization norms under weight-norm restrictions, not this fixed first-Hermite disk spectrum. No claim of uniqueness in the world's literature is made from these searches.

## Limitations
This result concerns the first excited Landau level, centered *disks*, and the specific Gaussian normalization. It neither handles higher Hermite windows nor asserts the same extremizers for translated annuli or general radial masks. The exact eigenvalue integral is previously known; the contribution is the all-radius global ranking, threefold critical eigenspace, and sharp piecewise spectral-gap rigidity. An equivalent treatment under Laguerre-distribution or Hermite spectrogram terminology may exist; priority has not been independently verified.

## References
1. L. D. Abreu and M. Speckbacher, *Donoho–Logan Large Sieve Principles for Modulation and Polyanalytic Fock Spaces*, arXiv:1808.02258v1 (7 August 2018), Sections 4–5, https://arxiv.org/html/1808.02258v1.
2. E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (2 May 2019), Proposition 6.3 and Section 6, https://arxiv.org/abs/1905.00978.
3. H. Knutsen, *Daubechies' Time–Frequency Localization Operator on Cantor Type Sets I*, Journal of Fourier Analysis and Applications 26 (2020), 47, Theorem 2.1 (Gaussian-window spectral formula), https://doi.org/10.1007/s00041-020-09751-9.
4. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624 (18 July 2022), https://arxiv.org/abs/2207.08624.
