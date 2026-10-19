# Sharp dispersion envelope for biased periodic capture of Brownian motion

## Finding

A diffusing particle which is intermittently captured by a periodic lattice can acquire directed motion when capture basins are asymmetric. In the *instantaneous* Poisson-capture model defined below, its long-time effective diffusivity is a strictly increasing function of capture asymmetry at fixed bare diffusivity, period and capture rate. The sharp bounds, including all equality conditions, are

\[
\frac{z^2\cosh(z/2)}{4\sinh^2(z/2)}
\;\leq\;\frac{\mathcal D(\theta)}{D}
\;\leq\;\frac{z^2}{4}\coth^2(z/2),
\qquad z=L\sqrt{r/D}.
\]

The lower equality holds exactly at the nearest-site partition \(\theta=1/2\); the upper equality holds exactly at the two extreme directed partitions \(\theta\in\{0,1\}\). For every \(z>0\), \(\mathcal D(\theta)\) strictly increases with \(|\theta-1/2|\) from the lower endpoint to the upper endpoint.

An exact formula underlying the envelope is

\[
\frac{\mathcal D(\theta)}{D}=\frac{z^2}{2}
\left[b(z,\delta)+z\,m(z,\delta)\,\partial_zm(z,\delta)\right],
\]

where \(\delta=1/2-\theta\),

\[
m(z,\delta)=\frac{\sinh(\delta z)}{2\sinh(z/2)},\qquad
b(z,\delta)=\frac{\cosh(\delta z)\cosh(z/2)}{2\sinh^2(z/2)}.
\]

The drift is \(v=rLm(z,\delta)\), included for model identification rather than asserted as a new prior-independent result. In particular, \(\mathcal D(\theta)=\mathcal D(1-\theta)\), although the drift reverses.

## Assumptions and scope

Fix \(D,L,r>0\) and \(0\leq\theta\leq1\). From any lattice position \(jL\), the particle evolves as \(jL+\sqrt{2D}B_t\), for a standard Brownian motion \(B\), until an independent rate-\(r\) Poisson clock rings. At a clock event, a position belonging to the half-open interval

\[
[kL-(1-\theta)L,\,kL+\theta L)
\]

is instantaneously mapped to \(kL\). These intervals partition the line; boundaries have zero probability at a positive Poisson time, so boundary conventions do not affect the results. After every event the diffusion and the next exponential waiting time are independent of the preceding cycle. Start at the lattice origin. A reset that maps a particle to its current site is still a completed clock event.

For the resulting position \(X_t\), define the transport coefficients by

\[
v=\lim_{t\to\infty}\frac{\mathbb E X_t}{t},\qquad
\mathcal D=\lim_{t\to\infty}\frac{\operatorname{Var}(X_t)}{2t}.
\]

These limits exist and are finite for every fixed admissible parameter combination. The capture rule is deliberately different from nearest-site resetting unless \(\theta=1/2\). It represents an idealized instantaneous asymmetric ratchet, not a finite-duration return or particle dynamics in a continuously applied potential.

## Proof

**1. Independent renewal rewards.** Let \(T\) be an exponential waiting time of rate \(r\), independent of free Brownian motion, and \(Y=\sqrt{2D}B_T\). Its bilateral Laplace density is

\[
f_Y(y)=\frac{1}{2}\sqrt{r/D}\,e^{-\sqrt{r/D}\,|y|}.
\]

Write \(K\in\mathbb Z\) for the lattice-site index reached from the origin at the ensuing capture. For any integer \(j\geq1\), setting \(q=e^{-z}\), the geometric upper and lower tails are exactly

\[
\mathbb P(K\geq j)=\tfrac12e^{-z(\theta+j-1)},\qquad
\mathbb P(K\leq-j)=\tfrac12e^{-z(1-\theta+j-1)}.
\]

Consequently \(m=\mathbb EK\) and \(b=\mathbb EK^2\) are

\[
\begin{aligned}
m&=\frac{e^{-\theta z}-e^{-(1-\theta)z}}{2(1-e^{-z})}
=\frac{\sinh(\delta z)}{2\sinh(z/2)},\\
b&=\frac{(e^{-\theta z}+e^{-(1-\theta)z})(1+e^{-z})}{2(1-e^{-z})^2}
=\frac{\cosh(\delta z)\cosh(z/2)}{2\sinh^2(z/2)}.
\end{aligned}
\]

At the consecutive capture times, the pairs of rewards \((T_i,LK_i)\) are independent and identically distributed with finite moments of every order. Standard renewal-reward mean and central-limit calculations give

\[
v=\frac{L\mathbb EK}{\mathbb ET}=rLm,
\qquad
\mathcal D=\frac{\mathbb E[(LK-vT)^2]}{2\mathbb ET}
=\frac r2\mathbb E[(LK-vT)^2].
\]

To see directly why the continuous-position process has the same coefficients as the completed cycles: its difference from the sum of completed rewards is the displacement in the unfinished Brownian excursion. The age since the most recent Poisson event is stochastically bounded by an exponential time, uniformly in observation time; the excursion has uniformly bounded second moment. Its mean is bounded and its covariance with the completed reward sum is at most \(O(\sqrt t)\) by Cauchy–Schwarz, so neither linear-time coefficient changes.

**2. Time–displacement correlation.** The reward \(K\) and its cycle length \(T\) are *not* independent. Differentiating the absolutely convergent mixture identity

\[
m(r)=r\int_0^\infty e^{-rt}\,\mathbb E[K\mid T=t]\,dt
\]

with \(D,L,\theta\) fixed yields

\[
\mathbb E[TK]=\frac mr-\partial_rm.
\]

Since \(\mathbb ET^2=2/r^2\), expanding the centered cycle reward gives

\[
\mathbb E[(LK-vT)^2]
=L^2\bigl(b+2r\,m\,\partial_rm\bigr)
=L^2\bigl(b+z\,m\,\partial_zm\bigr).
\]

This proves the asserted exact diffusivity formula, including the covariance correction often missed by approximating the process by a compound Poisson walk.

**3. Strict sharp comparison.** Put \(a=z/2>0\), \(w=|\delta|z\in[0,a]\), \(S=\sinh a\) and \(C=\cosh a\). Direct substitution in the formula above gives

\[
R(a,w):=\frac{\mathcal D}{D}
=\frac{a^2}{S^2}\left[
C\cosh w+\frac w2\sinh w\cosh w
-\frac{aC}{2S}\sinh^2w\right].
\]

For \(0<w\le a\), differentiating and dividing by the positive factor \((a^2/S^2)\sinh w\cosh w\) gives

\[
\frac{S^2\,\partial_wR}{a^2\sinh w\cosh w}
=\frac{C}{\cosh w}+w\coth(2w)+\frac12-a\coth a.
\]

Define \(h(s)=s\coth s\) for \(s>0\). The elementary strict inequalities

\[
0<h'(s)=\frac{\sinh s\cosh s-s}{\sinh^2s}<\tanh s
\]

follow from \(\sinh s\cosh s>s\) and \(s\cosh s>\sinh s\). For \(0<w\le a\), integrating the second inequality shows

\[
h(a)-h(w)\le\log\frac{\cosh a}{\cosh w}
\le\frac{\cosh a}{\cosh w}-1,
\]

with the first comparison strict when \(w<a\). On the other hand,

\[
w\coth(2w)+\frac12-h(w)
=\frac12-\frac{w}{\sinh(2w)}>0
\]

for every \(w>0\). Inserting these relations into the derivative formula proves \(\partial_wR>0\) throughout \((0,a]\). Continuity at \(w=0\) proves strict increase across the entire interval \([0,a]\). The exact endpoint evaluations are

\[
R(a,0)=\frac{a^2\cosh a}{\sinh^2a},\qquad
R(a,a)=a^2\coth^2a.
\]

These yield the sharp envelope and all equality conditions because \(w=0\) is equivalent to \(\theta=1/2\), while \(w=a\) is equivalent to \(\theta\in\{0,1\}\).

**4. Distinct strong-capture regimes.** Taylor expansion at \(z=0\), uniform for \(|\delta|\le1/2\), gives

\[
\frac{\mathcal D}{D}=1+
\left(\frac1{24}+\frac{\delta^2}{2}\right)z^2+O(z^4).
\]

For any fixed interior \(0<\theta<1\), the geometric-tail expressions for \(m\) and \(b\) imply \(\mathcal D/D\to0\) as \(z\to\infty\): both terms are exponentially small up to polynomial prefactors. At either extreme \(\theta=0\) or \(1\), the exact upper expression instead satisfies \(\mathcal D/D\sim z^2/4\to\infty\). Thus sufficiently weak capture enhances dispersion relative to bare Brownian motion for every fixed gate, but sufficiently strong capture suppresses it for every fixed strictly interior gate. No uniqueness of the intermediate crossing is asserted.

## Verification

The accompanying standalone `check_dispersion.py` computes the Laplace-tail moments in two algebraically distinct forms, differentiates the first moment independently at high precision, checks the strict sharp envelope across the complete parameter boundary using sampled values, tests the weak- and strong-rate limits, and uses independently simulated exponential-cycle durations and Brownian rewards to check the speed and covariance-corrected diffusivity. The actual run passed 246 assertions. This finite program is diagnostic evidence; the global inequalities and all parameter quantifiers follow from the proof above. Run with Python 3, NumPy and mpmath: `python check_dispersion.py`.

## Relationship to prior work

Ghosh et al. introduced directed transport from position resetting into asymmetric periodic potential wells [1], motivating the ideal instantaneous capture model. Roberts, Sezik and Lardet studied a switching ratchet with a free-diffusion phase and gave exact stationary currents and efficiency [2]; its current formula (and equivalent first-reward formulas) is prior work, not the new assertion here. Alston and Bertrand obtained a diffusion coefficient for symmetric nearest-site resetting and an optimization over the *positions* of sites [3]. Their nearest-site result agrees with the \(\theta=1/2\) lower endpoint; shifting a capture boundary while fixing the same periodic lattice leaves their nearest-site setting. The new result is the full *bias-dependent* dispersion, its time–displacement covariance term, and the strict sharp envelope across all capture gates.

The renewal-reward central-limit theorem and geometric tail summation are standard inputs. General results for periodically driven Brownian ratchets [4] concern tilted potentials and different generators, not this discrete instantaneous capture rule. The present assessment did not identify a published assertion implying this exact one-parameter envelope, but such a result might exist within broader renewal or resetting literature.

## Limitations

The model assumes instantaneous capture, an independent exponential clock, Brownian free phases, one-dimensional equal-spacing lattice points, and spatially identical capture gates. There is no statement for finite-speed ratchet relaxation, position-dependent clocks, arbitrary nonuniform resetting sites, or a general stationary density on the line (the process is transporting). Strong-capture limits for gate endpoints are singular relative to limits with a fixed strictly positive basin on both sides of every site. The dispersive envelope does not imply uniqueness of the rate at which effective diffusivity crosses the bare value. A general originality priority claim is not established beyond the inspected literature.

## References

1. P. K. Ghosh, S. Nayak, J. Liu, Y. Li, F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting*, arXiv:2307.06202v1 (first posted 12 July 2023), https://arxiv.org/abs/2307.06202.
2. C. Roberts, E. Sezik, E. Lardet, *Ratchet-mediated resetting: current, efficiency, and exact solution*, arXiv:2405.10698v1 (17 May 2024), https://arxiv.org/abs/2405.10698.
3. H. Alston, T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1 (23 January 2024), https://arxiv.org/abs/2401.12772.
4. P. Reimann et al., *Diffusion in tilted periodic potentials: Enhancement, universality, and scaling*, Physical Review E 65, 031104 (2002), https://doi.org/10.1103/PhysRevE.65.031104.
