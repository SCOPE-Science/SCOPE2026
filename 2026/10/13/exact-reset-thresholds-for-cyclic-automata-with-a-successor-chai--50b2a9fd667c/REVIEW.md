# Scientific review

## Correctness — PASS
The transition domain and indexing are explicit, and the proof constructs all shortest reset lengths by optimizing inverse preimages of cyclic intervals. The critical nonstandard domination lemma checks \(A(I)\subseteq B(I)\) at the unique extension trigger and otherwise \(B(I)=I\) or \(B(I)\subseteq A(I)\); monotonicity of preimages turns these into a globally optimal greedy rule, not just a plausible strategy. The proof identifies \(\{k\}\) as an optimal target, enumerates each phase, gives the forward witness, and covers \(k=n-1\), zero remainder, and nonzero remainder. Independent finite exhaustive BFS and interval checks using the embedded `verify.py` returned `VERIFY_OK bfs_cases=105 bfs_states=1622619 interval_cases=53130 large_witnesses=1606`. The result for all integers follows from the argument rather than sampling.

## Originality — PASS, with priority risk
The primary PDFs of Rystsov–Szykuła (2023, §§3–4), Zhu (2024, §§1–3), Grech–Kisielewicz (2012, §§3–4), and Don (2016, §§2–4) were examined at their relevant definitions, theorem statements, and proof sections. Rystsov–Szykuła classify synchronizability in certain primitive and semiconstant families, not exact lengths of the nonidempotent chain letter. Zhu's general quadratic bound applies, but does not imply the exact two-parameter formula. Grech–Kisielewicz give the Černý upper bound for orientable automata, not equality for this family. Scientific-literature and published-record searches identified Černý \(k\)-avoiding thresholds and one-cluster censuses, neither of which subsumes this construction. Related finite and cyclic-reset results differ by objectives or transition maps; the historical claims checked do not cover this theorem. An unindexed derivation or specialized older treatment remains possible; no independence claim is made.

## Value — PASS
This is an exact, all-parameter shortest-reset classification of a natural deformation of the Černý automaton within the rank-\(n-1\), circular automaton class. The strict transition from idempotent one-state collapse to a nonidempotent successor chain has substantive effect on reset complexity: the whole two-parameter threshold and explicit optimal words are determined, including an asymptotic quadratic-to-linear regime change. The all-family lower-bound mechanism is a structural interval-dominance statement, rather than an arbitrary finite census or a small numerical improvement.

## Limits
Only the specified transition family is covered, not the general transitive-permutation group class; there is no classification of every optimal word. Computation is finite corroboration. An unindexed equivalent publication is a genuine originality risk. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
