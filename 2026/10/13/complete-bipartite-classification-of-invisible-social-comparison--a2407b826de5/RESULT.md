# Complete-bipartite classification of invisible social comparison in death–birth games

## Finding

**Theorem (complete characterization of comparison invisibility).** Let \(G=(V,E)\) be any finite connected, undirected, loopless, unweighted simple graph with \(|V|=N\ge 2\). Fix a selection strength \(\delta>0\). For a vector of social-comparison susceptibilities \(\lambda\in\mathbb R^V\), call \(\lambda\) *replacement-invisible* when the individual conditional replacement probabilities in the social-comparison donation game are exactly the same as those for \(\lambda=0\), for **every** binary strategy configuration \(x\in\{0,1\}^V\), every \(b,c>0\), and every permitted reproducer/death-site pair.

The set of all replacement-invisible profiles is exactly
\[
\mathcal Z(G)=\begin{cases}
\{0\},& G\text{ is not a complete bipartite graph},\\
\{\lambda:\lambda_i=a\text{ on }A,\ \lambda_j=d\text{ on }B,\ a,d\in\mathbb R\},&G=K_{|A|,|B|}.
\end{cases}
\]
The bipartition parts \(A,B\) are nonempty, but either may consist of one vertex. The statement holds at **every fixed** \(\delta>0\), not only in the weak-selection limit. On a complete bipartite graph, any two profiles constant within each part produce **identical individual replacement probabilities**, hence the same full discrete-time strategy transition kernel, finite-time distributions, fixation probabilities, and distributions of absorption times. The two part constants may be arbitrarily large, unequal, and of either sign.

In particular, a star may have an arbitrarily comparison-oriented hub with entirely neutral comparison susceptibilities on the leaves without affecting any replacement event.

## Assumptions and scope

Write \(A_G\) for the adjacency matrix and \(P=D^{-1}A_G\) for simple random walk, so \(P_{ij}=1/\deg(i)\) precisely when \(ij\in E\). Fix \(b,c,\delta>0\). For \(x\in\{0,1\}^V\), the *expected* donation payoff, effective fitness, and probability that \(i\) replaces the uniformly selected dead vertex \(j\) are respectively
\[
 u(x)=-cx+bPx,\quad F_i^\lambda(x)=\exp\!\bigl(\delta[u_i(x)+\lambda_i(Pu(x))_i]\bigr),
\]
\[
 e_{ij}^{\lambda}(x)=\frac1N\,\frac{1_{\{ij\in E\}}F_i^\lambda(x)}{\sum_{k\sim j}F_k^\lambda(x)}.
\]
These are the expected-payoff version of the fitness and death–birth rules of Xiong et al., equations (1), (2), and (7), arXiv:2609.39012v1. The definition of replacement-invisibility is equality of the **individual reproducer probabilities**, not merely equality of aggregated strategy-state transitions or of a fixation statistic. The theorem requires the equality for all strategy configurations and all positive benefit/cost parameters, with fixed \(\delta>0\) and fixed \(\lambda\).

## Proof

**1. Competitor-ratio cancellation.** For any death site \(j\) and its two distinct neighboring competitors \(i,k\), exponentials are strictly positive and the factors \(1/N\) cancel. Equality of the conditional replacement probabilities with their values at \(\lambda=0\) is equivalent to
\[
\lambda_i(Pu(x))_i=\lambda_k(Pu(x))_k
\tag{1}
\]
for all choices of \(x,b,c\). Necessity follows by taking logarithms of the ratio of the probabilities for \(i\) and \(k\); sufficiency follows because all competitors at a given vacancy then receive the same positive fitness multiplier. At a site with just one neighbor, there is no pairwise condition and its replacement probability is always \(1/N\).

**2. Two identities forced by universal invisibility.** For the fully cooperative configuration \(x=\mathbf1\), stochasticity of \(P\) gives \(u=(b-c)\mathbf1\) and \(Pu=(b-c)\mathbf1\). Choose \(b\ne c\) in (1); then
\[
 \lambda_i=\lambda_k\quad\text{whenever }i,k\text{ share a neighbor}.\tag{2}
\]
If this common susceptibility equals \(a\ne0\), substitute \(u=-cx+bPx\) into (1):
\[
 a(P_i-P_k)(-cI+bP)x=0\quad\text{for every }x,b,c.
\]
Fix \(b>0\) and vary \(c>0\); the coefficient of \(c\) must vanish. Choosing each binary basis vector \(x=e_v\) yields \((P_i-P_k)e_v=0\) for every vertex \(v\), therefore
\[
P_i=P_k\quad\text{for any common-neighbor pair with nonzero common susceptibility}.\tag{3}
\]
Here \(P_i\) denotes row \(i\) of \(P\). In a loopless unweighted graph, equality of these rows is equivalent to equality of the open neighbor sets.

**3. Graph structure of common-neighbor pairs.** Form an auxiliary graph \(H\) on \(V\), linking distinct vertices when they share a neighbor in \(G\). A path of even length in \(G\) becomes a walk in \(H\) by skipping every other vertex. If \(G\) is connected and bipartite, the two bipartition parts are exactly the connected components of \(H\) (including singleton components). If \(G\) is connected and nonbipartite, its odd cycle lets any walk's parity be changed by a detour, hence any two vertices are connected by an even walk. Thus \(H\) is connected.

Equation (2) makes \(\lambda\) constant on every component of \(H\). If \(G\) is nonbipartite and \(\lambda\ne0\), this common constant is nonzero. By (3), all rows of \(P\) are identical. But adjacent vertices \(v,w\) cannot have equal rows, because \(P_{vw}>0\) while \(P_{ww}=0\). Thus nonbipartite \(G\) allows only \(\lambda=0\).

If \(G\) is bipartite with sides \(A,B\), (2) makes \(\lambda\) constant on each side. Suppose \(\lambda\ne0\); at least one side, say \(A\), has a nonzero constant. Equation (3) says all \(P_i\) with \(i\in A\) are identical, hence all members of \(A\) have the same neighbor set \(S\subseteq B\). Connectedness guarantees that every vertex of \(B\) is adjacent to at least one vertex of \(A\), so \(S=B\). Consequently every edge between \(A\) and \(B\) is present: \(G=K_{|A|,|B|}\). The argument is unchanged when \(A\) or \(B\) is a singleton.

**4. Sufficiency and exact consequences.** If \(G=K_{|A|,|B|}\), rows \(P_i\) coincide on each side. For every death vertex \(j\in A\), all competitors lie in \(B\), and for \(\lambda\) constant on \(B\) the added term \(\lambda_i(Pu)_i\) is the same for every competitor. Their fitnesses are all multiplied by a common factor, which cancels from the denominator of \(e_{ij}^\lambda\). The same argument applies when \(j\in B\). Hence all individual replacement probabilities equal their zero-comparison values. The replacement-rule identity at every state makes the finite Markov transition kernels identical. All conclusions about distributions and fixation follow by equality of Markov transition kernels. This proves both directions.

**A transition-changing witness outside the classified class.** On the four-vertex path \(0-1-2-3\) let \(x=(1,0,0,0)\), \(b=c=1\), and all \(\lambda_i=1\). For the death of vertex \(1\), its competitors \(0,2\) have \(u_0=-1\), \(u_2=0\), while \((Pu)_0=1/2\), \((Pu)_2=1/4\). Their reproduction odds differ from the no-comparison odds by a factor \(e^{\delta/4}\). Since the competitors have different strategies, the strategy-transition probabilities actually change in this example.

## Verification

The accompanying standard-library-only file `verify_graph.py` is executable with `python verify_graph.py`. Its exact-rational calculations exhaust all connected labelled simple graphs on \(2\) through \(6\) vertices, independently checking that the common-neighbor row-equality property characterizes complete bipartite graphs. For sizes \(2\) through \(5\), it independently checks the full susceptibility-profile characterization for all vectors with entries in \(\{-1,0,1\}\) (180099 graph-profile combinations). It then tests every binary strategy state on \(K_{2,3}\) for two unequal nonzero side constants and exact rational payoffs and verifies the explicit path witness. Its printed `VERIFY_OK` is a finite sanity check, not a substitute for the unrestricted proof above.

## Relationship to prior work

Xiong, Li, Kurths, Szolnoki, and Feng (2026) introduced the social-comparison exponential fitness and death–birth rules and derived weak-selection coalescent expressions. The present finding takes those model equations as assumptions. It proves a different structural statement: an all-strength, all-configuration equality of complete microscopic replacement rules, with a graph-theoretic if-and-only-if classification and complete susceptibility-profile space. In particular, identical weak-selection cooperation thresholds alone would be weaker than the Markov-kernel equality proved here.

Peña and Rochat (2012) examined bipartite *interaction/group structures* and associated multiplayer games; their results do not state comparison-neutrality of the particular death–birth donation-game update considered here. Szolnoki and Perc (2021) studied strategy-selective averaged-payoff *imitation*, not the neighbor-mean additive exponential fitness used here. General death–birth game analyses such as Ohtsuki et al. (2006) do not assert this complete comparison-invisibility classification. These differences are about the mathematical implications of the update rules, rather than terminology alone.

## Limitations

The all-graph converse concerns equality of **individual replacement probabilities for all binary states and positive benefits and costs**. It does not classify graphs on which one particular fixation probability might happen to be unchanged, or profiles producing equal *aggregated* strategy-state kernels without equality of microscopic replacement events. No assertion is made for directed/weighted/disconnected graphs, self-loops, birth–death updates, strategy-selective imitation, randomly realized single-encounter payoffs instead of the stated expected-payoff rule, or endogenously evolving susceptibilities. At \(\delta=0\) all profiles are trivially invisible; hence strictly positive selection is necessary for the converse. The argument is exact for each finite \(\delta>0\), and does not rely on a weak-selection truncation.

## References

1. Xiong, X., Li, Q., Kurths, J., Szolnoki, A., and Feng, M. *Social comparison shapes the evolution of cooperation in structured populations*. arXiv:2609.39012v1, first publicly posted 2026-09-30. https://arxiv.org/html/2609.39012v1 . See especially Methods (1), (2), (7).
2. Peña, J. and Rochat, Y. *Bipartite Graphs as Models of Population Structures in Evolutionary Multiplayer Games*. PLOS ONE **7**, e44514 (2012). https://doi.org/10.1371/journal.pone.0044514 ; open full text https://pmc.ncbi.nlm.nih.gov/articles/PMC3438187/ .
3. Szolnoki, A. and Perc, M. *The self-organizing impact of averaged payoffs on the evolution of cooperation*. New Journal of Physics **23** (2021). arXiv:2107.01997v1. https://arxiv.org/pdf/2107.01997 .
4. Ohtsuki, H., Hauert, C., Lieberman, E., and Nowak, M. A. *A simple rule for the evolution of cooperation on graphs and social networks*. Nature **441**, 502–505 (2006). https://doi.org/10.1038/nature04605 .
