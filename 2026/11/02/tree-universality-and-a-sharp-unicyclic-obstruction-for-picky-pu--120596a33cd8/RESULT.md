# Tree universality and a sharp unicyclic obstruction for picky public-goods equilibria

## Finding

**Theorem.** Fix any integer \(q\ge2\). In the strict homogeneous binary public-goods game on a finite simple undirected graph \(G=(V,E)\), each vertex chooses \(x_v\in\{0,1\}\) and its unique best response to \(k\) active neighbors is
\[
T_q(k)=\begin{cases}1&k\in\{0,q\},\\0&\text{otherwise}.\end{cases}
\]

1. On **every finite forest**, there is a pure Nash equilibrium. A profile can be constructed in \(O(|V|+|E|)\) arithmetic operations, including for unbounded degree and arbitrary \(q\ge2\).
2. For **every \(q\ge3\)** there is a connected unicyclic graph with exactly \(2q+1\) vertices and no pure Nash equilibrium: take a triangle, distinguish two vertices, and attach \(q-1\) pendant leaves to each of those two vertices.
3. For \(q=3\), seven vertices is the **smallest possible order of a connected unicyclic graph without a pure Nash equilibrium**. Exhaustive exact enumeration gives no obstruction on \(3,4,5,6\) vertices (respectively \(1,15,222,3660\) distinct labeled unicyclic graphs); the seven-vertex construction in part 2 has no equilibrium.

The first part asserts existence and an explicit algorithm, not convergence of asynchronous best-response dynamics. For every nonempty forest an equilibrium is nonzero, because \(T_q(0)=1\).

## Assumptions and scope

Graphs are finite, simple, loopless, undirected, and unweighted; forests may have multiple components or isolated vertices. The parameter \(q\) is the same integer at every vertex; actions are simultaneous binary strategic choices, but the equilibrium condition is static:
\[
x_v=T_q\left(\sum_{u\in N(v)}x_u\right)\qquad(v\in V).
\]
There are no indifferent best responses. The unicyclic graph has exactly one independent cycle. The assertions do not cover directed edges, heterogeneous thresholds, weighted neighbors, or an arbitrary nonmonotone response pattern.

## Proof

### Universal forest existence and construction

Root a tree, and for each vertex \(v\) with parent \(p\), let \(S_v(a)\subseteq\{0,1\}\) denote the possible value(s) of \(x_v\) for a strategy assignment on the subtree at \(v\) in which every subtree vertex best responds, conditional on the parent action \(x_p=a\). For a root, use a fictitious parent acting \(0\), which contributes nothing to its neighbor count. We inductively prove the three invariants
\[
S_v(0)\ne\varnothing,\qquad S_v(1)\subseteq\{0\},\qquad
S_v(1)=\varnothing\Longrightarrow S_v(0)=\{0,1\}.
\]

For a leaf, \(S_v(0)=\{1\}\) and \(S_v(1)=\{0\}\), since \(T_q(0)=1\) and \(T_q(1)=0\).

Suppose the invariants hold for the children of \(v\). If \(v\) chooses \(0\), each child can choose from its nonempty \(S_u(0)\). Let \(I=[L,U]\cap\mathbb Z\) be all possible sums of active children: a singleton child set forces its value, and a child set \(\{0,1\}\) contributes a free binary choice, so *every* integer between the minimum and maximum is feasible. Thus \(v=0\) is feasible with parent action \(a\) exactly when some \(s\in I\) has \(a+s\notin\{0,q\}\).

If \(v\) chooses \(1\), each child must choose from \(S_u(1)\subseteq\{0\}\). Consequently \(v=1\) is feasible for parent action \(0\) precisely when every child has nonempty \(S_u(1)\); it is never feasible for parent action \(1\), since the resulting active-neighbor count is \(1\) and \(T_q(1)=0\). This proves \(S_v(1)\subseteq\{0\}\).

To show \(S_v(0)\ne\varnothing\), if every child has nonempty \(S_u(1)\), choose \(v=1\) and all children \(0\). Otherwise some child has \(S_u(1)=\varnothing\), hence \(S_u(0)=\{0,1\}\) by induction. Therefore \(U>L\). Two consecutive integers cannot both belong to \(\{0,q\}\) when \(q\ge2\); thus some \(s\in I\) satisfies \(T_q(s)=0\), allowing \(v=0\).

Finally, if \(S_v(1)=\varnothing\), then \(v=0\) is impossible for parent action \(1\). Hence for *every* \(s\in I\), \(T_q(1+s)=1\). Since \(s\ge0\) and \(q\ge2\), this forces \(I=\{q-1\}\). In particular, no child has \(S_u(0)=\{0,1\}\), so by the inductive implication no child has empty \(S_u(1)\). Thus \(v=1\) is feasible for parent action \(0\). Also \(T_q(q-1)=0\), so \(v=0\) is feasible for parent action \(0\). Hence \(S_v(0)=\{0,1\}\), closing the induction.

At a root, \(S_v(0)\ne\varnothing\) yields an equilibrium on that tree. Combine independent tree solutions across components. Computing each set requires only the child forced-one count and flexible-child count, plus whether any child has empty \(S_u(1)\). For backtracking, choose a child sum in the feasible integer interval and assign that many flexible children action \(1\), then descend. Every vertex and incident edge is processed a constant number of times, giving \(O(|V|+|E|)\) arithmetic operations.

### A one-cycle obstruction for every \(q\ge3\)

Use a triangle on vertices \(r,u,v\). Attach \(q-1\) leaves to \(u\) and \(q-1\) leaves to \(v\). In any equilibrium each leaf must choose the opposite action to its hub, because its only possible active-neighbor counts are zero and one.

Write \(a=x_u\), \(b=x_v\), \(c=x_r\). The triangle vertex sees \(a+b\le2<q\), so \(c=1\) exactly when \(a=b=0\). If \((a,b)=(0,0)\), then \(c=1\) and each hub sees \(q\) active neighbors and should choose \(1\), contradiction. If \((a,b)=(1,0)\) or \((0,1)\), the inactive hub sees the active other hub together with its \(q-1\) active leaves, hence \(q\) active neighbors and should choose \(1\), contradiction. If \((a,b)=(1,1)\), then \(c=0\), every hub sees just its active opposite hub, and should choose \(0\), contradiction. These four cases exhaust all hub actions. The graph has \(3+2(q-1)=2q+1\) vertices and exactly one simple cycle.

### Sharpness at seven vertices for \(q=3\)

Every connected unicyclic graph on \(n\) labeled vertices is obtained by taking a labeled spanning tree and adding an unordered edge absent from it. The standard Prüfer correspondence enumerates every labeled tree exactly once using a word of length \(n-2\). The executable `verify.py` constructs each such tree for \(3\le n\le6\), adds every nonedge, deduplicates by exact sorted edge lists, and tests the equilibrium equations for all \(2^n\) binary action profiles. Its verified distinct-graph counts are \(1,15,222,3660\), and **every graph in that exhaustive list admits an equilibrium** for \(q=3\). The explicit seven-vertex graph from the preceding part has none; therefore seven is sharp. Here exhaustive enumeration proves the finite lower bound because the generation is provably complete, not because random tests found no counterexample.

## Verification

Run `python3 verify.py` using Python's standard library. The program checks every labeled tree on at most six vertices for \(q=2,3,4,5,6\), compares constructive feasible-subtree states with brute-force equilibrium existence, enumerates all labeled connected unicyclic graphs on \(3\) through \(6\) vertices for \(q=3\), and checks the explicit triangular double-hub obstructions for \(q=3,\ldots,8\). The inductive theorem and the all-parameter obstruction are proved above independently of these finite checks.

## Relationship to prior work

Klimm and Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs* (arXiv:2301.11849v1, first posted January 27, 2023), prove NP-completeness on unrestricted undirected graphs for precisely the finite nonmonotone family \(T_q\), \(q\ge2\). The present result instead isolates an entire unbounded-degree graph class with unconditional pure equilibrium existence, and identifies the first minimal one-cycle failure for \(q=3\). General NP-hardness does not imply either existence on forests or the minimal obstruction.

Gilboa's *A Characterization of Complexity in Public Goods Games* (arXiv:2301.11580v1) independently proves general finite-pattern hardness. Yu et al., *Computing Equilibria in Binary Networked Public Goods Games* (arXiv:1911.05788v4), and Maiti and Dey, *On Parameterized Complexity of Binary Networked Public Goods Game* (arXiv:2012.01880v1), provide algorithms for restricted network structures, including generic tree equilibrium *decisions* and guaranteed existence on paths/cycles/bicliques. These are different logical claims: a decision algorithm may report nonexistence, while existence on paths does not imply existence on all branching trees. Gilboa and Nisan (arXiv:2207.04238v1) classify related response patterns and establish hardness but do not give this tree-plus-unicyclic boundary in the inspected text.

## Limitations

The exact seven-vertex minimum is asserted only for **connected unicyclic graphs with \(q=3\)**. Although the explicit construction gives an obstruction on \(2q+1\) vertices for every \(q\ge3\), no general minimality claim for \(q>3\) is made. The results do not settle whether every unicyclic graph admits a pure equilibrium for \(q=2\), do not bound best-response trajectory lengths, and do not address welfare optimality. The uniqueness or global bibliographic priority of the result is not asserted; unlocated specialized graph-game literature may contain equivalent statements. The small finite certificate uses exact integers and exhaustive enumeration; no computational search substitutes for the forest induction.

## References

- Klimm, M., and Stahlberg, M. J., *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849v1 (2023), https://arxiv.org/abs/2301.11849 .
- Gilboa, M., *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580v1 (2023), https://arxiv.org/abs/2301.11580 .
- Gilboa, M., and Nisan, N., *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238v1 (2022), https://arxiv.org/abs/2207.04238 .
- Yu, S., Zhou, K., Brantingham, P. J., and Vorobeychik, Y., *Computing Equilibria in Binary Networked Public Goods Games*, arXiv:1911.05788v4, https://arxiv.org/html/1911.05788v4 .
- Maiti, A., and Dey, P., *On Parameterized Complexity of Binary Networked Public Goods Game*, arXiv:2012.01880v1, https://arxiv.org/abs/2012.01880 .
