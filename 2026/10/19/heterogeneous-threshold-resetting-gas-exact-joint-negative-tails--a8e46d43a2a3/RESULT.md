# Heterogeneous threshold-resetting gas: exact joint negative tails and threshold-free extremal dependence

## Finding
For any fixed integer \(N\geq3\), consider \(N\) independent one-dimensional Brownian motions with individual diffusivities \(D_i>0\), all starting at zero. Whenever any particle reaches its own positive level \(L_i>0\), simultaneously return every particle to zero, then repeat independently. The convention is that free motion has generator \(D_i\partial_{x_i}^2\) (variance \(2D_i t\)).

Write \(\pi\) for the stationary law; let
\[
 S_i(t)=\operatorname{erf}\!\left(\frac{L_i}{\sqrt{4D_it}}\right),\qquad
 \mu=\int_0^\infty\prod_{i=1}^N S_i(t)\,dt,\qquad
 A=\prod_{i=1}^N\frac{L_i}{\sqrt{\pi D_i}},\qquad
 \nu=\frac N2-1.
\]
These constants satisfy \(0<\mu,A,\nu<\infty\). For each nonempty set of tagged indices \(J\subseteq\{1,\ldots,N\}\) and every choice of fixed positive constants \(c_j\) for \(j\in J\), the complete finite-population joint negative-excursion law is
\[
 \boxed{\lim_{R\to\infty}R^{N-2}
 \Pr_\pi\{X_j<-Rc_j\text{ for every }j\in J\}
 =\frac{A\Gamma(\nu)}{\mu}
 \left(\frac4{\sum_{j\in J}c_j^2/D_j}\right)^\nu.}
\]
In particular, for every pair \(i\neq j\), the stationary far-left tail-dependence coefficient is
\[
 \boxed{\lim_{R\to\infty}\Pr_\pi\{X_j<-R\mid X_i<-R\}
 =\left(\frac{D_j}{D_i+D_j}\right)^\nu.}
\]
This coefficient is independent of every reset threshold and all untagged diffusivities. It is strictly between zero and one, depends asymmetrically on the ordering of the two tagged diffusivities, and shows that simultaneous extreme negative excursions retain nonvanishing conditional dependence despite independent inter-reset Brownian motions. For each \(i\) and real \(p>0\),
\[
 \boxed{\mathbb E_\pi|X_i|^p<\infty\quad\Longleftrightarrow\quad p<N-2.}
\]
The boundary moment at \(p=N-2\) diverges logarithmically. These are joint statements in the finite-\(N\), fixed-parameter regime, not approximations based on \(N\to\infty\).

## Assumptions and scope
Fix arbitrary deterministic \(N\in\{3,4,\ldots\}\), positive diffusivities \(D_1,\ldots,D_N\), and positive absorbing/reset levels \(L_1,\ldots,L_N\). Between resets, the Brownian coordinates are independent, with zero drift, and a reset is instantaneous and complete: all coordinates become zero when the first coordinate hits its own upper level. All post-reset trajectories use independent fresh noise. Simultaneous first hits have probability zero. Observation is in the invariant stationary regime. Every \(R\to\infty\) limit holds with \(N,D_i,L_i,J,c_j\) fixed; none of the \(c_j\) may be zero. The result does not concern negative triggering barriers, independent resetting clocks, or interaction forces.

The complementary error function is \(\operatorname{erfc}(z)=1-\operatorname{erf}(z)\), while \(\Gamma\) denotes Euler's gamma function. The free killed transition subprobability density on \(( -\infty,L_i)\) is
\[
 G_i(x,t)=\frac{e^{-x^2/(4D_it)}-e^{-(x-2L_i)^2/(4D_it)}}{\sqrt{4\pi D_it}}\,\mathbf1_{\{x<L_i\}}.
\]
The formula is well defined for \(t>0\), with starting position zero.

## Proof
**1. Finite-mean renewal and stationary representation.** The reflection principle yields the survival probability of a single free coordinate up to time \(t\): \(S_i(t)=\int_{-\infty}^{L_i}G_i(x,t)\,dx\). Independence of free coordinates gives the no-reset survival probability \(\prod_iS_i(t)\). Since \(\operatorname{erf}(z)\sim2z/\sqrt\pi\) as \(z\downarrow0\),
\[
 S_i(t)\sim\frac{L_i}{\sqrt{\pi D_i}}\,t^{-1/2},\qquad
 \prod_{i=1}^N S_i(t)\sim A t^{-N/2}\quad(t\to\infty).
\]
It follows that the expected regeneration period \(\mu=\int_0^\infty\prod_iS_i(t)\,dt\) is finite and strictly positive exactly when \(N>2\). Standard finite-mean regenerative occupation gives a probability distribution
\[
 \pi(d\mathbf x)=\frac1\mu\int_0^\infty\prod_{i=1}^N G_i(x_i,t)\,dt\,d\mathbf x,
\]
which is invariant. Every trajectory resets in finite time almost surely and the renewal durations have a continuous nonlattice law; thus the regenerative equilibrium is the unique attracting stationary law. The known homogeneous form of this representation is not claimed as new.

**2. Exact killed left-tail factorization.** For \(z>0\), integrate the reflected Gaussian density and translate the second integral:
\[
 H_i(z,t):=\Pr\{X_i(t)<-z,\ T_i>t\}
 =\frac1{\sqrt{4\pi D_it}}\int_z^{z+2L_i}e^{-y^2/(4D_it)}\,dy,
\]
where \(T_i\) is the free first hitting time of \(L_i\). Another exact integral expression is
\[
 S_i(t)=\frac1{\sqrt{4\pi D_it}}
 \int_{-L_i}^{L_i}e^{-u^2/(4D_it)}\,du.
\]
Therefore the claimed joint tail, denoted \(P_J(R)\), has the exact identity
\[
 P_J(R)=\frac1\mu\int_0^\infty
 \left(\prod_{j\in J}H_j(Rc_j,t)\right)
 \left(\prod_{i\notin J}S_i(t)\right)dt.
\]
No independence is assumed for stationary positions; conditional independence at a given common elapsed renewal age produces precisely this mixture.

**3. Dominated asymptotic for fixed \(N\).** For each fixed \(s>0\), let \(t=R^2s\). Directly from the two short Gaussian integrals,
\[
 \lim_{R\to\infty}R S_i(R^2s)
 =\frac{L_i}{\sqrt{\pi D_i s}},\qquad
 \lim_{R\to\infty}\frac{H_j(Rc_j,R^2s)}{S_j(R^2s)}
 =e^{-c_j^2/(4D_js)}.
\]
To justify integrating these limits, note the **uniform** bound
\[
 S_i(t)\le\frac{L_i}{\sqrt{\pi D_it}}\quad\text{for every }t>0.
\]
The integral formulas above also give, for every sufficiently large \(R\) with \(Rc_j\ge\sqrt2 L_j\),
\[
 0\le\frac{H_j(Rc_j,t)}{S_j(t)}
 \le\exp\!\left(-\frac{R^2c_j^2}{8D_jt}\right)
 \qquad(t>0).
\]
Indeed the numerator is bounded by its interval length times \(e^{-R^2c_j^2/(4D_jt)}\), while the denominator is at least its equal interval length times \(e^{-L_j^2/(4D_jt)}\). The assumed inequality \(R^2c_j^2\ge2L_j^2\) proves the last display. Consequently, after substituting \(t=R^2s\), the rescaled integrand in \(R^{N-2}P_J(R)\) is bounded above by
\[
 A s^{-N/2}\exp\!\left(-\frac1{8s}
 \sum_{j\in J}\frac{c_j^2}{D_j}\right).
\]
Because \(J\neq\varnothing\) and \(N>2\), this bound is integrable both at zero and at infinity. Dominated convergence therefore gives, writing \(Q=\sum_{j\in J}c_j^2/D_j>0\),
\[
 \lim_{R\to\infty}R^{N-2}P_J(R)
 =\frac A\mu\int_0^\infty s^{-N/2}e^{-Q/(4s)}\,ds
 =\frac{A\Gamma(N/2-1)}\mu\left(\frac4Q\right)^{N/2-1},
\]
by the substitution \(u=Q/(4s)\). This proves the first boxed formula for every nonempty tagged set and positive vector of relative excursion depths.

**4. Conditional tail dependence and moment cutoff.** Use the preceding expression with \(J=\{i,j\}\) and \(J=\{i\}\), both at unit depth. Their common \(A/\mu\) factor cancels; simplifying the two \(Q\)-values gives
\[
 \frac{(1/D_i+1/D_j)^{-\nu}}{(1/D_i)^{-\nu}}
 =\left(\frac{D_j}{D_i+D_j}\right)^\nu.
\]
Moreover \(X_i<L_i\) almost surely under \(\pi\), so the positive tail of \(|X_i|\) agrees for large thresholds with the negative tail \(\Pr_\pi(X_i<-R)\). This tail is equivalent to a strictly positive multiple of \(R^{-(N-2)}\). Integrating \(p\int_0^\infty R^{p-1}\Pr_\pi(|X_i|>R)\,dR\) proves finite absolute moments precisely for \(0<p<N-2\), with logarithmic divergence at equality.

## Verification
The accompanying standalone `verify.py` numerically evaluates the exact renewal-occupation integrals with independent Gaussian-interval quadrature. For \(N=4\), \(\mathbf D=(1,0.5,2,1.5)\), and \(\mathbf L=(1,1.5,0.7,1.2)\), it returns \(\mu\approx0.35698468349\), a one-particle tail coefficient \(1.16798046352\), and the joint coefficient for particles 1 and 2 \(0.38932682117\); the ratio is exactly \(1/3\). At increasing finite \(R\) it tests convergence to the analytically derived constants. Further checks change all the reset thresholds, and evaluate a heterogeneous \(N=5\) model and several tagged subsets. The numerical checks passed; finite quadrature is corroborative only, not a substitute for the dominated-convergence proof. Run from a directory with Python, NumPy and SciPy installed using `python verify.py`.

## Relationship to prior work
Biroli, Majumdar and Schehr, *First Passage Resetting Gas* (first public arXiv submission 29 November 2025, arXiv:2512.00440), derive an exact homogeneous stationary joint density and investigate large-population collective statistics. The renewal-kernel representation and the existence transition at \(N=3\) are due to that work. The present theorem instead treats **arbitrary unequal** diffusivities and upper triggering levels and rigorously classifies **all nonempty tagged joint negative excursions** in the fixed finite-population regime, identifying an invariant threshold-independent conditional tail-dependence spectrum and the exact marginal moment cutoff. These claims and constants are not stated in the inspected source. They are consequences of the heterogeneous renewal formulation and are not assertions of an independently new renewal principle.

Biswas, Majumdar and Pal, *Target Search Optimization by Threshold Resetting* (arXiv:2504.13501), study search completion time under threshold-triggered joint resetting, rather than the heterogeneous stationary negative-tail tensor. Biroli, Larralde, Majumdar and Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting* (arXiv:2211.00563), study a **constant-rate Poisson** resetting gas, where the large-age mixing law is exponential rather than the algebraic survival weight relevant here. General regenerative-mixture or regular-variation results may yield alternative proofs or implicitly contain this specialization; no claim of exclusive general-method priority is made.

## Limitations
The asymptotic is pointwise in each fixed parameter set and tagged subset; it is not uniform as \(N\), thresholds, diffusivities, or the relative depths vary, and it makes no assertion about rightward positive excursions beyond triggering barriers. Only ordinary zero-drift independent Brownian motion between global resets is covered. The tail-dependence coefficient compares **negative** excursions and should not be confused with Pearson correlation. The exact renewal representation is previously known in its homogeneous form. Literature searching and source inspection cannot rule out every implicit reduction to broader regenerative or multivariate-regular-variation theory; independent assessment of originality has not been performed.

## References
1. M. Biroli, S. N. Majumdar and G. Schehr, *First Passage Resetting Gas*, arXiv:2512.00440, version 1 initially public 29 November 2025; https://arxiv.org/abs/2512.00440. Inspected full openly available HTML version: https://arxiv.org/html/2512.00440v2.
2. A. Biswas, S. N. Majumdar and A. Pal, *Target Search Optimization by Threshold Resetting*, arXiv:2504.13501; https://arxiv.org/abs/2504.13501.
3. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme Statistics and Spacing Distribution in a Brownian Gas Correlated by Resetting*, arXiv:2211.00563; https://arxiv.org/abs/2211.00563.
