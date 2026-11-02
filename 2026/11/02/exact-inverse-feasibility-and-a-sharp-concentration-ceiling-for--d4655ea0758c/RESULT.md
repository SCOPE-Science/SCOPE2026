# Exact inverse feasibility and a sharp concentration ceiling for fractional delegation

## Finding

**Inverse-weight theorem.** Let \(G=(V,E)\) be any finite directed trust network, with \(V=\{1,\ldots,n\}\), \(n\ge2\), and no loops. Fix individual vote-retention fractions \(\tau_i\in(0,1)\). Each agent initially contributes one unit of vote. Whenever a unit reaches agent \(j\), that agent casts the fraction \(\tau_j\) and delegates the remaining fraction \(1-\tau_j\) along the allowed outgoing arcs, using the same distribution at every visit.

A proposed final vote-weight vector \(w=(w_i)_{i\in V}\) is realizable by such fractional delegation **if and only if**

\[
\sum_{i\in V}w_i=n,\qquad w_i\ge\tau_i\ \text{for every }i,
\tag{1}
\]

and for **every** subset \(S\subseteq V\),

\[
\boxed{\displaystyle
\sum_{i\in S}\left(\frac{w_i}{\tau_i}-1\right)
\le
\sum_{j\in\Gamma^-(S)}\frac{(1-\tau_j)w_j}{\tau_j}},
\qquad
\Gamma^-(S)=\{j\in V:\exists i\in S,\ (j,i)\in E\}.
\tag{2}
\]

For rational inputs, realizability and a rational delegation matrix are computable by one bipartite maximum-flow problem. In particular, the set of attainable vote-weight vectors is a convex polytope described by (1)–(2), even though the forward delegation map is a matrix resolvent.

**Sharp loopless concentration law.** If every distinct pair is a permitted delegation arc and \(\tau_i=\tau\in(0,1)\) for all agents, the attainable set is exactly

\[
\boxed{\displaystyle
\left\{w\in\mathbb R^n:\sum_iw_i=n,\ \tau\le w_i\le
\frac{n(1-\tau)+\tau}{2-\tau}\ \text{for all }i\right\}.}
\tag{3}
\]

Every coordinate ceiling in (3) is attained by a bidirectional star: all other agents delegate their residual weight to the distinguished agent, which distributes its own residual weight equally back to them. No individual can obtain a strict majority of the total vote: the ceiling is at most \(n/2\), and is strictly less when \(n>2\). For fixed \(n>2\), the fraction of votes at the maximally influential agent approaches \(1/2\) as \(\tau\downarrow0\).

## Assumptions and scope

The word *weight* denotes the final fractionally aggregated ballot mass, **not** the Penrose–Banzhaf probability of being pivotal or the outcome of a strategic equilibrium game. The trust network \(G\) is fixed; its permitted arcs may be assigned probability zero. No direct self-delegation arc is permitted, since self-retention is separately forced by \(\tau_i>0\). Every agent uses a constant outgoing probability distribution and splits incoming and initial mass by the same fixed retention. The theorem allows cycles and disconnected graphs; it does not require strong connectivity. Each vertex must have at least one permitted outgoing arc for a feasible process, a requirement already enforced by (2).

Write \(Q_{ij}\) for the fraction delegated from agent \(j\) to agent \(i\). Thus \(Q\) is nonnegative and column stochastic, with \(Q_{ij}=0\) unless \((j,i)\in E\). Let \(D=\operatorname{diag}(\tau_i)\), let \({\bf1}\) be the all-ones vector, and define the expected total arrival mass \(u\) and cast weights \(w\) by

\[
u={\bf1}+Q(I-D)u,
\qquad w=Du.
\tag{4}
\]

Since \(\|Q(I-D)\|_1=\max_i(1-\tau_i)<1\), equation (4) has the unique nonnegative solution \(u=(I-Q(I-D))^{-1}{\bf1}\). All votes eventually contribute to the cast weights, and \(\sum_iw_i=n\).

## Proof

**1. Necessity and the flow identity.** Set

\[
 r_i=\frac{w_i}{\tau_i}-1,
 \qquad c_j=\frac{(1-\tau_j)w_j}{\tau_j}.
\tag{5}
\]

By (4), \(r_i\ge0\), \(c_j>0\), and the actual delegated flow from \(j\) to \(i\) is \(F_{ij}=Q_{ij}c_j\ge0\). Its receiver sums and sender sums are respectively

\[
\sum_jF_{ij}=r_i,
\qquad \sum_iF_{ij}=c_j.
\tag{6}
\]

Moreover \(\sum_i r_i=\sum_j c_j\) is equivalent to \(\sum_i w_i=n\). All flow entering receiver set \(S\) must originate in its direct in-neighborhood \(\Gamma^-(S)\). Summing (6) proves (2).

**2. Sufficiency, including zero-edge cases.** Suppose (1)–(2) hold. Build a bipartite flow network with a source connected to sender node \(j\) with capacity \(c_j\), sender \(j\) connected to receiver \(i\) with capacity \(C:=\sum_jc_j\) exactly when \((j,i)\in E\), and receiver \(i\) connected to the sink with capacity \(r_i\). Both sides have equal total capacity \(C=\sum_ir_i\). A cut can obstruct full throughput precisely when some receiver set \(S\) has required inflow \(\sum_{i\in S}r_i\) greater than the capacity \(\sum_{j\in\Gamma^-(S)}c_j\) of its possible senders. By max-flow/min-cut and (2), a nonnegative matrix \(F\) supported on allowed arcs has exactly the sums (6).

Because every \(\tau_j\in(0,1)\) and \(w_j\ge\tau_j>0\), each \(c_j>0\); therefore define \(Q_{ij}=F_{ij}/c_j\). This \(Q\) is nonnegative, column stochastic, and supported on \(E\). Put \(u_i=w_i/\tau_i\). Equations (5)–(6) give \(u_i-1=\sum_jQ_{ij}(1-\tau_j)u_j\). Uniqueness of the resolvent solution to (4) proves that the resulting cast weights are exactly the target \(w\), not merely a surrogate flow profile. Standard exact rational maximum-flow arithmetic supplies a rational witness whenever \(w\) and \(\tau\) are rational.

**3. Complete loopless networks.** For the complete loopless directed graph, \(\Gamma^-(\{i\})=V\setminus\{i\}\). When all retention fractions equal \(\tau\), its singleton cut (2), after multiplying by \(\tau\), becomes

\[
 w_i-\tau\le(1-\tau)(n-w_i),
\quad\text{i.e.}\quad
 w_i\le U_{n,\tau}:=\frac{n(1-\tau)+\tau}{2-\tau}.
\tag{7}
\]

For any receiver set containing at least two different agents, every sender has an arc to some member of that set, so \(\Gamma^-(S)=V\). Since the receiver demands are nonnegative and total demand equals total supply, these remaining inequalities are automatic. Thus (1)–(2) reduce *exactly* to the box-with-sum in (3), including \(n=2\) (where that box forces \(w=(1,1)\)).

To attain equality in (7) at agent \(1\), prescribe \(Q_{1j}=1\) for each \(j\ne1\), and \(Q_{j1}=1/(n-1)\) for each \(j\ne1\), all other entries zero. By symmetry, the arrival masses obey

\[
 u_1=1+(n-1)(1-\tau)u_2,
 \qquad u_2=1+\frac{1-\tau}{n-1}u_1.
\]

Solving gives \(w_1=\tau u_1=U_{n,\tau}\) and \(w_j=(n-U_{n,\tau})/(n-1)\) for \(j\ne1\). Finally

\[
\frac n2-U_{n,\tau}
=\frac{\tau(n-2)}{2(2-\tau)}\ge0,
\tag{8}
\]

strictly for \(n>2\). This is the announced majority barrier and its equality characterization.

**4. Why group cuts cannot be discarded.** Consider six vertices, two disconnected directed triangles each allowing every arc between distinct vertices *within* the triangle, and common retention \(\tau=1/2\). The target \(w_i=11/10\) on the first triangle and \(w_i=9/10\) on the second has total weight six and passes every lower-bound and singleton cut. However, for the three-vertex set in the first component the receiver demand is \(18/5\) and the available outgoing supply is \(33/10\); hence (2) fails. This shows genuine collective obstructions that cannot be detected from individual bounds alone.

## Verification

The standalone `verify.py` performs 1,528 exact-rational consistency tests. It solves the resolvent via independent rational Gaussian elimination, checks every subset cut on sampled networks, constructs a witness by augmenting-path maximum flow, and recomputes the resulting cast weights. The tested inputs include 400 random sparse loopless trust networks with two through five vertices, heterogeneous retention fractions, feasible profiles obtained from random delegation matrices, perturbed proposed targets, and sharp complete-network examples with two through eight vertices. The checks passed. Finite computation does not replace the unrestricted proof above.

To reproduce: execute `python verify.py` with Python 3 and no third-party packages. All arithmetic is `fractions.Fraction`; the deterministic test seed is fixed within that file.

## Relationship to prior work

Bersetche's 2022 fractional multi-delegation model defines cast voting weights by a resolvent and studies their well-definedness, conservation and strategic equilibria. The present proof uses its mass-flow viewpoint but asks the *inverse* question: which prescribed vectors can be induced while retention fractions and a trust graph are held fixed? Bersetche's forward identities alone do not state the neighborhood-cut criterion or the complete-loopless concentration ceiling.

Berend (2020) studies inverse PageRank, optimizing edge transition probabilities to approximate a desired stationary score vector. Section 5.3 supplies some solvability observations, including a complete network with self-loops, and emphasizes obstacles in sparser networks; it does not present the exact all-subset flow feasibility criterion proved here. The distinction between a fully connected network *allowing* self-loops and the loopless network is essential to the sharp ceiling.

Gölz, Kahng, Mackenzie and Procaccia (2018) connect classical proxy-delegation concentration to confluent and splittable flows, but their agents either vote at designated sinks or fully delegate; our every-visit positive self-retention imposes different flow equalities and produces the explicit nonmajority barrier. Garcia and Romance (2021) treat unweighted network design for prescribed *rankings* rather than the exact quantitative vector on a fixed graph. Alouf-Heffetz and collaborators (2024) analyze election control by redirecting arcs and changing approval winners, not continuous retention and exact inverse cast-weight targets. General bipartite max-flow and Hall-type circulation criteria are classical; the claimed contribution is their exact inverse interpretation in this particular transitive retention model and its sharp attainable polytope, not the max-flow theorem itself.

## Limitations

The model fixes retention before choosing forwarding probabilities and permits zero weights on allowed arcs. The conclusion does not apply unchanged to arbitrary direct self-delegation probabilities, personalized source weights, heterogeneous individual initial votes, arbitrary nonconservative penalties, infinite networks, or a requirement that every allowed outgoing arc carry *strictly positive* probability. The no-majority result requires a **common** retention parameter; heterogeneous retention can give a single agent a strict majority. Publication priority beyond the specific inspected literature remains uncertain. No independent external audit has been performed.

## References

1. F. M. Bersetche, *Generalizing Liquid Democracy to multi-agent delegation: A Voting Power Measure and Equilibrium Analysis*, arXiv:2209.14128 (first submitted 2022-09-28), https://arxiv.org/abs/2209.14128 .
2. G. Berend, *Efficient algorithm to compute Markov transitional probabilities for a desired PageRank*, EPJ Data Science **9**, 23 (2020), https://doi.org/10.1140/epjds/s13688-020-00240-z .
3. P. Gölz, A. Kahng, S. Mackenzie and A. D. Procaccia, *The Fluid Mechanics of Liquid Democracy*, arXiv:1808.01906 (2018), https://arxiv.org/html/1808.01906v1 .
4. E. Garcia and M. Romance, *Controlling centrality: The Inverse ranking problem for spectral centralities of complex networks*, arXiv:2111.01473 (2021), https://arxiv.org/abs/2111.01473 .
5. M. Utke and U. Schmidt-Kraepelin, *Anonymous and Copy-Robust Delegations for Liquid Democracy*, NeurIPS 36 (2023), https://arxiv.org/abs/2307.01174 .
6. S. Alouf-Heffetz, T. Inamdar, P. Jain, Y. More and N. Talmon, *Controlling Delegations in Liquid Democracy*, arXiv:2403.07558 (2024), https://arxiv.org/abs/2403.07558 .
