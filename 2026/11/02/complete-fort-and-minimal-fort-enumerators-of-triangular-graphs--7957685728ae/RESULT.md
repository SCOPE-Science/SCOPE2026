# Complete fort and minimal-fort enumerators of triangular graphs

## Finding

Let \(T_n=L(K_n)=J(n,2)\), with \(n\ge 2\). A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Write
\[
\Phi_n(z)=\sum_{F\text{ a fort of }T_n}z^{|F|},\qquad
\mathcal M_n(z)=\sum_{F\text{ an inclusion-minimal fort of }T_n}z^{|F|}.
\]
Identify each \(F\) with the edges of a simple graph \(H\) on the \(n\) labeled root vertices. Then the inclusion-minimal forts are exactly:

1. All spanning star forests with no isolated vertices (each component a star, including a single-edge star).
2. All simple cycles of lengths \(3\) through \(n-1\) on proper subsets of root vertices.

In particular, their full cardinality distribution is
\[
\boxed{\mathcal M_n(z)=n![x^n]\exp\!\left(x(e^{xz}-1)-\frac{x^2z}{2}\right)
+\sum_{\ell=3}^{n-1}\binom n\ell\frac{(\ell-1)!}{2}z^\ell.}
\]
An empty upper-limit sum equals zero.

To count *all* forts, define \(A_0(z)=1\) and, for every integer \(n\ge0\),
\[
A_n(z)=\sum_{s=0}^n(-1)^s\binom ns
(1+z)^{\binom{n-s}{2}}
\sum_{k=0}^{\lfloor s/2\rfloor}
\frac{s!}{2^kk!(s-2k)!}(n-s)^{s-2k}z^{s-k},
\]
where \(0^0=1\). Put
\[
U_n(z)=\sum_{j=0}^n(-1)^j\binom nj(1+z)^{\binom{n-j}{2}},
\qquad
B_n(z)=\sum_{j=0}^n(-1)^j\binom nj A_{n-j}(z).
\]
Then the **complete fort polynomial** is
\[
\boxed{\Phi_n(z)=A_n(z)+U_n(z)-B_n(z)-1,\qquad n\ge2.}
\]
The minimum fort sizes, followed by their numbers of labeled minimizers, are \((1,1)\) at \(n=2\), \((2,3)\) at \(n=3\) and \(n=4\), \((3,40)\) at \(n=5\), \((3,35)\) at \(n=6\), and \((3,\binom n3)\) for \(n\ge7\). The total number of inclusion-minimal forts obeys
\[
\boxed{\mathcal M_n(1)\sim\frac{e-1}{2}(n-1)!\quad\text{as }n\to\infty.}
\]

## Assumptions and scope

All graphs are finite, simple and undirected, with labeled root vertices \([n]\). Vertices of \(T_n\) are the two-subsets of \([n]\); two are adjacent precisely when their subsets intersect. A spanning star forest may include \(K_{1,1}\), regarded as one component without a distinguished center. The star-forest and cycle cases above are disjoint. All formulas concern ordinary zero-forcing forts, not their skew or positive-semidefinite variants. The claimed formulas are valid for all integers \(n\ge2\), including small boundary orders.

## Proof

**Local characterization.** For any unselected root edge \(ab\), the corresponding vertex of \(T_n\) has exactly \(d_H(a)+d_H(b)\) selected neighbors. A sum of nonnegative integers equals one only for degree pair \((0,1)\) or \((1,0)\); in either case \(ab\notin E(H)\) automatically. Consequently the nonempty edge set \(E(H)\) is a fort if and only if \(H\) does not have both an isolated vertex and a degree-one vertex.

**Inclusion-minimal forts.** If a fort \(H\) has an isolated root vertex, it has no degree-one root vertex. Any nonempty finite graph with no degree-one vertices contains a cycle. Every simple cycle on a proper root subset is itself a fort, hence inclusion-minimality forces \(H\) to consist of that cycle alone. Removing any cycle edge creates a degree-one vertex while retaining a root isolate, so such cycles are indeed minimal.

If \(H\) has no isolated root vertices, it is a spanning edge cover and therefore a fort. An inclusion-minimal fort must be an inclusion-minimal edge cover, because any proper spanning edge subgraph would remain a fort. Inclusion-minimal edge covers are exactly spanning star forests: if an edge has neither endpoint of degree one, deleting it retains an edge cover; conversely, every edge of a spanning star forest has a leaf endpoint and is indispensable. Every proper subgraph of such a star forest has at least one isolated root and at least one degree-one root (after removing the first edge, an isolated leaf and a surviving leaf are present, unless the remaining graph is empty, in which case it is not a fort). Thus each spanning star forest is inclusion-minimal as a nonempty fort. The last assertion also covers a spanning matching: deleting an edge yields isolates and retained degree-one endpoints, or the empty set.

**Minimal-fort enumerator.** A labeled star component on \(r+1\) root vertices contributes \(x^{r+1}z^r/r!\) for \(r\ge2\), counting choices of center, while the \(r=1\) component contributes \(x^2z/2\) with no distinguished center. The exponential formula for sets of such components gives \(\exp(x(e^{xz}-1)-x^2z/2)\). A simple unoriented cycle of length \(\ell\) has \((\ell-1)!/2\) labeled realizations on a fixed \(\ell\)-subset, and only \(\ell<n\) is admissible here. Their disjoint contribution proves \(\mathcal M_n\).

**All-fort enumerator.** Let \(A_n\) enumerate all simple root graphs with no degree-one vertices (isolates permitted), \(U_n\) those with no isolates, and \(B_n\) those with neither. To construct \(A_n\), use inclusion-exclusion on the set \(S\) of \(s\) vertices required to have degree exactly one. Within \(S\), the selected edges are necessarily a matching on \(2k\) vertices, in \(s!/(2^kk!(s-2k)!)\) ways. The remaining \(s-2k\) vertices of \(S\) each choose one neighbor outside \(S\), in \((n-s)^{s-2k}\) ways; edges between the \(n-s\) other vertices are arbitrary. There are \(s-k\) forced selected edges. This proves the displayed \(A_n\). Standard isolation inclusion-exclusion yields \(U_n\). Applying isolation inclusion-exclusion to \(A_n\) yields \(B_n\). The local characterization makes every nonempty fort correspond to a graph counted by \(A_n\cup U_n\); their intersection is \(B_n\). Their union includes the empty edge set exactly once, so subtract one to obtain \(\Phi_n\).

**Minimum coefficients and asymptotic.** The cycle part first appears in degree three at \(n=4\) and has \(\binom n3\) triangles for \(n\ge4\). A spanning star forest has \(n-c\) edges for \(c\) components with each component of order at least two. Thus its minimum size is \(\lceil n/2\rceil\), attained by perfect matchings when \(n\) is even, and by one three-vertex star plus a matching when \(n\) is odd. The listed exceptional minimum coefficients now follow directly; for \(n\ge7\), spanning star forests have at least four edges, whereas triangles have three.

To prove the asymptotic, the cycle contribution at \(z=1\) equals
\[
\frac{n!}{2}\sum_{r=1}^{n-3}\frac1{(n-r)r!}
\sim \frac{e-1}{2}(n-1)!.
\]
For fixed \(\varepsilon>0\), the asymptotic follows by splitting the sum at a fixed large \(r\), controlling the tail with the factorial denominator, and then letting the split grow. The number of spanning star forests with \(c\) components is bounded above by \(\binom nc c^{n-c}\), by choosing one possible center per component and assigning other vertices to centers; the bound deliberately allows invalid assignments. Since \(c\le n/2\), split into \(c<2n/\log n\) and \(c\ge2n/\log n\). Summing the respective bounds gives at most \(n2^n(2n/\log n)^n\) and \(n2^nn^ne^{-2n}\), both \(o((n-1)!)\) by Stirling's inequality. Therefore the cycles control \(\mathcal M_n(1)\).

## Verification

The supplied `verify.py` enumerates every subset of vertices of \(T_n\) for \(2\le n\le7\) and tests the original outside-neighbor fort condition directly. It independently computes the polynomial \(\Phi_n\) by degree-one/isolated-vertex inclusion-exclusion, and \(\mathcal M_n\) by star-forest recurrence and cycle counting; it enumerates inclusion-minimal forts by subset containment. All coefficients and classification checks agree, ending in `VERIFY_OK`. At \(n=5\), the complete polynomial is \(40z^3+150z^4+252z^5+210z^6+120z^7+45z^8+10z^9+z^{10}\). The infinite claims follow from the proof, not from finite tests.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal and Schuerger (arXiv:2310.17904, first posted 2023-10-27) study forts, fractional zero forcing and Cartesian products; their examined results do not provide these triangular-graph enumerators. Becker, Cameron, Hanely, Ong and Previte (arXiv:2404.05963, first posted 2024-04-09) enumerate minimal forts for other graph families, but not this complete line-graph family. Afzali, Ghodrati and Maimani (DOI:10.1007/s12190-024-02064-w) report failed-zero-forcing numbers of Johnson and Kneser graphs; their scalar result is related to the smallest-fort size and is not claimed as new here. The full text of that last article was not available for the comparison. The mathematical contribution assessed here is the complete pair of enumerators and inclusion-minimal obstruction classification, not the already studied scalar smallest-fort value.

## Limitations

The conclusions apply specifically to \(J(n,2)\) and ordinary forts; general \(J(n,k)\) and other forcing variants are unaddressed. The finite verifier reaches \(n=7\), not arbitrary order. Publication-priority uncertainty remains, particularly because the complete text of the related 2024 Johnson-graph paper could not be checked; this is a self-review, not independent validation.

## References

1. Cameron, Hogben, Kenter, Mojallal, Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (2023).
2. Becker, Cameron, Hanely, Ong, Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (2024).
3. Afzali, Ghodrati, Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, DOI:10.1007/s12190-024-02064-w (2024).
