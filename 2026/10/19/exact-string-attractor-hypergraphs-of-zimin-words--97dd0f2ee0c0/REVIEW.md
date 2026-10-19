# Scientific review: Zimin-word string attractors

## Correctness — PASS

The exact factor-transport lemma follows from the ruler-word identity \(Z_n[j]=1+\nu_2(j)\): after excluding letters larger than \(k\), each component is a copy of \(Z_k\). A factor with maximum letter \(k\) must stay within one component, and its occurrence can be transferred to every component, always crossing that component's unique \(k\). Thus the entire occurrence class of \(k\) lies in the factor's coverage. Singleton factors supply the reverse, exact set of minimal coverage constraints. The independent-choice count gives the generating polynomial, and two nearest high-letter positions supply the sharp span bound. Explicit boundary cases \(n=1,2\) are handled. `check.py` independently enumerates factor coverages and all minimum-cardinality attractors through \(n=6\), including the span refinement; this finite run is corroboration, not the infinite proof.

## Originality — PASS on examined evidence

The October 2026 work of Faro, Marino, and Pavone gives the complete coverage antichain and arbitrary-cardinality certificate for Thue--Morse words, with \(8n-22\) constraints. Banbara and colleagues describe minimum-cardinality attractors for Fibonacci, period-doubling, and Thue--Morse words. These do not cover the Zimin family: their occurrence transport and position classes are structurally different, and their results do not imply that every Zimin factor is attracted by any selected occurrence of its maximum symbol. Béal, Crochemore, and Romana give general checking/construction algorithms but not an exact Zimin enumeration. Connor studies Zimin-instance distribution rather than factor-attractor coverage. Targeted phrase and concept searches did not reveal an exact classification or the all-size factorized enumerator. The most relevant retrieved published-record descriptions instead concern other morphic or pseudostandard families.

The originality assessment is a best-knowledge comparison, not an assertion of exhaustive indexing. Further semantic-record searches suffered intermittent service errors; differently phrased or unindexed coverage remains possible. These risks do not supply a known prior implication or negate the observed object-specific gap.

## Value — PASS

This is a complete classification of *arbitrary-cardinality* attractors and of the canonical minimal factor-coverage hyperedges for a canonical recursive pattern word. It collapses the globally quantified factor-hitting condition to precisely \(n\) irredundant one-letter tests, yields the full attractor-size polynomial, determines the complete minimum-solution count, and gives a sharp minimum-span refinement. In contrast with the nontrivial \(8n-22\) canonical constraints of Thue--Morse words, Zimin words exhibit a partition-transversal attractor hypergraph. This exact difference is mathematically motivated by recent attempts to classify all attractors and all minimal factor coverages, rather than a selected arbitrary finite statistic.

## Limitations

Only literal finite Zimin words on distinct letters are covered. General pattern morphic images may violate the transport lemma. Finite tests through order six do not substitute for proof. An independent scientific audit has not been performed, and prior-literature coverage cannot be guaranteed beyond inspected records.

Self-review: passed. Independent audit: not yet performed.
