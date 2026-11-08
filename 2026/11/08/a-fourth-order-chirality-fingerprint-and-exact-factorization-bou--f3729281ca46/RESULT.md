# A fourth-order chirality fingerprint and exact factorization boundary for harmonically trapped four-state swimmers

## Finding
For a planar four-direction run-and-tumble swimmer confined by an isotropic harmonic trap, differing clockwise and counterclockwise quarter-turn rates break the exact product decomposition of its stationary position law. Although all stationary positional moments of total degree at most three are invariant under reversal of that rate bias, the first signed, position-only chirality witness occurs at degree four. Its value, and a positive square-dependence diagnostic, have exact closed forms that are unchanged by isotropic translational Brownian noise.

Specifically, set \(\Gamma=a+b\), \(\Delta=a-b\), \(A=\mu+\Gamma\), \(Q=A^2+\Delta^2\) and \(R=(3\mu+\Gamma)^2+\Delta^2\). With rotated stationary coordinates \(U=(X+Y)/\sqrt{2}\) and \(V=(X-Y)/\sqrt{2}\),
\[
\boxed{\mathbb E[U^3V]=\frac{3c^4\Delta}{4AQR}.}
\]
Moreover, despite \(\mathbb E[UV]=0\),
\[
\boxed{\operatorname{Cov}(U^2,V^2)=\frac{c^4\Delta^2\big(\Delta^2+5\Gamma^2+14\mu\Gamma+9\mu^2\big)}{4\mu A Q^2R}.}
\]
Thus the fourth mixed moment has the sign of the clockwise-minus-counterclockwise rate and is nonzero exactly when those rates differ. The square covariance is strictly positive exactly then. The stationary positional law factors as a product in the \((U,V)\) coordinates **if and only if** \(a=b\), for every translational diffusivity \(D\ge0\). The signed fourth moment is a minimal-degree polynomial statistic for detecting the **sign** of the turning bias from stationary positions alone.

## Assumptions and scope
Let \(\Theta_t\in\{E,N,W,S\}\) be a continuous-time irreducible Markov chain. From each direction it turns clockwise by \(90^\circ\) at rate \(a>0\), or counterclockwise by \(90^\circ\) at rate \(b>0\), with no direct reversals. Its stationary distribution is uniform. Given \(\Theta_t\), let the planar position solve
\[
 d\mathbf X_t=(-\mu\mathbf X_t+c\mathbf e_{\Theta_t})\,dt+\sqrt{2D}\,d\mathbf B_t,
\]
where \(\mu>0\), \(c>0\), \(D\ge0\), \(\mathbf e_E=(1,0)\), \(\mathbf e_N=(0,1)\), \(\mathbf e_W=(-1,0)\), \(\mathbf e_S=(0,-1)\), and \(\mathbf B\) is a two-dimensional standard Brownian motion independent of \(\Theta\). All claims concern the unique stationary law; no initial-state or finite-time factorization is asserted when \(a\ne b\).

The stationary process is well-defined by the stable Ornstein--Uhlenbeck filter of a two-sided stationary orientation chain and an independent stationary Gaussian filter. The active part lies inside \(|U|,|V|\le c/(\sqrt2\mu)\). Gaussian thermal noise can make the full support unbounded, but does not change the stated connected fourth-order quantities.

## Proof
**1. Rotated sign process.** Let \(s,t\in\{-1,1\}\) encode the four directions in the order \(E=(+,+)\), \(N=(+,-)\), \(W=(-,-)\), \(S=(-,+)\). Write \(w=c/\sqrt2\). The active rotated position satisfies \(\dot U=-\mu U+ws\), \(\dot V=-\mu V+wt\). Set \(\gamma=\Gamma/2\), \(\eta=\Delta/2\). The orientation generator \(L\) acts by
\[
L1=0,\quad Ls=-2\gamma s-2\eta t,\quad Lt=2\eta s-2\gamma t,\quad L(st)=-4\gamma st.
\]
The distribution is invariant under simultaneous rotation of position and orientation by \(90^\circ\). Consequently the stationary means, all cubic moments, and \(\mathbb E[UV]\) vanish, while \(\mathbb E[U^2]=\mathbb E[V^2]\). The latter is
\[
\mathbb E[U^2]=\frac{c^2A}{2\mu Q}+\frac D\mu,
\]
which depends on \(a,b\) only through \(\Gamma\) and \(\Delta^2\). This proves that degrees at most three do not reveal the sign of \(\Delta\).

**2. Signed fourth moment.** Temporarily take \(D=0\), put \(z=U+iV\), \(h=s+it\), and let \(\bar h=s-it\). Then \(\dot z=-\mu z+wh\), \(Lh=(-2\gamma+2i\eta)h\), \(L\bar h=(-2\gamma-2i\eta)\bar h\), \(L(h^2)=-4\gamma h^2\), \(h\bar h=2\), and \(h^3=-2\bar h\). Stationarity of four successive polynomial observables gives
\[
\begin{aligned}
\mathbb E[z\bar h]&=\frac{2w}{\mu+2\gamma+2i\eta},\\
\mathbb E[z^2h^2]&=-\frac{4w^2}{(\mu+2\gamma)(\mu+2\gamma+2i\eta)},\\
\mathbb E[z^3h]&=\frac{3w\,\mathbb E[z^2h^2]}{3\mu+2\gamma-2i\eta},\\
\mathbb E[z^4]&=\frac{w\,\mathbb E[z^3h]}{\mu}.
\end{aligned}
\]
The complex fourth moment therefore equals
\[
-\frac{12w^4}{\mu(\mu+2\gamma)(\mu+2\gamma+2i\eta)(3\mu+2\gamma-2i\eta)}.
\]
Quarter-turn symmetry implies \(\mathbb E[UV^3]=-\mathbb E[U^3V]\), hence \(\operatorname{Im}\mathbb E[z^4]=8\mathbb E[U^3V]\). Taking the imaginary part and replacing \(w,\gamma,\eta\) by the physical parameters proves the first boxed formula.

**3. Squared-position dependence.** For real monomial degree indices \(i,j\ge0\), denote \(m_{ij;h}=\mathbb E[U^iV^jh]\) with \(h\in\{1,s,t,st\}\). At \(D=0\), the generator identity is
\[
(i+j)\mu m_{ij;h}-m_{ij;Lh}
=i w m_{i-1,j;sh}+j w m_{i,j-1;th},
\]
where \(m_{ij;Lh}\) denotes the linear combination prescribed by \(Lh\), and terms with zero coefficients are omitted. Start with \(m_{00;1}=1\) and \(m_{00;s}=m_{00;t}=m_{00;st}=0\). At each positive degree the four-by-four system is invertible: the eigenvalues of \(L\) are \(0,-4\gamma,-2\gamma\pm2i\eta\), with strictly negative real part except for the constant. Solving degrees one through four and simplifying yields
\[
\mathbb E[U^2V^2]-\mathbb E[U^2]\mathbb E[V^2]
=\frac{c^4\Delta^2(\Delta^2+5\Gamma^2+14\mu\Gamma+9\mu^2)}{4\mu A Q^2R}.
\]
All factors are positive except the explicit square \(\Delta^2\), establishing the exact vanishing criterion. The recurrence and an independent standard-library numerical implementation are supplied in `check.py`.

**4. Thermal-noise robustness and factorization.** The full stationary coordinate pair has the distribution \((U_0+G_1,V_0+G_2)\), where the subscript-zero process is the active \(D=0\) system, and \(G_1,G_2\) are mutually independent centered Gaussians with variance \(D/\mu\), independent of the active process. Since \(\mathbb E[U_0V_0]=0\), direct expansion shows that both \(\mathbb E[U^3V]\) and \(\operatorname{Cov}(U^2,V^2)\) are unchanged. If \(a=b\), the sign coordinates independently flip at rate \(a\), so their independent linear filters and independent thermal noises yield a product stationary law. Conversely, if \(a\ne b\), the nonzero fourth mixed moment precludes independence because each marginal has zero first and third moments. This proves the if-and-only-if assertion.

## Verification
Run `python3 check.py` in the package directory. The program uses only Python standard-library arithmetic, assembles the four-by-four generator equations degree by degree, and numerically compares their solutions with the claimed rational formulas over multiple positive trap strengths, speeds, clockwise and counterclockwise rates, and thermal diffusion values. It also checks symmetry and strict-sign cases. It reports `PASS 1024 independent deterministic moment checks` on successful completion. These are finite numerical diagnostics; they do not replace the generator proof or establish literature priority.

## Relationship to prior work
Smith, Le Doussal, Majumdar and Schehr [1] derive the full product stationary law for *equal* clockwise and counterclockwise quarter-turn rates, including thermal diffusion. The present theorem identifies the exact failure boundary and fourth-order signature under an unequal-rate deformation. Mallikarjun and Pal [2] study unequal turning rates and fourth positional moments of a **free** four-state chiral walker, not the stationary confined law or its rotated-coordinate factorization. Loewe, Kozhukhov and Shendruk [3] investigate right-angle tumbling dynamics and anisotropic free transport. Olsen and Löwen [4] analyze general chiral reorientations and free diffusion. Sun, Ye and Podgornik [5] derive general moment recurrences for finite-duration tumbling with independently re-sampled run directions, a different orientation-memory mechanism from the present correlated quarter-turn chain. The underlying Markov and harmonic-filter techniques are standard; no claim of novelty is made for those tools individually.

## Limitations
The phase boundary assumes homogeneous, position-independent turning rates, cardinal orientations, a common isotropic harmonic relaxation rate, and independent isotropic Gaussian translational noise. It does not classify nonlinear traps, directed velocities other than the four cardinal directions, or arbitrary orientation-memory laws. No finite-data estimator accuracy, noise robustness in relative signal-to-noise, or empirical validation is established. Although the derived moments follow from finite-dimensional linear equations, unindexed earlier derivations could affect publication priority.

## References
[1] N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (first publicly submitted July 21, 2022), https://arxiv.org/abs/2207.10445.

[2] R. Mallikarjun, A. Pal, *Chiral run-and-tumble walker: transport and optimizing search*, arXiv:2209.05912 (September 13, 2022), https://arxiv.org/abs/2209.05912.

[3] B. Loewe, T. Kozhukhov, T. N. Shendruk, *Anisotropic run-and-tumble-turn dynamics*, Soft Matter 20 (2024), 1133--1150; first preprint arXiv:2305.03663 (May 5, 2023), https://arxiv.org/abs/2305.03663.

[4] K. S. Olsen, H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326 (May 23, 2024), https://arxiv.org/abs/2405.14326.

[5] A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578 (September 1, 2024), https://arxiv.org/abs/2409.00578.
