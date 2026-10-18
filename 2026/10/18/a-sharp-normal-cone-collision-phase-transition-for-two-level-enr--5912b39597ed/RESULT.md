# A sharp normal-cone collision phase transition for two-level enriched chain polytopes

## Finding
For integers \(p,q\geq1\), let \(P_{p,q}\) be the ordinal sum of an antichain of size \(p\) and an antichain of size \(q\), and let \(K_{p,q}\subset\mathbb R^{p+q}\) be its **standard-coordinate enriched chain polytope**. Thus
\[
K_{p,q}=\operatorname{conv}\bigl(([-1,1]^p\times\{0\}^q)\cup(\{0\}^p\times[-1,1]^q)\bigr).
\]
This polytope has precisely \(2^p+2^q\) vertices. For a standard Gaussian objective \(G\), write \(\pi_{p,q}(v)\) for the probability that \(v\) is its unique exposed vertex. Put
\[
\rho_{p,q}=\Pr\left(\sum_{i=1}^{p}|G_i|>\sum_{j=p+1}^{p+q}|G_j|\right).
\]
Every vertex in the first cube has Gaussian normal-cone probability \(2^{-p}\rho_{p,q}\); every vertex in the second cube has probability \(2^{-q}(1-\rho_{p,q})\). In particular, the probability \(C_2(p,q)\) that two independent uniform spherical directions expose the same vertex is exactly
\[
C_2(p,q)=2^{-p}\rho_{p,q}^{\,2}+2^{-q}(1-\rho_{p,q})^{2}.
\]

For any integer sequence \(p_N+q_N=N\) with \(p_N/N\to\alpha\in(1/2,1)\), define
\[
M(s)=2e^{s^2/2}\Phi(s),\qquad
I(\alpha)=\sup_{s\geq0}\bigl\{-\alpha\log M(-s)-(1-\alpha)\log M(s)\bigr\}.
\]
Here \(\Phi\) is the standard normal distribution function. The angular collision exponent has the exact limit
\[
\boxed{\displaystyle
-\lim_{N\to\infty}\frac1N\log C_2(p_N,q_N)
=\min\bigl\{\alpha\log2,(1-\alpha)\log2+2I(\alpha)\bigr\}.}
\]
There is **exactly one** \(\alpha_*\in(1/2,1)\) satisfying
\[
2I(\alpha_*)=(2\alpha_*-1)\log2.
\]
A numerical solution is \(\alpha_*\approx0.6886330609\). For \(1/2<\alpha<\alpha_*\), the smaller cube's vertices dominate the collision probability at exponential order despite being exposed with exponentially small total probability. For \(\alpha_*<\alpha<1\), the larger cube's vertices dominate. At \(\alpha=\alpha_*\) both contributions have the same logarithmic exponential rate; their subexponential ratio is not claimed. This establishes a sharp phase transition in an intrinsic Euclidean angular invariant within a classical family of lattice polytopes.

An exact finite benchmark is
\[
\rho_{2,1}=\frac4\pi\arcsin\frac1{\sqrt3},\qquad
C_2(2,1)=\frac14\rho_{2,1}^{\,2}+\frac12(1-\rho_{2,1})^2.
\]

## Assumptions and scope
All coordinates carry their standard Euclidean metric; no affine rescaling or lattice-equivalent realization is substituted. A uniform spherical direction is equivalent to a standard Gaussian direction for exposure events. The integers \(p,q\) are positive. The asymptotic exponent requires \(p_N/N\to\alpha\in(1/2,1)\), with no restriction on the rate of convergence. All logarithms in the rate function are natural. The Gaussian objective has a unique maximizer almost surely. At \(p=q\), symmetry gives \(\rho_{p,p}=1/2\), hence \(C_2(p,p)=2^{-p-1}\).

## Proof
**Identification and exact angular law.** An enriched antichain vector has coordinates in \(\{-1,0,1\}\) and support an antichain. Since each element of the lower level is comparable with each element of the upper level, every antichain is contained in one level. Taking convex hulls gives the displayed join of two cubes. Every signed full-support corner of each cube is a vertex: a linear functional of sufficiently large magnitude on its own coordinate block uniquely exposes it. The two vertex sets are disjoint.

For \(g=(g',g'')\), the support function is
\[
h_{K_{p,q}}(g)=\max\left\{\sum_{i=1}^{p}|g'_i|,\sum_{j=1}^{q}|g''_j|\right\}.
\]
Conditional on the absolute Gaussian coordinates, the signs in each block are independent uniform signs. When the first block wins, each of its \(2^p\) corners is exposed with equal conditional probability; analogously for the other block. Since both block sums have continuous distributions, ties have probability zero. The exact vertex probabilities follow. Summing their squares proves the exact two-direction collision formula.

**Large-deviation rate.** Set \(X=|G_1|\). Direct Gaussian integration gives \(\mathbb Ee^{sX}=M(s)=2e^{s^2/2}\Phi(s)\), finite for every real \(s\). For \(p_N/N\to\alpha>1/2\), the scaled cumulant generating function of the difference of the two block sums is
\[
\Lambda_\alpha(t)=\alpha\log M(t)+(1-\alpha)\log M(-t).
\]
It is everywhere finite, differentiable, and strictly convex; its derivative at zero is \((2\alpha-1)\sqrt{2/\pi}>0\). The standard exponential-tilting proof of Cramér's large-deviation theorem (equivalently, the differentiable cumulant-generating-function theorem applied to this triangular array) gives
\[
\lim_{N\to\infty}\frac1N\log\Pr(S_{q_N}\ge S_{p_N})=-I(\alpha),
\]
where \(S_k\) denotes the sum of \(k\) independent half-normal variables. In detail, the Chernoff inequality at each \(s\ge0\) gives the upper bound; tilt the independent half-normals with densities proportional to \(e^{-sX}\) in the first block and \(e^{sX}\) in the second, choosing the unique \(s>0\) that makes their limiting mean difference zero. Under this tilted law, intervals of width \(o(N)\) about zero have subexponential probability by the law of large numbers, giving the matching lower bound. Moving the center slightly to the negative side and then letting that displacement tend to zero handles the strict inequality. Therefore
\[
1-\rho_{p_N,q_N}=\exp\bigl(-NI(\alpha)+o(N)\bigr),\qquad
\rho_{p_N,q_N}=1-o(1).
\]
Inserting these into the exact collision formula gives the minimum of the two exponential costs.

**Existence and uniqueness of the transition.** Write
\[
f(\alpha,s)=-\alpha\log M(-s)-(1-\alpha)\log M(s).
\]
For \(1/2<\alpha<1\), the strict convexity of \(\log M\) implies that \(f\) is strictly concave in \(s\); its derivative at zero is positive, and \(f(\alpha,s)\to-\infty\) as \(s\to\infty\). Therefore \(I(\alpha)=f(\alpha,s_\alpha)\) has a unique optimizer \(s_\alpha>0\), smooth in \(\alpha\). Both tilted expectations \((\log M)'(s)\) and \((\log M)'(-s)\) are positive, so the mixed derivative
\[
\partial_{s\alpha}f(\alpha,s)=(\log M)'(-s)+(\log M)'(s)>0.
\]
Implicit differentiation of the stationarity condition yields
\[
I''(\alpha)=-\frac{(\partial_{s\alpha}f(\alpha,s_\alpha))^2}{\partial_{ss}f(\alpha,s_\alpha)}>0.
\]
At \(\alpha=1/2\), \(I=0\) and the right derivative is zero. As \(\alpha\uparrow1\), \(I(\alpha)\to\infty\): for any fixed positive \(s\), the defining supremum tends at least to \(-\log M(-s)\), and this quantity grows without bound as \(s\to\infty\). Thus the strictly convex function \(2I(\alpha)-(2\alpha-1)\log2\) starts from zero with negative right derivative, tends to infinity, and has exactly one zero in \((1/2,1)\). Its sign gives the claimed two regimes.

**Exact three-dimensional benchmark.** For \((p,q)=(2,1)\), the probability that the one-coordinate cube wins is \(8\Pr(G_1>0,G_2>0,G_3-G_1-G_2>0)\). The three centered Gaussian forms have correlations \(0,-1/\sqrt3,-1/\sqrt3\). The standard trivariate Gaussian orthant identity gives this probability as \(1-4\arcsin(1/\sqrt3)/\pi\), proving the displayed exact value for \(\rho_{2,1}\).

## Verification
Execute `python CHECK.py` with NumPy and SciPy installed. The checker exhaustively compares explicit vertex support maximization against the block-sum formula on 16 block-size pairs, using 100 independent test directions per pair. It independently evaluates the exact three-dimensional normal-cone probability using a one-dimensional half-normal convolution integral, checks 131072 quasi-random exposures, and numerically verifies the unique-root equation and an enclosing bracket for the rate transition. These finite and numerical checks corroborate the exact and asymptotic proofs; they are not substitutes for the large-deviation or uniqueness arguments.

## Relationship to prior work
Okada and Tsuchiya, *Two enriched poset polytopes* (first publicly posted 2020-03-27; arXiv:2003.12271), supply the enriched chain-polytope framework, its antichain-coordinate construction, and lattice-theoretic correspondences. Kohl, Olsen, and Sanyal, *Unconditional reflexive polytopes* (arXiv:1906.01469), study the broader unconditional-chain framework and its combinatorial and algebraic structure. Their constructions are not claimed as new here. Cramér exponential tilting and the trivariate normal orthant identity are standard probability tools. The contribution here is the complete two-level Gaussian angular spectrum and the uniquely located competition transition between the two vertex orbits' collision exponents. Related geometric results on radii, volumes, and ellipsoids do not themselves assert a collision probability or its large-deviation competition.

## Limitations
The theorem treats standard-coordinate enriched chain polytopes of *complete* two-level posets and angular collisions of two independent isotropic directions. It does not classify arbitrary posets, arbitrary affine realizations, or collision moments of other orders. The numerical value of the transition is an approximation; uniqueness is proved analytically. The transition statement identifies leading exponential rates, not the relative polynomial prefactor exactly at the critical parameter. Bibliographic searches cannot exclude an equivalent earlier result under different Gaussian large-deviation or Hanner-polytope terminology. No independent mathematical audit has been performed.

## References
1. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271 (initial public version 2020-03-27), https://arxiv.org/abs/2003.12271.
2. F. Kohl, M. Olsen, and R. Sanyal, *Unconditional reflexive polytopes*, arXiv:1906.01469 (initial public version 2019-06-03), https://arxiv.org/abs/1906.01469.
3. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, Israel J. Math. 237 (2020), 485–500; arXiv:1812.02097.
4. Standard results: Cramér's large-deviation theorem for exponentially integrable independent variables and the centered trivariate Gaussian orthant-probability identity.
