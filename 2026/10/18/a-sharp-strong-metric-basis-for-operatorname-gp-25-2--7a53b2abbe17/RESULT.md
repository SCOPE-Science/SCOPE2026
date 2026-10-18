# A sharp strong metric basis for \(\operatorname{GP}(25,2)\)

## Finding

The generalized Petersen graph \(G=\operatorname{GP}(25,2)\) has strong metric dimension
\[
\boxed{\operatorname{sdim}(G)=34.}
\]
This is one less than \(5k+5=35\) for \(k=6\) in the prediction for \(\operatorname{GP}(4k+1,2)\) stated as an open problem in Kratica–Kovačević-Vujčić–Čangalović's 2015 preprint and as an experimental hypothesis in the 2017 journal version. The published upper bound \(\operatorname{sdim}\leq35\) remains valid.

## Assumptions and scope

Indices are taken modulo \(25\). The undirected simple graph \(G\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/25\mathbb Z\) and the 75 edges
\[
\{u_i,u_{i+1}\},\qquad\{u_i,v_i\},\qquad\{v_i,v_{i+2}\}
\quad(i\in\mathbb Z/25\mathbb Z).
\]
For a graph with shortest-path distance \(d\), a vertex \(s\) *strongly resolves* distinct vertices \(x,y\) if
\[
d(s,x)=d(s,y)+d(x,y)\quad\text{or}\quad
d(s,y)=d(s,x)+d(x,y).
\]
A strong resolving set satisfies this for every unordered pair of distinct vertices; the strong metric dimension is its minimum cardinality. Only this 50-vertex graph and this invariant are covered by the theorem.

## Proof

**1. The strong resolving graph and vertex covers.** Call a pair \(a,b\) *mutually maximally distant* (MMD) if, for each neighbor \(a'\) of \(a\) and each neighbor \(b'\) of \(b\),
\[
d(a',b)\leq d(a,b),\qquad d(a,b')\leq d(a,b).
\]
Let \(R\) be the graph on the vertices of \(G\) whose edges are precisely these pairs. A strong resolving set is exactly a vertex cover of \(R\): an MMD pair cannot be strongly resolved by a third vertex, since a geodesic extending beyond either endpoint would contradict maximal distance. Conversely, a shortest path between any \(x,y\) may be extended, in the finite graph, to an inclusion-maximal geodesic with MMD endpoints \(a,b\). Any cover of \(R\) contains \(a\) or \(b\), which strongly resolves \(x,y\) along that geodesic. Therefore
\[
\operatorname{sdim}(G)=\tau(R)=50-\alpha(R).
\]
This is the standard strong-resolving-graph reduction, included here with its argument.

**2. Exact distance table and MMD graph.** By simultaneous cyclic rotation and reflection, graph distances depend only on vertex types and the circular index separation \(j=\min\{i,25-i\}\in\{0,\ldots,12\}\). Directly from the three kinds of edges, the complete distance data are

| \(j\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(d(u_0,u_j)\) | 0 | 1 | 2 | 3 | 4 | 5 | 5 | 6 | 6 | 7 | 7 | 8 | 8 |
| \(d(u_0,v_j)\) | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 7 | 7 |
| \(d(v_0,v_j)\) | 0 | 3 | 1 | 4 | 2 | 5 | 3 | 6 | 4 | 7 | 5 | 7 | 6 |

The table is a finite, exactly reproducible computation: distances from each starting vertex are obtained by ordinary breadth-first search on the displayed edge set; the second verifier independently uses Floyd–Warshall. Alternatively, each table row can be certified by checking the edge-wise one-Lipschitz inequalities, a zero at the target, and a neighbor of value one less at every other vertex. These local checks force equality with shortest-path distance.

Substituting the table into the displayed MMD inequalities gives all edges of \(R\):
\[
\begin{aligned}
 u_i u_{i+j}\in E(R)&\iff j\bmod25\in\{\pm5,\pm7,\pm9,\pm11,\pm12\},\\
 v_i v_{i+j}\in E(R)&\iff j\bmod25\in\{\pm9,\pm11\},\\
 u_i v_j&\notin E(R)\quad\text{for all }i,j.
\end{aligned}
\]
Consequently \(R\) is a disjoint union of two explicit 25-vertex circulant graphs, with 125 outer edges and 50 inner edges.

**3. Outer independence number is six.** Fix any nonempty independent set of the outer component and rotate indices so that it contains \(u_0\). Its other indices must lie in
\[
A=\{1,2,3,4,6,8,10,15,17,19,21,22,23,24\}.
\]
These 14 vertices partition into five cliques (parenthesized groups)
\[
(2,15,22),\quad(4,17,24),\quad(1,6,19),\quad(3,8,21),\quad(10,23).
\]
Every pair within each group has circular separation in \(\{5,7,9,11,12\}\). At most one element can be chosen from each, so the independent set has at most \(1+5=6\) vertices. The set
\[
I_u=\{u_0,u_2,u_4,u_6,u_8,u_{10}\}
\]
is independent and has six vertices, proving \(\alpha(R_u)=6\).

**4. Inner independence number is ten.** Partition the 25 inner indices into the following five vertex-disjoint five-cycles, written in their cyclic adjacency order:
\[
(t,t+9,t+18,t+2,t+11)\pmod{25},\qquad t\in\{0,5,10,15,20\}.
\]
Successive differences, including the closing difference, are \(\pm9\) or \(\pm11\) modulo \(25\); hence these really are five-cycles in \(R_v\). The five cycles partition all indices: the five residues of the first cycle modulo five are distinct, and its four translates by five partition their respective residue classes. An independent set meets each five-cycle at most twice, so \(\alpha(R_v)\leq10\). The following ten indices give equality:
\[
I_v=\{v_0,v_2,v_5,v_7,v_{10},v_{12},v_{15},v_{17},v_{20},v_{22}\}.
\]
No two of these differ by \(\pm9\) or \(\pm11\). Thus \(\alpha(R_v)=10\).

**5. Exact conclusion and explicit basis.** Since there are no outer–inner edges of \(R\),
\[
\alpha(R)=\alpha(R_u)+\alpha(R_v)=6+10=16,
\qquad \operatorname{sdim}(G)=50-16=34.
\]
In particular, a minimum strong resolving set is the complement of \(I_u\cup I_v\) among the 50 vertices. This is an explicit 34-vertex counterexample to the proposed value \(35\), and the clique and odd-cycle covers prove that no 33-vertex strong resolving set exists. No optimization solver or extrapolation is needed for the lower bound.

## Verification

The standalone Python 3 programs `verify_bfs.py` and `verify_floyd.py` use only the standard library, construct \(G\) from its edges, and do not read each other's results. Run

```
python3 verify_bfs.py > bfs_output.json
python3 verify_floyd.py > floyd_output.json
```

The first program performs 50 breadth-first searches, constructs all 175 MMD pairs, checks both independent witnesses and directly checks all \(\binom{50}{2}=1225\) vertex pairs for strong resolution by the 34-vertex basis. The second calculates all-pairs distances by Floyd–Warshall, reconstructs the MMD graph, verifies the five outer cliques and five inner odd cycles as exact independence upper-bound certificates, and verifies both independent witnesses. Outputs `bfs_output.json` and `floyd_output.json` are included and deterministic.

## Relationship to prior work

Kratica, Kovačević-Vujčić and Čangalović, arXiv:1507.00881v1 (publicly submitted 2015-07-03), prove the upper bound \(\operatorname{sdim}(\operatorname{GP}(4k+1,2))\leq5k+5\) and explicitly state the conjectured equality for \(k\ge5\) as Open Problem 1. Their 2017 journal paper retains the same bound and gives the equality as an experimental hypothesis. Their exact computational table ends at \(n\le19\); neither edition determines the case \(n=25\). The reduction of strong metric dimension to vertex cover of the strong resolving graph is established background, not a novelty claim. The new contribution is the exact exceptional value and its small structural optimality certificate.

## Limitations

The result settles only \(\operatorname{GP}(25,2)\), not the full \(n\equiv1\pmod4\) family, and does not supply a replacement infinite-family formula. The distance table and clique/cycle certificates are finite and exactly reproducible; their statements should not be extrapolated to other parameters. A search of accessible literature and mathematical records did not identify a later published exact evaluation covering this instance, but unindexed work remains possible.

## References

1. J. Kratica, V. Kovačević-Vujčić, and M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, arXiv:1507.00881v1, 2015-07-03. https://arxiv.org/html/1507.00881v1
2. J. Kratica, V. Kovačević-Vujčić, and M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, *Applicable Analysis and Discrete Mathematics* 11 (2017), 1–10, DOI:10.2298/AADM161110032K. https://doiserbia.nb.rs/img/doi/1452-8630/2017/1452-86301600032K.pdf
3. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, *Discrete Applied Mathematics* 155 (2007), 356–364.
