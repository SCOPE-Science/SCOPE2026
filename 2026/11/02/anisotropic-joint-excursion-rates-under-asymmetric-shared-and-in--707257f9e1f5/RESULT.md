# Anisotropic joint-excursion rates under asymmetric shared and individual Brownian resetting

## Finding

Consider two independently diffusing one-dimensional coordinates exposed to three independent Poisson reset streams: one resets only the first coordinate, another resets only the second, and a third resets both simultaneously. **For arbitrary strictly positive and unequal individual resetting rates**, their stationary simultaneous large-displacement probability has an exact three-sector exponential rate. Two angular boundaries distinguish a shared-age fluctuation from fluctuations assisted by the unshared age of one coordinate. The rate is continuously differentiable but has a jump in angular second derivatives at each boundary.

In particular, fixing both single-coordinate resetting rates and increasing the rate of the shared stream strictly increases the probability of sufficiently extreme simultaneous excursions at the exponential scale, although both stationary one-coordinate distributions remain exactly unchanged. The shared rate is uniquely identifiable from any one strictly positive directional joint-tail exponent when the marginal resetting rates are known.

**Theorem.** Let \(a,b,c,D_1,D_2>0\), with \(a\ne b\), and put
\[
 A=a+c,\qquad B=b+c,\qquad \Lambda=a+b+c=A+B-c.
\]
Let \((X,Y)\) have the stationary distribution defined below, and normalize its coordinates as
\[
 U=\sqrt{A/D_1}\,X,\qquad V=\sqrt{B/D_2}\,Y.
\]
For every \(x,y>0\),
\[
 \lim_{t\to\infty}-\frac1t\log\Pr\{U>tx,\,V>ty\}=I(x,y),
\]
where
\[
 I(x,y)=
 \begin{cases}
  y+x\sqrt{a/A},&\displaystyle\frac{x}{y}\le\frac{\sqrt{Aa}}{B},\\[6pt]
  \sqrt{\Lambda\left(\frac{x^2}{A}+\frac{y^2}{B}\right)},&\displaystyle\frac{\sqrt{Aa}}{B}<\frac{x}{y}<\frac{A}{\sqrt{Bb}},\\[9pt]
  x+y\sqrt{b/B},&\displaystyle\frac{x}{y}\ge\frac{A}{\sqrt{Bb}}.
 \end{cases}
\]
The two transition rays are distinct because \(AB>ab\). The formulas agree with matching first derivatives across both rays. Across either ray a transverse second derivative changes discontinuously, so \(I\) is \(C^1\) on the positive quadrant but not \(C^2\) at either transition ray.

Fix distinct positive marginal resetting rates \(A,B\). For \(0<c<\min(A,B)\), set \(a=A-c\) and \(b=B-c\), and write the corresponding rate as \(I_c\). Then for any \(x,y>0\) and any \(0<c_1<c_2<\min(A,B)\),
\[
 I_{c_2}(x,y)<I_{c_1}(x,y).
\]
Consequently the map \(c\mapsto I_c(x,y)\) is continuous and strictly decreasing. It identifies the shared resetting rate from the directional exponent, given \(A,B\).

For every allowed rate choice, both \(U\) and \(V\) have the standard centered Laplace law with density \(\frac12e^{-|u|}\), and \(\mathbb E[UV]=0\). Nevertheless,
\[
 \operatorname{Cov}(U^2,V^2)=\frac{4c}{\Lambda}>0.
\]
Furthermore \(I(1,1)>1\), so the upper-tail dependence coefficient is zero even though the centered squared-coordinate covariance is positive. In the special **symmetric benchmark** \(A=B=\mu\), already within the scope of earlier uniform batch-resetting results, the diagonal exponent reduces to \(\sqrt{4-2c/\mu}\). This symmetric benchmark is a consistency check, not the assessed asymmetric contribution.

## Assumptions and scope

Take independent two-sided standard Wiener processes \(W_1,W_2\). Between resets the coordinates solve
\[
 dX_t=\sqrt{2D_1}\,dW_{1,t},\qquad dY_t=\sqrt{2D_2}\,dW_{2,t}.
\]
Three independent homogeneous Poisson point processes with intensities \(a\), \(b\), and \(c\) enact, respectively, the instantaneous maps
\[
 (X,Y)\mapsto(0,Y),\quad (X,Y)\mapsto(X,0),\quad (X,Y)\mapsto(0,0).
\]
All rates and diffusion constants are strictly positive. Resets occur independently of the Brownian motions and of the current positions. There are no interactions, drift, observation noise, or random reset locations. The novelty assessment pertains to the genuinely asymmetric subfamily \(a\ne b\); formulas at equality are given for comparison with published symmetric protocols.

The claim concerns the stationary distribution and logarithmic (speed-\(t\)) asymptotics at fixed positive thresholds \(x,y\). It does not claim an exact nonasymptotic exceedance probability, a polynomial prefactor, or a uniform asymptotic across vanishing angles or parameter boundaries.

## Proof

### 1. Stationarity, unique law, and its positive mixture

Every first coordinate is reset by a Poisson clock of rate \(A=a+c\), and every second coordinate by a Poisson clock of rate \(B=b+c\). A stationary realization is obtained using two-sided Poisson clocks and Brownian increments since the last reset of each coordinate. Each last reset is almost surely at finite backward distance. Two coupled trajectories sharing all future Brownian increments and all future resetting streams coalesce after each coordinate has experienced a reset; therefore the stationary law is unique.

Write \(\Phi(k,l)=\mathbb E\exp(i kU+i lV)\). The generator acting on the Fourier observable, followed by stationarity, gives
\[
 (\Lambda+A k^2+B l^2)\Phi(k,l)
 =c+a\Phi(0,l)+b\Phi(k,0).
\]
Each normalized marginal is a standard Laplace variable, so \(\Phi(k,0)=(1+k^2)^{-1}\) and \(\Phi(0,l)=(1+l^2)^{-1}\). Therefore
\[
 \boxed{\displaystyle
 \Phi(k,l)=\frac{c+a/(1+l^2)+b/(1+k^2)}{\Lambda+A k^2+B l^2}.}
\]

This identity has an important positive probabilistic decomposition. Let \(T\) be exponential with rate \(\Lambda\), let \(G_1,G_2\) be independent standard Gaussians, and put
\[
 H=\left(\sqrt{2AT}\,G_1,\sqrt{2BT}\,G_2\right).
\]
Let \(L_1,L_2\) be independent standard Laplace variables, independent of \(H\). Independently choose one of the following alternatives:
\[
 (U,V)\ \stackrel{d}{=}\
 \begin{cases}
  H,&\text{probability }c/\Lambda,\\
  H+(0,L_2),&\text{probability }a/\Lambda,\\
  H+(L_1,0),&\text{probability }b/\Lambda.
 \end{cases}
\]
Indeed the three characteristic functions have exactly the numerator above after division by \(\Lambda\). The representation can also be obtained by conditioning on the most recent event affecting either coordinate: after a single-coordinate reset, the surviving coordinate retains its stationary Laplace law while both coordinates accumulate independent Brownian increments until observation.

### 2. Large deviations of the three mixture components

The density of \(H\) is
\[
 f_H(u,v)=\frac{\Lambda}{2\pi\sqrt{AB}}
 K_0\!\left(\sqrt{\Lambda\left(\frac{u^2}{A}+\frac{v^2}{B}\right)}\right),
\]
where \(K_0\) is the modified Bessel function. The classical asymptotic \(K_0(z)\sim\sqrt{\pi/(2z)}e^{-z}\), combined with exponential tightness, yields a large-deviation principle for \(H/t\) at speed \(t\), with good rate
\[
 J_0(u,v)=\sqrt{\Lambda\left(\frac{u^2}{A}+\frac{v^2}{B}\right)}.
\]
An alternative verification integrates over the exponentially distributed age \(T\): the exponent for producing \((tu,tv)\) at an age \(ts\) is
\[
 \Lambda s+\frac{u^2/A+v^2/B}{4s},\qquad s>0,
\]
whose minimum is precisely \(J_0(u,v)\). The centered Gaussian conditional laws provide local lower bounds, and the transform domain provides exponential tightness.

Independently, \(L_i/t\) satisfies a good speed-\(t\) large-deviation principle with rate \(|z|\). By independence and contraction, the two convolution components have rates
\[
 J_x(u,v)=\inf_{z\in\mathbb R}\left\{|z|+J_0(u-z,v)\right\},\qquad
 J_y(u,v)=\inf_{z\in\mathbb R}\left\{|z|+J_0(u,v-z)\right\}.
\]
As all three mixture probabilities are strictly positive and independent of \(t\), the stationary scaled vector \((U/t,V/t)\) has good rate
\[
 J(u,v)=\min\{J_0(u,v),J_x(u,v),J_y(u,v)\}.
\]
The minimum is appropriate here because the *actual law is a positive finite mixture*, not because of a general claim that the support function of every mixed moment-generating-function domain gives the exact large-deviation rate.

### 3. Minimization and the angular transitions

For \(u,v>0\), the minimizing shift in \(J_x(u,v)\) lies in \([0,u]\); outside that interval the absolute-shift cost and the radial cost cannot improve. Define
\[
 g_x(z)=z+\sqrt{\Lambda\left(\frac{(u-z)^2}{A}+\frac{v^2}{B}\right)},\qquad 0\le z\le u.
\]
This function is convex. Its derivative at zero is negative exactly when
\[
 u>\frac{A}{\sqrt{Bb}}\,v,
\]
using \(\Lambda-A=b\). When this happens, its unique minimizer is
\[
 z_x=u-\frac{A}{\sqrt{Bb}}\,v,
\]
and substitution gives \(J_x(u,v)=u+v\sqrt{b/B}\). Otherwise \(J_x=J_0\). Similarly, using \(\Lambda-B=a\),
\[
 J_y(u,v)=
 \begin{cases}
 v+u\sqrt{a/A},&v>Bu/\sqrt{Aa},\\
 J_0(u,v),&v\le Bu/\sqrt{Aa}.
 \end{cases}
\]
The two strict-improvement regions cannot overlap because \(AB>ab\). Taking the minimum of the three component rates gives exactly the claimed three-sector expression for \(I\).

Each branch is strictly increasing in both positive coordinates; thus the infimum of \(J\) over \(\{u\ge x,v\ge y\}\) occurs at \((x,y)\). The same infimum holds over the open quadrant by continuity. The large-deviation lower and upper bounds therefore coincide and prove the asserted probability limit.

At the right-hand sector boundary \(u=Av/\sqrt{Bb}\), both formulas have gradient \((1,\sqrt{b/B})\). But the second \(u\)-derivative of the central branch is
\[
 \frac{\sqrt\Lambda\,v^2}{AB\big(u^2/A+v^2/B\big)^{3/2}}>0,
\]
while it vanishes identically in the outer affine branch. The left boundary has the analogous property with the roles of \(u,v\) interchanged. Hence \(I\) is \(C^1\) but not \(C^2\) on either positive transition ray.

### 4. Strict common-reset ordering at fixed marginals

With \(A,B\) fixed, the positive-quadrant rate can equivalently be written
\[
 I_c(x,y)=\max\left\{sx+ty:\ 0\le s,t\le1,\quad As^2+Bt^2\le A+B-c\right\}.
\]
This representation follows either by maximizing on the elliptical arc and its two box intersections, which reproduces the three branches, or by the elementary Lagrange-multiplier conditions.

For \(0<c_1<c_2<\min(A,B)\), the feasible region for \(c_2\) is a strict subset of that for \(c_1\). Its unique maximizing point for \(x,y>0\) lies on the ellipse and has at least one coordinate strictly below one. The less restrictive ellipse for \(c_1\) allows that coordinate to increase slightly, while respecting both box constraints. Because \(x,y>0\), this strictly raises the linear objective. Thus \(I_{c_1}(x,y)>I_{c_2}(x,y)\). Compactness also yields continuity in \(c\), proving one-exponent identification of \(c\) once \(A,B\) are known.

Finally, stationary generator moment equations give \(\mathbb E U^2=\mathbb E V^2=2\) and
\[
 0=2A\mathbb E V^2+2B\mathbb E U^2-\Lambda\mathbb E(U^2V^2),
\]
so \(\mathbb E(U^2V^2)=4(A+B)/\Lambda\) and \(\operatorname{Cov}(U^2,V^2)=4c/\Lambda\). Brownian sign symmetry gives \(\mathbb E UV=0\). Since every directional rate exceeds the marginal rate for positive thresholds, \(\Pr(V>t\mid U>t)\) tends to zero exponentially. This finishes the proof.

## Verification

The included standard-library Python program `verify_shared_reset_tails.py` uses exact rational arithmetic to check the stationary generator identity, marginal transforms and positive-mixture transform, then compares the closed-form sector rates to *independent golden-section minimizations* of the infimal-convolution costs across a broad deterministic parameter grid. It also checks strict fixed-marginal shared-reset ordering, the symmetric limiting benchmark, and the original uniform-batch two-point transform as a covered specialization.

Running `python3 verify_shared_reset_tails.py` passed **7,784 assertions**. These finite checks test algebraic identities and representative parameter settings; the proof above, not the finite tests, supports the all-parameter and infinite-threshold claims. No external library or internet access is needed to run the checker.

## Relationship to prior work

De Mauro, Majumdar and Schehr (2026), arXiv:2601.20077, introduce uniformly selected fixed-size batch resetting and establish an exact two-particle Fourier transform and joint density for that model (main equation (5), Supplement S3 equation (S36)). At the level of two selected particles, their Poisson-thinning model has *equal* rates \(a=b\). In fact, for their batch rate \(r\), group size \(m\) and number of particles \(N\), the pairwise rates are
\[
 a=b=\frac{r m(N-m)}{N(N-1)},\qquad
 c=\frac{r m(m-1)}{N(N-1)}.
\]
The resulting symmetric normalized Fourier transform is precisely their formula. **That entire symmetric subclass is covered prior work and is not claimed as new here.** The present result addresses independently chosen, genuinely unequal individual rates, sharp angular rare-event sectors, and strict identification of a common reset rate at fixed unequal marginals; these results are not supplied by their uniform-subset formula.

Opitz (2015), arXiv:1507.02537, analyzes asymptotic independence and residual extremes for *elliptical multivariate Laplace* vectors, including the purely shared-age Gaussian-exponential mixture. The present distribution with both distinct individual reset streams is a nonelliptical positive mixture of that Laplace vector and coordinatewise Laplace convolutions. The nonelliptical angular transitions and fixed-marginal shared-rate ordering do not follow as special cases of the quoted elliptical result.

De Mauro, Biroli, Majumdar and Schehr (2025), arXiv:2509.06658, analyze particles reset *fully simultaneously* under general renewal intervals; their fully simultaneous protocol differs from the mixed local/shared streams used here. Relevant earlier work on unequal exclusion probabilities for simultaneous near-complete batches obtains finite mixed cumulants, whereas the claim here is a logarithmic joint-excursion rate over all positive rays; finite cumulants do not fix it. Earlier stable-flight batch extreme asymptotics concern strictly non-Gaussian stable indices and algebraic rather than exponential tails.

## Limitations

This theorem concerns two independent Brownian free motions with constant local and common Poisson intensities, complete reset to zero, positive rates, and a stationary law. It provides logarithmic tail rates, not polynomial prefactors, finite-threshold precision, or statistical confidence intervals for rate estimators. It does not establish a pathwise stochastic order of excursions as the common resetting rate varies, nor a finite-threshold probability ordering. The exact formulas at equal individual rates are a published symmetric specialization; the assessed scientific contribution is the genuinely asymmetric angular law and strict fixed-marginal ordering.

The literature comparison uses accessible primary sources and mathematical research-index searches. The cited 2025 simultaneous-renewal work was available through bibliographic material but its complete manuscript was not examined, leaving a bounded residual priority risk. More general unpublished common-shock or renewal results might subsume parts of the theorem. No independent audit or literature-wide priority certification has been performed.

## References

1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077, first posted 2026-01-27, https://arxiv.org/abs/2601.20077 ; accessible full text https://arxiv.org/html/2601.20077 .
2. T. Opitz, *Modeling asymptotically independent spatial extremes based on Laplace random fields*, arXiv:1507.02537, first posted 2015-07-09, https://arxiv.org/abs/1507.02537 .
3. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, first posted 2025-09-08, https://arxiv.org/abs/2509.06658 .
4. N. Nolde, *Geometric interpretation of the residual dependence coefficient*, Journal of Multivariate Analysis 123 (2014), 85–95, https://doi.org/10.1016/j.jmva.2013.08.018 .
