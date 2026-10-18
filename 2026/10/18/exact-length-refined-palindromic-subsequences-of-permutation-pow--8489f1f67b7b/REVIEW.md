# Scientific review

## Correctness — PASS

For every \(q\ge2\), \(m\ge1\), and permutation \(P\), the greedy subsequence lemma gives the exact minimum number of periods \(1+d(v)\). Mirrored adjacent comparisons in a palindrome contribute exactly \(t+e\) weak descents for both parities, including a central equal comparison in even length. Enumerating first halves by their equal edges proves the two formulas without double-counting distinct words. Summation by minimum period count proves the rational bivariate generating function, and coefficient extraction gives the recurrence and extremal length. The standalone checker independently compares exhaustive position-subset enumeration against the spectrum for 17 small parameter pairs and interval dynamic programming against the totals for 138 further cases. Finite checks corroborate; the all-parameter proof is the greedy/mirror argument.

## Originality — PASS within examined sources

The exact binary alternating-word maximum-length special case was already observed by Müllner and Ryzhikov (2019) and is credited. The original full text studied palindromic length bounds, not exact distinct counts by each length. Brodal, Fagerberg, and Rysgaard (2024) address LPS algorithmic recovery, not the distribution. Amarilli and colleagues (2025) study regular-language-constrained subsequence optimization; such a result does not imply an exact palindromic spectrum in a nonregular language. The 2017 palindromic subsequence automata article represents all palindromes of any input, but its accessible abstract/preview does not assert this closed-form periodic family; its complete text was inaccessible, a significant remaining originality risk. The published-result comparisons checked related palindromic-factor, subsequence-universality, and palindromic-duplication work: those assertions do not imply the theorem here. Search failure alone was not used as proof of novelty.

## Value — PASS

The result determines a natural two-parameter infinite family at every length, not just longest length or one small parameter. It supplies an exact distribution, total-count recurrence, exponential growth rate, and a simple if-and-only-if combinatorial characterization usable as a benchmark in palindromic subsequence counting and automata implementations. These conclusions go materially beyond a known binary maximum-length observation and a generic dynamic-programming algorithm.

## Closest literature and limits

Closest primary sources: Müllner–Ryzhikov (2019), Brodal–Fagerberg–Rysgaard (2024), Amarilli et al. (2025), and Hasan–Islam–Rahman–Sen (2017). The original 2017 automata article was available as abstract and publisher preview only; an implicit specialization or different-name count remains a risk. Unindexed equivalent formulas cannot be ruled out. The code is finite corroboration, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
