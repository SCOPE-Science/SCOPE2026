# Review: finite \(\mathsf{S5}\) bisimulation witness census

## Correctness — PASS

The full argument starts from the atomic, forth and back clauses and proves that each **active pair** of accessibility classes must have identical sets of atomic profiles and a spanning bipartite cover for each profile. The converse construction verifies the same clauses explicitly. Because active pairs are independent, ordinary witness counts factor. The proof separately checks the two nested levels of inclusion-minimality; this is important because a global witness can be minimal without having only one active class pair. Inclusion-exclusion proves the all-cover coefficients, and the degree-one-endpoint characterization proves the star-forest exponential formula and recurrence for minimal covers. The empty compatibility graph, isolated class vertices and unequal cardinalities are handled. The accompanying independent brute-force checker compares the four derived counts with direct clause tests on 2,504 pairs of small models; its output is `ALL_CHECKS_OK model_pairs=2504 profile_cases=5`. The computation checks finite instances and does not replace the universal proof.

## Originality — PASS within inspected evidence

Burrieza–Soler-Toscano–Yuste-Ginel, *A meta-modal logic for bisimulations* (arXiv:2507.15117), develops bisimulation and its logical expressibility, but the inspected full text through its conclusions does not supply a counting or minimality formula for relations between two fixed S5 models. Van Ditmarsch–Fernández-Duque–van der Hoek, *On the definability of simulation and bisimulation in epistemic logic* (2014), defines total bisimulation and proves a logical definability result, not enumeration of witnesses. Conventional edge-cover and star-forest combinatorics are openly acknowledged ingredients, not separately claimed as new. Searches for counting, weighted bisimulation, minimal witnesses, component compatibility, and competing stronger formulations found no covering result among inspected sources. Different terminology or less accessible work could imply the theorem; absence of a retrieved result is not proof of absolute novelty.

## Mathematical value — PASS

The number of bisimulation witnesses is a natural quantitative invariant for comparing fixed finite epistemic models, while ordinary results usually ask only whether witnesses exist or whether bisimilarity is definable. The structural theorem gives four all-size exact counts, separates partial from global witnesses, and exhibits the distinctive **two-stage star-forest** condition for inclusion-minimal global witnesses. Its arbitrary class multiplicities and atomic-support patterns include both disconnected and connected S5 frames and rule out reductions based only on world counts. It does not claim a general theorem for multiple agents or arbitrary frame relations.

## Closest literature and residual risks

The exact bisimulation definition and relevance of relation quantification are in the 2025–2026 meta-modal paper; the precise totality condition and definability context are in the 2014 epistemic-logic article. Graph edge-cover identities are standard, but these references do not state the four weighted finite-model formulas. An older enumeration of finite bisimulation relations or a general relational combinatorics theorem with equivalent implications remains possible; no exhaustive priority claim is made. Verification remains internal and no independent validation has occurred.

Self-review: passed. Independent audit: not yet performed.
