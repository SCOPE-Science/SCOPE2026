# Partition-quotiented chamber bound for polygonal links
## Finding
For every integer \(N\ge4\), let \(\mathcal L_N\) be the set of ambient-isotopy classes of ordinary unoriented unordered links in \(\mathbb R^3\) that admit a polygonal representative using at most \(N\) total sticks. Let \(p_{\ge3}(N)\) denote the number of integer partitions of \(N\) into parts at least \(3\). Then there is an absolute constant \(A>0\) such that
\[
|\mathcal L_N|\le p_{\ge3}(N)(AN)^{3N}.
\]
In particular,
\[
|\mathcal L_N|\le N^{3N+o(N)}.
\]

The recent source proves that, for any fixed labeled cyclic decomposition of the \(N\) vertex slots into link components, the complement of its cubic and quartic self-intersection walls has at most \((AN)^{3N}\) connected chambers, but then sums this over at most \(N!\) labeled decompositions to obtain \(N^{4N+o(N)}\). The factorial factor is unnecessary for ordinary unordered links: only the cycle type of the decomposition permutation matters after relabeling the coordinate slots.

## Assumptions and scope
A polygonal link component is a nondegenerate embedded polygon and therefore uses at least \(3\) sticks. A link using fewer than \(N\) total sticks may be subdivided along its edges to use exactly \(N\) sticks without changing ambient-isotopy type. As in the source argument, an arbitrarily small generic perturbation can then be used to avoid the finite wall family while preserving the link type.

The claim concerns ordinary unoriented unordered links. It does not count labeled components, oriented components, or geometrically marked vertices. Those variants retain additional combinatorial data and are not covered by the quotient used here.

## Proof
Fix \(N\). A labeled cyclic decomposition of the vertex set \(\{1,\ldots,N\}\) is equivalently a permutation \(\sigma\in S_N\) whose cycles are the cyclic vertex orders of the components. For a nondegenerate polygonal link every cycle has length at least \(3\).

Relabeling the \(N\) coordinate slots by a permutation \(\tau\in S_N\) replaces the decomposition permutation by
\[
\sigma\longmapsto \tau\sigma\tau^{-1}.
\]
This relabeling is only a change of names of the vertex coordinates. It does not create a new ordinary link type, and every geometric realization for the original decomposition is carried to a realization in the relabeled decomposition.

Two permutations are conjugate in \(S_N\) exactly when they have the same cycle type. Hence, to cover all ordinary links with exactly \(N\) sticks, it is enough to choose one canonical cyclic decomposition for each cycle type with all parts at least \(3\). Those cycle types are in bijection with integer partitions
\[
N=n_1+\cdots+n_c,\qquad n_i\ge3,
\]
so there are exactly \(p_{\ge3}(N)\) canonical combinatorial models to consider.

For each fixed model, the source's determinantal argument uses at most \(N^2/2\) non-incident-edge determinant walls together with exactly \(N\) adjacent-edge squared-cross-product walls, all of bounded degree in \(3N\) real coordinates. Its sign-condition component estimate gives at most
\[
(AN)^{3N}
\]
chambers for that fixed cyclic decomposition, with \(A\) absolute and independent of the decomposition. Every chamber carries at most one ordinary link type. Summing only over the \(p_{\ge3}(N)\) canonical cycle types gives
\[
|\mathcal L_N|\le p_{\ge3}(N)(AN)^{3N}.
\]

Finally \(p_{\ge3}(N)\le p(N)\), where \(p(N)\) is the ordinary partition function. The Hardy--Ramanujan asymptotic gives
\[
p(N)\sim \frac1{4N\sqrt3}\exp\!\left(\pi\sqrt{\frac{2N}3}\right),
\]
so \(\log p_{\ge3}(N)=O(\sqrt N)=o(N\log N)\). Therefore
\[
p_{\ge3}(N)(AN)^{3N}=N^{3N+o(N)}.
\]

## Verification
The logical reduction does not depend on finite computation. The bundled verifier exhaustively checks, for \(3\le N\le9\), that labeled cyclic decompositions with no cycles of length \(1\) or \(2\) collapse under conjugation to exactly the restricted integer partitions of \(N\) into parts at least \(3\). It also checks the standard conjugacy-class size formula and an independent dynamic-programming count of the same restricted partitions.

These finite checks are regression tests for the combinatorial quotient only. The general proof is the conjugacy classification of permutations together with the source's uniform fixed-decomposition chamber estimate.

## Relationship to prior work
Kolpakov and Rivin's 2026 manuscript proves the fixed-combinatorics chamber bound \((AN)^{3N}\) and, in its link remark, multiplies by at most \(N!\) labeled cyclic decompositions, obtaining
\[
|\mathcal L_N|\le N^{4N+o(N)}.
\]
The present observation removes that extra factorial-scale loss for ordinary unoriented unordered links by quotienting the labeled decompositions by vertex relabeling before summation. The relevant quotient is exact: conjugacy classes of the decomposition permutations are cycle types, hence integer partitions of \(N\), and the restriction to genuine polygonal components removes parts \(1\) and \(2\).

Targeted searches for the resulting \(N^{3N+o(N)}\) link bound, for a cycle-type or integer-partition reduction of the source's \(N!\) factor, and for equivalent component-length formulations did not identify an already stated result. The recent preprint itself still states the \(N^{4N+o(N)}\) bound in its current author manuscript.

## Limitations
This is an upper-bound refinement only. It does not improve the known lower constructions for links and therefore does not determine a sharp leading exponent. It also inherits the source's semialgebraic chamber estimate; the new contribution is solely the exact quotient of the component-combinatorics factor for ordinary links.

The source is a recent preprint and may be revised. An unindexed later note could independently contain the same relabeling reduction.

## References
1. Alexander Kolpakov and Igor Rivin, *Discriminant Varieties for Stick Knots and Links*, arXiv:2608.01277v1, first posted 2026-08-02. The author manuscript's link remark gives the fixed-decomposition \((AN)^{3N}\) chamber bound and then the \(N!\) summation producing \(N^{4N+o(N)}\).
2. G. H. Hardy and S. Ramanujan, *Asymptotic Formulae in Combinatory Analysis*, Proceedings of the London Mathematical Society, 1918, DOI 10.1112/plms/s2-17.1.75.
