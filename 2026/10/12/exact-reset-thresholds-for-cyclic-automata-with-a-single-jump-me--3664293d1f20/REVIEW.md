# Scientific review: exact reset thresholds for a directed cyclic jump-merge automaton

## Correctness — PASS
The domain \(n\ge2\), \(1\le h<n\), two fixed unit-cost directed letters, and reset definition are explicit. The proof checks the residue obstruction for \(\gcd(n,h)>1\), interval preservation under both inverse letters when coprime, the mandatory \(n-1\) growth events, and the \(n-h\) rotation gap between consecutive events. The constructed word meets the lower bound. A direct forward subset-BFS verifier confirmed all 66 cases through \(n=12\) and additional structural/witness computations. Finite searches are corroboration, not a substitute for the infinite argument.

## Originality — PASS, with bibliographic risk
Don (2016), Proposition 15, already proves that coprime excluded-to-contracted distance gives synchronization with a quadratic reset bound. Rystsov (2025), Theorems 4.4–4.5, gives the same construction on specialization and a broad synchronization criterion. The **new statement** is the matching lower bound for arbitrary words using exactly the directed cycle generator, yielding the exact parametric minimum; the gcd test and witness alone are not presented as novel. Volkov (2024) gives general primitivity conditions. Published-result, alias, and overlap comparisons found no dominating exact formula in the inspected sources. The 2000 and 2022 simple-idempotent papers remain primary-text access risks, so the originality assessment is qualified by that uncertainty.

## Value — PASS
A complete exact reset-threshold formula, not only a construction, settles a natural parameterized automaton family. It exhibits the sharp separation between \(R(n,1)=(n-1)^2\) and \(R(n,n-1)=2n-3\), and supplies a nontrivial geometric lower-bound method. This is mathematically meaningful even without a theorem for arbitrary circular automata.

## Literature and limits
Principal sources are Don (2016), Volkov (2024; preprint 2023), and Rystsov (2025). The claim is confined to one forward generator and one unitary letter; adding the inverse-cycle letter can shorten reset words. The theorem does not assert independent validation or complete coverage of unindexed literature.

Self-review: passed. Independent audit: not yet performed.
