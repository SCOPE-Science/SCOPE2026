# One vacancy forces terminating jumps on complete bipartite networks; two vacancies can restore cycles

## Finding

**One-vacancy convergence and the sharp vacancy obstruction.** Let \(G=K_{s,t}\) be a complete bipartite graph with \(s,t\geq1\), occupied by \(r\geq b\geq1\) individually distinguishable red and blue agents and exactly one vacant vertex, so \(s+t=r+b+1\). Every agent of color \(c\in\{R,B\}\) receives payoff \(u_c(f)\), where \(u_R,u_B:[0,1]\to\mathbb R\) are *arbitrary fixed functions* and \(f\) is the fraction of agents of the same color in the occupied closed neighborhood, including the agent herself. An allowed jump moves one agent to the vacant vertex and is improving only when its own payoff strictly increases.

Every sequence of strictly improving jumps terminates at a pure Nash equilibrium after at most \(2b+1\) jumps, regardless of update order or the utility functions. In particular this holds for the single-peaked jump Schelling model for **every** peak \(\Lambda\in(0,1)\), every permitted single-peaked payoff, and every balanced or unbalanced population.

The guarantee is sharp *in its vacancy assumption*: with two vacant vertices, the standard single-peaked model has an improving-response cycle on \(K_{3,3}\) with three red and one blue agent. For the normalized tent payoff with peak \(\Lambda=9/20\), the repeated four-jump sequence is
\[
 R_2:b_1\to a_2,\qquad B:b_3\to a_3,\qquad
 R_2:a_2\to b_1,\qquad B:a_3\to b_3,
\]
starting from red agents at \(a_1,b_1,b_2\), blue at \(b_3\), and vacancies at \(a_2,a_3\). Here \(a_1,a_2,a_3\) and \(b_1,b_2,b_3\) are the two parts of \(K_{3,3}\). This sequence returns to the **same labeled state**, and every move is strictly improving.

## Assumptions and scope

The graph is simple and complete bipartite. There are exactly two colors, positive populations of both colors, no immobile agents, and initially exactly one vacancy for the convergence theorem. Agents of one color share their payoff function, but the two color functions may differ; neither function need be continuous, monotone, nor single-peaked. All moves are unilateral jumps into a vacancy. A terminal state is a pure Nash equilibrium precisely because no strictly improving jump is available.

The single-peaked specialization uses \(p_\Lambda(f)=f/\Lambda\) for \(0\leq f\leq\Lambda\) and \(p_\Lambda(f)=(1-f)/(1-\Lambda)\) for \(\Lambda\leq f\leq1\). This is one admissible payoff in the single-peaked model and is used for the counterexample, whereas the convergence theorem holds for the entire permitted family.

## Proof

**1. Reduction to a path of population states.** Write \(A,B\) for the two vertex parts of sizes \(s,t\). When the unique vacancy belongs to \(A\), write \(A_i\) if exactly \(i\) red agents occupy \(A\); this state then has \(s-1-i\) blue agents in \(A\). When the vacancy belongs to \(B\), write \(B_i\) if exactly \(i\) red agents occupy \(A\), which then has \(s-i\) blue agents in \(A\). Only feasible states are considered, i.e. all counts are nonnegative and agree with the total \(r,b\).

A jump between vertices of the same part leaves the jumping agent's occupied opposite-part neighbors unchanged, hence leaves her same-color fraction and payoff unchanged. Every strictly improving jump therefore changes the vacancy's part. From \(A_i\) a red agent jumping from \(B\) to \(A\) reaches \(B_{i+1}\), and a blue agent jumping from \(B\) to \(A\) reaches \(B_i\). Reversing such a jump gives the only corresponding reverse possibilities. Thus the **undirected** graph of possible population-state changes is a subgraph of the integer-indexed path with edges
\[
 A_i-B_i,\qquad A_i-B_{i+1}.
\]
This graph has no undirected cycle.

**2. Every population-state edge has a fixed strict direction.** For the red transfer \(A_i\to B_{i+1}\), the mover's pre- and post-jump same-color fractions are, respectively,
\[
 \frac{i+1}{s}\quad\text{and}\quad\frac{r-i}{t}.
\]
For any reverse red transfer \(B_{i+1}\to A_i\), these two fractions occur in exactly the reverse order. Both transfers involve the same color-specific function \(u_R\); at most one direction can be strictly improving. Likewise, the blue transfer \(A_i\to B_i\) compares
\[
 \frac{s-i}{s}\quad\text{with}\quad\frac{b-s+i+1}{t},
\]
and the reverse blue transfer exchanges those fractions. Therefore every undirected population-state edge is oriented in at most one direction by all possible improving jumps. No directed improving walk can revisit a population state, since a consistently oriented forest has no directed cycle.

**3. Bound and existence.** For each location of the vacancy, the number of blue agents in \(A\) is one of \(0,1,\dots,b\), and fixes its red count. Hence there are at most \(2(b+1)\) feasible population states. Each improving jump visits a new state, so there are at most \(2b+1\) such jumps. In a finite game, a maximal sequence consequently terminates in a configuration with no improving jump, which is a pure Nash equilibrium. The argument applies to *every* choice of updates and does not use any single-peaked condition.

**4. Two-vacancy obstruction.** Give \(K_{3,3}\) its two parts \(\{a_1,a_2,a_3\}\) and \(\{b_1,b_2,b_3\}\), place red agents \(R_1,R_2,R_3\) initially at \(a_1,b_1,b_2\), blue agent \(B\) at \(b_3\), and leave \(a_2,a_3\) empty. For \(\Lambda=9/20\), use the normalized tent function \(p_\Lambda\) above. Moving \(R_2:b_1\to a_2\) improves her payoff from \(p_\Lambda(1)=0\) to \(p_\Lambda(2/3)=20/33\). Next \(B:b_3\to a_3\) improves from \(p_\Lambda(1/3)=20/27\) to \(p_\Lambda(1/2)=10/11\). Moving the *same* \(R_2:a_2\to b_1\) improves from \(0\) to \(20/33\), and the *same* \(B:a_3\to b_3\) improves from \(20/27\) to \(10/11\). All four improvements are strict, and the initial labeled placement is restored. The one-vacancy condition cannot be relaxed to two vacancies, even for regular bicliques and a genuine single-peaked payoff. \(\square\)

## Verification

The included `verify.py` is standalone Python using exact rational arithmetic. It replays the **labeled** four-jump cycle, asserts each exact payoff pair and strict improvement, and checks that the final six-vertex configuration is identical to the initial configuration. It also enumerates all feasible compressed population states for every \(1\leq b\leq r\leq9\), every possible pair of nonempty part sizes with one vacancy, four normalized single-peaked payoffs, and deterministic arbitrary color-specific payoff tables; it checks all computed transitions against the path graph, absence of reverse directed edges and directed cycles, and the cardinality bound. These finite checks corroborate, but do not replace, the general proof above. Run `python verify.py` in a Python 3.9+ environment; no external packages are required.

## Relationship to prior work

Friedrich, Lenzner, Molitor and Seifert (arXiv:2302.12107v1, 2023) introduce the single-peaked jump model. Their Theorem 2.4 proves termination on cycles at peak \(1/2\) with one vacant node, and their Corollary 3.3 guarantees equilibrium *existence* on bipartite graphs when the red population is at least half the graph order. Neither statement supplies arbitrary-peak, every-update convergence for complete bipartite graphs; in particular their population condition excludes balanced populations with one vacancy. Their Theorem 2.1 gives a two-vacancy improving cycle on paths/rings, not on complete bipartite graphs.

Narayanan, Sabbagh and Voudouris (arXiv:2305.17757, 2023) obtain one-vacancy convergence on regular graphs and spiders for a different, monotone diversity payoff. This does not imply the theorem for arbitrary nonmonotone functions or irregular complete bipartite networks. Bilò, Bilò, Lenzner and Molitor (arXiv:2204.12599, 2022) study **swap** moves with no vacancies, a different move model. Earlier strategic Schelling improvement dynamics (Echzell et al., arXiv:1907.07513, 2019) study threshold-based, monotone objectives and have no complete-bipartite one-vacancy arbitrary-payoff theorem. Schelling games with monotone objectives (Elkind et al., arXiv:1902.07937, 2019) likewise do not imply the claimed preference-independent improvement bound.

The substantive new mechanism is that exactly one vacancy collapses all two-color moves on a biclique onto an *oriented path*, whereas a second vacancy already permits a four-step improving square. This is a statement about the entire improvement relation, not simply existence of a stable placement.

## Limitations

The path argument uses complete cross-part adjacency, exactly two homogeneous colors, and a single vacancy. It does not cover incomplete bipartite graphs, individual-specific payoff functions, three or more agent types, immobile agents, or multiple vacancies. The explicit two-vacancy example proves failure of the finite-improvement property, **not** absence of Nash equilibria. The \(2b+1\) convergence bound is universal but is not claimed to be optimal for the restricted single-peaked family. Literature priority remains subject to specialized, possibly unindexed results on exact Schelling game dynamics. No independent validation has been performed.

## References

1. T. Friedrich, P. Lenzner, L. Molitor, L. Seifert, *Single-Peaked Jump Schelling Games*, arXiv:2302.12107v1, first posted 2023-02-23. https://arxiv.org/abs/2302.12107
2. L. Narayanan, Y. Sabbagh, A. A. Voudouris, *Diversity-Seeking Jump Games in Networks*, arXiv:2305.17757v1, first posted 2023-05-28. https://arxiv.org/abs/2305.17757
3. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Tolerance Is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599v1, first posted 2022-04-26. https://arxiv.org/abs/2204.12599
4. E. Elkind, J. Gan, A. Igarashi, W. Suksompong, A. A. Voudouris, *Schelling Games on Graphs*, arXiv:1902.07937v1, first posted 2019-02-21. https://arxiv.org/abs/1902.07937
5. H. Echzell, T. Friedrich, P. Lenzner, L. Molitor, M. Pappik, F. Schöne, F. Sommer, D. Stangl, *Convergence and Hardness of Strategic Schelling Segregation*, arXiv:1907.07513v1, first posted 2019-07-17. https://arxiv.org/abs/1907.07513
