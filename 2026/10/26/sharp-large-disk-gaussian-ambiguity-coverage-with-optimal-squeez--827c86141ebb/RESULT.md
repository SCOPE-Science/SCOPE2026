# Sharp large-disk Gaussian ambiguity coverage with optimal squeezing and angular rigidity

## Finding

For any integer \(m\geq 3\), positive \(t\), squeeze \(a\geq1\), and orientations \(\Theta=(\theta_0,\ldots,\theta_{m-1})\in(\mathbb R/\pi\mathbb Z)^m\), set
\[
q_a(d)=a^{-1}\cos^2d+a\sin^2d,\qquad
L_m(t;a,\Theta)=\min_{\phi\in\mathbb R/\pi\mathbb Z}\frac1m\sum_{j=0}^{m-1}e^{-tq_a(\phi-\theta_j)}.
\]
Let \(L_m^*(t)=\sup_{a\geq1,\Theta}L_m(t;a,\Theta)\). Define \(\delta_m=\pi/(2m)\), \(a_m=\cot\delta_m\), and \(s_m=\sin(\pi/m)\). Then
\[
\boxed{\lim_{t\to\infty}e^{ts_m}L_m^*(t)=\frac2m.}
\]
Every choice of maximizers, after cyclic relabeling and a common rotation, satisfies
\[
a(t)=a_m+o(t^{-1/2}),\qquad
\theta_j(t)=\theta_0(t)+\frac{j\pi}{m}+o(t^{-1}),
\quad j=0,\ldots,m-1.
\]
More sharply, if \(v,u_0,\ldots,u_{m-1}\) are any *fixed* real numbers and
\[
a(t)=a_m+v/\sqrt t,\qquad
\theta_j(t)=\theta_0+j\pi/m+u_j/t,
\]
then, putting \(u_m=u_0\),
\[
\boxed{\lim_{t\to\infty}\frac m2e^{ts_m}L_m(t;a(t),\Theta(t))
=\exp\!\left[-\frac{\sin^3\delta_m}{\cos\delta_m}v^2
-\cos(\pi/m)\max_{0\leq j<m}(u_{j+1}-u_j)\right].}
\]
For \(m=1\) or \(m=2\), the exact optimum at every \(t>0\) is \(L_m^*(t)=e^{-t}\), obtained only at \(a=1\) (angles then play no role). Thus three is the smallest number of equal-precision Gaussian channels that improves the sharp large-disk exponential coverage rate below \(1\). For \(m=3\), the rate is \(\sqrt3/2\), the optimal squeeze is \(\sqrt3\), and the optimal prefactor is \(2/3\).

## Assumptions and scope

The Fourier convention is \(\widehat f(\omega)=\int_{\mathbb R}f(x)e^{-2\pi i\omega x}\,dx\). The normalized Gaussian \(g_a(x)=(2a)^{1/4}e^{-\pi ax^2}\) has ambiguity magnitude
\[
|\mathcal A g_a(X,\Omega)|^2=e^{-\pi(aX^2+a^{-1}\Omega^2)}.
\]
Rotations through fractional Fourier transforms, followed if necessary by a common quarter-turn, produce precisely \(e^{-\pi r^2q_a(\phi-\theta)}\). With equal independent channel-noise variances and a fixed total precision budget, \(m^{-1}\sum_j|\mathcal A g_{a,\theta_j}|^2\) is the squared norm of the normalized pointwise linear ambiguity-inversion multiplier. On the disk \(X^2+\Omega^2\leq R^2\), all the summands decrease radially and the minimum occurs on its boundary, with \(t=\pi R^2\). The theorem concerns this explicitly defined linear multiplier and does not assert global nonlinear phase-retrieval stability.

We optimize over a *common* Gaussian squeeze, arbitrary orientation angles (repetitions allowed), and equal channel precision. Each \(m\) is fixed while \(t\to\infty\). The angular and squeeze perturbation formula applies for fixed parameters \(u_j,v\), and any common rotation \(\theta_0\).

## Proof

**1. Angular geometry and global exponential bound.** Order the orientation axes cyclically on a circle of circumference \(\pi\). If \(g\) is the largest of the \(m\) consecutive gaps, then \(g\geq\pi/m\). At its midpoint, the circular geodesic distance to every axis is at least \(g/2\); two gap endpoints are at distance exactly \(g/2\). For \(a\geq1\), \(q_a(d)\) is increasing in the geodesic distance \(d\in[0,\pi/2]\). Therefore
\[
L_m(t;a,\Theta)\leq e^{-tq_a(g/2)}
\leq e^{-tq_a(\delta_m)}\leq e^{-ts_m}.
\]
The final inequality follows from
\(q_a(\delta_m)=a^{-1}\cos^2\delta_m+a\sin^2\delta_m\geq2\sin\delta_m\cos\delta_m=s_m\),
with equality precisely at \(a=a_m\). When \(m\geq3\), the inequality in the gap is strict unless \(g=\pi/m\) and \(a=a_m\).

**2. Equispaced lower construction and its exact prefactor.** Set \(a=a_m\), \(\theta_j=j\pi/m\). Each gap midpoint has exactly two nearest axes at distance \(\delta_m\), with all other axes at strictly greater distance. At each such midpoint the normalized sum equals
\[
\frac2m e^{-ts_m}(1+O_m(e^{-c_mt}))
\]
for a fixed \(c_m>0\). These midpoints are the asymptotic global minima. Indeed, away from their neighborhoods the nearest axis has \(q_{a_m}(d)<s_m-\epsilon\) for some positive \(\epsilon\), making the normalized sum exponentially larger than \(e^{-ts_m}\). In a neighborhood of any midpoint write \(\phi=\phi_{\rm mid}+z/t\). Taylor expansion for bounded \(z\), with \(b_m=q'_{a_m}(\delta_m)=2\cos(\pi/m)>0\), gives
\[
\frac1m\sum_j e^{-tq_{a_m}(\phi-\theta_j)}
=\frac2m e^{-ts_m}(\cosh(b_mz)+o(1)).
\]
If \(|z|\to\infty\) while \(\phi\to\phi_{\rm mid}\), one of the two terms dominates and grows relative to \(e^{-ts_m}\), so no smaller limiting value is possible. It follows that
\(L_m(t;a_m,(j\pi/m)_j)=(2/m+o(1))e^{-ts_m}\).

**3. Global optimal constant and rigidity.** A maximum exists for fixed \(t\): the orientations form a compact torus, and letting \(a\to\infty\) makes the value at the midpoint of a largest gap tend uniformly to zero (since \(g\geq\pi/m\)). Let \(a(t),\Theta(t)\) maximize. Combining Step 1 with Step 2 shows \(q_{a(t)}(g(t)/2)-s_m=O(1/t)\); hence \(a(t)\to a_m\) and \(g(t)\to\pi/m\). As the \(m\) gaps sum to \(\pi\), all gaps tend to \(\pi/m\). At the midpoint of any largest gap, exactly the two adjacent axes have limiting distance \(\delta_m\). Every other axis has a uniformly larger limiting distance, so its exponential contribution is negligible. Consequently
\[
L_m^*(t)\leq\frac2m e^{-tq_{a(t)}(g(t)/2)}(1+o(1))
\leq\frac2m e^{-ts_m}(1+o(1)).
\]
Together with Step 2 this proves the first displayed limit. In fact, the same inequalities now imply
\(t[q_{a(t)}(g(t)/2)-s_m]\to0\). Since \(q_a(d)\) has strictly positive \(d\)-derivative at \((a_m,\delta_m)\) and a strictly positive second \(a\)-derivative there, the separate nonnegative increments
\[
q_{a(t)}(g(t)/2)-q_{a(t)}(\delta_m),\qquad
q_{a(t)}(\delta_m)-s_m
\]
force \(t(g(t)-\pi/m)\to0\) and \(\sqrt t(a(t)-a_m)\to0\). Summing the gap deviations and using their maximum shows that *every* gap differs from \(\pi/m\) by \(o(t^{-1})\); cyclic integration proves the stated angular rigidity.

**4. Sharp perturbation law.** In the regime of the third display, the \(j\)-th gap has size \(\pi/m+(u_{j+1}-u_j)/t\). At its midpoint, a two-variable Taylor expansion gives
\[
tq_{a(t)}\!\left(\frac{\theta_{j+1}(t)-\theta_j(t)}2\right)
=ts_m+\cos(\pi/m)(u_{j+1}-u_j)
+\frac{\sin^3\delta_m}{\cos\delta_m}v^2+o(1).
\]
Here \(\partial_aq_{a_m}(\delta_m)=0\), \(\partial_dq_{a_m}(\delta_m)=2\cos(\pi/m)\), and \(\tfrac12\partial_a^2q_{a_m}(\delta_m)=\sin^3\delta_m/\cos\delta_m\). At an additional angular offset \(z/t\) from that midpoint, the two neighboring terms have limiting relative sum \(2\cosh(2\cos(\pi/m)z)\); all other terms are exponentially smaller. As in Step 2, compactness away from midpoints and nearest-axis domination for unbounded rescaled offsets show that all minima are captured by these local profiles. Minimizing each \(\cosh\) at zero, and then choosing the largest gap increment, proves the asserted perturbation formula.

**5. One and two channels.** For \(m\leq2\), the largest gap is at least \(\pi/2\) when \(m=2\) (and \(\pi\) when \(m=1\)). At its midpoint all distances are at least \(\pi/4\); thus \(q_a\geq(a+a^{-1})/2\geq1\) for \(m=2\), with strict inequality if \(a>1\). For \(m=1\), the opposite point has \(q_a=a\geq1\). The isotropic Gaussian \(a=1\) attains \(e^{-t}\) for either number of channels, establishing the exact claim.

## Verification

The stand-alone script `checks/gaussian_design_check.py` (Python standard library only) evaluates discrete-angle minima for equispaced and perturbed designs, confirms the asymptotic prefactors numerically for several \(m\), checks the one-/two-window identity, and verifies the elementary derivative and squeeze identities. It was executed from its delivered path and returned `PASS: 86 finite analytic-identity and numerical assertions.` These finite computations corroborate the formulas but do not establish any continuum minimax assertion; Steps 1–5 supply those proofs.

## Relationship to prior work

Alaifari and Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval* (arXiv:2410.05486, first posted 2024-10-07), Section 2.1 and Remark 2.1, introduce the rotated/dilated Gaussian construction, use equally spaced orientations, and calculate the threshold-ellipse intersection denominator \(a^{-1}\cos^2(\pi/(2m))+a\sin^2(\pi/(2m))\). That geometric formula yields the corresponding threshold-coverage exponential rate after minimizing in \(a\); it is therefore **not** claimed here as a novel standalone observation. The present statement instead optimizes the *sum of squared ambiguity magnitudes* over arbitrary orientation placement and common squeeze, identifies the sharp multiplicative factor \(2/m\), proves asymptotic optimizer rigidity at two distinct scales, and obtains the fully quantitative perturbation penalty. Those are distinct from the largest disk contained in a union of threshold ellipses or a positive *unsquared* ambiguity sum. The comparison is conditional on the specific equal-noise least-squares multiplier defined above.

Hardin, Kendall, and Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials* (arXiv:1208.5261, 2012), prove equally spaced optimality for nonincreasing *convex* geodesic-distance potentials. The potential here is \(e^{-tq_a(d)}\), which has negative second derivative at \(d=0\) for every \(a>1,t>0\), so the stated convexity hypothesis does not apply. The theorem therefore cannot be inferred directly from that polarization result. Existing general Gaussian ambiguity formulas justify the normalization and rotation model, not the asserted sum-of-squares global asymptotics and microscopic rigidity.

## Limitations

No claim is made about arbitrary window families, unequal channel weights, channel-dependent squeezing, noncircular regions, increasing \(m\), exact optimal orientations at finite \(t\) for \(m\geq3\), or nonlinear stability of recovering a signal from STFT magnitudes. The asymptotic \(o(\cdot)\) terms are for fixed \(m\); the local perturbation statement is for fixed real offsets. The uniqueness assertion for \(m=1,2\) concerns squeezing, not the irrelevant orientations at \(a=1\). Although targeted searches and primary-text comparisons found no covering quantitative theorem, unseen literature on Gaussian polarization or optimized multiwindow inversion remains a historical-priority risk.

## References

1. R. Alaifari and Y. Yang, *Multi-Window Approaches for Direct and Stable STFT Phase Retrieval*, arXiv:2410.05486 (first posted 2024-10-07), particularly Section 2.1, Remark 2.1 and equation (7). https://arxiv.org/abs/2410.05486
2. D. P. Hardin, A. P. Kendall and E. B. Saff, *Polarization optimality of equally spaced points on the circle for discrete potentials*, arXiv:1208.5261 (2012), Theorem 1. https://arxiv.org/abs/1208.5261
3. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser (2001), for the classical ambiguity/STFT normalization and identities; cited for background rather than novelty comparison.
