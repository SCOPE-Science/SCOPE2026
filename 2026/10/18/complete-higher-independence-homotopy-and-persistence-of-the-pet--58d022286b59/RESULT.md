# Complete higher-independence homotopy and persistence of the Petersen graph

## Finding
Let \(P=KG(5,2)\) be the Petersen graph, and set \(X_r=\operatorname{Ind}_r(P)\), where an induced vertex subset is a simplex precisely when each of its connected components has at most \(r\) vertices. The complete integral homotopy classification is:

| \(r\) | Nonempty simplices | Integral homotopy type |
|:---:|---:|:---|
| 1 | 75 | \(\bigvee^4 S^2\) |
| 2 | 260 | \(S^3\) |
| 3 | 380 | \(S^3\) |
| 4 | 510 | \(\bigvee^{11} S^3\) |
| 5 | 702 | \(\bigvee^{61} S^4\) |
| 6 | 857 | \(\bigvee^{74} S^5\) |
| 7 | 967 | \(\bigvee^{36} S^6\) |
| 8 | 1012 | \(\bigvee^9 S^7\) |
| 9 | 1022 | \(S^8\) |
| 10 | 1023 | contractible |

In addition, the **entire reduced persistent homology over \(\mathbb F_2\)** of the inclusions \(X_1\subseteq\cdots\subseteq X_{10}\), using half-open parameter intervals, consists precisely of:

| Homological degree | Interval | Multiplicity |
|:---:|:---:|---:|
| 2 | \([1,2)\) | 4 |
| 3 | \([2,5)\) | 1 |
| 3 | \([4,5)\) | 10 |
| 4 | \([5,6)\) | 61 |
| 5 | \([6,7)\) | 74 |
| 6 | \([7,8)\) | 36 |
| 7 | \([8,9)\) | 9 |
| 8 | \([9,10)\) | 1 |

No other nonzero-length reduced bars occur. In particular, the degree-three class born at parameter \(2\) survives both inclusions through parameter \(4\), while ten independent degree-three classes first appear at parameter \(4\); all eleven disappear at parameter \(5\).

## Assumptions and scope
The ten vertices of \(P\) are the two-element subsets of \(\{0,1,2,3,4\}\), ordered lexicographically. Two vertices are adjacent precisely when their corresponding subsets are disjoint. For each \(r\in\{1,\ldots,10\}\), include the empty simplex and every subset \(S\) for which the largest component of \(P[S]\) has cardinality at most \(r\). Realizations and homotopy equivalences are ordinary, nonequivariant ones. Integral coefficients are used for the homotopy classification; the persistence statement is solely over \(\mathbb F_2\).

## Proof
**Complete finite enumeration.** Encode each vertex subset by a ten-bit mask. For every mask, construct its induced connected components by transitive breadth-first expansion using the graph's fifteen disjointness edges. The maximum component size is its earliest filtration index. Testing all \(2^{10}=1024\) masks produces the face counts in the table, including the ten-vertex full simplex only at parameter \(10\).

**Discrete Morse reductions.** At each parameter from \(1\) through \(9\), begin with all nonempty faces unmatched. Process the ten vertices in the explicit order specified in `verify_petersen.py`. At pivot \(v\), visit currently unmatched faces in increasing mask order, and match every still-unmatched face not containing \(v\) to its coface obtained by adding \(v\), if that coface is also still unmatched. Each pair is a codimension-one face/coface pair. The checker visits every covering incidence, orienting matched covers upward and all others downward, and topologically sorts the resulting directed graph. It establishes acyclicity **at every parameter**, not just the critical-cell counts. The resulting numbers of critical cells (dimensions indicated) are:

| \(r\) | Critical cells |
|:---:|:---|
| 1 | one \(0\)-cell; four \(2\)-cells |
| 2 | one \(0\)-cell; one \(3\)-cell |
| 3 | one \(0\)-cell; one \(3\)-cell |
| 4 | one \(0\)-cell; fifteen \(3\)-cells; four \(4\)-cells |
| 5 | one \(0\)-cell; sixty-one \(4\)-cells |
| 6 | one \(0\)-cell; seventy-four \(5\)-cells |
| 7 | one \(0\)-cell; thirty-six \(6\)-cells |
| 8 | one \(0\)-cell; nine \(7\)-cells |
| 9 | one \(0\)-cell; one \(8\)-cell |

For every row except \(r=4\), discrete Morse theory immediately identifies a wedge of spheres of the displayed common dimension: there are no possible positive-dimensional attaching maps because no critical cells occur in neighboring dimensions.

**The exceptional attaching maps at parameter \(4\).** Orient each simplex by increasing vertex index. Eliminate every matched \(3\)-cell/\(4\)-cell incidence by integral unit-pivot cancellation, then restrict the resulting differential to the fifteen critical \(3\)-cells and four critical \(4\)-cells, both sorted by vertex mask. The four columns of the resulting integral Morse boundary form the matrix
\[
B=\begin{pmatrix}
0&0&0&0\\
-1&0&0&0\\
0&0&0&0\\
0&0&1&0\\
-1&-1&0&1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&-1\\
0&1&-1&-1\\
0&0&0&0\\
0&0&0&0\\
0&1&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
\]
Its rows \(2,4,9,13\) (counting from one) have determinant \(+1\) as a four-by-four minor. Consequently its four invariant factors are all units over \(\mathbb Z\). The Morse CW complex consists of one vertex, fifteen \(3\)-cells and four \(4\)-cells, hence is \(2\)-connected. The Hurewicz isomorphism \(\pi_3(\bigvee^{15}S^3)\cong\mathbb Z^{15}\), together with integral elementary basis changes of the degree-three sphere wedge, cancels the four primitive attaching degrees. Thus \(X_4\simeq\bigvee^{11}S^3\). Finally, \(X_{10}\) is the full nine-simplex and therefore contractible.

**Persistent homology.** Order all masks, including the empty mask, by the tuple (earliest parameter, cardinality, integer mask). Reduce the simplicial boundary matrix over \(\mathbb F_2\) from left to right. Include the augmented empty simplex in dimension \(-1\), so vertices map to it, giving reduced rather than unreduced persistence. The exact birth/death pairs obtained from the 1024 columns are precisely those listed above. This is a complete finite computation of the filtered chain complex, not an inference from the Betti numbers of separate stages.

## Verification
Run `python3 verify_petersen.py` and `python3 crosscheck_petersen.py` using Python 3, without third-party dependencies. The first program independently generates the graph, all 1024 masks, the nine discrete Morse matchings, every covering incidence and an explicit acyclicity topological ordering. It computes the integral signed exceptional Morse boundary, verifies a determinant-one maximal minor, and reduces the augmented boundary matrix over \(\mathbb F_2\) for the entire persistence barcode. The second program constructs components by a distinct graph traversal, computes reduced simplicial Betti numbers over the primes \(2,3,5,7\) at all ten stages from uncompressed chain complexes, and directly checks that the map on degree-three homology from parameter \(2\) to parameter \(4\) has rank one over \(\mathbb F_2\). Both scripts exhaust all subsets of the ten-vertex graph.

## Relationship to prior work
Deshpande and Singh (2020) introduced systematic homotopy calculations of higher-independence complexes and classify complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect arity trees. Their inspected paper does not calculate the Petersen graph. The earlier published Petersen two-independence calculation already establishes \(X_2\simeq S^3\); this isolated stage is **not** claimed as new here. Previously published ordinary independence, graph Čech persistence, and cut-complex results use either the first stage or different filtrations. None of those statements determines the complete integral homotopy sequence and, especially, the parameter-\(2\)-through-\(4\) persistent class or the ten classes born at parameter \(4\). The comparison is not a proof that no equivalent unindexed computation exists.

## Limitations
The theorem concerns only the canonical Petersen graph, not all cubic graphs, Kneser graphs, or higher-independence filtrations. Homotopy equivalence is proved stagewise; no assertion is made that the filtration is equivalent, as a filtered space, to a wedge filtration. The barcode is over \(\mathbb F_2\) only, while each individual stage has free integral homology. There is no claimed equivariant decomposition or integer persistence classification. All finite calculations are exhaustive within the stated ten-vertex domain; they make no infinite-family assertion.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public version January 15, 2020; especially Sections 1–3 and 6.
2. P. Deshpande, S. Shukla, and A. Singh, *Distance \(r\)-domination number and \(r\)-independence complexes of graphs*, arXiv:2001.06775, first public version January 19, 2020. Its chordal-graph results do not cover the nonchordal Petersen graph.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
4. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, Chapter 11 (acyclic matchings and critical-cell theorem).
