# Sharp large-disk Gaussian ambiguity coverage with optimal squeezing and angular rigidity

## Finding

For a fixed integer \(m\ge3\), set \(q_a(d)=a^{-1}\cos^2d+a\sin^2d\) for a common squeeze \(a\ge1\), and let \(\Theta\) be any \(m\) axes on the circle of circumference \(\pi\), with repetitions allowed. Define
\[
L_m(t;a,\Theta)=\min_\phi\frac1m\sum_{j=0}^{m-1}e^{-tq_a(\phi-\theta_j)},\quad
L_m^*(t)=\sup_{a,\Theta}L_m(t;a,\Theta),\quad
\delta=\frac{\pi}{2m},\quad a_m=\cot\delta,\quad s_m=\sin(\pi/m).
\]
For \(t>0\) the supremum is attained, and \(e^{ts_m}L_m^*(t)\to 2/m\) as \(t\to\infty\). For every family of maximizing configurations, **first list the axes in positive cyclic order**, choose any first axis, and take increasing lifts on an interval of length \(\pi\) starting at that axis. Then
\[
a(t)=a_m+o(t^{-1/2}),\qquad \theta_j(t)-\theta_0(t)=j\pi/m+o(t^{-1}).
\]
For fixed real \(v,u_0,\ldots,u_{m-1}\), set \(a(t)=a_m+v/\sqrt t\) and \(\theta_j(t)=\theta_{\rm ref}+j\pi/m+u_j/t\), where \(\theta_{\rm ref}\) is a common reference angle. With \(u_m=u_0\),
\[
\lim_{t\to\infty}\frac m2e^{ts_m}L_m(t;a(t),\Theta(t))
=\exp\left[-\frac{\sin^3\delta}{\cos\delta}v^2-\cos(\pi/m)\max_j(u_{j+1}-u_j)\right].
\]
For \(m=1,2\) and every \(t>0\), \(L_m^*(t)=e^{-t}\), with equality only at \(a=1\) and arbitrary angles. Three is the first channel count to improve the exponential rate below 1; at \(m=3\) the large-disk rate, squeeze and prefactor are \(\sqrt3/2,\sqrt3,2/3\), respectively.

## Assumptions and scope

With \(\widehat f(\omega)=\int f(x)e^{-2\pi i\omega x}\,dx\), the normalized Gaussian \(g_a(x)=(2a)^{1/4}e^{-\pi ax^2}\) has \(|\mathcal A g_a(X,\Omega)|^2=e^{-\pi(aX^2+a^{-1}\Omega^2)}\), by completing the square. Rotation gives the angular profiles above, with a common quarter-turn if needed. In the pointwise linear model with independent equal-noise channels and fixed total precision, the whitened forward vector for the unknown scalar consists of \(m^{-1/2}\mathcal A g_{a,\theta_j}\), up to a common precision factor. The sum of squared magnitudes of that vector is the normalized information gain; its reciprocal is the noise variance factor for the linear least-squares inverse. This is not a claim about nonlinear phase retrieval. Each summand decreases radially, so the minimum gain on a disk of radius \(R\) is at its boundary and \(t=\pi R^2\).

## Proof

**Global upper bound and existence.** Let \(g\ge\pi/m\) be the largest gap in cyclic order. Its midpoint has geodesic distance at least \(g/2\) from every axis. Because \(q_a\) is nondecreasing on \([0,\pi/2]\),
\[
L_m\le e^{-tq_a(g/2)}\le e^{-tq_a(\delta)}\le e^{-ts_m}.
\]
The last step is AM–GM and is an equality only at \(a=a_m\). For \(a>1\) the gap step is strict if \(g>\pi/m\). For fixed \(t\), the first upper bound tends uniformly to zero as \(a\to\infty\), since \(q_a(g/2)\ge a\sin^2\delta\). The objective is continuous on compact parameter sets, and the value at \(a=1\) is positive, so a maximizer exists.

**Minimum near an equispaced design.** Consider \(a\to a_m\) and all cyclic gaps \(g_j\to2\delta\). Write \(Q=\max_j q_a(g_j/2)\). In a small fixed neighborhood of a gap midpoint the endpoint distances are \(g_j/2\pm x\). Here \(q'_a\) has a uniform positive lower bound and \(q''_a\) is bounded. Therefore \((e^{-tq_a})''=e^{-tq_a}(t^2(q'_a)^2-tq''_a)>0\) on the distance band for all sufficiently large \(t\). The sum of the two endpoint terms is at least \(2e^{-tq_a(g_j/2)}\) by convexity, hence at least \(2e^{-tQ}\). Outside these midpoint neighborhoods, the nearest axis has distance at most \(g_j/2-\varepsilon\) within its gap, so by monotonicity and the same positive slope near \(g_j/2\) its exponent is at most \(Q-c\) for some fixed \(c>0\). Its term alone exceeds \(2e^{-tQ}\) for sufficiently large \(t\). At a midpoint of a largest gap exactly two axes have distance \(g/2\); all other distances stay uniformly separated above \(g/2\), as in the equispaced limit. At that point the other terms are bounded by \(O(e^{-t(Q+c')})\) for a fixed \(c'>0\). Thus in this regime
\[
L_m=\frac2m e^{-tQ}(1+O(e^{-c't})).
\]
In particular, the equispaced configuration at \(a_m\) has \(Q=s_m\).

**Optimality and rigidity.** Comparing the equispaced lower value with the global upper bound at maximizers gives \(0\le q_a(g/2)-s_m=O(1/t)\). Coercivity and the unique minimizer of \(q_a(\delta)\) imply \(a\to a_m\); monotonicity, strict at the limiting squeeze, implies \(g\to2\delta\). All gaps then tend to \(2\delta\), since their sum is \(\pi\). The preceding asymptotic now applies to the maximizers and shows \(e^{ts_m}L_m^*(t)\to2/m\) and \(t(Q-s_m)\to0\). The gap and squeeze increments in
\[
Q-s_m=[q_a(g/2)-q_a(\delta)]+[q_a(\delta)-q_{a_m}(\delta)]
\]
are both nonnegative. The first bounds a positive multiple of \(g-2\delta\) near the limit; the second bounds a positive multiple of \((a-a_m)^2\). Thus \(g-2\delta=o(t^{-1})\) and \(a-a_m=o(t^{-1/2})\). The gap deviations sum to zero and so each is \(o(t^{-1})\); summing them in positive cyclic order yields the asserted angular estimate.

**Perturbations.** Now \(g_j/2=\delta+(u_{j+1}-u_j)/(2t)\). At \((a_m,\delta)\), \(\partial_a q=0\), \(\partial_d q=2\cos(\pi/m)\) and \(\tfrac12\partial_a^2q=\sin^3\delta/\cos\delta\). Taylor expansion, with vanishing rescaled mixed and higher terms, gives
\[
t(q_a(g_j/2)-s_m)=\cos(\pi/m)(u_{j+1}-u_j)+\frac{\sin^3\delta}{\cos\delta}v^2+o(1).
\]
Taking the maximum over the finitely many gaps and applying the midpoint estimate proves the formula. For \(m=2\), the largest-gap midpoint has all distances at least \(\pi/4\), so \(L_m\le e^{-t(a+a^{-1})/2}<e^{-t}\) if \(a>1\). For \(m=1\) the direction orthogonal to the axis gives \(L_1=e^{-ta}\). In both cases \(a=1\) attains \(e^{-t}\).

## Verification and limitations

The accompanying `checks/gaussian_design_check.py` reports 86 finite identity and numerical checks in the archived verification. Finite angle grids do not establish the continuum minima or asymptotic law; the proof above supplies those conclusions. The theory fixes \(m\), uses a common squeeze and equal precision on a circular region, and does not assert finite-\(t\) angular optimality for \(m\ge3\), optimization over unequal weights or other windows, or nonlinear recovery stability.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, [arXiv:2410.05486](https://arxiv.org/abs/2410.05486), §2.1 and Remark 2.1, use equally spaced squeezed Gaussians. Their threshold-ellipse denominator supplies the same geometric exponential rate after minimizing in the squeeze; that rate alone is not claimed as a new finding. Their threshold construction and positive unsquared recovery sum do not give the prefactor, arbitrary-angle optimality and rigidity, or angular perturbation law of the equal-weight squared sum. The separate three-window squared-sum [record a5ef66ef0375](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-sharp-squeezing-threshold-for-three-rotated-gaussian-ambiguity-w--a5ef66ef0375) obtains the same leading factor and rate on the fixed three-axis grid while allowing variable weights and optimizing the squeeze. Its fixed-placement result does not supply the placement rigidity or the general common-squeeze theorem here. Hardin, Kendall and Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, [arXiv:1208.5261](https://arxiv.org/abs/1208.5261), Theorem 1, require a convex geodesic-distance potential. Here \((e^{-tq_a})''(0)=-2t(a-a^{-1})e^{-t/a}<0\) at nontrivial squeezes. Historical priority beyond these statement comparisons is not certified.
