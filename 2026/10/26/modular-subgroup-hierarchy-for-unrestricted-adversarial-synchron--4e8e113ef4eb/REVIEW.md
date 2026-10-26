# Self-review: modular subgroup hierarchy for cyclic adversarial synchronization

## Correctness — PASS
The proof verifies that the operator \(\Phi(K)=\{d:f(x+d)-f(x)\in K\ \forall x\}\) is an additive subgroup operator and is monotone. Exact pair-game induction handles arbitrary initial adversarial words and proves equivalence of merging a difference in \(t\) Alice turns with its membership in \(H_t\). Reduction of a full state set by repeated winning pair strategies proves the forward direction; an adversarial rotation invariant on any difference outside the stable subgroup proves necessity. The semiprime subgroup lattice reduces the winners to periodic maps with single residue-class output, and elementary inclusion-exclusion counts them. A separately coded exhaustive powerset-game attractor matches the subgroup criterion on all \(n^n\) maps for \(2\le n\le6\), and a nontrivial three-stage chain is checked at \(n=8\).

## Originality — PASS within examined evidence
Lipin–Volkov (arXiv:2601.18362, Sections 2–3 and 5) gives the unrestricted game and general relation algorithms, but the cyclic-group subgroup hierarchy, sharp prime/composite dichotomy, and complete semiprime map enumerator are not stated there. Singh–Raj (arXiv:1808.01711) concerns ordinary circular-automaton synchronization and cannot by itself settle adversarial winning. Searches for cyclic game subgroups, prime/composite obstruction and semiprime counts did not yield an equivalent or stronger result; related finite automaton thresholds and prior finite four-state game counts have different hypotheses and conclusions. Residual risk: relevant unindexed specialization or unpublished equivalence.

## Mathematical value — PASS
The exact all-order criterion turns an unrestricted strategy game into arithmetic of divisors with a provably terminating small subgroup hierarchy, and the prime/composite boundary and semiprime closed enumeration give genuinely structural families, not a single parameter example. It resolves a natural test class of the recently introduced adversarial model and exposes a strict difference from ordinary synchronization. The two-letter cyclic assumption is essential; broader automata and closed enumeration for orders with three or more prime factors remain open here.

Self-review: passed. Independent audit: not yet performed.
