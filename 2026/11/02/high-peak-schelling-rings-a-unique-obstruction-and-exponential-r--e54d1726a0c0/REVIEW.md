# Scientific review: high-peak swap Schelling games on rings

## Correctness — PASS

The strict payoff ranking follows from the stipulated single-peaked function, not from an arbitrary surrogate. Each legal swap is divided into the adjacent and nonadjacent cases; the updated same-type neighbor counts are \(1-k\) or \(2-k\), respectively. These two identities prove exactly the two forbidden-pattern mechanisms. The constructive proof handles the smallest population sizes and derives the sole six-vertex exception. The transfer matrix has a direct cyclic-word interpretation, and the asymptotic uses an explicit primitive Perron component and an entrywise smaller forbidden-triple matrix. Every integer matrix coefficient and characteristic polynomial was recomputed from the standalone verifier, and the direct exhaustive oracle independently matched the structural characterization for every colored ring of order three through fifteen. Finite tests support, but are not substituted for, the infinite proofs.

## Originality — PASS

The initiating 2022 paper, Bilò–Bilò–Lenzner–Molitor, Theorem 2, already establishes failure of equilibrium on the balanced six-cycle for peak above one half. That negative example is credited, not reasserted as new. The new statement is the *universal positive complement*, the if-and-only-if forbidden-factor characterization, exact labeled generating matrices, and an exponential asymptotic for stable-coloring rarity. The inspected source's Theorem 2 and ring-welfare sections do not contain those results. Its generic existence arguments at lower peaks do not imply them. The full published parent text was compared; the jump-game study uses vacancies and unilateral moves, whereas the earlier monotone swap model has a different utility ranking. A separate lower-peak ring classification with tied isolation/boundary utility does not imply the high-peak results. Searches for synonymous claims, binary-word formulations and dominating transfer-matrix results yielded no specific equivalent publication. Residual risk: an equivalent combinatorial characterization or enumeration may be implicit in specialist Schelling or symbolic-dynamics literature not found by the searches. No independent publication-priority certification is claimed.

## Mathematical value — PASS

The parent paper exhibits an obstruction to equilibrium even on degree-two graphs but leaves the reader without an all-size description of when that pathology occurs. Establishing that the six-vertex balanced case is the **only** obstruction is a natural and sharp classification, not an arbitrary small-parameter census. The exact transfer formula resolves the full equilibrium spectrum and exposes a complementary structural phenomenon: almost every permitted population split has an equilibrium but uniformly sampled colorings are exponentially unlikely to be stable. The Perron constant comes from the actual stability automaton and gives a reusable quantitative benchmark for dynamics or sampling on rings. These motivations and proofs are intrinsic to the model, independent of running code.

## Closest sources and limitations

- Bilò, Bilò, Lenzner and Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games* (2022), https://arxiv.org/abs/2204.12599 ; inspected full text, especially model, Theorem 2, ring welfare results, and conclusion.
- Friedrich, Lenzner, Molitor and Seifert, *Single-Peaked Jump Schelling Games* (2023), https://arxiv.org/abs/2302.12107 ; vacancy-jump variant, not a stronger high-peak swap theorem.
- Bilò, Bilò, Lenzner and Molitor, *Topological Influence and Locality in Swap Schelling Games* (2020), https://arxiv.org/abs/2005.02752 ; monotone swap utilities.

Only two colors, full occupancy, strict mutual exchange improvements, undirected simple cycles, and the specified strict single-peaked payoff class are covered. The theorem says nothing about convergence of arbitrary exchange paths or additional graph families. The remaining publication-priority risk is specialist coverage not identified in the inspected sources. Direct enumeration is a bounded check, not an infinite certificate.

Self-review: passed. Independent audit: not yet performed.
