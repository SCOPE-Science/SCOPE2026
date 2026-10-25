# Scientific review: integral torsion in a directed tournament Hom complex

## Correctness — PASS
The statement uses the standard directed multihomomorphism cells \(\Delta A\times\Delta B\times\Delta C\) for the three oriented edges of \(\overrightarrow C_3\). The full checker independently enumerates cells by common in/out neighborhoods and by extension from all directed triangle assignments. It obtains the exact cell counts \((165,495,330)\), verifies \(d_1d_2=0\) and one connected component, and performs 329 explicitly integral unit-pivot cancellations on the two-boundary. The one-column remainder has 33 entries of absolute value 33; hence the Smith factors are 329 units and a 33. The full boundary has rank 330, yielding no two-dimensional homology and a first homology group \(\mathbb Z\oplus\mathbb Z/33\mathbb Z\). Modular ranks at five primes independently check critical divisibility. The checker source in this package reproduces these computations without third-party dependencies.

## Originality — PASS on checked evidence
The closest foundational source, Dochtermann–Singh, arXiv:2108.10948, was materially inspected in its full open-access PDF, especially its construction of directed Hom cells and its tournament examples and questions. The surveyed material does not calculate \(\operatorname{Hom}(\overrightarrow C_3,P_{11})\). A mathematical-record result for \(\operatorname{Hom}(\overrightarrow C_3,R_9)\simeq S^1\) addresses a different tournament and has only a summary available for this comparison; it does not imply the eleven-vertex Paley calculation. Searches for alternative terminology including multihomomorphism, torsion, tournament, directed triangle, Paley eleven, and the invariants 33, 3, and 11 identified no statement covering the claim. The full text of the nine-vertex record and potentially unindexed results were not inspected; they remain risks, not asserted proofs of uniqueness.

## Value — PASS
The canonical smallest nontrivial doubly regular tournament beyond the order-seven case is a motivated target for a directed three-cycle Hom complex, whose topology extends graph-homomorphism reconfiguration theory. The explicit composite torsion order 33 gives both three-primary and eleven-primary obstructions invisible in rational homology and refutes a wedge-of-spheres expectation for this natural instance. This is an exact, complete homology calculation, not a random parameter slice or a conjectured infinite family.

## Boundaries
No claim is made about the full homotopy type, the fundamental group, universality of the phenomenon, or minimal torsion order. The review is a self-review of the proof and available literature and not an external independent validation.

Self-review: passed. Independent audit: not yet performed.
