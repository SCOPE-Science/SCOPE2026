# Perfect edge domination of circular ladder graphs

## Finding
For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the labelled prism with vertices \(u_i,v_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). An edge set \(F\) is **perfect edge dominating** when every edge outside \(F\) has exactly one distinct edge of \(F\) sharing an endpoint with it; selected edges have no restriction. Its complete cardinality polynomial is
\[
\mathcal D_n(z)=\sum_{F\text{ perfect edge dominating}}z^{|F|}
=z^{3n}+6\,\mathbf{1}_{\{6\mid n\}}z^n.
\]
Moreover, the six proper solutions when \(6\mid n\) are exactly the six cyclic phases of the period-six column word \((0,1,5,0,2,6)\), where column code \(a_i=T_i+2B_i+4R_i\) encodes the selected top rail, bottom rail and rung edges. Thus minimum perfect edge domination has size \(n\) with six minimizers when \(6\mid n\); otherwise its unique solution is the entire edge set of size \(3n\).

## Assumptions and scope
All graphs are finite, simple and labelled; \(n\) is an integer at least three, and the two horizontal rails and the spokes are edges of the Cartesian product. The edges in column \(i\) are \(T_i=u_iu_{i+1}\), \(B_i=v_iv_{i+1}\), \(R_i=u_iv_i\) (subscripts modulo \(n\)). The same symbols denote their indicator values in \(\{0,1\}\). The polynomial counts actual subsets of the \(3n\) labelled edges, without quotienting by graph automorphisms.

## Proof
Every edge in this cubic graph is adjacent to exactly four other edges. The definition translates exactly into these three simultaneous conditions for every \(i\):
\[
R_i=1\ \text{or}\ T_{i-1}+T_i+B_{i-1}+B_i=1,
\]
\[
T_i=1\ \text{or}\ T_{i-1}+T_{i+1}+R_i+R_{i+1}=1,
\]
\[
B_i=1\ \text{or}\ B_{i-1}+B_{i+1}+R_i+R_{i+1}=1.
\]
The word 'or' is inclusive: a selected edge automatically satisfies its own clause.

Construct the finite directed graph \(H\) with vertex set consisting of the pair states \((a,b)\in\{0,\ldots,7\}^2\) that participate in at least one allowed transition. Put an arc \((a,b)\to(b,c)\) exactly when the displayed three conditions hold at the centre column encoded by \(b\). A periodic valid edge selection on \(P_n\) is therefore in exact bijection with a closed directed walk of length \(n\) in \(H\), beginning at its labelled column zero; its weight is the sum of the three binary digits of the first component of each pair state.

**Finite transition lemma.** The graph \(H\) has exactly \(42\) participating pair states and \(102\) distinct arcs. Its only strongly connected components containing a directed cycle are the single state \((7,7)\), having its loop, and the six states
\[
(0,1)\to(1,5)\to(5,0)\to(0,2)\to(2,6)\to(6,0)\to(0,1).
\]
Each such component is itself exactly the displayed simple directed cycle; no other component contains a loop. This is a finite, exhaustive lemma, with a complete standard-library Python certificate in `verification/verify.py`: the code examines all \(8^3=512\) triples, constructs every participating state and transition, computes strongly connected components independently of any graph package, and asserts the exact vertex, arc, and recurrent-component lists. The transition predicate is a literal transcription of the three displayed equalities, so this finite inspection covers all possible local configurations, not a sample of graph orders.

A closed directed walk lies entirely inside one strongly connected component. The loop \((7,7)\) gives one all-edge solution with \(3n\) selected edges. The six-cycle permits a closed walk of length \(n\) if and only if \(6\mid n\); when permitted its six initial phases give six distinct selections. Over one traversal, the first components are \(0,1,5,0,2,6\), which have six set binary digits in total; hence each solution has exactly \(n\) selected edges. No other closed walks are possible. This proves the complete classification and both formulas.

## Verification
Run `python3 verification/verify.py` with Python 3.8 or later. The certificate confirms the \(42\)-state, \(102\)-arc transition graph, exactly the loop and six-cycle as recurrent components, and the resulting coefficient predictions through length \(48\). An independent direct edge-neighbourhood enumeration checks **every** subset of the labelled prism edges for \(3\le n\le6\). A separate direct C++17 search inspected every subset for \(3\le n\le7\) during development; the universal conclusion relies on the exhaustive finite transition lemma rather than these small-order tests.

## Relationship to prior work
Grippo, Lin, Moyano and Vera (2026) study perfect edge dominating-set enumeration and give general counting algorithms for generalized series-parallel graphs and chordal graphs. The prisms considered here have induced squares (hence are not chordal), and a \(K_4\) minor (hence are not generalized series-parallel); their stated algorithmic classes do not directly provide this periodic closed formula. Earlier perfect-edge-domination work gives graph-class complexity and structure but no located exact cyclic-prism counting statement. Related open ladders have different nonperiodic boundary behaviour: the cyclic phase condition is a genuinely additional global constraint.

## Limitations
The assertion concerns unweighted perfect **edge** domination, not ordinary edge domination, vertex perfect domination, or dominating induced matchings. It does not count by symmetry or address arbitrary generalized Petersen graphs. Historical novelty remains conditional on full-text comparison with broader graph algorithms and any as-yet-unlocated specialized prism enumerations; accessible information for the principal 2026 preprint included its abstract and an extended secondary account, but not its complete primary PDF. The finite-state proof certificate is computationally checked, not independently formally verified.

## References
1. L. N. Grippo, M. C. Lin, V. Moyano and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, first public 2026-07-04, https://arxiv.org/abs/2607.03894.
2. M. C. Lin, V. Lozin, V. A. Moyano and J. L. Szwarcfiter, *Perfect Edge Domination: Hard and Solvable Cases*, arXiv:1705.08379, https://arxiv.org/abs/1705.08379.
3. L. N. Grippo, M. C. Lin and C. Vera, *Perfect Edge Domination in \(P_6\)-free Graphs and in Graphs Without Efficient Edge Dominating Sets*, preprint 2025, https://arxiv.org/abs/2509.04598.
