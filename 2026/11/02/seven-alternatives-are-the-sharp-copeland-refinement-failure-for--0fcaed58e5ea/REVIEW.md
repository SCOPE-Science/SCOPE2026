# Scientific review

## Correctness — PASS

The result is a finite, sharply scoped theorem. The explicit seven-vertex adjacency lists define one orientation per pair. The tournament-specialized DSR score is algebraically identical to equations (6)–(9) of the cited 2024 paper; in particular, the simplification of the partition-eligibility conditions accounts for both the bipartition and tripartition cases. The reference four-alternative worked example gives the exact source scores \((3,4,1,0)\). A complete C99 enumeration of all \(2^{\binom n2}\) labeled tournaments at every order \(2\le n\le7\) finds no failures for \(n\le6\), and \(5,040\) failures at seven. An independent matrix-based implementation returns the same first failure and total. A complete relabeling orbit contains \(5,040\) distinct members and matches the complete failure set. All loops are bounded and use exact integer operations. The certified conclusion is finite; no infinite implication is inferred from this computation.

## Originality — PASS with residual risk

The 2024 primary full text [1] directly poses the general Copeland-containment question, proving only the up-to-four result and noting a five-alternative check. The first-failure and complete-classification statement is not present there. The related 2025 journal abstract [2] still describes only the up-to-four guarantee. The distinct later DSR tournament solution [3] uses indicator-based placement rather than the exact 2024 home-plus-away score; its abstract does not state the present sharp counterexample. Its full text remained inaccessible, a nonzero residual bibliographic risk. Targeted mathematical research-record searches for the source, the precise conjecture, seven-candidate aliases, the witness code, exact failure count, and tournament refinements found only other voting-rule comparisons. Matching cardinality seven with results for Banks, covering sets or uncovered sets is not statement equivalence. These negative searches do not prove priority.

## Mathematical value — PASS

The original rule was explicitly proposed as a possible universal refinement of Copeland. The proof identifies the smallest genuine obstruction, classifies its entire first failure layer, and quantifies the failure rate exactly. The result distinguishes two conceptually different properties of a scoring rule—choosing within the uncovered set and choosing within the Copeland set. This is an interpretable, naturally motivated boundary, not an arbitrary slice selected after enumeration.

## Closest literature and limitations

The original exact formula is Hou 2024, Section 4, equations (5)–(9), and the conjecture appears in Section 6.3 and the conclusion. The 2025 and 2026 follow-ups are considered separately because their available descriptions do not determine the first-failure classification for the original formula; the latter's full text is a material access limitation. The claim does not extend to ties or to larger-order classification. No independent audit or external validation has been performed.

Self-review: passed. Independent audit: not yet performed.
