# Sharp horizon-dependent rank reversal for antithetic Gaussian particle matching

## Finding

For the one-dimensional heat-equation gradient random-walk estimator with equal nonzero signed particle masses in two replicas, **minimizing total matching distance need not minimize integrated conditional sampling variance**. Let \(r\ge 1\) be the number of diffusion stages from the current stage through the terminal stage, let each diffusion increment have standard deviation \(\sigma>0\), and let the two strictly ordered sets of \(n\ge 2\) entering positions be \(a_1<\cdots<a_n\) and \(b_1<\cdots<b_n\). All masses in both replicas equal a common \(\mu\ne0\). We compare bijections between these sets; within each pair, the Gaussian displacements are perfectly reflected, and pairs have independent driving Gaussian variables. All such pairings preserve both individual simulation laws.

Write
\[
 g_\tau(d)=\mathbb E|d+\tau Z|=\tau\sqrt{2/\pi}\,e^{-d^2/(2\tau^2)}+d\,\operatorname{erf}\!\left(\frac{d}{\sqrt2\tau}\right),\quad Z\sim N(0,1),
\]
\[
 W_r(d)=g_{\sigma\sqrt{2(r+1)}}(d)-g_{\sigma\sqrt{2r}}(d),\qquad
 T_r=\sigma\sqrt{2r(r+1)\log(1+1/r)}.
\]
The spatially integrated conditional variance contribution \(\mathcal V_\pi\) of the current stage to the terminal two-replica mean field is exactly
\[
 \mathcal V_\pi=C-\frac{\mu^2}{4}\sum_{i=1}^n W_r(a_i-b_{\pi(i)}),
\]
where \(C\) is independent of the bijection \(\pi\). The even function \(W_r\) is strictly concave on \((-T_r,T_r)\) and strictly convex on each of \((T_r,\infty)\) and \((-\infty,-T_r)\).

Consequently, the identity (sorted or rank) assignment is the **unique** variance-minimizing bijection whenever \(\max_{i,j}|a_i-b_j|<T_r\). The reverse-rank assignment \(\pi(i)=n+1-i\) is the **unique** variance-minimizing bijection whenever the two point clouds are completely separated by more than the threshold, namely \(a_n+T_r<b_1\) or \(b_n+T_r<a_1\). These assertions hold for every \(n\), and the same sharp threshold governs all strictly ordered configurations in each respective region.

A quantified crossover occurs for two-particle blocks \(a=(0,\delta)\), \(b=(d,d+\delta)\). For every sufficiently small \(\delta>0\), there is exactly one switch \(d_r(\delta)>\delta\) between identity and reverse assignment, and
\[
 d_r(\delta)=T_r+\frac{(2r+1)\log(1+1/r)-1}{12T_r}\,\delta^2+O_{r,\sigma}(\delta^4).
\]
For \(0\le d<d_r(\delta)\) rank matching is better, and for \(d>d_r(\delta)\) reverse matching is better. The displayed coefficient is strictly positive for \(r\ge1\).

For the separated two-particle sets \(a=(0,D)\), \(b=(2D,3D)\) and \(D>T_r\), let \(G_{\rm rank}\) and \(G_{\rm reverse}\) denote the respective positive decreases of integrated conditional variance against **independently drawn** replica displacements. Then
\[
 \frac{G_{\rm reverse}}{G_{\rm rank}}
 =\frac{W_r(D)+W_r(3D)}{2W_r(2D)}
 \sim 2\exp\!\left(\frac{3D^2}{4(r+1)\sigma^2}\right)
 \quad (D/\sigma\to\infty),
\]
for fixed \(r\). The absolute gains both vanish in this limit, but rank matching loses an exponentially large **relative share of the attainable variance reduction**.

## Assumptions and scope

Fix a conditional pair of particle configurations just before one diffusion stage of the scalar **heat equation**, without nonlinear transport. The same common mass \(\mu\) is assigned to each particle in both configurations, and positions are strictly increasing within each. The stage diffusion noises are independent standard normals across pairs, but are negatives across the two partners of each pair. Future independent diffusion stages enter the stagewise terminal-field martingale conditional mean through smoothing width \(s=\sigma\sqrt{r-1}\). Exactly \(r\) stages, including the current one, remain, each of Gaussian standard deviation \(\sigma\). These hypotheses are conditional on the entering state and do not require the two replicas to have been initialized separately.

Each field is the cumulative sum of particle masses, and the estimator is the average of the two fields. The variance integral is over the real line. Although cumulative fields can have nonzero limiting means, each conditional variance and the difference of such variances is integrable; Gaussian-tail bounds justify the covariance integration. In this statement, *optimal* means optimal **among all bijections with independent reflected Gaussian pairs**, not among arbitrary non-Gaussian, cross-pair-dependent or inter-stage-adaptive couplings. An assignment changes the cross-replica covariance but leaves both replicas' one-step laws and marginal variance contributions unchanged. Particle equality cases are excluded to obtain uniqueness.

## Proof

**1. Exact assignment objective.** For a particle at \(z\), the conditional expectation of its terminal contribution after the remaining diffusion stages is \(F_s(x-z-\sigma Z)\), with \(F_s(t)=\Phi(t/s)\) for \(s>0\) and the indicator \(\mathbf 1\{t\ge0\}\) for \(s=0\). For a reflected matched pair at entering separation \(d\), the difference of the two terminal Gaussian locations has variance \(4\sigma^2+2s^2=2(r+1)\sigma^2\). If the two present-stage displacements were independent instead, that difference would have variance \(2\sigma^2+2s^2=2r\sigma^2\). The indicator-covariance integral identity
\[
 \int_{\mathbb R}\operatorname{Cov}(\mathbf1\{X\le x\},\mathbf1\{Y\le x\})\,dx
 =\tfrac12\bigl(\mathbb E|X-Y'|-\mathbb E|X-Y|\bigr),
\]
where \(Y'\) is independent with the same marginal as \(Y\), follows by integrating differences of centered half-line indicators and Fubini. The same identity applies after convolution with independent Gaussian smoothing. It gives the conditional integrated covariance of one reflected pair as \(-W_r(d)/2\). The cross term in the variance of \((U^A+U^B)/2\) has coefficient \(\mu^2/2\), producing \(-\mu^2W_r(d)/4\). All same-replica contributions and all different-pair cross covariances are assignment-independent, since the noises of distinct matched pairs are independent. Summing yields the asserted objective. Its baseline is a common independent-displacement coupling, so each reflected pairing has strictly positive gain \(\mu^2W_r(d)/4\) per pair.

**2. The unique inflection.** Direct differentiation gives
\[
 W_r''(d)=\sqrt{\frac2\pi}\left[
 \frac{e^{-d^2/(4(r+1)\sigma^2)}}{\sigma\sqrt{2(r+1)}}-
 \frac{e^{-d^2/(4r\sigma^2)}}{\sigma\sqrt{2r}}
 \right].
\]
The ratio of the first bracketed term to the second increases strictly with \(|d|\), beginning below one and tending to infinity. Its unique positive intersection is the stated \(T_r\), proving both strict curvature regimes; \(W_r'''(T_r)>0\).

**3. Global permutation extremizers.** If \(a_i<a_j\) and \(b_k<b_l\), the assignment cross-difference is
\[
 W_r(a_i-b_k)+W_r(a_j-b_l)
 -W_r(a_i-b_l)-W_r(a_j-b_k)
 =-\int_{a_i}^{a_j}\!\int_{b_k}^{b_l} W_r''(x-y)\,dy\,dx.
\]
For every cross difference within \((-T_r,T_r)\), the right-hand side is strictly positive, so uncrossing improves the sum of \(W_r\)'s and the unique maximizing bijection is identity. When one entire point cloud is separated from the other by more than \(T_r\), every point of every exchange rectangle has difference of magnitude greater than \(T_r\); the integral is then strictly negative, so crossing improves the sum and reverse rank is the unique maximizer. Mere pairwise separation of the finitely many cross-distances does not suffice if their convex hulls overlap. Maximizing this sum is equivalent to minimizing integrated conditional variance. The familiar Monge exchange principle is used here, but the present, horizon-dependent curvature boundary must be computed for the **actual Gaussian variance-gain kernel**, not for distance.

**4. Sharp small-spacing transition.** For the translated two-particle blocks with \(d>\delta\), reverse minus rank gain, without the common positive factor, is
\[
 \Delta_\delta(d)=W_r(d-\delta)+W_r(d+\delta)-2W_r(d)
 =\int_{-\delta}^{\delta}(\delta-|u|)W_r''(d+u)\,du.
\]
Choose \(\delta\) small enough that \(W_r'''\) is positive throughout \([T_r-2\delta,T_r+2\delta]\) and \(\delta<T_r/3\). Then \(\Delta_\delta<0\) for \(\delta<d\le T_r-\delta\) (also the rank assignment wins for \(0\le d\le\delta\), because all four cross distances lie in the concave region), it is positive for \(d\ge T_r+\delta\), and it is strictly increasing in the transition band since the derivative of the integral has positive integrand. Hence a unique crossover lies in that band. Taylor expansion about \(T_r\), using \(W_r''(T_r)=0\) and \(W_r'''(T_r)>0\), gives
\[
 d_r(\delta)-T_r=-\frac{W_r^{(4)}(T_r)}{12W_r'''(T_r)}\delta^2+O_{r,\sigma}(\delta^4).
\]
Differentiating the two Gaussian terms at \(T_r\) yields \(-W_r^{(4)}(T_r)/W_r'''(T_r)=((2r+1)\log(1+1/r)-1)/T_r\), as required. For \(r\ge1\) this numerator is positive; for instance its extension to positive real \(r\) follows by the elementary inequality \(\log(1+x)>x/(1+x/2)\) for \(x>0\). Since \(d_r(\delta)\to T_r\), neither uniform global assignment regime can be extended past the stated curvature threshold.

**5. Relative efficiency of rank matching.** Put \(a=(0,D)\), \(b=(2D,3D)\). Both rank distances equal \(2D\), while reverse distances are \(D,3D\). For fixed \(\tau>0\), the folded-Gaussian tail identity and integration by parts give
\[
 g_\tau(d)-d\sim\sqrt{2/\pi}\,\tau^3d^{-2}\exp(-d^2/(2\tau^2))\quad(d\to+\infty).
\]
As \(\tau_+>\tau_-\), the \(\tau_+\) term dominates \(W_r(d)\). Substituting into the exact two-pair ratio yields \(\frac12\cdot4\exp(3D^2/(2\tau_+^2))(1+o(1))=2\exp(3D^2/[4(r+1)\sigma^2])(1+o(1))\). This is a statement about **relative** variance-gain efficiency, not about an unbounded absolute variance.

## Verification

Run `python3 check_matching.py` using Python 3 and only the standard library. It verifies the curvature signs and inflection equality, exhaustive small-dimensional permutation extremizers in both geometric regimes, two-block transition brackets and second-order displacement scaling, and finite-distance relative-gain ratios. These tests are finite computational checks; Steps 1–5 above supply the universally quantified proof. The checker does not certify a general coupling beyond the stated independent reflected-pair family.

## Relationship to prior work

Abkin and Daripa (arXiv:2610.01120, Sections 3.1, 4.2–4.4) derive the pairwise integrated variance-gain kernel for a **fixed** matching, and note that rank matching minimizes total absolute partner distance; Corollary 4.8 establishes that a fixed pair's variance reduction decreases with separation. Their Proposition 4.5 extends fixed-matching variance calculations to stages of the heat-equation solver. These exact source formulas are starting points, **not** independent discoveries here. They do not state that rank matching globally optimizes variance over bijections, or give the curvature crossover, global rank/reverse optimum regions, and exponentially separated rank-efficiency ratio established above. We make no novelty claim for monotone rearrangement, Gaussian folded-normal identities, or the standard Monge exchange inequality.

Delon–Salomon–Sobolevskii (arXiv:0902.3527) give matching theory for Monge costs on a circle; that generic framework is compatible with the exchange step but does not identify the nonuniformly curved reflected-Gaussian sampling objective here. Nüsken–Pavliotis (arXiv:1806.11026) study optimal coupling of Markov samplers for asymptotic variance; their general framework is conceptually relevant but has a different objective and coupling class. These comparisons do not establish uniqueness of the present result in the entire historical literature.

## Limitations

All masses have equal magnitude and one common sign, and only bijective independent-pair Gaussian **reflection** is optimized. The result is conditional on entering positions and concerns the stagewise integrated conditional variance of the terminal average field for the **linear heat equation**. It does not optimize cumulative full-run variance when past control choices alter entering-state distributions, nor prove a rule for mixed mass signs, nonlinear flux, multivariate particles, or arbitrary Gaussian cross-pair coupling. The strict inequalities for position geometry exclude ties and equality at the inflection boundary. The exponential ratio concerns gains against independence, both of which vanish as block separation grows. The published sources inspected and semantic-record searches leave a residual risk of a prior equivalent application of Monge theory or Gaussian variance-kernel assignment outside the indexed material. Independent scientific audit has not been performed.

## References

1. Stephen Abkin and Prabir Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection–diffusion equations*, arXiv:2610.01120v2 (2026), Sections 3.1, 4.2–4.4; initially publicly submitted 2026-10-01. https://arxiv.org/html/2610.01120v2
2. Julie Delon, Julien Salomon, and Andrei Sobolevskii, *Fast transport optimization for Monge costs on the circle*, arXiv:0902.3527 (2009/2010). https://arxiv.org/abs/0902.3527
3. Nikolas Nüsken and Grigorios A. Pavliotis, *Constructing sampling schemes via coupling: Markov semigroups and optimal transport*, arXiv:1806.11026 (2018). https://arxiv.org/abs/1806.11026
