# Sharp online neighborhood bounds for line graphs of girth-five graphs

## Finding

For every finite simple graph \(G\) of girth at least five (meaning it has no triangle or four-cycle; forests are included), form its line graph \(L(G)\). The ground set is \(E(G)\). For each unknown edge \(e\in E(G)\), define the Boolean hypothesis \(h_e\) by
\[
h_e(q)=\begin{cases}1,&e\ne q\text{ and }e\cap q\ne\varnothing,\\0,&\text{otherwise},\end{cases}\qquad q\in E(G).
\]
Thus this is precisely the open-neighborhood concept class \(\mathcal N(L(G))\), with deterministic realizable point queries. Let \(v\) and \(\ell\) denote its VC and Littlestone dimensions, respectively. Then, for **all** such graphs, including graphs with isolated vertices or no edges,
\[
\boxed{v\le\ell\le\min\{3,v+1\}.}
\]
If the maximum degree of \(G\) is at most three, then \(\ell\le2\). Both sharpness boundaries hold already for trees: a five-vertex path has \((v,\ell)=(1,2)\), while the nine-vertex tree with edge list
\[
(0,1),(0,6),(1,2),(2,3),(2,4),(2,5),(6,7),(7,8)
\]
has \((v,\ell)=(2,3)\) and maximum degree four. No tree on fewer than nine vertices can have \(\ell=3\). In particular, degree four is the smallest possible maximum degree for a girth-at-least-five graph with \(\ell=3\).

## Assumptions and scope

All graphs are finite, undirected, simple and of girth at least five; acyclic graphs have infinite girth. An edge is identified with its unordered pair of endpoints. A complete depth-\(d\) Littlestone tree assigns a query to each internal node and admits, for every length-\(d\) answer string, a hypothesis realizing the answers along that path. VC dimension uses a fixed query set and all its Boolean patterns. Dimensions of the empty class and classes containing only a single distinct Boolean function are taken to be zero. Duplicate edge-indexed functions, where present, are identified; counting edges always gives a valid upper bound on the number of distinct functions.

## Proof

**Lemma 1: Two positive answers leave online depth at most one.** Take two distinct queried edges \(f\) and \(g\) for which both answers are one. If \(f\) and \(g\) are disjoint, any consistent center edge must join an endpoint of \(f\) to an endpoint of \(g\). At most one such joining edge exists: two of them create a triangle when sharing an endpoint (together with \(f\) or \(g\)), or a four-cycle if their endpoints are distinct. Thus at most one center remains. If \(f\) and \(g\) meet at vertex \(w\), every center adjacent to both is an edge through \(w\) other than \(f\) or \(g\). Any extra center avoiding \(w\) would join their other endpoints and create a triangle. Among the remaining star edges, an additional query through \(w\) labels all centers one except possibly itself; a query avoiding \(w\) labels at most one center one, because an edge between two neighbors of \(w\) would create a triangle. Hence no query has both branches containing at least two distinct remaining functions. The residual Littlestone dimension is at most one. A complete depth-four tree would contain a first-two-answers-\(11\) branch of depth two, contradicting the lemma. Therefore \(\ell\le3\).

**Lemma 2: Maximum degree three excludes depth three.** Fix an initial positive edge query \(f=uv\). Its candidate centers are the disjoint sets \(U\) of other edges through \(u\) and \(V\) of other edges through \(v\). For a subsequent query \(q\) meeting \(u\) but not equal to \(f\), the only positive centers are \(U\setminus\{q\}\): a center from \(V\) meeting \(q\) away from \(u\) would make a triangle. Similarly for a query through \(v\). If \(q\) meets neither \(u\) nor \(v\), it has at most one positive center in \(U\cup V\): two incidences would force either a triangle or a four-cycle containing \(f\). The query \(q=f\) cannot split the positive family. When \(\Delta(G)\le3\), both stars have at most two centers, so every query on this positive branch has a side containing at most one center. Therefore the positive branch has dimension at most one, which excludes a depth-three tree. Thus \(\ell\le2\).

**Lemma 3: Depth three forces VC dimension at least two.** If \(\ell=3\), some root query \(f=uv\) has a positive branch of Littlestone dimension at least two. A query in that branch must split its remaining hypotheses into two sides with at least two distinct functions each. By the preceding case analysis, such a query must pass through one endpoint, say \(u\), and there must be at least three other edges through \(u\) and at least one other edge through \(v\): \(\deg(u)\ge4\), \(\deg(v)\ge2\). Choose two distinct edges \(a,b\) at \(u\) different from \(f\). On the two fixed queries \(a,b\), the hypotheses centered at \(a,b,f\), and at an edge \(c\) through \(v\) other than \(f\), respectively, give the patterns \(01,10,11,00\). The final \(00\) holds because a connection from \(c\) to the non-\(u\) endpoint of \(a\) or \(b\) would create a triangle with \(f\). So \(v\ge2\). If \(\ell\) is zero, one or two, then \(v\ge\ell-1\) follows from \(v\ge0\) and, when \(\ell\ge1\), the fact that a depth-one shattered tree supplies a shattered single query. This proves \(\ell\le v+1\). The standard inequality \(v\le\ell\) holds because the same fixed shattered queries can be used at every level of an adaptive tree.

**Sharpness and minimal tree order.** Enumerate the eight edges of the displayed tree in the order written. A complete depth-three decision tree is given in `tree_certificate.json`; `verify_edge_neighborhood.py` verifies all eight root-to-leaf Boolean histories. Hence its \(\ell\ge3\), and Lemma 1 gives equality. The two fixed queries indexed \(3,4\) are shattered: the centers indexed \(3,4,2,0\) realize \(01,10,11,00\). Of the eight possible edge queries, the numbers of positive hypothesis centers are \(2,2,4,3,3,3,2,1\). Since three shattered coordinates among exactly eight hypothesis centers would have to be positive on exactly four centers each, while only one query has four positives, VC dimension is at most two. Thus \(v=2\). For the five-vertex path, the supplied checker verifies \(v=1\) and \(\ell=2\); this realizes the one-unit gap even at maximum degree two. Finally a depth-three tree has at least four distinct centers on each side of its root query, requiring at least eight edge hypotheses. Every tree on at most eight vertices has at most seven edges. Therefore the nine-vertex example has the minimum possible order among trees with \(\ell=3\), and by Lemma 2 its maximum degree four is optimal.

## Verification

From this package directory run `python3 verify_edge_neighborhood.py`. The script uses only the Python standard library; it reads the included `tree_certificate.json`. It checks tree connectivity and acyclicity, exact eight-center Boolean incidence rows, all paths of the explicit depth-three tree, exhaustive finite VC and Littlestone recurrences for the nine-vertex example and the five-vertex path, and the degree-profile obstruction to three-query shattering. The exact expected stdout is included as `verification_output.txt` and was reproduced by execution of the packaged source. The infinite-family bounds are proved by Lemmas 1–3; finite replay alone is not claimed to establish them.

## Relationship to prior work

Adler, Benediktsson and Macpherson (2020) study the same open-neighborhood Boolean relation on Johnson graphs, including the triangular graph \(J(n,2)=L(K_n)\), and prove VC dimension and density bounds. Any line graph \(L(G)\) embeds as the induced subgraph on the selected edges of a triangular graph. That broader-universe inclusion alone does not imply the stronger bound \(\ell\le3\) for girth-five graphs, the degree-three depth-two boundary, the one-unit VC–Littlestone gap, or the smallest sharp tree. An ambient complete-line-graph estimate, even if as small as four, would be strictly weaker and could not determine the girth-sensitive bounds or sharpness witnesses.

Bergold, Hochstättler and Mayer (2020/2022) study common-neighborhood set enumeration and neighborhood polynomials for chordal graphs, including classes containing line graphs of trees. Their neighborhood polynomial counts sets admitting a common neighbor; it does not give the adversarial alternating-branch Littlestone dimension or the present degree threshold. The graph family here also includes line graphs of graphs with long cycles, which need not be chordal. Different invariants and quantifier requirements prevent either cited paper's statements from implying the claim.

## Limitations

The girth condition is essential to the **proof**, not established as a necessary condition for the inequalities. Nothing is asserted about all line graphs containing triangles or squares, about closed neighborhoods, about weighted/randomized/agnostic learning, or about exact dimensions of each individual girth-five graph. The exact nine-vertex witness is a finite certificate; the all-graph assertions depend on the explicitly proved local incidence lemmas. Novelty assessments are restricted to the cited full-text portions and accessible search records; unidentified equivalent results may exist. No independent scientific audit has been performed.

## References

1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first public 2020-07-31. https://arxiv.org/abs/2007.16042
2. H. Bergold, W. Hochstättler and U. Mayer, *The Neighborhood Polynomial of Chordal Graphs*, arXiv:2008.08349, first public 2020-08-19; *Discrete Mathematics & Theoretical Computer Science* 24:1 (2022). https://arxiv.org/abs/2008.08349
