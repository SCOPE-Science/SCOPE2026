# A sharp circular covering law for binary words of weight two

## Finding

Let \(n\ge 4\). A *circular covering* of the binary weight-two language \(\mathcal W_{n,2}\) is a nonempty finite cyclic binary word in which every binary length-\(n\) word containing exactly two ones occurs as a cyclic length-\(n\) factor. Other factors and repeated factors are allowed. The minimum circular length is exactly

\[
\boxed{\operatorname{cov}_{\circ}(\mathcal W_{n,2})=\binom n2+n-1=\binom{n+1}{2}-1.}
\]

More specifically, there is an optimum whose cyclic length-\(n\) factors consist of every weight-two word exactly once, except that \(1 0^{n-2}1\) occurs twice, together with every weight-one word having its unique one in an interior position of its length-\(n\) factor. Thus its factor multiset has exactly one repeated required word, and exactly \(n-2\) weight-one factors; no factor has any other weight.

The order restriction matters: the weight-two languages at \(n=2,3\) each admit a circular cover with exactly \(\binom n2\) positions. The theorem makes no claim about uniqueness of optimal cycles.

## Assumptions and scope

All strings are binary and indexed from zero. A cyclic word of length \(L\) has \(L\) starting positions, and its cyclic length-\(n\) factors wrap around the end, even if \(L<n\). The cyclic word is not identified with the individual length-\(n\) words under rotation; every distinct *indexed* binary word of weight two must occur. The optimum counts **symbols in the cyclic word**, not symbols in a linearized word with an appended overlap.

Use the binary order-\(n-1\) de Bruijn directed graph with vertices \(\{0,1\}^{n-1}\). Each binary \(n\)-word \(a_0\dots a_{n-1}\) labels one edge
\[
(a_0\dots a_{n-2})\longrightarrow(a_1\dots a_{n-1}).
\]
A circular covering is equivalently a closed directed edge walk traversing every required weight-two edge at least once.

## Proof

### 1. Mandatory edges form disconnected rotation cycles

Let \(M\) be the subgraph containing every weight-two edge exactly once. At any vertex incident with \(M\), the vertex has weight one or two. At a weight-one vertex, precisely one outgoing and one incoming edge extend the vertex to weight two (append/prepend one); at a weight-two vertex, precisely one outgoing and one incoming edge do so (append/prepend zero). Therefore \(M\) is a disjoint union of directed cycles. Its successor on an \(n\)-bit edge is a one-position cyclic rotation; its components are the rotation orbits of weight-two length-\(n\) words. Every component contains a vertex with weight one: rotate a word until an endpoint contains one of its ones, then delete that endpoint.

For \(n\ge4\), there are at least two components: a pair of circularly adjacent ones and a pair of circularly nonadjacent ones have different rotation orbits. Denote by \(C_*\) the component of \(110^{n-2}\). Its vertices consist precisely of the two weight-one vertices with a one at the leftmost or rightmost position, and the weight-two vertices whose two ones are adjacent within the length-\(n-1\) word. In particular, every other mandatory component is disjoint from these vertices.

### 2. Lower bound from periods of residual circuits

Consider any covering word of length \(L\). Subtract one occurrence of every mandatory edge from its closed edge-walk multigraph. This leaves a balanced directed edge multigraph \(E\) with
\[
|E|=L-\binom n2.
\]
A balanced finite directed multigraph decomposes into directed simple cycles, each counted with multiplicity. Suppose for contradiction that \(|E|\le n-2\). Every simple cycle in \(E\) has length \(p\le n-2\) and corresponds to the length-\(n-1\) windows of a binary doubly infinite periodic word whose period divides \(p\).

**A short residual cycle meeting \(C_*\) meets no other mandatory component.** A length-\(n-1\) word with a single one at its first position cannot have period \(p\le n-2\): position \(p\) would also be one. The analogous last-position word cannot have that period either. Thus a residual cycle meeting \(C_*\) must meet it at a vertex with adjacent ones. Its periodic word then contains the factor \(11\). In a \(p\)-periodic word, *every* block of length \(p+1\) contains an occurrence of \(11\); since \(n-1\ge p+1\), every vertex of this residual cycle contains \(11\). Any such vertex belonging to \(M\) must have weight two, with its two ones adjacent, and hence lies in \(C_*\). This proves the assertion.

**Distinct underlying short residual cycles cannot intersect.** Suppose two simple directed cycles of lengths \(p\) and \(q\) share a vertex (a common binary word of length \(n-1\)). The shared word then has both periods \(p\) and \(q\), and
\[
n-1\ge p+q+1>p+q-\gcd(p,q).
\]
By the Fine–Wilf periodicity theorem it has period \(\gcd(p,q)\). Since its length exceeds both initial periods, each periodic extension is forced, and the two simple directed cycles are the same periodic orbit. Thus different underlying residual cycles are vertex-disjoint; extra copies of the same orbit do not change connectivity.

The complete covering walk is connected. Yet every residual cycle touching \(C_*\) touches no other mandatory component, and no different residual cycle can share even a nonmandatory vertex with it. The mandatory edges themselves never leave their own components. Hence \(C_*\) cannot be connected to another mandatory component, a contradiction. Consequently
\[
L-\binom n2\ge n-1.
\]

### 3. Matching Eulerian construction

Write \(v_j=0^j1 0^{n-2-j}\) for the weight-one vertex with the unique one at position \(j\), for \(0\le j\le n-2\). Add the \(n-2\) previously absent edges
\[
0^j1 0^{n-1-j}:v_j\longrightarrow v_{j-1},\qquad 1\le j\le n-2,
\]
and add **one extra copy** of the mandatory edge
\[
1 0^{n-2}1:v_0\longrightarrow v_{n-2}.
\]
The \(n-1\) new edge copies form a directed cycle traversing *every* weight-one vertex. Each mandatory rotation component contains at least one such vertex, so its union with the added cycle is connected (and balanced). It has an Eulerian circuit. Reading the last bit of each traversed edge yields a cyclic binary covering of length \(\binom n2+n-1\), with exactly the factor multiplicities asserted. This matches the lower bound for every \(n\ge4\).

## Verification

The standalone `verify.py` uses Python's standard library to build every required edge, partition the mandatory edges into rotation orbits, construct the \(n-1\)-edge connector, obtain an Eulerian circuit, and check the **entire cyclic factor multiset** including the duplicated required word. These checks are run for \(4\le n\le15\). Separate finite stress checks enumerate all primitive short-period cycles for \(4\le n\le9\), verify their separation from other mandatory components when touching \(C_*\), and verify that two short cycles with \(p+q\le n-2\) cannot share a vertex. Exhaustive enumeration of binary cyclic words independently rules out shorter coverings at \(n=4,5\). Execution command: `python3 verify.py`; its terminal marker is `VERIFY_OK`.

The checks reproduce the theorem's finite instances; **the all-\(n\) proof is the graph and periodicity argument above**, not an extrapolation from the finite runs. For example, an optimal order-four word is `010011001`, of length nine.

## Relationship to prior work

Blanca and Godbole's *On Universal Cycles for new Classes of Combinatorial Structures*, arXiv:1008.2251 (first public 13 August 2010), Section 2, Definition and Theorem 4, uses the very same notion of a circular word covering every encoded weight-\(k\) length-\(n\) word, and constructs a covering of length \(\binom nk+\binom n{k-1}\). For weight two that bound specializes to \(\binom n2+n\). The present theorem proves that the exact optimum is one less, and gives a lower-bound obstruction absent from their constructive upper bound. In particular, no claim of novelty is made for the concept of the problem or for the older upper construction.

Ruskey, Sawada, and Williams's *De Bruijn Sequences for Fixed-Weight Binary Strings* (2012, DOI:10.1137/100808782) constructs length-\(\binom n2\) **shorthand** cycles: the windows have length \(n-1\), and a missing final bit must be supplied externally to recover the fixed-weight length-\(n\) words. They are not length-\(n\) cyclic-window coverings in this theorem. Their weight-one/weight-two Eulerian construction of size \(\binom n2+n\) does give an upper bound of the same form as Blanca–Godbole, but does not imply the strict optimum here.

Dębski and Lonc's *Universal Cycle Packings and Coverings for k-Subsets of an n-Set* (2016, DOI:10.1007/s00373-016-1727-6) studies circles over the **alphabet of subset elements**, where a length-\(k\) window is a \(k\)-subset. Section 1.2 explicitly distinguishes Blanca–Godbole's binary length-\(n\) encoding as a *different* covering notion; therefore its \(c_{n,k}\) is not the optimum here.

Mitchell and Wild's *Weight-constrained cut-down de Bruijn sequences*, arXiv:2607.22350 (first submitted 24 July 2026), proves Eulerian existence for adjacent weight ranges and characterizes connectivity for individual fixed weights, but does not optimize the shortest covering allowing repeated weight-two edges and other-weight edges. The Fine–Wilf theorem supplies the standard periodicity implication in the lower bound.

## Limitations

The theorem treats binary circular sequences and **exactly two ones** in each required length-\(n\) factor, for \(n\ge4\). It does not determine the optimum for three or more ones, for linear coverings, or for coverings under reversal equivalence. It does not classify all shortest covering words. Computational checks are finite and are not a substitute for the infinite proof. A review of relevant indexed records and primary texts found no previously published exact formula, but unindexed or inaccessible work may affect historical priority; no independent scientific audit has been performed.

## References

- A. Blanca and A. P. Godbole, *On Universal Cycles for new Classes of Combinatorial Structures*, arXiv:1008.2251 (13 August 2010), especially Section 2, Definition and Theorem 4. https://arxiv.org/abs/1008.2251 ; DOI:10.1137/100805674.
- F. Ruskey, J. Sawada and A. Williams, *De Bruijn Sequences for Fixed-Weight Binary Strings*, SIAM J. Discrete Math. 26 (2012), 605–617, DOI:10.1137/100808782. https://doi.org/10.1137/100808782.
- M. Dębski and Z. Lonc, *Universal Cycle Packings and Coverings for k-Subsets of an n-Set*, Graphs Combin. 32 (2016), 2323–2337, Section 1.2, DOI:10.1007/s00373-016-1727-6. https://link.springer.com/article/10.1007/s00373-016-1727-6.
- C. J. Mitchell and P. R. Wild, *Weight-constrained cut-down de Bruijn sequences*, arXiv:2607.22350 (24 July 2026), Section 3. https://arxiv.org/abs/2607.22350.
- N. J. Fine and H. S. Wilf, *Uniqueness theorems for periodic functions*, Proc. Amer. Math. Soc. 16 (1965), 109–114, DOI:10.1090/S0002-9939-1965-0174934-9.
