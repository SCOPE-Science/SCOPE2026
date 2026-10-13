# A normalized-contact invasion-threshold reversal in an age-structured network SIR model

## Finding

For the **literal normalized contact probability** and demographic equations of Yang–Martcheva–Zhang–Sun's degree-structured SIR model, the infection-invasion characteristic equation is
\[
1=\beta\frac{\sum_{k=1}^{n}k^2}{\sum_{k=1}^{n}k}\int_0^\infty e^{-\lambda a}\pi(a)\,da,
\qquad \pi(a)=\exp\!\left(-\int_0^a[\mu+\gamma(s)+r(s)]\,ds\right).
\]
Thus the corresponding invasion threshold is
\[
\mathcal R_{\mathrm{contact}}=\beta\frac{\sum_{k=1}^n k^2}{\sum_{k=1}^n k}\int_0^\infty\pi(a)\,da,
\]
**without a prefactor** \(\Lambda/\mu\). The source instead prints \(\mathcal R_{\mathrm{source}}=(\Lambda/\mu)\mathcal R_{\mathrm{contact}}\) and uses its value to decide disease-free stability. The difference can reverse the qualitative conclusion, not just rescale a reported numerical estimate.

Specifically, in the admissible constant-rate case with degree set \(\{1,2\}\) and
\[
\Lambda=1,\quad \mu=\tfrac12,\quad \beta=\tfrac12,\quad
\gamma(a)=r(a)=\tfrac14,\quad \alpha=1,
\]
the printed quantity is \(\mathcal R_{\mathrm{source}}=5/3>1\), whereas the complete finite-dimensional linearization of the very same normalized-contact equations has eigenvalues \(-1\), \(-1/6\), and \(-1/2\) with multiplicity four. Therefore the disease-free equilibrium is **locally asymptotically stable**, contrary to the source's \(\mathcal R_{\mathrm{source}}>1\) instability criterion.

## Assumptions and scope

Degree classes are \(k=1,\ldots,n\) with integer \(n\ge2\); demographic rates satisfy \(\Lambda,\mu>0\), transmission \(\beta>0\), saturation coefficient \(\alpha\ge0\), and measurable nonnegative bounded rates \(\gamma,r\). The full source has susceptible density \(S_k(t)\), recovered density \(R_k(t)\), and nonnegative infection-age density \(I_k(a,t)\) with total class size
\[
N_k(t)=S_k(t)+\int_0^\infty I_k(a,t)\,da+R_k(t).
\]
We use **exactly the source's normalized infection contact probability** (section 2):
\[
\Theta(t)=\frac{\sum_{k=1}^n k\int_0^\infty I_k(a,t)\,da}{\sum_{k=1}^n kN_k(t)}.
\]
Its printed model has \(S'_k=\Lambda-\beta k S_k\Theta-\mu S_k\), infection-age transport \((\partial_t+\partial_a)I_k=-[\mu+\gamma(a)+r(a)/(1+\alpha\Theta)]I_k\), inflow \(I_k(0,t)=\beta kS_k\Theta\), and a recovered equation receiving both clearance flows and losing \(\mu R_k\). The fraction \(p(k)\) defined in the source is \(N_k/\sum_jN_j\), not an additional freely selectable demographic parameter.

The exact counterexample additionally fixes constant recovery/treatment rates, so integration over infection age closes to the ordinary six-variable SIR system. It is a genuine parameter subfamily allowed by the source assumptions; no zero or singular parameter is used. The local stability conclusion refers to this autonomous constant-rate system. The general age-structured formula characterizes exponential infection-invasion modes; a separate infinite-dimensional nonlinear stability theorem is **not** claimed.

## Proof

**1. Demographic balance and degree weights.** Integrate the infection-age transport equation over age, use the inflow boundary, and add the susceptible and recovered equations. Infection transfers and recovery transfers cancel, leaving
\[
\frac{dN_k}{dt}=\Lambda-\mu N_k.
\]
Thus every disease-free class has \(N_k^0=S_k^0=\Lambda/\mu\), and the source's definition forces \(p^0(k)=1/n\). In particular, if its per-class birth rates are truly all equal, prescribing a nonuniform fixed degree distribution is not a stationary realization of these equations.

**2. Linearization of the normalized contact term.** Put \(L=\sum_{k=1}^n k\), \(Q=\sum_{k=1}^n k^2\), and let \(J_k(t)=\int_0^\infty I_k(a,t)\,da\). At the disease-free state, the numerator in \(\Theta\) vanishes and its denominator equals \((\Lambda/\mu)L\). Hence its differential is precisely
\[
D\Theta=\frac{\mu}{\Lambda L}\sum_{j=1}^n j\,DJ_j.
\]
The infected boundary inflows linearize to
\[
DI_k(0,t)=\beta k(\Lambda/\mu)D\Theta
=\frac{\beta k}{L}\sum_{j=1}^n j\,DJ_j.
\]
Crucially, the factor \(\Lambda/\mu\) cancels. The treatment saturation denominator contributes no linear correction at disease-free state because it multiplies an already vanishing infected density. At this order, infection-age survival is \(\pi(a)\) as above.

**3. Invasion characteristic equation.** For a nonzero exponentially varying infected boundary flux \(b_k(t)=u_k e^{\lambda t}\), the age profile is \(I_k(a,t)=u_k e^{\lambda(t-a)}\pi(a)\), whenever the Laplace integral exists. Consequently \(J_k(t)=b_k(t)\int_0^\infty e^{-\lambda a}\pi(a)da\). The linearized boundary condition becomes a positive rank-one eigenvalue equation on the vector \((u_k)\); taking the degree-weighted sum gives
\[
1=\beta\frac{Q}{L}\int_0^\infty e^{-\lambda a}\pi(a)da.
\]
At \(\lambda=0\) its right-hand side is \(\mathcal R_{\mathrm{contact}}\). For nonnegative integrable \(\pi\) this scalar function is strictly decreasing on nonnegative real \(\lambda\), tends to zero as \(\lambda\to+\infty\), and hence has a positive real root if and only if \(\mathcal R_{\mathrm{contact}}>1\). This establishes a precise invasion-mode threshold, without a claim about all spectrum of the general age PDE.

**4. Complete finite-dimensional counterexample.** At the stated constant rates, put \(\delta=\mu+\gamma+r=1\) and \(J_k=\int I_k\). The integrated system is
\[
\begin{aligned}
\dot S_k&=1-\tfrac12 kS_k\Theta-\tfrac12S_k,\\
\dot J_k&=\tfrac12 kS_k\Theta-\left(\tfrac34+\frac{1/4}{1+\Theta}\right)J_k,\\
\dot R_k&=\left(\tfrac14+\frac{1/4}{1+\Theta}\right)J_k-\tfrac12R_k,\\
\Theta&=\frac{J_1+2J_2}{S_1+J_1+R_1+2(S_2+J_2+R_2)}.
\end{aligned}
\]
The disease-free equilibrium is \((S_1,S_2,J_1,J_2,R_1,R_2)=(2,2,0,0,0,0)\). In that order the full exact Jacobian is
\[
\begin{pmatrix}
-1/2&0&-1/6&-1/3&0&0\\
0&-1/2&-1/3&-2/3&0&0\\
0&0&-5/6&1/3&0&0\\
0&0&1/3&-1/3&0&0\\
0&0&1/2&0&-1/2&0\\
0&0&0&1/2&0&-1/2
\end{pmatrix}.
\]
The infected subblock has trace \(-7/6\), determinant \(1/6\), and eigenvalues \(-1\), \(-1/6\). The four other eigenvalues equal \(-1/2\) by triangular block structure. All six have strictly negative real parts, so standard finite-dimensional linearization proves local asymptotic stability. In contrast, because \(\pi(a)=e^{-a}\) and \(Q/L=5/3\), the source's written threshold gives
\[
\mathcal R_{\mathrm{source}}=\frac12\cdot2\cdot\frac53=\frac53>1,
\qquad
\mathcal R_{\mathrm{contact}}=\frac12\cdot\frac53=\frac56<1.
\]
This contradicts precisely the instability implication of Theorem 3.1 when applied to the source's section-2 normalized-contact equations.

**5. Transfer of stability to the constant-rate infection-age system.** The integrated six-dimensional dynamics are exactly closed for constant \(r,\gamma\), so their exponentially attracting disease-free equilibrium controls the time-dependent infection boundary fluxes \(B_k(t)=\beta kS_k(t)\Theta(t)\) and ensures \(B_k(t)=O(e^{-ct})\) for some \(c>0\) and all sufficiently small initial perturbations. The original age density is reconstructed by characteristics. In the initial-data region \(a>t\), the decay factor is at most \(e^{-(\mu+\gamma)t}\); for \(0<a<t\), it is at most \(e^{-(\mu+\gamma)a}\) times \(B_k(t-a)\), because the exact total removal hazard \(\mu+\gamma+r/(1+\alpha\Theta)\) is bounded below by \(\mu+\gamma=3/4\) for nonnegative solutions. Therefore
\[
\|I_k(\cdot,t)\|_{L^1}\le e^{-3t/4}\|I_k(\cdot,0)\|_{L^1}+\int_0^t e^{-3(t-s)/4} B_k(s)\,ds\longrightarrow0.
\]
The first term and the convolution both decay exponentially (possibly with a harmless polynomial factor when rates coincide); the susceptible and recovered variables converge exponentially by the closed ODE. This lifts local asymptotic stability from the six-dimensional projection to the full positive infection-age state space for this constant-rate counterexample; it does not establish a general age-dependent global stability theorem.

## Verification

The accompanying standalone standard-library-only `verification.py` uses exact rational forward-mode differentiation of **the nonlinear six-dimensional vector field**, independently recomputes its full Jacobian, checks the infected block's exact characteristic polynomial and all remaining eigenvalues, and checks both threshold fractions. Running `python3 verification.py` prints `VERIFY_OK`. This is a complete exact certificate for the finite-dimensional counterexample; no simulation or floating-point eigenvalue judgment is needed.

## Relationship to prior work

The source paper explicitly prints a reproduction threshold containing \(\Lambda/\mu\) in section 3 and uses it in Theorem 3.1 and the appendix (equation (7.1)); its section 2 instead defines the contact probability as infected half-edge counts divided by **all** half-edge counts. The calculation here maintains the latter normalization consistently. Classical network SIR theory often uses a second-moment/first-moment degree factor, but that general factor is **not** the new contribution. The contribution is the exact incompatible population-scale factor in this specific 2026 non-Markovian model and a fully admissible, explicit counterexample reversing its printed disease-free stability verdict. The related Li–Yousef network model and general non-Markovian-network literature concern background mechanisms, rather than the exact contradiction established here.

## Limitations

The threshold is derived for the **literal** normalized contact definition and per-class recruitment terms. A deliberately different model, such as one defining an unnormalized infected-edge density and correspondingly changing variable meanings and/or degree-specific recruitment rates, can exhibit a different threshold; that is not the printed model studied here. The counterexample proves local asymptotic stability only, not global stability, endemic equilibrium classification, or the truth/falsity of every backward-bifurcation analysis in the source. The nonuniform static degree-distribution issue is ancillary to the stability reversal and is not used to generalize empirical network predictions. No empirical disease conclusions, priority over classical threshold formulas, or independent verification are claimed.

## References

1. J. Yang, M. Martcheva, J. Zhang, and G.-Q. Sun, “Global Dynamics of a Non-Markovian Epidemic Model on Complex Networks,” *SIAM Journal on Applied Mathematics* **86** (2026), 2206–2230, https://doi.org/10.1137/24M1711546. Public online date: 18 August 2026; source sections 2–3, 7 and appendix.
2. C. H. Li and A. M. Yousef, “Bifurcation analysis of a network-based SIR epidemic model with saturated treatment function,” *Chaos* **29** (2019), 033129, https://doi.org/10.1063/1.5079631 (contextual predecessor cited in the motivating paper).
