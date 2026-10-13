# Scientific review

## Correctness — PASS

For a fixed alphabet of size \(q\), the proof and `verify.cpp` exhaustively generate every square-free restricted-growth word up to the reported minimal length. The program only adds a symbol if no square is created at the new suffix, a sufficient and necessary incremental condition. It checks all insertion gaps, every possible square length and every feasible factor start; each candidate square has exactly one inserted-letter position, which uniquely determines the forbidden symbol. Words missing a symbol cannot be locally blocked, justifying early use-of-all-symbols pruning. Terminal counts are \(6936\) canonical square-free words for \(q=5\) and \(6480694\) for \(q=6\), with respectively two and one canonical blocked words. Neither has a preceding blocked representative. A separate Python substring algorithm verifies every claimed witness insertion. The explicit disjoint-alphabet Zimin concatenation proves constructive upper bounds. These together prove exactly the stated finite claims; they do not imply global optimality for larger alphabets.

## Originality — PASS, with priority risk

The 2022 Dębski–Grytczuk–Pawlik work defines bifurcate words, studies complete trees and already obtains an obstruction on four letters at length six (Theorem 7). The 2021 Grytczuk–Kordulewski–Pawlik paper analyzes Zimin words with unextendable end gaps. Neither inspected paper states the exact first blocked lengths \(10\) and \(14\) for five and six letters or their complete shortest-word classifications. The 2026 Hng–Rathke result concerns the much stronger all-gaps extremality property; its abstract and definition do not cover the one-gap statement. The consulted public literature did not disclose an equivalent five/six-letter census. These observations support originality but cannot exclude unindexed equivalent work. The known four-letter and Zimin upper-bound components are explicitly excluded from the originality claim.

## Mathematical value — PASS

Bifurcation and complete insertion trees are central to the motivating source's extension questions. The first length at which universal bifurcation fails is a natural boundary invariant: an exact cutoff distinguishes guarantees for every word from existence of a single obstruction. The two previously unlisted five- and six-letter thresholds and the uniqueness classification are substantial, complete natural finite cases, with more than six million canonical candidates ruled through the six-letter cutoff. The precise values also identify the first obstructions under the smallest alphabets where completely extremal words are ruled out by later theory. These are not arbitrary parameter slices or merely a code execution record; the Zimin mechanism provides a common structural explanation.

## Closest literature and limits

- Dębski, Grytczuk, Pawlik (2022), arXiv:2209.08507v1, Theorems 3 and 7, and bifurcate tree definitions. The four-letter construction is prior work.
- Grytczuk, Kordulewski, Pawlik (2021), arXiv:2104.04841v3, Section 3.2, Zimin extension properties. One-sided Zimin blocking is prior work.
- Hng, Rathke (2026), arXiv:2608.10591v1, extremality across all gaps, not single-gap failure.

Residual risks: unindexed previous finite computations; the newer paper's complete technical proof has not been checked, though its main theorem has a distinct implication direction. Values above six symbols are not resolved.

Self-review: passed. Independent audit: not yet performed.
