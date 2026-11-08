# A cubical complete-graph bridge geometry for token sliding on subdivided stars

## Finding

Let \(S_m\) be the tree obtained by subdividing each edge of the star \(K_{1,m}\) exactly once, where \(m\ge3\). Write its central vertex as \(c\), its inner arm vertices as \(a_i\), and its leaves as \(b_i\), for \(i\in[m]\); its edges are \(ca_i\) and \(a_ib_i\). Define \(R_m\) to be the graph of independent sets of size \(m-1\) in \(S_m\), with an edge when a single selected vertex slides across a tree edge and the resulting set stays independent.

**Theorem.** The graph \(R_m\) consists exactly of \(m\) induced, isometric copies \(Q_{m-1}^{(h)}\) of the \((m-1)\)-cube, one for each absent arm \(h\), together with one degree-two bridge vertex \(V_{\{h,k\}}\) for every unordered pair of distinct arms. This vertex makes a two-edge path between the one-coordinate vertices \(U_h(\{k\})\) and \(U_k(\{h\})\) of their respective cubes. There are no other edges. Consequently,
\[
|V(R_m)|=m2^{m-1}+\binom m2,\qquad
|E(R_m)|=m(m-1)2^{m-2}+m(m-1).
\]
The graph is connected and its **exact diameter** is
\[
\operatorname{diam}(R_m)=2m.
\]

In more detail, for \(h\in[m]\) and \(A\subseteq[m]\setminus\{h\}\), let
\[
U_h(A)=\{a_i:i\in A\}\cup\{b_i:i\in[m]\setminus(A\cup\{h\})\}.
\]
For distinct \(h,k\), let
\[
V_{\{h,k\}}=\{c\}\cup\{b_i:i\in[m]\setminus\{h,k\}\}.
\]
The exact distance between **any two cube vertices** is
\[
d(U_h(A),U_k(B))=
\begin{cases}
|A\triangle B|,&h=k,\\
|A\triangle\{k\}|+2+|B\triangle\{h\}|,&h\ne k.
\end{cases}
\]
Distances involving a bridge vertex are recovered exactly by taking one step to either of its two cube neighbors and minimizing; when both endpoints are the same bridge vertex the distance is zero.

In particular, for \(h\ne k\) and \(A=[m]\setminus\{h,k\}\), the two independent sets \(U_h(A)\) and \(U_k(A)\) differ only in which one of the two leaves \(b_h,b_k\) is occupied, yet their sliding distance is **\(2m\)**. Their ordinary set symmetric difference has cardinality two.

## Assumptions and scope

All graphs are finite and simple; arm indices are individually labelled. A legal move changes exactly one vertex of an independent set by sliding the token to an adjacent empty vertex of \(S_m\), preserving cardinality and independence. The theorem concerns **exactly \(m-1\) indistinguishable tokens**, not all token layers and not token jumping. It holds for every integer \(m\ge3\), including the smallest three-arm spider. The full independent-set reconfiguration graph on other token counts is not classified here.

## Proof

**1. Exhaustive state classification.** If \(c\notin I\), each pair \(\{a_i,b_i\}\) contributes at most one selected vertex. Since \(|I|=m-1\), exactly one arm, say \(h\), is empty, and each other arm contributes exactly one selected vertex. The set of arms represented by an inner vertex is \(A\), so \(I=U_h(A)\), uniquely. If \(c\in I\), no inner vertex may be selected; exactly \(m-2\) leaves are selected, giving a unique \(V_{\{h,k\}}\). Thus the stated collection is exhaustive and disjoint.

**2. Exhaustive edge classification.** In a state \(U_h(A)\), sliding between \(a_i\) and \(b_i\) on an occupied arm toggles the membership of \(i\) in \(A\), so for fixed \(h\) the states induce \(Q_{m-1}\). The only possible move involving \(c\) is \(a_k\to c\), and this is permitted exactly when \(A=\{k\}\): every other inner vertex would be adjacent to the newly occupied center. The target is \(V_{\{h,k\}}\). Conversely, \(c\) in \(V_{\{h,k\}}\) can slide only to \(a_h\) or \(a_k\); no occupied leaf can move inward while the center remains selected. Thus \(V_{\{h,k\}}\) has precisely the two neighbors \(U_h(\{k\})\) and \(U_k(\{h\})\). No move changes an empty arm without using such a bridge. This proves the entire graph description, the enumerations, and connectivity for \(m\ge3\).

**3. Exact metric between cube states.** A path of length \(|A\triangle B|\) within one cube connects \(U_h(A)\) to \(U_h(B)\). For \(h\ne k\), toggling the coordinates of \(A\) until only \(k\) remains, crossing the two-edge bridge, and then toggling coordinates to \(B\) gives a path of the advertised length.

To prove optimality simultaneously for both formulas, fix a target cube vertex \(T=U_k(B)\), and assign to every cube vertex the proposed number
\[
f(U_h(A))=
\begin{cases}
|A\triangle B|,&h=k,\\
|A|+|B|+4-2\mathbf1_{k\in A}-2\mathbf1_{h\in B},&h\ne k.
\end{cases}
\]
Across every within-cube edge, exactly one coordinate is toggled and \(f\) changes by exactly one. For each bridge with neighbors \(X=U_i(\{j\})\) and \(Y=U_j(\{i\})\), direct substitution shows \(|f(X)-f(Y)|\le2\): if \(k=i\) or \(k=j\), the difference is two; otherwise, the difference is \(2|\mathbf1_{i\in B}-\mathbf1_{j\in B}|\). Set
\[
f(V_{\{i,j\}})=1+\min\{f(X),f(Y)\}.
\]
Because the two neighboring cube values differ by at most two, \(f\) changes by at most one across either bridge edge. Hence \(f\) is globally \(1\)-Lipschitz on \(R_m\), and \(f(T)=0\). The distance from any vertex \(W\) to \(T\) is therefore at least \(f(W)\). The explicit within-cube or single-bridge path attains this bound whenever \(W\) is a cube vertex, establishing the claimed formula. Since every bridge has exactly two neighbors, the stated endpoint-minimization formula for distances involving bridges follows, including its zero-distance exception.

**4. Sharp diameter.** For cube vertices with the same missing arm, the distance is at most \(m-1\). For distinct missing arms \(h,k\), the formula is at most \(2m\): when neither \(k\in A\) nor \(h\in B\), each of \(A,B\) has size at most \(m-2\); when exactly one occurs, the upper bound improves to \(2m-1\); and when both occur, it improves to \(2m-2\). Equality \(2m\) is attained with \(A=B=[m]\setminus\{h,k\}\).

For a cube vertex to a bridge, if the cube has a missing arm among the bridge's two arms, the distance is at most \(m\). Otherwise, the endpoint-minimization formula gives
\[
d(U_h(A),V_{\{i,j\}})=|A|+6-2\max\{\mathbf1_{i\in A},\mathbf1_{j\in A}\}\le m+3.
\]
The inequality follows by separating the cases where neither, one, or both of \(i,j\) belong to \(A\), noting that \(h\notin\{i,j\}\). Since \(m+3\le2m\) for \(m\ge3\), this creates no larger pair.

Two distinct bridges sharing an arm have distance at most four, by moving inside the corresponding cube between its two one-coordinate vertices. If the two pairs of arms are disjoint (possible only for \(m\ge4\)), there is a path of length eight through an intermediate bridge and two cubes. Since \(8\le2m\) for \(m\ge4\), this completes the global upper bound and the diameter proof.

## Verification

Two standalone programs are included. `check_spider_formula.py` builds independent sets directly from the original tree, derives every legal slide, performs breadth-first search between every pair for \(3\le m\le7\), and compares all distances, vertex counts and edge counts with the formulas. `check_spider_independent.cpp` independently builds the same state spaces using packed bitmasks, reconstructs moves from the tree edges, and checks all ordered pairs for \(3\le m\le9\). Both programs check the exact diameter. Example commands:

```sh
python3 check_spider_formula.py
g++ -std=c++17 -O2 check_spider_independent.cpp -o check_spider
./check_spider
```

The finite checks validate stated cases and independent implementations; they are not substituted for the all-order argument above.

## Relationship to prior work

Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees* (arXiv:1406.6576, first posted June 25, 2014), establish efficient reachability and polynomial-length reconfiguration sequences on trees. Hoang, Khorramian and Uehara, *Shortest Reconfiguration Sequence for Sliding Tokens on Spiders* (arXiv:1806.08291, first posted June 21, 2018), supply a shortest-sequence algorithm for arbitrary spiders, and thus **already solve the algorithmic shortest-path task for this family**. Neither is claimed to lack this general algorithmic capability. Avis and Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding* (arXiv:2203.16861, first posted March 31, 2022), study structural and realizability properties of token-sliding graphs.

The present statement instead explicitly identifies every vertex and edge of this particular full \((m-1)\)-token state graph, its cubical bridge architecture, a closed pair-distance law and its sharp global diameter with a two-vertex-difference extremal pair. The inspected texts do not state this simultaneous family classification; an equivalent unindexed description remains possible. A generic shortest-path algorithm does not itself state the graph isomorphism, counts, or global diameter.

## Limitations

The mathematical proof is an infinite-family proof for \(m\ge3\); no claim is made about other token counts, arbitrary spiders, or unlabeled token routings. Only the relevant accessible literature and indexed research records were checked; no global originality guarantee or independent scholarly audit is asserted. Reconfiguration states are distinct independent sets, not individual-token trajectories. Verification programs are bounded finite checks.

## References

1. E. D. Demaine et al., *Linear-Time Algorithm for Sliding Tokens on Trees*, arXiv:1406.6576 (first version 2014-06-25), https://arxiv.org/abs/1406.6576.
2. D. A. Hoang, A. Khorramian, R. Uehara, *Shortest Reconfiguration Sequence for Sliding Tokens on Spiders*, arXiv:1806.08291 (first version 2018-06-21), https://arxiv.org/abs/1806.08291.
3. D. Avis and D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (first version 2022-03-31), https://arxiv.org/abs/2203.16861.
