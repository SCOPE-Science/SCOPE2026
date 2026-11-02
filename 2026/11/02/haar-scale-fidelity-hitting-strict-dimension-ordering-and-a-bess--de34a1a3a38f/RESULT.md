# Haar-scale fidelity hitting: strict dimension ordering and a Bessel-to-exponential clock

## Finding
Consider isotropic Brownian motion on complex projective pure-state space in complex Hilbert-space dimension \(n\), started at a state orthogonal to a fixed target. With \(\kappa=4D>0\), where \(D\) multiplies the Fubini–Study Laplace–Beltrami operator, let \(\mathcal T_{n,z}\) be \(n\) times the first time that fidelity with the target reaches \(z/n\), for integer \(n\ge2\) and \(0<z<n\). For every \(s>0\),
\[
\mathbb E e^{-s\mathcal T_{n,z}}
=\left[\sum_{k=0}^{\infty}\frac{z^k}{(k!)^2}
\prod_{j=0}^{k-1}\left(\frac{s}{\kappa}+j+\frac{j(j-1)}n\right)\right]^{-1}.
\]
The empty product is one. At every fixed \(z>0\), for all integers \(n>z\), the transforms are strictly ordered:
\[
\mathbb E e^{-s\mathcal T_{n,z}}
<\mathbb E e^{-s\mathcal T_{n+1,z}}
<\frac1{{}_1F_1(s/\kappa;1;z)}.
\]
They converge to the rightmost transform, defining a nondegenerate limit \(\mathcal T_z\). Hence dimension controls the *entire hitting-time law in Laplace-transform order*, not only its mean. The invariant Haar probability of the target cap is \((1-z/n)^{n-1}\to e^{-z}\), so \(z\) is the natural fixed-rarity parameter.

Define
\[
H(z)=\sum_{k=1}^{\infty}\frac{z^k}{k\,k!},\qquad
C(z)=H(z)+\frac{(z-3)e^z+3}{2}
=\sum_{k=3}^{\infty}\frac{(k-1)(k-2)z^k}{2k\,k!}>0.
\]
Then the finite-dimensional mean is strictly decreasing to the limiting mean and has the sharp first correction
\[
\mathbb E\mathcal T_{n,z}
=\frac1\kappa\left(H(z)+\frac{C(z)}n+O_z(n^{-2})\right),\qquad
\mathbb E\mathcal T_z=\frac{H(z)}\kappa.
\]
With the harmonic numbers \(h_0=0\) and \(h_j=\sum_{r=1}^{j}r^{-1}\), put
\[
K(z)=2\sum_{k=1}^{\infty}\frac{h_{k-1}z^k}{k\,k!}.
\]
The limiting variance is exactly \(\operatorname{Var}(\mathcal T_z)=[H(z)^2-K(z)]/\kappa^2\). The normalized limiting clock interpolates between two distinct complete laws:
\[
\lim_{z\downarrow0}\mathbb E\exp\!\left(-\lambda\frac{\mathcal T_z}{\mathbb E\mathcal T_z}\right)
=\frac1{I_0(2\sqrt\lambda)},\qquad
\lim_{z\to\infty}\mathbb E\exp\!\left(-\lambda\frac{\mathcal T_z}{\mathbb E\mathcal T_z}\right)
=\frac1{1+\lambda},\quad \lambda\ge0.
\]
In particular, its squared coefficient of variation tends to \(1/2\) and \(1\), respectively. An exact calibration identity at the target-relaxation rate is \(\mathbb E e^{-\kappa\mathcal T_z}=e^{-z}\), equal to the limiting Haar cap probability.

## Assumptions and scope
For each integer \(n\ge2\), choose an isotropic Brownian motion on \(\mathbb CP^{n-1}\) with generator \(D\Delta_{\mathrm{FS}}\), with the usual Fubini–Study metric and the **same fixed** \(D>0\) in each dimension. Fix a target ray \(\eta\), and start from a ray orthogonal to it. The fidelity \(F_t^{(n)}=|\langle\psi_t,\eta\rangle|^2\) has state space \([0,1]\) and generator
\[
\mathcal G_n f(u)=\kappa\big[u(1-u)f''(u)+(1-nu)f'(u)\big],\qquad\kappa=4D.
\]
The endpoint \(u=0\) is a regular entrance value for the initial condition. For \(0<z<n\), define \(\tau_{n,z}=\inf\{t\ge0:F_t^{(n)}\ge z/n\}\) and \(\mathcal T_{n,z}=n\tau_{n,z}\). All statements concern this continuous Brownian model, not a general finite-step random walk, an arbitrary quantum channel, or a microscopic Lindblad dynamics. The limit \(n\to\infty\) is taken at fixed \(D\) and fixed \(z>0\); the subsequent \(z\downarrow0\) and \(z\to\infty\) limits concern the *limiting* clock, not a simultaneous uncontrolled joint limit.

## Proof
**Radial reduction.** The radial Fubini–Study generator follows from the isotropic Brownian radial Laplacian. Set \(Y_t^{(n)}=nF_{t/n}^{(n)}\). Chain rule and time change yield its generator, on \([0,n]\),
\[
\mathcal L_n f(y)=\kappa\left[y\left(1-\frac yn\right)f''(y)+(1-y)f'(y)\right].
\]
Its first-hitting time of \(z\) is precisely \(\mathcal T_{n,z}\). At \(n\to\infty\), the limiting generator \(\mathcal L_\infty f=\kappa[yf''+(1-y)f']\) is the square-root (CIR) diffusion with exponential invariant law. The boundary-value arguments below independently establish convergence of its hitting-time distribution, without relying on informal path convergence.

**Exact transform and dimension comparison.** Let \(q=s/\kappa>0\), and let \(A_n(y;q)\) be the solution, analytic at \(y=0\) and normalized by \(A_n(0;q)=1\), of
\[
y(1-y/n)A_n''+(1-y)A_n'-qA_n=0.
\]
Writing \(A_n(y;q)=\sum_{k\ge0}a_{n,k}(q)y^k\) gives the exact recurrence
\[
a_{n,0}=1,\qquad
(k+1)^2a_{n,k+1}=\left(q+k+\frac{k(k-1)}n\right)a_{n,k}.
\]
All coefficients are positive for \(q>0\), and the series converges for \(|y|<n\). The bounded-at-zero solution of the hitting-time boundary-value problem \(\mathcal L_n u=su\), \(u(z)=1\), is \(u(y)=A_n(y;q)/A_n(z;q)\), so \(\mathbb E_0e^{-s\mathcal T_{n,z}}=1/A_n(z;q)\). For each \(k\ge3\), its coefficient is strictly decreasing with \(n\), since \(j(j-1)/n\) strictly decreases for \(j\ge2\). Coefficients for \(k\le2\) are independent of \(n\). Positivity proves both strict Laplace inequalities. For any fixed \(z\), choose a finite integer \(n_0>z\). Since the terms for \(n\ge n_0\) are dominated by the summable \(A_{n_0}\) terms, their limit is
\[
A_\infty(z;q)=\sum_{k=0}^{\infty}\frac{(q)_k z^k}{(k!)^2}={}_1F_1(q;1;z),
\]
where \((q)_k\) is the rising factorial. This is the regular Laplace-transform solution for the CIR hitting clock and proves distributional convergence by uniqueness of Laplace transforms. Analytic convergence around \(q=0\), alternatively the standard compact-level hitting-time moment recursions, gives convergence of the displayed first two moments.

**Strict finite-dimensional delay and first correction.** Differentiating \(A_n\) at \(q=0\) gives the exact convergent positive series
\[
\kappa\mathbb E\mathcal T_{n,z}
=\sum_{k=1}^\infty\frac{z^k}{k\,k!}
\prod_{j=1}^{k-2}\left(1+\frac jn\right),
\]
where a product with upper index smaller than its lower index is one. Every coefficient from \(k=3\) strictly decreases with \(n\), proving strict decrease of the mean. For fixed \(z\), expand the product to first order: its coefficient is \((k-1)(k-2)/(2n)\). Uniform convergence on compact \(z\)-intervals gives the stated \(H(z)+C(z)/n+O_z(n^{-2})\). Independently, the exact integral
\[
\kappa\mathbb E\mathcal T_{n,z}
=\frac n{n-1}\int_0^z\frac{(1-y/n)^{-(n-1)}-1}{y}\,dy
\]
allows a uniform Taylor expansion and the equivalent closed form for \(C(z)\). Its power series proves strict positivity.

**Variance and small-target clock.** For \(M(q,z)={}_1F_1(q;1;z)\), differentiating its rising-factorial series at \(q=0\) yields \(\partial_qM(0,z)=H(z)\) and \(\partial_q^2M(0,z)=K(z)\). Twice differentiating \(1/M(s/\kappa,z)\) gives \(\mathbb E\mathcal T_z=H(z)/\kappa\) and \(\operatorname{Var}(\mathcal T_z)=(H(z)^2-K(z))/\kappa^2\). Since \(H(z)=z+O(z^2)\) and \(K(z)=z^2/2+O(z^3)\), the squared coefficient of variation tends to \(1/2\). To identify the *complete* small-target law, take \(q=\lambda/H(z)\sim\lambda/z\). The coefficient identity \((q)_kz^k=\prod_{j=0}^{k-1}(qz+jz)\) and a uniform ratio bound permit termwise convergence to \(\sum_{k\ge0}\lambda^k/(k!)^2=I_0(2\sqrt\lambda)\). Taking reciprocals proves the small-target transform.

**Large-target exponential clock.** Set \(H(z)=\sum_{k\ge1}z^k/(k\,k!)\) and define the probability law \(\nu_z(k)=z^k/(k\,k!H(z))\), for integers \(k\ge1\). For \(q>0\),
\[
M(q,z)=1+qH(z)\,\mathbb E_{\nu_z}\!\left[\prod_{j=1}^{K-1}(1+q/j)\right].
\]
For \(0<q\le1\), the product is between \(1\) and \(e^qK^q\). Concavity implies \(\mathbb E_{\nu_z}K^q\le(\mathbb E_{\nu_z}K)^q\), and \(\mathbb E_{\nu_z}K=(e^z-1)/H(z)\sim z\), whereas \(H(z)\sim e^z/z\). Choosing \(q=\lambda/H(z)\) gives an expectation between \(1\) and \(e^q((e^z-1)/H(z))^q\to1\). Therefore \(M(\lambda/H(z),z)\to1+\lambda\), proving the unit-mean exponential limit. Finally \(K(z)/(2H(z))=\mathbb E_{\nu_z}h_{K-1}\le1+\log\mathbb E_{\nu_z}K=O(\log z)\), so \(K(z)/H(z)^2\to0\), establishing the variance-ratio limit. The identity \(M(1,z)=e^z\) gives the exact Haar-calibration identity.

## Verification
The accompanying `verify.py` is executable using the Python standard library. Run `python verify.py`. It checks exact rational recurrences for the regular hitting-transform series; strict dimension comparisons and mean-series comparisons over multiple dimensions; and numerical moment, boundary, and finite-size-correction identities. The checker reports **927 successful bounded checks** in the recorded execution. These checks are finite demonstrations, not certifications of infinite series, all dimensions, or either limiting distribution; those conclusions are established by the proofs above. The exact finite-dimensional transform can also be reproduced as \(A_n(z;s/\kappa)={}_2F_1(a,b;1;z/n)\), where \(a+b=n-1\) and \(ab=sn/\kappa\).

## Relationship to prior work
Tóth (2026, arXiv:2606.11438v1, first public June 9, 2026) gives the isotropic projective Brownian framework, the radial Jacobi spectral representation, and finite-dimensional first-passage means and long-time tails. Those results, including the exact finite-dimensional hitting problem, are *prior work*. The claim here is the strict **cross-dimensional** Laplace-transform comparison under the Haar-scale threshold \(z/n\), its positive sharp finite-size correction, and the complete two-regime **normalized** first-hitting law. A generic CIR process's Kummer first-passage transform is also known; its use alone is not claimed to be new (Song, Xu, Wang, 2016). General Jacobi hitting problems and OU first-passage asymptotics are further relevant context (D'Onofrio, Patie, Sacerdote, 2022; Martin, Kearney, Craster, 2019). The closest full projective paper does not state a dimension-to-dimension Laplace comparison or these explicit normalized crossover laws; the earlier general CIR/Jacobi works may provide broader methods but do not, in accessible descriptions, identify this particular projective-fidelity comparison.

## Limitations
Only projectively isotropic Brownian dynamics at a *fixed* Fubini–Study diffusion coefficient are treated. The two asymptotic target regimes are sequential after the dimension limit; uniform joint-limit rates are not asserted. Laplace-transform order is weaker than samplewise or usual stochastic order. No claim is made for individual experimental quantum systems or general finite-step random walks. The standard CIR hitting-function and generic confluent limit are credited as existing techniques. A yet-unlocated abstract Jacobi dimension-comparison theorem could imply the strict-order statement, and prior work beyond the inspected sources remains a publication-priority risk. No independent proof audit or independent publication-priority determination has been performed.

## References
- G. I. Tóth, *Isotropic random walks and Brownian diffusion on complex projective space*, arXiv:2606.11438v1 (public June 9, 2026), https://arxiv.org/abs/2606.11438 ; full text https://pdfs.assets.alphaxiv.org/2606.11438v1.pdf .
- S. Song, G. Xu, Y. Wang, *On First Hitting Times for Skew CIR Processes*, Methodology and Computing in Applied Probability 18 (2016), 169–180, https://doi.org/10.1007/s11009-014-9406-7 .
- G. D'Onofrio, P. Patie, L. Sacerdote, *Jacobi processes with jumps as neuronal models: a first passage time analysis*, arXiv:2205.08237 (2022), https://arxiv.org/abs/2205.08237 .
- R. J. Martin, M. J. Kearney, R. V. Craster, *Long- and short-time asymptotics of the first-passage time of the Ornstein-Uhlenbeck and other mean-reverting processes*, Journal of Physics A 52 (2019), https://doi.org/10.1088/1751-8121/ab0836 .
