# Scientific review

## Correctness — PASS

The theorem quantifies over all positive integers \(m\) and uses the standard scattered-subsequence notion. The first lemma forces one symbol count to reach \(2m\); minimality bounds each symbol count from above by \(2m\). An explicit intersecting-embedding argument eliminates simultaneous saturation. For the zero-rich case, both embedding conditions become the exact inequalities \(x+y\ge m\) and \(y+z\ge m\); deletion-minimality forces \(x=z=j\), yielding a unique factorization. Converse minimality is proved position by position, with complement symmetry giving the disjoint second family. Binomial counting and a dominated geometric tail establish the exact length spectrum and asymptotic proportion. The independent deletion-by-deletion verifier reproduces the theorem for all candidates at \(m\le5\); no finite test is substituted for the general proof.

## Originality — PASS within examined evidence

The most relevant recent paper, Sopp–Liyanage–Gong–Zhu, arXiv:2603.22591v1, handles arbitrary-input MCS enumeration algorithmically but does not explicitly classify the opposite-run family by words and lengths. Older work of Irving–Fraser and Fraser provides an algorithmic historical precursor. The refined two-parameter spectrum and structural necessity/converse were not found in those examined materials. However, the **unrefined total sequence** is exactly twice an index-shift of OEIS A112029, and its purely numerical/asymptotic identity is expressly **not** claimed as novel. An unseen equivalent structural result is still possible, especially in incompletely accessible older full text; this review is not independent priority confirmation.

## Mathematical value — PASS

For a natural pair of opposing two-run strings, minimal supersequences have a nontrivial range of lengths rather than only the shortest length. The theorem completely describes every minimal witness and the exact number at each attainable length, sharply identifies both extremal lengths, and establishes concentration of the longest witnesses. This resolves a motivated structural instance of recent general-purpose enumeration algorithms and supplies explicit benchmark distributions, not merely a routine renaming of the already indexed numerical sum.

## Closest prior literature and restrictions

Sopp et al. (2026), arXiv:2603.22591v1: general polynomial-delay enumeration, no explicit opposite-run length spectrum in the examined full text. Irving–Fraser (1994) and Fraser's related thesis: algorithms and maximal/minimal string theory, without an identified direct length-spectrum theorem; complete early primary article not accessed. OEIS A112029: exact same scaled total number sequence, but not a classification of MCS words by length. The result does not extend to arbitrary two-string inputs, and independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
