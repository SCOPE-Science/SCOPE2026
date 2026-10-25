# Log-periodic high-mode spectrum and sharp Schatten threshold for a critical Cantor Bergman localization

## Finding

Put \(\delta=\log 2/\log 3\). In the weighted analytic Bergman space specified below, the nested critical-scale Cantor-annulus localization operators converge **in operator norm** to a positive compact Toeplitz operator \(T_\infty\). Its eigenvalues in the normalized monomial basis obey
\[
\lambda_k=k^{\delta-1}\bigl(P_\alpha(k)+o(1)\bigr)\qquad(k\to\infty),
\]
where \(P_\alpha:(0,\infty)\to(0,\infty)\) is explicitly given below, is real-analytic and **not constant**, and satisfies \(P_\alpha(3r)=P_\alpha(r)\). Thus the sharp power law carries a genuine logarithmically periodic leading modulation, not a fixed constant. The exact Schatten transition is
\[
T_\infty\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac{1}{1-\delta},\qquad 0<p<\infty.
\]
At the critical exponent the operator lies in weak Schatten class but not strong Schatten class.

## Assumptions and scope

Let \(\alpha>0\), \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and let \(A^2_\alpha\) be the analytic subspace of \(L^2(\mathbb D,d\mu_\alpha)\), where
\[
d\mu_\alpha(z)=2\alpha(1-|z|^2)^{2\alpha-1}\frac{dA(z)}{\pi}.
\]
For \(n\ge0\) set \(D_n=\{\sum_{j=0}^{n-1}2\varepsilon_j3^j:\varepsilon_j\in\{0,1\}\}\), with \(D_0=\{0\}\), and
\[
E_n=\bigcup_{a\in D_n}[a,a+1],\quad E_\infty=\bigcup_{n\ge0}E_n,\quad
\Omega_n=\left\{z\in\mathbb D:\frac{|z|^2}{1-|z|^2}\in E_n\right\}.
\]
These are precisely the middle-third hyperbolic Cantor annuli at the critical scale \(R=3^n\). Write \(\Omega_\infty\) for the analogous set with \(E_\infty\), and define the bounded operators \(T_n=P_\alpha M_{\mathbf1_{\Omega_n}}|_{A^2_\alpha}\) and \(T_\infty=P_\alpha M_{\mathbf1_{\Omega_\infty}}|_{A^2_\alpha}\), with \(P_\alpha\) the orthogonal Bergman projection. These definitions apply even though \(\Omega_\infty\) is not relatively compact in the disk.

Let \(X=\sum_{j\ge1}2\varepsilon_j3^{-j}\), with fair independent binary digits, and let \(\mu_C\) denote its distribution (the standard Cantor probability measure). There is a unique locally finite measure \(\nu\) on \([0,\infty)\) satisfying, for every integer \(j\ge0\) and Borel \(B\subset[0,3^j]\),
\[
\nu(B)=2^j\,\mu_C(3^{-j}B).
\]
Consistency follows from the left-branch self-similarity of \(\mu_C\). This infinite Cantor measure satisfies \(\nu(3B)=2\nu(B)\), is singular with respect to Lebesgue measure and obeys \(\nu([0,x])\le Cx^\delta\).

Define, for \(r>0\),
\[
F_\alpha(r)=\frac{r^{2\alpha}}{\Gamma(2\alpha)}
\int_{(0,\infty)}x^{-2\alpha-1}e^{-r/x}\,d\nu(x),\qquad
P_\alpha(r)=r^{1-\delta}F_\alpha(r).
\]
Both integrals converge absolutely; this formula specifies the entire leading profile without any numerical fitting.

## Proof

**1. Exact diagonalization and monotone limit.** The normalized monomials diagonalize every operator above. Direct polar integration with \(t=|z|^2/(1-|z|^2)\) yields their eigenvalues
\[
\lambda_k^{(n)}=\int_{E_n}g_{k,\alpha}(t)\,dt,\quad
\lambda_k=\int_{E_\infty}g_{k,\alpha}(t)\,dt,
\qquad
g_{k,\alpha}(t)=\frac{t^k}{B(k+1,2\alpha)(1+t)^{k+2\alpha+1}}.
\]
The density integrates to one on \((0,\infty)\), so \(0\le\lambda_k^{(n)}\uparrow\lambda_k\le1\). Proving \(\lambda_k\to0\) below establishes compactness. Then monotone convergence for finitely many indices, together with \(0\le\lambda_k-\lambda_k^{(n)}\le\lambda_k\) on the remaining tail, proves \(\|T_n-T_\infty\|\to0\).

**2. Infinite Cantor scaling.** Let
\[
\eta_m(dx)=\left(\frac32\right)^m\mathbf1_{E_\infty}(3^m x)\,dx.
\]
For any integer \(j\ge0\), its restriction to \([0,3^j]\), for sufficiently large \(m\), has mass \(2^j\) and is the rescaled uniform interval measure on the \((m+j)\)-step middle-third Cantor approximation. Standard cylinder-counting therefore gives \(\eta_m\Rightarrow\nu\) vaguely on \([0,\infty)\). The elementary count \(|E_\infty\cap[0,T]|\le C\max\{T,T^\delta\}\), with the sharper \(CT^\delta\) for \(T\ge1\), implies uniformly
\[
\eta_m([0,x])\le Cx^\delta\qquad(x>0,m\ge0).
\]
The limit \(\nu\) has the same bound. Each \(\nu\)-restriction to \([0,3^j]\) is a scaled Cantor measure, proving singularity, and the displayed definition implies the exact scaling identity \(\nu(3B)=2\nu(B)\).

**3. Uniform inverse-gamma local limit and tails.** Write \(b=2\alpha>0\). By the gamma-ratio asymptotic,
\[
\frac{1}{B(k+1,b)}=\frac{k^b}{\Gamma(b)}\bigl(1+O_b(k^{-1})\bigr).
\]
Hence for \(k_m=\lfloor r3^m\rfloor\), uniformly when \(r\) varies in a compact subset of \((0,\infty)\) and \(x\) in a compact subset of \((0,\infty)\),
\[
3^m g_{k_m,\alpha}(3^m x)\longrightarrow
\frac{r^b}{\Gamma(b)}x^{-b-1}e^{-r/x}.
\]
For \(r\in[1,3]\), \(x\ge3^{-m}\), the left side is bounded by \(C x^{-b-1}e^{-c/x}\), using \(\log(1+1/t)\ge1/(2t)\) for \(t\ge1\). On \(0<x<3^{-m}\), the contribution to \(\int 3^m g_{k_m,\alpha}(3^mx)\,d\eta_m(x)\) is at most \((3/2)^m Ck_m^b2^{-k_m}\), which tends to zero. The common growth estimate \(\eta_m([0,x])\le Cx^\delta\) controls the remaining tails: for \(R\ge1\),
\[
\int_{[R,\infty)}x^{-b-1}\,d\eta_m(x)\le C_b R^{\delta-b-1},
\]
and for \(0<x<\varepsilon\), the exponential factor gives a uniformly vanishing integral. Vague convergence plus these estimates, and a finite-net argument for the parameter \(r\), prove locally uniformly in \(r>0\) that
\[
\left(\frac32\right)^m\lambda_{\lfloor r3^m\rfloor}
\longrightarrow F_\alpha(r).
\]
Here \(\lambda_k\) integrates over the **infinite** set \(E_\infty\); this is not merely a fixed-level finite Cantor estimate.

**4. The nonconstant periodic profile.** From \(\nu(3B)=2\nu(B)\), changing variables \(x=3y\) gives
\[
F_\alpha(3r)=\frac23F_\alpha(r),\qquad
P_\alpha(3r)=P_\alpha(r).
\]
Taking \(m=\lfloor\log_3 k\rfloor\) and \(r=k/3^m\in[1,3)\) in the locally uniform convergence yields the asserted \(\lambda_k=k^{\delta-1}(P_\alpha(k)+o(1))\). Positivity and continuity give uniform positive upper and lower bounds on \(P_\alpha\).

To prove the oscillation is genuine, define a measure on logarithmic coordinates by \(d\rho(y)=e^{-\delta y}\,d\nu(e^y)\) in the pushforward sense. It is periodic of period \(L=\log3\) and is singular on one period. With \(s=b+1-\delta>0\), the function \(Q(t)=P_\alpha(e^t)\) is the periodized convolution
\[
Q(t)=\frac1{\Gamma(b)}\int_{\mathbb R}
\exp\!\left[-s(y-t)-e^{-(y-t)}\right]d\rho(y).
\]
The kernel has Fourier transform \(\Gamma(s+i\omega)\) (up to the sign convention), which never vanishes. If \(Q\) were constant, Fourier uniqueness on the circle would force every nonzero Fourier coefficient of \(\rho\) to vanish; hence \(\rho\) would be a multiple of Lebesgue measure, contradicting its Cantor singularity. The kernel is analytic after complexifying \(t\) in a small strip and has integrable derivatives there; thus \(Q\) and \(P_\alpha\) are real-analytic. This proves strict nonconstancy.

**5. Sharp Schatten transition.** Since \(P_\alpha\) is bounded above and away from zero, \(c_\alpha k^{\delta-1}\le\lambda_k\le C_\alpha k^{\delta-1}\) for all sufficiently large \(k\). For any \(0<p<\infty\), the exact diagonal criterion \(\sum_k\lambda_k^p<\infty\) is equivalent to \(p(1-\delta)>1\). At equality the series diverges, but the uniform upper power bound gives membership in the weak Schatten class. No reordering assumption about the radial eigenvalues is needed for the summability criterion.

## Verification

The normalization follows from the beta-prime density \(g_{k,\alpha}\), whose integral equals one. The Cantor scaling measure is checked by direct interval counting. For \(\alpha=1\), the exact beta CDF is \((k+2)u^{k+1}-(k+1)u^{k+2}\), where \(u=t/(1+t)\); this gives an independent finite-sum route for numerical comparisons. A standalone standard-library script in `checks/numeric.py` compares scaled finite-level eigenvalues with truncated Cantor-measure quadrature for several mode indices. These finite checks corroborate the asymptotic but are not used as its proof.

## Relationship to prior work

Abreu, Mouayn, and Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets* (arXiv:2201.11705, first posted 2022-01-27), derive the exact finite-level beta-prime eigenvalue formula (Proposition 4.1) and two-sided bounds for the **operator norm** of the finite Cantor-annulus localizations (Theorem 2.1). The critical specialization \(R=3^n\) is part of that geometric framework; its full infinite-symbol compact limit, high-monomial inverse-gamma/Cantor spectral profile, nonconstant log-periodic coefficient and sharp Schatten transition are separate statements not provided by those results.

Knutsen's *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I* (2019/2020) and *II* (2021) give related Gaussian-STFT Cantor localization and operator-norm bounds, but use a different Gaussian/Fock density and do not imply this weighted-Bergman inverse-gamma profile. Rozenblum's 2011 radial Toeplitz spectral estimates focus on compactly supported symbols in the Bergman disk and therefore do not cover the boundary-accumulating symbol here. General results on radial Toeplitz eigenvalue sequences provide background but are not claimed to be superseded.

## Limitations

The theorem gives asymptotics in the **monomial mode index**, not an exact closed-form descending rearrangement of all eigenvalues. Its explicit positive periodic profile is an integral over a singular measure; no elementary closed form is asserted. It does not treat arbitrary Cantor alphabets, nonradial masks, or the scaling regime \(R\asymp3^{n/2}\) used for decaying-norm fractal uncertainty. Priority beyond the inspected sources remains subject to independent specialist review.

## References

1. L. D. Abreu, Z. Mouayn, F. Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (initial submission 2022-01-27), https://arxiv.org/abs/2201.11705 . In particular, Section 2, Proposition 4.1 and Theorem 2.1.
2. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets I*, arXiv:1907.00848 (2019), https://arxiv.org/abs/1907.00848 ; J. Fourier Anal. Appl. 26 (2020), 47.
3. H. Knutsen, *Daubechies' Time-Frequency Localization Operator on Cantor Type Sets II*, arXiv:2104.10976 (2021), https://arxiv.org/abs/2104.10976 .
4. G. Rozenblum, *On lower eigenvalue bounds for Toeplitz operators with radial symbols in Bergman spaces*, J. Spectr. Theory 1 (2011), 299–325, https://doi.org/10.4171/JST/13 .
5. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, Bull. Lond. Math. Soc. 40 (2008), 631–641, https://doi.org/10.1112/blms/bdn042 .
