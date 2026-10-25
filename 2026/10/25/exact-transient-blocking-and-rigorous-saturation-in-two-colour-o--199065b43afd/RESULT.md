# Exact transient blocking and rigorous saturation in two-colour one-dimensional adsorption

## Finding

Consider the infinite nearest-neighbour lattice with two irreversibly adsorbing species, each proposed independently at rate \(1/2\) per site. A proposed particle is accepted precisely when its site is unoccupied and neither adjacent site contains the opposite species; rejected proposals do not consume the site. Initially all sites are empty. Let \(B(t)\) denote the probability that the origin, at time \(t\geq0\), is empty **and** has an A particle on one side and a B particle on the other (so it is permanently blocked). Then, with \(u(t)=1-e^{-t}\),

\[
\boxed{B(t)=\frac12 u(t)^2e^{-u(t)}.}
\]

In particular, the exact jammed occupied-site density is

\[
\boxed{\theta_\infty=1-\lim_{t\to\infty}B(t)=1-\frac1{2e}.}
\]

Furthermore, the blocked-site density approaches its limit with the sharp asymptotic

\[
\frac1{2e}-B(t)\sim \frac{e^{-t}}{2e}\qquad(t\to\infty).
\]

These formulas concern **repeated attempts** and the infinite lattice, not a single-attempt-per-site process or a claimed exact finite-ring formula.

## Assumptions and scope

At each \(i\in\mathbb Z\), independent homogeneous Poisson clocks propose A and B at rates \(1/2\) each. All clocks at different sites and of different species are independent. Each site changes only once, from vacant to A or B. An unoccupied site whose two neighbours carry opposite species cannot ever change; that state is called blocked. Time is measured in units of the combined per-site attempt rate. The assertion is for the infinite one-dimensional lattice and every finite \(t\ge0\), as well as the limit \(t\to\infty\).

The Harris graphical construction is well-defined on finite time intervals: to influence the origin through a nearest-neighbour path with \(m\) backward-in-time transitions before fixed \(t\), there must be a chronologically ordered chain of at least \(m\) clock rings. Bounding the number of spatial paths by \(2^m\) and their temporal intensity by \(t^m/m!\) makes the probability of an arbitrarily long causal ancestor path zero. The infinite-time configuration is the monotone sitewise limit of the finite-time states.

## Proof

**1. One-sided cavity law.** Hold site \(0\) permanently vacant and let \(T\) be the first successful occupation time of site \(1\) in the half-line \(\{1,2,\ldots\}\). Let \(g(t)=\Pr(T>t)\). First also freeze site \(1\) and let \(S\) be the first occupation time of site \(2\) in that auxiliary system. Translation invariance along the half-line gives \(S\stackrel d=T\), and \(S\) is independent of the proposal clocks at site \(1\).

Before time \(S\), the two neighbours of site \(1\) are vacant, so successful proposals there have rate \(1\). After \(S\), while site \(1\) remains vacant, only proposals matching the species at site \(2\) can succeed, hence the successful rate is \(1/2\). Consequently

\[
g(t)=\mathbb E\!\left[e^{-\min(t,S)-(t-S)_+/2}\right]
=e^{-t}g(t)+e^{-t/2}\int_0^t e^{-s/2}\,(-dg(s)).
\]

Since \(g(0)=1\), integration by parts yields the exact Volterra relation

\[
g(t)=e^{-t/2}\left(1-\frac12\int_0^t e^{-s/2}g(s)\,ds\right).
\]

Putting \(h(t)=e^{t/2}g(t)\), this becomes \(h'(t)=-e^{-t}h(t)/2\), with \(h(0)=1\). Its unique solution is

\[
\boxed{g(t)=\exp\!\left(-\frac t2-\frac{1-e^{-t}}2\right)}.
\]

In particular \(g(t)\to0\), so the cavity boundary site is eventually occupied almost surely. Species-exchange symmetry shows that the accepted species is an independent fair A/B label conditional on its occupation time.

**2. Weighted cavity occupation by time \(t\).** Write

\[
M(t)=\mathbb E\left[e^{-T/2}\mathbf1_{\{T\le t\}}\right]
=\int_0^t e^{-s/2}\,(-dg(s)).
\]

The integration-by-parts identity above gives

\[
M(t)=1-e^{-t/2}g(t)-\frac12\int_0^t e^{-s/2}g(s)\,ds
=h(t)-e^{-t}h(t).
\]

Thus

\[
\boxed{M(t)=(1-e^{-t})\exp\!\left(-\frac{1-e^{-t}}2\right)}.
\]

**3. Blocked-site factorization.** Hold the central site \(0\) vacant. Its left and right half-line systems have independent proposal clocks. Their boundary occupation times \(T_-\) and \(T_+\) are independent copies of \(T\); their accepted species are independent fair labels, independent of those times. Couple the true process to this frozen-centre process by using the same proposal clocks. Until the first successful deposition at site \(0\), the two processes coincide away from \(0\).

If the two cavity boundary species agree, site \(0\) cannot become permanently blocked by their occupation. If they disagree, successful attempts at site \(0\), conditional on the two frozen-side histories, occur at rate \(1\) before \(\min(T_-,T_+)\), at rate \(1/2\) between those occupation times, and at rate zero afterward. The conditional chance of no successful proposal through \(\max(T_-,T_+)\) is therefore

\[
\exp\!\left[-\min(T_-,T_+)-\frac12|T_--T_+|\right]
=e^{-(T_-+T_+)/2}.
\]

The origin is blocked by time \(t\) exactly when this no-success event occurs, the two boundary colours differ, and both occupation times are at most \(t\). Independence and the probability \(1/2\) of opposite colours yield

\[
B(t)=\frac12\mathbb E\left[e^{-T_-/2}\mathbf1_{\{T_-\le t\}}\right]
\mathbb E\left[e^{-T_+/2}\mathbf1_{\{T_+\le t\}}\right]
=\frac12M(t)^2.
\]

Substitution proves the finite-time formula.

**4. Saturation and relaxation.** Since both frozen-side boundary occupation times are almost surely finite, an origin that never becomes occupied ultimately has two occupied neighbours. If these neighbours have the same colour, proposals of that colour subsequently succeed at rate \(1/2\), contradicting perpetual vacancy. Thus the only ultimately vacant sites are permanently blocked. Letting \(t\to\infty\) proves the exact jammed density. Expanding \(\frac12u^2e^{-u}\) at \(u=1\), using \(1-u=e^{-t}\), gives the relaxation coefficient. Translation ergodicity of the Poisson construction additionally makes the same constant the almost-sure spatial frequency of blocked sites in the infinite system.

## Verification

The standalone pure-standard-library script `check.py` verifies algebraic identities and separately computes the exact absorbing-chain expectation on periodic rings of sizes \(4\) through \(12\) using rational arithmetic. The latter agrees with the finite-ring expression reported conjecturally in the motivating paper, but checking those sizes is **not a proof** of that finite-ring expression. The script also simulates the **original repeated-proposal dynamics**, with independent Poisson attempts and fixed random seed, on rings of length \(1500\) for \(450\) independent realizations at six positive times. Its output is archived in `check_results.txt`. All six comparisons lie within five estimated standard errors of the analytic blocked fractions. These finite tests corroborate but do not replace the infinite-lattice proof above.

## Relationship to prior work

Martins, Dickman and Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions* (arXiv:2211.04622, first posted 2022-11-09), introduce the identical repeated-attempt antagonistic adsorption rule and report in Section V a numerical three-site approximation, simulations, and a conjectural finite-cycle coverage expression converging to \(1-1/(2e)\). The limiting **number** is therefore prior conjectural evidence, not claimed as a newly discovered constant. The present result supplies an exact infinite-volume **time-dependent blocked fraction**, an explicit one-sided cavity law, and a rigorous derivation of that limit without the approximate three-site factorization.

Do Amaral and dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site* (arXiv:2306.09786, first posted 2023-06-16), solve a different one-attempt-per-site rule, in which a site can remain forever empty even when its two occupied neighbours agree. Its time and jamming laws do not imply the repeated-attempt formula established here. Penrose and Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs* (Ann. Appl. Probab. 15 (2005), 853–889), study graph deposition and annihilation with other blocking rules and are relevant as general graphical-method background, rather than as a documented evaluation of this two-colour observable.

## Limitations

This proof uses equal species proposal rates, nearest-neighbour exclusion, independent Poisson clocks, repeated attempts, and the infinite line. Unequal arrival rates require a different weighted cavity system. No exact finite-cycle formula is proved here, no claim is made about multi-dimensional systems, and the source's numerical finite-ring conjecture remains logically separate. The evidence search is not a mathematical proof of priority; a prior equivalent formula expressed through a different stochastic representation cannot be ruled out without independent scholarly assessment.

## References

1. P. H. L. Martins, R. Dickman and R. M. Ziff, *Percolation in two-species antagonistic random sequential adsorption in two dimensions*, arXiv:2211.04622 (first posted 2022-11-09), Section V. https://arxiv.org/abs/2211.04622
2. C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site*, arXiv:2306.09786 (first posted 2023-06-16), Sections 1 and 4–6. https://arxiv.org/html/2306.09786v1
3. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Annals of Applied Probability 15 (2005), 853–889.
