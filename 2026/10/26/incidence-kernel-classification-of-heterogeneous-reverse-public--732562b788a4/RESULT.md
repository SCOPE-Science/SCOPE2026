# Incidence-kernel classification of heterogeneous reverse public-goods equivalence

## Finding

A regular multiplayer interaction structure can make the ordinary and reversed public-goods games **exactly indistinguishable under every finite-strength pairwise Fermi imitation update**, even when the players' waste/productivity factors are unequal. The precise condition is a nullspace of the vertex-to-group incidence matrix, not homogeneity.

**Theorem (complete classification).** Let \(H=(V,\mathcal E)\) be a finite connected \(g\)-uniform, \(r\)-regular hypergraph, where \(g\ge2\), \(r\ge1\), \(n=|V|\ge2\), and connected means that its two-section (vertices adjacent when they share a group) is connected. Write \(B\in\{0,1\}^{n\times |\mathcal E|}\) for its unsigned vertex–group incidence matrix. Fix \(m>0\), a vector of player-specific factors \(\lambda\in(1,g)^n\), and a finite selection strength \(\omega>0\). Match the reverse-game defection bit \(y_i\in\{0,1\}\) with the ordinary-game cooperation bit \(x_i=1-y_i\). Define conditional imitation probabilities for every directed adjacent pair by the same logistic rule, using accumulated game payoffs and the same exogenous sampling convention in both games.

The following are equivalent:

1. For every binary strategy profile and every ordered adjacent pair, the two models assign the same *conditional probability of imitation*.
2. All strategy-independent differences between the players' accumulated reverse and ordinary payoffs agree.
3. \(BB^{\mathsf T}\lambda\) is constant across vertices.
4. \(B^{\mathsf T}(\lambda-\bar\lambda\mathbf1)=0\), where \(\bar\lambda=n^{-1}\sum_i\lambda_i\).

Consequently, exactly the parameter vectors in \((\bar\lambda\mathbf1+\ker B^{\mathsf T})\cap(1,g)^n\) produce the full equality, and nonconstant such vectors exist if and only if \(\operatorname{rank}B<n\). When these conditions hold, the two finite-state strategy processes admit a coupling under which their entire trajectories coincide almost surely, for **every initial law and every finite horizon**. The statement is exact at all \(\omega>0\), not merely in a weak-selection limit.

**Sharp graph specialization.** If each group is an edge of a connected \(d\)-regular simple graph, a nonconstant factor vector gives this exact equality if and only if the graph is bipartite and the factor is constant on each bipartition class. The two class values may differ, provided both lie in \((1,2)\). In a connected nonbipartite regular graph, only the constant factor vectors qualify.

**Genuinely multiplayer examples.** If \(H\) is the complete \(g\)-partite \(g\)-uniform hypergraph with \(q\ge2\) vertices in each class (one vertex of every class per group), then \(\ker B^{\mathsf T}\) has dimension \(g-1\). All and only the factor assignments constant within each class qualify; their class values may vary freely subject to a fixed sum. Thus two-person bipartiteness is the first case of a larger family of exactly neutral heterogeneities.

**Quantitative obstruction away from equivalence.** On a connected nonbipartite \(d\)-regular graph, let \(Q=dI+A\) be the signless Laplacian, \(L=dI-A\) the Laplacian, and \(v=\lambda-\bar\lambda\mathbf1\). Then

\[
\left(\sum_{\{i,j\}\in E}[(Q\lambda)_i-(Q\lambda)_j]^2\right)^{1/2}
\ge \sqrt{\lambda_2(L)}\,\lambda_{\min}(Q)\,\|v\|_2.
\]

Both spectral factors are strictly positive. Thus every nonconstant heterogeneity creates a nonzero *measurable edgewise payoff-shift discrepancy*. More generally, for any regular uniform hypergraph and directed adjacent pair \(i\leftarrow j\), the difference of the two conditional imitation probabilities is at most

\[
\frac{\omega m}{4g}\left|(BB^{\mathsf T}\lambda)_i-(BB^{\mathsf T}\lambda)_j\right|.
\]

If an exogenous update-pair distribution is common to the models, their strategy-state distributions after \(T\) steps (from the same initial law) differ in total variation by at most \(\min\{1,T\varepsilon\}\), with \(\varepsilon\) the largest right-hand side above.

## Assumptions and scope

The hypergraph may have any finite size, but all its groups have size \(g\), each vertex lies in exactly \(r\) groups, and its two-section is connected. All players have the same positive requirement/contribution capacity \(m\); only the efficiency/waste factors \(\lambda_i\) vary. Each factor lies strictly in \((1,g)\). Strategies are binary and factors are fixed to individuals. Payoffs are *summed* over every incident group (which is also equivalent to group averaging here because \(r\) is uniform). Directed adjacent pairs are sampled with a common payoff-independent rule assigning positive probability to each directed pair. An individual may copy a neighbor with strictly increasing logistic probability \(\sigma_\omega(z)=1/(1+\exp(-\omega z))\), where \(z\) is neighbor payoff minus focal payoff.

In each incident group \(e\), the matched game payoffs are defined by

\[
\pi^{R,e}_i=m y_i-\frac m g\sum_{j\in e}\lambda_j y_j,
\qquad
\pi^{P,e}_i=-m(1-y_i)+\frac m g\sum_{j\in e}\lambda_j(1-y_j).
\]

The first is the player-heterogeneous reverse public-goods rule of Wang–Szolnoki specialized to common capacity. The second is the ordinary public-goods rule with player-specific return factors and equal contribution capacities. These explicit choices, rather than all possible conventions for public-goods games, are the theorem's domain.

The equivalence is an *iff* statement about conditional directed imitation probabilities (and the resulting pathwise agreement when equal); it does **not** assert that equality of unconditional, already-averaged Markov transition matrices in arbitrary sampling schemes forces the same condition.

## Proof

**1. Strategy-independent payoff offset.** Substituting \(x_i=1-y_i\) into the ordinary payoff expression yields, for every group \(e\ni i\) and every strategy configuration,

\[
\pi^{R,e}_i-\pi^{P,e}_i=m-\frac m g\sum_{j\in e}\lambda_j.
\]

Summing over the \(r\) groups incident to vertex \(i\) produces a deterministic offset

\[
\Delta_i:=\Pi_i^R-\Pi_i^P
=mr-\frac m g(BB^{\mathsf T}\lambda)_i.
\]

For a directed comparison \(i\leftarrow j\), the two logistic arguments differ by \(\Delta_j-\Delta_i\). Strict monotonicity of \(\sigma_\omega\) for any finite \(\omega>0\) proves equality of the conditional probability for all strategy profiles precisely when \(\Delta_i=\Delta_j\) on every adjacent ordered pair. Connectivity then implies a common offset on all vertices. This proves statements 1–3 equivalent. A common external randomization for selecting a pair and accepting imitation gives an explicit synchronous pathwise coupling whenever all conditional probabilities agree.

**2. Incidence nullspace.** Uniformity and regularity give \(B^{\mathsf T}\mathbf1_n=g\mathbf1_{|\mathcal E|}\) and \(B\mathbf1_{|\mathcal E|}=r\mathbf1_n\). Consequently \(BB^{\mathsf T}\mathbf1_n=gr\mathbf1_n\). Let \(v=\lambda-\bar\lambda\mathbf1_n\). If \(BB^{\mathsf T}\lambda\) is constant, taking its scalar product with \(\mathbf1_n\) shows it equals \(gr\bar\lambda\mathbf1_n\). Hence \(BB^{\mathsf T}v=0\). The identity \(v^{\mathsf T}BB^{\mathsf T}v=\|B^{\mathsf T}v\|_2^2\) forces \(B^{\mathsf T}v=0\). The converse is immediate. Because \(B\mathbf1_{|\mathcal E|}=r\mathbf1_n\), every vector in \(\ker B^{\mathsf T}\) already sums to zero. A sufficiently small nonzero multiple of any nonzero kernel vector added to any fixed interior constant factor remains admissible. This proves statement 4 and the rank criterion.

**3. Graph dichotomy.** When groups are graph edges, \((B^{\mathsf T}v)_{\{i,j\}}=v_i+v_j\). Along every edge, therefore, \(v_j=-v_i\). Connectivity propagates one amplitude with alternating signs. An odd cycle forces that amplitude to vanish; without odd cycles the graph is bipartite and every vector is an alternating constant on its two color classes. These are all solutions. A connected regular bipartite graph has equally many vertices on each class, so the displayed \(\bar\lambda\) is their arithmetic mean.

**4. Complete multipartite hypergraphs.** For complete \(g\)-partite uniform groups, \(B^{\mathsf T}v=0\) means that the sum over one selected vertex from each part is zero for every selection. Holding all choices but one fixed and changing the chosen vertex shows the two corresponding coordinates of \(v\) coincide. Thus \(v\) is constant on each part; then the only remaining equation is that the \(g\) part constants sum to zero. This is a \((g-1)\)-dimensional subspace. Equal part sizes guarantee regularity and mean zero of these vectors.

**5. Quantitative estimates.** For graph groups, \(BB^{\mathsf T}=Q\), and \(Q\mathbf1=2d\mathbf1\). On a nonbipartite connected graph, \(Q\) is positive definite; connectedness gives \(\lambda_2(L)>0\). Put \(w=Qv\); since \(\mathbf1^{\mathsf T}w=0\),

\[
\sum_{\{i,j\}\in E}(w_i-w_j)^2=w^{\mathsf T}Lw
\ge\lambda_2(L)\|w\|_2^2
\ge\lambda_2(L)\lambda_{\min}(Q)^2\|v\|_2^2.
\]

The constant component of \(Q\lambda\) cancels in each edge difference. Finally, \(\sup_z|\sigma'_\omega(z)|=\omega/4\), so the mean-value theorem applied to the two payoff differences yields the one-step bound. Coupling the exogenous pair selection and the Bernoulli accept/reject randomness stepwise gives a mismatch probability at most \(\varepsilon\) per still-coupled step; the union bound gives the stated finite-horizon total-variation estimate.

## Verification

The self-contained Python 3 program `verify_equivalence.py` uses only the standard library. Run `python verify_equivalence.py` from the package directory. It performs 1,227 assertions, including exact `Fraction` comparisons of accumulated reverse and ordinary payoffs for every binary strategy profile of a four-cycle, triangle, and six-vertex complete tripartite three-uniform hypergraph; conditional logistic probability checks; and an exact spectral identity on the triangle. It prints `PASS 1227 exact/numeric checks; nonzero mismatch cases=12; triangle spectral equality=27/50` when all checks succeed. The numerical logistic evaluations are finite diagnostics, not a proof of the universal theorem.

For an explicit four-cycle, set consecutive vertex factors to \((6/5,9/5,6/5,9/5)\) and \(m=1\). Each vertex has reverse-minus-ordinary total payoff exactly \(-1\), independently of all four strategies, so the dynamics are identical at every selection strength. For a triangle, factors \((6/5,3/2,9/5)\) instead give respective offsets \((-17/20,-1,-23/20)\), violating equivalence. On the triangle the spectral lower bound is attained with both squared sides equal to \(27/50\).

For the complete tripartite three-uniform hypergraph with two vertices per class and class factors \((6/5,9/5,3/2)\), there are eight groups, every vertex is in four groups, and every total payoff offset equals \(-2\) for all \(64\) binary strategy configurations.

## Relationship to prior work

Wang and Szolnoki (2022), Sections 2.2, 3.2–3.3, 4.1–4.2, establish the reverse public-goods model, its homogeneous correspondence with the ordinary public-goods game, and heterogeneous examples with differing evolutionary outcomes. Their printed formula for heterogeneous reverse payoffs is the starting point here. The present result classifies *which nonconstant player-specific factors still yield exact equality of every directed Fermi comparison* on an arbitrary regular uniform group structure, identifies the graph bipartiteness boundary, and provides quantitative nonbipartite obstruction and multiplayer kernel families. It does not challenge their heterogeneous examples, whose interaction groups and factor patterns need not meet the kernel condition.

Lüthi, Tomassini and Pestelacci (2009) examine payoff-shift invariance for network replicator dynamics, especially degree heterogeneity and normalization. They do not present the reverse-versus-ordinary heterogeneous group-payoff incidence classification or the graph/hypergraph kernel conclusions. Flores and collaborators (2023) study evolving contribution heterogeneity in ordinary public-goods games via Fermi simulations, but not reversed-versus-ordinary fixed-factor pathwise identity. Bervoets and Makihara (2023 working paper) study Nash-equilibrium comparative statics of network public-goods provision rather than Fermi stochastic imitation. The signless-Laplacian bipartite nullspace itself is standard graph theory; the novelty assessment concerns its *model-specific necessary-and-sufficient interpretation and resulting dynamic coupling*, not rediscovery of that graph fact.

## Limitations

Factors are fixed and represent equal-capacity individual heterogeneity; the models do not permit factor values to change when a strategy is copied. Equality is for the stated matched payoff conventions and common payoff-independent pair sampling with finite positive selection strength. Nonregular or nonuniform group incidence, mixed group-size conventions, player-specific consumption capacities, mutation or payoff-dependent sampling are not covered. The quantitative graph lower bound concerns edgewise payoff-shift differences, not a uniform positive lower bound on Fermi probability differences; the logistic slope can become small. No claim of independent review or priority certification is made. Broader unpublished work on payoff gauges or evolutionary games could contain equivalent formulations.

## References

1. Chaoqian Wang and Attila Szolnoki (2022), *A reversed form of public goods game: equivalence and difference*, New Journal of Physics 24, 123030; arXiv:2212.05014 (first public preprint 2022-12-09), https://arxiv.org/abs/2212.05014 . Relevant primary sections 2.2, 3.2–3.3, 4.1–4.2.
2. Leslie Lüthi, Marco Tomassini, Enea Pestelacci (2009), *Evolutionary games on networks and payoff invariance under replicator dynamics*, Biosystems 96, 213–222; arXiv:0902.1447, https://arxiv.org/abs/0902.1447 .
3. Lucas S. Flores, Mendeli H. Vainstein, Heitor C. M. Fernandes, Marco A. Amaral (2023), *Heterogeneous contributions can jeopardize cooperation in the Public Goods Game*, arXiv:2305.11257, https://arxiv.org/abs/2305.11257 .
4. Sebastian Bervoets and Kohmei Makihara (2023), *Public Goods in Networks: Comparative Statics Results*, AMSE Working Paper 2317, https://www.amse-aixmarseille.fr/sites/default/files/working_papers/wp_2023_-_nr_17.pdf .
