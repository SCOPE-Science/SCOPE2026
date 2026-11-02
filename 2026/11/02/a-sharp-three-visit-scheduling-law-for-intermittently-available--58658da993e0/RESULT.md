# A sharp three-visit scheduling law for intermittently available species

## Finding

A stationary two-state availability process is observed at three predetermined occasions: the first at time \(0\), the last at time \(T>0\), and a freely placed middle occasion \(t\in[0,T]\). Each occasion has its own nonzero conditional detection probability \(p_1,p_2,p_3\). The first and last times and all detection probabilities are fixed before optimizing. Availability follows a continuous-time two-state Markov chain whose transition intensities can vary with time by a common positive multiplier.

Write \(\pi\in(0,1)\) for the common stationary availability probability and \(\Lambda(t)\) for the cumulative Markov relaxation rate from time zero, with \(L=\Lambda(T)>0\). The **unique** time maximizing the probability of at least one detection obeys

\[
\boxed{\Lambda(t_*)=\operatorname{clip}_{[0,L]}\!\left(\frac{L}{2}+\frac12\log\frac{p_1(1-\pi p_3)}{p_3(1-\pi p_1)}\right).}
\]

Here \(\operatorname{clip}_{[0,L]}(u)=\max\{0,\min\{L,u\}\}\). Consequently, the optimal middle occasion is **independent of its own detection probability** \(p_2>0\). When \(p_1=p_3\), it bisects the cumulative relaxation clock, not necessarily physical time. For unequal endpoint detection strengths it shifts toward the less reliable endpoint. It coincides with an endpoint if and only if the signed log-ratio lies outside the exact interval \((-L,L)\). In the coincident case, two instantaneous detection attempts are independent conditional on the same availability state.

This classifies the entire three-visit schedule under the stated model, including the interior, first-endpoint, and last-endpoint regimes. Optimizing instead occupancy-estimator variance, first-detection delay, or any objective beyond probability of at least one detection is not asserted.

## Assumptions and scope

Let \(X(s)\in\{0,1\}\) mean that a target species is locally unavailable or available, respectively. For fixed \(\alpha,\beta>0\) and a continuous \(h:[0,T]\to(0,\infty)\), let the time-dependent generator, in state order \((0,1)\), be

\[
Q(s)=h(s)\begin{pmatrix}-\alpha&\alpha\\ \beta&-\beta\end{pmatrix},\qquad
\pi=\frac{\alpha}{\alpha+\beta},\qquad
\Lambda(t)=(\alpha+\beta)\int_0^t h(s)\,ds.
\]

Initially, \(X(0)\) has the stationary Bernoulli law with availability probability \(\pi\). The common multiplicative time dependence preserves this law at every time. Detection attempts at the three occasions \(0,t,T\) have fixed conditional success probabilities \(p_i\in(0,1]\) if \(X=1\) and zero false positives if \(X=0\). Attempts are independent conditional on their three availability states, even if occasions coincide. The species is assumed present in the larger survey region throughout the interval, while availability at the immediate observation station fluctuates. Exactly three attempted observations are made, including two with fixed times. The objective is \(P_{\mathrm{det}}(t)=\Pr(\text{at least one success})\).

The formula does not require constant instantaneous transition intensities; it does require their ratio to be constant, thereby keeping \(\pi\) fixed. No species colonization or permanent extinction is modeled.

## Proof

Put \(u=\Lambda(t)\in[0,L]\), \(x=e^{-u}\), and \(y=e^{-(L-u)}\); thus \(xy=e^{-L}\). Because the generators are scalar multiples of one fixed generator, their transition matrices satisfy

\[
\Pr(X(b)=j\mid X(a)=i)=\pi_j+e^{-[\Lambda(b)-\Lambda(a)]}(\mathbf{1}_{\{i=j\}}-\pi_j),
\]

where \(\pi_1=\pi\) and \(\pi_0=1-\pi\). Directly,

\[
\mathbb E X_i=\pi,\quad
\mathbb E(X_iX_j)=\pi^2+\pi(1-\pi)e^{-[\Lambda(t_j)-\Lambda(t_i)]}\quad(i<j),
\]

and, by the Markov property conditional on middle-state availability,

\[
\mathbb E(X_1X_2X_3)=\pi[\pi+(1-\pi)x][\pi+(1-\pi)y].
\]

Let \(N(u)=\Pr(\text{no successful detection})=\mathbb E\prod_{i=1}^3(1-p_iX_i)\). Substituting these moments and collecting the terms depending on \(u\) gives

\[
N(u)=C+A e^{-u}+B e^{-(L-u)},
\]

where the explicit constant is

\[
\begin{aligned}
C={}&1-\pi(p_1+p_2+p_3)
+\pi^2(p_1p_2+p_1p_3+p_2p_3)-\pi^3p_1p_2p_3\\
&+e^{-L}\pi(1-\pi)p_1p_3-e^{-L}\pi(1-\pi)^2p_1p_2p_3,
\end{aligned}
\]

and

\[
A=\pi(1-\pi)p_1p_2(1-\pi p_3)>0,\qquad
B=\pi(1-\pi)p_2p_3(1-\pi p_1)>0.
\]

Hence \(N''(u)=Ae^{-u}+Be^{-(L-u)}>0\), so the objective has a unique global minimizer on \([0,L]\). The unconstrained stationary point solves

\[
Ae^{-u}=Be^{-(L-u)},\qquad
u=\frac{L+\log(A/B)}{2}.
\]

Strict convexity proves the constrained minimizer is \(\operatorname{clip}_{[0,L]}(u_{\mathrm{free}})\), and strict positivity of \(\Lambda'\) yields a unique physical time \(t_*\). The factor \(p_2\) cancels from \(A/B\), and

\[
\frac AB=\frac{p_1(1-\pi p_3)}{p_3(1-\pi p_1)}.
\]

Since \(p\mapsto p/(1-\pi p)\) is strictly increasing on \((0,1]\), the unconstrained shift has the sign of \(p_1-p_3\). More precisely, letting

\[
r=\log\frac{p_1(1-\pi p_3)}{p_3(1-\pi p_1)},
\]

we have the sharp three-way classification: \(r\le-L\) yields \(t_*=0\); \(-L<r<L\) yields the interior point \(\Lambda(t_*)=(L+r)/2\); and \(r\ge L\) yields \(t_*=T\). At equality the corresponding endpoint is still the unique minimizer by strict convexity. This completes the proof for every allowed parameter choice.

## Verification

The standalone `check.py` uses exact rational hidden-state summation over all eight three-occasion state paths and independently compares it to the derived expression at **729 parameter choices**. It additionally verifies optimality, strict midpoint convexity, and invariance under changing \(p_2\) in deterministic numerical test grids. All checks passed when run with Python's standard library.

For example, with \(\pi=0.3\), \((p_1,p_2,p_3)=(0.8,0.5,0.4)\), and \(L=3\), the optimal hazard coordinate is about \(1.91987532737591\), with nondetection probability \(0.59233177479710\), versus \(0.59427079529642\) at hazard midpoint. With \(\pi=0.35\), \((p_1,p_2,p_3)=(0.95,0.6,0.1)\), and \(L=1\), the optimum is the **last endpoint**: its nondetection probability is about \(0.568865084302834\), versus \(0.595143985970051\) at the hazard midpoint.

The finite checks are independent corroboration of the identity, not a substitute for the preceding all-parameter proof. To reproduce: `python3 check.py`.

## Relationship to prior work

Kendall, Nichols and Hines (1997) model Markovian temporary emigration in capture–recapture studies. MacKenzie and Royle (2005) study occupancy-survey design, including survey timing and survey effort, but their explicit allocation optimization assumes a constant detection probability across occasions and minimizes estimator variance rather than the three-occasion first-confirmation failure probability under Markov availability. Nichols and coauthors (2008) handle unequal detection devices and local availability in multiscale occupancy models, but the inspected development concerns estimation and modeling, not a complete time-placement optimum for three attempts.

The elementary two-state transition and conditional-detection identities are not claimed as new. The claim here is the specific strict, all-parameter, three-regime optimum with an exact hazard-clock shift, endpoint-collapse criteria, and cancellation of middle-visit detectability. No published-source priority or independent scientific validation is asserted.

## Limitations

The objective is detection at least once for an already present species, not precise occupancy estimation, optimal information gain, adaptive observation policies, or minimum cost. The earliest and latest occasions are fixed, and the ability to perform two conditionally independent attempts at a shared time is assumed. State-dependent false positives, different temporal dependence in the two transition rates, variation in the common stationary availability fraction, observer effects, effort-dependent visit quality, and environmental feedback are not covered. This is a theoretical scheduling benchmark rather than a directly estimated empirical wildlife model. Broader hidden-Markov sensor-scheduling theorems might imply the formula; historical priority remains subject to further examination.

## References

1. Kendall, W. L., Nichols, J. D., and Hines, J. E. (1997). *Estimating temporary emigration using capture–recapture data with Pollock's robust design*. Ecology 78, 563–578. DOI: 10.1890/0012-9658(1997)078[0563:ETEUCR]2.0.CO;2. First published 1997-03-01.
2. MacKenzie, D. I., and Royle, J. A. (2005). *Designing occupancy studies: general advice and allocating survey effort*. Journal of Applied Ecology 42, 1105–1114. DOI: 10.1111/j.1365-2664.2005.01098.x.
3. Nichols, J. D., et al. (2008). *Multi-scale occupancy estimation and modelling using multiple detection methods*. Journal of Applied Ecology 45, 1321–1329. DOI: 10.1111/j.1365-2664.2008.01509.x.
