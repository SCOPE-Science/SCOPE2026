# Exact Fourier-mode staircase and critical conditioning for cyclic Bergman kernels

## Finding

Let \(A^2(\mathbb D)\) be the analytic Bergman space with normalized area measure. For an integer \(N\ge2\) and \(0<q<1\), take the normalized reproducing kernels at \(z_a=\sqrt q\,e^{2\pi ia/N}\), \(0\le a<N\). The Gram matrix of these kernels has Fourier-mode eigenvalues
\[
\lambda_{N,j}=\frac{N(1-q)^2q^j}{1-q^N}\left(j+1+\frac{Nq^N}{1-q^N}\right),\qquad 0\le j<N.
\]
The minimum is attained uniquely by mode \(N-1\). Define
\[
T_N(q)=\frac{q}{1-q}-1-\frac{Nq^N}{1-q^N}.
\]
If \(T_N(q)\notin\mathbb Z_{\ge0}\), the maximum is attained uniquely by mode \(\max\{0,\lceil T_N(q)\rceil\}\). If \(T_N(q)=k\in\mathbb Z_{\ge0}\), precisely modes \(k,k+1\) attain the maximum. The function \(T_N\) is strictly increasing from \(-1\) to \((N-3)/2\). Thus there is exactly one transition in the maximizing mode for each integer \(0\le k<(N-3)/2\); as \(q\) increases, the maximizing modes run from \(0\) to \(\lfloor(N-2)/2\rfloor\) with no skips. This classifies ties **at the maximum**, not coincidences between nonextremal eigenvalues.

For fixed \(c>0\), put \(q_N=1-c/N\) for integers \(N>\max\{2,c\}\). Uniformly over the Fourier spectrum,
\[
\max_{0\le j<N}|\lambda_{N,j}-F_c(j/N)|=O_c(N^{-1}),\qquad
F_c(x)=c^2e^{-cx}\left(\frac{x}{1-e^{-c}}+\frac{e^{-c}}{(1-e^{-c})^2}\right).
\]
The limiting profile on \([0,1]\) has equal minima at \(0\) and \(1\) and a unique maximum at
\[
x_c=\frac1c-\frac1{e^c-1}\in(0,1/2).
\]
Every maximizing index divided by \(N\) tends to \(x_c\). The Gram spectral condition number has the limit
\[
\kappa(c)=\lim_{N\to\infty}\frac{\lambda_{\max}}{\lambda_{\min}}
=\frac{e^c-1}{c}\exp\left(-1+\frac{c}{e^c-1}\right).
\]
It is strictly greater than one, equals \(1+c^2/8+O(c^4)\) as \(c\downarrow0\), and is asymptotic to \(e^{c-1}/c\) as \(c\to\infty\). The largest and smallest Gram eigenvalues are the sharp upper and lower bounds on the squared norm of kernel synthesis per unit squared coefficient norm; the synthesis condition number is the square root of the Gram condition number.

## Assumptions and scope

Use the norm \(\|f\|^2=\pi^{-1}\int_{\mathbb D}|f(z)|^2\,dA(z)\), and the kernel \(K(z,w)=(1-z\overline w)^{-2}\). The normalized kernel at \(w\) is \((1-|w|^2)K(\cdot,w)\). With the inner product linear in the first entry, use the Gram convention \(G_{ab}=\langle k_{z_b},k_{z_a}\rangle\); mode \(j\) corresponds to the vector \((e^{2\pi ija/N})_a\). The finite claims apply to every \(N\ge2\) and \(0<q<1\). The limiting claims hold with \(c\) fixed before \(N\to\infty\).

## Proof

**Fourier diagonalization.** With \(\omega=e^{2\pi i/N}\),
\[
G_{ab}=(1-q)^2(1-q\omega^{a-b})^{-2}
=(1-q)^2\sum_{n\ge0}(n+1)q^n\omega^{n(a-b)}.
\]
Roots-of-unity orthogonality filters this absolutely convergent series to give \(N(1-q)^2\sum_{\ell\ge0}(j+1+\ell N)q^{j+\ell N}\). Summing the geometric series and its first moment gives the stated positive eigenvalues.

**Maximum staircase.** Put \(A=Nq^N/(1-q^N)\). The adjacent ratio \(q(j+2+A)/(j+1+A)\) is strictly decreasing in \(j\); it is greater than, equal to, or less than one as \(j\) is less than, equal to, or greater than \(T_N(q)\). For \(s=-\log q>0\),
\[
\frac{d}{ds}T_N(e^{-s})=-\frac1{4\sinh^2(s/2)}+\frac{N^2}{4\sinh^2(Ns/2)}<0
\]
by \(\sinh(Nt)>N\sinh(t)\) for \(t>0\). The limit at \(s\to\infty\) is \(-1\), and \((e^s-1)^{-1}=s^{-1}-1/2+O(s)\) gives the limit \((N-3)/2\) at \(s\downarrow0\). This proves the exact transition count and the maximum classification, including the cases with no transition. For example, it does not rule out a nonextremal tie: for \(N=6\), at \(T_6=0\) one has \(\lambda_0>\lambda_2\), and at \(T_6=1\) one has \(\lambda_0<\lambda_2\). Between these two radii there is a radius with \(\lambda_0=\lambda_2\), at which mode \(1\) is uniquely maximal.

**Minimum.** The function \(j\mapsto j\log q+\log(j+1+A)\) is strictly concave, so any discrete minimum is at an endpoint. The endpoint ratio is
\[
\lambda_{N,N-1}/\lambda_{N,0}=\frac{Nq^{N-1}}{1+(N-1)q^N}<1.
\]
Indeed the denominator minus the numerator vanishes at 1 and has derivative \(N(N-1)q^{N-2}(q-1)<0\) on \((0,1)\). This proves uniqueness of the minimum.

**Critical scaling.** For fixed \(c>0\), the expansion \(\log q_N=-c/N+O_c(N^{-2})\) implies \(q_N^j=e^{-cj/N}(1+O_c(N^{-1}))\) uniformly for \(0\le j<N\), and \(q_N^N=e^{-c}+O_c(N^{-1})\). Substituting in
\[
\lambda_{N,j}=c^2q_N^j\left(\frac{j/N+1/N}{1-q_N^N}+\frac{q_N^N}{(1-q_N^N)^2}\right)
\]
proves the uniform estimate. The derivative of the profile is \(c^3e^{-cx}(x_c-x)/(1-e^{-c})\). The inequalities \(e^c-1>c\) and \(\coth(c/2)>2/c\) give \(0<x_c<1/2\). Also \(F_c(0)=F_c(1)=c^2e^{-c}/(1-e^{-c})^2>0\). Uniform convergence and grid density give the limiting maximum \(F_c(x_c)=ce^{-cx_c}/(1-e^{-c})\); the unique finite minimum gives the limiting minimum \(F_c(1)\). The ratio simplifies to \(\kappa(c)\), and the strict interior maximum gives \(\kappa(c)>1\). The adjacent-mode criterion with \(T_N(q_N)=Nx_c+O_c(1)\) also gives convergence of every maximizing index after division by \(N\). At small \(c\), expanding the two factors in \(\log\kappa(c)=\log((e^c-1)/c)-1+c/(e^c-1)\) gives \(c^2/8+O(c^4)\). At large \(c\), \((e^c-1)/e^c\to1\) and \(c/(e^c-1)\to0\). The synthesis bounds follow from the Gram quadratic form.

## Verification

The accompanying standard-library script `check_bergman_spectrum.py` compares the exact formula with a direct discrete Fourier transform, checks the extremal modes and top ties, and compares finite-size profiles and condition numbers with the critical limits. Run `python3 check_bergman_spectrum.py` in the record directory. These finite checks do not establish the infinite theorem; the proof above gives both the exact extrema and the uniform limit. The nonmaximal tie follows from the two strict comparisons at \(T_6=0,1\) and continuity, without numerical root finding.

## Relationship to existing work

Aadi, Cruz, Hartmann, and Kellay treat weighted Bergman sampling and interpolation with multiplicities, a different scope from this exact one-ring extremal-mode problem. For the Szegő kernel on a regular orbit, the analogous Fourier spectrum is geometric and does not have a radius-driven maximizing-mode staircase. For the Dirichlet-type kernel in *Critical exponential boundary layer for cyclic Dirichlet Gram spectra*, the uniform profile and condition-number law use a different kernel and an exponential distance of the squared radius from one. The residue-vector norms in *Exact cyclic Bergman kernel approximation and its Gamma capture law* directly give the same finite Bergman eigenvalue formula after Gram normalization. That work studies monomial projection and an optimized-radius, high-degree law at fixed orbit size, not the extremal modes or the many-node conditioning law here. The distinct content claimed here is the complete extremal-mode staircase and its uniform critical conditioning law, not the standard residue filtering or the resulting finite formula in isolation.

## Limitations

The classification concerns the minimum and maximum, not all nonextremal eigenvalue coincidences. The analysis does not optimize irregular point sets or general kernel powers, and does not assert uniform error constants for \(c\) varying with \(N\). The cited comparisons do not certify publication priority.

## References

1. D. Aadi, C. Cruz, A. Hartmann, and K. Kellay, *Multiple sampling and interpolation in Bergman spaces*, https://arxiv.org/abs/2202.07263.
2. *Sharp determinant stability and conditioning of concentric Szegő kernel configurations*, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa.
3. *Critical exponential boundary layer for cyclic Dirichlet Gram spectra*, https://github.com/Resultary/2026/tree/main/2026/10/27/SCOPE-critical-exponential-boundary-layer-for-cyclic-dirichlet-gram-sp--e03594da668d.
4. *Exact cyclic Bergman kernel approximation and its Gamma capture law*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-cyclic-bergman-kernel-approximation-and-its-gamma-capture--973f6bafeca1.
