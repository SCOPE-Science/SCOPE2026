# Exact Fourier-mode staircase and critical conditioning for cyclic Bergman kernels

## Finding
Let \(A^2(\mathbb D)\) be the unweighted analytic Bergman space with probability area measure. For every integer \(N\ge2\) and \(0<q<1\), take the \(N\) normalized reproducing kernels at \(z_a=\sqrt q\exp(2\pi ia/N)\), \(0\le a<N\), and their \(N\)-by-\(N\) Gram matrix \(G_{N,q}\). Its cyclic Fourier-mode eigenvalues, labeled by \(0\le j<N\), are exactly
\[
\lambda_{N,j}=\frac{N(1-q)^2q^j}{1-q^N}\left(j+1+\frac{Nq^N}{1-q^N}\right).
\]
For every \(N,q\), the *unique smallest* eigenvalue is \(\lambda_{N,N-1}\). Define
\[
T_N(q)=\frac{q}{1-q}-1-\frac{Nq^N}{1-q^N}.
\]
When \(T_N(q)\notin\mathbb Z_{\ge0}\), the *unique largest* eigenvalue has index \(\max\{0,\lceil T_N(q)\rceil\}\). When \(T_N(q)=k\in\mathbb Z_{\ge0}\), precisely the adjacent modes \(k,k+1\) tie for largest. The function \(T_N\) is strictly increasing from \(-1\) to \((N-3)/2\). Consequently exactly one radius-squared transition occurs for each integer \(0\le k<(N-3)/2\); the largest-eigenvalue mode climbs monotonically from \(0\) to \(\lfloor(N-2)/2\rfloor\) as \(q\uparrow1\), without skipped modes or other degeneracies.

For fixed \(c>0\) and integers \(N>\max\{2,c\}\), set \(q_N=1-c/N\). With \(x=j/N\), all eigenvalues converge **uniformly over their entire Fourier spectrum**:
\[
\max_{0\le j<N}\bigl|\lambda_{N,j}-F_c(j/N)\bigr|=O_c(N^{-1}),\qquad
F_c(x)=c^2e^{-cx}\left(\frac{x}{1-e^{-c}}+\frac{e^{-c}}{(1-e^{-c})^2}\right).
\]
The limiting profile has equal minima at \(x=0,1\), and its unique maximum occurs at
\[
x_c=\frac1c-\frac1{e^c-1}\in\left(0,\frac12\right).
\]
The maximum-eigenvalue Fourier index divided by \(N\) converges to \(x_c\), and the sharp **Gram spectral condition number** has the explicit limit
\[
\boxed{\displaystyle\lim_{N\to\infty}\frac{\lambda_{\max}(G_{N,q_N})}{\lambda_{\min}(G_{N,q_N})}
=\frac{e^c-1}{c}\exp\left(-1+\frac{c}{e^c-1}\right).}
\]
The limiting condition number is strictly larger than one for every \(c>0\), approaches \(1+c^2/8+O(c^4)\) as \(c\downarrow0\), and is asymptotic to \(e^{c-1}/c\) as \(c\to\infty\). For normalized kernel synthesis, the optimal upper and lower squared Riesz bounds are the corresponding largest and smallest Gram eigenvalues; its operator condition number is the square root of the displayed Gram condition number.

## Assumptions and scope
The Hilbert norm is \(\|f\|_{A^2}^2=\pi^{-1}\int_{|z|<1}|f(z)|^2\,dA(z)\); hence \(K(z,w)=(1-z\overline w)^{-2}\) and the unit-norm kernel at \(w\) is \(k_w(z)=(1-|w|^2)(1-z\overline w)^{-2}\). The eigenvalue index \(j\) refers to the Fourier vector \((\exp(2\pi ija/N))_{a=0}^{N-1}\). The finite claims hold for all integers \(N\ge2\), all \(q\in(0,1)\), and include every degeneracy. The limiting claims fix \(c>0\) **before** sending \(N\to\infty\); error constants are not asserted uniform for \(c\) varying with \(N\).

## Proof
**Cyclic diagonalization.** Write \(\omega=\exp(2\pi i/N)\). The normalized kernel Gram matrix has entries
\[
(G_{N,q})_{ab}=\frac{(1-q)^2}{(1-q\omega^{a-b})^2}
=(1-q)^2\sum_{n\ge0}(n+1)q^n\omega^{n(a-b)}.
\]
All series are absolutely convergent for \(0<q<1\). Fourier orthogonality shows that the \(j\)-th eigenvalue equals \(N(1-q)^2\sum_{\ell\ge0}(j+1+\ell N)q^{j+\ell N}\). Summing both geometric series gives the formula in the finding, in particular proving strict positivity and invertibility.

**Largest-mode staircase.** Put \(A=Nq^N/(1-q^N)\), so apart from a positive common factor the eigenvalues are \(q^j(j+1+A)\). For \(0\le j\le N-2\),
\[
\frac{\lambda_{N,j+1}}{\lambda_{N,j}}=q\frac{j+2+A}{j+1+A},
\qquad \lambda_{N,j+1}\begin{cases}>\lambda_{N,j}&j<T_N(q),\\=\lambda_{N,j}&j=T_N(q),\\<\lambda_{N,j}&j>T_N(q).\end{cases}
\]
The ratio strictly decreases with \(j\); therefore there is a unique peak except for the stated adjacent pair at equality. For strict monotonicity of the transition parameter, set \(h=-\log q>0\). Then
\[
T_N(e^{-h})=\frac1{e^h-1}-\frac N{e^{Nh}-1}-1,
\quad
\frac{dT_N(e^{-h})}{dh}=-\frac1{4\sinh^2(h/2)}+\frac{N^2}{4\sinh^2(Nh/2)}<0.
\]
The strict inequality follows from \(\sinh(Nt)>N\sinh(t)\) for \(t>0\) and integers \(N\ge2\). The elementary large-\(h\) limit and the expansion \((e^h-1)^{-1}=h^{-1}-1/2+O(h)\) give the endpoint values \(-1\) and \((N-3)/2\). The intermediate value theorem gives all and only the listed transition radii and maximizing modes.

**Smallest mode.** The sequence \(\log\lambda_{N,j}=\mathrm{const}+j\log q+\log(j+1+A)\) is strictly concave as a real function of \(j\); its discrete minimum must occur at an endpoint. Directly,
\[
\frac{\lambda_{N,N-1}}{\lambda_{N,0}}
=\frac{Nq^{N-1}}{1+(N-1)q^N}<1.
\]
For the last inequality, \(g(q)=1+(N-1)q^N-Nq^{N-1}\) satisfies \(g(1)=0\) and \(g'(q)=N(N-1)q^{N-2}(q-1)<0\) on \((0,1)\), so \(g(q)>0\). This proves uniqueness of the least eigenmode.

**Critical scaling and sharp conditioning.** For fixed \(c>0\), \(q_N^N=e^{-c}+O_c(N^{-1})\) and \(q_N^j=e^{-cj/N}(1+O_c(N^{-1}))\) uniformly for \(0\le j<N\). Rewriting the exact formula as
\[
\lambda_{N,j}=c^2q_N^j\left(\frac{j/N+1/N}{1-q_N^N}+\frac{q_N^N}{(1-q_N^N)^2}\right)
\]
proves the claimed uniform \(O_c(N^{-1})\) estimate. Differentiating the positive limiting profile yields
\[
F_c'(x)=\frac{c^3e^{-cx}}{1-e^{-c}}(x_c-x).
\]
Since \(e^c-1>c\) and \(\coth(c/2)>2/c\), its critical point obeys \(0<x_c<1/2\), and it is the unique strict maximum. The equality \(F_c(0)=F_c(1)=c^2e^{-c}/(1-e^{-c})^2\) identifies the endpoint minima. Uniform convergence and density of the grids imply convergence of maximal eigenvalues to \(F_c(x_c)\); the exact minimum-mode classification gives convergence of minimal eigenvalues to \(F_c(1)\). At the critical point, \(x_c+e^{-c}/(1-e^{-c})=1/c\), so \(F_c(x_c)=ce^{-cx_c}/(1-e^{-c})\), yielding precisely the displayed condition number. The maximizing-index convergence follows also from \(T_N(q_N)=Nx_c+O_c(1)\). Taylor expansion at \(c=0\) and elementary large-\(c\) comparison establish the two terminal asymptotics. Positivity of \(F_c\) throughout the compact interval establishes nondegenerate limiting upper and lower Riesz bounds.

## Verification
The standalone standard-library program `check_bergman_spectrum.py` evaluates eigenvalues both from direct cyclic Fourier diagonalization of the normalized kernel Gram matrix and from the closed formula, verifies the predicted extremizing indices for multiple degrees and radii, and compares finite-size spectra with the critical profile and condition-number limit. Running `python3 check_bergman_spectrum.py` prints `PASS: 177 finite DFT, extrema, and limiting-profile cases`. These computations are finite corroboration only: the proof of the unrestricted \(N,q\) theorem and the uniform limiting law is analytic above.

## Relationship to prior work
Aadi, Cruz, Hartmann, and Kellay (2022) develop sampling and interpolation criteria for weighted Bergman spaces, including the normalized reproducing-kernel model; their principal results are geometric conditions for possibly multiple nodes, not exact finite cyclic Gram spectra or this radius-driven extremal-mode classification. Earlier general RKHS sampling and interpolation theory gives the motivation for sharp Riesz bounds.

A closely related published result for **Hardy/Szegő** kernel orbit frames has a geometric-progression Fourier spectrum and monotone eigenvalues. The Bergman kernel has a squared denominator instead: its Fourier eigenvalues are nonmonotone, with an interior maximizing index and an infinite family of discrete mode transitions as the number of points varies. A separate two-ring Hardy/Bergman point-configuration result addresses optimal *relative rotation* of two concentric rings; it does not classify the one-ring radius-dependent maximizing modes or the critical one-ring scaling limit. Related Fourier diagonalizations of weighted harmonic Bergman circle-trace inequalities concern a continuous trace quadratic form, not this finite normalized-kernel interpolation Gram matrix. The elementary kernel power-series identity is standard and is not claimed as novel. The claimed contribution is the complete extremal-mode staircase together with its uniform critical spectral profile and explicit interpolation-conditioning law.

## Limitations
The theorem concerns the unweighted analytic Bergman disk, exactly regular \(N\)-gons, normalized point-evaluation kernels, and Gram/Riesz conditioning. It does not optimize arbitrary irregular point sets, handle weighted kernel powers other than two, claim sampling for an infinite union of these finite rings, or give joint limits with \(c\) varying with \(N\). The algebraic calculation of the finite spectrum may have unindexed prior formulations; novelty of the combined phase diagram and scaling law requires broader historical verification. Finite checker runs cannot establish an infinite theorem or resolve priority.

## References
1. D. Aadi, C. Cruz, A. Hartmann, and K. Kellay, *Multiple sampling and interpolation in Bergman spaces*, arXiv:2202.07263, first public 2022-02-15, https://arxiv.org/abs/2202.07263.
2. A. Aleman, M. Hartz, J. E. McCarthy, and S. Richter, *Interpolating sequences in spaces with the complete Pick property*, arXiv:1701.04885, https://arxiv.org/abs/1701.04885 (comparison context only, not an implication for Bergman kernel power two).
3. K. Tanaka, S. Särkkä, and T. Karvonen, *Kernel-based interpolation at approximate Fekete points*, arXiv:1912.07316, https://arxiv.org/abs/1912.07316 (kernel design context, not an exact circular spectrum).
