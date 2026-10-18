# A critical entropy-tilt edge with logarithmic finite-size response in a skew-coupled Gaussian chain

## Finding

A nonreciprocal Ornstein–Uhlenbeck chain can have an exactly factorized stationary Gaussian law while its **entropy-production fluctuations** develop a singular many-particle response. For the open, antisymmetrically coupled chain defined below, set
\[
\lambda_*:=\frac{\sqrt{1+\kappa^2/(4J^2)}-1}{2},\qquad
L_*:=\sqrt{1+\kappa^2/(4J^2)}.
\]
The finite-chain scaled cumulant generating function \(\Psi_N\) of the stochastic entropy production obeys the **exact identity**
\[
\boxed{\displaystyle
\Psi_N(\lambda_*)=\frac{\kappa}{2}\left[N-\cot\!\left(\frac{\pi}{2(N+1)}\right)\right].}
\]
Its derivative at the same, infinite-chain critical tilt has the **sharp two-term finite-size asymptotic**
\[
\boxed{\displaystyle
\Psi_N'(\lambda_*)=\frac{8J^2L_*}{\pi\kappa}(N+1)
\left[\log(N+1)+\gamma+\log(2/\pi)-1\right]
+O_{\kappa,J}(1).}
\]
Here \(\gamma\) is Euler's constant. Consequently \(\Psi_N(\lambda_*)/N\to\kappa(1/2-1/\pi)\), but \(\Psi_N'(\lambda_*)/(N\log N)\to8J^2L_*/(\pi\kappa)>0\). The mean entropy-production rate at zero tilt, by contrast, is \(\Psi_N'(0)=2J^2(N-1)/\kappa\). The novel claim is the exact **critical many-particle edge behavior** and its sharp divergence, not the general Riccati solution of finite-dimensional Gaussian large deviations.

## Assumptions and scope

Fix an integer \(N\ge2\), friction \(\kappa>0\), coupling \(J>0\), and diffusivity \(D>0\). Define the real \(N\times N\) skew-symmetric matrix \(A_N\) by \((A_N)_{i,i+1}=J\), \((A_N)_{i+1,i}=-J\) for \(1\le i<N\), with every other entry zero. Let \(X_t\in\mathbb R^N\) solve the Itô equation
\[
 dX_t=(-\kappa I_N+A_N)X_t\,dt+\sqrt{2D}\,dW_t,
\]
where \(W_t\) is standard \(N\)-dimensional Brownian motion and \(X_0\) is independent and distributed according to the stationary law \(\mathcal N(0,(D/\kappa)I_N)\). Define the time-integrated medium entropy production with a positive time-reversal convention by
\[
 S_T=\frac1D\int_0^T(A_NX_t)\cdot\circ dX_t.
\]
The circle denotes a Stratonovich integral. For real \(\lambda\) in the interior of the interval on which the long-time exponential moment is finite, set
\[
 \Psi_N(\lambda)=\lim_{T\to\infty}\frac1T
 \log\mathbb E\big[\exp(\lambda S_T)\big].
\]
All displayed claims use **open boundary conditions** and this normalization of \(S_T\), not a boundary-to-boundary heat flux. The critical tilt \(\lambda_*\) is a function of \(\kappa/J\) and **does not depend on \(N\) or \(D\)**. Every finite \(N\) admits \(\lambda_*\) as an interior tilt. The limit \(T\to\infty\) is taken before \(N\to\infty\).

## Proof

**1. Stationarity and the tilted generator.** Since \(A_N^{\mathsf T}=-A_N\), the covariance matrix \((D/\kappa)I_N\) solves the Lyapunov equation, and all eigenvalues of \(-\kappa I_N+A_N\) have real part \(-\kappa\). Thus the claimed Gaussian law is uniquely stationary. Furthermore \(\nabla\cdot(A_Nx)=\operatorname{tr}A_N=0\); the Stratonovich integral therefore equals its Itô version. The deterministic contribution to entropy production is \(D^{-1}|A_NX_t|^2\), because \((A_Nx)\cdot x=0\). Exponential Itô tilting gives the Feynman–Kac generator
\[
 \mathcal L_\lambda=
 D\Delta+[-\kappa x+(1+2\lambda)A_Nx]\cdot\nabla
 +\frac{\lambda(1+\lambda)}D|A_Nx|^2.
\]
At \(\lambda=0\), stationary averaging yields
\[
 \Psi_N'(0)=\frac1D\mathbb E|A_NX_0|^2
 =\frac1\kappa\operatorname{tr}(A_N^{\mathsf T}A_N)
 =\frac{2J^2(N-1)}\kappa.
\]

**2. Exact finite-chain spectral formula.** Multiplying \(A_N\) by \(i\) and performing the diagonal unitary phase change gives the Hermitian open-chain tridiagonal adjacency matrix with hopping \(J\). Its eigenvalues are \(2J\cos(\pi j/(N+1))\), for \(1\le j\le N\). The real skew matrix therefore admits an orthogonal direct sum of planar rotation blocks with positive frequencies
\[
 \omega_j=2J\cos\!\left(\frac{\pi j}{N+1}\right),\quad
 1\le j\le m:=\lfloor N/2\rfloor,
\]
plus one zero mode when \(N\) is odd. Orthogonal transformation preserves independent isotropic noises and the stationary Gaussian, so the tilted expectation factorizes by blocks.

For one planar block of frequency \(\omega>0\), use the Gaussian ansatz \(u(t,x)=\exp(a(t)|x|^2/(2D)+b(t))\) for \(\mathbb E_x[e^{\lambda S_t}]\). The displayed tilted generator yields, with \(a(0)=b(0)=0\),
\[
 a'=2(a^2-\kappa a+\omega^2\lambda(1+\lambda)),
 \qquad b'=2a.
\]
For tilts with \(\kappa^2-4\omega^2\lambda(1+\lambda)>0\) in a neighborhood of zero, the solution converges to the stable root
\[
 a_-=\frac{\kappa-\sqrt{\kappa^2-4\omega^2\lambda(1+\lambda)}}2,
\]
which satisfies \(a_-<\kappa\). Integration over the stationary Gaussian contributes only a bounded logarithmic prefactor because \(a(t)<\kappa\), and hence the planar scaled cumulant generating function is \(2a_-\). Summing independent blocks proves, for all \(\lambda\) in the connected admissible open interval containing zero,
\[
 \boxed{\displaystyle
 \Psi_N(\lambda)=\sum_{j=1}^{m}
 \left[\kappa-\sqrt{\kappa^2-16J^2\lambda(1+\lambda)
 \cos^2\!\left(\frac{\pi j}{N+1}\right)}\right].}
\]
For \(\lambda\) at the stated critical value the radicands are strictly positive, because each finite-chain cosine has magnitude below one. The same formula gives the fluctuation symmetry \(\Psi_N(\lambda)=\Psi_N(-1-\lambda)\) wherever both sides are defined.

**3. Critical finite-size identity.** The defining identity \(16J^2\lambda_*(1+\lambda_*)=\kappa^2\) makes the \(j\)-th square root \(\kappa\sin(\pi j/(N+1))\). Put \(n=N+1\). The finite sine-sum identity, proved by summing a geometric progression of complex unit roots, is
\[
 \sum_{j=1}^{\lfloor N/2\rfloor}\sin\frac{\pi j}{n}
 =\frac12\left[\cot\frac{\pi}{2n}
 -\mathbf 1_{\{N\ \mathrm{odd}\}}\right].
\]
Together with \(2\lfloor N/2\rfloor+\mathbf 1_{\{N\ \mathrm{odd}\}}=N\), this establishes the exact cotangent expression. The standard small-argument expansion of cotangent gives the finite limit \(\Psi_N(\lambda_*)/N\to\kappa(1/2-1/\pi)\).

**4. Logarithmically divergent critical derivative.** Differentiating the finite-chain expression (legal because \(\lambda_*\) is interior for every finite \(N\)) gives
\[
 \Psi_N'(\lambda_*)=\frac{8J^2L_*}{\kappa}
 \sum_{j=1}^{\lfloor N/2\rfloor}
 \left[\csc\frac{\pi j}{n}-\sin\frac{\pi j}{n}\right].
\]
The sine sum is \(n/\pi+O(1)\), by the exact identity in step 3. For the cosecant sum, subtract the harmonic singularity:
\[
 \sum_{j=1}^{\lfloor N/2\rfloor}\csc\frac{\pi j}{n}
 =\frac n\pi H_{\lfloor N/2\rfloor}
 +\sum_{j=1}^{\lfloor N/2\rfloor}
 \left(\csc\frac{\pi j}{n}-\frac n{\pi j}\right).
\]
The function \(f(x)=\csc(\pi x)-1/(\pi x)\), continuously extended to \([0,1/2]\), is smooth, so the last sum is
\[
 n\int_0^{1/2}f(x)\,dx+O(1)
 =\frac n\pi\log\frac4\pi+O(1).
\]
Since \(H_{\lfloor N/2\rfloor}=\log n+\gamma-\log2+O(1/n)\),
\[
 \sum_{j=1}^{\lfloor N/2\rfloor}\csc\frac{\pi j}{n}
 =\frac n\pi\left[\log n+\gamma+\log(2/\pi)\right]+O(1).
\]
Subtracting the sine sum proves the claimed sharp two-term expansion with an \(O(1)\) absolute remainder. This completes the proof.

## Verification

The standalone file `verify.py` reconstructs the skew-tridiagonal spectrum numerically and independently solves the planar finite-time Riccati problem; checks the exact critical cotangent identity, fluctuation symmetry, and zero-tilt entropy rate; and compares the sharp critical derivative with direct mode sums at multiple \(\kappa,J,N\). Its recorded run completed **366 assertions** successfully (including \(N\) through \(4000\) for the edge asymptotic). These finite computations corroborate the formulas but do not replace the spectral and analytic proof.

To reproduce in a Python environment with NumPy and SciPy installed, execute `python verify.py` beside this document. The calculations require no external data.

## Relationship to prior work

Pal and Gupta (2026) introduce nonreciprocal Ornstein–Uhlenbeck models and identify the stationary factorization and complex-mode decomposition of the antisymmetric regime, together with stationary heat/entropy-production observables. Those are not asserted to be new here. Du Buisson and Touchette (2023) give **general linear-diffusion current large-deviation formulas**, including the Riccati route used here, and Mazzolo and Monthus (2022) analyze entropy-production large deviations in Gaussian gyrators. Such results already imply a route to the finite-dimensional tilted formula; that finite-dimensional derivation is explicitly treated as supporting machinery, not the new theorem. Godrèche and Luck (2018) analyze irreversible OU stationary states and Gaussian spin-chain means. Jakšić, Pillet, and Shirikyan (2017) establish fluctuation theorems and the matrix-Riccati/spectral characterization for general thermally driven harmonic networks; their source concerns bath-driven oscillator networks rather than the present skew first-order chain, but it reinforces that general entropy-current spectral machinery is prior art.

The distinct statement established here is the **specific many-body critical spectral edge** of an open skew chain: exact finite-length cotangent generating function at a size-independent critical tilt, together with the sharp \((N+1)\log(N+1)\) derivative divergence, including its coefficient and linear correction. The inspected primary materials did not provide this many-particle critical fluctuation statement. Nonetheless, a more general harmonic-network asymptotic or an uninspected appendix might imply it; search exhaustiveness and priority beyond the compared sources are not claimed.

## Limitations

The theorem applies to homogeneous, open-boundary, antisymmetrically coupled linear diffusions started in their stationary state. The stochastic action is medium entropy production; a finite observation-window boundary contribution to total entropy changes at most the finite-time generating function and may alter its analyticity domain, so it is not silently substituted. The \(T\to\infty\) limit precedes the many-particle limit. The result does not establish a full infinite-chain rate function, a finite-time large-deviation estimate uniform in chain length, nonlinear or disordered interactions, or independence from all possible alternative definitions of entropy production. General OU fluctuation theory and the source's stationary factorization are prior work. No independent audit has been performed.

## References

1. S. K. Pal and S. Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration*, arXiv:2609.05391v1 (first public version September 4, 2026), https://arxiv.org/abs/2609.05391.
2. J. du Buisson and H. Touchette, *Dynamical large deviations of linear diffusions*, arXiv:2212.12022 (2022 preprint; published 2023), https://arxiv.org/abs/2212.12022.
3. C. Monthus and C. Mazzolo, *Nonequilibrium diffusion processes via non-Hermitian electromagnetic quantum mechanics with application to the statistics of entropy production in the Brownian gyrator*, arXiv:2210.05353 (2022), https://arxiv.org/abs/2210.05353.
4. C. Godrèche and J. M. Luck, *Characterising the nonequilibrium stationary states of Ornstein-Uhlenbeck processes*, arXiv:1807.00694 (2018), https://arxiv.org/abs/1807.00694.
5. V. Jakšić, C.-A. Pillet and A. Shirikyan, *Entropic fluctuations in thermally driven harmonic networks*, arXiv:1606.01498 (2016 preprint; published 2017), https://arxiv.org/abs/1606.01498.
