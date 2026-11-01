# Scientific review

## Correctness — PASS

The stated scope is precisely \(a,b\ge2\), one deleted cross-edge, simultaneous binary majority and retention on ties. The four-coordinate count reduction is exact at the configuration level, including individually retained bits on tied neighborhoods. The finite sign partition has three universal side-size signatures. All six unordered combinations are explicitly enumerated, and all binomial class multiplicities are symbolic rather than fitted to sampled sizes. Its exact polynomial output yields all equilibrium counts, recurrent states, two-cycle basins and the claimed sharp entry times. The comparison with undeleted complete bipartite graphs follows from strict-majority versus tie counts. Standalone `verify_defect.py` replays nine exact coefficientwise class identities; 861,184 quotient-compatibility checks, 63,504 directly enumerated bit configurations and 841 benchmark cases passed. No enumeration is used to replace the infinite proof.

## Originality — PASS, qualified

Tamuz and Tessler (arXiv:1307.4035, §3.7) explicitly considered an odd balanced complete bipartite graph with one deleted edge and proved a two-step stabilization property; this antecedent is **not** claimed as new. The remaining cross-parity classification, especially the even-even equilibrium halving, the size-two versus larger-even reversal in periodic basin response, and sharp three/four-update transitions for unequal sides, is not supplied by that work. The prior general threshold-network period-two result of Goles and Olivos and the graph-uniform voting-time bounds of Kaaser, Mallmann-Trenn and Natale do not imply these counts. The examined primary literature and publication searches were compared for explicit formula equivalence, aliases, stronger graph families, and matching tables. No direct coverage of the combined all-part-sizes result was located. A different historical formulation remains possible; a complete copy of Goles--Olivos (1980) was not available, although its abstract was inspected.

## Mathematical value — PASS

One edge is a minimal perturbation of an elementary highly symmetric network. The complete all-parameter census gives a novel distinction between orbit count (unchanged at one), fixed states (halved non-consensus excess for even-even sizes), and oscillatory-basin size (increase or decrease depending on the even side). The sharp size-two and parity boundaries give direct structural information beyond a generic period-at-most-two theorem; these are not routine rephrasings of a known fixed-point count.

## Limitations and closest literature

The first-public source date refers to the accessible Tamuz--Tessler preprint (2013-07-15), which establishes a genuine previously known subcase. No claim of independent validation is made; other prior sources may contain implicit special cases. This work does not address multiple deleted edges, directed or weighted networks, asynchronous updates, or all separate fixed-point basin sizes. The self-contained proof and reproducibility code are provided without any external certification.

Self-review: passed. Independent audit: not yet performed.
