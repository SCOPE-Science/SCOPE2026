# Connected graphs with total burning number two
## Finding
Let \(G\) be a connected finite simple graph on \(n\ge 2\) vertices, let \(T(G)\) be its total graph, and write \(b_T(G)=b(T(G))\). Then
\[
b_T(G)=2
\]
if and only if \(G\cong K_{1,n-1}\), or, for \(n\ge 3\), \(G\) is obtained from \(K_{1,n-1}\) by adding exactly one edge joining two leaves.

Consequently, among connected graphs with \(b(G)=2\), these are exactly the graphs for which \(b_T(G)=b(G)\). Every other connected graph with \(b(G)=2\) satisfies \(b_T(G)=3\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph \(G\) is connected and has \(n\ge 2\) vertices. Graph burning is the standard discrete-time process in which one new source may be ignited in each round and fire spreads one graph edge per round. The total graph \(T(G)\) has one vertex for each vertex and each edge of \(G\); two vertices of \(T(G)\) are adjacent exactly when the corresponding objects of \(G\) are adjacent or incident.

The case \(n=1\) is excluded because then \(T(G)\) has one vertex and \(b_T(G)=1\).

## Proof
We first use a two-round criterion valid for every graph \(H\) with at least two vertices:
\[
b(H)=2
\quad\Longleftrightarrow\quad
\text{some }x\in V(H)\text{ has at most one nonneighbor.}
\]
Indeed, a two-round burning sequence covers
\[
V(H)=N_H[x_1]\cup\{x_2\},
\]
so every vertex except possibly \(x_2\) lies in \(N_H[x_1]\). Conversely, if \(x\) has at most one nonneighbor, ignite \(x\) first and, if needed, ignite the unique nonneighbor second. Since \(|V(H)|\ge2\), one round cannot finish the process.

Apply the criterion to \(H=T(G)\).

First suppose the initial source \(x\) is the vertex-node corresponding to \(v\in V(G)\). Put \(d=d_G(v)\) and \(m=|E(G)|\). The nonneighbors of \(v\) in \(T(G)\) are exactly:
\[
n-1-d
\]
vertex-nodes corresponding to nonneighbors of \(v\) in \(G\), together with
\[
m-d
\]
edge-nodes corresponding to edges of \(G\) not incident with \(v\). Hence
\[
(n-1-d)+(m-d)\le1.
\]
Write \(r=n-1-d\) and \(s=m-d\). If \(r=1\) and \(s=0\), let \(u\) be the unique vertex not adjacent to \(v\). Connectivity forces \(u\) to be incident with an edge, but that edge cannot be incident with \(v\) because \(uv\notin E(G)\), contradicting \(s=0\). Therefore \(r=0\): the vertex \(v\) is universal in \(G\). The inequality now gives \(s\le1\). Thus all edges of \(G\), apart from at most one, are incident with \(v\). Since \(v\) is adjacent to every other vertex, \(G\) is the star \(K_{1,n-1}\), with the only possible additional edge joining two leaves.

Now suppose the initial source \(x\) is the edge-node corresponding to \(e=uv\in E(G)\). Among the vertex-nodes of \(T(G)\), the node \(e\) is adjacent only to \(u\) and \(v\), so it has at least \(n-2\) nonneighbors. The two-round criterion therefore forces \(n\le3\). The connected graphs on two or three vertices are \(K_2\), \(P_3\), and \(K_3\), all of which belong to the two families already listed.

It remains to verify sufficiency. If \(G=K_{1,n-1}\) with center \(v\), then the vertex-node \(v\) is universal in \(T(G)\), so \(b_T(G)=2\). If \(G\) is a star plus one edge between two leaves, then the center vertex-node has exactly one nonneighbor in \(T(G)\), namely the edge-node corresponding to the added leaf-edge. The two-round criterion again gives \(b_T(G)=2\).

Finally, for a connected graph with \(b(G)=2\), the known bound
\[
b(G)\le b_T(G)\le b(G)+1
\]
gives \(2\le b_T(G)\le3\). The classification above determines exactly when the lower value occurs, proving the stated consequence.

## Verification
The proof is self-contained and reduces the classification to the exact two-round neighborhood criterion. The two source types in \(T(G)\)—vertex-nodes and edge-nodes—are exhausted separately, and the boundary cases \(n=2\) and \(n=3\) are included explicitly.

As an auxiliary finite stress test, every connected isomorphism type in the standard Graph Atlas through seven vertices was checked by constructing its total graph and applying the two-round criterion. The only types with total burning number two were the star and the star with one added leaf-edge. This finite check is not used as a proof.

## Relationship to prior work
Moghbel introduced total burning and formulated the general problem of characterizing graphs with prescribed total burning number. Antony, Chandran, Das, Gosavi, Jacob, and Kulamarva proved for connected graphs that
\[
b(G)\le b_T(G)\le b(G)+1
\]
and identified equality questions among ordinary, edge, and total burning parameters as a direction for further study. The result above supplies a complete answer for the first nontrivial total-burning value and, equivalently, resolves the equality split inside the layer \(b(G)=2\).

A 2025 article by Komala and Mary uses the related phrase “total graph source vertex” and reports a different value for stars. Under the standard parameter \(b_T(G)=b(T(G))\) used here and in the cited total-burning literature, the center vertex-node of a star is universal in \(T(G)\), which directly yields \(b_T(G)=2\). The 2025 statement is therefore not statement-equivalent to the parameter evaluated here.

## Limitations
The classification concerns only the layer \(b_T(G)=2\), together with its immediate consequence for graphs satisfying \(b(G)=2\). It does not classify \(b_T(G)=k\) for \(k\ge3\), nor does it characterize equality \(b_T(G)=b(G)\) for larger burning number.

Targeted searches found no earlier statement equivalent to the classification, but absence from searched indexes is not a proof of novelty. The terminology mismatch with the 2025 source is recorded as a residual literature-comparison risk.

## References
1. Daniel Moghbel, *Topics in Graph Burning and Datalog*, PhD dissertation, Ryerson University, 2020. Repository record DOI: 10.32920/19775380.
2. Dhanyamol Antony, L. Sunil Chandran, Anita Das, Shirish Gosavi, Dalu Jacob, and Shashanka Kulamarva, *Graph Burning: Bounds and Hardness*, arXiv:2402.18984, first submitted 29 February 2024.
3. Komala S. and Mary U., article on total source-vertex numbers in *Indian Journal of Natural Sciences*, Vol. 16, Issue 89, April 2025, pp. 91649–91650.
