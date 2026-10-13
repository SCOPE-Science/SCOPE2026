# Bondage edge-set enumerator of crown graphs
## Finding
For every integer \(n\ge3\), write the crown graph as
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
so \(a_i b_j\) is an edge exactly when \(i\ne j\). For an edge-deletion set \(F\subseteq E(\operatorname{Cr}_n)\), form a simple graph \(H_F\) on the index set \([n]\) by declaring \(ij\in E(H_F)\) when at least one of the two crown edges \(a_i b_j\) and \(a_j b_i\) belongs to \(F\).

Then
\[
\gamma(\operatorname{Cr}_n-F)>2
\quad\Longleftrightarrow\quad
H_F\text{ has no isolated vertex}.
\]
Therefore the complete enumerator of domination-disrupting edge sets is
\[
B_n(x)=\sum_{F:\,\gamma(\operatorname{Cr}_n-F)>2}x^{|F|}
=\sum_{j=0}^n(-1)^j\binom{n}{j}(1+x)^{(n-j)(n-j-1)}.
\]
In particular,
\[
b(\operatorname{Cr}_n)=\left\lceil\frac n2\right\rceil.
\]
The number of minimum bondage edge sets is
\[
2^{n/2}(n-1)!!=\frac{n!}{(n/2)!}
\]
for even \(n\), and
\[
2^{(n+1)/2}\,\frac{n(n-1)}2\,(n-2)!!
\]
for odd \(n\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The statement concerns \(n\ge3\). The bondage number \(b(G)\) is the least cardinality of an edge set \(F\) such that \(\gamma(G-F)>\gamma(G)\). The polynomial \(B_n(x)\) is defined here only as an enumerator of all edge-deletion sets that raise the domination number; no claim is made that this notation is standard in the literature.

## Proof
First, \(\gamma(\operatorname{Cr}_n)=2\), and its dominating two-sets are exactly
\[
D_i=\{a_i,b_i\},\qquad 1\le i\le n.
\]
Indeed, \(D_i\) dominates because \(a_i\) reaches every \(b_j\) with \(j\ne i\), while \(b_i\) reaches every \(a_j\) with \(j\ne i\). A pair contained in one bipartition class leaves every unchosen vertex of that class undominated. A cross-pair \(\{a_i,b_j\}\) with \(i\ne j\) leaves \(a_j\) (and symmetrically \(b_i\)) undominated. Thus no other two-set dominates.

Deleting edges cannot create a new dominating pair. Fix \(i\). In \(D_i\), every vertex \(b_j\) with \(j\ne i\) is dominated through the unique edge \(a_i b_j\), and every vertex \(a_j\) with \(j\ne i\) is dominated through the unique edge \(a_j b_i\). Hence \(D_i\) survives in \(\operatorname{Cr}_n-F\) exactly when \(F\) contains none of those edges. By the definition of \(H_F\), this is exactly the assertion that index \(i\) is isolated in \(H_F\). Therefore \(\gamma(\operatorname{Cr}_n-F)=2\) exactly when \(H_F\) has an isolated vertex, proving the equivalence.

For the polynomial, apply inclusion-exclusion to the events that specified indices are isolated in \(H_F\). If a fixed set of \(j\) indices is required to be isolated, every deleted crown edge must have both endpoint-indices among the remaining \(n-j\) indices. There are \((n-j)(n-j-1)\) such directed crown edges, and their weighted subset enumerator is \((1+x)^{(n-j)(n-j-1)}\). Inclusion-exclusion gives the displayed formula.

Each deleted crown edge can make at most two indices nonisolated in \(H_F\), so every disrupting set has size at least \(\lceil n/2\rceil\). Equality is attained by orienting the edges of a minimum edge cover of \(K_n\). For even \(n\), such a cover is a perfect matching, giving \(2^{n/2}(n-1)!!\) oriented lifts. For odd \(n\), a minimum edge cover consists of one three-vertex path and a matching on the other \(n-3\) vertices; the number of underlying covers is \(n(n-1)(n-2)!!/2\), and each of its \((n+1)/2\) edges has two orientations. This yields the stated count.

## Verification
The standalone checker `verify.py` reconstructs each crown graph directly. For \(3\le n\le5\) it first enumerates all dominating vertex pairs from adjacency, then exhausts every edge-deletion subset and compares direct survival of those pairs with the auxiliary no-isolated-vertex criterion. It also compares the complete coefficient vector against the inclusion-exclusion formula. The coefficient formula and the minimum-size multiplicity are additionally checked for \(3\le n\le12\). The recorded replay output is:

`VERIFY_OK n_exhaustive=3..5 subset_checks=1052736 pair_survival_checks=5218737 coefficient_checks=580 formula_range=3..12`

These finite checks support the proof but are not used as a substitute for the all-\(n\) argument above.

## Relationship to prior work
Fink, Jacobson, Kinch, and Roberts introduced the bondage number in 1990 and determined it for several standard graph classes. Xu's 2013 open survey gives the definition, records those standard exact families, and surveys bounds and special classes. A full-text search of that survey found no occurrence of “crown”; its occurrences of “perfect matching” concern complete graphs with a perfect matching removed, not the bipartite crown graph. The survey also emphasizes that exact bondage values depend strongly on the structure of minimum dominating sets.

The present statement is not the complete-multipartite formula: \(\operatorname{Cr}_n\) is obtained from \(K_{n,n}\) by deleting a perfect matching and is not complete multipartite for \(n\ge3\). The claim is also stronger than a scalar bondage-number evaluation: it identifies every edge-deletion set that raises domination and gives the full cardinality enumerator through an edge-cover correspondence on the index graph.

## Limitations
The proof concerns ordinary bondage under edge deletion only. It does not address vertex bondage, total bondage, Roman bondage, or other variants. The 1990 foundational paper was identified through bibliographic metadata and the later full survey, but its full text was not available through the lawful sources inspected in this run; this leaves a residual risk of an older equivalent formulation under nonstandard terminology. The fully searchable 2013 survey contained no crown-graph instance or equivalent bipartite-perfect-matching-deletion formula. The date used in metadata is the exact first-publication date verified for that survey; the older foundational paper is bibliographically dated 1990 without an exact public day in the inspected records.

## References
1. J. F. Fink, M. S. Jacobson, L. F. Kinch, and J. Roberts, “The bondage number of a graph,” *Discrete Mathematics* 86 (1990), 47–57. DOI: 10.1016/0012-365X(90)90348-L.
2. J.-M. Xu, “On Bondage Numbers of Graphs: A Survey with Some Comments,” *International Journal of Combinatorics* 2013, Article 595210. First published 13 May 2013. DOI: 10.1155/2013/595210.
3. “Upper bounds on the bondage number of a graph,” *Discussiones Mathematicae Graph Theory*, DOI: 10.7151/dmgt.1419. The article records 2000 Mathematics Subject Classification 05C69 for bondage-number work.
