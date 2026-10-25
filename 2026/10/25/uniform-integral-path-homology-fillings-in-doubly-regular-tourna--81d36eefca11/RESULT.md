# Uniform integral path-homology fillings in doubly regular tournaments

## Finding
Let \(T\) be any doubly regular tournament on \(4t+3\) vertices, with integer \(t\ge 1\). For the integral regular path-chain complex of Grigor'yan, Lin, Muranov and Yau,
\[
H_1^{\mathrm{path}}(T;\mathbb Z)=0.
\]
More quantitatively, each integral cycle \(z\in\ker(\partial_1:\Omega_1(T;\mathbb Z)\to\Omega_0(T;\mathbb Z))\) bounds an integral chain \(B\in\Omega_2(T;\mathbb Z)\) consisting solely of *transitive* directed two-paths and satisfying
\[
\partial_2B=z,\qquad \lVert B\rVert_1\le 3\lVert z\rVert_1.
\]
For every directed three-cycle, exactly \(t\) other vertices either dominate all three vertices or are dominated by all three. For \(t=0\), the directed three-cycle instead has \(H_1^{\mathrm{path}}\cong\mathbb Z\); thus the size restriction is necessary.

## Assumptions and scope
A tournament is a finite loopless directed graph with exactly one arc between each pair of distinct vertices. A doubly regular tournament has \(4t+3\) vertices, each with outdegree and indegree \(2t+1\), and each distinct pair has exactly \(t\) common out-neighbors. The standard equivalent common-in-neighbor condition follows by counting, or can be included as a symmetric hypothesis. Here we assume both pairwise counts explicitly to avoid relying on a nontrivial equivalence.

For a directed path \([a,b]\), the chain differential is \(\partial[a,b]=[b]-[a]\). For an allowed directed two-path \([a,b,c]\), its formal boundary is \([b,c]-[a,c]+[a,b]\); it belongs to the integral regular path-chain group \(\Omega_2\) when that boundary contains only allowed arcs. In particular a *transitive two-path* means \(a\to b\to c\) and \(a\to c\), and it lies in \(\Omega_2\) as a single generator. No claim concerns nonregular conventions, higher-degree path homology, or integral homotopy type.

Write \(\lVert z\rVert_1\) for the sum of absolute integral coefficients of allowed oriented arcs and \(\lVert B\rVert_1\) for the analogous sum for the chosen transitive two-path generators. These are chain-level norms, not homology norms.

## Proof
**1. Every cyclic triangle admits exactly \(t\) cone vertices.** Fix \(a\to b\to c\to a\). For each vertex \(d\notin\{a,b,c\}\), let \(k(d)\) count how many of the three fixed vertices \(d\) dominates. For each of the three pairs inside the directed cycle there are \(t\) common in-neighbors and \(t\) common out-neighbors; none is a vertex of the cycle itself. Double-counting such common neighbors gives
\[
6t=\sum_{d\notin\{a,b,c\}}\left(\binom{k(d)}2+\binom{3-k(d)}2\right).
\]
The summand equals \(3\) when \(k(d)\in\{0,3\}\) and \(1\) otherwise. There are \(4t\) outside vertices, so if \(h\) counts those with \(k(d)\in\{0,3\}\), then \(6t=4t+2h\); hence \(h=t\). Since \(t\ge1\), such a cone vertex exists. It either dominates all three vertices or is dominated by all three.

**2. Every oriented triangle is a short integral boundary.** For distinct \(a,b,c\), define its oriented perimeter as
\[
C(a,b,c)=e(a,b)+e(b,c)+e(c,a),\quad
 e(u,v)=\begin{cases}[u,v]&u\to v,\\-[v,u]&v\to u.\end{cases}
\]
For a transitive triple ordered \(a\to b\to c\), \(a\to c\), the perimeter satisfies \(C(a,b,c)=\partial[a,b,c]\), up to reversing its orientation. If the triple is directed cyclically \(a\to b\to c\to a\) and \(d\) dominates all its members, then
\[
C(a,b,c)=\partial\big([d,a,b]+[d,b,c]+[d,c,a]\big).
\]
If all its members dominate \(d\), the corresponding equality is
\[
C(a,b,c)=\partial\big([a,b,d]+[b,c,d]+[c,a,d]\big).
\]
Each of the three displayed two-paths in either expression is transitive and its shortcut arc exists. The identities therefore hold **inside the integral regular path-chain complex**: no nonallowed face is introduced. A triangle perimeter bounds a chain of one or three transitive paths, with integral coefficient norm at most three.

**3. Integral cycle-basis argument.** Fix a root vertex \(r\), with an arbitrary order on all other vertices. Because the underlying undirected graph is complete, the oriented perimeters \(C(r,i,j)\), one for each unordered pair of vertices \(i,j\ne r\), form an integral basis of \(\ker\partial_1\). Indeed, every such perimeter has coefficient \(\pm1\) on its own nonroot edge \(\{i,j\}\) and coefficient \(0\) on all other nonroot edges. Given any integral cycle \(z\), subtract the corresponding integer multiples of these perimeters to eliminate every nonroot edge. The remainder is a cycle supported on a star, and each nonroot vertex's zero net boundary forces its unique star-edge coefficient to vanish. Thus no remainder remains, and the absolute sum of basis coefficients is exactly the sum of \(\lvert z_e\rvert\) over nonroot edges, at most \(\lVert z\rVert_1\).

Using the short fillings from step 2 for each basis perimeter and combining them integrally gives \(B\in\Omega_2\), \(\partial B=z\) and \(\lVert B\rVert_1\le3\lVert z\rVert_1\). Consequently \(\ker\partial_1=\operatorname{im}\partial_2\) over \(\mathbb Z\), as asserted. This proves vanishing including all possible integral torsion, not merely rational vanishing.

**4. Boundary at three vertices.** For the directed three-cycle, its three possible allowed directed two-paths each has a distinct forbidden shortcut face. No nonzero integer combination can cancel these forbidden faces. Hence \(\Omega_2=0\), while the directed perimeter generates \(\ker\partial_1\cong\mathbb Z\), giving \(H_1^{\mathrm{path}}\cong\mathbb Z\).

## Verification
The standalone `verify_drt_path_h1.py` (Python standard library only) reconstructs the prime Paley tournaments at orders \(7,11,19,23,31\), checks every required regularity and common-neighbor count, enumerates and fills every vertex-triple perimeter with an explicit integral transitive-path chain, and verifies the exact cone count for every directed triangle. It also separately constructs the integral two-path generators (transitive triangles and differences between two-paths with the same missing shortcut) and computes first-boundary ranks modulo \(2,3,5,101\) for Paley orders \(7,11\), contrasting with the ordinary cyclic tournament on seven vertices. Run `python3 verify_drt_path_h1.py`; the accompanying `verify_drt_path_h1.log` ends with `VERIFY_OK_DRT_INTEGRAL_PATH_H1`. Computations test finite examples; the counting and integral cycle-basis argument prove all parameter values.

## Relationship to prior work
The regular path-chain theory and its first-homology definitions originate in Grigor'yan–Lin–Muranov–Yau's *Homologies of path complexes and digraphs* (first arXiv version dated 2012-07-12). Their later *Homotopy theory for digraphs* relates path homology to directed homotopy and fundamental groups. The general theory of first path homology for undirected graphs, including cycle-space/triangle-square interpretations, is not a theorem about one-way orientations of tournaments. Published computations of cyclic-tournament first path homology instead give a nonzero integral first class for a different family; directed-flag-complex results on Paley tournaments use a different chain complex. The local precise cone count, uniform integral three-path filling and doubly regular tournament conclusion are the specific claims assessed here, not the existence of path homology itself.

## Limitations
The homology statement concerns integral **regular GLMY path homology in degree one**. It does not assert simply connectedness of an associated space, vanishing in higher path-homology degrees, a decomposition of a directed flag complex, or sharp optimality of the coefficient three. The bibliographic search cannot rule out all equivalent previously published but unindexed statements; closest relevant full and partial sources and remaining uncertainty are described in `REVIEW.md` and `AUDIT.json`. Finite checks are not a substitute for the uniform proof.

## References
1. A. Grigor'yan, Y. Lin, Y. Muranov, S.-T. Yau, *Homologies of path complexes and digraphs*, arXiv:1207.2834, initial public version 2012-07-12, https://arxiv.org/abs/1207.2834 .
2. A. Grigor'yan, Y. Lin, Y. Muranov, S.-T. Yau, *Homotopy theory for digraphs*, arXiv:1407.0234, initial public version 2014-07-01, https://arxiv.org/abs/1407.0234 .
3. M. Kempton, F. Münch, S.-T. Yau, *Relationships between cycle spaces, gain graphs, graph coverings, fundamental groups and path homology*, arXiv:1710.01264, 2017, https://arxiv.org/abs/1710.01264 ; undirected/bidirected graph comparison, not a directed-tournament implication.
