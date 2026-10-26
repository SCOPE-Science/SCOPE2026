# Exact rooted counting-refinement depth of long cycle powers and its sharp boundary

## Finding
Let \(k\ge2\) be an integer. Let \(C_n^k\) be the simple graph with vertex set \(\mathbb Z/n\mathbb Z\), where two *distinct* vertices are adjacent precisely when their cyclic distance is at most \(k\). Colour vertex \(0\) individually and all other vertices alike; perform synchronous one-dimensional counting colour refinement, always retaining the old colour while replacing the neighbourhood multiset by an exact colour-count signature. Let \(\mathcal P_r\) denote the partition after \(r\) strict rounds, counting the initial colouring as round zero.

For every \(n\ge4k+1\), put \(D=\lfloor n/2\rfloor\) and \(T_j=\{v:\min(v,n-v)=j\}\) for \(0\le j\le D\). The exact stable partition is \(\{T_0,T_1,\ldots,T_D\}\), consisting of \(D+1\) classes. Its **exact first stabilization round** is
\[
R(n,k)=\left\lceil\frac{D-1}{k}\right\rceil.
\]
In particular, the stable partition is exactly the orbit partition of the pointwise stabilizer of the marked vertex. The exception at the sharp lower boundary is:
\[
R(4k,k)=3\quad(k\ge2),
\]
where the same final orbit partition holds, but the displayed ceiling expression would instead give \(2\). Thus the uniform depth law begins sharply at \(n=4k+1\).

More precisely, when \(n\ge4k+1\), round one consists of \(T_0\), the union of \(T_1,\ldots,T_k\), and the union of \(T_{k+1},\ldots,T_D\). For every \(2\le r\le R(n,k)\), round \(r\) consists of separate \(T_0,T_1,\ldots,T_{\min(rk,D)}\), together with the union of all \(T_j\) satisfying \(rk<j\le D\), if nonempty. The final residual union, if it remains at \(r=R(n,k)\), contains just the one stratum \(T_D\).

## Assumptions and scope
All statements concern finite simple undirected graphs with no loops. The source graph has \(n\) labelled vertices and parameter \(k\ge2\); the main theorem assumes \(n\ge4k+1\), and its separate boundary clause assumes \(n=4k\). A round is *strict* precisely when the partition increases. Once a round produces the final partition, the next equality test has no additional strict round. The result concerns one initially individualized vertex, not arbitrarily many marked vertices, unrooted refinement, or graph isomorphism identification.

The classes \(T_j\) have size two for \(1\le j<D\), while \(T_0\) has size one. The last class has size one when \(n\) is even and two when \(n\) is odd. The reflection \(v\mapsto-v\) is always an automorphism fixing the root.

## Proof
**Automorphism upper bound.** The rooted reflection preserves adjacency and the initial colouring, hence every round of colour refinement merges the two members of each \(T_j\). No round can separate them. It remains to prove that the required rounds distinguish different distance indices.

**Initial two rounds for \(n\ge4k+1\).** Since each vertex has exactly \(2k\) neighbours, after the first round vertices have three colours: the root, the vertices at distances \(1,\ldots,k\), and vertices at distances \(k+1,\ldots,D\). Indeed, all nonroot vertices at distance at most \(k\) have exactly one root neighbour and others have none.

At the second round, a vertex of distance \(j\) for \(1\le j\le k\) has exactly \(j\) neighbours in the first-round far class. To see this, represent the vertex by \(j\): its positive steps \(1,\ldots,k\) cross the right endpoint of the rooted radius-\(k\) interval exactly \(j\) times, while its negative steps remain in that interval. The inequality \(n\ge4k+1\) prevents winding around the opposite boundary. Thus these \(k\) distances become separate.

A vertex of distance \(j\) with \(k+1\le j\le2k\) has exactly \(2k-j+1\) neighbours in the first-round near class, namely the positive-side vertices at distances \(j-k,\ldots,k\). It has no neighbours in the reflected negative-side near class, because \(n-j-k\ge k+1\). Distances \(j>2k\) have no near-class neighbours. Therefore the second-round partition has distinct classes \(T_0,T_1,\ldots,T_{\min(2k,D)}\), and one combined tail of the larger distances, if any. All far-tail vertices have the same old colour, no root neighbour and no near neighbour, so they are not further split at this stage.

**Inductive frontier.** Suppose for some \(r\ge2\) that the current partition has the distinct distance strata \(T_0,\ldots,T_a\), where \(a=rk<D-1\), and one remaining tail containing distances \(a+1,\ldots,D\). Consider a vertex at distance \(j>a\), represented by \(j\). For each already separate stratum \(T_i\), \(0\le i\le a\), a neighbour can occur only if the circular gap between \(j\) and \(i\), or between \(j\) and \(n-i\), is at most \(k\). Since \(j\le D\), \(n-j\ge j\), so **no** previously separated distance \(i<j-k\) is adjacent to \(j\). If \(j\le a+k\), the first such adjacent stratum is *exactly* \(T_{j-k}\): the vertex at \(j-k\) is joined to \(j\) by an edge of length \(k\). Here \(j-k\ge a+1-k\ge k+1>0\). Therefore vertices at distinct new distances \(a+1,\ldots,\min(a+k,D)\) have distinct first nonzero entries in their vectors of neighbour counts to the old singleton-distance strata. Vertices at distance \(j>a+k\) have zero neighbours in every previously separated stratum. All such vertices have the same old tail colour and degree \(2k\), so their remaining neighbour-count entries coincide too. This proves the asserted next partition, without assuming that all prior distance classes have just one vertex.

**Exact depth.** For \(n\ge4k+1\) we have \(D\ge2k\), hence the displayed ceiling is at least two. By the preceding induction, after round \(r\ge2\) every distance at most \(rk\) is separate, and all larger distances form one combined class. This class is itself a single distance stratum exactly when \(D-rk\le1\). Whenever \(D-rk\ge2\), the next round splits it (by the frontier argument), so the process has not yet stabilized. The first final partition is therefore attained precisely at \(r=\lceil(D-1)/k\rceil\). Since the distance partition is preserved by the reflection automorphism, it is equitable and remains unchanged thereafter.

**Boundary at \(n=4k\).** Round one has the same three colour classes. On the near group, the second-round number of neighbours in the far group is \(j\) for distance \(1\le j\le k\), so those distances separate. On the far group, the number of neighbours in the near group equals \(2k-j+1\) for \(k+1\le j\le2k-1\), while the antipodal distance \(j=2k\) has exactly two such neighbours (one on each side). Consequently round two separates every \(T_j\) except that \(T_{2k-1}\) and \(T_{2k}\) still form a single class. Since \(k\ge2\), a vertex in \(T_{2k-1}\) has a neighbour in the already distinct \(T_{k-1}\), while the antipodal vertex in \(T_{2k}\) has none. These two classes split at round three, reaching the reflection-orbit partition. It was not reached at round two, and the sharp boundary statement follows.

**Orbit identification.** Every orbit of the rooted automorphism group is contained in a refinement colour class, because all automorphisms preserve every refinement signature. Conversely each \(T_j\) is precisely an orbit of the reflection fixing the root (the reflection acts transitively on its one or two vertices). Hence the colour classes equal all rooted automorphism orbits, including the even antipodal singleton.

## Verification
The supplied standard-library programs `verify_full.py` and `verify_quotient.py` are independent finite checks, not infinite proofs. The first builds the entire adjacency graph, runs synchronous counting refinement and checks every intermediate partition predicted above. The second builds the exact distance-quotient neighbour-count matrix directly from cyclic distances and separately refines it. Both also test the sharp \(n=4k\) boundary. Execute them with `python3 verify_full.py` and `python3 verify_quotient.py` in a directory containing the attached files. The embedded successful execution records are `full_output.txt` and `quotient_output.txt`.

The direct implementation checked 840 main-family parameter pairs and 29 boundary instances, covering 402,409 vertex-round instances. The quotient implementation independently checked the same 869 instances and 206,045 intermediate distance-profile entries. These finite ranges do not establish statements for larger parameters; the algebraic induction above does.

## Relationship to prior work
The definition and broad computational interpretation of counting refinement follow Kersting, Mladenov, Garnett and Grohe (2014). Arvind, Köbler, Rattan and Verbitsky (2015) discuss the distinction between equitable partitions and automorphism orbits, without providing the present special-family round count. Kiefer and McKay (2020) study worst-case refinement iteration numbers; their main bounds do not give the rooted cycle-power depth.

Kluge (2022), especially Lemma 38, proves that for a circulant graph of **prime** order with one marked vertex the stable partition is the orbit partition of the multiplier stabilizer of the connection set. Thus the **partition conclusion in the relevant prime-order subfamily is already implied** by that stronger general theorem, after identifying the multipliers preserving the consecutive symmetric generating set. The contribution claimed here is the exact, parameter-uniform intermediate-round evolution and sharp depth formula, including all composite orders \(n\ge4k+1\), and the exceptional \(n=4k\) depth. These features are not implied by the eventual-prime-order partition statement alone.

## Limitations
This theorem is not a claim about arbitrary circulant graphs, two-dimensional Weisfeiler–Leman, the number of rounds needed to distinguish nonisomorphic graphs, or all smaller cycle powers. For \(2k+2\le n<4k\) the intermediate partitions can behave differently and are not classified here. One-point orbit recovery should not be confused with a graph-canonization guarantee. The literature search is not an exhaustive proof of publication priority, and specialized earlier results on cycle powers may remain unexamined. The independent scientific review of the result has not yet occurred.

## References
- K. Kersting, M. Mladenov, R. Garnett and M. Grohe, *Power Iterated Color Refinement*, AAAI 2014, public proceedings record dated 2014-06-21, https://ojs.aaai.org/index.php/AAAI/article/view/8992.
- V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness?*, Electronic Colloquium on Computational Complexity Report 32 (2015), https://eccc.weizmann.ac.il/report/2015/032/.
- S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182 (2020), https://arxiv.org/abs/2005.10182.
- L. Kluge, *Combinatorial refinement on circulant graphs*, arXiv:2204.01054 (2022), https://arxiv.org/abs/2204.01054.
