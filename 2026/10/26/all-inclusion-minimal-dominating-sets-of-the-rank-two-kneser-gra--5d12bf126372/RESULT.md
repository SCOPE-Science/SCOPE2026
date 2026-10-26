# All inclusion-minimal dominating sets of the rank-two Kneser graphs

## Finding
For every integer \(n\ge5\), let \(KG(n,2)\) have vertex set \(\binom{[n]}2\), with two distinct vertices adjacent precisely when the represented pairs are disjoint. A set \(D\) dominates if every vertex outside \(D\) is adjacent to some member of \(D\); it is *inclusion-minimal* if deleting any one member destroys domination. Interpret \(D\) as the edge set of a simple graph \(H_D\) on \([n]\), allowing isolated vertices.

**Theorem.** Every inclusion-minimal dominating set is exactly one of the following five families of edges, and conversely every listed family is inclusion-minimal dominating:

1. The three edges of a triangle.
2. Three pairwise disjoint edges.
3. The entire \((n-1)\)-edge star centered at one point of \([n]\).
4. The five edges of a simple five-cycle.
5. A balanced double star with centers \(a,b\) and distinct leaves \(x_1,x_2,y_1,y_2\): the five edges \(ab, ax_1,ax_2,by_1,by_2\).

Here an edge family may leave unused points of \([n]\), except that the full star contains every edge at its center. The five families are pairwise disjoint even when their sizes coincide (for example \(n=6\)). With \(\binom nk=0\) for \(k>n\), the generating polynomial for *inclusion-minimal* dominating sets by cardinality is
\[
I_n(z)=\left(\binom n3+15\binom n6\right)z^3+\left(12\binom n5+\binom n2\binom{n-2}2\binom{n-4}2\right)z^5+n z^{n-1}.
\]
In particular \(\gamma(KG(n,2))=3\) and the upper domination number, the largest size of an inclusion-minimal dominating set, is \(\Gamma(KG(n,2))=\max\{5,n-1\}\). The polynomial \(I_n\) is **not** the ordinary domination polynomial (which counts all dominating sets).

## Assumptions and scope
The graph is finite, simple, and labeled on \([n]\), with \(n\ge5\). Distinct labels count as distinct dominating sets. A graph-theoretic vertex cover of an edge family \(H\) is a subset of its underlying point set meeting every edge; write \(\tau(H)\) for the minimum cover size and \(\nu(H)\) for its maximum matching size. A two-point cover \(\{u,v\}\) is simultaneously an edge of \(K_n\), hence a vertex of \(KG(n,2)\). No geometric or graph-regularity assumption beyond these definitions is used.

## Proof
**Criterion.** A nonempty edge family \(D\subseteq E(K_n)\) dominates \(KG(n,2)\) if and only if every two-point vertex cover of \(H_D\) is itself an edge belonging to \(D\). Indeed, a pair \(e\notin D\) is undominated exactly when it intersects every edge of \(D\); this says that the two endpoints of \(e\) form a vertex cover of \(H_D\). This proves the criterion in both directions.

Fix an inclusion-minimal dominating family \(D\), and put \(H=H_D\).

**Case \(\tau(H)=1\).** All selected edges pass through some point \(a\). Every \(\{a,x\}\), where \(x\ne a\), covers \(H\). The criterion therefore forces every edge \(ax\) to be selected. Thus \(D\) is a full star.

**Case \(\tau(H)=2\).** Choose a two-point cover \(\{a,b\}\) of \(H\). By the criterion \(ab\in D\), so every edge of \(H\) is incident with \(a\) or \(b\). If \(H\) has a triangle, its three edges themselves dominate: the triangle has no two-point cover outside its own edges. Inclusion-minimality then forces \(D\) to consist exactly of those three edges. Otherwise \(H\) is triangle-free. The neighbors of \(a\) outside \(b\) form a set \(A\), and the neighbors of \(b\) outside \(a\) a set \(B\); triangle-freeness makes \(A\cap B=\varnothing\). Since \(\tau(H)=2\), both \(A,B\) are nonempty. If \(A=\{x\}\), then \(\{b,x\}\) meets every edge of \(H\) but \(bx\notin D\), contradicting the criterion. Thus \(|A|\ge2\); symmetrically \(|B|\ge2\). Selecting any two leaves from each side together with \(ab\) gives a balanced double star. Its only possible two-point vertex cover is \(\{a,b\}\), which belongs to the selected edges; hence it dominates. Inclusion-minimality forces \(D\) to be precisely this five-edge double star.

**Case \(\tau(H)\ge3\).** If \(H\) has a triangle, that triangle dominates, forcing \(D\) to be its three edges. If \(H\) has a matching of size three, its three mutually disjoint edges have no two-point cover and hence dominate; minimality forces \(D\) to equal those three edges. In the remaining case \(H\) has no triangle and \(\nu(H)\le2\). If \(H\) were bipartite, König's vertex-cover theorem would give \(\tau(H)=\nu(H)\le2\), a contradiction. Thus it contains an odd cycle. Triangle-freeness forces that cycle to have length at least five; the bound \(\nu(H)\le2\) forbids any cycle of length seven or more, since such a cycle contains three disjoint edges. Hence \(H\) contains a five-cycle. This cycle has vertex-cover number three, so its five edges dominate. Again inclusion-minimality implies \(D\) is exactly that five-cycle.

**Minimality of all types.** Every triangle or three-edge matching dominates. A family of at most two selected edges cannot dominate for \(n\ge5\): either the two selected edges meet at \(a\) and an unselected pair \(\{a,x\}\) with \(x\) outside both edges covers them, or they are disjoint and an unselected pair joining one endpoint of each covers them. Thus the three-edge types are inclusion-minimal. A full star dominates by the criterion; deleting the spoke \(ax\) makes the unselected pair \(\{a,x\}\) cover all remaining edges. A five-cycle dominates because its cover number is three; deleting one edge gives a five-vertex path, whose two nonadjacent internal vertices form an unselected two-point cover. A balanced double star dominates as shown; deleting the center edge \(ab\) makes \(\{a,b\}\) an unselected cover, while deleting a spoke \(ax_i\) makes \(\{b,x_j\}\) an unselected cover when \(x_j\) denotes the other \(a\)-leaf, and symmetrically for spokes at \(b\). This establishes every listed family's inclusion-minimality.

**Enumeration.** Triangles are indexed by three-element point sets, and size-three matchings by six-element point sets with fifteen pairings. Full stars have one choice of center. Each five-point set supports \((5-1)!/2=12\) undirected five-cycles. A balanced double star has a uniquely recoverable unordered pair of adjacent degree-three centers, followed by an ordered choice of two leaves at the first center and two disjoint leaves at the second; for any fixed ordering of the center pair, this gives \(\binom n2\binom{n-2}2\binom{n-4}2\) configurations. All templates are distinct by their incidence structures, proving the polynomial and its two extremal cardinality consequences.

## Verification
Two self-contained Python 3 programs accompany this statement. `check_exhaustive.py` constructs closed neighborhoods of every vertex of \(KG(n,2)\), exhaustively tests all \(2^{\binom n2}-1\) nonempty vertex subsets for \(n=5,6,7\), and checks inclusion-minimality by each possible single deletion. It finds precisely \(27,203,1029\) inclusion-minimal dominating sets respectively, with five-template size/degree profiles. `check_structural.py` independently generates all claimed templates for \(5\le n\le9\), checks unique representations, actual domination and deletion minimality by a direct disjointness predicate, and reports totals \(27,203,1029,3676,10425\). Both scripts terminate with explicit success assertions; accompanying plain-text outputs record the verified cases. These finite checks corroborate, but are not substituted for, the proof for all \(n\ge5\).

## Relationship to prior work
Ivančo and Zelinka (1993) established the domination number and minimum three-edge configurations for these Kneser graphs. The 2007 thesis of Gorodezky studies minimum domination. The 2015 article by Östergård, Shao and Xu supplies bounds and numerical domination-number tables. Cornet and Torres (2023; revised 2024) furnish a general membership criterion for \(k\)-tuple dominating sets of \(KG(n,2)\); at \(k=1\), this can in principle be combined with a minimality test. The present theorem isolates the **complete set of inclusion-minimal—not merely minimum-cardinality—ordinary dominating sets**, recognizes their five graph structures and counts them at every cardinality. Thus the known Petersen-graph value of 27 minimal sets is a covered small instance rather than a new standalone count. The claim does not extend to general \(KG(n,k)\) with \(k>2\).

## Limitations
This classification concerns ordinary domination and inclusion-minimality, not minimal total domination, all dominating sets, or larger-rank Kneser graphs. Its novelty assessment is provisional: a logically broader membership test is known, and unindexed treatments of its minimal solutions could already state an equivalent classification. Verification programs establish only the indicated finite orders. Independent scientific validation has not been performed.

## References
1. J. Ivančo and B. Zelinka, *Domination in Kneser graphs*, Mathematica Bohemica 118 (1993), 147–152. https://dml.cz/bitstream/handle/10338.dmlcz/126050/MathBohem_118-1993-2_3.pdf
2. J. Gorodezky, *Dominating sets in Kneser graphs*, University of Waterloo thesis, 2007. Public repository record dated 2007-08-29. https://uwspace.uwaterloo.ca/items/162bbbfc-6952-4188-8d4a-e403b81807c4/full
3. P. R. J. Östergård, Z. Shao and X. Xu, *Bounds on the domination number of Kneser graphs*, Ars Mathematica Contemporanea 9 (2015), 187–195. https://www.dlib.si/details/URN:NBN:SI:doc-G3YP01PE
4. M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603, 2023; version 2, 2024. https://arxiv.org/html/2308.15603v2
5. SageMath graph-domination reference, documentation of inclusion-minimal dominating sets for the Petersen graph. https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/domination.html
