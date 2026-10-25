# Self-review

## Correctness — PASS

The barycentric orbit-complex construction correctly models geometric fixed points, not merely vertexwise fixed sets or invariant homology. The weight-three obstruction is necessary. All binary linear subspaces whose nonzero words have weight at most two are classified: rank-one generators of weight one/two, rank-two coordinate planes or parity planes supported on three coordinates. The explicitly calculated orbit edges are respectively the hypercube graph and the empty graph; the general proof covers all dimensions \(n\ge3\). The executable finite test independently reconstructed all admissible subgroup orbit complexes for \(2\le n\le6\) and passed 125 instances. There are no missing boundary cases in the stated range.

## Originality — PASS, qualified

Adamaszek–Adams [1] establishes the nonequivariant wedge-of-three-spheres classification, and Galetto–Montaño–Wellner [2] establishes the full characteristic-zero homology **representation**. Neither inspected theorem states or implies the complete geometric fixed-space homotopy classification; representation characters determine single-element Lefschetz numbers, not fixed-space dimensions and attaching data, nor common fixed-point topology for rank-two subgroups. Closest database hits concerned homology representations of scale-two Čech complexes rather than Rips fixed spaces. Earlier scientific records giving translation characters for this Rips complex were treated as covering the character/Euler data, **not** as fresh novelty. Unindexed equivalent work remains possible, and the full text of the potentially related quotient-thickening study [3] was not accessible.

## Value — PASS

A complete infinite-parameter geometric fixed-point classification under every subgroup of the natural translation group is a structural equivariant homotopy invariant: it distinguishes empty sets, graphs with exponentially growing integral first homology, and finite point sets. For \(n\ge4\), the ambient complex has no reduced degree-one homology, yet every weight-one or weight-two translation has a fixed graph with nontrivial degree-one homology. The rank-two case probes simultaneous stabilizers unavailable from elementwise homology characters. This is not a reformulation of a Betti number or a prescribed finite-parameter slice.

## References and limits

[1] Adamaszek–Adams, arXiv:2103.01040, Theorem 1. [2] Galetto–Montaño–Wellner, arXiv:2606.20784, Section 5. [3] Adams–Heim–Peterson, arXiv:1911.00732 (abstract only). Proof and finite checks are reproducible in the accompanying files; independent external validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
