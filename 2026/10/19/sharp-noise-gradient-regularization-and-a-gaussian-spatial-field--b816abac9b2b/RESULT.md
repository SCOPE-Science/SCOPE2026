# Sharp noise-gradient regularization and a Gaussian spatial field at a nonnormal exceptional point

## Finding

An open unidirectional Ornstein–Uhlenbeck chain with spatially graded independent noise exhibits a sharp suppression threshold at bath exponent \(\beta=1/2\), despite having the identical stable drift spectrum in every system size. For gradients below that threshold, the stationary coordinates separated by order \(\sqrt N\) converge, after amplitude rescaling, to an explicitly determined Gaussian spatial field. This is a statement about **spatially inhomogeneous baths**; the homogeneous-noise covariance and the exceptional-point drift were established previously [1].

Precisely, for \(D>0\), \(k>0\), \(\beta\geq0\), and any integer \(N\geq1\), the stationary covariance \(C^{(N)}_{ij}=\mathbb E[X_iX_j]\) is, for \(1\leq i\leq j\leq N\),
\[
C^{(N)}_{ij}(k,\beta)=\frac{D}{k}\sum_{m=0}^{N-j}
\frac{(j+m)^{-\beta}}{k^{2m+j-i}}
\frac{\binom{2m+j-i}{m}}{2^{2m+j-i}}.
\tag{1}
\]
The covariance is symmetric in \(i,j\). At the critical damping \(k=1\), the upstream variance \(V_N=C^{(N)}_{11}(1,\beta)\) satisfies the **complete bath-gradient trichotomy**
\[
V_N\sim\frac{D}{\sqrt\pi(1/2-\beta)}N^{1/2-\beta}
\quad(0\leq\beta<1/2),
\qquad V_N=\frac{D}{\sqrt\pi}\log N+O(1)\quad(\beta=1/2),
\]
while for every \(\beta>1/2\),
\[
V_N\uparrow V_\infty(D,\beta)=D\sum_{m=0}^{\infty}
(m+1)^{-\beta}\binom{2m}{m}4^{-m}<\infty.
\tag{2}
\]

For \(0\leq\beta<1/2\) and any fixed \(\lambda\in\mathbb R\), set \(k_N=1+\lambda/N\) (positive for all sufficiently large \(N\)), and for \(u\geq0\) define \(i_N(u)=1+\lfloor u\sqrt N\rfloor\) and \(Z_N(u)=N^{\beta/2-1/4}X^{(N)}_{i_N(u)}\) in the stationary chain with damping \(k_N\). Then for every finite collection of \(u\)'s, \(Z_N\) converges jointly in law to a centered Gaussian field with covariance
\[
K_{\lambda,\beta}(u,v)=\frac{D}{\sqrt\pi}
\int_0^1 t^{-\beta-1/2}\exp\!\left(-2\lambda t-\frac{(u-v)^2}{4t}\right)dt.
\tag{3}
\]
Its local increment variance has the exact leading power, for \(h\downarrow0\),
\[
K_{\lambda,\beta}(0,0)-K_{\lambda,\beta}(0,h)
\sim \frac{D\,\Gamma(\beta+1/2)}{
\sqrt\pi\,(1/2-\beta)\,2^{1-2\beta}}h^{1-2\beta}.
\tag{4}
\]
The leading local coefficient is independent of \(\lambda\). The Gaussian field need not be identified with fractional Brownian motion: equation (4) describes only its local second-order roughness.

## Assumptions and scope

Consider independent standard two-sided Brownian motions \(W_j\), and, for each fixed finite \(N\), the unique stationary solution of
\[
 dX_j=(-kX_j+X_{j+1})\,dt+\sqrt{2D\,j^{-\beta}}\,dW_j,
 \qquad 1\leq j\leq N,\qquad X_{N+1}=0.
 \tag{5}
\]
The drift matrix is \(-kI+J_N\), where \((J_N)_{j,j+1}=1\) and other entries vanish. For \(N\geq2\), it is one Jordan block with repeated eigenvalue \(-k<0\); thus there is a unique stationary centered Gaussian vector for every \(k>0\), regardless of the system size. The spatial bath intensity is \(D_j=Dj^{-\beta}\). The critical value \(k=1\) is measured in units of the fixed directional coupling, which is one. The thermodynamic limit is along positive integers \(N\); no uniform-in-\(N\) mixing-time or pathwise limit is claimed.

## Proof

**Exact covariance.** The nilpotence of \(J_N\) gives, for \(\tau\geq0\),
\[
(e^{(-kI+J_N)\tau})_{i\ell}
=\mathbf1_{\{\ell\geq i\}}e^{-k\tau}\frac{\tau^{\ell-i}}{(\ell-i)!}.
\]
Writing the stationary solution as a stochastic convolution against past increments of the independent \(W_\ell\)'s and applying Itô isometry, for \(i\leq j\),
\[
C^{(N)}_{ij}
=2D\sum_{\ell=j}^{N}\ell^{-\beta}
\int_0^\infty e^{-2k\tau}
\frac{\tau^{2\ell-i-j}}{(\ell-i)!(\ell-j)!}\,d\tau.
\]
Use \(\int_0^\infty e^{-2k\tau}\tau^q d\tau=q!/(2k)^{q+1}\) for integer \(q\geq0\), then substitute \(\ell=j+m\), to get equation (1) exactly. This also verifies every covariance normalization factor without reliance on previously published finite-chain formulas.

**Bath-gradient trichotomy.** At \(i=j=k=1\), equation (1) reduces to
\[
V_N=D\sum_{m=0}^{N-1}(m+1)^{-\beta}b_m,
\qquad b_m=\binom{2m}{m}4^{-m}.
\]
Stirling's formula gives \(b_m=(\pi m)^{-1/2}(1+O(m^{-1}))\) for \(m\geq1\). Therefore the summand is \(\pi^{-1/2}m^{-\beta-1/2}(1+O(m^{-1}))\). Elementary power-sum and harmonic-sum estimates prove all three cases in (2), including the exact constants and the \(O(1)\) remainder at \(\beta=1/2\). In the convergent case the tail is \(O(N^{1/2-\beta})\), and positivity makes the limit monotone. The \(\beta=0\) homogeneous special case follows from earlier covariance theory; the transition for spatial bath gradients is the new conclusion.

**Critical-window Gaussian field.** Take \(i=i_N(u)\), \(j=i_N(v)\) and exchange indices if necessary. Let \(d=j-i\), so \(d/\sqrt N\to|u-v|\). Set
\[
b_{m,d}=2^{-2m-d}\binom{2m+d}{m}.
\]
Uniform Stirling expansion on \(m/N\in[\varepsilon,1]\), for each fixed \(\varepsilon>0\), yields
\[
b_{m,d}=\frac{1+o(1)}{\sqrt{\pi m}}
\exp\!\left(-\frac{d^2}{4m}\right).
\]
Moreover, a global binomial mass bound implies \(b_{m,d}\leq C(m+1)^{-1/2}\) for all \(m,d\geq0\). Since \(j+m\geq m+1\), for fixed \(\lambda\) the factor \(k_N^{-(2m+d+1)}\) is uniformly bounded over \(0\leq m\leq N\). Thus, after multiplying the covariance by \(N^{\beta-1/2}\), the terms with \(m\leq\varepsilon N\) contribute at most \(C_{\lambda,\beta}\varepsilon^{1/2-\beta}+o(1)\). On the remaining range, \((j+m)/N\to t\), \(k_N^{-(2m+d+1)}\to e^{-2\lambda t}\), and the sum in (1) is a Riemann sum converging to (3). Sending \(\varepsilon\downarrow0\) completes the covariance limit, including coinciding observation sites. All finite-dimensional vectors are Gaussian, so convergence of their covariance matrices proves joint convergence in distribution. Positive definiteness of (3) also follows directly by observing that for each \(t>0\), \(\exp(-(u-v)^2/(4t))\) is a Gaussian covariance kernel, and (3) is its positive integral mixture.

**Small-separation law.** Subtract (3) at separation zero and at \(h>0\), and substitute \(s=h^2/(4t)\). After division by \(h^{1-2\beta}\), dominated convergence applies because \(0\leq\beta<1/2\) and
\[
\int_0^\infty s^{\beta-3/2}(1-e^{-s})ds
=\frac{\Gamma(\beta+1/2)}{1/2-\beta}.
\]
This gives (4). The factor \(e^{-2\lambda h^2/(4s)}\) tends to one, explaining the independence of the leading local coefficient from the critical-window parameter.

## Verification

The standalone file `VERIFIER.py` verifies, with exact rational arithmetic, the full finite-dimensional continuous Lyapunov identities for multiple sizes, positive dampings, and three integer bath exponents. Additional deterministic floating-point checks compare finite \(N\) weighted covariances against equation (3), verify the variance asymptotics and their logarithmic increment, and test the local roughness coefficient. At the time of this report it passed **1,864 assertions**. These tests do not prove the infinite-dimensional scaling or source novelty; the preceding calculations provide the mathematical proof. Reproduce with `python3 VERIFIER.py` in the directory containing this file.

## Relationship to prior work

Pal and Gupta [1], Model III, section IV.C, equation (84), obtain the finite-chain covariance at the exceptional point with **spatially constant** noise intensity. Inverting the site ordering matches the homogeneous \(\beta=0\) specialization of (1); it is expressly prior art. Their analysis of exceptional-point relaxation and the homogeneous covariance does not give the \(\beta>0\) bath-regularization threshold or the critical-window spatial field (3)–(4). Their general Gaussian stochastic-convolution identity is likewise not claimed as new. The extension to heterogeneous baths is computationally elementary at finite \(N\); the value here is the sharp infinite-chain classification and its spatial limiting law.

Hennequin, Vogels and Gerstner [2] analyze nonnormal amplification, including feedforward connectivity, in stochastic neuronal networks. Their general physical mechanism is foundational background, but their analyzed random-network amplification observables differ from the spatially graded one-way chain, and the paper does not state the particular \(\beta=1/2\) threshold or the kernel (3). A further mathematical result about singular spectra of nilpotent-shift resolvents [3] treats operator singular values, not heterogeneous stationary stochastic convolution covariances; it neither states nor directly implies (2)–(4).

## Limitations

The independent noise has exactly the fixed power-law profile \(D_j=Dj^{-\beta}\), the directional coupling is one and the drift is an open chain. There is no claim for periodic boundaries, correlated noises, nonlinear response, growing observation windows, or fixed positive values of \(k\) away from the critical window. Equation (3) establishes finite-dimensional distribution convergence, **not** path-space convergence. The local law (4) is a second-moment asymptotic, not an identification of the entire Gaussian field as a fractional Brownian process. Prior general OU covariance identities supply the main algebraic starting point, and potential implicit coverage by a broader weighted local-limit theorem remains an originality risk; no independent audit has occurred.

## References

[1] S. K. Pal and S. Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration*, arXiv:2609.05391v1 (first posted 2026-09-04), especially section IV.C and Eq. (84). https://arxiv.org/pdf/2609.05391

[2] G. Hennequin, T. P. Vogels and W. Gerstner, *Nonnormal amplification in random balanced neuronal networks*, arXiv:1204.2945v1 (2012), sections 1–3. https://arxiv.org/pdf/1204.2945

[3] *First-order critical-window singular spectra of nilpotent-shift resolvents*, public mathematical research record, 2026 (publicly indexed prior result). This comparison concerns resolvent singular values, not noise-weighted OU stationary covariances.
