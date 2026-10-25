# A sharp endpoint normal-cone boundary anomaly for path symmetric edge polytopes

## Finding
For every integer \(n\ge3\), let \(P_n\) be the convex hull of the \(2(n-1)\) roots \(\pm(e_j-e_{j+1})\), for \(1\le j<n\), in the Euclidean hyperplane \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\). Let \(\omega_n\) be the normalized spherical measure of the outward normal cone at the oriented endpoint root \(e_1-e_2\). Then

\[
\lim_{n\to\infty}n^{4/3}(\log n)^{1/3}
\left(2\omega_n-\frac1{n-1}\right)
=\frac{\sqrt3\,\Gamma(4/3)}{2\pi^{1/3}}.
\]

The limit is strictly positive (approximately \(0.528026236281815\)). Equivalently,
\[
2\omega_n=\frac1n+
\frac{\sqrt3\,\Gamma(4/3)}{2\pi^{1/3}}
\frac{1+o(1)}{n^{4/3}(\log n)^{1/3}}.
\]
The opposite oriented endpoint root and both orientations of the opposite path-end edge have the same angle. Thus an endpoint root has a positive sharp correction to the uniform-vertex benchmark \(1/[2(n-1)]\), despite all tree symmetric edge polytopes being combinatorially crosspolytopes. No assertion of the same correction for interior roots is made.

## Assumptions and scope
All Euclidean geometry is intrinsic to the *canonical root embedding* in \(H_n\), with the standard inherited inner product. A normalized spherical normal-cone angle is the probability of exposure by a direction uniform on the unit sphere of \(H_n\). The symbol \(\Phi\) denotes the standard normal distribution function, \(\overline\Phi=1-\Phi\), and \(\Gamma\) is Euler's gamma function. Probabilistic ties have probability zero. The asymptotic assertion concerns integer \(n\to\infty\); the exact identities in the proof hold for every \(n\ge3\).

## Proof
**1. Gaussian support-function model.** Let \(G_1,\ldots,G_n\) be independent standard normal variables and define \(X_j=(G_j-G_{j+1})/\sqrt2\), \(1\le j<n\). The orthogonal projection of the Gaussian vector onto \(H_n\), divided by its norm, has uniform spherical direction. Projection and common positive normalization do not change comparisons of scalar products with roots. Consequently
\[
2\omega_n=q_n:=\Pr\{|X_1|>\max_{2\le j<n}|X_j|\}.
\]
The factor two follows from simultaneous sign reversal of the Gaussian vector.

**2. Exact cycle-closure identity.** Add the closing increment \(X_n=(G_n-G_1)/\sqrt2\). The vector of the \(n\) absolute cyclic increments is invariant under rotation of its indices, so each increment is the unique absolute maximum with probability \(1/n\). Splitting the path-end event according to whether the closing increment exceeds the first yields the exact identity
\[
q_n=\frac1n+E_n,\quad
E_n=\Pr\bigl\{|X_n|>|X_1|>\max_{2\le j<n}|X_j|\bigr\}.
\]
In particular \(E_n>0\). This identity is not an asymptotic approximation.

**3. Conditional Gaussian tail.** Set \(T=|X_1|\), with density \(f(t)=2\phi(t)\), tail \(p(t)=2\overline\Phi(t)\) for \(t>0\), and \(\phi\) the standard normal density. Since \(\operatorname{Corr}(X_1,X_n)=-1/2\), conditioning on either sign of \(X_1\) gives
\[
a(t):=\Pr\{|X_n|>t\mid T=t\}
=\overline\Phi(t/\sqrt3)+\overline\Phi(\sqrt3t).
\]
Mills' ratio implies
\[
a(t)\sim\frac{\sqrt3}{\sqrt{2\pi}\,t}e^{-t^2/6},\qquad
p(t)\sim\frac{\sqrt{2/\pi}}t e^{-t^2/2},
\]
and hence, as \(p(t)\downarrow0\),
\[
a(t)\sim \frac{\sqrt3}{2\pi^{1/3}}
 p(t)^{1/3}\bigl(\log(1/p(t))\bigr)^{-1/3}.
\]

**4. Interior maximum and exceptional adjacent increments.** For \(n\ge6\), write \(M_n=\max_{3\le j\le n-2}|X_j|\). All increments defining \(M_n\) depend only on \(G_3,\ldots,G_{n-1}\) and are independent of \((X_1,X_n)\). They form a one-dependent stationary Gaussian-difference sequence. At the unique level \(t=t_n(u)\) satisfying \(np(t)=u\), for each fixed \(u>0\), its number of exceedances converges to a Poisson variable of mean \(u\), and therefore
\[
\Pr\{M_n<t_n(u)\}\longrightarrow e^{-u}.
\]
To verify the required Poisson approximation, nonadjacent exceedance indicators are independent, and for adjacent standardized increments their absolute-value joint exceedance probability obeys
\[
\Pr\{|X_j|>t,|X_{j+1}|>t\}
\le4\overline\Phi(2t/\sqrt3)
=O(t^{-1}e^{-2t^2/3}).
\]
Thus the dependency-neighborhood Poisson error is bounded by a constant multiple of \(np(t)^2+n\Pr\{|X_j|>t,|X_{j+1}|>t\}\), which tends to zero when \(np(t)\to u\).

The omitted increments \(X_2\) and \(X_{n-1}\) do not alter the leading conditional probability. Indeed, condition on \(X_1=t>0\) and \(|X_n|>t\). The overwhelmingly dominant branch is \(X_n<-t\). Under that conditioning \(X_n/t\to-1\) in probability by Gaussian tail ratios. Conditional Gaussian regression then gives \(G_2/t\to-\sqrt2/3\) and \(G_n/t\to-\sqrt2/3\); the conditional residual variances are bounded. Since \(G_3\) and \(G_{n-1}\) remain independent standard Gaussians, \(|X_2|/t\to1/3\) and \(|X_{n-1}|/t\to1/3\) in probability. The same conclusion holds for \(X_1=-t\) by sign symmetry. Hence, writing
\[
b_n(t)=\Pr\{|X_n|>t,\max_{2\le j<n}|X_j|<t\mid T=t\},
\]
we have \(b_n(t_n(u))/a(t_n(u))\to e^{-u}\) for each fixed \(u>0\). This conclusion uses actual Gaussian tail concentration, not a simulation or an unjustified independence assumption.

**5. Integration and the sharp constant.** The exact integral \(E_n=\int_0^\infty f(t)b_n(t)\,dt\) becomes, under \(u=np(t)\),
\[
E_n=\frac1n\int_0^n b_n(t_n(u))\,du.
\]
Since every second member of the interior sequence is independent, for sufficiently large \(n\), \(\Pr(M_n<t)\le\exp(-np(t)/3)\). In particular \(b_n(t)\le a(t)\exp(-np(t)/3)\). For \(0<u\le n^{1/2}\), Gaussian tail inequalities and \(t_n(u)\ge c\sqrt{\log n}\) imply
\[
n^{1/3}(\log n)^{1/3}a(t_n(u))\le C u^{1/3}
\]
with an absolute constant \(C\); the remaining integration range has exponentially vanishing contribution because \(\exp(-u/3)\) dominates its polynomial prefactor. Dominated convergence therefore gives
\[
\begin{aligned}
\lim_{n\to\infty}n^{4/3}(\log n)^{1/3}E_n
&=\frac{\sqrt3}{2\pi^{1/3}}\int_0^\infty u^{1/3}e^{-u}\,du\\
&=\frac{\sqrt3\,\Gamma(4/3)}{2\pi^{1/3}}.
\end{aligned}
\]
Finally, \(1/[n(n-1)]=o(n^{-4/3}(\log n)^{-1/3})\), so replacing \(1/n\) by the uniform path-edge benchmark \(1/(n-1)\) preserves this limit. Dividing by two yields the oriented normal-cone statement. \(\square\)

## Verification
The embedded `verify.py` tests the exact cycle-closure identity sample-by-sample for several dimensions, checks cyclic uniformity and the exact three-vertex symmetry case, and computes the limiting gamma constant. It also numerically evaluates the one-dimensional Gaussian-tail integral arising from the proof for increasing \(n\). Repeated Gaussian sampling supports the predicted positive boundary anomaly. These finite numerical diagnostics **do not** prove the limiting theorem; the analytical argument above supplies the proof. Run `python verify.py` with NumPy and SciPy installed.

## Relationship to prior work
D'Alì, Delucchi and Michałek [1] study symmetric edge polytopes, their relation to Kantorovich–Rubinstein polytopes, and unimodular equivalence of the tree examples to crosspolytopes. This combinatorial equivalence does **not** preserve the inherited Euclidean inner product and does not imply equality of spherical normal-cone measures. Chen, Davis and Korchevskaia [2] describe facet/face subgraphs rather than Euclidean normal-cone probabilities. Braun and Bruegge [3] count facets of sparse graph polytopes, likewise without a terminal-root angular anomaly. Classical local-dependence Gaussian extreme-value estimates explain the leading Gumbel approximation, but the sharp endpoint exposure correction follows here from the exact cycle-closure event and its bivariate Gaussian tail. Publicly indexed comparison records about path inradii, tree-zonotope width variances, and path Laplacian simplices concern different invariants or different Euclidean polytopes; they do not imply the claimed constant.

## Limitations
The theorem concerns only the canonical Euclidean embedding of the symmetric edge polytope of an unweighted path and its endpoint-root angles, not arbitrary weighted trees or an arbitrary unimodular realization. It does not classify interior root angles, give a finite exact elementary formula for every dimension, or establish priority against unindexed literature. It is independently unvalidated. Simulation and one-dimensional numerical quadrature are diagnostic only.

## References
[1] A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first publicly posted 2019-10-11), Sections 2.1, 3, 4. https://arxiv.org/html/1910.05193v1

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first publicly posted 2021-07-26), Sections 1–4. https://arxiv.org/abs/2107.12315

[3] B. Braun, K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303 (first publicly posted 2022-01-31), Sections 2–4. https://arxiv.org/abs/2201.13303
