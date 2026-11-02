# A graph-universal stationary law for rare stubborn contacts

## Finding
For a fixed finite connected weighted network, making all contacts with stubborn agents arbitrarily rare does **not** collapse the stationary opinion law to a deterministic consensus. The agents agree with one another asymptotically, but their common opinion retains an explicit, graph-independent random distribution. Moreover, the rate of agreement is controlled by the spectral gap of the internal network.

Let \(N\ge2\) be fixed. Write \(\bar X=N^{-1}\sum_i X_i\). The theorem gives, for every \(\varepsilon>0\),
\[
\mathbb E_{\Pi_\varepsilon}\!\left[\sum_{i=1}^N(X_i-\bar X)^2\right]\le\frac{10\varepsilon B R^2}{\lambda_2},
\]
and for every regular agent \(i\),
\[
 W_1\bigl(\operatorname{Law}_{\Pi_\varepsilon}(X_i),\operatorname{Law}(Y_N)\bigr)
 \le 2R\sqrt{\frac{10\varepsilon B}{\lambda_2}}.
\]
Here \(Y_N\) is a universal weighted random series that depends only on the numbers and opinions of stubborn contacts, not on the regular-to-regular graph:
\[
Y_N=\frac1{2N}\sum_{k=0}^{\infty}
\left(1-\frac1{2N}\right)^k S_k,
\qquad
\Pr(S_k=s_j)=\frac{\sum_i b_{ij}}{B}.
\]
The empirical-mean law obeys the same Wasserstein bound with half the displayed constant. In particular,
\[
\Pi_\varepsilon\ \Longrightarrow\ \operatorname{Law}(Y_N\mathbf1)
\qquad (\varepsilon\downarrow0).
\]
The exact first two moments of the common limiting opinion are
\[
\mathbb EY_N=\sum_j\frac{\sum_i b_{ij}}B s_j,
\qquad
\operatorname{Var}(Y_N)=\frac{\operatorname{Var}(S_0)}{4N-1}.
\]
For two antagonistic stubborn opinions \(-1\) and \(+1\) with equal *total* contact coefficients, the variance is \(1/(4N-1)>0\). As a second, sequential limit after \(\varepsilon\downarrow0\), \(\sqrt{4N-1}\,Y_N\) converges to the standard normal law as \(N\to\infty\) in that symmetric binary case.

## Assumptions and scope
Take any undirected connected simple graph \(G=(V,E)\) on \(N\ge2\) regular agents. For each edge \(\{i,k\}\in E\), fix \(w_{ik}=w_{ki}>0\). The weighted Laplacian is \(L\), and its second eigenvalue is \(\lambda_2>0\), with normalization
\[
\sum_{\{i,k\}\in E}w_{ik}(x_i-x_k)^2\ge\lambda_2\sum_i(x_i-\bar x)^2.
\]
There are finitely many stubborn agents indexed by \(j\), permanently holding values \(s_j\in[-R,R]\), where \(R>0\). A regular-to-stubborn pair \((i,j)\) has weight \(\varepsilon b_{ij}\), with \(b_{ij}\ge0\) and \(B=\sum_{ij}b_{ij}>0\). There are no other effective updates. At each discrete time, independently select one effective edge with probability proportional to its weight; the normalizing sum is \(W+\varepsilon B\), where \(W=\sum_{\{i,k\}\in E}w_{ik}\).

When a regular--regular edge is selected, *both* regular opinions become their average. When a regular--stubborn edge is selected, its regular opinion becomes \((X_i+s_j)/2\), and the stubborn opinion does not change. Every regular initial opinion lies in \([-R,R]\). For each \(\varepsilon>0\), \(\Pi_\varepsilon\) denotes the invariant law on this compact state cube. \(W_1\) denotes one-dimensional Wasserstein distance with cost \(|x-y|\).

The limits are taken for fixed \(N\), fixed internal graph, fixed anchor coefficients and fixed stubborn values, then \(\varepsilon\downarrow0\). Disconnected regular graphs, state-dependent contact probabilities, asynchronous *one-sided* copying, and simultaneous large-network/rare-contact limits are not covered.

## Proof
**1. Existence and uniqueness.** Every edge update is a continuous affine map preserving the cube, and their state-independent mixture is Feller. The compact-state Krylov--Bogoliubov averaging argument yields an invariant law. To prove uniqueness, couple two trajectories with the *same* independent edge choices. Their coordinatewise differences are not increased in the maximum norm by either kind of update. Choose a regular vertex with a positive anchor coefficient and a spanning tree rooted there. One finite positive-probability word first updates this root against the stubborn neighbor, then updates the tree edges with each parent encountered before its child. If the preceding maximum discrepancy is \(M\), at the end of this word every discrepancy is at most \((1-2^{-N})M\): the root starts with half its old discrepancy, and at most \(N-1\) subsequent midpoint steps can dilute this improvement. The block word appears infinitely often in independent fixed-length blocks, almost surely. Hence synchronous coupling drives every initial pair together almost surely. Compactness and continuity imply uniqueness of the invariant law.

**2. A stationary disagreement estimate.** Define
\[
D(x)=\sum_i(x_i-\bar x)^2.
\]
A regular--regular midpoint update on \(\{i,k\}\) conserves \(\bar x\) and changes \(D\) by exactly \(-\tfrac12(x_i-x_k)^2\). A regular--stubborn update of coordinate \(i\) by \(\delta=(s_j-x_i)/2\) changes it by
\[
D(x+\delta e_i)-D(x)=2\delta(x_i-\bar x)+(1-1/N)\delta^2.
\]
Since \(|\delta|\le R\) and \(|x_i-\bar x|\le2R\), its increase is at most \(5R^2\). The stationary generator identity for \(D\), multiplied by the common edge-normalization factor, is therefore
\[
\frac12\sum_{\{i,k\}\in E}w_{ik}\,\mathbb E(X_i-X_k)^2
=\varepsilon\sum_{ij}b_{ij}\,\mathbb E[\Delta_{ij}D]
\le5\varepsilon BR^2.
\]
Apply the specified spectral-gap inequality to obtain
\[
\mathbb E_{\Pi_\varepsilon}D\le10\varepsilon BR^2/\lambda_2.
\]
This estimate uses neither symmetry among regular vertices nor uniform anchor locations.

**3. A contractive effective mean chain.** Only a regular--stubborn update changes \(\bar X\), and its increment is \(\eta(s_j-X_i)\), where \(\eta=1/(2N)\). Under stationarity, condition on having selected an anchor edge: the index pair \((I,J)\) is independent of the current state and has distribution \(\Pr(I=i,J=j)=b_{ij}/B\). Thus \(\bar X\) and \(\bar X+\eta(s_J-X_I)\) have the same law, call it \(Q_\varepsilon\).

Let \(K\) be the scalar Markov kernel sending \(y\) to \((1-\eta)y+\eta S\), with independent \(S\) satisfying \(\Pr(S=s_j)=\sum_i b_{ij}/B\). Under the coupling using the same \(\bar X,I,J\),
\[
W_1(Q_\varepsilon,KQ_\varepsilon)
\le\eta\,\mathbb E|X_I-\bar X|
\le\eta\sqrt{\mathbb ED}.
\]
The first equality in law used above holds because, in the stationary generator identity for every bounded continuous scalar test function, all regular--regular updates contribute zero and the anchor terms have the same constant factor \(\varepsilon B/(W+\varepsilon B)\); that factor cancels. This does **not** require the sample of \(I\) to be uniform or uncorrelated with the opinion profile; only the selected indices are independent of the state.

The kernel \(K\) contracts \(W_1\) by \(1-\eta\). Its unique invariant law \(\nu_N\) is the almost surely convergent random series
\[
Y_N=\eta\sum_{k\ge0}(1-\eta)^kS_k.
\]
The triangle inequality and contraction give
\[
W_1(Q_\varepsilon,\nu_N)
\le\eta\sqrt{\mathbb ED}+(1-\eta)W_1(Q_\varepsilon,\nu_N),
\]
so \(W_1(Q_\varepsilon,\nu_N)\le\sqrt{\mathbb ED}\). Coupling each coordinate to its own empirical mean gives
\[
W_1(\operatorname{Law}(X_i),\nu_N)
\le\mathbb E|X_i-\bar X|+\sqrt{\mathbb ED}
\le2\sqrt{\mathbb ED}.
\]
Substitution of Step 2 proves the two error bounds. Also \(\|X-\bar X\mathbf1\|_2^2=D\), so the joint weak convergence follows by tightness, concentration on the diagonal, and convergence of the scalar mean law.

**4. Moments and large-network corollary.** The stationary recursion \(Y\overset d=(1-\eta)Y+\eta S\), with independent right-hand variables, gives \(\mathbb EY=\mathbb ES\) and
\[
\operatorname{Var}(Y)=\frac{\eta^2\operatorname{Var}(S)}{1-(1-\eta)^2}
=\frac{\operatorname{Var}(S)}{4N-1}.
\]
For symmetric \(\pm1\) anchor values, the centered normalized sum is a weighted triangular array of independent Rademacher variables. Its squared coefficients sum to one after normalization, and its maximum absolute coefficient is \(\sqrt{(4N-1)}/(2N)\to0\). Boundedness ensures the Lindeberg condition and hence asymptotic normality.

## Verification
A standalone exact-rational script, `verify_gossip.py`, constructs finite-dimensional stationary first- and second-moment linear equations directly from all edge-update matrices, solves them by rational Gaussian elimination, and separately checks every first- and second-moment stationary generator equation. The script tests paths, stars, a cycle, weighted edges, symmetric and asymmetric stubborn contact patterns, and five positive values of \(\varepsilon\) per graph, for 290 exact-rational assertions. It also checks the disagreement energy bound and the predicted universal limiting second moments at a small positive \(\varepsilon\), with a rigorously justified error allowance. These finite checks are not offered as a substitute for the all-graph proof above.

To reproduce with Python 3, place `verify_gossip.py` in the same directory and run `python verify_gossip.py`. Expected final output: `PASS 290 exact-rational generator, topology, and rare-anchor checks`.

## Relationship to prior work
Xing and Johansson's publicly posted 2022 *Transient Behavior of Gossip Opinion Dynamics with Community Structure* (arXiv:2205.14784) studies transient second moments, community-specific concentration and times to approach stationary behavior. Their 2023 *What is the Expected Transient Behavior of Opinion Evolution for Two Communities?* (arXiv:2304.12495) concentrates on transient expected opinions. The present theorem instead takes a **fixed finite connected graph's stationary law first**, then makes stubborn contacts rare, and obtains a complete limiting distribution with explicit spectral-gap control. It permits arbitrary connected weighted regular networks and arbitrary finite anchor placement.

Acemoglu, Como, Fagnani and Ozdaglar's *Opinion Fluctuations and Disagreement in Social Networks* (arXiv:1009.2653) establishes the stationary-disagreement framework, including general stationary moment equations and large-network regimes. Those known facts are not claimed as new. The claimed additional statement is the explicit *fixed-network, vanishing-anchor* distributional limit, its topology-independent Bernoulli-convolution form and quantitative rate. Xing, He, Fang and Johansson's *Community Detection for Gossip Dynamics with Stubborn Agents* (arXiv:2003.14028) focuses on stationary expectations and network inference, not this singular law. An equivalent older perturbation theorem not found in the inspected sources remains a priority risk.

## Limitations
The parameter \(N\) and graph are fixed when \(\varepsilon\to0\); the spectral gap may vanish in a sequence of larger networks, so no uniform large-network interchange is established. Midpoint averaging on both endpoints and state-independent edge selection are essential to the exact scalar contraction. A disconnected regular network can have distinct limiting consensus coordinates. The stationary law is specified as a convergent random series, not as an elementary density, and such a density need not exist in every generalized anchor-value family. The mathematical priority assessment is based on the inspected literature and is not an exhaustive guarantee. No independently performed verification is claimed.

## References
1. Yu Xing and Karl H. Johansson, *Transient Behavior of Gossip Opinion Dynamics with Community Structure*, first arXiv version May 29, 2022, https://arxiv.org/abs/2205.14784 .
2. Yu Xing and Karl H. Johansson, *What is the Expected Transient Behavior of Opinion Evolution for Two Communities?*, first arXiv version April 24, 2023, https://arxiv.org/abs/2304.12495 .
3. Daron Acemoglu, Giacomo Como, Fabio Fagnani and Asuman Ozdaglar, *Opinion Fluctuations and Disagreement in Social Networks*, https://arxiv.org/abs/1009.2653 .
4. Yu Xing, Xingkang He, Haitao Fang and Karl Henrik Johansson, *Community Detection for Gossip Dynamics with Stubborn Agents*, https://arxiv.org/abs/2003.14028 .
