# Scientific review

## Correctness

**PASS.** The bit recurrence is read directly from the 16-bit diagram, with its conditionally complemented bits and final XOR feedback. Rank-nullity proves the output-parity hyperplane and absence of transients longer than one for every word length at least three. An explicit characteristic-polynomial elimination, two irreducibility gcds, and three primitive-order residues establish the exact orbit partition at sixteen bits. The standalone verifier independently executes all \(65536\) states and binary-polynomial arithmetic; it is not substituted for the algebraic proof.

## Originality

**PASS, with residual risk.** The originating open-access paper was materially inspected in Sections 2.2, 3.1 and 3.2, Figure 2, its discussion of statistical tests and its conclusions. It provides the circuit but not the rank-15 primitive cycle statement or forbidden output parity. General LFSR theory does imply maximum cycle length from a primitive polynomial but does not identify this concrete tent-circuit realization, its one-step kernel, or the particular polynomial. The later Nardo thesis has overlapping circuit material, but its complete relevant chapter was not obtained; this is an explicit priority uncertainty. Targeted equivalent-formulation and mathematical-record searches did not identify a stronger source covering the complete circuit-specific result; absence of search hits is not proof of uniqueness.

## Value

**PASS.** The article explicitly evaluates this circuit as a pseudo-random generator using sample-based tests and contrasts it with linear-feedback registers. The finding identifies an exact circuit-level linear restriction, a maximum-length orbit in a 15-dimensional subspace, and an exactly unreachable half of the 16-bit alphabet. These are natural dynamical invariants of the implementation, make a scientifically consequential distinction between full-resolution and coarse-resolution statistics, and supply a complete benchmark for any hardware reconstruction. No claim is made that the original statistical tests necessarily fail.

## Principal literature and limits

Nardo et al., *Electronics* 12 (2023), 1953, DOI: 10.3390/electronics12081953; standard primitive-LFSR theory as presented in N. P. Smart's *Cryptography: An Introduction*; and Nardo's 2024 PhD thesis (partial relevant chapter access). The complete exact result is restricted to the stated gate transition, not arbitrary circuit variants or continuous tent dynamics. Specialist comparison and independent audit have not occurred.

Self-review: passed. Independent audit: not yet performed.
