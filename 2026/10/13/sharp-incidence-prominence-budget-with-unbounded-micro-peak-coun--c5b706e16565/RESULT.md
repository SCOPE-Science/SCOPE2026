# Sharp incidence-prominence budget with unbounded micro-peak count under monotone transmission

## Finding

There is a sharp contrast between the number of strict incidence peaks and their total relative depth in a closed susceptible–infectious–removed epidemic. **A nonincreasing transmission rate can generate arbitrarily many strict incidence peaks while infection prevalence rises throughout**, even when transmission is real analytic, its logarithmic slope has a uniform bound independent of the number of peaks, and its total logarithmic decline is arbitrarily small. Conversely, whenever the susceptible–infectious state contributes nonnegative instantaneous incidence growth, the **sum of the logarithmic peak-to-trough drops cannot exceed the total logarithmic drop in transmission**, with optimal constant one.

More precisely, consider positive differentiable transmission \(\beta\) on \([0,T]\), removal rate \(\gamma>0\), and the normalized SIR equations
\[
\dot S=-\beta SI,\qquad \dot I=\beta SI-\gamma I,\qquad \dot R=\gamma I,
\]
with \(S(0),I(0)>0\), \(S+I+R=1\), and incidence \(c=\beta SI\). Put
\[
H(t)=\beta(t)\bigl(S(t)-I(t)\bigr)-\gamma.
\]
If \(\beta\) is nonincreasing and \(H\geq0\) on \([0,T]\), then for any finite sequence of pairwise interior-disjoint, chronologically ordered incidence-drop intervals \([u_j,v_j]\) with \(0\leq u_j<v_j\leq T\),
\[
\sum_j\log\frac{c(u_j)}{c(v_j)}\leq\log\frac{\beta(0)}{\beta(T)}.
\]
Here the intervals may be chosen from a local maximum of incidence to its subsequent local minimum. The constant one is sharp among models satisfying \(H>0\), even with \(S(0)=9/10\), \(I(0)=1/10\), \(\gamma=1\), and \(T=1/20\). A negative logarithmic drop is allowed in the displayed general inequality; for peak-to-trough intervals every term is positive.

For those same four fixed initial parameters and for each integer \(k\geq1\) and each \(\varepsilon>0\), there exists a real-analytic, strictly decreasing transmission function such that
\[
\beta(0)=4,\quad 0<\log\frac{\beta(0)}{\beta(T)}<\varepsilon,\quad 0<-\frac{d}{dt}\log\beta(t)<5,
\]
for every \(t\in[0,T]\), while \(\dot I(t)>0\) everywhere and \(c(t)\) has at least \(k\) distinct strict interior local maxima separated by distinct strict interior local minima. All these examples satisfy \(H>0\). Thus fixed positive log-prominence cannot persist across arbitrarily many peaks at a fixed forcing budget, although the unthresholded count is unbounded.

## Assumptions and scope

The population is homogeneously mixed, closed, deterministic and normalized to one. Transmission is exogenously time varying and positive. The general budget requires \(\beta\in C^1([0,T])\), \(\beta'\leq0\), \(H\geq0\); it makes no assertion when the last inequality fails. The construction uses a fixed short observation window \(T=1/20\) in units in which \(\gamma=1\). Strict peaks mean strict local maxima of the unsmoothed instantaneous incidence, not prevalence or clinically significant outbreaks. No uniform positive peak prominence or minimum time separation is asserted as \(k\to\infty\).

## Proof

**1. Exact budget.** Positive solutions satisfy the logarithmic derivative identity
\[
\frac{d}{dt}\log c(t)=\frac{\beta'(t)}{\beta(t)}+\beta(t)(S(t)-I(t))-\gamma
=\frac{d}{dt}\log\beta(t)+H(t).
\]
Consequently, for each \(u<v\),
\[
\log\frac{c(u)}{c(v)}=\log\frac{\beta(u)}{\beta(v)}-\int_u^v H(t)\,dt.
\]
When \(H\geq0\) and the intervals are disjoint and ordered, add the inequalities and use monotonicity of \(\beta\) to bound their total transmission drop by its drop over the entire interval. This proves the displayed bound, including the sharp coefficient candidate.

**2. Bounds uniform in the construction.** Fix \(k\geq1\), \(\varepsilon>0\), set
\[
T=\frac1{20},\quad \delta=\min\{\varepsilon,\frac1{100}\},\quad d=\min\{\frac1{10},\frac{\delta}{8T}\},\quad \Delta=\frac{T}{k+1},\quad t_j=j\Delta.
\]
Choose a width \(w>0\) with
\[
w<\min\{\frac\Delta{10},\frac{\delta}{64k}\}.
\]
Define the nonnegative logarithmic removal rate and its integral by
\[
q(t)=d+4\sum_{j=1}^{k}\exp\left(-\frac{(t-t_j)^2}{w^2}\right),\quad
\Theta(t)=\int_0^t q(s)\,ds,\quad \beta(t)=4e^{-\Theta(t)}.
\]
Finite sums and integrals of Gaussian functions are real analytic. Clearly \(-\beta'/\beta=q>0\), so \(\beta\) decreases. The Gaussian area estimate \(\int_{-\infty}^{\infty}e^{-z^2}\,dz=\sqrt\pi<2\) yields
\[
0<\Theta(T)<dT+8kw\leq\frac\delta8+\frac\delta8=\frac\delta4<\varepsilon.
\]
Thus \(\beta(t)\geq4e^{-\delta/4}>39/10\). For any \(t\), because the centers have separation \(\Delta>10w\), at most one center is nearest and the others give a rapidly convergent Gaussian tail:
\[
\sum_{j=1}^k e^{-(t-t_j)^2/w^2}
\leq 1+2\sum_{m=0}^{\infty}e^{-(5+10m)^2}
<1+\frac{2e^{-25}}{1-e^{-100}}<\frac{101}{100}.
\]
To see the first inequality, count the nearest center by at most one, and place at most one other center on each side in each successive distance band of width \(\Delta\), starting at distance \(\Delta/2>5w\). Hence \(q(t)<d+4(101/100)<5\), uniformly in \(k\) and \(\varepsilon\).

As \(0<\beta\leq4\), solution comparison gives, for \(0\leq t\leq T\),
\[
S(t)\geq\frac9{10}e^{-4t}\geq\frac{18}{25},\qquad
I(t)\leq\frac1{10}e^{3t}\leq\frac2{17},\qquad S(t)\leq\frac9{10}.
\]
Here \(e^{-1/5}\geq1-1/5\) and \(e^{3/20}\leq1/(1-3/20)\). Thus
\[
\frac{2867}{2125}=\frac{39}{10}\left(\frac{18}{25}-\frac2{17}\right)-1
\leq H(t)\leq4\cdot\frac9{10}-1=\frac{13}{5}.
\]
In particular \(H(t)>13/10\), while \(\beta(t)S(t)>\frac{39}{10}\frac{18}{25}>1\), proving \(\dot I(t)>0\) everywhere.

**3. At least \(k\) pairs of extrema.** Let \(t_0=0\), \(t_{k+1}=T\), and let \(s_j=(t_j+t_{j+1})/2\) for \(j=0,\ldots,k\). At each pulse center \(t_j\), \(q(t_j)\geq4\), so
\[
\frac{d}{dt}\log c(t_j)=H(t_j)-q(t_j)\leq\frac{13}{5}-4<0.
\]
At every midpoint \(s_j\), all pulse centers are at distance at least \(\Delta/2>5w\); summing on either side gives
\[
\sum_{\ell=1}^k e^{-(s_j-t_\ell)^2/w^2}
\leq\frac{2e^{-25}}{1-e^{-100}}<\frac1{100}.
\]
Therefore
\[
\frac{d}{dt}\log c(s_j)>\frac{2867}{2125}-\frac1{10}-\frac4{100}>0.
\]
Continuity and the extreme value theorem give a local maximum in every open interval \((s_{j-1},t_j)\) and a local minimum in \((t_j,s_j)\), all disjoint. The incidence is real analytic and not constant on any open interval (its derivative has strict signs at the chosen sample points); hence its local extrema are strict. This provides \(k\) distinct maxima and minima for every \(k\).

**4. Sharpness of the coefficient one.** Choose any fixed integer \(k\), distinct interior centers \(t_j\), and positive pulse masses \(a_j\) with \(A=\sum_j a_j<1/100\). Take \(w\downarrow0\) and a strictly positive drift \(d_w\downarrow0\); set
\[
q_w(t)=d_w+\sum_j\frac{a_j}{\sqrt\pi w}\exp\left(-\frac{(t-t_j)^2}{w^2}\right),\qquad
\beta_w(t)=4\exp\left(-\int_0^tq_w(s)\,ds\right).
\]
The preceding state comparisons with \(0<\log(4/\beta_w(T))<1/100+o(1)\) give a uniform strictly positive lower bound on \(H_w\) and a finite upper bound. For small \(w\), the logarithmic-incidence derivative is positive at \(t_j\pm\sqrt w\) and negative at \(t_j\). Hence each short pulse neighborhood contains a maximum \(p_j\) followed by a minimum \(v_j\), both within \([t_j-\sqrt w,t_j+\sqrt w]\). Since the local maximum is no lower than incidence at the left endpoint and the local minimum is no higher than incidence at the right endpoint,
\[
\log\frac{c_w(p_j)}{c_w(v_j)}
\geq\int_{t_j-\sqrt w}^{t_j+\sqrt w}q_w(t)\,dt
-\int_{t_j-\sqrt w}^{t_j+\sqrt w}H_w(t)\,dt
\longrightarrow a_j.
\]
The general budget gives the opposite upper bound \(\sum_j\log(c_w(p_j)/c_w(v_j))\leq\log(\beta_w(0)/\beta_w(T))\to A\). Consequently the ratio of these two sums tends to one. The constant in the budget cannot be reduced under the stated hypotheses. All pulse maxima and minima are interior and separated for small \(w\).

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to check the comparison margins \(H>13/10\), \(H<13/5\), and \(\beta S>1\). It also evaluates five explicit Gaussian forcing schedules (one, two, four, seven, and twelve pulses) and integrates their SIR equations using a fourth-order Runge–Kutta implementation as an independent finite numerical sanity check. Execute `python verify.py` with Python 3 standard library; expected output begins with `VERIFY_OK`. The unrestricted assertions for every \(k\geq1\), every \(\varepsilon>0\), and the sharp budget are established analytically above, **not** by the finite checks.

## Relationship to prior work

Rabajante (2026), arXiv:2610.05556v1, equation (21) and Proposition 2, gives the exact incidence-growth identity and explains that incidence may peak even while prevalence increases. Corollary 1 of that work already constructs arbitrarily many incidence peaks with unrestricted time-varying transmission, a result explicitly treated here as prior. Neither the stationary-point identity nor unrestricted representability is claimed as new. The present result adds a sharp *aggregate logarithmic prominence bound* with a realizable equality limit and a *uniform-slope analytic counterfamily with arbitrarily many incidence peaks and strictly increasing prevalence*. These two conclusions distinguish mathematical extrema from peaks surviving a minimum-prominence threshold; they are not obtained merely by relabeling the stationary-point identity.

Pollicott, Wang and Weiss (2012) develop inversion of time-dependent transmission from observed trajectories; their reconstruction mechanism does not impose monotone forcing or prove a sharp prominence budget. Wang and Wang (2026) study reconstruction robustness across transmission and observation structures. Setianto and Hidayat (2023) fit epidemic waves using multiple Gaussian transmission pulses, whereas the present construction places positive Gaussian pulses in the *decrease rate of logarithmic transmission*, making the transmission function strictly decreasing. These precedents establish that flexible transmission reconstruction and Gaussian epidemic forcing are already known.

## Limitations

Extrema produced by arbitrarily narrow pulses have vanishing prominence when the total forcing variation tends to zero; their number is not a proxy for separate clinically relevant epidemic waves. The example is deterministic and on a short time window, and no inference about intervention efficacy, actual observed outbreaks, data resolution or causal mechanisms follows. The prominence bound needs \(H\geq0\); outside this region independent depletion or recovery effects enter. No claim is made about exact peak count (only a lower bound), spacing-independent lower prominence, global outbreak trajectories after \(T\), or all possible model extensions. Full independent scientific review has not been performed.

## References

1. J. F. Rabajante, *How Simple Models Can Reproduce Multiple Epidemic Waves: Peak Topology, Minimal Dynamic Complexity, and Inference for Time-Varying Transmission*, arXiv:2610.05556v1 (public 2026-10-04), https://arxiv.org/html/2610.05556v1. Especially Section 4.2, Proposition 2, and Sections 5–7.
2. M. Pollicott, H. Wang, H. Weiss, *Extracting the time-dependent transmission rate from infection data via solution of an inverse ODE problem*, J. Biol. Dyn. 6 (2012), 509–523, https://doi.org/10.1080/17513758.2011.645510.
3. X. Wang and H. Wang, *Robust Inverse Reconstruction of Time-Varying Transmission Rates Across Model Structures and Incidence Forms* (2026), https://doi.org/10.1007/s11538-026-01597-4.
4. M. B. Setianto and R. Hidayat, *Modeling the time-dependent transmission rate using gaussian pulses for analyzing the COVID-19 outbreaks in the world*, Scientific Reports (2023), https://doi.org/10.1038/s41598-023-31714-5.
