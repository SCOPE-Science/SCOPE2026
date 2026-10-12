# A topology-explicit inverse-dispersal law for stochastic Allee fixation

## Finding
Consider a connected simple undirected habitat graph \(G=(V,E)\) with \(n\geq2\) vertices. Each vertex carries a population density in \([0,1]\). Every edge, independently at rate \(\alpha>0\), replaces the densities at its endpoints by reciprocal \(\mu\)-mixes, for a fixed \(0<\mu\leq1/2\). Independently, every vertex is refreshed at rate one: it becomes zero below a common Allee threshold \(0<\theta<1\), becomes one above it, and chooses zero or one equally at equality. The only absorbing configurations are the all-zero and all-one configurations.

For a deterministic initial state \(x\in[0,1]^V\), put
\[
\bar x=\frac1n\sum_{v\in V}x_v,\qquad
\Delta=|\bar x-\theta|,\qquad
H(x)=\sum_{v\in V}(x_v-\bar x)^2.
\]
Let \(\lambda_2(G)>0\) be the second eigenvalue of the combinatorial graph Laplacian. If \(\Delta>0\), then the probability of fixation **opposite to the sign of \(\bar x-\theta\)** satisfies, for every \(\alpha>0\),
\[
\boxed{\quad
\Pr(\text{wrong absorbing state})\leq
\min\!\left\{1,\frac{nH(x)}{\Delta^2\left[n+2\alpha\mu(1-\mu)\lambda_2(G)\right]}\right\}.\quad}
\]
In particular, for every fixed connected graph and noncritical initial average, the fixation outcome converges in probability to the initial-average threshold rule as \(\alpha\to\infty\), at an explicit inverse-dispersal rate depending on algebraic connectivity. **The inverse-rate order cannot be improved uniformly:** on the two-vertex graph with initial densities \((1,0)\), \(\mu=1/5\) and \(\theta=9/20\), the wrong-fixation probability is \(\Theta(1/\alpha)\).

## Assumptions and scope
The graph is finite, simple, connected, undirected and has at least two vertices. Each unordered edge has an independent rate-\(\alpha\) Poisson clock. A clock on edge \(\{u,v\}\) maps
\[
(x_u,x_v)\longmapsto ((1-\mu)x_u+\mu x_v,\;\mu x_u+(1-\mu)x_v).
\]
Every vertex has an independent rate-one Poisson clock. On ringing, that coordinate is set to \(1\) if it is strictly above \(\theta\), to \(0\) if strictly below, and to an independent fair Bernoulli state at equality. All clocks and tie coins are independent. The initial configuration is deterministic, but the inequality also holds conditionally on an independent random initial configuration for which \(\bar x\ne\theta\).

Write \(\mathsf E_+\) for absorption at the all-one state and \(\mathsf E_-\) for absorption at all zero. The 'wrong' event is \(\mathsf E_-\) if \(\bar x>\theta\), and \(\mathsf E_+\) if \(\bar x<\theta\). The case \(\bar x=\theta\) is deliberately excluded: the bound's threshold margin then vanishes. Neither the relative order of graph size and dispersal rate nor a regularity assumption on vertex degrees is required.

## Proof
**Absorption and threshold regions.** The regions with all coordinates strictly greater than \(\theta\), or all strictly less than \(\theta\), are invariant under both mixing and local updates. From either region, absorption at the corresponding constant state happens almost surely. Indeed, let \(m=|E|\). From any configuration in either region, the probability that the next \(n\) clock rings are, in a prescribed order, one local ring at each different vertex (and no edge rings) is \((n+\alpha m)^{-n}>0\). Such a sequence reaches the relevant absorbing state. Repeating blocks of \(n\) rings and using the strong Markov property shows that one of these prescribed sequences eventually occurs almost surely. For completeness, absorption also occurs almost surely from any starting state. Force one local ring at each vertex before any edge ring: the resulting state is a binary vector. For each of the finitely many binary vectors with average different from \(\theta\), a finite prescribed sequence of edge rings can bring every density strictly to the average side of \(\theta\), because repeated symmetric mixing on a connected graph converges to consensus. If a binary vector has average exactly \(\theta\), it is nonconstant; choose an edge joining a zero to a one, ring it, and then ring one of its endpoints locally. Its postmix value lies strictly between zero and one, so this local reset changes the global average away from \(\theta\). Then perform finite consensus mixing as before. Finally ring every vertex locally to absorb. Thus each binary vector has a finite positive-probability route to absorption; finiteness of the binary state space makes the absorption probability within a bounded number of future events uniformly positive. Iterating gives almost-sure absorption from arbitrary states. The probability bound below needs only the simpler invariant-region argument.

**Pure-mixing contraction.** Suppress all local refreshes and call the resulting process \(X(t)\). Mixing preserves its mean \(\bar x\). Set \(H(t)=\sum_v(X_v(t)-\bar x)^2\). A ring of an edge \(\{u,v\}\) decreases this quantity by exactly
\[
2\mu(1-\mu)(X_u(t)-X_v(t))^2.
\]
Consequently its pure-mixing generator satisfies
\[
\mathcal LH=-2\alpha\mu(1-\mu)\sum_{\{u,v\}\in E}(X_u-X_v)^2
\leq-2\alpha\mu(1-\mu)\lambda_2(G)H.
\]
Dynkin's formula and Gronwall's inequality (all states are bounded) give
\[
\mathbb E H(t)\leq H(x)\exp\!\left[-2\alpha\mu(1-\mu)\lambda_2(G)t\right].
\]

**Competing exponential clocks.** Let \(T\) be the first local-refresh time over the \(n\) sites. It is independent of pure mixing and has exponential rate \(n\). Therefore
\[
\mathbb E H(T)\leq \int_0^\infty ne^{-nt}H(x)e^{-2\alpha\mu(1-\mu)\lambda_2(G)t}\,dt
=\frac{nH(x)}{n+2\alpha\mu(1-\mu)\lambda_2(G)}.
\]
If \(H(T)<\Delta^2\), then each coordinate differs from \(\bar x\) by less than \(\Delta\), hence every coordinate lies strictly on the same side of the threshold as \(\bar x\). In this event the first refresh, and every subsequent event, preserves the corresponding threshold region; fixation is therefore correct. Markov's inequality yields
\[
\Pr(\text{wrong fixation})\leq\Pr(H(T)\geq\Delta^2)
\leq\frac{\mathbb EH(T)}{\Delta^2},
\]
which proves the asserted inequality, including its truncation at one.

**Sharpness of inverse-rate order.** On the two-vertex graph, take \(x=(1,0)\), \(\mu=1/5\), \(\theta=9/20\). The initial average \(1/2\) exceeds \(\theta\), so extinction is the wrong outcome. Consider the following first two chronological clock events: first the edge mixing clock, then the local clock at the site that was initially empty. This sequence has probability
\[
\frac{\alpha}{\alpha+2}\,\frac1{\alpha+2}=\frac{\alpha}{(\alpha+2)^2}.
\]
The first event gives densities \((4/5,1/5)\), and the second changes them to \((4/5,0)\), because \(1/5<9/20\). The new average is \(2/5<9/20\). For this new state, \(H=8/25\), \(\Delta=1/20\), and \(\lambda_2(G)=2\); applying the already proved bound with the opposite target shows that its conditional probability of eventual extinction is at least
\[
1-\min\!\left\{1,\frac{(16/25)}{(1/400)(2+(16/25)\alpha)}\right\},
\]
which tends to one. Thus the wrong-fixation probability for the initial state is at least the product of this quantity and \(\alpha/(\alpha+2)^2\), giving
\[
\liminf_{\alpha\to\infty}\alpha\Pr(\mathsf E_-)\geq1.
\]
The general upper bound applied to the initial state is \(O(1/\alpha)\), completing the \(\Theta(1/\alpha)\) proof.

## Verification
The self-contained `verify_gap.py` script uses exact rational arithmetic and the Python standard library. It checks the edgewise energy decrement for 35,952 finite combinations, the complete-graph Laplacian identity for 1,089 finite combinations, and the exact inequalities and event probabilities in the two-patch sharpness example. The successful output is:

`VERIFY_OK edge_energy_identities=35952 complete_graph_gap_identities=1089 two_patch_lower_event=1`

The unrestricted conclusion is established by the proof, not by the finite checks. Reproduce with `python3 verify_gap.py`.

## Relationship to prior work
Kang and Lanchier's 2010 two-patch stochastic Allee model uses edge mixing at rate one and site updates at a separate rate; it discusses synchronization and initial-average behavior under strong relative dispersal, including a qualitative two-patch limiting prediction. Lanchier's 2013 multi-patch model treats general habitat graphs with unit-rate edge mixing and proves results for growing complete graphs and rings. The contribution here is not the qualitative principle that fast mixing homogenizes densities. It is a uniform **finite-graph, nonasymptotic, algebraic-connectivity-dependent error inequality**, valid for arbitrary initial densities away from the threshold, accompanied by a two-patch example proving that the inverse-relative-dispersal *order* of its error cannot in general be improved. The result uses a distinct fixed-graph, accelerated-clock limit rather than the source paper's increasing-graph-size limit.

More general fast-stirring and averaging results could imply qualitative convergence; a full historical priority claim for such principles is not made. No inspected source established the displayed inequality together with the order-sharp ecological example.

## Limitations
The result assumes a common threshold and exchange fraction, symmetric edge mixing, independent Poisson clocks and no environmental heterogeneity. It does not cover a critical initial average \(\bar x=\theta\), joint limits in which graph size grows, arbitrary directed/asymmetric dispersal, noisy observations or finite-population birth/death events. The upper-bound coefficient is not claimed optimal, although the inverse-rate scaling is sharp. The model gives no empirical estimate of ecological migration rates or persistence probability outside its idealized dynamics. General fast-stirring literature might contain an equivalent bound and warrants further independent comparison.

## References
1. Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, initial arXiv version dated 2010-02-27, arXiv:1003.0121v1, https://arxiv.org/abs/1003.0121.
2. N. Lanchier, *The role of dispersal in interacting patches subject to an Allee effect*, initial arXiv version dated 2013-01-01, arXiv:1301.0125v1, https://arxiv.org/abs/1301.0125.
3. O. Vilk and M. Assaf, *Extinction risk of a metapopulation under the Allee effect*, arXiv:1908.09026 (different demographic model; only summary-level comparison), https://arxiv.org/abs/1908.09026.
