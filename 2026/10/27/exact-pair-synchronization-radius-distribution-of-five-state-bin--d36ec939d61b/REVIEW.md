# Scientific review

## Correctness — PASS

The explicit ten-pair transition graph gives a finite, complete correctness argument for computing every prescribed-pair shortest merge length. Both exhaustive C++17 implementations independently enumerate all \(5^{10}\) ordered binary transition pairs and agree on each of the ten radius frequencies, \(1{,}702{,}240\) nonsynchronizing cases, and the \(240\)-member extremal set. The reverse implementation verifies that all extremizers form one orbit under the full state-and-letter symmetry. Source code, an independent direct witness checker, and a replay script are included. The sharp general upper bound and the classical witness are correctly attributed to prior work.

## Originality — PASS within examined literature

The closest source is M. Szykuła, *Synchronizing Automata: Open Problems* (2026), Sections 2.3–2.6. It gives the standard prescribed-pair upper bound and Černý tightness but no five-state distribution or equality-class census. M. de Bondt, H. Don, and H. Zantema, *Slowly synchronizing automata with fixed alphabet size* (2016), Section 4, census reset thresholds, which do not imply the distribution of worst prescribed-pair merger times. Related prior finite findings concern reset thresholds, unconstrained pairing, triple rendezvous, and reaching-diameter invariants rather than the radius defined here. Negative searches do not prove unique historical priority: an unindexed earlier pair-radius enumeration remains possible.

## Mathematical value — PASS

The prescribed-pair merge radius controls the hardest two-state synchronization instance and is central to pair-graph synchronizability algorithms. Its full labeled distribution gives a non-arbitrary benchmark for random binary five-state automata, an exact mean, a sharp finite tail, and an exhaustive orbit classification of all maximizers. Those facts are not implied by the already known quadratic upper bound or the global reset-length distribution. The result makes no unsupported claim for larger sizes.

Self-review: passed. Independent audit: not yet performed.
