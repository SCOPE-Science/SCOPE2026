# A sharp edge-density threshold for optimal spatial resetting

## Finding

Let a freely diffusing Brownian searcher on the positive half-line be absorbed at the origin. Its diffusivity is \(D>0\), its reset clock is Poisson with rate \(r>0\), and each new launch point is an independent sample of \(Y_d=d+U\), where \(d>0\), \(B>0\), and \(U\) has density
\[
 f_p(u)=\frac{p u^{p-1}}{B^p}\mathbf 1_{(0,B)}(u),\qquad p>0.
\]
The initial launch point also has this distribution. Write \(T_d(r)\) for the mean time to absorption averaged over all randomness, and \(\mathcal R_d=\operatorname*{argmin}_{r>0}T_d(r)\). Each \(\mathcal R_d\) is nonempty and compact.

There is an exact **edge-density transition at \(p=2\)**. For every fixed \(D,B>0\):

1. If \(0<p<2\), put \(a=2-p\). For *every* choice of global optimum \(r_d\in\mathcal R_d\), as \(d\downarrow0\),
\[
\boxed{\frac{d^2 r_d}{D}\longrightarrow a^2,\qquad
 \frac{\min_{r>0}T_d(r)}{d^a}\longrightarrow
 \frac{B^p e^a}{D\,\Gamma(p+1)a^a}.}
\]
Thus the optimal reset rate diverges as the inverse square of the target-to-support gap; the optimized mean falls with the edge-exponent-dependent power \(d^{2-p}\). At an optimal rate the distance \(U_{\mathrm{last}}\) of the launch point of the *successful final excursion* from the support edge satisfies
\[
\boxed{\frac{U_{\mathrm{last}}}{d}\ \Longrightarrow\
 \operatorname{Gamma}(p,\mathrm{rate}=2-p).}
\]
The initial launch counts as a launch point if absorption precedes the first reset.

2. If \(p\ge2\), all the sets \(\mathcal R_d\), for sufficiently small \(d>0\), lie in a common compact subinterval of \((0,\infty)\). Every accumulation point as \(d\downarrow0\) is an optimizer of the limiting \(d=0\) mean first-passage time. No uniqueness of global minimizers is asserted.

In particular, uniform edge density (\(p=1\)) gives \(r_d\sim D/d^2\) and \(\min T_d\sim eBd/D\), whereas linearly *vanishing* edge density (\(p=2\)) already keeps the optimal reset rate finite. The exponent threshold is a statement about changing the *launch-position distribution*, not the distribution of resetting times.

## Assumptions and scope

The motion is the diffusion \(dX_t=\sqrt{2D}\,dW_t\) between instantaneous resets, with perfect absorption at \(0\), no drift and no reflection other than the natural positive-half-line absorption. Each Poisson reset completely renews the launch position, independently of the past. Parameters \(D,B,p\) remain fixed while \(d\downarrow0\). The edge law has support \([d,d+B]\), with density proportional to the \((p-1)\)-st power of the distance from the closest allowed launch location \(d\). The result allows \(0<p<1\), for which this density has an integrable singularity at its near edge.

Define \(k=\sqrt{r/D}\). The Laplace transform of a single launch's successful absorption-before-reset probability is
\[
 I_d(k)=\mathbb E[e^{-kY_d}]=e^{-dk}G_p(k),\qquad
 G_p(k)=p\int_0^1t^{p-1}e^{-Bkt}\,dt.
\]
Here \(\Gamma\) is Euler's gamma function. The distinction between global minimizers and merely local stationary points is essential; optimization need not be unimodal for arbitrary distributed resetting laws.

## Proof

**Renewal identity.** Starting from distance \(y>0\), the no-reset Brownian hitting-time transform is \(\mathbb E_y[e^{-s\tau_0}]=e^{-y\sqrt{s/D}}\). One launch succeeds before the independent exponential reset time with probability \(I_d(k)\), averaged over the starting distribution. A launch lasts an expected \((1-I_d(k))/r\) up to success or reset. Renewal over independent launches therefore gives
\[
 T_d(Dk^2)=\frac{I_d(k)^{-1}-1}{Dk^2}
 =\frac{e^{dk}/G_p(k)-1}{Dk^2}.
 \tag{1}
\]
Equivalently, the same identity follows from averaging the published distributed-reset first-passage formula. Since \(\mathbb E Y_d=d+pB/(p+1)>0\), equation (1) diverges as \(k\downarrow0\) like \(\mathbb E Y_d/(Dk)\). The exact asymptotic in the next paragraph and \(d>0\) imply divergence as \(k\to\infty\), giving a positive finite global minimum.

**Large-rate kernel.** Changing variables \(z=Bkt\) yields
\[
 G_p(k)=\frac{p}{(Bk)^p}\int_0^{Bk}z^{p-1}e^{-z}\,dz
 \sim \frac{\Gamma(p+1)}{B^pk^p}.
 \tag{2}
\]
In fact, for every sequence \(k\to\infty\) and \(d\ge0\), equation (1) has the *uniform relative asymptotic*
\[
 T_d(Dk^2)=\frac{B^p}{D\Gamma(p+1)}e^{dk}k^{p-2}(1+o(1)),
 \tag{3}
\]
because the omitted subtraction is a relative factor \(1-e^{-dk}G_p(k)\to1\), uniformly over \(d\ge0\). No fixed-\(dk\) assumption is needed for this estimate.

**Global optimizer when \(p<2\).** Put \(a=2-p>0\). Trial rates with \(k=a/d\) and (3) show that \(\inf_kT_d(Dk^2)=O(d^a)\to0\). For every fixed \(k>0\), \(T_d(Dk^2)\ge T_0(Dk^2)>0\). Uniform divergence at \(k\downarrow0\) consequently forces every global optimizer \(k_d=\sqrt{r_d/D}\) to tend to infinity. Now write \(v_d=d k_d\). By (3), for such optimizers,
\[
 \frac{T_d(Dk_d^2)}{d^a}=
 \frac{B^p}{D\Gamma(p+1)}e^{v_d}v_d^{-a}(1+o(1)).
 \tag{4}
\]
The trial \(v=a\) bounds the left side. Since \(e^v v^{-a}\to\infty\) both as \(v\downarrow0\) and \(v\to\infty\), the optimizer sequence \(v_d\) remains in a fixed compact subset of \((0,\infty)\). The function \(e^v v^{-a}\) has a unique global minimum at \(v=a\), since its logarithmic derivative is \(1-a/v\). Comparison with the trial rate gives \(v_d\to a\) and the first two boxed limits. This compares *all* global minimizers and does not assume uniqueness or convexity of \(T_d\) at finite \(d\).

**The critical and supercritical cases.** The inequality \(T_d(Dk^2)\ge T_0(Dk^2)\) holds for all \(d\ge0\). For \(p>2\), (3) at \(d=0\) shows \(T_0(Dk^2)\to\infty\) as \(k\to\infty\); it also diverges as \(k\downarrow0\). This confines all minimizers for small \(d\) to a compact interval. For \(p=2\), direct integration gives
\[
 G_2(k)=\frac{2[1-(1+Bk)e^{-Bk}]}{B^2k^2},\quad
 T_0(Dk^2)=\frac{B^2}{2D[1-(1+Bk)e^{-Bk}]}-\frac1{Dk^2}.
 \tag{5}
\]
Thus \(T_0(Dk^2)=B^2/(2D)-1/(Dk^2)+o(k^{-2})\) at infinity: its infimum is *strictly below* its limiting value, and is attained at some finite positive \(k\). The bound \(T_d\ge T_0\) then excludes the far tail for all small \(d\), because evaluating \(T_d\) at one fixed strictly-better finite rate converges to its \(d=0\) value. The small-rate divergence excludes zero uniformly. Continuity on the remaining compact interval proves that every accumulation point minimizes \(T_0\).

**Location of the last successful launch.** Each independent launch at \(Y_d=d+u\) succeeds before a reset with probability \(e^{-k(d+u)}\). Conditional on being the final successful launch, its edge offset has density
\[
 \mathbb P(U_{\mathrm{last}}\in du)=\frac{u^{p-1}e^{-ku}\mathbf1_{(0,B)}(u)\,du}{\int_0^B v^{p-1}e^{-kv}\,dv}.
 \tag{6}
\]
In particular \(kU_{\mathrm{last}}\) has density proportional to \(z^{p-1}e^{-z}\mathbf1_{(0,Bk)}\); as \(k\to\infty\) it converges in total variation to \(\operatorname{Gamma}(p,\mathrm{rate}=1)\). Along any minimizing sequence in the subcritical case, \(dk_d\to 2-p\), so continuous scaling gives the third boxed assertion.

## Verification

The standalone file `verify.py` evaluates the exact lower incomplete-gamma representation of (1), scans for global minima on a logarithmic grid and refines each interval, and compares optimization and successful-launch moments with the stated asymptotic constants at decreasing gaps. It also checks (5) independently against quadrature. Run with `python verify.py` after installing `numpy` and `scipy`. Computations are diagnostic finite-parameter checks; the conclusions for arbitrary positive parameters and limiting gaps follow from the proof above, not from finite numerical sampling.

## Relationship to prior work

Méndez, Flaquer-Galmés and Campos (2024) derived the general averaged resetting first-passage transform, studied uniform and other spatial resetting distributions, and established qualitative existence of optimal rates outside compact resetting intervals. Their uniform case corresponds to \(p=1\) here, after translating the origin and interval. The renewal formula (1) and its uniform specialization are **prior facts**, not claimed discoveries. Julián-Salgado, Dagdug and Boyer (2025) investigated discontinuous optimal-rate transitions for truncated Gaussian, exponential and two-site resetting laws and derived the exponential tilt for the successful last launch. Their printed high-rate edge approximation assumes a nonzero, finite edge density, whereas the present \(p>1\) family has a vanishing edge density and \(0<p<1\) a singular edge density. The present claim is the global-optimum *edge-collision scaling*, the sharp \(p=2\) retention boundary and the coupled Gamma scaling **at the optimizer**; it neither reclaims the general renewal identity nor asserts global uniqueness at finite gap.

## Limitations

The result is one-dimensional, drift-free, with instantaneous independent Poisson resets and exact power-law densities on a fixed finite support. It does not establish that the minimizing rate is unique for every positive gap, does not classify metastable optima, and does not extend the critical case to arbitrary densities merely asymptotic to a linear edge. The source formulas determine this family implicitly, so an unrecognized equivalent asymptotic theorem in other distributed-resetting literature remains a novelty risk.

## References

1. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (initial version made public 2024-01-02), Sections II, III, VI, VII, https://arxiv.org/abs/2401.01125 .
2. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (2025), especially equations (3)–(9), (27)–(29), and Sections III, V, VI, https://arxiv.org/pdf/2507.14483 .
3. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, J. Phys. A 44, 435001 (2011), arXiv:1107.4225, https://arxiv.org/abs/1107.4225 .
