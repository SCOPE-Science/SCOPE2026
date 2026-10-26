# Rigidity of intersecting triple systems at positive pair codegree three

## Finding

Let \(H=(V,E)\) be a finite, simple, nonempty \(3\)-uniform hypergraph. Say that \(H\) is intersecting if \(e\cap f\ne\varnothing\) for every two distinct edges \(e,f\in E\). For a pair \(p\subseteq V\), write \(d_H(p)=|\{e\in E:p\subseteq e\}|\), and define the minimum positive pair codegree by
\[
\delta_2^+(H)=\min_{p:d_H(p)>0}d_H(p).
\]
If \(H\) is intersecting and \(\delta_2^+(H)\ge3\), then there is a unique five-element set \(S\subseteq V\) such that
\[
E=\binom{S}{3}.
\]
In other words, the non-isolated part of \(H\) is exactly \(K_5^{(3)}\). Conversely, \(K_5^{(3)}\) together with any number of isolated vertices is intersecting and has \(\delta_2^+=3\). Thus the sharp maximum of \(\delta_2^+(H)\) over nonempty intersecting \(3\)-graphs is \(3\), with the stated unique support structure.

## Assumptions and scope

All hypergraphs are finite, simple, and \(3\)-uniform. “Intersecting” means that every two distinct hyperedges meet in at least one vertex; it does not mean pairwise intersection of size at least two. Positive pair codegree ignores pairs not contained in any edge. Isolated vertices are allowed and do not affect \(\delta_2^+\). The result concerns only intersecting triple systems, not arbitrary triple systems or uniformities greater than three.

## Proof

Assume \(H\) is nonempty, intersecting, and \(\delta_2^+(H)\ge3\). Choose a pair \(\{a,b\}\) in an edge. Its codegree is at least three, so there are distinct vertices \(c,d,e\notin\{a,b\}\) with
\[
abc,\quad abd,\quad abe\in E.
\]

First, any edge avoiding both \(a\) and \(b\) must meet each of \(abc,abd,abe\). Since it has size three, it must be exactly \(cde\). Hence \(cde\) is the only possible edge avoiding \(a,b\).

Next, suppose \(axy\in E\) with \(x,y\notin\{a,b\}\). The pair \(xy\) must lie in at least three edges. The only possible such triples are \(axy\), \(bxy\), and (if \(\{x,y\}\subseteq\{c,d,e\}\)) the edge \(cde\). Therefore \(\{x,y\}\subseteq\{c,d,e\}\). By symmetry, the same holds for any edge containing \(b\) but not \(a\).

If \(abx\in E\) for some \(x\notin\{c,d,e\}\), then the only edge that can contain the pair \(ax\) is \(abx\): any other edge containing \(a,x\) but not \(b\) is excluded by the preceding paragraph. This contradicts \(d_H(\{a,x\})\ge3\). Thus every edge containing both \(a,b\) has its third vertex in \(\{c,d,e\}\). Combining these facts, every edge of \(H\) lies inside
\[
S=\{a,b,c,d,e\}.
\]

The pair \(ac\) occurs in \(abc\) and must have codegree at least three. Because all edges lie in \(S\), this forces \(acd,ace\in E\). The pair \(ad\), already in \(abd,acd\), then forces \(ade\in E\). The pair \(bc\) forces \(bcd,bce\in E\); the pair \(bd\) forces \(bde\in E\); and the pair \(cd\), already in \(acd,bcd\), forces \(cde\in E\). These are all ten triples on \(S\), so \(E=\binom{S}{3}\). No edge can use a vertex outside \(S\), as already proved.

Conversely, any two triples on a five-element set intersect, and each pair of its vertices lies in exactly three triples. Hence \(K_5^{(3)}\) has \(\delta_2^+=3\), proving sharpness and uniqueness.

## Verification

The proof uses only the definitions of intersection and positive pair codegree. The key finite deductions are: (i) the three edges through \(ab\) force the only possible edge avoiding \(a,b\) to be \(cde\); (ii) the codegree of any pair \(xy\) in an edge \(axy\) forces \(x,y\in\{c,d,e\}\); and (iii) once the support is confined to five vertices, the codegree requirement forces every triple. The converse checks both intersection and the exact codegree of every pair. No finite enumeration is used as proof.

## Relationship to prior work

Balogh, Lemons, and Palmer introduced the relevant minimum-positive-codegree extremal setting and proved that, for fixed parameters and sufficiently large order, a maximum-size intersecting \(r\)-graph with minimum positive co-degree at least \(k\) is a \(k\)-kernel system. Their Proposition 4 gives the general feasibility bound \(k\le r\). Spiro extended the maximum-size result to \(t\)-intersecting hypergraphs with positive co-degrees of lower-dimensional faces. In the parameter choice \(r=k=3\), these results identify \(K_5^{(3)}\) as the large-order extremal construction, but they do not state that every admissible hypergraph—not merely a maximum-size one—is forced to be \(K_5^{(3)}\) for every order. The present claim is this all-orders structural rigidity statement.

## Limitations

The classification relies on uniformity three and ordinary intersection (intersection size at least one). It does not establish an analogous classification for \(r\ge4\), for \(t\)-intersecting systems with \(t\ge2\), or for minimum positive codegrees of smaller faces. The literature search was bounded; absence of an exact-match result is not a proof that no earlier statement exists.

## References

1. J. Balogh, N. Lemons, and C. Palmer, “Maximum size intersecting families of bounded minimum positive co-degree,” arXiv:2005.04282 (first posted 2020-05-08); *SIAM Journal on Discrete Mathematics* 35(3) (2021), 1525–1535. DOI: 10.1137/20M1336989.
2. S. Spiro, “On \(t\)-Intersecting Hypergraphs with Minimum Positive Codegrees,” arXiv:2110.10317 (first posted 2021-10-20); *SIAM Journal on Discrete Mathematics* 37(2) (2023), 675–683. DOI: 10.1137/21M1465998.
