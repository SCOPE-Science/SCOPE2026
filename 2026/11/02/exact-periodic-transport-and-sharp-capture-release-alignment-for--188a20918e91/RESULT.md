# Exact periodic transport and sharp capture–release alignment for reversible run-and-tumble particles

## Finding

A run-and-tumble particle that can be immobilized and subsequently reactivated has an **exact**, not merely asymptotic-in-the-period, effective transport coefficient in every bounded, strictly positive periodic capture–release environment. The coefficient depends on the environment only through two spatial averages, while a sharp rearrangement principle determines the optimal relative placement of capture and release regions.

Let \(G=\frac1L\int_0^L\gamma(x)\,dx\) and \(R=\frac1L\int_0^L\frac{\gamma(x)}{\delta(x)}\,dx\). Then

\[
\boxed{D_{\mathrm{eff}}=\frac{v^2}{(\alpha+G)(1+R)}.}
\]

For any initial deterministic position and internal state, unwrapped displacement has zero limiting drift and converges under diffusive rescaling to Brownian motion with variance parameter \(2D_{\mathrm{eff}}\). For fixed histograms of the two rate profiles, aligning high capture rates with high release rates is optimal for spreading; opposing their ranks is worst. Both bounds are exact, and neither depends on the order in which paired regions appear along the period.

## Assumptions and scope

Fix \(L,v,\alpha>0\). On the real line, let \(X_t\) have an internal state \(S_t\in\{-1,0,+1\}\). In state \(s=\pm1\), the position travels at velocity \(sv\). An orientation flip \(s\mapsto-s\) occurs at rate \(\alpha/2\), and capture \(s\mapsto0\), without a position jump, occurs at rate \(\gamma(X_t)\). In state \(0\), the position does not move; reactivation occurs at rate \(\delta(X_t)\), without a position jump, and independently selects \(+1\) or \(-1\) equiprobably. Assume that \(\gamma,\delta\) are measurable, \(L\)-periodic, and bounded above and away from zero. Rates are understood almost everywhere, allowing piecewise-constant zones with jumps. The process is independent of any external Brownian forcing.

The generator for test functions \(f_s(x)\), in the moving states, is
\[
\mathcal Lf_s=sv\,\partial_xf_s+\frac\alpha2(f_{-s}-f_s)+\gamma(x)(f_0-f_s),
\qquad s=\pm1;
\]
while \(\mathcal Lf_0=\delta(x)[(f_++f_-)/2-f_0]\). Write \(\bar X_t=X_t\bmod L\) for the process on the periodic cell. Define \(G\) and \(R\) as in the finding. An increasing quantile function \(a^\uparrow(u)\) is a nondecreasing measurable function on \((0,1)\) with the same spatial value distribution as \(a(x)\) over a uniformly sampled period.

## Proof

**1. Invariant law and ergodicity.** The probability densities on the periodic cell
\[
\pi_+(x)=\pi_-(x)=\frac1{2L(1+R)},\qquad
\pi_0(x)=\frac{\gamma(x)}{L\delta(x)(1+R)}
\]
are normalized and solve the three stationary forward equations: the active advective currents cancel between directions, symmetric flipping balances, and \(\delta(x)\pi_0(x)=\gamma(x)(\pi_+(x)+\pi_-(x))\) at every relevant position. Positivity and boundedness of the rates, together with \(\alpha,v>0\), give a uniform accessibility/minorization after a sufficiently long fixed time: from any state one may reactivate if necessary, follow prescribed moving intervals, and use one or two orientation reversals to obtain a final moving-position density bounded below on the circle. Such event paths have probabilities bounded uniformly below because all transition intensities lie between positive finite constants. Hence the compact phase process has a unique invariant law and its time averages converge to the displayed stationary averages from every starting state.

**2. Exact harmonic coordinate.** Put
\[
 g=\frac{v}{\alpha+G},\qquad
 h'(x)=\frac{\gamma(x)-G}{\alpha+G},
\]
with \(h\) any absolutely continuous, \(L\)-periodic antiderivative; it exists because the derivative has zero period average. Define \(F_s(x)=x+h(x)+sg\) for \(s=\pm1,0\). In a moving state,
\[
\mathcal LF_s=s\left[v(1+h')-(\alpha+\gamma(x))g\right]=0,
\]
while \(\mathcal LF_0=\delta[(F_++F_-)/2-F_0]=0\). Therefore \(M_t=F_{S_t}(X_t)-F_{S_0}(X_0)\) is a square-integrable martingale. The correction \(F_s(x)-x\) is bounded uniformly in \(x,s\), and jump sizes of the martingale are bounded by \(2g\).

**3. Quadratic variation and diffusion.** An active particle flips at rate \(\alpha/2\), giving a martingale increment of magnitude \(2g\), and is captured at rate \(\gamma(x)\), giving magnitude \(g\). The corresponding predictable quadratic-variation rate is \((2\alpha+\gamma(x))g^2\). A resting particle reactivates at rate \(\delta(x)\), producing an increment of magnitude \(g\), so its rate is \(\delta(x)g^2\). Average over the invariant law:
\[
\lim_{t\to\infty}\frac{\langle M\rangle_t}{t}
=\frac{g^2}{1+R}\left[(2\alpha+G)+G\right]
=\frac{2v^2}{(\alpha+G)(1+R)}
\quad\text{almost surely}.
\]
The bounded-jump martingale functional central limit theorem gives \(T^{-1/2}M_{T\cdot}\Rightarrow\sqrt{2D_{\mathrm{eff}}}\,B_\cdot\) in path space as \(T\to\infty\). The bounded corrector transfers this to \((X_{T\cdot}-X_0)/\sqrt T\). Martingale isometry gives \(\mathbb EM_t^2/t\to2D_{\mathrm{eff}}\), while the correction and its covariance contribute only \(o(t)\), proving \(\operatorname{Var}(X_t)/(2t)\to D_{\mathrm{eff}}\). The mean displacement divided by \(t\) vanishes because the martingale has mean zero and the correction is bounded.

**4. Sharp spatial pairing.** At fixed marginal spatial laws for \(\gamma\) and \(\delta\), the average \(G\) is fixed. To optimize \(D_{\mathrm{eff}}\), one must minimize or maximize \(R=\int\gamma/\delta\) under couplings of those two laws. For \(g_1\ge g_2\) and \(d_1\ge d_2>0\),
\[
\left(\frac{g_1}{d_1}+\frac{g_2}{d_2}\right)
-\left(\frac{g_1}{d_2}+\frac{g_2}{d_1}\right)
=(g_1-g_2)\left(\frac1{d_1}-\frac1{d_2}\right)\le0.
\]
Thus exchanging two out-of-order assignments decreases \(R\) when the ranks become aligned. Repeated exchanges establish the minimum for comonotone coupling and maximum for countermonotone coupling for finite simple profiles. Bounded approximation and dominated convergence give the general Hardy–Littlewood rearrangement bounds
\[
\int_0^1\frac{\gamma^\uparrow(u)}{\delta^\uparrow(u)}\,du
\le R\le
\int_0^1\frac{\gamma^\uparrow(u)}{\delta^\uparrow(1-u)}\,du.
\]
Both endpoint couplings can be implemented as periodic measurable profiles, proving sharpness. Since \(D_{\mathrm{eff}}\) decreases strictly with \(R\), the first coupling maximizes diffusion and the second minimizes it. Equality need not determine a unique spatial arrangement in the presence of level sets or translations.

**5. A concrete strict design gap.** For two equal-width zones let \(\gamma\) take values \(1/2,3/2\), let \(\delta\) take the same values, and fix \(v=7/5,\alpha=6/5\). Aligned zones give \(G=1,R=1,D_{\mathrm{eff}}=49/110\); anti-aligned zones give \(G=1,R=5/3,D_{\mathrm{eff}}=147/440\). The exact gain is \(D_{\mathrm{aligned}}/D_{\mathrm{anti}}=4/3\). No small-period assumption is involved.

## Verification

Run `python check_transport.py` with Python 3, NumPy and SciPy installed. Its finite verification independently discretizes active motion as nearest-grid Markov jumps, solves the periodic Poisson corrector equation numerically, evaluates the stationary martingale variance, and checks convergence under mesh refinement for three spatial designs. It also checks the continuum harmonic-coordinate identity in exact rational arithmetic and enumerates the sharp pairings of several finite histograms. The packaged checker passed 217 exact/finite assertions. These finite diagnostics do not establish the quantified continuum theorem; the proof above does.

## Relationship to prior work

Angelani's 2023 study treats irreversible absorption in trapping regions and explicitly identifies reversible activation and periodic trapping intervals as prospective extensions. Hillen's 2003 resting-phase velocity-jump model permits spatial capture variation, but imposes spatially constant reactivation and derives an outer parabolic scaling; it does not state the exact fixed-period diffusion coefficient or the two-profile coupling optimum. Lutscher and Hillen's 2021 work homogenizes heterogeneous *two-moving-state* correlated walks, without a distinct immobilized compartment. Taylor-King et al. (2015) analyze general running/resting durations and displacement moments in spatially homogeneous settings. Berezhkovskii and Bezrukov (2011) give homogeneous mobile–immobile transport moments. The novelty assessed here is the exact finite-rate periodic capture/release transport law and its rearrangement principle, not the velocity-jump model itself, standard martingale theory, or classical rearrangement inequalities.

## Limitations

The claim assumes a constant speed, symmetric orientation flips, fair fresh-direction choice on reactivation, a stationary periodic environment, and strictly positive bounded capture/release rates. It does not cover directional memory through rest, spatially varying speeds, non-exponential waits, irreversible absorption, finite-time diffusivity optimization, or nonperiodic random media. The result is a self-review, not an independent external audit; related homogenization theory could contain a more general implicit antecedent even where no directly covering profile-specific statement was located.

## References

1. L. Angelani, *Run-and-tumble motion in trapping environments* (first public 2023-03-06), https://arxiv.org/abs/2303.03078.
2. T. Hillen, *Transport equations with resting phases*, European Journal of Applied Mathematics **14** (2003), 613–636, https://doi.org/10.1017/S0956792503005291; open full text https://www.math.ualberta.ca/~thillen/paper/hillenejam.pdf.
3. F. Lutscher and T. Hillen, *Correlated random walks in heterogeneous landscapes: Derivation, homogenization, and invasion fronts*, AIMS Mathematics **6** (2021), 8920–8948, https://doi.org/10.3934/math.2021518.
4. J. P. Taylor-King et al., *From Birds to Bacteria: Generalised Velocity Jump Processes with Resting States*, Bulletin of Mathematical Biology **77** (2015), https://doi.org/10.1007/s11538-015-0083-7.
5. A. M. Berezhkovskii and S. M. Bezrukov, *Effective drift and diffusion of a particle jumping between mobile and immobile states*, Journal of Electroanalytical Chemistry **660** (2011), 352–355, https://doi.org/10.1016/j.jelechem.2010.08.017.
