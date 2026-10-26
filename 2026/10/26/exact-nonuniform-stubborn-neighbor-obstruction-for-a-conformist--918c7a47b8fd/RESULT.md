# Exact nonuniform stubborn-neighbor obstruction for a conformist–rebel edge

## Finding
In a finite undirected multi-strategy network game, let adjacent flexible vertices \(u\) and \(v\) be, respectively, a conformist and a rebel. Assume every other neighbor of either vertex is stubborn. For \(m\ge2\) strategies, define \(p_i\) and \(q_i\) as the counts of stubborn neighbors choosing strategy \(i\) at \(u\) and \(v\), and set
\[
P=\operatorname*{arg\,max}_{1\le i\le m}p_i,
\qquad Q=\operatorname*{arg\,min}_{1\le i\le m}q_i.
\]
**Exact local obstruction theorem.** The conformist and rebel admit no pair of simultaneous pure best responses **if and only if** \(|Q|\ge2\) and \(Q\subseteq P\). Accordingly, this condition forbids a pure Nash equilibrium in *any* larger network containing such an edge, regardless of the rest of the network. If these two flexible vertices are the only nonstubborn agents, the condition is also necessary and sufficient for nonexistence of a pure Nash equilibrium.

The criterion extends the uniformly pinned local obstruction to arbitrary, independently nonuniform pinned-neighbor counts. In particular, for three strategies the vectors \(p=(0,1,1)\) and \(q=(1,0,0)\) forbid equilibrium even though neither endpoint has uniform pinned counts. For two strategies, obstruction occurs precisely when both count vectors are balanced.

## Assumptions and scope
Let \(G\) be a finite simple undirected graph, \(m\ge2\), and each player use one of \(m\) strategies. A conformist maximizes the number of neighbors matching its own strategy; a rebel maximizes the number disagreeing (equivalently minimizes the number matching); a stubborn player has a fixed strategy and never deviates. Ties are legitimate best responses. Suppose \(u\sim v\), \(u\) is conformist, \(v\) is rebel, and every neighbor of \(u\) other than \(v\), and every neighbor of \(v\) other than \(u\), is stubborn. The neighbors may overlap, have arbitrary fixed strategies, or have other edges; only their stubborn behavior matters. The counts \(p_i,q_i\) are arbitrary nonnegative integers, and zeros are permitted. The claim concerns pure strategies, not mixed Nash equilibria or best-response convergence.

## Proof
Let \(a\) be the conformist's strategy and \(b\) the rebel's strategy. For any strategy \(i\), the conformist's matching payoff after choosing \(i\) is
\[
C_i(b)=p_i+\mathbf 1_{\{i=b\}},
\]
and the rebel's matching *cost* after choosing \(i\), which it seeks to minimize, is
\[
R_i(a)=q_i+\mathbf 1_{\{i=a\}}.
\]
This computation includes exactly one possible contribution from the active edge; fixed neighbors contribute the integer counts. Therefore \((a,b)\) is a simultaneous best response precisely when \(a\) maximizes \(C_i(b)\) and \(b\) minimizes \(R_i(a)\).

**Nonexistence direction.** Suppose \(|Q|\ge2\) and \(Q\subseteq P\). If \(b\notin Q\), choose any \(j\in Q\setminus\{a\}\), which is possible because \(Q\) has at least two members. Then \(R_j(a)=\min_i q_i\), whereas \(R_b(a)\ge\min_i q_i+1\). Thus a best-responding rebel must choose \(b\in Q\). Because \(Q\subseteq P\), this \(b\) also maximizes \(p_i\). Hence \(C_b(b)=\max_i p_i+1\), strictly exceeding every \(C_i(b)\) with \(i\ne b\): the conformist must choose \(a=b\). But choose \(j\in Q\setminus\{b\}\). Now \(R_j(b)=\min_i q_i<R_b(b)=\min_i q_i+1\), contradicting that the rebel best responds. There is no simultaneous best response.

**Existence direction, case one.** Suppose \(Q\not\subseteq P\). Choose any \(b\in Q\setminus P\) and \(a\in P\). Because \(a\ne b\) and the counts are integers, \(p_a\ge p_b+1\). Thus \(C_a(b)=p_a\) is maximal among all conformity choices: \(C_b(b)=p_b+1\le p_a\), and for other strategies \(C_i(b)=p_i\le p_a\). The rebel at \(b\) has matching cost \(R_b(a)=q_b=\min_i q_i\), hence also best responds. This gives an explicit equilibrium pair.

**Existence direction, case two.** Suppose \(Q\subseteq P\) and \(|Q|=1\). Let \(Q=\{a\}\) and choose \(b=a\). Then the conformist's match count \(p_a+1\) exceeds that at every other strategy because \(a\in P\). For each \(j\ne a\), the integer strict inequality \(q_j>q_a\) implies \(q_j\ge q_a+1\). Consequently, the rebel's matching cost \(q_a+1\) at \(a\) is no greater than the cost \(q_j\) of any deviation. Both agents best respond. These cases exhaust the complement of \(|Q|\ge2\) and \(Q\subseteq P\), completing the proof.

The local result applies without change within a larger network, because neither flexible endpoint interacts with any other nonstubborn agent. For the entire two-hub network containing only these flexible players and stubborn neighbors, the exhibited pair together with stubborn agents' fixed behavior gives a pure Nash equilibrium whenever the obstruction fails.

For \(m=2\), the only subset \(Q\) with \(|Q|\ge2\) is the whole two-strategy set, so \(Q\subseteq P\) requires \(P\) to be the whole set as well. Thus both count vectors must be constant. For \(m=3\), \(p=(0,1,1)\) and \(q=(1,0,0)\) give \(P=Q=\{2,3\}\) and so produce a nonuniform obstruction. The corresponding tree has degrees three and two at the flexible vertices (neither is congruent to one modulo three) and maximum degree three, so it lies outside both the original balanced-motif degree pattern and the strictly larger-action-than-degree regime of the earlier tree existence theorem.

## Verification
The standalone program `verify.py` enumerates the pure best-response inequalities directly, independently of the set criterion, for every pair of vectors in \(\{0,1,2\}^m\) when \(m=2,3,4\) and for all pairs in \(\{0,1\}^5\). In each configuration, it compares the existence of a simultaneous best response with the negation of the proposed obstruction and validates the constructive witness when an equilibrium exists. In total, 7,371 plus 1,024 configurations are checked, all exactly using integer arithmetic. It separately tests the stated three-strategy nonuniform instance. The finite computation is a regression check, not the proof for unbounded counts or strategies.

Reproduce with `python verify.py` using Python 3 and its standard library; no optional dependencies are needed.

## Relationship to prior work
Pei, Cao, and Zhang (2026) introduce and analyze the multi-strategy conformist–rebel–stubborn model. Their local \(M^*\) obstruction assumes equal stubborn-neighbor counts across every strategy at *both* endpoints. Their tree characterization applies under the restriction that the number of strategies exceeds the maximum graph degree. The exact condition here includes every \(M^*\) configuration, but also handles nonuniform counts and provides the reverse, constructive existence direction in the two-hub setting. The displayed nonuniform instance has three strategies and maximum degree three and is not an \(M^*\) configuration. Their star theorem treats a single strategic hub, not the two adjacent strategic hubs studied here.

Cao, Sánchez, and Zhang (2026) study a predecessor with binary choices, heterogeneous payoffs, and a balanced conformist–rebel local obstruction. Its binary obstruction agrees with the two-strategy specialization, rather than covering the new multi-strategy classification. General matching-pennies observations explain why a wholly unbiased matching/anti-matching pair has no pure equilibrium, but they do not entail the precise extremal-set criterion for arbitrary nonuniform stubborn-neighbor counts.

## Limitations
This theorem characterizes one naturally isolated flexible edge and gives a reusable *sufficient* obstruction in an otherwise arbitrary network. It does not supply a necessary-and-sufficient equilibrium criterion for arbitrary networks with interacting flexible players. It neither asserts uniqueness of equilibria when they exist nor addresses their dynamics, mixed equilibria, or probabilities of encountering this local structure in random graphs. The specific analytic criterion is independently proved; a search cannot completely exclude an equivalent unpublished or differently indexed earlier result.

## References
1. Shan Pei, Wenjie Cao, Boyu Zhang. *Network games with three types of players*. arXiv:2607.10997, first posted 2026-07-13. https://arxiv.org/abs/2607.10997 . Consulted model definition, Definition 2/Lemma 1, Theorem 5 and star section.
2. Wenjie Cao, Ángel Sánchez, Boyu Zhang. *Network games with heterogeneous players*. arXiv:2607.05932, first posted 2026-07-07. https://arxiv.org/abs/2607.05932 . Consulted binary sufficient existence conditions, balanced local obstruction and supplementary argument.
3. Classical matching-pennies game, for the symmetric two-action matching versus mismatching intuition; no historical novelty is claimed for this special case.
