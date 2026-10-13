# Four symmetry types and 448 minimum locating-dominating codes of the Heawood graph

## Finding
Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. A locating-dominating set \(S\subseteq V(H)\) is a set for which the signatures
\[
N(v)\cap S,\qquad v\in V(H)\setminus S,
\]
are all nonempty and pairwise distinct. **Exactly \(448\) six-vertex subsets** are locating-dominating. Since no set of at most five vertices qualifies, these are precisely all minimum locating-dominating sets.

Under the full automorphism group of \(H\), of order \(336\), these optimal sets form exactly **four orbits**, of cardinalities
\[
\boxed{28,\quad84,\quad168,\quad168.}
\]
Their geometric types are as follows. Write \(p\) for the number of selected point vertices, \(q=6-p\) for the number of selected line vertices, and \(e\) for the number of Heawood edges induced by the selected set.

| Geometric type | \(p,q\) | \(e\) | Number of sets | Orbit size |
| --- | --- | --- | ---: | ---: |
| Three selected points lie on one Fano line | \(3,3\) | \(3\) | \(28\) | \(28\) |
| Three selected points are noncollinear, two selected incidences | \(3,3\) | \(2\) | \(84\) | \(84\) |
| Three selected points are noncollinear, three selected incidences | \(3,3\) | \(3\) | \(168\) | \(168\) |
| Two points and four lines, or its point–line dual | \(2,4\) or \(4,2\) | \(2\) | \(84+84\) | \(168\) |

Thus \(280\) optimal sets have a \(3+3\) point–line split; \(84\) have a \(2+4\) split; and \(84\) have a \(4+2\) split. The four orbit types also have distinct multisets of signature sizes among the eight vertices outside \(S\): respectively \(\{1^6,3^2\}\), \(\{1^2,2^6\}\), \(\{1^4,2^4\}\), and \(\{1^3,2^4,3^1\}\).

## Assumptions and scope
Vertices of \(H\) are seven points \(p_0,\ldots,p_6\) and seven lines \(\ell_0,\ldots,\ell_6\) of the projective plane of order two. Identify an index \(i\) with the nonzero binary three-vector encoded by integer \(i+1\). Incidence is given exactly by
\[
p_i\sim\ell_j\iff\left\langle i+1,j+1\right\rangle_{\mathbb F_2}=0,
\]
where the bracket denotes binary dot product. Equivalently the seven Fano lines, given as point-index triples, are
\[
\begin{array}{c|ccccccc}
 j&0&1&2&3&4&5&6\\ \hline
 \ell_j&135&034&236&012&146&056&245.
\end{array}
\]
For example, \(135\) means \(\{p_1,p_3,p_5\}\). This completely specifies the labeled graph; no choice of drawing or embedding matters. The result is for the ordinary locating-dominating notion: only vertices outside \(S\) must be separated, and an outside signature must be nonempty. It is not a claim about identifying codes, which must separate all vertices.

## Proof
**1. A bipartition-signature lemma and the lower bound.** Let \(P\) and \(Q\) be the selected point and line indices of \(S\), respectively, and put \(p=|P|\), \(q=|Q|\). Every point outside \(P\) has its signature inside the selected line vertices, whereas every line outside \(Q\) has its signature inside the selected point vertices. Hence signatures from the two outside sides are automatically distinct whenever nonempty. The condition reduces *exactly* to requiring distinct nonempty selected-line traces for the \(7-p\) outside points, and distinct nonempty selected-point traces for the \(7-q\) outside lines. Therefore
\[
7-p\le 2^q-1,\qquad 7-q\le 2^p-1.\tag{1}
\]
When \(p+q=5\), every integer value of \(p\) violates at least one inequality (1): for \(p=2,q=3\), for example, the four outside lines would need four distinct nonempty subsets of only two selected points; the \(p=3,q=2\) case is dual, and the remaining cases are more restrictive. Enlarging a locating-dominating set preserves that property, so no smaller set exists. When \(p+q=6\), inequalities (1) allow only \(p\in\{2,3,4\}\).

**2. Exhaustive geometric count with a seven-line incidence table.** For fixed \(P\) and \(q=6-|P|\), the condition of Step 1 is decided by the seven line triples displayed above. The full lists of admissible line-index sets \(Q\) in three canonical cases are:

| Canonical \(P\) | Geometric kind | All admissible \(Q\) |
| --- | --- | --- |
| \(\{0,1\}\) | Point pair | \(0126,0256,1246,2456\) |
| \(\{0,1,2\}\) | Collinear point triple | \(012,056,146,245\) |
| \(\{0,1,3\}\) | Noncollinear point triple | \(026,046,126,156,246,256,346,356,456\) |

Here each string of digits specifies the set of line indices, not a decimal integer. To check completeness directly, run through the \(\binom{7}{q}\) subsets \(Q\) and compute, for every \(i\notin P\), the set of selected \(j\in Q\) whose displayed line triple contains \(i\), and symmetrically for each \(j\notin Q\) the set \(P\cap\ell_j\). Reject precisely if either side has an empty or repeated set. This is a finite, explicit incidence-table proof requiring at most \(35\) choices per canonical case; the standalone checker repeats it by independent set and bitmask implementations.

The Fano-plane collineation group is transitive on unordered pairs, on collinear triples, and on noncollinear triples. There are \(\binom72=21\) unordered pairs, \(7\) collinear point triples, and \(\binom73-7=28\) noncollinear triples. The first three rows thus give \(21\cdot4=84\), \(7\cdot4=28\), and \(28\cdot9=252\) codes. Point–line duality gives another \(84\) codes with \(p=4\). They are disjoint by the value of \(p\). Consequently the complete count is
\[
84+28+252+84=\boxed{448}.\tag{2}
\]

**3. Exact orbit classification.** The point–line-preserving automorphisms are the \(168\) invertible linear maps \(A\in\mathrm{GL}(3,2)\), acting by \(x\mapsto Ax\) on points and \(y\mapsto A^{-T}y\) on line normals. Interchanging \(x\) and \(y\) is an additional incidence-preserving duality. Since \(H\) is connected bipartite and every point–line-preserving automorphism is a Fano-plane collineation, these account for the full automorphism group of order \(336\).

For fixed collinear \(P\), its four admissible \(Q\)'s form one orbit under the stabilizer of \(P\); this yields the orbit of size \(7\cdot4=28\). For fixed noncollinear \(P\), its nine admissible \(Q\)'s split under the stabilizer of \(P\) into three configurations with \(e=2\) and six with \(e=3\); the stabilizer is transitive on each class. These give two orbits of sizes \(28\cdot3=84\) and \(28\cdot6=168\). For fixed two-point \(P\), the stabilizer is transitive on its four admissible \(Q\)'s; this gives one \(84\)-element orbit of \(2+4\) splits, joined by duality with the \(84\)-element orbit of \(4+2\) splits. No two types can fuse: their point-split/collinearity/incidence data are preserved by collineations and dualities. Together these are the four stated orbits.

In the chosen indexing, representatives \(S\) can be listed as sets of global vertex indices, with point \(p_i\) indexed \(i\) and line \(\ell_j\) indexed \(7+j\):

| Orbit size | Representative \(S\) |
| ---: | --- |
| \(28\) | \(\{0,1,2,7,8,9\}\) |
| \(84\) | \(\{0,1,3,9,11,13\}\) |
| \(168\) with \(3+3\) split | \(\{0,1,3,7,9,13\}\) |
| \(168\) with \(2+4\) or \(4+2\) split | \(\{0,1,7,8,9,13\}\) |

## Verification
The standalone `verify.py` constructs the fourteen-vertex incidence graph from binary dot products, checks the Fano-plane intersection axioms, and independently tests every six-subset twice: once by set-valued signatures and once by bitmasks. It also tests every subset of cardinality less than six, enumerates the three canonical incidence-table rows, constructs all \(168\) matrices in \(\mathrm{GL}(3,2)\), obtains all \(336\) automorphisms, and partitions all \(448\) solutions into the claimed orbits. Run it with `python3 verify.py`. Successful execution reports `VERIFY_OK`; only Python's standard library is required. The finite search covers exactly \(2^{14}=16{,}384\) vertex subsets and \(\binom{14}{6}=3{,}003\) six-subsets; it is an exhaustive finite verification, not a sample or a claim of independent external certification.

## Relationship to prior work
Balbuena, Foucaud, and Hansberg proved in Proposition 24 of their 2015 study that the Heawood graph has location-domination number \(6\) and exhibited one minimum set. Their proof concerns the minimum size, not the number of minimum sets or their orbit decomposition. The present result refines that established extremal parameter to an exact labeled count, four symmetry classes, and an explicit Fano-plane characterization. The general global location-domination problem of Hernando, Mora, and Pelayo is a different requirement (simultaneous location-domination in a graph and its complement); results about it do not determine this ordinary-code census. Their 2015 bipartite-graph follow-up develops an associated-graph construction and complement comparisons, not an optimal Heawood code census.

## Limitations
The result concerns exactly the Heawood graph and ordinary locating-dominating sets of minimum cardinality, not identifying codes or all larger locating-dominating sets. The orbit classification is under the full graph automorphism group, which includes point–line dualities. The original 2015 paper already proves the minimum size; no priority over that theorem is claimed. Prior exact enumerations under different Fano-plane, test-cover, or code terminology cannot be definitively excluded by finite bibliographic searches. The finite certificate is complete for the specified graph, but independent mathematical audit is not yet performed.

## References
1. C. Balbuena, F. Foucaud, and A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, Electronic Journal of Combinatorics **22** (2015), #P2.15, Proposition 24. DOI:10.37236/4562; arXiv:1407.7263 (first posted 2014-07-27 UTC).
2. C. Hernando, M. Mora, and I. M. Pelayo, *On global location-domination in graphs*, arXiv:1312.0772 (2013). The global variant is distinguished from ordinary location-domination in the comparison above.
3. C. Hernando, M. Mora, and I. M. Pelayo, *On global location-domination in bipartite graphs*, arXiv:1506.03442 (first posted 2015-06-10).
