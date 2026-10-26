# Scientific review

## Correctness — PASS

Every output word of length \(n\) is counted exactly once, through the product of four-pair predecessor relations. The existence of any directed cycle in that product is necessary and sufficient for its periodic bi-infinite output to have a predecessor, whose period may be a multiple of \(n\). The finite-state transition matrix gives exact \(P_r(n)\) for all \(n\). For each of 256 rules, an integer recurrence is tested at as many consecutive positions as its full reachable state dimension, so Cayley–Hamilton proves the recurrence at all periods. Identical initial terms and recurrences prove equality within classes, while pairwise different length-eight vectors prove separation. The standalone verifier executes successfully, with a separate expanded-phase graph enumeration as a cross-check. Risk: dependence on the exact finite computation; the raw tables and complete checker are included for reproducibility.

## Originality — PASS under inspected evidence

Manada–Kashyap (arXiv:0904.2375, especially Theorem III.10) establish general zeta computation for periodic-finite-type shifts, not a quantitative census of elementary CA images. Salo (arXiv:2209.13373, including image-type and periodic-preimage discussions) addresses split epicness and regularity, not the complete counting sequences. Earlier individual image zeta computations, including Rule 110, are included as *covered individual examples*, not claimed as new. The new claim is the all-256, 31-class exact partition and minimal eight-period fingerprint, which are not implied by the inspected statements. Risk: an equivalent unindexed compilation or an implicit specialization of general methods could predate the present result.

## Mathematical value — PASS

Spatial periodic-point counts and Artin–Mazur zeta functions are natural conjugacy invariants of symbolic dynamical systems. A complete exact spectrum across the canonical finite rule family, rather than a list of isolated examples, distinguishes 31 non-equivalent periodic-orbit signatures. The unexpected sharp finite fingerprint means period data through eight settle all later periodic-output counts in this family, despite some exact recurrence orders reaching 56. The sharp Rules 7/25 example demonstrates that the cutoff is substantive, not an arbitrary enumeration range. Scope: one-step spatial images; no claim about temporal dynamics or conjugacy classification.

## Closest literature and limitations

Manada and Kashyap, *The Zeta Function of a Periodic-Finite-Type Shift* (2009), arXiv:0904.2375v1; Ville Salo, *On von Neumann regularity of cellular automata* (2022), arXiv:2209.13373v1; Lind and Marcus, *An Introduction to Symbolic Dynamics and Coding* (1995), on general sofic zeta theory. The novelty assessment concerns the exact census and cutoff only. Priority uncertainty, possible unindexed tables, and the need for independent scrutiny remain explicit.

Self-review: passed. Independent audit: not yet performed.
