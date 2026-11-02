# A unique frequency reversal in heuristic Michaelis–Menten substrate-noise spectra

## Finding

The stationary substrate-concentration power spectra predicted by the full linear-noise approximation (LNA) and the standard one-species heuristic stochastic quasi-steady-state approximation (hQSSA) for an *open* Michaelis–Menten enzyme network have a sharp, universal comparison. If substrate–enzyme dissociation has strictly positive rate, the heuristic spectrum is larger below exactly one positive frequency and smaller above it. If dissociation is absent, the heuristic spectrum is larger at every finite frequency. The result is an all-positive-parameter statement about these two precisely specified Gaussian LNA models, not a claim about the exact chemical master equation.

Write \(u=k_0s>0\), \(v=k_0e>0\), \(d=k_1\ge0\), \(k=k_2>0\), \(L=d+k\), \(h=u+d\), and \(a=u+d+k\). Let \(c>0\) be the steady complex concentration and \(\Omega>0\) the volume. Define

\[
B=k^2u+2kvh+kv^2\left(1-\frac{kL}{a^2}\right),\qquad
C_0=\frac{v^2k^4u}{a^2}.
\]

Both constants are strictly positive. Using the common two-sided angular-frequency PSD normalization, for every real \(\omega\),

\[
\boxed{\quad S_{\mathrm{heur}}(\omega)-S_{\mathrm{full}}(\omega)
=\frac{2c}{\Omega}\frac{-d\omega^4+B\omega^2+C_0}
{\left[(vk-\omega^2)^2+(a+v)^2\omega^2\right]
\left[\omega^2+(vk/a)^2\right]}.\quad}
\]

When \(d>0\), set

\[
\boxed{\qquad\omega_*^2=\frac{B+\sqrt{B^2+4dC_0}}{2d}.\qquad}
\]

The difference is strictly positive for \(|\omega|<\omega_*\), vanishes exactly at \(\omega=\pm\omega_*\), and is strictly negative for \(|\omega|>\omega_*\). When \(d=0\), the difference is strictly positive for every finite real \(\omega\). This dichotomy includes all strictly positive binding, catalytic and steady-state free-enzyme/substrate parameters; no asymptotic time-scale separation is assumed for the algebraic identity.

## Assumptions and scope

The reaction network is

\[
\varnothing\xrightarrow{k_{\mathrm{in}}}S,\qquad
S+E\mathrel{\mathop{\rightleftharpoons}^{k_0}_{k_1}} C,
\qquad C\xrightarrow{k_2}E+P.
\]

The total enzyme concentration \(E_T=e+c\) is conserved; \(k_0,k_2,k_{\mathrm{in}},E_T,\Omega>0\) and \(k_1\ge0\). We assume a positive deterministic stationary state with substrate \(s>0\), free enzyme \(e>0\), and complex \(c>0\), so \(k_0se=(k_1+k_2)c\) and \(k_{\mathrm{in}}=k_2c\). Equivalently, it suffices that \(0<k_{\mathrm{in}}<k_2E_T\). The product is removed from the state description after formation and does not feed back. The concentration fluctuations, in the usual system-size LNA, are modeled by their stationary Gaussian Ornstein–Uhlenbeck processes. The reduced *heuristic* model has birth reaction \(\varnothing\to S\) of rate \(k_{\mathrm{in}}\) and loss reaction \(S\to P\) with macroscopic rate \(k_2E_Ts/(K_M+s)\), \(K_M=(k_1+k_2)/k_0\). The compared observable is the *free substrate* concentration in both models, not the total substrate-plus-complex amount.

For a stationary scalar concentration fluctuation \(\delta s(t)\), the two-sided PSD is \(S(\omega)=\int_{\mathbb R}e^{-i\omega t}\operatorname{Cov}(\delta s(t),\delta s(0))\,dt\), so \(\operatorname{Var}(\delta s)=(2\pi)^{-1}\int_{\mathbb R}S(\omega)\,d\omega\). All displayed spectra share this normalization.

## Proof

**1. Drift and diffusion for the full network.** Use state order \((\delta c,\delta s)\). Deterministic mass action gives \(\dot c=k_0s(E_T-c)-(k_1+k_2)c\) and \(\dot s=k_{\mathrm{in}}-k_0s(E_T-c)+k_1c\). At the positive equilibrium, the Jacobian is

\[
J=\begin{pmatrix}-a&v\\h&-v\end{pmatrix}.
\]

The four elementary reaction channels (influx, binding, dissociation, catalysis) have respective equilibrium intensities \(kc,Lc,dc,kc\) and stoichiometric steps \((0,1),(1,-1),(-1,1),(-1,0)\) in \((c,s)\) order. Consequently their diffusion covariance for the concentration LNA is

\[
D=\frac c\Omega\begin{pmatrix}2L&-(2d+k)\\-(2d+k)&2L\end{pmatrix}.
\]

The characteristic polynomial of \(J\) is \(z^2+(a+v)z+vk\). Because its coefficients are strictly positive, both drift eigenvalues have negative real part, and the stationary LNA exists and is unique.

**2. The exact spectra.** The stationary spectral matrix is \((i\omega I-J)^{-1}D(-i\omega I-J^{\mathsf T})^{-1}\). Inverting the two-by-two matrix and taking the substrate entry gives

\[
S_{\mathrm{full}}(\omega)=\frac{2c}{\Omega}
\frac{L\omega^2+k(ha+kL)}{(vk-\omega^2)^2+(a+v)^2\omega^2}.
\]

For the heuristic model the effective propensity derivative at the same fixed point is \(vk/a\), so its one-dimensional drift is \(-vk/a\). Equilibrium input and output propensities both equal \(kc\), yielding the heuristic LNA diffusion \(2kc/\Omega\). Hence

\[
S_{\mathrm{heur}}(\omega)=\frac{2kc/\Omega}{\omega^2+(vk/a)^2}.
\]

Both denominators are strictly positive for real \(\omega\), since \(a,v,k>0\).

**3. A polynomial numerator and its sign.** Put \(x=\omega^2\). Bringing the last two rational expressions to a common denominator and expanding produces

\[
k\left[(vk-x)^2+(a+v)^2x\right]
-\left[Lx+k(ha+kL)\right]\left[x+(vk/a)^2\right]
=-dx^2+Bx+C_0.
\]

The constant satisfies \(C_0>0\). In addition, \(a^2-kL=u^2+2u(d+k)+d(d+k)>0\), so all three terms in the definition of \(B\) are nonnegative and the first two are strictly positive: \(B>0\). For \(d>0\), the polynomial \(-dx^2+Bx+C_0\) has one strictly positive and one strictly negative root, with positive root \(x_*=(B+\sqrt{B^2+4dC_0})/(2d)\). It is positive on \([0,x_*)\), zero at \(x_*\), and negative on \((x_*,\infty)\). Pulling back through \(x=\omega^2\) proves the stated unique crossing. For \(d=0\), the polynomial is \(Bx+C_0>0\) for all \(x\ge0\), giving the no-crossing boundary case.

**4. Endpoint and degeneracy checks.** Substitution at zero frequency gives the exact positive excess

\[
S_{\mathrm{heur}}(0)-S_{\mathrm{full}}(0)=\frac{2cu}{\Omega v^2}.
\]

For \(d>0\), the leading high-frequency coefficients give

\[
\lim_{|\omega|\to\infty}\omega^2\bigl(S_{\mathrm{full}}(\omega)-S_{\mathrm{heur}}(\omega)\bigr)=\frac{2cd}{\Omega}>0.
\]

The same expression tends to zero when \(d=0\), consistent with strict nonnegative-frequency dominance in that case. Holding \(u,v,k>0\) fixed as \(d\downarrow0\), \(B\) tends to a positive limit \(B_0\), and the crossing escapes to infinity as \(\omega_*\sim\sqrt{B_0/d}\). No statement about exact discrete-molecule stochastic processes follows from these Gaussian rational-spectrum identities without a separate approximation theorem.

## Verification

The accompanying standalone Python checker `checks/check_spectrum.py` independently constructs the full drift and diffusion matrices from elementary reaction events, computes the spectral-matrix inverse, and compares the substrate diagonal entry with the displayed rational formula on 1,200 randomly drawn positive parameter points (including the dissociation-free boundary). It verifies the reduced one-dimensional spectrum, exact difference factorization, zero-frequency identity, positivity, and both sides of the crossing. In 100 further independently parameterized positive equilibrium networks, it solves the stationary two-by-two Lyapunov equation as a four-by-four linear problem and compares the resulting full and heuristic substrate variances against the established variance formulas. A separate symbolic expansion confirms the exact numerator identity. The script reports `PASS 5000 independently computed comparisons; max_rel=3.047e-09`. Floating-point tests are supporting checks: the polynomial sign argument is the proof for the full continuum of permitted parameters.

Run with `python checks/check_spectrum.py` in a Python environment with NumPy installed.

## Relationship to prior work

Thomas, Straube and Grima (2011) established for this exact open Michaelis–Menten reaction that the conventional stochastic QSSA can overestimate the **integrated steady-state substrate variance**, and derived an explicit relative variance error. Their statement does not establish a frequency-by-frequency inequality. Thomas, Straube and Grima (2012) developed the correct slow-scale LNA and compared it with heuristic stochastic reduction, including general power-spectral methods; those generic methods do not directly state the all-parameter **unique crossing and dissociation-free exception** here. Eilertsen, Srivastava and Schnell (2021/2022) examined geometric validity of stochastic reductions. Marmolejo Lozano, Popović and Grima (2025) investigated **substrate–product cross-coherence and information transfer** in an enzyme model with downstream product decay, with full and reduced spectral matrices; their conclusions are not the scalar substrate auto-spectrum sign classification stated here. These works supply the correct physical context and spectral matrix formalism and are not claimed as new. The present contribution is the explicit signed scalar-spectrum comparison, unique finite crossover, and sharp absence-of-dissociation boundary for the unreduced physical model.

## Limitations

All comparisons are exact *within the specified LNAs*. At high frequencies, where the reversal may occur, heuristic QSSA often lies outside its physically justified slow-timescale accuracy range. The finding is not a claim that high-frequency substrate fluctuations of the full chemical master equation are Gaussian or accurately resolved by the reduced stochastic model at low molecule counts. The result concerns the basic substrate-input Michaelis–Menten network with a fixed conserved enzyme pool, free-substrate observable, no feedback from product, and the conventional birth–death heuristic reduced law. It does not encompass other definitions of the substrate observable, total-QSSA propensities, rigorous ssLNA, extrinsic colored noise, enzyme synthesis/degradation, downstream feedback, or additional species. Spectral conventions are fixed to a common two-sided concentration PSD. A comprehensive independent historical-priority and scientific audit has not been performed.

## References

1. P. Thomas, A. V. Straube and R. Grima, “Limitations of the stochastic quasi-steady-state approximation in open biochemical reaction networks,” arXiv:1110.6617, first posted 30 October 2011. https://arxiv.org/html/1110.6617v1
2. P. Thomas, A. V. Straube and R. Grima, “The slow-scale linear noise approximation: an accurate, reduced stochastic description of biochemical networks under timescale separation conditions,” *BMC Systems Biology* 6, 39 (2012). https://doi.org/10.1186/1752-0509-6-39
3. J. Eilertsen, K. Srivastava and S. Schnell, “Stochastic enzyme kinetics and the quasi-steady-state reductions: Application of the slow scale linear noise approximation à la Fenichel,” arXiv:2101.04814 (2021). https://arxiv.org/abs/2101.04814
4. J. D. Marmolejo Lozano, N. Popović and R. Grima, “Effects of Model Reduction on Coherence and Information Transfer in Stochastic Biochemical Systems,” arXiv:2510.27600, first posted 31 October 2025. https://arxiv.org/html/2510.27600v1
