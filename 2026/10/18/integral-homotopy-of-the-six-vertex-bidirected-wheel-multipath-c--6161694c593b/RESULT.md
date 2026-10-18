# Integral homotopy of the six-vertex bidirected wheel multipath complex

## Finding
Let \(G\) be the wheel on six vertices, with a five-cycle and one universal hub. Replace each of its ten undirected edges by the two oppositely directed arcs to obtain \(\overleftrightarrow G\). Let \(\mathcal X(\overleftrightarrow G)\) be the simplicial multipath complex: its vertices are the 20 arcs, and a set of arcs is a simplex precisely when it is a disjoint union of consistently directed simple paths. Then there is an **integral homotopy equivalence**
\[
\mathcal X(\overleftrightarrow G)\simeq
\bigvee^{2}S^{2}\vee\bigvee^{23}S^{3}\vee\bigvee^{10}S^{4}.
\]
In particular, all integral homology is free, and the nonzero reduced ranks are \(2,23,10\) in degrees \(2,3,4\), respectively. This is a homotopy assertion, not just a Betti-number computation.

## Assumptions and scope
Label the hub \(0\) and the rim \(1,2,3,4,5\) modulo five. The underlying undirected edges are \(\{0,i\}\) for \(1\le i\le5\), together with \(\{i,i+1\}\) for \(i\) modulo five. The arcs are ordered lexicographically by their ordered endpoint pairs. An arc subset is a multipath exactly when every vertex has indegree and outdegree at most one and the directed subgraph contains no directed cycle. The theorem concerns this particular bidirected wheel, not arbitrarily oriented wheels or a claimed infinite family.

## Proof
**1. Exact simplicial model.** A recursive extension enumeration and a separate partial-injection enumeration agree on all \(871\) augmented simplices. The numbers with \(0,1,2,3,4,5\) arcs are \(1,20,130,330,310,80\). The complex has dimension four and \(2910\) covering incidences in its augmented face poset. These figures are computed afresh by `verify_wheel_homology.py`.

**2. Integral cellular reduction.** The deterministic greedy matching in that program pairs \(408\) face-poset incidences. Reverse matched arrows in the full Hasse diagram and topologically sort its \(871\) vertices: the algorithm verifies acyclicity exhaustively, not probabilistically. The empty simplex belongs to a matched pair, giving one critical ordinary vertex; there are no other critical cells of dimension below two. The remaining critical-cell counts are \(12\) in dimension two, \(33\) in dimension three and \(10\) in dimension four. The associated signed integral algebraic-Morse differential \(d_3:\mathbb Z^{33}\to\mathbb Z^{12}\) has exactly ten unit Smith pivots and no nonunit pivot; \(d_4:\mathbb Z^{10}\to\mathbb Z^{33}\) is identically zero. These assertions are checked by integer-only elimination. Thus the space is simply connected and its integral homology is \(\mathbb Z^2,\mathbb Z^{23},\mathbb Z^{10}\) in dimensions two through four, respectively, without torsion.

**3. The attaching maps, not merely their boundaries.** Cancelling the ten integral degree-one three-to-two cellular pairs gives a three-skeleton homotopy equivalent to \(\bigvee^2 S^2\vee\bigvee^{23}S^3\). This is legitimate for a simply connected three-dimensional CW complex: the unit integer cellular matrix admits elementary homotopy cancellations after the corresponding basis changes, and the residual three-cell attaching classes are measured by their integral degrees in \(\pi_2(\bigvee^2 S^2)\). All ten four-cell attaching maps have zero degree onto every three-sphere, since \(d_4=0\). Their remaining possible components belong to
\[
\pi_3(S^2\vee S^2)\cong\mathbb Z\{\eta_1,\eta_2,[\iota_1,\iota_2]\},
\]
where \(\eta_i\) are the two Hopf generators and \([\iota_1,\iota_2]\) is the mixed Whitehead product. This decomposition is integral and torsion-free. The coefficients of these three components are detected by the integral cup products of degree-two classes evaluated on the four-dimensional cellular fundamental cycles (diagonal products detect Hopf coefficients, off-diagonal products the Whitehead coefficient).

The independent exact cup-product program `verify_wheel_cup.py` constructs two linearly independent integral degree-two cocycles in the original simplex basis, verifies their coboundaries vanish on **all 310** three-simplices, and constructs **ten integral four-cycles**, one above each critical four-cell, with zero original simplicial boundary. Every one of the four ordered cup pairings for every one of these ten cycles is **exactly zero**. Since the two cocycles form a rational basis of the rank-two integral degree-two cohomology, this vanishing implies all rational quadratic attaching coefficients vanish. Since \(\pi_3(S^2\vee S^2)\) is torsion-free, each integral attaching coefficient is zero as well. Thus every four-cell is homotopically free, yielding the asserted wedge of spheres.

## Verification
Execute the three embedded, standard-library-only programs together in the same directory:

`python3 verify_wheel_homology.py`

`python3 verify_wheel_cup.py`

`python3 direct_gf2_check.py`

The first gives `VERIFIED_BIDIRECTED_WHEEL_INTEGRAL_HOMOLOGY`; the second gives `ALL_INTEGRAL_CUP_PAIRINGS_ZERO`; the third independently computes all original simplicial boundary ranks over \(\mathbb F_2\), without using the Morse reduction, and gives `INDEPENDENT_DIRECT_GF2_BOUNDARIES_AGREE`. The full enumeration, integral elimination, chain lifts and cup products are recreated rather than assumed from supplied logs. The included `CERTIFICATE.txt` is a convenience record, not a substitute for code replay.

## Relationship to prior work
The 2022 foundational study *On the homotopy type of multipath complexes* (arXiv:2208.04656) defines and studies multipath complexes for several directed graph families. The 2026 *Multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670) analyzes bidirected **cycles**, without their universal hub. Neither directly includes the bidirected wheel, whose hub introduces additional compatible and cyclically prohibited path patterns. Published results about the ordinary discrete-Morse complex of a wheel concern a different simplicial complex with different vertices; they do not imply this theorem. An indexed-mathematics search and direct examination of these primary sources found no stated equivalent, but absence from the searched sources is not a proof of historical priority.

## Limitations
Only the exact six-vertex wheel is classified; no uniform result for all wheel sizes or equivariant representation is asserted. The cup calculation detects homotopy attaching invariants using an integral, rather than floating-point, finite chain computation, and the separate mod-two checks alone would not prove the claimed integral conclusion. Independent external proof review has not been performed.

## References
1. Caputi, Collari, Di Trani and Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public version 2022-08-09. https://arxiv.org/abs/2208.04656
2. Caputi, Collari and Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, 2026. https://arxiv.org/abs/2601.05670
3. Caputi, Collari and Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206. https://arxiv.org/abs/2110.11206
