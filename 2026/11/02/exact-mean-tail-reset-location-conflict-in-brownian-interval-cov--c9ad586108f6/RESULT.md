# Exact mean–tail reset-location conflict in Brownian interval coverage

## Finding

Fix \(L,D,r>0\). A reflected Brownian particle on \([0,L]\), with generator \(D\partial_{xx}\), starts at \(z\in[0,L]\) and is instantaneously reset to \(z\) at the event times of an independent rate-\(r\) Poisson clock. Visits to either endpoint are remembered permanently across resets. Let \(T_z\) be the first time at which **both** endpoints have been visited; visiting an endpoint at time zero counts. Put \(s=L\sqrt{r/D}\), \(u=z/L\), and \(s_{\rm sp}=2\operatorname{arsinh}(5^{-1/4})\). Define

\[
 s_*=2\operatorname{arcosh}\left(\frac{1+\sqrt{17}}4\right),\qquad s_*^2=2.14832149293397\ldots.
\]

**Coupled location-design theorem.** At every fixed \(r>0\), the complete set of global minimizers of the mean \(\mathbb E T_z\) is \(\{0,L\}\) when \(s<s_*\), \(\{0,L/2,L\}\) when \(s=s_*\), and \(\{L/2\}\) when \(s>s_*\). The switch is discontinuous. For \(s\le s_{\rm sp}\), the midpoint maximizes the mean and the endpoints minimize it; for \(s>s_{\rm sp}\), the midpoint and both endpoints are strict local minima (the latter relative to the closed feasible interval), separated by precisely two symmetric interior local maxima. Their global ordering changes at \(s_*\).

In contrast, for **every** \(r>0\), the long-time exponential cover-completion rate
\[
 \Lambda_r(z):=-\lim_{t\to\infty}\frac1t\log\Pr(T_z>t)
\]
exists, is positive, and is uniquely maximized by \(z=L/2\). Consequently, throughout \(0<s<s_*\), every mean-optimal reset location has a strictly **worse** exponential completion-time tail than the midpoint. At \(s=s_*\) the midpoint is both tail-optimal and tied for mean-optimality.

The exact mean formula used in the proof is
\[
 \mathbb E T_z=\frac1r\left[
 \frac{\cosh s}{\cosh(su)}+
 \frac{\cosh s}{\cosh(s(1-u))}-
 \frac{\cosh(s/2)}{\cosh(s(u-1/2))}-1\right].
\]
The general reset-renewal and all-location mean-cover formulas are prior theory; the new assessed result is the **complete sharp location-design phase diagram together with the universally opposite tail optimum**.

## Assumptions and scope

The particle is one-dimensional, continuously reflected at both endpoints, with independent Poisson resets to its fixed starting site. Endpoint-detection flags persist after every reset, and \(r,D,L\) are fixed and strictly positive. The objective varies only \(z\) while holding these parameters fixed. The asymptotic rate concerns the full persistent-memory cover time, not the time to hit just one endpoint, and no claim is made about minimizing quantiles at every finite observation horizon.

## Proof

**Step 1: the exact mean.** Write \(\tau_0,\tau_L,\tau_{\{0,L\}}\) for the first times to hit the left endpoint, the right endpoint, and either endpoint under resetting. The event that coverage is incomplete at time \(t\) equals the union of the events that the two respective endpoints are unvisited. Therefore, without independence assumptions,
\[
 \mathbb E T_z=\mathbb E\tau_0+\mathbb E\tau_L-\mathbb E\tau_{\{0,L\}}.
\]
For any nonreset first-hitting time \(\tau\) from the reset point, set \(\phi(q)=\mathbb E e^{-q\tau}\). A first-cycle renewal decomposition at rate \(r\) gives the mean under resetting as \([\phi(r)^{-1}-1]/r\). Standard backward boundary-value equations \(Df''=qf\) give
\[
 \phi_0(q)=\frac{\cosh(\sqrt{q/D}(L-z))}{\cosh(\sqrt{q/D}L)},\quad
 \phi_L(q)=\frac{\cosh(\sqrt{q/D}z)}{\cosh(\sqrt{q/D}L)},\quad
 \phi_{\{0,L\}}(q)=\frac{\cosh(\sqrt{q/D}(z-L/2))}{\cosh(\sqrt{q/D}L/2)}.
\]
Here the unhit single target is absorbing, the other endpoint reflecting. Substitution proves the displayed mean, with boundary cases understood directly or by continuity.

**Step 2: global mean minimizers and the two thresholds.** Set \(C=\cosh(s/2)\), \(a=\sinh^2(s/2)=C^2-1\) and \(t=\cosh(s(u-1/2))\). As \(u\) runs through \([0,1/2]\), \(t\) decreases strictly from \(C\) to \(1\). Hyperbolic addition identities reduce the mean exactly to
\[
 r\mathbb E T_z+1= C\frac{(1+4a)t^2-a}{t(t^2+a)}.
\]
Its derivative with respect to \(t\) has the sign of
\[
 P_a(t^2)=-(1+4a)t^4+4a(1+a)t^2+a^2.
\]
For \(a>0\), \(P_a(q)\) has exactly one positive zero; moreover \(P_a(1)=5a^2-1\) and \(P_a(C^2)=-1-2a<0\). Thus when \(a\le 5^{-1/2}\), the mean strictly increases from the endpoint to the midpoint. When \(a>5^{-1/2}\), it rises to one interior strict maximum and then falls toward the midpoint, so all global minima must occur among the endpoints and midpoint, and exactly the claimed local extrema occur by symmetry. The spinodal value is \(s_{\rm sp}=2\operatorname{arsinh}(5^{-1/4})\).

At an endpoint \(r\mathbb E T_0=\cosh s-1=2(C^2-1)\); at the midpoint \(r\mathbb E T_{L/2}=3C-2/C-1\). Their difference is
\[
 r(\mathbb E T_0-\mathbb E T_{L/2})
 =\frac{(C-1)(2C^2-C-2)}{C}.
\]
Since \(C>1\), it changes sign precisely at \(C=(1+\sqrt{17})/4\), proving the global optimizer classification and its strictness. At the equality, only \(0,L/2,L\) minimize.

**Step 3: existence of the decay rates.** Let \(S^0_{0,z}(t)\) be the survival probability for hitting \(0\) from \(z>0\) *without* resetting (absorption at \(0\), reflection at \(L\)). Its Laplace transform
\[
 H_0(q;z)=\int_0^\infty e^{-qt}S^0_{0,z}(t)\,dt
\]
is finite for \(q>-\delta\), where \(\delta=D\pi^2/(4L^2)\), and strictly decreases from infinity to zero as \(q\) runs from \(-\delta\) to infinity. The nonreset kernel has the explicit representation \(H_0(q;z)=[1-\phi_0(q)]/q\), continued at \(q=0\) and analytically through allowed negative \(q\). The resetting renewal equation gives
\[
 \widehat S^r_{0,z}(p)=\frac{H_0(p+r;z)}{1-rH_0(p+r;z)}.
\]
There is a unique \(q_0(z)>-\delta\) satisfying \(rH_0(q_0(z);z)=1\). The pole \(p=q_0(z)-r\) is simple, and positivity-improving compact killed reflected diffusion with a bounded reset operator gives a simple dominant eigenvalue. Consequently
\[
 S^r_{0,z}(t)=A_0(z)e^{-\lambda_0(z)t}(1+o(1)),\quad
 \lambda_0(z)=r-q_0(z)>0,\quad A_0(z)>0.
\]
The analogous statement holds for survival of the right endpoint with \(\lambda_L(z)=\lambda_0(L-z)\). At \(z=0\) or \(L\), the already visited endpoint contributes identically zero to the unfinished-coverage probability.

**Step 4: strict spatial monotonicity and no cancellation.** Comparison for one-dimensional reflected Brownian motions driven by the same Brownian path shows \(S^0_{0,z}(t)\) is strictly increasing in \(z\) for every \(t>0\), away from coincident endpoints. Therefore \(H_0(q;z)\) is strictly increasing in \(z\) for all \(q>-\delta\); the root \(q_0(z)\) is strictly increasing, so \(\lambda_0(z)\) is strictly decreasing. Reflection gives \(\lambda_L(z)\) strictly increasing.

The reset survival probability for hitting **neither** endpoint has a corresponding positive principal rate \(\lambda_{\{0,L\}}(z)\). Its nonreset survival transform is strictly smaller than each single-target transform; its admissible Laplace domain extends further left because the Dirichlet–Dirichlet first eigenvalue exceeds the Dirichlet–Neumann eigenvalue. Comparing the unique renewal roots gives \(\lambda_{\{0,L\}}(z)>\max\{\lambda_0(z),\lambda_L(z)\}\) for interior \(z\). Thus inclusion–exclusion cannot cancel the slowest positive exponential, and
\[
 \Lambda_r(z)=\min\{\lambda_0(z),\lambda_0(L-z)\},\qquad 0<z<L.
\]
The limiting boundary formula uses the opposite-endpoint hitting rate. Since \(\lambda_0\) is strictly decreasing, \(\Lambda_r\) strictly increases on \([0,L/2]\) and strictly decreases on \([L/2,L]\), proving its unique center optimum. This completes the coupled theorem.

## Verification

The accompanying Python program `verify_cover.py` performs 53 deterministic assertions with `numpy` and `scipy`. They check (i) the exact endpoint/midpoint and global comparisons over sampled positions and rates; (ii) mean cover times independently by solving a three-phase finite-state killed Markov generator that explicitly retains visited-endpoint flags; and (iii) the single-endpoint principal decay eigenvalue by an independent finite-state generator against the analytical renewal root. All 53 assertions passed in the packaged file. The finite-state tests are discretization checks only, and do not replace Steps 1–4 of the proof.

At \(L=D=1\), the mean-optimal reset site switches at \(r=s_*^2=2.14832149293397\ldots\); the midpoint becomes locally mean-stable earlier at \(r=s_{\rm sp}^2=1.57186229708842\ldots\).

Reproduce with `python verify_cover.py` in an environment with Python 3, NumPy and SciPy installed.

## Relationship to prior work

Ghosh and Sabhapandit (arXiv:2605.31207v1, publicly submitted 2026-05-29) calculate the entire cover-time distribution and mean for resetting to the midpoint, and optimize reset **frequency** at that fixed location. Linn and Lawley (arXiv:2406.12154v2, first submitted 2024-06-17) give an exact reflected-interval all-location mean and general cover-time renewal/inclusion–exclusion relations, so **the mean formula itself, and its parameter dependence, are not new**. The location-optimizer part follows from this known formula with the separate global stationary-point and algebraic phase-boundary analysis in Step 2. Neither inspected work establishes the complete sharp reset-*position* phase diagram and the distinct, always-center optimal **long-time cover-tail exponent** with the resulting mean–tail conflict. The tail theorem depends on a spectral comparison not furnished by the known mean formula. A related fixed-rate mean–variance calculation does not cover the present all-rate mean–tail theorem. General killed-Markov and renewal theory provide standard ingredients, not an asserted new method.

## Limitations

This is a fixed-rate reset-location theorem, not joint optimization over location and reset frequency; independent scientific and publication-priority audit has not been performed. The instantaneous reset mechanism preserves endpoint-visit memory. Reset delays, state-dependent resetting, non-Poisson clocks, imperfect detection, and unequal reflection laws are not covered. The tail-optimality theorem concerns the exponential asymptotic rate; it does not claim full stochastic ordering of cover times or superiority for every finite-time quantile. The all-location exact mean was already available in the literature. Publication novelty of the additional optimizer/tail classification is assessed on the inspected sources and available search evidence, not proven by a negative search.

## References

1. A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting*, arXiv:2605.31207v1 (2026-05-29), https://arxiv.org/html/2605.31207 .
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154v2 (first submitted 2024-06-17), https://arxiv.org/pdf/2406.12154 ; *Chaos* **35**, 043124 (2025).
3. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, *Physical Review Letters* **106**, 160601 (2011).
