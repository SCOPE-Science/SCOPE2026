# Rigorous uniqueness and universal mode splitting at the trapped run-and-tumble thermal transition

## Finding
For the one-dimensional, symmetric, harmonically trapped run-and-tumble model defined below, the previously identified curvature-zero thermal boundary is a **globally unique, strictly decreasing analytic curve**, with **exactly two modes on its low-noise side and exactly one mode on and above it**. If \(m_\ell(t)>0\) denotes the right-hand modal position in units of the active trapping length, then the new local quantitative classification is
\[
 m_\ell(t)^2=3\bigl(t_c(\ell)-t\bigr)+O_\ell\!\left(\bigl(t_c(\ell)-t\bigr)^2\right),\qquad t\uparrow t_c(\ell),
\]
with an **exact coefficient of three independent of persistence**. The implicit curvature-zero equation itself, the existence of a qualitative transition and its endpoint asymptotics are prior results, not new assertions here.

For every \(0<\ell<1\), there is one \(t_c(\ell)>0\); it satisfies \(t_c'(\ell)<0\), \(\lim_{\ell\downarrow0}t_c(\ell)=1\) and \(\lim_{\ell\uparrow1}t_c(\ell)=0\). For \(\ell\ge1\), the density is strictly unimodal at every positive noise strength.

## Assumptions and scope
Let \(v,k,D,\gamma>0\). Consider the unique stationary position law of
\[
 dX_s=(-kX_s+v\sigma_s)\,ds+\sqrt{2D}\,dW_s,
\]
where \(\sigma_s\in\{-1,+1\}\) flips sign at rate \(\gamma\), independently of standard Brownian motion \(W\). Define the active length \(L=v/k\), dimensionless persistence parameter \(\ell=\gamma/k\), and dimensionless thermal variance \(t=Dk/v^2\). The dimensionless stationary position \(Z=X/L\) has density
\[
 f_{\ell,t}(x)=\int_{-1}^{1}\frac{\Gamma(\ell+1/2)}{\sqrt\pi\Gamma(\ell)}(1-y^2)^{\ell-1}\frac{e^{-(x-y)^2/(2t)}}{\sqrt{2\pi t}}\,dy.
\]
This convolution is known in the prior literature. The present result concerns the complete **number and locations of modes**, **uniqueness and monotonicity of the transition curve**, and **its near-critical mode displacement**; it does not assert novelty of the density formula or the previously derived critical-temperature integral.

For \(U\in(0,1)\) let
\[
 A_\ell(\beta)=\int_0^1u^{-1/2}(1-u)^{\ell-1}e^{-\beta u}\,du,\quad
 m_\ell(\beta)=-\frac{A_\ell'(\beta)}{A_\ell(\beta)},\quad h_\ell(\beta)=2\beta m_\ell(\beta).
\]
The previously established curvature-zero condition becomes \(h_\ell(\beta_c)=1\) with \(\beta_c=1/(2t_c)\). Its explicit equivalent is
\[
 \frac{2\beta_c}{2\ell+1}\frac{{}_1F_1(3/2;\ell+3/2;-\beta_c)}{{}_1F_1(1/2;\ell+1/2;-\beta_c)}=1.
\]

## Proof
**1. Stationary law and curvature.** The sum of the stationary two-orientation master equations gives zero position current. Eliminating the orientation difference gives, in the athermal case, the symmetric density proportional to \((1-y^2)^{\ell-1}\) on \((-1,1)\). The independent thermal forcing produces a stationary Ornstein–Uhlenbeck component with variance \(D/k\), giving the displayed convolution. Equivalently, \(Z=Y+\sqrt t\,G\) with \(G\) standard Gaussian and \(Y\) symmetric with the displayed beta density. Differentiation inside the integral yields
\[
 f_{\ell,t}''(0)=\frac{f_{\ell,t}(0)}{t}\bigl(h_\ell(1/(2t))-1\bigr).
\]
This recovers the **previously known** implicit curvature boundary and is used here as an input for new global deductions.

**2. A unique transverse crossing.** The Kummer equation for \(A_\ell(\beta)=B(1/2,\ell){}_1F_1(1/2;\ell+1/2;-\beta)\) is
\[
 \beta A_\ell''+(\beta+\ell+1/2)A_\ell'+A_\ell/2=0.
\]
Consequently \(m=m_\ell\) satisfies \(m'=m^2-[1+(\ell+1/2)/\beta]m+1/(2\beta)\). Substituting \(m=1/(2\beta)\) at **any** root of \(h_\ell=1\) gives the exact transversal derivative
\[
 h_\ell'(\beta)\big|_{h_\ell(\beta)=1}=\frac{1-\ell}{\beta}.
\]
For \(0<\ell<1\), \(h_\ell(\beta)\to0\) as \(\beta\downarrow0\), while Laplace expansion near \(u=0\) gives \(h_\ell(\beta)=1+(1-\ell)/\beta+O_\ell(\beta^{-2})\) as \(\beta\to\infty\). Existence follows by continuity. Every crossing is strictly upward, hence two distinct crossings are impossible: between two upward crossings would be a downward crossing. The implicit function theorem gives analyticity of the unique \(\beta_c(\ell)\).

Write \(\pi_{\ell,\beta}\) for the probability density proportional to \(u^{-1/2}(1-u)^{\ell-1}e^{-\beta u}\) on \((0,1)\). Differentiation under the integral gives \(\partial_\ell m=\operatorname{Cov}_{\pi_{\ell,\beta}}(U,\log(1-U))<0\). Differentiating the implicit equation and using the positive transversal derivative yields the exact slope identity
\[
 t_c'(\ell)=\frac{\operatorname{Cov}_{\pi_{\ell,\beta_c(\ell)}}(U,\log(1-U))}{1-\ell}<0.
\]
As \(\ell\downarrow0\), the unweighted beta law tends to the point mass at \(U=1\), making \(h\to2\beta\) on compact positive intervals; thus \(t_c\to1\). At \(\ell=1\), direct integration by parts gives \(h_1(\beta)=1-2e^{-\beta}/A_1(\beta)<1\) for every finite \(\beta\); this forces \(\beta_c(\ell)\to\infty\), hence \(t_c\to0\), as \(\ell\uparrow1\).

**3. No hidden additional modes.** We supply the finite-sign-change argument rather than inferring global modal structure from central curvature alone. For any finite signed measure on a compact interval with at most \(q\) alternating sign blocks, its bilateral Laplace transform has at most \(q-1\) real zeros counted with multiplicity. To prove this, induct on \(q\). When \(q=1\), the transform has fixed sign. Otherwise choose a boundary \(c\) between two consecutive sign blocks. Multiplying the transform by \(e^{-cx}\) does not change its zeros; differentiation corresponds to multiplying the signed measure by \(y-c\), eliminating at least one sign change. Rolle's theorem with multiplicities completes the induction.

For \(0<\ell<1\), truncate the athermal density to \([-b,b]\), \(b<1\), and normalize. Its distributional derivative consists of a positive left-endpoint atom, a negative density on \((-b,0)\), a positive density on \((0,b)\), and a negative right-endpoint atom: four alternating sign blocks. Convolution with a Gaussian converts its derivative into a positive Gaussian factor times a bilateral Laplace transform of a signed measure with those four blocks. Thus the smoothed derivative has at most three sign changes. As \(b\uparrow1\), the truncated densities converge in \(L^1\), and their smoothed derivatives converge uniformly on compact intervals; four alternating signs in the limiting derivative would contradict the approximating bound. The true \(f'_{\ell,t}\) therefore has at most three sign changes on the whole real line. It is odd, and \(f'_{\ell,t}(x)<0\) for \(x>1\).

If \(t<t_c\), the curvature at zero is positive: \(f'\) is positive just right of zero and negative past one. By symmetry and the three-sign-change bound, there is exactly one positive-to-negative transition on the positive half-line and its negative mirror, so the density has exactly two symmetric maxima and a strict central minimum. If \(t>t_c\), the central curvature is negative; an off-center positive derivative excursion would force at least five sign changes. Hence the center is the unique mode. At \(t=t_c\), the next step proves strict negative fourth derivative, so the same argument applies. For \(\ell\ge1\), the original beta density is symmetric unimodal, and its convolution with a nondegenerate Gaussian is strictly unimodal (also directly from log-concavity for \(\ell>1\), and by an explicit Gaussian-difference derivative at \(\ell=1\)).

**4. Universal modal splitting.** The Gaussian smoothing family satisfies the heat equation \(\partial_t f_{\ell,t}=\tfrac12\partial_x^2f_{\ell,t}\). At \(t=t_c\), the crossing identity of step 2 gives
\[
 \partial_t f_{\ell,t}''(0)\big|_{t_c}=-\frac{(1-\ell)f_{\ell,t_c}(0)}{t_c^2},\qquad
 f_{\ell,t_c}^{(4)}(0)=-\frac{2(1-\ell)f_{\ell,t_c}(0)}{t_c^2}<0.
\]
The function \(G(t,s)=f_{\ell,t}'(\sqrt{s})/\sqrt{s}\), analytically continued at \(s=0\), satisfies \(G(t_c,0)=0\), \(\partial_sG(t_c,0)=f^{(4)}_{\ell,t_c}(0)/6\ne0\), and \(\partial_tG(t_c,0)=f^{(4)}_{\ell,t_c}(0)/2\). The implicit function theorem therefore gives a unique small positive modal root with \(d(m_\ell^2)/dt=-3\) at the transition. Analyticity supplies \(m_\ell(t)^2=3(t_c-t)+O_\ell((t_c-t)^2)\). Global uniqueness in step 3 identifies this root with the actual positive mode.

## Verification
Run `python verify.py` with Python 3.10+, NumPy, SciPy and SymPy. It checks the Riccati transversal identity symbolically, computes independent hypergeometric transition roots, checks the exact critical fourth-derivative identity through Gaussian--Jacobi integration, verifies modal signs and confirms convergence of the squared mode displacement divided by the thermal variance deficit to three. The verifier prints **170 passed deterministic assertions**. These finite numerical tests support but do not prove the all-parameter theorem, whose proof is above.

Representative \((\ell,t_c)\) pairs are \((0.25,0.53856358179)\), \((0.5,0.31646434035)\), and \((0.75,0.18327381606)\).

## Relationship to prior work
Guéneau, Majumdar and Schehr (2026), Section V.A.1, equations (95)–(97) in the accessible revision, already derive the **same implicit critical-temperature equation**, plot the phase diagram, describe the modality transition and give endpoint asymptotics. Sabhapandit and Majumdar (2024), Section 4.1.1, equations (94)–(96), supply an equivalent telegraph-driven-trap-center density, a hypergeometric curvature criterion and a numerical phase diagram. Sevilla and Meléndez Mora (2026), Section III, provide the thermal/athermal convolution and qualitative profiles. These are not priority claims here.

The assessed new result is the rigorous global **one-crossing/no-reentrance theorem**, its exact **negative slope/covariance identity**, the **global at-most-two-mode classification** without assuming center curvature controls all peaks, and the **universal coefficient three in near-critical squared modal displacement**. These are not explicitly established in the materially inspected sections of those primary works. Established general variation-diminishing/heat-flow principles are proof tools, not claimed discoveries. A broader preexisting modality theorem might subsume some of these refinements; this is a residual originality risk, not a claim of priority certification.

## Limitations
The proof applies only to a symmetric two-velocity process, constant orientation-flip rate, harmonic confinement, independent additive Gaussian thermal noise, and the unique stationary one-particle marginal. It does not address asymmetric switching, nonlinear traps, time-dependent transient modes or interacting particles. The asymptotic expansion holds for each fixed \(0<\ell<1\), not uniformly as \(\ell\to0\) or \(\ell\to1\). The earlier physical phase boundary and its implicit equation must not be attributed to this result. No independent mathematical or literature audit has been performed.

## References
1. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first public 2026-02-09), especially Section V.A.1 of the revised PDF. https://arxiv.org/abs/2602.08436
2. S. Sabhapandit, S. N. Majumdar, *Noninteracting particles in a harmonic trap with a stochastically driven center*, arXiv:2404.02480 (first public 2024-04-03), Section 4.1.1. https://arxiv.org/abs/2404.02480
3. F. J. Sevilla, J. A. Meléndez Mora, *Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach*, arXiv:2608.21781 (first public 2026-08-22), Section III. https://arxiv.org/abs/2608.21781
4. R. Garcia-Millan, G. Pruessner, *Run-and-tumble motion: field theory and entropy production*, arXiv:2012.02900 (2020), especially stationary distribution in Appendix G. https://arxiv.org/abs/2012.02900
