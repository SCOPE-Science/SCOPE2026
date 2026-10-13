# Scientific review

## Correctness — PASS
The counting formula is proved by a complete partition according to the number of initially white vertices. Four or more white vertices cannot be forced, using the prohibition of four-cycles in a tree; two-white failures are exactly sibling leaves; and three-white successful sets correspond to one or two valid witness centers. The unique double-counts are the unoriented five-vertex paths, so their correction is exact. A separate direct zero-forcing implementation checks each coefficient in 20,110 labeled or seeded trees, covering 3,134,704 candidate initial-white subsets. The executable is included and rerunnable. Bounds: graph order at least five and ordinary forcing only.

## Originality — PASS, with residual risk
Boyer et al. (arXiv:1801.08910, 2018) define the polynomial and enumerate other graph classes. Curl et al. (arXiv:2206.03932, 2022) establish the minimum zero-forcing number for complements of nonstar trees and stars, but do not provide the complete polynomial or the five-vertex-path correction. A separately retrieved published study of zero-forcing polynomials compares nonpath trees **themselves**, not their complements, and does not imply this formula. Searches for complement-tree enumerators, leaf-twin correction formulas, minimum-set multiplicities and equivalent five-vertex-path expressions uncovered no dominating result. This is not a proof of global bibliographic uniqueness; unindexed equivalent formulas remain a risk.

## Value — PASS
The result refines a known extremal invariant for the unrestricted class of tree complements to a complete polynomial, counts all minimum sets exactly, gives a linear-time method, and detects branching structure not fixed by degree sequence. The correction by the number of five-vertex paths is essential; omitting it systematically double-counts minimum sets. This is neither a single parameter instance nor a generic substitution into an existing polynomial.

## References and limitations
Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910 (2018). Curl et al., *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932 (2022). Scope: simple trees of order at least five; no independence verification or claim of an exhaustive novelty certificate. Finite tests complement, but do not replace, the proof.

Self-review: passed. Independent audit: not yet performed.
