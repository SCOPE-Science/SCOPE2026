# Shape ordering and two-end laws for affine sections of high-dimensional boxes

## Finding
Consider an orthotope \(Q_d=\prod_{i=1}^{d}[-\ell_{d,i},\ell_{d,i}]\) with aspect parameters uniformly bounded above and away from zero. Select a Euclidean-motion-invariant affine hyperplane, conditioned to intersect \(Q_d\), and denote the number of vertices of its generic section by \(N_d\). Suppose the empirical half-length distributions converge weakly to a probability measure \(\mu\) on a fixed interval \([a,b]\subset(0,\infty)\).

Set \(m=\sqrt{2/\pi}\), \(M_r=\int t^r\,\mu(dt)\), and
\[
\Lambda_\mu(\lambda)=\int\mathbb E[\log\cosh(\lambda tG)]\,\mu(dt),\qquad I_\mu(s)=\sup_{\lambda\ge0}\{\lambda s mM_1-\Lambda_\mu(\lambda)\},
\]
where \(G\) is standard normal and \(0\le s\le1\). Let \(U\) be uniform on \([0,1]\). Then
\[
\frac{\log N_d}{d}\ \Longrightarrow\ Y_\mu=\log2-I_\mu(U).
\]
The function \(I_\mu\) is continuous, strictly increasing, and maps \([0,1]\) onto \([0,\log2]\). Consequently the limiting logarithmic complexity has a continuous, nondegenerate law supported on \([0,\log2]\), with distribution function \(\Pr(Y_\mu\le y)=1-I_\mu^{-1}(\log2-y)\) for \(0<y<\log2\).

There is a strict shape-ordering principle. Writing \(\mu_0=\delta_{M_1}\) for the constant-length (cubical) shape, for every non-point-mass \(\mu\) and every \(0<s<1\),
\[
I_\mu(s)< I_{\mu_0}(s),\qquad Y_\mu\text{ strictly first-order stochastically dominates }Y_{\mu_0}.
\]
Thus heterogeneous side lengths make the typical exponential-scale section complexity strictly larger than in the cubical case, although the *finite-dimensional arithmetic mean* \(\mathbb EN_d=2^{d-1}\) is independent of all side lengths. This mean identity is previously known and is not claimed as new.

Both ends of the limiting law have explicit sharp constants:
\[
\Pr(Y_\mu>\log2-\varepsilon)\sim\frac{\sqrt{\pi M_2}}{M_1}\sqrt\varepsilon,
\qquad
\Pr(Y_\mu\le\varepsilon)\sim\frac{3}{\pi M_1M_{-1}}\varepsilon^2
\quad(\varepsilon\downarrow0).
\]
The two coefficients separate the second moment and reciprocal first moment of the side-length law.

## Assumptions and scope
For every integer \(d\ge2\), \(\ell_{d,i}\in[a,b]\) for fixed \(0<a\le b<\infty\), and \(d^{-1}\sum_i\delta_{\ell_{d,i}}\Rightarrow\mu\). The hyperplane measure is normalized by conditioning Euclidean-motion-invariant hyperplane measure on those intersecting \(Q_d\). In particular, the normal orientation is **width biased**, and conditional on its normal the offset is uniform across the directional support interval. The stated weak convergence concerns the unscaled natural logarithm of the vertex count divided by \(d\); it makes no claim of pointwise concentration of \(N_d\). All genericity assertions hold with probability one for the continuous random hyperplane measure.

## Proof
**1. Kinematic sampling.** Represent an unoriented unit normal by \(u=g/\|g\|_2\), with independent \(g_i\sim N(0,1)\). Put \(W_d=\sum_i\ell_{d,i}|g_i|\). Conditional on this normal, the offset divided by \(\|g\|_2\) is uniform on \([-W_d,W_d]\). After reflecting the normal, the absolute offset is \(T_d=UW_d\), with independent uniform \(U\in(0,1)\). The true orientation distribution, relative to Gaussian-induced Haar orientation, has Radon–Nikodym derivative
\[
\frac{W_d/\|g\|_2}{\mathbb E[W_d/\|g\|_2]}.
\]
Because \(W_d/\|g\|_2\le b\sqrt d\) and \(\mathbb E[W_d/\|g\|_2]\ge a\,\mathbb E\sum_i|u_i|\sim am\sqrt d\), this density is uniformly bounded for large \(d\). Hence any probability-zero or convergence-in-probability statement established in the unweighted model transfers to the true conditioned hyperplane law.

**2. Section vertices become a Boolean edge boundary.** For any fixed generic \(g,T_d\), assign to a vertex sign pattern \(\sigma\in\{-1,1\}^d\) the linear height \(H_\sigma=\sum_i\sigma_i\ell_{d,i}g_i\). Let \(B_d=\{\sigma:H_\sigma>T_d\}\). Every section vertex uniquely arises at an original box edge crossing the plane; therefore \(N_d=|\partial B_d|\), where \(\partial\) is the edge boundary in the \(d\)-cube graph. As \(T_d>0\) and heights come in opposite pairs, \(1\le |B_d|\le 2^{d-1}\), almost surely.

For every \(B\subset\{-1,1\}^d\) with \(|B|\le2^{d-1}\), elementary edge expansion yields
\[
|B|\le|\partial B|\le d|B|.
\]
For completeness, the left inequality follows by induction in \(d\). Partition \(B\) into its two coordinate slices of sizes \(r,s\), with \(r\ge s\). If both do not exceed \(2^{d-2}\), apply induction to each slice. Otherwise apply induction to the complement of the larger slice and to the smaller slice, and use the at least \(r-s\) edges joining the slices. In that case the resulting lower bound is \(2^{d-1}\ge r+s\). Thus
\[
\left|d^{-1}\log N_d-d^{-1}\log|B_d|\right|\le d^{-1}\log d\longrightarrow0.
\]

**3. Quenched signed-sum exponent.** For independent uniform signs \(\sigma_i\), conditional on the Gaussian vector,
\[
|B_d|=2^d\Pr_\sigma\!\left\{d^{-1}\sum_i\sigma_i\ell_{d,i}|g_i|>Ud^{-1}W_d\right\}.
\]
For any fixed \(\lambda\ge0\), its conditional logarithmic moment-generating function is \(d^{-1}\sum_i\log\cosh(\lambda\ell_{d,i}|g_i|)\). Independent Gaussian concentration, the bounded half-lengths, and weak empirical convergence imply locally uniform convergence in probability to \(\Lambda_\mu(\lambda)\). Also \(d^{-1}W_d\to mM_1\). Differentiation under expectation gives
\[
\Lambda_\mu'(\lambda)=\int\mathbb E[t|G|\tanh(\lambda t|G|)]\,\mu(dt),\quad
\Lambda_\mu''(\lambda)=\int\mathbb E[t^2G^2\operatorname{sech}^2(\lambda tG)]\,\mu(dt)>0.
\]
Its derivative increases from zero to \(mM_1\). The one-dimensional exponential-tilting lower bound and Chernoff upper bound therefore give, at every strictly interior \(s\in(0,1)\),
\[
\frac1d\log\Pr_\sigma\!\left(d^{-1}\sum_i\sigma_i\ell_{d,i}|g_i|\ge smM_1\right)\ \xrightarrow{\Pr}\ -I_\mu(s).
\]
For clarity, under the exponentially tilted signs at the unique \(\lambda\) satisfying \(\Lambda_\mu'(\lambda)=smM_1\), the normalized signed sum converges in probability to its tilted mean because its variance is uniformly \(O(1/d)\); a small interval around this mean provides the matching logarithmic lower bound. Threshold monotonicity and continuity permit replacing \(smM_1\) by the random \(U W_d/d\). Consequently \(d^{-1}\log |B_d|\to\log2-I_\mu(U)\) jointly with \(U\), in probability in the Gaussian setup, and therefore in distribution in the kinematic setup.

**4. Strict shape comparison.** For \(\lambda>0\) the function \(t\mapsto\mathbb E\log\cosh(\lambda tG)\) is strictly convex on \((0,\infty)\), its second derivative being positive. Strict Jensen gives \(\Lambda_\mu(\lambda)>\Lambda_{\delta_{M_1}}(\lambda)\) for every \(\lambda>0\) unless \(\mu\) is a point mass. At each \(0<s<1\), the supremum defining \(I_\mu(s)\) is attained at a finite positive parameter. Evaluating the inequality at that optimizer gives the strict rate comparison. Coupling both limit variables with the same \(U\) proves strict stochastic dominance, including strict inequality of distribution functions at every interior threshold.

**5. End constants.** At \(\lambda\downarrow0\), dominated Taylor expansion gives \(\Lambda_\mu(\lambda)=M_2\lambda^2/2+O(\lambda^4)\), hence
\[
I_\mu(s)=\frac{m^2M_1^2}{2M_2}s^2+O(s^4)=\frac{M_1^2}{\pi M_2}s^2+O(s^4),\quad s\downarrow0.
\]
Inverting at a uniform \(U\) yields the upper-end square-root coefficient stated above.

For large \(\lambda\), the exact identity \(\log\cosh z=|z|-\log2+\log(1+e^{-2|z|})\), the half-normal density \(m e^{-t^2/2}\), and \(\int_0^\infty\log(1+e^{-v})\,dv=\pi^2/12\) give uniformly over \(t\in[a,b]\),
\[
\Lambda_\mu(\lambda)=mM_1\lambda-\log2+\frac{m\pi^2M_{-1}}{24\lambda}+O(\lambda^{-3}).
\]
Legendre optimization near \(s=1\) now yields
\[
\log2-I_\mu(s)=\sqrt{\frac\pi3M_1M_{-1}}\sqrt{1-s}+o(\sqrt{1-s}).
\]
Inverting proves the lower-end quadratic probability law.

**6. Existing exact finite mean.** For a fixed direction, the total offset lengths for which a hyperplane crosses edges of the box is \(2^{d-1}\sum_i 2\ell_{d,i}|u_i|\). Division by the entire admissible offset interval length \(2\sum_i\ell_{d,i}|u_i|\) gives \(\mathbb E[N_d\mid u]=2^{d-1}\). This is recalled as prior knowledge, not presented as an original mean theorem.

## Verification
The accompanying `verify.py` directly enumerates Boolean-cube edge boundaries at multiple offsets in dimension eight, checks the exact offset-integrated mean formula, and computes the two-point half-length example \(\mu=(\delta_{1/2}+\delta_{3/2})/2\) using 240-node Gaussian quadrature and numerical Legendre optimizers. Across five interior thresholds the heterogeneous rate is strictly below the cubical rate; the endpoint constants are reproduced. Run with `python verify.py` under Python 3 with NumPy and SciPy. The verifier reports `ALL_CHECKS_PASSED`. Finite computations test specific consequences; they are not an infinite-dimensional proof.

## Relationship to prior work
Kabluchko, Prochno and Thäle (2019, arXiv:1910.02676), Theorem 1.3 and Section 2.2, establish a quenched large-deviation principle for projections of **identically distributed** product measures, including the discrete uniform cube with \(\mathbb E\log\cosh(\lambda G)\). The cubical rate expression itself is consequently not new. Their theorem does not state the deterministic non-identically distributed side-length profile \(\int\mathbb E\log\cosh(\lambda tG)\mu(dt)\), the affine-section edge-boundary transformation, the strict side-profile stochastic ordering, or the sharp two-end probability constants. Replacing their common coordinate law by a mixture is not equivalent: this produces \(\mathbb E_G\log\mathbb E_{t\sim\mu}\cosh(\lambda tG)\), rather than the integral of logarithms here.

Swan (2016; arXiv repost 2018, arXiv:1808.09482) gives the exact expected number of vertices of suitably sampled cube slices, recovered in the preceding proof. Brandenburg, De Loera and Meroni (2023, arXiv:2304.14239) develop combinatorial chambers for general affine polytope sections, but not this asymptotic shape-ordering law. Results for central random cube sections correspond to the deterministic offset zero and cannot supply the uniform-offset limit distribution.

## Limitations
The theorem requires positive uniformly bounded half-lengths and weak convergence of their empirical law. The comparison concerns limiting logarithmic complexity, not finite-dimensional stochastic ordering or moments of \(N_d\). Non-orthogonal parallelotopes, anisotropic hyperplane orientation laws, and arbitrary convex polytopes are not covered. The literature comparison is bounded; unseen equivalent work, including work on triangular-array quenched large deviations and Boolean edge boundaries, remains a priority risk. No independent mathematical review has been performed.

## References
1. Z. Kabluchko, J. Prochno, C. Thäle, *A new look at random projections of the cube and general product measures*, arXiv:1910.02676, first submitted 2019-10-07; Bernoulli 27 (2021), 2117–2138. https://arxiv.org/abs/1910.02676
2. H. Swan, *Expected Number of Vertices of a Hypercube Slice*, American Mathematical Monthly 123 (2016), 600–604; arXiv:1808.09482, submitted 2018-08-28. https://arxiv.org/abs/1808.09482
3. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first submitted 2023-04-27. https://arxiv.org/abs/2304.14239
