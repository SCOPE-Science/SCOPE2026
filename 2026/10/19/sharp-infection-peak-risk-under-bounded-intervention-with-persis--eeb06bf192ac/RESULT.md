# Sharp infection-peak risk under bounded intervention with persistent multiplicative noise

## Finding

Consider a stochastic susceptible–infected epidemic with suppressible incidence and independent multiplicative noise in the infected compartment. Regardless of the chosen bounded nonnegative intervention, its infected path dominates a single geometric Brownian process. When full incidence suppression and maximal treatment are admissible, this lower envelope is attained **as a process**, so it determines simultaneously the exact minimal terminal exceedance probability and the exact minimal probability of breaching any infection threshold by any specified time. In particular, for every threshold strictly above the initial infection level, the minimal probability of *ever* breaching it is positive, with an explicit power law. Every bounded-domain approximation of the unreflected stochastic model also incurs a quantitative, positive terminal-distribution discrepancy.

Write \(i>0\) for the deterministic initial infected level, \(L>i\) for a threshold, and define
\[
 a=\gamma+\delta+H,\qquad k=a+\frac{\sigma^2}{2},\qquad h=\log(L/i),\qquad d_T=\sigma\sqrt T.
\]
Here \(H<\infty\) is the maximal treatment rate and \(\sigma>0\) is the persistent infected-noise intensity. With \(\Phi\) the standard normal distribution function, for every \(T>0\), the **exact** optimal terminal and threshold-hitting probabilities are
\[
 \inf_u\mathbb P_u\{I_T>L\}=
 \Phi\!\left(\frac{-h-kT}{d_T}\right),
\]
\[
 \inf_u\mathbb P_u\!\left\{\sup_{0\le t\le T}I_t\ge L\right\}
 =\Phi\!\left(\frac{-h-kT}{d_T}\right)
 +e^{-2kh/\sigma^2}\Phi\!\left(\frac{-h+kT}{d_T}\right).
\]
For controls allowed on the whole nonnegative time axis,
\[
 \inf_u\mathbb P_u\!\left\{\sup_{t\ge0}I_t\ge L\right\}
 =e^{-2kh/\sigma^2}
 =\left(\frac{i}{L}\right)^{1+2a/\sigma^2}>0.
\]
All three infima are attained by the **same** intervention: complete transmission suppression and maximal treatment at all times. Thus the formulas give a single sharp stochastic lower envelope, not merely unrelated probability bounds.

## Assumptions and scope

Fix \(b,\beta,\gamma,\delta,\sigma>0\), maximal treatment \(H\ge0\), maximal vaccination intensity \(V\ge0\), and deterministic \(S_0=s>0\), \(I_0=i>0\). On a filtered probability space carrying a standard Brownian motion \(W\), consider the Itô system
\[
 \begin{aligned}
 dS_t&=\big[b-(1-\alpha_t)\beta S_tI_t-(v_t+\delta)S_t\big]dt,\\
 dI_t&=\big[(1-\alpha_t)\beta S_t-(\gamma+\eta_t+\delta)\big]I_tdt
      +\sigma I_tdW_t.
 \end{aligned}
\]
The admissible controls are progressively measurable with \(0\le\alpha_t\le1\), \(0\le v_t\le V\), and \(0\le\eta_t\le H\), almost everywhere. Deterministic bounded-variation controls are included. The noise \(\sigma I_t dW_t\) is **exogenous compartment-specific fluctuation** and does not disappear when transmission is suppressed; the claim does not apply without modification to transmission-rate noise proportional to \((1-\alpha_t)S_tI_t\), nor does it assert properties of a finite-state epidemic process. The formula for hitting requires \(L>i\); if \(L\le i\), the time-zero hitting probability is one. The terminal exceedance formula remains valid for every \(L>0\) when \(h=\log(L/i)\) is allowed to be nonpositive.

For an arbitrary initial distribution independent of future Brownian increments, the same probability lower bounds hold with an additional factor \(m\) whenever \(\mathbb P\{I_0\ge i_*\}=m>0\), replacing \(i\) by \(i_*>0\); optimality for such a mixture is not asserted. Every initial distribution giving positive probability to \(I_0>0\) has at least one such \(i_*\).

## Proof

**1. Global positivity and well-posedness.** Local existence and uniqueness follow from local Lipschitz coefficients. While the state is nonnegative,
\[
 0<S_t\le K:=\max\{s,b/\delta\},
\]
because \(\dot S=b-[(1-\alpha)\beta I+v+\delta]S\le b-\delta S\), and at \(S=0\) the vector field points inward with velocity \(b>0\). On every interval before possible explosion, the linear infected equation has the exponential representation
\[
 I_t=i\exp\!\left(\sigma W_t-\frac{\sigma^2t}{2}
 +\int_0^t\big[(1-\alpha_r)\beta S_r-\gamma-\eta_r-\delta\big]dr\right)>0.
\]
As \(0\le (1-\alpha)\beta S\le\beta K\) and \(0\le\eta\le H\), this formula bounds \(I\) on each fixed finite interval by a finite random exponential depending on \(\sup_{r\le t}|W_r|\). Hence no finite-time explosion occurs, and these representations hold globally.

**2. A simultaneous pathwise lower envelope.** Set \(Z_t=i\exp(\sigma W_t-kt)\). Subtracting logarithms yields the exact identity
\[
 \log(I_t/Z_t)
 =\int_0^t\big[(1-\alpha_r)\beta S_r+H-\eta_r\big]dr\ge0.
\]
Thus \(I_t\ge Z_t\) for **all** \(t\ge0\), almost surely, for every admissible (even adapted) intervention. For \(\alpha_t\equiv1\) and \(\eta_t\equiv H\), the integrand is identically zero; hence \(I_t=Z_t\) for all \(t\), regardless of the vaccination control. This proves that the same policy attains every monotone-path exceedance bound.

**3. Terminal and finite-time crossing laws.** The Gaussian identity \(\log(Z_T/i)=\sigma W_T-kT\) gives the first probability formula. For \(L>i\), the event \(\sup_{t\le T}Z_t\ge L\) is the first passage of the drifted Brownian motion \(X_t=\sigma W_t-kt\) through \(h>0\). The reflection principle with drift (equivalently, the absorbing heat kernel obtained by the method of images) gives the first-passage density
\[
 f_{\tau_h}(t)=\frac{h}{\sigma\sqrt{2\pi t^3}}
 \exp\!\left[-\frac{(h+kt)^2}{2\sigma^2t}\right],\qquad t>0.
\]
Its integral from zero to \(T\) is the displayed two-normal-term formula: differentiating that formula reproduces \(f_{\tau_h}\), because
\[
 \varphi\!\left(\frac{-h-kT}{d_T}\right)
 =e^{-2kh/\sigma^2}\varphi\!\left(\frac{-h+kT}{d_T}\right),
\]
where \(\varphi=\Phi'\); both sides of the cumulative formula vanish as \(T\downarrow0\). Combining this with step 2 proves the exact minimum over controls.

**4. Unbounded-horizon crossing.** Since \(k>0\), the first normal term tends to zero and the second tends to \(e^{-2kh/\sigma^2}\) as \(T\to\infty\). Monotone convergence of the hitting events establishes the eventual-hitting formula. The strictly positive result holds for every finite threshold \(L>i\) and every finite removal capacity \(H\), although \(Z_t\to0\) almost surely; rare temporary peaks and eventual extinction are consistent.

**5. Quantitative consequence for bounded-domain laws.** Let \(\mu_T^u\) be the terminal law of \((S_T,I_T)\) under any chosen control, and let \(\nu\) be **any** probability law supported in the half-plane \(I\le L\), in particular a normalized Fokker–Planck law on a bounded domain contained therein. For total variation defined by \(d_{\mathrm{TV}}(\mu,\nu)=\sup_A|\mu(A)-\nu(A)|\), choose \(A=\{I>L\}\). Then
\[
 d_{\mathrm{TV}}(\mu_T^u,\nu)
 \ge\mathbb P_u(I_T>L)
 \ge\Phi\!\left(\frac{-h-kT}{d_T}\right)>0.
\]
The second inequality is sharp over controls, but equality in total variation is claimed only over arbitrary supported comparison measures: for the fully suppressing policy, conditioning its true terminal law on \(I\le L\) attains exactly this discrepancy. Such a conditioned measure is **not** claimed to solve a prescribed reflecting or zero-flux boundary problem.

Finally, for a random initial state with \(\mathbb P(I_0\ge i_*)=m>0\), the same logarithmic comparison starts from \(I_0\) and lower-bounds it on that initial event by \(i_*\exp(\sigma W_t-kt)\). Independence of the Brownian future and the initial event proves the stated \(m\)-weighted bounds. Thus any initial law with positive infectious mass and an unbounded-infection support noise as specified cannot be contained in an almost-surely invariant bounded domain at any positive time.

## Verification

The standalone standard-library script `verify.py` checks the finite-time Gaussian formula against independent numerical integration of the first-passage density, the algebraic equality between the infinite-horizon probability and the power law, and the strict order of terminal, finite-horizon peak, and eventual-peak probabilities for four parameter sets. These checks are finite numerical consistency tests; the proof for all admissible controls and thresholds is the analytic comparison above.

For \(i=1/4\), \(L=1/2\), \(\gamma=1/5\), \(\delta=1/10\), \(H=1/4\), \(\sigma=T=1\), the minimal terminal, time-one peak, and eventual peak risks are respectively approximately \(0.040653954517\), \(0.189799045911\), and \(0.233258247884\). The infection-peak probability is not interchangeable with the terminal exceedance probability.

## Relationship to prior work

Parkinson and Roy's stochastic epidemic control formulation (arXiv:2601.20181, later Journal of Mathematical Biology 93, article 47) motivates both the bounded Fokker–Planck domain and the capacity-threshold objective; its Section 2 explicitly allows compartment-proportional noise among several noise specifications. The present theorem treats the **specified persistent infected-only multiplicative-noise specialization** and the exact worst-case-over-controls pathwise peak/terminal risk, neither of which is the numerical noise choice in their Section 5: that choice is proportional to the transmission product, with a transmission control ceiling strictly below one. No conclusion here transfers automatically to those numerical experiments.

Gray et al. (2011) study stochastic SIS dynamics with a common transmission-perturbation Brownian motion, which conserves the coupled susceptible–infected total in their closed model; this differs from the persistent infected-only noise assumed here. Chen et al. (2026) analyze first-passage distributions in a finite-state Markov jump SIS model, which supplies a relevant but structurally different notion of epidemic hitting risk. The present derivation uses the classical Brownian reflection principle and does not claim novelty for that probabilistic tool itself. The contribution is the **simultaneously sharp intervention-uniform pathwise risk law and its quantitative bounded-domain implication** for the indicated controlled stochastic epidemic family.

## Limitations

The statement is about an Itô diffusion, not integer-valued infection counts. Its irreducible risk arises specifically because noise remains active after complete incidence suppression. If the infected noise also vanishes under complete transmission suppression, the sharp lower envelope and power-law result generally change; the theorem says nothing about that alternative. Full incidence suppression \(\alpha=1\) and constant maximal treatment \(\eta=H\) must be admissible to attain equality. Random initial data yield a lower bound, not usually the exact optimum. No claim is made about treatment budgets, feedback-control uniqueness, a physical finite-population upper cap, or the error of a particular PDE discretization beyond the stated support-based total-variation bound. Independent scientific validation is not implied by the analytic and numerical checks.

## References

1. C. Parkinson and S. Roy, “A Fokker-Planck framework for control of epidemics,” arXiv:2601.20181 (first version January 28, 2026), *Journal of Mathematical Biology* **93**, article 47 (2026), DOI:10.1007/s00285-026-02462-7.
2. A. Gray, D. Greenhalgh, L. Hu, X. Mao and J. Pan, “A stochastic differential equation SIS epidemic model,” *SIAM Journal on Applied Mathematics* **71** (2011), 876–902, DOI:10.1137/10081856X.
3. T. Chen, Z. Jin, G. Liu and C. Jia, “Exact results for the stochastic SIS epidemic model in densely populated environments,” *SIAM Journal on Life Sciences* (2026), DOI:10.1137/25M1805321. The first-passage result there concerns a finite-state Markov jump process, not the present controlled diffusion.
