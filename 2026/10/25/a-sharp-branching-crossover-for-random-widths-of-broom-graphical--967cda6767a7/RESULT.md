# A sharp branching crossover for random widths of broom graphical zonotopes

## Finding

Let \(B_{n,d}\) be the broom tree on \(n\) vertices with a hub, \(d\) pendent leaves incident to the hub, and one further path (possibly of length one) incident to the hub. Consider the centered graphical zonotope
\[
Z(B_{n,d})=\sum_{\{i,j\}\in E(B_{n,d})}\left[-\frac{e_i-e_j}{2},\frac{e_i-e_j}{2}\right]
\subset\left\{x\in\mathbb R^n:\sum_i x_i=0\right\}.
\]
Its width \(W_{n,d}\) is measured in a direction uniform on the ambient unit sphere. Let \(d=d_n\) be any nonnegative integer sequence with \(d_n=o(n)\), and put
\[
\mu=\frac{2}{\sqrt\pi},\quad
\sigma^2=\frac83+\frac{4\sqrt3-14}{\pi}>0,\quad
c=\frac13+\frac{2\sqrt3-4}{\pi}>0,
\]
\[
\psi(z)=\sqrt{\frac2\pi}e^{-z^2/2}+z(2\Phi(z)-1)-\mu,
\]
where \(\Phi\) is the standard normal distribution function. Write \(G\) for a standard normal variable and \(Z\) for an independent \(N(0,\sigma^2)\) variable. Then:

1. If \(d_n/\sqrt n\to\beta\in[0,\infty)\),
\[
W_{n,d_n}-\mu\sqrt n\ \Longrightarrow\ Z+\beta\psi(G).
\tag{1}
\]
The limit is Gaussian exactly when \(\beta=0\). At every \(\beta>0\), it is a genuine non-Gaussian convolution. Its variance is \(\sigma^2+c\beta^2\).
2. If \(d_n/\sqrt n\to\infty\) while \(d_n=o(n)\),
\[
\frac{\sqrt n}{d_n}\left(W_{n,d_n}-\mu\sqrt n\right)
\ \Longrightarrow\ \psi(G),
\tag{2}
\]
which is non-Gaussian, with variance \(c\).

For every admissible finite \(n,d\), the exact mean is
\[
\mathbb E W_{n,d}=(n-1)\frac{\sqrt2\,\Gamma((n-1)/2)}{\sqrt\pi\,\Gamma(n/2)}
=\mu\sqrt n+O(n^{-1/2}).
\tag{3}
\]
The already-known general moment formula also yields the exact identity
\[
\operatorname{Var}(W_{n,d})=
\operatorname{Var}(W_{n,0})+\frac{c\,d(d-1)}{n-1};
\tag{4}
\]
(4) corroborates, but is not the new distributional claim. The sharp transition \(d\asymp\sqrt n\) in (1)--(2) is the finding.

## Assumptions and scope

Take \(n\ge4\), \(0\le d\le n-2\), vertex labels \(0,1,\ldots,n-1\), hub \(0\), leaves \(1,\ldots,d\), and consecutive path vertices \(d+1,\ldots,n-1\). The edges are \(\{0,j\}\) for \(1\le j\le d\), the connector \(\{0,d+1\}\), and \(\{i,i+1\}\) for \(d+1\le i\le n-2\). Here \(d=0\) is an ordinary path. The Euclidean metric is inherited from \(\mathbb R^n\), the direction is Haar-uniform on the sphere in the \((n-1)\)-dimensional zero-sum subspace, and widths use the centered half-edge-segment convention displayed above. All limits allow arbitrary integer sequences satisfying the indicated hypotheses; there is no assumption of monotonicity. The theorem does not cover a hub occupying a positive fraction of vertices.

## Proof

**Exact support function.** Minkowski additivity of support functions gives, for every unit direction \(u\) in the zero-sum subspace,
\[
W_{n,d}(u)=\sum_{\{i,j\}\in E(B_{n,d})}|u_i-u_j|.
\tag{5}
\]
Take independent \(G_0,\ldots,G_{n-1}\sim N(0,1)\), their mean \(\bar G_n\), and \(R_n=(\sum_i(G_i-\bar G_n)^2)^{1/2}\). Centered Gaussian projection divided by \(R_n\) is uniform on the relevant sphere. Since differences erase \(\bar G_n\), (5) gives the distributional identity
\[
W_{n,d}\stackrel d=\frac{S_{n,d}}{R_n},\qquad
S_{n,d}=\sum_{\{i,j\}\in E(B_{n,d})}|G_i-G_j|.
\tag{6}
\]
The Gaussian edge difference is \(N(0,2)\), hence has mean \(\mu=2/\sqrt\pi\), and its conditional mean given \(G_0=z\) is \(\mathbb E|z-G_1|=\mu+\psi(z)\). This proves \(\mathbb E\psi(G_0)=0\).

**Conditional hub decomposition.** Separate the \(d\) hub-to-leaf edges, the one connector, and the \(n-d-2\) edges within the long path. Let
\[
A_n=\sum_{i=d+1}^{n-2}(|G_i-G_{i+1}|-\mu),\quad
H_n=\sum_{j=1}^{d}\bigl(|G_0-G_j|-\mu-\psi(G_0)\bigr),\quad
C_n=|G_0-G_{d+1}|-\mu.
\]
Consequently
\[
S_{n,d}=\mu(n-1)+A_n+d\psi(G_0)+H_n+C_n.
\tag{7}
\]
The leaf terms in \(H_n\), conditional on \(G_0\), are independent, centered, and have uniformly integrable finite second moments. Their unconditional cross terms vanish, so \(\mathbb E H_n^2\le2d\). Also \(\mathbb E C_n^2<\infty\). Thus \(H_n/\sqrt n\to0\) and \(C_n/\sqrt n\to0\) in \(L^2\) whenever \(d=o(n)\).

**Joint central limit theorem for the path and the radius.** Put \(Q_n=n^{-1/2}\sum_{i=0}^{n-1}(G_i^2-1)\). The summands in \(A_n\) form a stationary one-dependent sequence, and the relevant quadratic summands in \(Q_n\) can be coupled to the same stationary one-dependent vector sequence. The \(d+1=o(n)\) excluded coordinates alter \(Q_n\) by \(o_{L^2}(1)\). Joint convergence follows from the standard finite-moment blocking proof for one-dependent sequences: divide the long path into independent blocks of length \(b_n\to\infty\), with \(b_n=o(n)\), separate neighboring blocks by one deleted summand, use an \(O(n/b_n)\) variance estimate for the deleted part and the fourth-moment \(O(b_n^2)\) bound for each retained block to verify Lindeberg by taking \(b_n=o(n)\). Apply the Cramér--Wold device.

The covariance entries can be calculated without limiting approximations. For two distinct incident edges, the corresponding Gaussian differences have correlation of magnitude \(1/2\), and
\[
\operatorname{Cov}(|G_1-G_2|,|G_2-G_3|)
=\frac13+\frac{2\sqrt3-4}{\pi}=c.
\tag{8}
\]
For a single edge, \(\operatorname{Var}(|G_1-G_2|)=2-4/\pi\), and a direct Gaussian change of variables gives
\[
\operatorname{Cov}(|G_1-G_2|,G_1^2-1)
=\operatorname{Cov}(|G_1-G_2|,G_2^2-1)=\mu/2.
\tag{9}
\]
It follows that
\[
\left(\frac{A_n}{\sqrt n},Q_n\right)
\Longrightarrow(A,Q),
\]
where \((A,Q)\) is centered Gaussian with
\[
\operatorname{Var}A=2-\frac4\pi+2c,\quad
\operatorname{Var}Q=2,\quad
\operatorname{Cov}(A,Q)=\mu.
\tag{10}
\]
The limiting vector is independent of \(G_0\): replace \(Q_n\) by its long-path contribution, which is independent of \(G_0\) for every \(n\), and note that the omitted terms vanish in \(L^2\).

**Spherical normalization and critical limit.** Since \(n\bar G_n^2=O_{\mathbb P}(1)\),
\[
R_n^2=n+\sqrt n\,Q_n-n\bar G_n^2,
\qquad
\frac{\sqrt n}{R_n}=1-\frac{Q_n}{2\sqrt n}+o_{\mathbb P}(n^{-1/2}).
\tag{11}
\]
If \(d/\sqrt n\to\beta<\infty\), insert (7) into (6), use (11), and collect the leading terms:
\[
W_{n,d}-\mu\sqrt n
=\frac{A_n}{\sqrt n}+\frac d{\sqrt n}\psi(G_0)-\frac\mu2Q_n+o_{\mathbb P}(1).
\tag{12}
\]
Therefore the limit is \(Z+\beta\psi(G_0)\), with \(Z=A-\mu Q/2\). By (10),
\[
\operatorname{Var}Z=(2-4/\pi+2c)+\mu^2/2-\mu^2
=\frac83+\frac{4\sqrt3-14}{\pi}=\sigma^2.
\]
The conditional-mean variance identity yields \(\operatorname{Var}\psi(G)=c>0\), since two edges from a common hub are conditionally independent given that hub and have covariance \(c\). The function \(\psi\) is even, bounded below by \(-\mu\), unbounded above, and nonconstant. Consequently \(\psi(G)\) is not Gaussian; for \(\beta>0\) its convolution with independent Gaussian \(Z\) cannot be Gaussian by the Gaussian decomposition theorem. At \(\beta=0\), (12) is Gaussian.

**Supercritical limit.** When \(d\gg\sqrt n\) but \(d=o(n)\), write \(S_{n,d}=\mu(n-1)+d\psi(G_0)+O_{\mathbb P}(\sqrt n+\sqrt d)\) using (7) and the variance bound for \(A_n\). Divide by \(R_n\), whose ratio to \(\sqrt n\) converges to one. Multiply the centered width by \(\sqrt n/d\). The centered path term is \(O_{\mathbb P}(\sqrt n/d)\to0\), the leaf-noise term is \(O_{\mathbb P}(1/\sqrt d)\to0\), and the radial-normalization correction is \(O_{\mathbb P}(\sqrt n/d)\to0\). Slutsky's theorem proves (2).

**Exact mean and variance consistency.** The radius \(R_n\) and uniform spherical direction are independent, with \(\mathbb E R_n=\sqrt2\,\Gamma(n/2)/\Gamma((n-1)/2)\). Taking expectations of (6) using Gaussian radial independence proves (3), including its gamma-ratio expansion. For (4), the published general graphical-zonotope width-variance identity uses the incident-edge pair count \(q(B_{n,d})=n-2+d(d-1)/2\) and \(q(B_{n,0})=n-2\); its difference is exactly \(c d(d-1)/(n-1)\). This gives the variance limits stated with (1) and (2) independently of weak-convergence moment arguments.

## Verification

A reproducible standalone program, `check.py`, checks the exact support-function formula (5) against explicit enumeration of all segment-sign sums in \(384\) small cases, evaluates \(\mathbb E\psi(G)\) and \(\mathbb E\psi(G)^2=c\) by high-precision one-dimensional quadrature, and samples three distinct growth regimes as numerical diagnostics. Run `python3 check.py` with NumPy and SciPy installed. The diagnostics are finite tests; they do not prove the asymptotic limits, which follow from the analytic argument.

## Relationship to prior work

The graphical-zonotope framework and its combinatorial normal-fan structure are developed by Padrol, Pilaud and Poullot (arXiv:2111.12422), and an earlier polyhedral study of zonotope computations appears in Deza and Pournin (arXiv:1912.02439). The published *Sharp width-variance extremizers among tree graphical zonotopes* derives exact first and second spherical-width moments, including path and star extremizers, but does not establish the distribution of their widths. Equation (4), along with all first-two-moment consequences here, is already covered by that work. The present theorem instead determines the complete weak-limit crossover at the square-root branching scale, including independent Gaussian and non-Gaussian components. Schneider's random-zonotope limit theory (arXiv:2202.06774) concerns convex bodies generated by independently random segments, not the random direction of a fixed graph-determined zonotope. These mathematical distinctions do not exclude unindexed earlier work on graph-indexed Gaussian absolute variations.

## Limitations

The result concerns one-hub broom *trees* under the standard Euclidean metric, not general trees or weighted root segments. Only sequences \(d=o(n)\) are covered; when the hub degree is proportional to \(n\), other radial-normalization effects may enter. The statement describes weak convergence and first-two-moment limits, not a local limit theorem, explicit error rate, or stochastic ordering. Historical coverage has been checked through the closest indexed results and relevant primary papers, but an equivalent theorem could exist in less-indexed Gaussian graphical-functionals literature. No independent mathematical audit has been performed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first submitted 24 November 2021, https://arxiv.org/abs/2111.12422 (graphical constructions, normal fans and deformation theory).
2. A. Deza and L. Pournin, *A Linear Optimization Oracle for Zonotope Computation*, arXiv:1912.02439, first submitted 5 December 2019, https://arxiv.org/abs/1912.02439 (zonotope optimization framework).
3. R. Schneider, *Random Zonotopes and Valuations*, arXiv:2202.06774, first submitted 14 February 2022, https://arxiv.org/abs/2202.06774 (random-generator, rather than random-direction, asymptotic theory).
4. *Sharp width-variance extremizers among tree graphical zonotopes*, published 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269 (exact first and second directional-width moments and tree extremizers).
