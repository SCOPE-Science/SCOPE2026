# Curvature restores Gaussian diffusion in heavy-tailed renewal swimmers

## Finding
A chiral swimmer with independent uniform heading resets and finite-mean renewal intervals has an exact Gaussian functional scaling limit at every fixed nonzero angular speed, even if the interval distribution has infinite variance. In the heavy-tailed Pareto-II family the effective diffusivity diverges with an explicit noninteger power as angular speed approaches zero, whereas the zero-curvature trajectory has superlinear mean-squared displacement.

The path is not reset at reorientation events. The particle simply changes heading and continues moving.

For every fixed \(\omega\ne0\),
\[
\frac{X(T\cdot)}{\sqrt T}\ \Longrightarrow\ \sqrt{2D(\omega)}B(\cdot),\qquad
D(\omega)=\frac{v^2}{2\mu\omega^2}\mathbb E[1-\cos(\omega L)],
\]
where \(B\) is standard planar Brownian motion and \(D\) is the per-coordinate diffusion coefficient. The limiting Brownian motion is degenerate if \(\omega L\in2\pi\mathbb Z\) almost surely; in that case each complete circular flight has zero displacement.

For \(\mathbb P(L>s)=(1+s/\ell)^{-\alpha}\), \(1<\alpha<2\), the diffusivity is strictly positive at each nonzero angular speed and
\[
D(\omega)\sim\frac{v^2\ell^{\alpha-1}}2\Gamma(2-\alpha)
\left[-\cos\left(\frac{\pi\alpha}{2}\right)\right]
|\omega|^{\alpha-2}\qquad (\omega\to0).
\]
In contrast, at exactly \(\omega=0\),
\[
\mathbb E|X(t)|^2\sim
\frac{2v^2\ell^{\alpha-1}}{(2-\alpha)(3-\alpha)}t^{3-\alpha}.
\]

## Assumptions and scope
Let \(v>0\) and let \(L_1,L_2,\ldots\) be iid strictly positive flight durations satisfying \(0<\mu=\mathbb E L<\infty\). At the beginning of each new flight choose a heading \(\Theta_j\), independently and uniformly on \([0,2\pi)\); these headings are independent of all flight durations. Within flight \(j\), whose starting time is \(S_j\), the complex-valued position derivative is
\[
\dot X(t)=v\exp\{i[\Theta_j+\omega(t-S_j)]\},\qquad S_j\le t<S_j+L_j.
\]
The position is continuous at each renewal. There is no rotational Brownian noise. To state the exact two-time correlation and mean-square identity without initial transients, sample the initial flight from the equilibrium length-biased distribution, place time zero uniformly within that flight, and choose its heading uniformly. All future renewal cycles follow the iid prescription. We set \(X(0)=0\). This equilibrium construction exists for every finite \(\mu\), including when \(\mathbb E L^2=\infty\).

Here and below \(L\) is a generic fresh renewal interval, not the equilibrium length-biased interval, and convergence of processes is in the topology of uniform convergence on compact time intervals.

## Proof
**1. Bounded geometric increments.** For \(\omega\ne0\), a complete renewal flight has complex displacement
\[
Y_j=\frac{v e^{i\Theta_j}}{i\omega}\big(e^{i\omega L_j}-1\big),
\qquad |Y_j|\le\frac{2v}{|\omega|}.
\]
The increments are iid, centered by the independent uniform headings. Rotational symmetry and \(|e^{it}-1|^2=2(1-\cos t)\) give
\[
\operatorname{Cov}(Y_j)=\frac{v^2}{\omega^2}\mathbb E[1-\cos(\omega L)]I_2.
\]
This covariance is finite regardless of the second moment of \(L\).

**2. Functional Gaussian limit.** The iid vector-increment invariance principle yields Brownian motion when complete flights are indexed by their count. The renewal strong law gives \(N(Ts)/T\to s/\mu\), uniformly for \(s\) in compact intervals, in probability. The time-change theorem applies even though \(L_j\) and \(Y_j\) are dependent, because the limiting time change is deterministic. The initial equilibrium residual arc and every unfinished arc have displacement magnitude at most \(2v/|\omega|\); their \(T^{-1/2}\)-scaled contributions are uniformly negligible. Hence the path has the stated functional Gaussian limit with covariance rate \(\operatorname{Cov}(Y_1)/\mu=2D(\omega)I_2\). If this covariance is zero the same argument gives the zero process.

**3. Exact stationary mean square.** Let \(R(s)=\mathbb E[(L-s)_+]/\mu\) denote the equilibrium probability that no renewal occurs during an interval of length \(s\). Two velocities separated by \(s\) share their heading only in the absence of a renewal. If a renewal occurs, the later heading is independent and uniform. Thus
\[
C_\omega(s):=\mathbb E[\dot X(0)\cdot\dot X(s)]
=v^2R(s)\cos(\omega s),
\]
where the dot is the Euclidean scalar product, and exactly for all \(t\ge0\),
\[
\mathbb E|X(t)|^2=2v^2\int_0^t(t-s)R(s)\cos(\omega s)\,ds.
\]
Since \(R\) decreases to zero, its cosine transform converges as an improper integral at nonzero \(\omega\) (Dirichlet's test). Integration by parts using \(R'(s)=-\mathbb P(L>s)/\mu\) almost everywhere, followed by the elementary characteristic-function identity, gives
\[
\int_0^\infty R(s)\cos(\omega s)\,ds
=\frac{\mathbb E[1-\cos(\omega L)]}{\mu\omega^2}.
\]
Cesàro convergence applied to the time-integrated correlation proves \(\mathbb E|X(t)|^2/t\to4D(\omega)\), including the degenerate case.

**4. The Pareto-II singularity.** Take \(\mathbb P(L>s)=(1+s/\ell)^{-\alpha}\) with \(\ell>0\) and \(1<\alpha<2\). Then \(\mu=\ell/(\alpha-1)\) and its continuous density is \(\alpha\ell^\alpha(s+\ell)^{-1-\alpha}\). By the substitution \(y=|\omega|s\),
\[
\frac{\mathbb E[1-\cos(\omega L)]}{|\omega|^\alpha}
=\alpha\ell^\alpha\int_0^\infty\frac{1-\cos y}{(y+\ell|\omega|)^{1+\alpha}}\,dy.
\]
The integrand is dominated by \((1-\cos y)y^{-1-\alpha}\), which is integrable for \(0<\alpha<2\). Dominated convergence and the classical cosine integral
\[
\alpha\int_0^\infty(1-\cos y)y^{-1-\alpha}\,dy
=\Gamma(1-\alpha)\cos(\pi\alpha/2)
\]
prove the stated asymptotic using \(\Gamma(2-\alpha)=(1-\alpha)\Gamma(1-\alpha)\). The coefficient is strictly positive. A continuous interval law cannot satisfy \(\omega L\in2\pi\mathbb Z\) almost surely, establishing strict positivity of \(D(\omega)\).

**5. Exactly zero curvature.** Here the equilibrium survival is explicit:
\[
R(s)=(1+s/\ell)^{1-\alpha}.
\]
Using the exact covariance identity at \(\omega=0\), substitute \(s=tu\) and apply dominated convergence to obtain
\[
\lim_{t\to\infty}\frac{\mathbb E|X(t)|^2}{t^{3-\alpha}}
=2v^2\ell^{\alpha-1}\int_0^1(1-u)u^{1-\alpha}\,du
=\frac{2v^2\ell^{\alpha-1}}{(2-\alpha)(3-\alpha)}.
\]
This exponent is strictly greater than one. The result makes no assertion of a Gaussian limit at zero curvature.

## Verification
The accompanying `checks/verify.py` is a standalone finite numerical test suite using NumPy, SciPy and mpmath. It compares a high-precision characteristic-function representation with the small-frequency asymptotic, the exact zero-curvature mean-square integral with its elementary antiderivative and large-time asymptotic, and iid complete-flight simulation moments with the exact renewal coefficient. It also checks the closed-circle degeneracy. These finite checks support the algebra but do not replace the functional limit proof or the infinite-time asymptotics. Run: `python checks/verify.py`.

## Relationship to prior work
Olsen and Löwen (arXiv:2405.14326) analyze chiral active motion under constant-rate Poisson reorientations, including exact angular correlations and optimal diffusion strategies. The present renewal law allows infinitely variable, non-Poisson flight durations, and isolates the crossover from superdiffusion to a Gaussian functional limit when a small deterministic curvature is introduced. Classical straight Lévy-walk limit theorems establish the uncurved anomalous regime; those results do not have bounded complete-flight displacements under nonzero curvature. Rutenberg, Richardson and Montgomery analyze diffusion with stochastic curvature fluctuations, not independently reset full-circle arcs with infinite-variance flight durations. Tromer and collaborators investigate detection of Lévy patterns in curved trajectories, with a different noisy-curvature mechanism. Raghavendra and collaborators experimentally program straight heavy-tailed flights and circular swimming as separate modes; neither their measurements nor the cited chiral Poisson model give this combined singular-limit classification.

The iid regenerative invariance principle and the cosine-transform identity are established tools; no novelty is claimed for those general techniques. The assessed contribution is their sharp combination for this specific continuous chiral motion, including its exact diffusivity and heavy-tail singular coefficient.

## Limitations
The reorientation is an independent complete angular refresh and renewal times have finite mean. The result does not include correlated headings, rotational diffusion within flights, random angular speeds, position resets, or infinite-mean intervals. The Gaussian scaling is for every *fixed* nonzero angular speed before the long-time limit; no joint \(t\)- versus \(\omega\)-crossover limit is established. The diffusion can be degenerate for specially supported noncontinuous flight-duration laws. The claimed originality has not been verified against all possible prior publications, and no independent scientific audit has been performed.

## References
1. K. Stølevik Olsen and H. Löwen, *Optimal diffusion of chiral active particles with strategic reorientations*, arXiv:2405.14326v1 (first posted 23 May 2024), https://arxiv.org/abs/2405.14326 .
2. M. Magdziarz and collaborators, *Limit theorems and governing equations for Lévy walks*, *Stochastic Processes and their Applications* (2015), https://doi.org/10.1016/j.spa.2015.05.014 .
3. A. D. Rutenberg, A. J. Richardson, C. J. Montgomery, *Diffusion of Asymmetric Swimmers*, arXiv:cond-mat/0302387 (2003), https://arxiv.org/abs/cond-mat/0302387 .
4. R. M. Tromer and collaborators, *Inferring Lévy walks from curved trajectories: A rescaling method*, *Physical Review E* 92, 022147 (2015), https://doi.org/10.1103/PhysRevE.92.022147 .
5. T. S. Raghavendra and collaborators, *Programmable persistent random walks in active Brownian particles govern emergent dynamics*, *Communications Physics* 9, 166 (2026), https://doi.org/10.1038/s42005-026-02596-6 .
