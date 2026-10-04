# Bipartiteness exactly characterizes numerical index one for finite graph metrics
## Finding
Let \(G=(V,E)\) be a finite connected simple graph with \(|V|\ge 2\). Give \(V\) the shortest-path metric in which every edge has length \(1\), choose an arbitrary base vertex, and form the real Lipschitz-free space \(X=\mathcal F(V)\). Then
\[
n(X)=1 \quad\Longleftrightarrow\quad G\text{ is bipartite}.
\]
Equivalently, among finite unit-edge graph metrics, bipartiteness is exactly the graph-theoretic condition for the associated real Lipschitz-free space to have maximal numerical index.

## Assumptions and scope
All Banach spaces and functionals are real. The graph is finite, connected, simple, and unweighted; its metric is the unit-edge shortest-path metric. The numerical index is
\[
n(X)=\inf\{v(T):T\in\mathcal L(X),\ \|T\|=1\},
\]
where
\[
v(T)=\sup\{|x^*(Tx)|:x\in S_X,\ x^*\in S_{X^*},\ x^*(x)=1\}.
\]
For distinct vertices \(u,v\), write
\[
m_{uv}=\frac{\delta_u-\delta_v}{d(u,v)}.
\]
For \(f\in\operatorname{Lip}_0(V)\), an edge \(uv\in E\) is called tight for \(f\) when \(|f(u)-f(v)|=1\). The spanning subgraph formed by the tight edges is denoted \(H_f\).

The theorem does not determine the numerical index of a nonbipartite graph; it only gives the exact threshold criterion for the value \(1\).

## Proof
Because \(V\) is finite, every extreme point of \(B_X\) is an elementary molecule. For a graph metric, the metric segment between distinct vertices \(u,v\) contains only \(u,v\) exactly when \(uv\in E\): an edge has no third point on a path of length \(1\), whereas a nonedge has an interior vertex on every chosen shortest path. Hence
\[
\operatorname{ext} B_X=\{m_{uv}:uv\in E\text{ with an orientation}\}.
\]

We next characterize the dual vertices. Since edge inequalities generate all shortest-path inequalities,
\[
B_{X^*}=\left\{f:V\to\mathbb R:f(o)=0,\ |f(u)-f(v)|\le1\text{ for every }uv\in E\right\}.
\]
We claim that
\[
f\in\operatorname{ext}B_{X^*}\quad\Longleftrightarrow\quad H_f\text{ is connected}.
\]
If \(H_f\) is connected and \(f=(g+h)/2\) with \(g,h\in B_{X^*}\), then on every tight edge the two numbers \(g(u)-g(v)\) and \(h(u)-h(v)\), each lying in \([-1,1]\), average to \(1\) or \(-1\). They therefore coincide with that endpoint value. Thus \(g-h\) is constant along every tight edge. Connectedness of \(H_f\), together with \(g(o)=h(o)=0\), yields \(g=h=f\).

Conversely, suppose \(H_f\) is disconnected. Pick a component \(C\) not containing the base vertex. Every graph edge crossing from \(C\) to its complement is nontight, and there are finitely many such edges, so their positive slacks
\[
1-|f(u)-f(v)|
\]
have a positive minimum. For sufficiently small \(\varepsilon>0\), adding \(\varepsilon\) on \(C\) and leaving the other components unchanged, or subtracting the same quantity, preserves all edge inequalities. These give two distinct points of \(B_{X^*}\) whose midpoint is \(f\), so \(f\) is not extreme. This proves the claim.

Assume first that \(G\) is bipartite and let \(f\in\operatorname{ext}B_{X^*}\). For any graph edge \(uv\), choose a path from \(u\) to \(v\) inside the connected graph \(H_f\). Every edge of that path changes the value of \(f\) by \(1\) or \(-1\). Since \(u\) and \(v\) lie in opposite bipartition classes, every \(u\)-to-\(v\) path has odd length. Therefore \(f(u)-f(v)\) is an odd integer. The original edge inequality gives \(|f(u)-f(v)|\le1\), and hence
\[
|f(u)-f(v)|=1.
\]
Thus every dual extreme point has modulus-one pairing with every primal extreme point:
\[
|f(m_{uv})|=1 \qquad (uv\in E).
\]
McGregor's finite-dimensional criterion now yields \(n(X)=1\).

Assume next that \(G\) is nonbipartite. Choose a spanning tree \(T\) rooted at the base vertex \(o\), and define the parity potential
\[
f(v)=d_T(o,v)\pmod 2,
\]
with values in \(\{0,1\}\). Every graph edge changes \(f\) by at most \(1\), so \(f\in B_{X^*}\), while every tree edge is tight. Hence \(H_f\) contains the spanning tree \(T\) and is connected, so \(f\) is an extreme point of \(B_{X^*}\). If every graph edge joined vertices of opposite tree parity, those parity classes would be a bipartition of \(G\). Since \(G\) is nonbipartite, some graph edge \(uv\) joins vertices of the same parity. For that edge,
\[
f(m_{uv})=f(u)-f(v)=0.
\]
The molecule \(m_{uv}\) is a primal extreme point, so McGregor's criterion excludes \(n(X)=1\). Therefore \(n(X)<1\), completing the equivalence.

## Verification
The proof was reconstructed directly from the graph metric, the dual edge-inequality polytope, and McGregor's finite-dimensional criterion. The key new finite-dimensional lemma—dual extremality is equivalent to connectedness of the tight-edge subgraph—was checked in both directions, including the positive-slack perturbation needed for the converse.

A standalone exact checker exhaustively enumerates all connected labeled simple graphs on \(2\) through \(5\) vertices. For every integer-valued 1-Lipschitz potential in the necessary finite range, it tests dual extremality by tight-edge connectedness and verifies that every dual extreme potential saturates every graph edge exactly when the graph is bipartite. Its output is:

`VERIFY_OK connected_labeled_graphs=771 extreme_dual_vertices=16716 n=2..5`

This finite enumeration is corroborative only. The theorem for arbitrary finite order is established by the symbolic proof above.

## Relationship to prior work
Cobollo, Guirao, and Montesinos initiated the systematic computation of the numerical index of Lipschitz-free spaces with the two-dimensional case. Their theorem covers three-point metric spaces and shows that numerical index \(1\) occurs exactly in the metrically aligned case. For connected three-vertex unit-edge graph metrics, that is precisely the path-versus-triangle bipartite dichotomy. Their paper does not state a finite-graph characterization in arbitrary dimension.

The extreme-molecule input is standard in the finite metric setting and is also recorded in the literature on extremal structure of Lipschitz-free spaces: a molecule is extreme exactly when its metric segment has no third point. McGregor's classical finite-dimensional criterion characterizes numerical index \(1\) by modulus-one pairings between all primal and dual extreme points. The present result combines these ingredients with the new graph-specific description of dual extreme Lipschitz potentials by connected tight-edge subgraphs.

A targeted comparison also considered graph-associated CL-spaces with unconditional bases. Those results concern a different graph-to-Banach-space construction and do not identify general Lipschitz-free graph spaces with that class. No inspected source states the bipartiteness equivalence above.

## Limitations
The result is restricted to finite connected simple unweighted graph metrics and real scalars. It does not compute \(n(\mathcal F(V))\) when \(G\) is nonbipartite. Weighted graphs require a different parity argument because tight increments need not be integral. The exhaustive checker covers only graphs through five vertices and is not used as an infinite-family proof.

There remains a bibliographic risk that an equivalent criterion has appeared under Arens--Eells, transportation-cost, CL-space, or polyhedral terminology not captured by the targeted searches. The inspected sources did not reveal such coverage.

## References
1. C. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, first public 2023-04-25; later J. Math. Anal. Appl. 538 (2024), 128333.
2. C. M. McGregor, *Finite-Dimensional Normed Linear Spaces with Numerical Index 1*, J. London Math. Soc. (2) 3 (1971), 717--721, DOI 10.1112/jlms/s2-3.4.717.
3. L. García-Lirola, C. Petitjean, A. Procházka, A. Rueda Zoca, *Extremal Structure and Duality of Lipschitz Free Spaces*, arXiv:1707.09307; Mediterr. J. Math. 15 (2018), 69, DOI 10.1007/s00009-018-1113-0.
4. S. Reisner, *Certain Banach Spaces Associated with Graphs and CL-Spaces with 1-Unconditional Bases*, J. London Math. Soc. (2) 43 (1991), 137--148, DOI 10.1112/jlms/s2-43.1.137.
