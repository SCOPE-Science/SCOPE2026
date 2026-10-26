# Complete semitotal-domination polynomial of fully subdivided complete graphs

## Finding

Let \(H_n=S(K_n)\) be formed from the complete graph on \(n\ge3\) labeled original vertices by replacing every edge with a path of length two. A semitotal dominating set \(X\subseteq V(H_n)\) dominates every vertex and has the property that each \(x\in X\) has a distinct \(y\in X\) with \(d_{H_n}(x,y)\le2\). Let \(\mathcal S_n(z)=\sum_X z^{|X|}\), summed over all such sets.

For integers \(a,b\ge0\) with \(a+b=n\), define
\[
Q_{a,b}(z)=\begin{cases}
(1+z)^{ab}-1,&a,b\ge1\text{ and }(a=1\text{ or }b\in\{1,2\}),\\
(1+z)^{ab},&\text{otherwise}.
\end{cases}
\]
Then the complete semitotal-domination polynomial is
\[
\boxed{\mathcal S_n(z)=\sum_{b=0}^{n}\binom nb z^{n-b+\binom b2}(1+z)^{\binom{n-b}{2}}Q_{n-b,b}(z).}
\]
In particular, its least nonzero degree is \(n\), and the number of minimum semitotal dominating sets is
\[
\boxed{[z^n]\mathcal S_n(z)=1+n(n-1)^2+\binom n3-4\mathbf1_{\{n=4\}}.}
\]
The minimum number \(\gamma_{t2}(H_n)=n\) is also implied by a previously published theorem on subdivisions; the **complete polynomial and minimum-set multiplicities**, not the minimum number by itself, are the claimed contribution.

## Assumptions and scope

All graphs are finite, simple, and undirected, with ordinary graph distance. Label the original vertices by \([n]\). For each unordered pair \(\{i,j\}\), let \(e_{ij}\) denote its inserted degree-two vertex. Thus, the vertices of \(H_n\) are the disjoint union of \([n]\) and the \(\binom n2\) symbols \(e_{ij}\), with edges \(i e_{ij}\) and \(j e_{ij}\). Selected inserted vertices are identified with a set of unordered pairs \(F\subseteq\binom{[n]}2\). A set \(X\) is uniquely represented as \(A\cup\{e_{ij}:\{i,j\}\in F\}\), with \(A\subseteq[n]\). Put \(B=[n]\setminus A\), \(a=|A|\), and \(b=|B|\).

## Proof

**Distance observations.** Any two distinct original vertices have distance two. An original vertex is within distance two of an inserted vertex precisely when it is one of that inserted vertex's endpoints (their distance is then one). Two distinct inserted vertices are within distance two precisely when their underlying edges of \(K_n\) share an endpoint (their distance is then two). These facts follow directly from the bipartite incidence construction: opposite-type distances are odd and same-type distances are even.

**Domination.** For every pair of omitted original vertices in \(B\), its inserted vertex must be selected, because neither endpoint is selected. Equivalently,
\[
\binom B2\subseteq F.
\]
Conversely, this condition dominates all inserted vertices. Every omitted original vertex needs an incident selected inserted vertex. If \(b\ge2\), one is already forced by \(\binom B2\). If \(b=1\), at least one cross edge between \(A\) and \(B\) must be in \(F\). If \(b=0\), there is no omitted original vertex.

**Semitotal witness condition.** If \(a\ge2\), each selected original vertex witnesses every other selected original vertex at distance two. If \(a=1\), its unique selected original vertex needs at least one selected incident inserted vertex, which here must come from an edge between \(A\) and \(B\). Every selected inserted vertex with an endpoint in \(A\) has a selected original endpoint witnessing it at distance one. An inserted vertex whose underlying edge lies wholly in \(B\) instead needs a second selected inserted vertex sharing an endpoint. When \(b\ge3\), the forced complete edge set \(\binom B2\) provides such a witness for each forced vertex. When \(b=2\), the single forced edge requires at least one selected cross edge; edges wholly in \(A\) cannot witness it. For \(b\le1\), there are no forced edges wholly inside \(B\). Thus all semitotal and domination conditions are met exactly when \(\binom B2\subseteq F\) and, additionally, at least one cross edge is selected if \(a,b\ge1\) and either \(a=1\) or \(b\in\{1,2\}\). There are no further restrictions.

**Counting.** For fixed \(B\), the \(\binom b2\) within-\(B\) inserted vertices are forced, contributing \(z^{\binom b2}\), while the \(a\) chosen originals contribute \(z^a\). All \(\binom a2\) inserted vertices within \(A\) are freely chosen, giving \((1+z)^{\binom a2}\). The \(ab\) crossing inserted vertices are freely chosen except in the exact cases just identified, when the empty choice is excluded. This gives \(Q_{a,b}(z)\). There are \(\binom nb\) choices for \(B\), and distinct \(B\)'s partition all configurations. Summing proves the polynomial.

**Minimum and multiplicity.** For \(b=0\), the least possible size is \(n\), attained only by all originals. For \(b=1\) or \(b=2\), one cross edge is required, and the least size is respectively \((n-1)+1=n\) or \((n-2)+1+1=n\). Their counts are \(n(n-1)\) and \(\binom n2\,2(n-2)=n(n-1)(n-2)\). For \(b=3\), the forced three inserted vertices give least size \(n\) unless \(a=1\), which occurs exactly at \(n=4\) and requires an additional cross edge. Thus this case contributes \(\binom n3\) when \(n=3\) or \(n\ge5\), and zero when \(n=4\). For \(b\ge4\), the least size is at least \(n-b+\binom b2=n+b(b-3)/2>n\). This exhausts the possibilities and yields the coefficient shown.

## Verification

The attached `checker.py` constructs \(H_n\) from adjacency lists and tests every subset directly against (1) domination via immediate neighborhoods and (2) each selected vertex having another selected vertex at graph distance at most two. It does not use the structural characterization as its feasibility test. For \(n=3,4,5,6\), it checked all \(63+1023+32767+2097151=2,131,004\) nonempty subsets (the exact counts are in `checker_output.json`), with matching coefficients in every degree. Minimum multiplicities are respectively \(14,37,91,171\). These finite tests corroborate but do not replace the all-\(n\) proof above.

## Relationship to prior work

Alikhani and Zaherifar's 2021 paper introduced and studied cardinality polynomials of semitotal dominating sets for other graph families, including stars, complete bipartite graphs, and friendship graphs. It does not state a complete polynomial for fully subdivided complete graphs. Cabrera-Martínez and collaborators' 2026 paper analyzes the *minimum* semitotal (and independent semitotal) domination number on subdivisions of general connected graphs; its result implies \(\gamma_{t2}(S(K_n))=n\) since \(K_n\) has no induced three-vertex path. The present count at every cardinality and its explicit minimum-set multiplicity are not consequences of the minimum-number statement. A graph domination polynomial, even if known on this family, is not automatically a semitotal domination polynomial because the distance-two witness condition excludes some dominating sets. Priority against possible unindexed counting results is not settled by unsuccessful search alone.

## Limitations

The formula applies to full one-step edge subdivisions of complete graphs with \(n\ge3\), not arbitrary base graphs or partial subdivisions. It does not settle root-location or unimodality questions for these polynomials. The minimum value \(n\) is previously covered; only the stronger enumerative statement and its consequences are advanced. No independent mathematical audit is claimed.

## References

1. Z. Kartal Yıldız and A. Aytaç, *Semitotal domination number of some graph operations*, first published 20 January 2021, DOI: `10.1002/num.22746`, https://doi.org/10.1002/num.22746.
2. S. Alikhani and H. Zaherifar, *On the semitotal dominating sets of graphs*, arXiv:2107.01424v1 (3 July 2021), https://arxiv.org/pdf/2107.01424.
3. A. Cabrera-Martínez, J. L. López-Carmona, I. Rios-Villamar, and A. Serrano-Díaz, *On the (independent) semitotal domination in subdivision, middle, and central graphs*, arXiv:2609.33932v1 (27 September 2026), https://arxiv.org/abs/2609.33932.
