# Two unequal stationary gap edges in a two-particle active Dyson gas

## Finding
Consider two ordered, harmonically confined, logarithmically repelling run-and-tumble particles with independent symmetric orientation switches. Their stationary separation has two different algebraic endpoint laws, and consequently two different critical orientation-flip rates. For the constants and notation defined below, there are strictly positive finite constants \(C_a,C_b\) such that
\[
\Pr(a<G<a+\varepsilon)=C_a\varepsilon^{\alpha_a}(1+O(\varepsilon)),\qquad
\Pr(b-\varepsilon<G<b)=C_b\varepsilon^{\alpha_b}(1+O(\varepsilon)),
\]
where
\[
\alpha_a=\frac{2\gamma a}{\lambda(a+b)},\qquad
\alpha_b=\frac{2\gamma b}{\lambda(a+b)},\qquad 0<\alpha_a<\alpha_b.
\]
The stationary separation density \(p_G\) satisfies
\[
p_G(a+\varepsilon)=C_a\alpha_a\varepsilon^{\alpha_a-1}(1+O(\varepsilon)),\qquad
p_G(b-\varepsilon)=C_b\alpha_b\varepsilon^{\alpha_b-1}(1+O(\varepsilon)).
\]
Define
\[
\gamma_{\mathrm{outer}}=\frac{\lambda K}{K+v},\qquad
\gamma_{\mathrm{inner}}=\frac{\lambda K}{K-v}.
\]
They satisfy \(0<\gamma_{\mathrm{outer}}<\gamma_{\mathrm{inner}}\). When \(0<\gamma<\gamma_{\mathrm{outer}}\), the density diverges at both endpoints; when \(\gamma_{\mathrm{outer}}<\gamma<\gamma_{\mathrm{inner}}\), it diverges at the smaller gap but vanishes at the larger gap; when \(\gamma>\gamma_{\mathrm{inner}}\), it vanishes at both endpoints. At each critical rate the associated endpoint density converges to a strictly positive finite constant. A regime where the small-gap density vanishes but the large-gap density diverges is impossible. The exact sum and difference identities are
\[
\alpha_a+\alpha_b=\frac{2\gamma}{\lambda},\qquad
\alpha_b-\alpha_a=\frac{2\gamma v}{\lambda K}.
\]

## Assumptions and scope
Fix arbitrary \(\lambda,g,v,\gamma>0\). The particles have positions \(x_1(t)<x_2(t)\) and obey the piecewise-deterministic equations
\[
\dot x_1=-\lambda x_1+\frac{g}{x_1-x_2}+v\sigma_1(t),\qquad
\dot x_2=-\lambda x_2+\frac{g}{x_2-x_1}+v\sigma_2(t).
\]
Each \(\sigma_i\) independently changes sign at rate \(\gamma\); there is no thermal diffusion, external time dependence, or orientation-dependent interaction. This is the two-particle specialization of the all-orientation-interacting active Dyson model (model II). Define the gap \(G=x_2-x_1>0\) and the three-valued orientation difference \(S=(\sigma_2-\sigma_1)/2\in\{-1,0,1\}\). Then
\[
\dot G=F_S(G),\quad F_s(x)=-\lambda x+\frac{2g}{x}+2vs,
\]
with mode transition rates \(-1\to0\) and \(+1\to0\) each \(2\gamma\), and \(0\to\pm1\) each \(\gamma\). Put
\[
K=\sqrt{v^2+2\lambda g},\quad a=(K-v)/\lambda,\quad b=(K+v)/\lambda.
\]
Every formula concerns the unique stationary law of this autonomous gap-and-mode process. Its gap support is exactly \([a,b]\), with \(0<a<b\). All asymptotics are for positive \(\varepsilon\downarrow0\) with the physical parameters fixed. The \(O(\varepsilon)\) remainders may depend on those fixed parameters and are not asserted uniform near zero interaction, zero propulsion, or a vanishing flip rate.

## Proof
**1. Contractive stationary dynamics and support.** For each mode, \(F_s'(x)=-\lambda-2g/x^2<-\lambda\) on \((0,\infty)\). Positive initial gaps remain positive because the force diverges repulsively near zero. Two gaps driven by the same orientation path satisfy \(|G_t-\widehat G_t|\le e^{-\lambda t}|G_0-\widehat G_0|\). Coupling the finite-state irreducible orientation chain in the remote past and then using this contraction gives a unique joint invariant law. The extremal vector fields are
\[
F_-(x)=-\lambda\frac{(x-a)(x+b)}{x},\qquad
F_+(x)=\lambda\frac{(b-x)(x+a)}{x},
\]
so scalar comparison confines its gap marginal to \([a,b]\). Persistent runs of either extremal mode have positive probability and approach the associated equilibrium arbitrarily closely; hence both endpoints belong to the support, as does every intervening open subinterval. No atom occurs at either endpoint because a finite run cannot reach the attracting equilibrium from a different starting point. Conditioning on the continuously distributed holding time following the last mode switch gives densities \(p_-(x),p_0(x),p_+(x)\) in the open interval, with no stationary atoms; the switching rates are independent of position. Their local regularity is sufficient for the distributional stationary transport equations below (and gives continuous representatives away from the interior zero of \(F_0\)).

**2. Conservation equations and boundary fluxes.** In the stationary law, the three coupled one-dimensional forward equations are
\[
(F_-p_-)'=\gamma p_0-2\gamma p_-,\quad
(F_0p_0)'=2\gamma(p_-+p_+)-2\gamma p_0,\quad
(F_+p_+)'=\gamma p_0-2\gamma p_+.
\]
All three probability currents vanish at each support boundary. One way to see this without presupposing density behavior is to integrate the weak equations over shrinking endpoint strips: the switching source terms have vanishing integrals, no exterior stationary probability exists, and the flow does not transport mass through either boundary. Write \(H_s(x)=\int_a^x p_s(u)\,du\). Integrating from \(a\) to \(x\) gives
\[
F_-p_-=\gamma H_0-2\gamma H_-,\quad
F_0p_0=2\gamma(H_-+H_+-H_0),\quad
F_+p_+=\gamma(H_0-2H_+).
\]

**3. Sharp small-gap asymptotic.** Let \(x=a+\varepsilon\). Both \(F_0\) and \(F_+\) are uniformly positive for small \(\varepsilon\), while
\[
F_-(a+\varepsilon)=-h_a\varepsilon+O(\varepsilon^2),\qquad
h_a=\lambda+\frac{2g}{a^2}=\lambda\frac{a+b}{a}.
\]
The integrated flux equations imply the pointwise inequalities \(p_0(x)\le C(H_-(x)+H_+(x))\) and \(p_+(x)\le C H_0(x)\) near \(a\). Integrating these inequalities, then absorbing the small terms, yields
\[
H_0(a+\varepsilon)=O(\varepsilon H_-(a+\varepsilon)),\qquad
H_+(a+\varepsilon)=O(\varepsilon^2H_-(a+\varepsilon)).
\]
The denominator \(H_-\) is strictly positive for every \(\varepsilon>0\): the stationary orientation chain visits state \(-1\) with positive probability and sufficiently long such runs move the gap into any prescribed neighborhood of \(a\). The first flux relation therefore gives
\[
\frac{d}{d\varepsilon}\log H_-(a+\varepsilon)
=\frac{2\gamma-\gamma H_0/H_-}{-F_-(a+\varepsilon)}
=\frac{2\gamma}{h_a\varepsilon}+O(1).
\]
Integrating the bounded remainder establishes \(H_-(a+\varepsilon)=C_a\varepsilon^{2\gamma/h_a}(1+O(\varepsilon))\) for a constant \(0<C_a<\infty\). Adding the two negligible mode masses gives the left endpoint CDF. Differentiating through the displayed flux identities, rather than differentiating the \(O\)-estimate, yields the density asymptotic and its controlled relative remainder.

**4. Sharp large-gap asymptotic.** Apply exactly the same argument to \(T_s(x)=\int_x^b p_s(u)\,du\) at \(x=b-\varepsilon\). Now \(F_-\) and \(F_0\) are uniformly negative, and
\[
F_+(b-\varepsilon)=h_b\varepsilon+O(\varepsilon^2),\qquad
h_b=\lambda+\frac{2g}{b^2}=\lambda\frac{a+b}{b}.
\]
The negative/zero mode contributions satisfy \(T_0=O(\varepsilon T_+)\) and \(T_-=O(\varepsilon^2T_+)\); the positive-mode current gives
\[
\frac{d}{d\varepsilon}\log T_+(b-\varepsilon)
=\frac{2\gamma}{h_b\varepsilon}+O(1).
\]
This proves the right endpoint CDF and density with a second strictly positive finite coefficient \(C_b\).

**5. Distinct phase thresholds.** Since \(b>a\), we have \(h_a>h_b>0\), hence \(\alpha_a<\alpha_b\). The endpoint density diverges when its exponent is less than one, has a positive finite limit when equal to one, and vanishes when greater than one. Substitution of the exact roots yields \(h_b/2=\lambda K/(K+v)\) and \(h_a/2=\lambda K/(K-v)\). Addition and subtraction give the claimed exponent identities and the exhaustive phase classification.

## Verification
A standalone reproducibility program `verify_gap_edges.py` builds a finite-volume upwind discretization of the full three-mode stationary transport generator. For each mode, fluxes through all cell faces generate nearest-neighbor transitions; mode-switch transitions use the exact rates above. It solves the normalized stationary nullvector with sparse linear algebra and checks the stationary mode masses \(1/4,1/2,1/4\). For \(\lambda=g=v=1\), across \(\gamma\in\{0.35,0.8,1,2.8\}\) and 5000 nonuniform cells, estimated small- and large-gap CDF log-slopes were respectively approximately \((0.1521,0.5543)\), \((0.3462,1.2605)\), \((0.4320,1.5724)\), and \((1.1965,4.3326)\). Their exact predictions are respectively \((0.1479,0.5521)\), \((0.3381,1.2619)\), \((0.4226,1.5774)\), and \((1.1834,4.4166)\). The observed finite-grid differences are consistent with first-order upwind numerical bias and finite fitting intervals; they do not establish the infinite-resolution asymptotics. Run with `python verify_gap_edges.py` with NumPy and SciPy. The proof is analytic and does not rely on these tests.

## Relationship to prior work
Touzo, Le Doussal and Schehr (2023, arXiv:2302.02937) introduced both active Dyson models and analyzed stationary finite-support **single-particle** densities, including finite-particle singular behavior; their two-particle configuration bounds are prior results. This note instead analyzes the **inter-particle separation marginal**, resolves both endpoint powers, and determines the two different flip-rate thresholds. Le Doussal, Majumdar and Schehr (2021, arXiv:2105.11838) derived generic two-particle stationary transport equations, discussed repulsive interactions and a force with reciprocal plus linear terms, and established support mechanisms. The integrated-flux analysis here is compatible with that general framework and claims no novelty for the general equations or existence of stationary confinement. Its stated distinct edge exponents and complete sign-phase diagram were not located explicitly there. Basu and collaborators (2019, arXiv:1910.10083) solved the *linear-force* three-state telegraph trap and its edge transitions; the present reciprocal-force nonlinear gap has different slopes at the two edges. Das, Dhar and Kundu (2019, arXiv:1912.13269) considered a different two-particle gap model with hard-core interactions and thermal noise on a ring. The gap-edge statement is a specialization of general piecewise-deterministic boundary-scaling principles; priority should be assessed in that broader literature as well.

## Limitations
The theorem applies only to exactly two particles with logarithmic repulsion, quadratic confinement, deterministic motion between independent Poisson tumbles, and fixed positive physical parameters. It gives sharp edge powers and signs but not closed forms for the positive amplitudes \(C_a,C_b\) or the complete interior density. It does not apply directly to finite-temperature diffusion, particles that exchange order, orientation-correlated flips, or many-particle gap distributions. No independent audit or definitive publication-priority certification is claimed. Generic PDMP boundary exponents or a previously unrecognized specialization of the 2021 general stationary ODE could imply the same classification; these remain scientific priority risks.

## References
1. L. Touzo, P. Le Doussal, G. Schehr, “Interacting, running and tumbling: the active Dyson Brownian motion,” arXiv:2302.02937v1 (first public 2023-02-06), https://arxiv.org/abs/2302.02937.
2. P. Le Doussal, S. N. Majumdar, G. Schehr, “Stationary nonequilibrium bound state of a pair of run and tumble particles,” arXiv:2105.11838v1 (2021-05-25), https://arxiv.org/abs/2105.11838.
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, “Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap,” arXiv:1910.10083v1 (2019-10-22), https://arxiv.org/abs/1910.10083.
4. A. Das, A. Dhar, A. Kundu, “Gap statistics of two interacting run and tumble particles in one dimension,” arXiv:1912.13269v1 (2019-12-31), https://arxiv.org/abs/1912.13269.
5. L. Touzo, P. Le Doussal, G. Schehr, “Fluctuations in the active Dyson Brownian motion and the overdamped Calogero-Moser model,” arXiv:2307.14306v1 (2023-07-26), https://arxiv.org/abs/2307.14306.
