# An integral mixed sphere wedge for the Paley-seven multipath complex

## Finding

Let \(P_7\) be the quadratic-residue Paley tournament on \(\mathbb F_7\). Its multipath complex \(X(P_7)\), with the directed arcs as vertices and vertex-disjoint unions of directed paths as simplices, has integral homotopy type

\[
X(P_7)\simeq \bigvee^{15}S^3\vee\bigvee^{38}S^4\vee\bigvee^{24}S^5.
\]

Thus its reduced integral homology is free, of ranks \(15\), \(38\), and \(24\) in degrees \(3\), \(4\), and \(5\), respectively, and zero in other degrees. This is a complete homotopy calculation for this specified tournament; it is not a claim about every Paley or doubly regular tournament.

## Assumptions and scope

Represent the vertex set as \(\{0,1,\ldots,6\}\), and orient \(u\to v\) if and only if \(v-u\pmod7\in\{1,2,4\}\). There are precisely \(21\) directed arcs, ordered lexicographically by \((u,v)\). A set of arcs defines a simplex if every vertex has indegree and outdegree at most one in the selected directed subgraph and no directed cycle occurs. Isolated vertices are harmless. The empty face is included conventionally, but the reported face vector counts nonempty faces.

The calculation is integral unless a coefficient field is explicitly displayed. No identification is made with directed flag, directed-path-homology, directed Hom, or out-neighborhood complexes: those are distinct constructions.

## Proof

**1. Exhaustive finite model and acyclic Morse matching.** For each arc subset, test the indegree/outdegree constraints and absence of directed cycles. Exactly \(2940\) nonempty faces arise, with numbers of faces in dimensions \(0,\ldots,5\) equal to

\[
(21,168,630,1113,819,189).
\]

The independent checker in `paley7_multipath_verify.py` implements this definition directly using the \(21\) lexicographically ordered arcs. It constructs a deterministic patchwork matching: in the consecutive arc-index order

`7,18,17,4,11,15,10,9,1,13,0,20,19,3,12,5,16,8,6,14,2`,

toggle the chosen arc between a live lower face and its live coface whenever both exist, and then remove the pair. This yields exactly \(1424\) pairs. An independent topological sort of all \(2940\) vertices of the fully oriented Hasse diagram establishes acyclicity: reverse each matched incidence, leave every unmatched incidence directed downwards, and visit all nodes without a directed cycle. The critical cell counts are one in dimension \(0\), \(22\) in dimension \(3\), \(45\) in dimension \(4\), and \(24\) in dimension \(5\), with none in any other dimension.

**2. Exact integral Morse boundary and free homology.** Equip every simplex with the ordering inherited from the lexicographic arc indices. For a matched lower cell \(\sigma\subset\tau\), let \(\varepsilon\in\{\pm1\}\) denote its incidence in \(\partial\tau\). The gradient projection to critical cells is recursively

\[
P(\sigma)=-\varepsilon\,\sum_{\rho\subset\tau,\,\rho\ne\sigma}[\tau:\rho]P(\rho),
\]

with \(P(\gamma)=\gamma\) on critical cells and \(P(\tau)=0\) on matched upper cells. Acyclicity makes this recursion well-founded. Applying \(P\) to ordinary signed simplicial boundaries gives the actual integer Morse differentials. The only possibly nonzero one is \(\partial_4:C_4\to C_3\): its \(22\times45\) matrix contains \(67\) nonzero entries, each \(\pm1\), and has Smith normal form with exactly \(7\) unit invariant factors, all remaining entries zero. The entire Morse map \(\partial_5:C_5\to C_4\) is zero. Unimodular row and column elimination, with an explicit assertion of the exact final diagonal, verifies these statements. Consequently the reduced integral ranks are \(22-7=15\) in degree \(3\), \(45-7=38\) in degree \(4\), and \(24\) in degree \(5\), and there is no torsion.

**3. The attaching maps of the five-cells vanish.** Cellular elimination of the seven unit \((3,4)\)-cell pairs yields a CW model whose four-skeleton has the homotopy type \(\bigvee^{15}S^3\vee\bigvee^{38}S^4\). The attaching homotopy class of each of the remaining \(24\) five-cells lies in

\[
\pi_4\!\left(\bigvee^{15}S^3\vee\bigvee^{38}S^4\right)
\cong(\mathbb Z/2)^{15}\oplus\mathbb Z^{38}.
\]

There are no Whitehead-product terms in this degree. The integral cellular boundary \(\partial_5=0\) forces every free \(\mathbb Z\)-component to vanish. It remains **essential** to exclude the possible stable Hopf-element components in \((\mathbb Z/2)^{15}\); integral homology by itself does not do so.

For this purpose the verifier constructs \(15\) explicit degree-three mod-two cocycles from the chain projection of part 2, checks them against every ordinary degree-four simplex, and checks that their cohomology classes are independent modulo the rank-\(482\) coboundary space. It then evaluates the standard simplicial cup-one square \(\alpha\smile_1\alpha\) on every ordered five-simplex, using the three Alexander–Whitney face-pattern pairs

`((0,3,4,5),(0,1,2,3))`, `((0,1,4,5),(1,2,3,4))`, `((0,1,2,5),(2,3,4,5))`.

Each resulting degree-five cocycle is verified, by exact mod-two row reduction, to belong to the rank-\(165\) degree-five coboundary space. Therefore

\[
Sq^2:H^3(X(P_7);\mathbb F_2)\longrightarrow H^5(X(P_7);\mathbb F_2)
\]

is the zero operation. In a wedge of three- and four-spheres with attached five-cells, \(Sq^2\) detects precisely these mod-two Hopf attaching coefficients (the attaching mapping cones of \(\eta:S^4\to S^3\) have nonzero \(Sq^2\)). All five-cell attaching classes are therefore nullhomotopic. This proves the asserted full integral sphere wedge, not merely its Betti numbers.

## Verification

Run `python3 paley7_multipath_verify.py` using a Python 3 standard-library installation. The code is fully self-contained and checks the defining graph, every admissible face and boundary, every Morse pair and directed Hasse incidence, exact integral unit-Smith reductions, and the vanishing of \(Sq^2\) on a complete degree-three basis. The recorded deterministic output is in `verification_output.txt`; its concluding marker is `PALEY7_MULTIPATH_INTEGRAL_HOMOTOPY_VERIFIED`. As an independent consistency check, ordinary degree-one-through-five mod-two boundary ranks are \((20,148,482,616,165)\), reproducing the claimed Betti numbers directly. This is exhaustive finite computation plus the explicit obstruction-theoretic inference above, not extrapolation from small examples.

## Relationship to prior work

Caputi, Collari and Di Trani introduced and studied multipath complexes and related path posets in [1]. The later work of Caputi, Collari, Di Trani and Smith [2] computes important families, including transitive tournaments (its theorem for transitive tournaments); the Paley tournament here is a nontransitive doubly regular tournament and is not a member of that family. The present calculation specifies the integral homotopy type of a different, highly symmetric target and supplies a direct certificate for the potential Hopf attaching obstruction. Accessible database and published-source comparisons did not identify an equivalent result, although absence from a search is not proof of absolute priority.

## Limitations

The result applies only to the specified seven-vertex tournament and the standard multipath-complex definition, not to all tournament orders or all digraph multipath complexes. It does not classify equivariant homotopy, ring structure, integral cohomology operations beyond those used here, or higher-order Paley tournaments. The self-review is reproducible but is not an independent external mathematical audit. Unindexed or inaccessible prior results remain a bibliographic risk.

## References

[1] L. Caputi, D. Collari and S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206, first posted 2021-10-21. https://arxiv.org/abs/2110.11206

[2] L. Caputi, D. Collari, S. Di Trani and J. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656, first posted 2022-08-09. https://arxiv.org/abs/2208.04656
