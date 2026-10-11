# Stationary-marginal identifiability of both parameters in the Ricker map
## Finding
Consider the deterministic Ricker map
\[
F_{r,K}(x)=x\exp\!\left(r\left(1-\frac{x}{K}\right)\right),
\qquad r>0,\quad K>0.
\]
Let \(\mu\) be an \(F_{r,K}\)-invariant Borel probability measure whose support is a compact subset of \((0,\infty)\), and let \(X(x)=x\).

Then the carrying-capacity parameter is exactly the stationary mean,
\[
K=\mathbb E_\mu[X].
\]
If \(\mu\) is not a point mass, the growth parameter is also determined by the same one-time marginal:
\[
r=
\frac{2\,\mathbb E_\mu[X]\,\operatorname{Cov}_\mu(\log X,X)}
{\operatorname{Var}_\mu(X)}.
\]
Equivalently,
\[
2K\,\operatorname{Cov}_\mu(\log X,X)
=
r\,\operatorname{Var}_\mu(X).
\]
Thus every non-equilibrium compact positive invariant law identifies both deterministic Ricker parameters without using lagged pairs. The exceptional stationary law \(\delta_K\) identifies \(K\) but cannot identify \(r\), because every \(r>0\) fixes \(K\). A non-Dirac law must also assign positive mass to each of \(X<K\) and \(X>K\).

## Assumptions and scope
The state space used here is the strictly positive half-line. Compact support means that there are finite constants \(0<m<M<\infty\) with \(m\le X\le M\) on the support. This makes \(\log X\) and \((\log X)^2\) bounded test functions, so invariance can be applied directly to both.

The result concerns the autonomous deterministic map with constant parameters \(r\) and \(K\). It does not assert that a particular non-Dirac invariant law exists for every parameter value, and it does not cover stochastic Ricker models, observation noise, transient samples, time-varying carrying capacity, or invariant probabilities with support meeting \(0\).

## Proof
Put
\[
U=\frac{X}{K},
\qquad
Y=\log U.
\]
The defining recurrence gives the pointwise cocycle identity
\[
Y\circ F_{r,K}-Y=r(1-U).
\]
Because \(Y\) is bounded on the compact positive support, invariance yields
\[
0=\mathbb E_\mu[Y\circ F_{r,K}-Y]
=r\left(1-\mathbb E_\mu[U]\right).
\]
Since \(r>0\),
\[
\mathbb E_\mu[U]=1,
\qquad
\mathbb E_\mu[X]=K.
\]

Now apply invariance to \(Y^2\). Using the same cocycle identity,
\[
0
=
\mathbb E_\mu\!\left[(Y+r(1-U))^2-Y^2\right]
=
2r\,\mathbb E_\mu[Y(1-U)]
+r^2\,\mathbb E_\mu[(1-U)^2].
\]
After division by \(r\),
\[
2\,\mathbb E_\mu[Y(U-1)]
=
r\,\mathbb E_\mu[(U-1)^2].
\]
Because \(\mathbb E_\mu[U]=1\), the right side is \(r\operatorname{Var}_\mu(U)\). Also constants disappear from covariance, so
\[
\mathbb E_\mu[Y(U-1)]
=
\frac{1}{K}\operatorname{Cov}_\mu(\log X,X),
\qquad
\operatorname{Var}_\mu(U)
=
\frac{1}{K^2}\operatorname{Var}_\mu(X).
\]
Therefore
\[
2K\,\operatorname{Cov}_\mu(\log X,X)
=
r\,\operatorname{Var}_\mu(X).
\]
If \(\mu\) is non-Dirac then \(\operatorname{Var}_\mu(X)>0\), and solving gives the displayed formula for \(r\). If the variance vanishes, \(X=K\) almost surely, hence \(\mu=\delta_K\); this is indeed invariant for every \(r>0\).

Finally, for a non-Dirac law the equality \(\mathbb E_\mu[X]=K\) rules out support entirely in either \(X\le K\) or \(X\ge K\), because equality of the mean with the corresponding endpoint would then force \(X=K\) almost surely. Hence both strict sides have positive mass.

## Verification
The proof is analytic and uses only invariance of two bounded observables. The bundled checker `verify_ricker.py` verifies the algebraic square expansion and covariance rescaling with exact rational arithmetic; `verification_output.txt` records its replay result. The checker is supplementary and is not used as a substitute for the invariant-measure proof.

The critical boundary cases were checked explicitly: the logarithmic tests require support bounded away from \(0\); the formula for \(r\) requires positive variance; and at zero variance the unique positive stationary law is the equilibrium atom \(\delta_K\), for which \(r\) is genuinely unidentifiable from the one-time marginal.

## Relationship to prior work
Ricker's 1954 stock-recruitment paper is the historical source for the population map and predates the archive cutoff. Sacker's 2007 full-text treatment of periodic Ricker maps uses the normalized recurrence \(x_{n+1}=x_n\exp(p_n-x_n)\) and explicitly derives the telescoping first-moment relation \(\sum x_i=\log(x_0/x_k)+\sum p_i\). For a periodic orbit this yields the familiar arithmetic-mean calibration; that first-moment phenomenon is treated here as prior, not as the originality claim.

The surviving statement is the second logarithmic-moment identity and its consequence: except at the equilibrium atom, the one-time invariant marginal itself identifies the intrinsic growth parameter through a covariance-to-variance ratio. The inspected Sacker full text contains no occurrences of “variance”, “covariance”, or “moment”, and its stated results concern periodic stability and average population. Kon's 2005 work concerns attenuation under periodically varying carrying capacity, while population-inference literature studies likelihood geometry and parameter fitting rather than an exact invariant-marginal formula. These statements do not imply the covariance identity above.

A mathematical-dynamics source that explicitly lists the classical Ricker map among its motivating discrete population maps is classified with primary MSC \(37N25\) and \(37G10\); \(37N25\) is used here as the primary classification for this dynamics finding.

## Limitations
The result is a structural identifiability theorem for an exact invariant probability law, not a finite-sample estimator or a robustness theorem. It gives no sampling-error bounds and makes no claim about noisy or partially observed data. The full text of the 1954 foundational paper was not available for inspection in this run; its bibliographic record and abstract were checked, and the closest later same-map full text was inspected in detail. An unindexed historical occurrence of the second-moment identity therefore remains a residual literature risk.

## References
W. E. Ricker, “Stock and Recruitment,” *Journal of the Fisheries Research Board of Canada* 11(5), 559–623 (1954). DOI: 10.1139/f54-039.

R. J. Sacker, “A note on periodic Ricker maps,” *Journal of Difference Equations and Applications* 13(1), 89–92 (2007). DOI: 10.1080/10236190601008752.

R. Kon, “Attenuant cycles of population models with periodic carrying capacity,” *Journal of Difference Equations and Applications* 11(4–5), 423–430 (2005). DOI: 10.1080/10236190412331335472.

L. Polansky, P. de Valpine, J. O. Lloyd-Smith, and W. M. Getz, “Likelihood ridges and multimodality in population growth rate models,” *Ecology* 90(8), 2313–2320 (2009). DOI: 10.1890/08-1461.1.
