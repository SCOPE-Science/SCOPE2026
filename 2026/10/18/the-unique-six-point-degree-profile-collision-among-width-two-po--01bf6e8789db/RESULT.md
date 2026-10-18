# The unique six-point degree-profile collision among width-two posets

## Finding
Let \(P=(V,<)\) be a nonempty finite strict partial order. For every \(x\in V\), define \(d_-(x)=|\{y:y<x\}|\) and \(d_+(x)=|\{y:x<y\}|\), and let \(\mathcal D(P)\) be the multiset of the ordered pairs \((d_-(x),d_+(x))\) over all vertices. This is the global one-round directed counting-colour-refinement fingerprint of the strict-order relation, starting from a uniform vertex colour (with the equality/absence relation treated separately).

**Sharp finite classification.** Among all isomorphism types of nonempty posets of width at most two and order at most six, the multiset \(\mathcal D\) distinguishes every pair of nonisomorphic posets except for precisely **one** unordered pair of six-element types. There are 75 six-element types and 74 distinct six-element fingerprints. Every type on at most five elements is determined by its fingerprint. Both exceptions have six distinct local degree pairs and are rigid; consequently a second global round of directed counting-colour refinement distinguishes the exceptions, and hence all width-two posets through six elements.

On \(V=\{1,2,3,4,5,6\}\), write
\[
E_0=\{(1,4),(1,5),(1,6),(2,5),(2,6),(3,4),(3,5),(4,5)\}.
\]
The two strict-order relations \(P=E_0\cup\{(1,2)\}\) and \(Q=E_0\cup\{(1,3)\}\) are both transitive, connected and of width two. They have the common profile
\[
\mathcal D(P)=\mathcal D(Q)=\{\!\{(0,2),(0,4),(1,2),(2,0),(2,1),(4,0)\}\!\}.
\]
They are not isomorphic.

## Assumptions and scope
A poset here is a finite irreflexive transitive binary relation, with all strict comparabilities present, **not** only its Hasse-cover arcs. Width at most two means that no three distinct elements are pairwise incomparable. Isomorphisms preserve arc orientation; order duality is not identified. The finite bound six is part of the theorem: no claim is made that only one collision occurs for larger posets. The multiset \(\mathcal D\) is a one-round global counting fingerprint, not complete \(C^2\)-equivalence.

## Proof
**Witness.** In \(P\), the degree-pair labels of vertices \(1,2,3,4,5,6\) are respectively \((0,4),(1,2),(0,2),(2,1),(4,0),(2,0)\). In \(Q\) they are respectively \((0,4),(0,2),(1,2),(2,1),(4,0),(2,0)\). These are the same six pair values, each exactly once. Any isomorphism must therefore fix \(1,4,5,6\) and exchange \(2,3\). However \(2<6\) in \(P\), while \(3\not<6\) in \(Q\). Hence there is no isomorphism. Direct inspection of the displayed relations verifies transitivity, the no-three-antichain condition, and connectedness of their underlying comparability graphs.

**Completeness.** Every finite poset admits a linear extension. Label its vertices increasingly in one such extension; every strict comparison is then among the \(\binom n2\) ordered pairs \((i,j)\) with \(1\le i<j\le n\). Thus every isomorphism type of order \(n\) occurs among the \(2^{\binom n2}\) binary selections of these pairs. The standalone verifier `verify_uppertriangular.py` enumerates **all** such selections for each \(1\le n\le6\), retains a selection exactly when it is transitively closed and has no three-element antichain, and groups candidates by the exact multiset \(\mathcal D\). Within each multiset group it constructs all possible bijections preserving each vertex's ordered degree pair and compares every arc; these are precisely all possible order isomorphisms. No graph-isomorphism heuristic, random sampling, or approximate hash is used. Hence the reported complete census is exhaustive.

The census gives the following exact triples \((\text{isomorphism types},\text{degree fingerprints},\text{collision groups})\):

| Order | Types | Fingerprints | Collision groups |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 |
| 2 | 2 | 2 | 0 |
| 3 | 4 | 4 | 0 |
| 4 | 10 | 10 | 0 |
| 5 | 26 | 26 | 0 |
| 6 | 75 | 74 | 1 |

The unique six-element collision group has cardinality two and is represented by \(P,Q\) above. All six degree pairs of each exception are distinct; thus the first-round colours identify its vertices individually. A second round then records, for each individually identified vertex, its complete predecessor and successor first-round colour sets. If the second-round global histograms of \(P,Q\) agreed, the degree-profile-matching bijection would preserve every relation, contradicting the preceding explicit mismatch. All other types were already distinguished at the first round.

## Verification
Three independent, standard-library-only Python programs can be run directly with Python 3:

`python3 verify_uppertriangular.py`

`python3 verify_permutation.py`

`python3 verify_witness.py`

The first program enumerates all upper-triangular relations (up to \(2^{15}=32768\) masks), giving the complete finite classification. The second independently generates all \(321\)-avoiding permutations through length six and their dimension-two posets, then performs a separately implemented degree-preserving isomorphism test; it reproduces all class and fingerprint counts. The third checks the explicit witness by direct integer arithmetic and verifies that the degree-preserving candidate bijection fails. The files `uppertriangular_output.txt`, `permutation_output.txt`, and `witness_output.txt` record actual successful executions. The two enumeration routes are supplementary independent checks, not extrapolations beyond six elements.

## Relationship to prior work
Atkinson, Sagan, and Vatter (arXiv:1102.5568v1, Section 1) discuss the classical encoding of dimension-two posets by permutations; the second verifier uses the resulting \(321\)-avoidance model of width-two posets. Their work does not establish the paired-degree collision census above.

Gellert and Sanyal, *On degree sequences of undirected, directed, and bidirected graphs* (arXiv:1512.08448v1, Theorem 3.6; also European Journal of Combinatorics 64 (2017)) state a stronger uniqueness property for connected width-two transitive digraphs under their net-degree sequence. If read as written, that assertion conflicts with the two explicit connected examples above: after relabelling \(Q\) by the unique degree-profile bijection, the **labelled net-degree vectors agree** even though the arc sets differ. Thus that published statement cannot serve as a valid uniqueness implication for the present classification. Their paper's more general discussion of degree-preserving operations is distinct from the precise finite multiset census established here. This comparison records a concrete mathematical discrepancy rather than treating an unverified literature assertion as an obstruction or assuming that no earlier coverage exists.

Searches of published mathematical records for width-two posets, predecessor/successor profiles, net-degree uniqueness, permutation encodings, and first-round counting refinement did not locate an equivalent sharp six-element classification. A prior small-order table or a specialized invariant paper not found by these searches remains possible.

## Limitations
Only the bound of six elements is certified. Finite exhaustive computation does not establish a general reconstruction theorem or a unique collision for all orders. The cited 2015/2017 uniqueness assertion has not been independently corrected by its authors here; the contradiction stated above concerns precisely its written hypotheses and conclusion. Complete priority over inaccessible or unindexed specialist literature is not established, and independent scientific audit is not performed.

## References
1. M. D. Atkinson, B. E. Sagan, and V. Vatter, *Counting (3+1)-avoiding permutations*, arXiv:1102.5568v1 (first posted 2011-02-28), Section 1. https://arxiv.org/abs/1102.5568
2. L. Gellert and R. Sanyal, *On degree sequences of undirected, directed, and bidirected graphs*, arXiv:1512.08448v1 (first posted 2015-12-28), Section 3, especially Theorems 3.4 and 3.6. https://arxiv.org/abs/1512.08448
3. L. Gellert and R. Sanyal, *On degree sequences of undirected, directed, and bidirected graphs*, European Journal of Combinatorics 64 (2017), 113–124, doi:10.1016/j.ejc.2017.04.002.
