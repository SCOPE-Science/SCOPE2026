# Universal transient entanglement and exact stationary decorrelation in a resonantly driven Gaussian quantum battery

## Finding
For every charger damping rate \(\gamma>0\), intermode hopping \(g>0\), and nonzero parametric drive \(0<\Omega<\gamma/2\), a resonant quadratic bosonic charger–holder battery started in its joint vacuum develops entanglement immediately after the drive is switched on, but becomes separable after a finite time and stays separable forever thereafter. More precisely, if \(E_{\mathrm N}(t)\) denotes natural-logarithm Gaussian logarithmic negativity, then
\[
E_{\mathrm N}(t)=g\Omega t^2+O(t^3)\quad (t\downarrow0),
\]
and there exists a finite \(T=T(g,\gamma,\Omega)\) such that \(E_{\mathrm N}(t)=0\) for every \(t\ge T\). The unique stationary Gaussian state is exactly a product of two opposite-quadrature squeezed thermal states, with zero cross correlations and zero mutual information, even though the holder has strictly positive stationary energy.

## Assumptions and scope
Let \(c,h\) be independent canonical bosonic annihilation operators and fix a rotating frame with exactly zero charger–holder and drive detunings. The Hamiltonian and vacuum-bath Lindblad generator are
\[
H=g(c^\dagger h+h^\dagger c)+\frac{i\Omega}{2}(c^{\dagger 2}-c^2),\qquad
\mathcal L(\rho)=-i[H,\rho]+\gamma\left(c\rho c^\dagger-\frac12\{c^\dagger c,\rho\}\right).
\]
A pump phase of \(\pi/2\) is a conventional quadrature choice; local phase rotations handle other fixed pump phases. Units satisfy \(\hbar=1\). The initial state is \(\rho(0)=|0,0\rangle\langle0,0|\), although stationary convergence below applies to any finite-second-moment initial Gaussian state.

Use \(d=\gamma/2\), \(R=(q_c,p_c,q_h,p_h)^\top\), \(q_a=(a+a^\dagger)/\sqrt2\), \(p_a=(a-a^\dagger)/(i\sqrt2)\). Covariances are \(V_{ij}=\langle\{R_i-\langle R_i\rangle,R_j-\langle R_j\rangle\}\rangle/2\), with vacuum covariance \(I_4/2\). The driving constraint \(0<\Omega<d\) and \(g>0\) is essential to the exponentially attractive finite stationary Gaussian state.

## Proof
**1. Exact Gaussian drift.** The Hamiltonian and vacuum-loss generator preserve Gaussianity, and the mean stays zero for the vacuum input. The covariance solves the constant Lyapunov differential equation
\[
\dot V=AV+VA^\top+D,\quad V(0)=I_4/2,
\]
where
\[
A=\begin{pmatrix}
\Omega-d&0&0&g\\
0&-\Omega-d&-g&0\\
0&g&0&0\\
-g&0&0&0
\end{pmatrix},\qquad D=\operatorname{diag}(d,d,0,0).
\]
Permuting coordinates into the \((q_c,p_h)\) and \((p_c,q_h)\) pairs gives independent drift blocks whose characteristic polynomials are
\[
\lambda^2+(d-\Omega)\lambda+g^2
\quad\text{and}\quad
\lambda^2+(d+\Omega)\lambda+g^2.
\]
Both polynomials are Hurwitz under the assumptions, so \(e^{At}\to0\) exponentially and the stationary covariance is unique.

**2. Exact stationary factorization.** Set \(v_+=d/[2(d-\Omega)]\) and \(v_-=d/[2(d+\Omega)]\). Direct substitution in the Lyapunov equation gives
\[
\boxed{V_\infty=\operatorname{diag}(v_+,v_-,v_-,v_+).}
\]
Indeed, the off-diagonal drift terms cancel pairwise because \((V_\infty)_{11}=(V_\infty)_{44}\) and \((V_\infty)_{22}=(V_\infty)_{33}\); the two damped diagonal equations reduce to \(2(\Omega-d)v_++d=0\) and \(-2(\Omega+d)v_-+d=0\). By Hurwitz uniqueness, this is the stationary covariance for every \(g>0\). Its cross block vanishes, so the zero-mean Gaussian stationary state is the product of the two one-mode Gaussian marginals. Their symplectic eigenvalues both equal
\[
\nu_\infty=\sqrt{v_+v_-}=\frac{d}{2\sqrt{d^2-\Omega^2}}>\frac12,
\]
which are mixed squeezed thermal states with opposite squeezing axes. Product structure proves vanishing mutual information and all bipartite entanglement. The holder occupation is \(\langle h^\dagger h\rangle_\infty=(v_++v_- -1)/2=\Omega^2/[2(d^2-\Omega^2)]>0\); this occupation is consistent with the previously published stationary energy formula, and is not an independently claimed discovery.

**3. Entanglement appears at quadratic order.** The exact evolution is
\[
V(t)=V_\infty+e^{At}(I_4/2-V_\infty)e^{A^\top t}.
\]
Taylor expansion directly from the differential equation yields
\[
V(t)=\frac{I_4}{2}+t\operatorname{diag}(\Omega,-\Omega,0,0)+t^2
\begin{pmatrix}
\Omega(\Omega-d)&0&0&-g\Omega/2\\
0&\Omega(\Omega+d)&-g\Omega/2&0\\
0&-g\Omega/2&0&0\\
-g\Omega/2&0&0&0
\end{pmatrix}+O(t^3).
\]
Write this covariance in charger and holder blocks \(V(t)=\begin{psmallmatrix}V_c&C\\C^\top&V_h\end{psmallmatrix}\). The displayed series implies \(\det V_c=1/4+O(t^3)\), \(V_h=I_2/2+O(t^3)\), and \(C=-(g\Omega/2)t^2\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}+O(t^3)\). A local one-mode symplectic squeeze \(S_c(t)=\operatorname{diag}((V_{c,22}/V_{c,11})^{1/4},(V_{c,11}/V_{c,22})^{1/4})\), which is \(I_2+O(t)\), therefore brings \(V_c\) to \(I_2/2+O(t^3)\) without changing \(C\)'s quadratic leading term. Local symplectic transformations preserve entanglement. The two-mode Gaussian partial-transpose symplectic spectrum now gives
\[
\widetilde\nu_-(t)=\frac12-\frac{g\Omega}{2}t^2+O(t^3).
\]
To see the coefficient explicitly, the leading locally transformed covariance has local diagonal blocks \(I_2/2\) and cross block \(-\varepsilon\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), where \(\varepsilon=g\Omega t^2/2\). Its smaller partially transposed symplectic eigenvalue is \(1/2-\varepsilon\); the omitted local contributions are \(O(t^3)\). The Gaussian PPT criterion states that such a two-mode state is entangled exactly when \(\widetilde\nu_-<1/2\). Consequently, \(\widetilde\nu_-(t)<1/2\) for all sufficiently small \(t>0\) and
\[
E_{\mathrm N}(t)=\max\{0,-\log(2\widetilde\nu_-(t))\}=g\Omega t^2+O(t^3).
\]

**4. Permanent eventual separability.** The exact solution converges exponentially to \(V_\infty\). Partial transposition of a covariance reverses \(p_h\). At the product limit, both partially transposed symplectic eigenvalues equal \(\nu_\infty>1/2\). Continuity of the finite-dimensional symplectic spectrum therefore supplies a finite \(T\) after which \(\widetilde\nu_-(t)>1/2\) for all \(t\ge T\), proving separability for every such time. This establishes at least one entanglement-to-separability transition, without asserting uniqueness of the crossing or excluding intermediate revivals.

## Verification
The standalone `verify.py` implements the stated drift, exact covariance flow, Gaussian partial-transpose eigenvalues, stationary Lyapunov residual, and independent finite-dimensional Fock-space Lindblad evolution for a representative setting. Reproduction requires Python 3 with NumPy and SciPy: run `python verify.py`. All analytic steps above are independent of finite-dimensional truncation, roundoff, or the number of tested parameter samples.

## Relationship to prior work
Downing and Ukhtary, *A quantum battery with quadratic driving* (2023), introduce the quadratic charger–holder model, compute stationary holder energies, ergotropies and quadrature behavior, and study stationary negativity at the nonzero detuning \(\Delta=\gamma/2\) in their Figure 5. Those energetic formulas and the underlying covariance method are prior work. The present claim concerns the exactly resonant, vacuum-initialized transient entanglement onset, permanent eventual separability, and coupling-independent product stationary covariance; the relevant statements are not identified in the inspected main article. Simon's two-mode Gaussian partial-transpose criterion and earlier beam-splitter nonclassicality-to-entanglement studies supply established methods rather than novelty. Isar's two-mode open-Gaussian entanglement study assumes uncoupled oscillators with a different thermal environment, so its initial-separable-state preservation theorem does not cover entanglement birth under intermode hopping and an active quadratic pump. The origin article's separately hosted supplementary covariance derivations could not be comprehensively examined, leaving a specific priority risk; no noncoverage conclusion is drawn about that inaccessible text.

## Limitations
The theorem requires exact resonance, pure vacuum initial state for the immediate birth claim, strictly positive coupling and drive, strictly positive charger loss, and drive strictly below the resonant stability threshold. It does not establish a single entanglement-death crossing or a universal numerical bound on its time, apply to generic non-Gaussian initial states, or include holder loss, thermal baths, nonlinearities, frequency detuning, or time-dependent pumps. A statement about stationary energy is merely a consistency check against the 2023 primary source. No independent scientific audit has been carried out.

## References
1. C. A. Downing and M. S. Ukhtary, *A quantum battery with quadratic driving*, Communications Physics **6**, 322 (2023); arXiv:2311.02424; https://doi.org/10.1038/s42005-023-01439-y (first publicly available 2023-11-04).
2. R. Simon, *Peres-Horodecki Separability Criterion for Continuous Variable Systems*, Physical Review Letters **84**, 2726–2729 (2000); arXiv:quant-ph/9909044; https://doi.org/10.1103/PhysRevLett.84.2726.
3. W. Ge, M. E. Tasgin and M. S. Zubairy, *Conservation relation of nonclassicality and entanglement for Gaussian states in a beam splitter*, Physical Review A **92**, 052328 (2015); arXiv:1506.04937; https://doi.org/10.1103/PhysRevA.92.052328.
4. C. A. Downing and M. S. Ukhtary, *Hyperbolic enhancement of a quantum battery*, Physical Review A **109**, 052206 (2024); https://doi.org/10.1103/PhysRevA.109.052206.
5. A. Isar, *Entanglement in two-mode continuous variable open quantum systems* (2011); arXiv:1102.4495, https://arxiv.org/abs/1102.4495.
