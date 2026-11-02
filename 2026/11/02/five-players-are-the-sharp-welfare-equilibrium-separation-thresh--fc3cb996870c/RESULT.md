# Five players are the sharp welfare–equilibrium separation threshold in binary network coordination

## Finding
For every connected simple undirected graph with between two and four vertices, and every heterogeneous preference vector with entries strictly between zero and one in the binary threshold-coordination model below, **every** welfare-maximizing action profile is a strict pure Nash equilibrium. Five vertices are sharp: the five-vertex path with preferences \((1/10,2/5,2/5,9/10,9/10)\) has the unique welfare optimum \((b,b,a,a,a)\), of welfare \(23/5\), but this is not a Nash equilibrium. The highest Nash-equilibrium welfare is \(9/2\), a strict loss of \(1/10\).

## Assumptions and scope
Let \(G=(V,E)\) be an undirected, simple, connected graph with \(2\le |V|<\infty\). Player \(i\) chooses \(a\) or \(b\), and has a fixed parameter \(0<\gamma_i<1\). For every neighbor choosing the same action \(a\), player \(i\) receives \(\gamma_i\); for every neighbor choosing the same action \(b\), player \(i\) receives \(1-\gamma_i\); mismatched edges give zero. Total utility is the sum across neighbors, and social welfare \(W\) is the sum of player utilities. A strict pure Nash equilibrium means that every unilateral action reversal strictly decreases the deviator's own utility. Vertices are labeled and welfare is *not* normalized by the number of players or edges.

## Proof
**Universal sharp lower-order statement.** In a mixed welfare-maximizing profile, each action must have at least two users. Indeed, a singleton action player receives zero from every incident edge; switching to the other action makes all these edges matched and raises social welfare strictly because both endpoints' matched-edge payoffs are positive. Thus, for two or three vertices, any welfare optimum must be unanimous. A unanimous profile is a strict Nash equilibrium on a connected graph, since each vertex has positive degree and changing action would erase all its strictly positive payoffs.

For four vertices, a mixed welfare optimum must have exactly two \(a\) and two \(b\) players. Both same-action pairs must be adjacent, or a vertex of a nonadjacent pair could switch and strictly raise welfare from zero incident matched edges. Write the two within-action edges as \(ab\) (action \(a\)) and \(cd\) (action \(b\)); let \(m\ge1\) count the cross-action edges. Mixed welfare is \(\gamma_a+\gamma_b+(1-\gamma_c)+(1-\gamma_d)<4\). For the two unanimous profiles, the sum of their respective welfare values is \(2|E|=2(m+2)\): each edge contributes \(\gamma_i+\gamma_j\) under unanimous \(a\) and \(2-\gamma_i-\gamma_j\) under unanimous \(b\). If \(m\ge2\), at least one unanimous profile therefore has welfare at least \(m+2\ge4\), contradicting mixed optimality. Hence \(m=1\), and the graph is the path \(a-b-c-d\) with first pair choosing \(a\) and second pair \(b\). Comparing the mixed welfare with the two unanimous profiles gives
\[
\gamma_b+3\gamma_c+2\gamma_d\le2,\qquad
2\gamma_a+3\gamma_b+\gamma_c\ge4.
\]
Since \(0<\gamma_d\) and \(\gamma_a<1\), these imply \(\gamma_b+3\gamma_c<2<3\gamma_b+\gamma_c\). In turn \(\gamma_b>1/2\) and \(\gamma_c<1/2\): if the first failed, the right inequality would force \(\gamma_c>1/2\), contradicting the left; the second follows symmetrically. Therefore the two interior vertices strictly prefer their current action to switching, since each has one same-action neighbor and one opposite-action neighbor. Both leaves strictly prefer to match their unique neighbor. The mixed optimum is a strict Nash equilibrium. This proves the universal claim for all \(|V|\le4\), without discretizing parameters.

**Sharp five-vertex witness.** Take the path with edges \((1,2),(2,3),(3,4),(4,5)\) and preference vector \((\gamma_1,\ldots,\gamma_5)=(1/10,2/5,2/5,9/10,9/10)\). For the prefix of length \(i\), let \(F_i(a)\) and \(F_i(b)\) be the maximum welfare of its edges among profiles whose final action is respectively \(a\) or \(b\). Define \(A_i=\gamma_i+\gamma_{i+1}\) and \(B_i=2-A_i\). Then \(F_1(a)=F_1(b)=0\) and
\[
F_{i+1}(a)=\max\{F_i(a)+A_i,F_i(b)\},\quad
F_{i+1}(b)=\max\{F_i(b)+B_i,F_i(a)\}.
\]
The exact successive pairs \((F_i(a),F_i(b))\) for \(i=2,3,4,5\) are \((1/2,3/2)\), \((3/2,27/10)\), \((14/5,17/5)\), and \((23/5,18/5)\). Backtracking the strictly dominant recurrence branches yields the unique full optimum \((b,b,a,a,a)\) of welfare \(23/5\). At player \(3\), the current action \(a\) matches player \(4\), yielding \(2/5\), while switching to \(b\) matches player \(2\), yielding \(3/5\). Thus player \(3\) has a strict gain \(1/5\): the optimum is not Nash.

For completeness, applying the elementary best-response inequality at every vertex to each of the exactly \(2^5=32\) action profiles yields exactly three Nash equilibria: \((a,a,a,a,a)\) (welfare \(22/5\)), \((b,b,b,a,a)\) (welfare \(9/2\)), and \((b,b,b,b,b)\) (welfare \(18/5\)). The full finite enumeration is implemented with exact rationals in `verify.py`; it enumerates every one of the \(32\) profiles, not a sample. The best equilibrium welfare is therefore \(9/2\).

## Verification
Execute `python verify.py` using Python's standard library. It verifies every one of the \(32\) witness profiles, reconstructs the unique optimum, the three equilibria, their exact rational welfare and the dynamic-programming maximum. As an additional sanity check it exhausts all simple connected graphs on two through four vertices using every preference vector in \(\{1/4,1/2,3/4\}^{|V|}\): 3,195 graph–parameter instances and 3,674 maximizing profiles. These finite grid tests corroborate the algebra but do **not** replace the above all-parameter proof.

## Relationship to prior work
Deligkas, Eiben, Gutin, Neary and Yeo (2023) develop the binary-action polymatrix/threshold model and investigate existence and computation of efficient outcomes, including complexity results. Their published formulations encompass this positive matched-edge special case, but their inspected equilibrium-efficiency and hardness results do not state the universal four-vertex welfare-to-Nash implication or the sharp five-vertex path witness. The 2017 work of Neary and Newton on heterogeneous threshold preferences is adjacent motivation; its abstract was inspected, while full-text overlap remains a literature risk. A negative database search alone is not evidence of uniqueness.

## Limitations
The universal theorem requires connected, simple, undirected networks, positive matched-edge rewards, two actions, and no action-specific base payoff. It is not a claim about general polymatrix games, about welfare maximization algorithms, or about minimum heterogeneity. The five-vertex welfare loss is one explicit example rather than an optimal price-of-stability bound. Independent validation has not been performed.

## References
- A. Deligkas, E. Eiben, G. Gutin, R. Neary and A. Yeo, *Complexity of Efficient Outcomes in Binary-Action Polymatrix Games with Implications for Coordination Problems*, first public version 2023-05-11, https://arxiv.org/abs/2305.07124 (full text: https://arxiv.org/html/2305.07124v1).
- A. Deligkas, E. Eiben, G. Gutin, R. Neary and A. Yeo, related later version, https://arxiv.org/html/2311.03195v2.
- P. R. Neary and J. Newton, *Heterogeneity in Preferences and Behavior in Threshold Models*, 2017, https://doi.org/10.22574/jmid.2017.12.005 (abstract consulted; full text not verified).
