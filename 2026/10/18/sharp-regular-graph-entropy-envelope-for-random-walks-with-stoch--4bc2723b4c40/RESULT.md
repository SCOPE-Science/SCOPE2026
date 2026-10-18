# Sharp regular-graph entropy envelope for random walks with stochastic resetting

## Finding
For every finite connected simple \(k\)-regular graph \(G\), \(k\ge2\), with reset vertex \(o\), consider the Markov chain that independently resets to \(o\) with probability \(r\in(0,1)\) or otherwise takes a uniformly selected neighbor. Its stationary **vertex-sequence** entropy rate is
\[
h_{G,o}(r)=B_k(r)-\rho_{G,o}(r)\Delta_k(r),\qquad
B_k(r)=-r\log r-(1-r)\log\frac{1-r}{k},
\]
where, setting \(a=(1-r)/k\),
\[
\Delta_k(r)=(r+a)\log(r+a)-r\log r-a\log a>0,
\quad\rho_{G,o}(r)=\pi_r(N(o)).
\]
This strictly corrects the expression \(B_k(r)\) previously used for the vertex entropy rate: reset and an ordinary step are the **same observed transition** from any neighbor of \(o\).

Define
\[
\mathcal G_k(z)=\frac{2(k-1)}{k-2+\sqrt{k^2-4(k-1)z^2}},\quad
\rho_{\infty,k}(r)=\frac{kr}{1-r}[\mathcal G_k(1-r)-1],
\]
\[
H_k(r)=B_k(r)-\rho_{\infty,k}(r)\Delta_k(r),\quad
H_k(0)=\log k,\quad H_k(1)=0.
\]
For every finite graph as above and \(0<r<1\),
\[
h_{G,o}(r)<H_k(r)<\log(k+1).
\]
Moreover
\[
\log k<\max_{0\le r\le1}h_{G,o}(r)<\max_{0\le r\le1}H_k(r)<\log(k+1).
\]
For any sequence of finite connected \(k\)-regular graphs whose girths tend to infinity, **uniformly over choice of reset vertices**, their entropy-rate functions converge uniformly to \(H_k\) on \([0,1]\). Thus \(\max_rH_k(r)\) is the sharp, nonattained universal supremum of the best resetting entropy rates on finite connected \(k\)-regular graphs. Natural logarithms are used throughout.

## Assumptions and scope
Graphs are finite, connected, simple, undirected, \(k\)-regular, with \(k\ge2\). The transition matrix is
\[
Q_r(i,j)=r\mathbf 1_{\{j=o\}}+\frac{1-r}{k}\mathbf 1_{\{i,j\}\in E(G)}.
\]
Its unique stationary law is \(\pi_r=r\sum_{t\ge0}(1-r)^t\delta_o P^t\), where \(P\) is simple random walk on \(G\). The random variable observed at each step is the **vertex**, not a tagged reset/hop action. The entropy rate is \(h=\lim_{T\to\infty}T^{-1}H(X_0,\ldots,X_T)=\sum_i\pi_r(i)H(Q_r(i,\cdot))\). Continuous endpoint conventions extend the formula to \(r=0,1\).

## Proof
**1. Collision correction.** If \(i\notin N(o)\), the ordinary neighbor transitions (each of mass \(a\)) and reset transition (mass \(r\)) lead to distinct vertices; their row entropy is \(B_k(r)\). If \(i\in N(o)\), the ordinary edge to \(o\) and the reset action have the same destination, producing mass \(r+a\) rather than two distinguishable outcomes. Their entropy loss is exactly \(\Delta_k(r)\), strictly positive by strict entropy concavity or direct differentiation. Stationary averaging gives the claimed identity.

**2. Return Green function.** For all \(t\ge0\), the undirected regularity identity
\[
P^{t+1}(o,o)=\frac1kP^t(o,N(o))
\]
holds. Therefore, writing \(z=1-r\) and \(\mathcal G_{G,o}(z)=\sum_{t\ge0}z^tP^t(o,o)\),
\[
\rho_{G,o}(r)=r\sum_{t\ge0}z^tP^t(o,N(o))
=\frac{kr}{z}\bigl[\mathcal G_{G,o}(z)-1\bigr].
\]

**3. Covering-tree sharp upper bound.** The universal cover of any connected \(k\)-regular graph is the infinite \(k\)-regular tree. Mapping any length-\(t\) closed tree walk to the graph preserves its probability \(k^{-t}\), and supplies an injection into graph closed walks. Hence \(P_G^t(o,o)\ge P_{\mathbb T_k}^t(o,o)\). The inequality is strict for some \(t\) because a finite graph possesses a cycle and therefore a closed walk whose lift to the tree is not closed. Summing with positive \(z^t\), and using the positive collision loss, proves \(h_{G,o}(r)<H_k(r)\). The standard first-return recursion for the infinite regular tree gives
\[
\mathcal G_{\mathbb T_k}(z)=\frac{2(k-1)}{k-2+\sqrt{k^2-4(k-1)z^2}}.
\]
The action-outcome entropy \(B_k(r)\) never exceeds \(\log(k+1)\), with equality only when \(r=1/(k+1)\); the positive correction makes \(H_k(r)<\log(k+1)\) for interior \(r\), while the two endpoint values are strictly below it. Compactness yields the strict bound on the maximum.

**4. Resetting strictly improves over ordinary walk.** As \(r\downarrow0\), stationarity of ordinary simple random walk on a connected regular graph and its resolvent representation imply \(\pi_r\to\mathrm{Uniform}(V(G))\), even for periodic walks. Thus \(\rho_{G,o}(r)\to k/|V(G)|\). Direct expansion yields
\[
B_k(r)=\log k+r\log(1/r)+O_k(r),\quad
\Delta_k(r)=r\log(1/r)+O_k(r),
\]
and hence
\[
h_{G,o}(r)=\log k+\left(1-\frac{k}{|V(G)|}\right)r\log(1/r)+O_G(r).
\]
Since a simple \(k\)-regular graph has at least \(k+1\) vertices, the coefficient is positive. This proves \(\max h_{G,o}>\log k\); consequently \(\max H_k>\log k\) too.

**5. High-girth sharpness.** Let \(g\) be the girth and \(m=\lfloor(g-1)/2\rfloor\). All transition probabilities from \(o\) to \(N(o)\) for walk lengths \(t\le m\) agree with the regular tree (a shorter discrepancy would give a cycle of length at most \(2t+1<g\)). Consequently
\[
0\le \rho_{G,o}(r)-\rho_{\infty,k}(r)\le (1-r)^{m+1},
\qquad
0\le H_k(r)-h_{G,o}(r)\le\Delta_k(r)(1-r)^{m+1}.
\]
The rightmost expression converges to zero **uniformly** on \(r\in[0,1]\): on \(r\ge\varepsilon\) use geometric decay; on \(r\le\varepsilon\), use \(\Delta_k(r)\to0\). Every fixed degree \(k\ge2\) admits finite connected \(k\)-regular graphs with arbitrarily large girth (cycles for \(k=2\), the classical Erdős–Sachs existence theorem for \(k\ge3\)). Therefore \(H_k\) is the sharp supremum of finite-graph entropy-rate functions, and uniform convergence also transfers maxima.

**6. Exact small-graph witness.** On the triangle \(G=K_3\), resetting to vertex \(o\) at \(r=1/3\), the stationary distribution is \((1/2,1/4,1/4)\). The reset row is uniform on three states, while each nonroot row has probabilities \((2/3,1/3)\) on two states. Thus
\[
h_{K_3,o}(1/3)=\tfrac12\log3+\tfrac12\bigl[-\tfrac23\log\tfrac23-\tfrac13\log\tfrac13\bigr]
\approx0.8675632285<\log3.
\]
This is a state-observable calculation, not a count of distinguishable action labels.

## Verification
The accompanying standard-library `verify.py` reconstructs finite stationary laws using exact rational Gaussian elimination. It compares entropy directly from each row with the collision correction on multiple regular graph families and rates, checks the closed tree formula and the girth-dependent finite-size envelope. The tests demonstrate examples and normalization; infinite claims are proved above and not inferred from finite tests.

## Relationship to prior work
Wang and Chen, *Entropy rate of random walks on complex networks under stochastic resetting* (arXiv:2208.05665, publicly available 2022-08-11), give the general Markov entropy-rate identity but subsequently display the regular-graph rate \(B_k(r)\) and conclude it can attain \(\log(k+1)\). That expression is the entropy of **labeled reset-versus-hop choices**, not of the resulting **vertex transition** when the current vertex neighbors the reset root. The positive collision correction is required for the state-sequence entropy rate, and yields a strictly smaller sharp large-girth envelope. Burda et al. study maximal-entropy walks with different transition restrictions; Wang, Chen and Huang study renewal/stationary resetting quantities rather than this conditional state entropy. The present sharp universal-cover entropy profile and high-girth approximation are not consequences of those stated results.

## Limitations
The theorem assumes a single deterministic reset root, a finite connected simple regular undirected graph and a constant reset rate. It does not cover heterogeneous degrees, multiple reset points, weighted walks or hidden-action entropy. The sharp universal supremum is not attained by a finite graph and no closed form for its optimizing reset probability is asserted. Numerical illustrations are not independently certified root enclosures. Full bibliographic priority cannot be established from the inspected literature alone.

## References
1. S. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665 (first available 2022-08-11), https://arxiv.org/abs/2208.05665.
2. Z. Burda, J. Duda, J. M. Luck and B. Waclaw, *Localization of maximal entropy random walk*, arXiv:0810.4113, https://arxiv.org/abs/0810.4113.
3. S. Wang, H. Chen and F. Huang, *Random walks on complex networks with multiple resetting nodes: a renewal approach*, arXiv:2105.08323, https://arxiv.org/abs/2105.08323.
4. P. Erdős and H. Sachs, *Reguläre Graphen gegebener Taillenweite mit minimaler Knotenzahl* (1963), on existence of regular graphs of arbitrarily large girth.
