# Self-review

## Correctness (C) — PASS
The greedy source-run index is derived from first-available subsequence embedding. For a candidate run of length \(t\), exactly \(\lceil t/2\rceil\) source blocks of that symbol are necessary; alternating candidate symbols cross exactly one intervening source block. This proves the embedding index \(\Phi=|u|-e+s\). A deletion in an even run does not change \(\Phi\), excluding such runs from minimal absences. The remaining deletion cases give the exact three conditions. Odd-part composition generating functions include the exceptional one-run first-and-last-long case, and yield the stated \(r\ge2\) spectrum; \(r=1\) is checked directly. The independent enumerator and scanner agree on 412,292 exact finite candidate decisions. Remaining mathematical risk is limited to the usual possibility of an unrecognized proof error, not an unverified computational premise.

## Originality (O) — PASS, with priority uncertainty
Kosche–Koß–Manea–Siemer, arXiv:2108.13968, Section 3, treat MASs structurally and produce an exponential lower bound for a periodic large-alphabet permutation family. Their \(B_k\) is not a doubled-run binary word, and the claim neither supplies the present exact count nor determines its length layers. Manea–Ringleb–Siemer–Winkler, arXiv:2504.21471v1, Sections 5–6, give enumeration algorithms for general words, not the odd-run classification or the closed form for this specific word family. A published Fibonacci law for *shortest* absent subsequence extremals is a different object and does not imply a count for all minimal absences of this fixed family. A separate known exact family concerns strictly alternating words \((01)^m\), not doubled runs. Database/alias searches found no dominating claim, but failures of search cannot prove absolute novelty; older unindexed formulas and the uninspected full text of Troníček (2023) remain residual risks.

## Value (V) — PASS
The minimal absent subsequence set of a word is its natural obstruction basis for the subsequence order. Complete length-layer enumeration is a motivated output-size benchmark for the 2025 optimal MAS enumeration algorithms. The doubled-run family is a basic symmetric binary periodic family that has additional MAS lengths beyond the shortest layer. Its exact Fibonacci growth coexists with a three-layer width and follows from a reusable greedy run cost, providing an interpretable infinite family result rather than a table or rephrasing of a general counting algorithm.

## Limits
No claim is made for unequal run lengths or for arbitrary binary words. Priority has been assessed against the cited sources and available research records, not exhaustively certified by an independent reviewer.

Self-review: passed. Independent audit: not yet performed.
