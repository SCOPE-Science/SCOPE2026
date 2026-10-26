# Self-review: Minimum signed double Roman functions on even prisms

## Correctness — PASS

The candidate theorem counts all functions with the four permitted labels on position-distinguished vertices of \(C_m\square K_2\), for even \(m\ge4\). The lower bound is reconstructed by the stated quarter-unit discharging: every positive vertex has at most two negative neighbors and retains at least \(1/2\); every negative vertex has at least two positive neighbors and receives enough to retain at least \(1/2\). Equality forces exactly the two local vertex types described as (E+) and (E−). Reversing the argument verifies feasibility, so the conditions are necessary and sufficient. The alternating \((2,2),(-1,-1)\) cycle proves attainable minimum weight \(m\).

The 256-state transfer counts rooted cyclic column sequences bijectively; the position labels preclude division by cycle length. The script constructs all transitions from the mathematical predicate, finds recurrent components of sizes \(22,4,4,4,2\), verifies the core characteristic polynomial \(t^{14}(t^8-7t^4+1)\) by exact integer Newton identities, and checks the remaining simple directed cycles. Eigenvalue power sums then establish the claimed recurrence for all even lengths. Unrestricted optimum-weight counts and a direct smallest-case enumeration were independently cross-checked, but those finite tests are not substituted for an infinite proof.

## Originality — PASS, with residual risk

Iurlano–Zec–Djukanovic–Raidl, arXiv:2308.01109v1, Theorem 6, determine only the scalar minimum weight of even prisms. The main arguments, the generalized Petersen section, and the appendices were materially inspected. They do not give a census of the entire optimizer set. The 2019 foundational signed-double-Roman works provide definitions, bounds and other graph families, not this cycle-of-columns enumerator. Searches also contrasted standard Roman, Roman \(\{3\}\), and ordinary domination counts, none of which has the same local constraint system. The corresponding indexed mathematical findings returned closest records on Roman \(\{3\}\) complete prisms and signed Roman multipartite graphs, which change both the graph family and the labeling rules. No covering theorem or exact table was located. Residual risk: some independent derivation may encode the same local transfer by other cyclic-word terminology; a failed search cannot prove novelty.

## Value — PASS

Minimum domination weights do not determine optimizer multiplicity. The exact labeled census is a natural equality-case invariant attached to the published prism family and demonstrates a sharp modular dichotomy: exactly two optima at all orders congruent to two modulo four, against an exponentially growing integer-recurrence family at orders divisible by four. Its finite-state equality characterization is useful for later extensions to perturbed prisms or constrained label sets. This is stronger than a routine numerical improvement or isolated small-case count; it is an infinite-family classification.

## Scientific limitations and priority caveats

The theorem is restricted to even prisms and position-distinguished labelings. Odd-prism optimizer counts, automorphism orbits, and nonminimal configurations remain open in this treatment. Integer characteristic-polynomial verification is reproducible and exact but has not been independently audited; priority searching cannot eliminate every unpublished or differently named equivalent.

Self-review: passed. Independent audit: not yet performed.
