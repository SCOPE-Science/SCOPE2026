# Finite-forest polarization bias on a heterogeneous three-person group

## Finding

In the heterogeneous-contribution Friedkin–Johnsen projection of a single three-person hyperedge [1], true stationary polarization does **not** depend on the distribution of influence among the three people. Yet the usual rooted-forest plug-in estimate of polarization has a strictly positive, contribution-dependent expectation bias. With intrinsic opinions \((0,0,1)\), group weight \(h>0\), positive contribution fractions \(\gamma_1+\gamma_2+\gamma_3=1\), and \(T\geq1\) independent full rooted-forest samples, the exact identities are

\[
P=\frac{2}{3(1+h)^2},\qquad
\mathbb E\widehat P_T
=\frac{2}{3(1+h)^2}\left(1+\frac{h(1+\gamma_3)}{T}\right).
\]

In particular, \(\mathbb E\widehat P_T/P=1+h(1+\gamma_3)/T\): **at any fixed finite sample size the relative expected overstatement diverges with group-interaction strength**, although the true polarization decreases as \(h^{-2}\). Increasing \(\gamma_3\) increases estimated expected polarization while leaving true polarization unchanged.

For any finite projected directed network and independent complete rooted-forest samples, an exact general bias formula and an unbiased two-sample cross-product estimator are given below. These results concern expectation and do not claim concentration in relative error when true polarization approaches zero.

## Assumptions and scope

There are three labeled people \(1,2,3\) in one hyperedge of weight \(h>0\). Fix strictly positive contribution fractions \(\gamma_i\), with sum one. The directed projection of [1, equation (4)] assigns the arc from \(i\) to \(j\), for distinct indices, weight \(w_{ij}=h\gamma_j\). The directed out-degree Laplacian is

\[
L=h(I-\mathbf 1\gamma^{\mathsf T}),\quad
\gamma=(\gamma_1,\gamma_2,\gamma_3)^{\mathsf T}.
\]

A fixed intrinsic-opinion vector \(x\in[0,1]^3\) induces equilibrium expressed opinions \(z=(I+L)^{-1}x\). For \(m\) opinions \(y\), let \(C_m=I-\mathbf1\mathbf1^{\mathsf T}/m\) and let \(P(y)=\lVert C_my\rVert_2^2\), the *unnormalized* mean-centered squared polarization used by [1]. When the argument is omitted, \(P=P(z)\).

A rooted converging forest is a spanning directed acyclic graph in which every vertex has at most one outgoing edge, all arrows point toward each component's unique root, and the forest weight is the product of its arc weights (empty product one). Draw each forest with probability proportional to its weight, independently across draws; \(Y_i=x_{r(i)}\) is the intrinsic opinion at the root reached from vertex \(i\). The matrix-forest identity used in [1] gives \(\mathbb EY=z\). For independent copies \(Y^{(1)},\dots,Y^{(T)}\), put \(\overline Y_T=T^{-1}\sum_sY^{(s)}\) and \(\widehat P_T=P(\overline Y_T)\).

The general bias and correction statements below require only finitely many vertices, \(x\in[0,1]^m\), and independent identically distributed rooted-opinion vectors satisfying \(\mathbb EY=z\). They do not require independent root opinions *within* one sampled forest.

## Proof

**1. Exact equilibrium and true contribution invariance.** Since \(\gamma^{\mathsf T}\mathbf 1=1\), \(Q=\mathbf1\gamma^{\mathsf T}\) is a projection. Consequently

\[
(I+L)^{-1}=\frac{I+hQ}{1+h},\qquad
z_i=\frac{x_i+h\sum_j\gamma_jx_j}{1+h}.
\]

All expressed opinion differences equal \((x_i-x_j)/(1+h)\). Centering annihilates the rank-one term, so \(P(z)=P(x)/(1+h)^2\) for *every* \(x\), independent of all influence fractions. For \(x=(0,0,1)\), \(P(x)=2/3\).

**2. Exact forest normalization.** On three labeled vertices there are exactly sixteen rooted converging forests: one with zero arcs, six with one arc and nine directed rooted trees with two arcs. The respective total weights are \(1\), \(2h\), and \(h^2\). For the last total, fix root \(r\): the three directed rooted trees have summed weight

\[
h^2\gamma_r(\gamma_1+\gamma_2+\gamma_3)=h^2\gamma_r.
\]

Summing over roots gives \(h^2\). Therefore the normalization is \(Z=(1+h)^2\).

**3. Exact one-draw polarization.** For \(x=(0,0,1)\), write \(K\) for the number of vertices whose sampled forest root is vertex 3. Then \(Y\) contains exactly \(K\) ones, and

\[
P(Y)=\frac{K(3-K)}{3}.
\]

Hence \(P(Y)=2/3\) precisely when \(K=1\) or \(K=2\). The zero-arc forest contributes weight 1 to this event. Of the one-arc forests, the four arcs \(1\to2\), \(2\to1\), \(1\to3\), and \(2\to3\) contribute total weight

\[
h(\gamma_2+\gamma_1+2\gamma_3)=h(1+\gamma_3).
\]

The remaining two one-arc forests have \(K=0\); each two-arc tree has \(K=0\) or \(K=3\). Thus

\[
\mathbb EP(Y)=\frac{2[1+h(1+\gamma_3)]}{3(1+h)^2}.
\]

Subtracting the true polarization gives exact one-draw bias

\[
\mathbb EP(Y)-P(z)=\frac{2h(1+\gamma_3)}{3(1+h)^2}>0.
\]

**4. General independent-forest bias identity.** For any finite network, independent samples have centered errors \(C_m(Y^{(s)}-z)\) of mean zero. Expand the squared norm of their average. All cross terms from distinct samples have zero expectation, yielding

\[
\mathbb E\widehat P_T-P(z)
=\frac1T\mathbb E\lVert C_m(Y-z)\rVert_2^2
=\frac{\operatorname{tr}(C_m\operatorname{Cov}(Y)C_m)}T\geq0.
\]

Using the result of step 3 proves the displayed exact three-person expression and its diverging relative factor. The effect of increasing \(\gamma_3\) is strictly positive at fixed \(h,T\), despite invariance in step 1.

**5. Unbiased correction using the same forests.** For \(T\ge2\), define

\[
U_T=\frac{1}{T(T-1)}\sum_{s\ne t}
\left\langle C_mY^{(s)},C_mY^{(t)}\right\rangle.
\]

Independence across forests gives \(\mathbb EU_T=\langle C_mz,C_mz\rangle=P(z)\), and direct expansion gives the computable identity

\[
U_T=\frac{T}{T-1}\widehat P_T-
\frac{1}{T(T-1)}\sum_{s=1}^TP(Y^{(s)}).
\]

For \(x\in[0,1]^m\), \(\lVert C_mY\rVert_2\le\sqrt m/2\) (the elementary bounded-sample-variance inequality). Thus each cross-product kernel lies in \([-m/4,m/4]\). Replacing one independent forest changes \(U_T\) by at most \(m/T\). McDiarmid's bounded-differences inequality therefore supplies the nonasymptotic absolute-error bound

\[
\Pr\{|U_T-P(z)|\ge\varepsilon\}
\le2\exp\!\left(-\frac{2T\varepsilon^2}{m^2}\right)
\qquad(\varepsilon>0).
\]

The correction is not guaranteed nonnegative on each sample and requires independent complete-forest realizations.

## Verification

Run `python forest_polarization_check.py` in the directory containing the embedded file. The standalone standard-library program enumerates all sixteen directed rooted forests with exact rational weights; independently solves the three-dimensional equilibrium linear system by rational Gaussian elimination; checks marginal root expectations, normalization, polarizations, the exact bias formula, the cross-forest estimator, and the finite-\(T\) ratio over several positive rational parameter sets and distinct intrinsic opinions. Its recorded deterministic output is `PASS: 1230 exact rational assertions`. No Monte Carlo approximations are used for these computations. The proof covers all admissible positive real weights and all positive integers \(T\); the finite test is corroboration, not an infinite proof.

## Relationship to prior work

Xu and Zhang [1] define the contribution-dependent directed projection, stationary FJ equation, forest-root sampling scheme, and plug-in polarization estimate (Algorithm 1, step 22–23). They explicitly show unbiasedness of the sampled **opinion coordinates**; no assertion that the squared polarization plug-in is unbiased is attributed to them. Their toy and empirical comparisons motivate asking whether finite sampling can itself introduce contribution-dependent polarization comparisons. The present claim is the exact three-person separation and its high-coupling scaling, plus a direct unbiased cross-forest alternative; it does not claim novelty for Jensen's inequality, U-statistics, or the matrix-forest theorem.

Neumann, Dong, and Peng [2] study sublinear estimation of network quantities through distinct local-query and personalized-PageRank techniques; their work addresses additive approximation rather than this specific directed single-hyperedge forest-sampler bias. Sun, Sun, Zhou, and Zhang [3] use partial rooted forests, a plug-in squared-opinion estimator, and additive-error guarantees for undirected networks, but do not establish the directed three-person model's exact group-contribution bias factor in the inspected sections. Either general purpose unbiased-quadratic-estimation theory or an unlocated specialized forest-sampling treatment could imply part of the result; no priority claim is made beyond the inspected sources.

## Limitations

The exact closed-form factor concerns a *single three-person hyperedge*, one intrinsic dissenter, and the stated directed projection. Other network structures can have different bias laws. The general correction requires iid forest draws; dependent sampling requires a separate covariance analysis. Unbiasedness is not a guarantee of nonnegative output or of finite relative error when \(P\) is tiny. In the high-influence limit the **absolute** plug-in bias still vanishes, even while its ratio to true polarization diverges. No global claim about causal changes in real-world social polarization or about the empirical results of [1] is made.

## References

[1] W. Xu and Z. Zhang, *Linear Opinion Dynamics Model with Higher-Order Interactions*, arXiv:2310.05689v1, first submitted 2023-10-09, https://arxiv.org/html/2310.05689 . In particular equations (2), (4), (10)–(13) and Algorithm 1.

[2] S. Neumann, Y. Dong and P. Peng, *Sublinear-Time Opinion Estimation in the Friedkin–Johnsen Model*, arXiv:2404.16464v1, first submitted 2024-04-25, https://arxiv.org/pdf/2404.16464 .

[3] H. Sun, Y. Sun, X. Zhou and Z. Zhang, *Fast Computation and Optimization for Opinion-Based Quantities of Friedkin-Johnsen Model*, NeurIPS 2025, https://proceedings.neurips.cc/paper_files/paper/2025/file/3660799b242a69dbc9cb8685cdf5ad64-Paper-Conference.pdf , section 5 and Algorithm 1.
