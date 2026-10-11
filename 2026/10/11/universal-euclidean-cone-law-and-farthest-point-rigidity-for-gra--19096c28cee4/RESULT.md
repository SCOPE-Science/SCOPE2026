# Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes

## Finding

Let \(H\) be **any** finite simple graph on \(m\ge2\) labeled vertices; it need not be connected or bipartite. Let \(H^+=K_1\vee H\) be the graph obtained by adjoining one vertex adjacent to every vertex of \(H\). For any graph \(G\), put
\[
Z_G=\sum_{\{u,v\}\in E(G)}[e_u,e_v]\subset\mathbb R^{V(G)},
\qquad
D_2(G)=\max_{x,y\in Z_G}\|x-y\|_2.
\]
All distances use the ordinary ambient Euclidean metric, **not** shortest-path distance in the one-skeleton. Then the exact universal cone identity is
\[
\boxed{D_2(H^+)^2=D_2(H)^2+m(m+1).}
\]
The unique Euclidean circumcenter of \(Z_G\) is \(c_G=\frac12\sum_{v\in V(G)}\deg_G(v)e_v\), and its circumradius is \(D_2(G)/2\). Thus coning raises the **squared circumradius** by exactly \(m(m+1)/4\), independently of the edges of \(H\).

There is also a complete criterion for the farthest vertices. Choose an arbitrary fixed orientation to write each incidence vector as \(b_e=e_u-e_v\), and choose edge signs \(\varepsilon_e\in\{-1,1\}\). Put \(d=\sum_e\varepsilon_e b_e\) and, independently, choose spoke signs \(s_i\in\{-1,1\}\) with \(S=\{i:s_i=-1\}\). The corresponding centered endpoint of the cone zonotope, doubled, is \((d+s,-\sum_i s_i)\). It is a farthest vertex if and only if \(\|d\|_2^2=D_2(H)^2\) and **either** \(S=\varnothing\) or \(S=V(H)\), **or** the nontrivial cut \((S,V(H)\setminus S)\) is complete and every crossing edge contributes \(-1\) to \(\sum_{i\in S}d_i\). In the latter case, \(\partial_HS\) contains every possible cross edge and \(\sum_{i\in S}d_i=-|S|(m-|S|)\). There are no other farthest points.

For bipartite \(H\), let \(c\) be the number of connected components containing at least one edge (isolated vertices do not count). Then
\[
\boxed{D_2(H^+)^2=m(m+1)+\sum_{v\in V(H)}\deg_H(v)^2,}
\]
and the total number of farthest **vertices** of \(Z_{H^+}\) is exactly
\[
\boxed{2^{c+1}+2\,\mathbf 1_{\{H\cong K_{p,q}\text{ for some }p,q\ge1\}}.}
\]
The final indicator concerns the whole graph: an extra isolated vertex makes it zero. In particular, for a connected bipartite graph that is not complete bipartite, there are exactly four farthest vertices; for a complete bipartite graph there are six.

## Assumptions and scope

Graphs are finite, simple, loop-free, and have unit (unweighted) edges. The graph \(H\) may have isolated vertices and multiple connected components. Graphical zonotopes lie in affine hyperplanes; all Euclidean measurements are inherited from the displayed ambient space, with no affine rescaling or altered inner product. The diameter is the maximum ordinary distance between *any two points* of the polytope. Farthest vertices mean those on the smallest enclosing Euclidean ball, centered at \(c_G\).

## Proof

**Step 1 — central symmetry and signed endpoints.** Write
\[
Z_G-c_G=\tfrac12\sum_{e\in E(G)}[-b_e,b_e],
\qquad c_G=\tfrac12\sum_{\{u,v\}\in E(G)}(e_u+e_v).
\]
This zonotope is centrally symmetric. For any compact centrally symmetric convex set \(K=-K\), its diameter is \(2\max_{z\in K}\|z\|_2\), attained by antipodes, and its smallest enclosing ball is the ball centered at the symmetry center; the Euclidean circumcenter is unique. By convexity of the squared norm, its maximum over a Minkowski sum of line segments is attained at a signed endpoint. Therefore,
\[
D_2(G)^2=\max_{\varepsilon\in\{-1,1\}^{E(G)}}
\left\|\sum_{e\in E(G)}\varepsilon_e b_e\right\|_2^2.
\]
Strict convexity implies that all norm-maximizing *points* are zonotope vertices; the characterization in signed endpoints therefore characterizes all farthest vertices.

**Step 2 — exact cone norm identity.** Orient the spoke incidence vectors as \(e_i-e_a\), where \(a\) denotes the apex. Let \(d=\sum_{e\in E(H)}\varepsilon_e b_e\), so \(\sum_i d_i=0\), and let \(s=(s_i)\) be their signs. Define \(S=\{i:s_i=-1\}\) and \(k=|S|\). Direct expansion gives
\[
\begin{aligned}
\left\|\left(d+s,-\sum_i s_i\right)\right\|_2^2
&=\|d\|_2^2+m+(m-2k)^2+2\sum_i d_i s_i\\
&=\|d\|_2^2+m(m+1)-4k(m-k)-4\sum_{i\in S}d_i.
\end{aligned}
\]
Each edge entirely inside or outside \(S\) contributes zero to \(\sum_{i\in S}d_i\); each edge crossing the cut contributes either \(-1\) or \(+1\). Consequently
\[
-\sum_{i\in S}d_i\le |\partial_H S|\le k(m-k).
\]
It follows for every pair of sign choices that the cone norm square is at most \(D_2(H)^2+m(m+1)\). Taking any maximizing \(\varepsilon\) for \(H\) and taking every spoke sign equal to \(+1\) or every sign equal to \(-1\) makes both cut terms vanish, proving the **global equality** for every graph.

**Step 3 — complete equality criterion.** Every inequality in the preceding bound has a nonnegative defect. Equality therefore requires that \(\|d\|_2^2=D_2(H)^2\) and that either \(k=0\) or \(k=m\), or both cut inequalities are sharp. For \(0<k<m\), sharpness of the second inequality is exactly completeness of the cut; sharpness of the first is exactly the specified sign contribution on *every* cut edge. Conversely, those conditions visibly make all defects zero. By strict convexity of the Euclidean squared norm, every farthest point is a vertex, completing the classification.

**Step 4 — bipartite specialization and counting.** For a bipartite \(H\), any signed incidence sum satisfies \(|d_i|\le\deg_H(i)\); thus \(\|d\|_2^2\le\sum_i\deg_H(i)^2\). Orient every edge consistently from one bipartition class to the other within each nontrivial connected component to attain equality at every vertex. Equality at every non-isolated vertex forces all its incident edges to have the same local sign, which forces precisely two source/sink assignments per nontrivial connected component. Hence there are precisely \(2^c\) farthest points for \(H\) itself, and each has exactly two uniform-spoke lifts, giving \(2^{c+1}\) farthest vertices for the cone.

A nontrivial complete cut in a bipartite graph excludes edges internal to either shore: such an internal edge, together with any vertex on the other shore, would form a triangle. Hence a nontrivial complete cut is possible **only when** the entire graph is a complete bipartite graph \(K_{p,q}\). For that graph there are exactly two further configurations, one with each bipartition class as \(S\) and with crossing edge contributions all negative on \(S\). Their spoke sums distinguish them from the uniform lifts, and their leaf-coordinate vectors distinguish them from each other. This gives exactly two additional farthest vertices, as claimed.

## Verification

The standalone file `verify_cone.py` uses only the Python 3 standard library and exact integer arithmetic. Execute `python3 verify_cone.py`. It enumerates **all** simple labeled graphs on \(2,3,4,5\) vertices, plus six additional six-vertex instances, totaling **1,104 graphs**, of which **431 are bipartite**. For every graph it exhausts all signed endpoints of both the original and coned zonotopes, checks the squared-diameter identity, checks the complete-cut equality criterion as an exact equality of vertex sets, and checks the bipartite degree formula and farthest-vertex count. The calculations serve as independent finite consistency checks; the cut inequality in the proof establishes the theorem for every \(m\ge2\).

As a concrete non-multipartite example, the path \(H=P_m\) with \(m\ge4\) has \(\sum_i\deg_H(i)^2=4m-6\), so its fan-graph cone has \(D_2(H^+)^2=m^2+5m-6\) and exactly four farthest vertices. When \(m=3\), the path is complete bipartite, and the contact count is six.

## Relationship to prior work

The standard graphical zonotope and its acyclic-orientation description are classical. Padrol, Pilaud and Poullot study deformation cones, not Euclidean diameters. Chapoton and Pilaud prove that shuffling graphical zonotopes corresponds to graph joins and give vertex/facet enumerations; their shuffle-with-a-point is the precise operation considered here, but the paper's metric content does not include the stated square-additivity law or the farthest-vertex classification. Deza, Pournin and Sukegawa use *diameter* for the shortest-path diameter of a polytope's one-skeleton; their invariant is different.

Certain special cases (notably complete multipartite graphs and permutohedra) admit previously known circumradius evaluations. The present claim concerns every graph \(H\), with an exact effect of coning and an equality-cut characterization; it does **not** assert novelty for any single complete-multipartite instance. A prior derivation using support functions, optimal orientation imbalance, or zonotope shuffles remains possible.

## Limitations

The formula is for **unweighted, simple** graphical zonotopes in the standard Euclidean metric. It does not assert an analogous universal constant for arbitrary edge weights, other convex-body norms, the graph-theoretic one-skeleton diameter, or a general join of two non-singleton graphs. The bipartite farthest-point count does not claim such a closed count for non-bipartite graphs. Source searches and document inspections cannot establish absolute novelty, and no independent mathematical audit has been performed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first public version 2021-11-24. Sections 1.3 and 2. https://arxiv.org/abs/2111.12422
2. F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first public version 2022-01-18. Sections 1.4, 2.3, 2.4, Proposition 98, Appendix A.1. https://arxiv.org/abs/2201.06896
3. A. Deza, L. Pournin and N. Sukegawa, *The diameter of lattice zonotopes*, arXiv:1905.04750, first public version 2019-05-12. Sections 1–2 (one-skeleton diameter). https://arxiv.org/abs/1905.04750
