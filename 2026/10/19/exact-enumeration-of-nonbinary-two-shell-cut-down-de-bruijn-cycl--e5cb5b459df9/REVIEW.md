# Scientific review: nonbinary two-shell universal-cycle enumeration

## Correctness — PASS

The directed graph and normalization are explicit: labelled symbols and edges, no quotient beyond cyclic rotation. Every allowed window corresponds to an edge, and each cyclic word is an Euler tour. The degree calculation and existence of a root-reaching directed tree prove the Eulerian hypothesis. Degree-two-weight vertices have forced outgoing zero-append arcs. Contracting those arcs gives a colored reduced Laplacian; splitting by color sums yields an upper-triangular difference block and a weighted one-dimensional index graph. The closed-interval obstruction for a high-index reflected step and the increasing-index argument for permitted lower-half reflected steps establish its complete tree count. BEST then gives the exact number. A full-graph Matrix-Tree computation and independently enumerated Euler tour orders agree in every listed test case; the program and output are embedded. Risks: the proof is for Hamming, not arithmetic, weight, and neither experiments alone nor finite checks imply the infinite assertion (which is separately proved).

## Originality — PASS within examined evidence

The closest original preprint, Mitchell–Wild (2026, arXiv:2607.22350), establishes existence for nonbinary weight bands without determining the number of cycles. Ruskey–Sawada–Williams (2012) addresses the binary framework. Fredricksen (1993) explicitly gives the binary weight-at-most-two count; the binary specialization is therefore excluded from the new claim. Li–Jiang–Lin (published online 2022) addresses binary weights at most two and a register-joining characterization. Chee et al. (2020) enumerate locally nonrepeating words subject to a different distance parameter, not exact prescribed Hamming-weight window sets. Its accessible abstract explicitly restricts the alphabet to binary and mentions only finite experimental enumerations. The nonbinary formula, particularly its color-difference determinant factor, is not implied by those visible claims. Searches of mathematical research records and overlapping prior claims found no equivalent enumeration. Main-text access to the 2022 paper was incomplete, and unrelated unindexed formulations remain a risk. The strongest originality claim is limited to \(q\ge3\), not the known \(q=2\) case.

## Value — PASS

This answers the natural enumeration problem left after existence of weight-constrained cut-down de Bruijn cycles on arbitrary alphabets. It supplies a closed form simultaneously for every nonbinary alphabet and span, with exact normalization, nontrivial factorial and exponential dependencies, and a structural explanation through symmetry decomposition. It is not a numerical table, a relabeling, or an arbitrary slice. The result does not purport to count broader weight ranges or extra symmetry orbits.

## Literature and verification limits

Primary literature inspected: full text of Mitchell–Wild (2026); substantive full text of Ruskey–Sawada–Williams (2012); introduction and weight-two enumeration of Fredricksen (1993); abstract and accessible appendix of Li–Jiang–Lin (2022/2023), with its subscription main section unavailable. Exact source citations are in RESULT.md and AUDIT.json. All computational evidence is finite. No independent scientific review or external certification has been performed.

Self-review: passed. Independent audit: not yet performed.
