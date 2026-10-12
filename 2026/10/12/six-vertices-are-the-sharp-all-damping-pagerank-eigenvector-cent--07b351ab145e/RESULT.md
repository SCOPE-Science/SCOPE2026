# Six vertices are the sharp all-damping PageRank–eigenvector-centrality maximizer boundary
## Finding
Let \(G\) be a connected finite simple undirected graph with
\[
n\ge2.
\]

Adjacency-eigenvector centrality is the positive Perron eigenvector of the adjacency matrix \(A\).

Standard PageRank with uniform teleportation and follow-link damping
\[
\alpha\in(0,1)
\]
is the probability vector \(p\) satisfying
\[
p
=
\frac{1-\alpha}{n}\mathbf 1
+
\alpha P^{\mathsf T}p,
\]
where \(P\) is the simple-random-walk transition matrix.

For every connected graph with
\[
n\le5
\]
and every
\[
\alpha\in(0,1),
\]
if both centralities have unique maximizing vertices, those maximizers are the same vertex.

This is sharp at
\[
n=6.
\]

Take the graph with edge set
\[
\{01,02,03,34,35,45\}.
\]
Thus vertices \(3,4,5\) form a triangle, vertex \(0\) is attached to vertex \(3\), and vertices \(1,2\) are leaves attached to vertex \(0\).

Adjacency-eigenvector centrality has unique maximizing vertex
\[
3.
\]

PageRank has unique maximizing vertex
\[
0
\]
for every
\[
0<\alpha<1.
\]

The disagreement is therefore not tied to the conventional numerical choice of damping. It persists throughout the entire nontrivial damping interval.

## Assumptions and scope
Graphs are connected, finite, simple, and undirected.

PageRank uses uniform teleportation. The parameter \(\alpha\) is the probability of following a graph edge; equivalently, the random-jump probability is \(1-\alpha\).

The result compares only unique maximizing vertices. It does not classify all differences lower in the ranking, nor cases in which one or both centralities have a tied maximum.

Eigenvector centrality means the ordinary adjacency Perron vector, not Katz or alpha-centrality.

## Proof
For the six-vertex witness, symmetry gives equal eigenvector-centrality scores on vertices \(1,2\) and on vertices \(4,5\).

Let the Perron eigenvalue be \(\rho\), and let the scores on a leaf, vertex \(0\), vertex \(3\), and a nonattachment triangle vertex be \(s,u,v,t\), respectively.

The eigenvector equations give
\[
\rho s=u,
\]
\[
\rho u=2s+v,
\]
and
\[
(\rho-1)t=v.
\]

The graph contains a triangle as a proper connected substructure, so Perron–Frobenius monotonicity gives
\[
\rho>2.
\]

Eliminating \(s\) gives
\[
\frac vu
=
\rho-\frac2\rho.
\]
Because \(\rho>2\),
\[
\rho-\frac2\rho>1,
\]
so
\[
v>u.
\]
Also
\[
s=\frac u\rho<u
\]
and
\[
t=\frac v{\rho-1}<v.
\]
Hence vertex \(3\) is the unique eigenvector-centrality maximizer.

For PageRank, exact solution of
\[
\left(I-\alpha P^{\mathsf T}\right)p
=
\frac{1-\alpha}{6}\mathbf 1
\]
gives the symmetry relations
\[
p_1=p_2,
\qquad
p_4=p_5,
\]
and the differences
\[
p_0-p_1
=
\frac{2\alpha(\alpha^2+\alpha-3)}
{(\alpha+3)(4\alpha^2-\alpha-6)},
\]
\[
p_0-p_3
=
\frac{3\alpha(\alpha-1)}
{(\alpha+3)(4\alpha^2-\alpha-6)},
\]
and
\[
p_0-p_4
=
\frac{\alpha(4\alpha^2+3\alpha-9)}
{2(\alpha+3)(4\alpha^2-\alpha-6)}.
\]

On
\[
0<\alpha<1,
\]
the common quadratic denominator factor satisfies
\[
4\alpha^2-\alpha-6<0.
\]
The three numerator factors
\[
\alpha^2+\alpha-3,
\qquad
\alpha-1,
\qquad
4\alpha^2+3\alpha-9
\]
are also negative throughout this interval. Therefore
\[
p_0>p_1=p_2,
\qquad
p_0>p_3,
\qquad
p_0>p_4=p_5.
\]
Thus vertex \(0\) is the unique PageRank maximizer for every nontrivial damping value.

For sharpness below six vertices, every connected simple graph was generated from labeled edge subsets and quotient-reduced by all vertex permutations. The numbers of connected unlabeled graphs obtained for orders
\[
2,3,4,5
\]
were
\[
1,2,6,21.
\]

For each graph, every PageRank coordinate was solved exactly as a rational function of \(\alpha\). Since
\[
I-\alpha P^{\mathsf T}
\]
is invertible for
\[
0<\alpha<1,
\]
pairwise PageRank order can change only at a zero of a pairwise-difference numerator. All such real roots in the open unit interval were isolated exactly; one exact sample in every resulting interval and every root point itself were checked.

The eigenvector maximizer was compared exactly using principal cofactors of
\[
\rho I-A
\]
at the Perron root \(\rho\). For a connected graph these cofactors are proportional to the squared Perron-vector coordinates.

No graph through five vertices has a damping value at which PageRank and adjacency-eigenvector centrality possess distinct unique maximizers.

## Verification
The embedded `verify_pagerank_eigenvector_boundary.py` is a standalone exact checker using Python and SymPy.

It independently generates all connected graph isomorphism classes through five vertices and reproduces the counts
\[
1,2,6,21.
\]

For every such graph it computes PageRank coordinates as exact rational functions of \(\alpha\), isolates every real crossing point in
\[
(0,1),
\]
checks every open ranking interval and every crossing point, and compares the result with the exact Perron-vector maximizer.

For the six-vertex witness it verifies the adjacency characteristic polynomial
\[
x(x+1)(x^4-x^3-5x^2+3x+4),
\]
checks that the Perron root exceeds \(2\), verifies unique eigenvector maximizer \(3\), derives the displayed PageRank formulas, and certifies
\[
p_0>p_j
\]
for every \(j\ne0\) throughout the open damping interval.

Run:

`python3 verify_pagerank_eigenvector_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The original PageRank report introduced link-based recursive ranking and the random-surfer interpretation.

Perra and Fortunato later compared PageRank with eigenvector-based spectral centralities, extended PageRank explicitly to undirected graphs, and compared rankings produced by spectral measures. Their empirical comparisons show that different spectral centralities can produce substantially different rankings on real networks.

That broader disagreement is therefore prior context, not the new claim.

The present result asks a finite structural question that the checked literature did not answer: what is the smallest connected undirected graph on which ordinary adjacency-eigenvector centrality and uniformly teleported PageRank choose different unique top vertices, with the PageRank choice remaining different for every nontrivial damping parameter?

Targeted searches using both centrality names, smallest-graph language, unique-maximizer language, all-damping language, and the triangle-plus-two-leaf witness did not locate this six-vertex boundary.

## Limitations
The theorem concerns undirected unweighted graphs and uniform teleportation.

Directed networks or personalized teleportation can behave differently and may admit smaller conflicts.

The lower-order statement concerns unique top vertices only; it does not assert equality of complete rankings.

Perra and Fortunato's open full text was inspected directly. The original PageRank technical report's exact date and bibliographic identity were verified through public Stanford-hosted reproductions and bibliographic records, but the legacy primary report host itself was not retrievable in this run.

An unindexed exercise, software test, or small-network example could contain the witness without identifying the all-damping minimality theorem.

## References
1. L. Page, S. Brin, R. Motwani, and T. Winograd, “The PageRank Citation Ranking: Bringing Order to the Web,” Stanford Digital Library Technologies Project technical report, dated 29 January 1998; later catalogued as report 1999-66.
2. N. Perra and S. Fortunato, “Spectral centrality measures in complex networks,” arXiv:0805.3322, first posted 21 May 2008; *Physical Review E* 78, 036107, published 5 September 2008. DOI: 10.1103/PhysRevE.78.036107.
