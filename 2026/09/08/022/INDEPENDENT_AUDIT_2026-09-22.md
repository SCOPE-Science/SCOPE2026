# Independent audit — 2026-09-22

**Disposition: ACCEPTED, with originality narrowed to the inversion-refined contribution.** Audited current `main` at `fd2a78c671f3d93289bb4d500e6fbc1bba9c9ede`; record tree `d049bb8311249a266c1bab289ee5e6f041171b1e`.

## Correctness
PASS. An independent hereditary insertion enumeration with a naive check of every 4-subsequence against ({1324,1243,1432}) regenerated the complete inversion distributions through (n=11). Totals 5150, 21517, 90921, 387595 and every stored cell matched. The audit confirms (a_8^6=15>11=a_9^6), (a_{10}^8=26>22=a_{11}^8), decrease for every (kle15) across (n=8..11), and the nonmonotone (k=16) row ((405,422,350,299)). The unsafe append-maximum witness and both (+n)-inversion shift embeddings were also rechecked.

## Originality
PASS WITH NARROWING. Searches: `"1324 1243 1432" inversion permutation avoiding`; `"Inversion monotonicity" subclasses 1324 avoiders`; `"A257562" 4123 4231 4312`; `"Case 237" 1324 1243 1432 inversion`. OEIS A257562 already supplies the Wilf-symmetric **univariate totals**, so those totals receive no novelty credit. Callan–Mansour (arXiv:1705.00933) supplies the exceptional triple-enumeration context. Claesson–Linusson–Ulfarsson–Verkama (arXiv:2604.01143) shows inversion monotonicity in 1324 subclasses is an active topic. No duplicate of this triple's inversion-refined table, finite transition, or shift lemmas was found in the searched sources.

## Scientific value
PASS. The surviving contribution is the bivariate inversion behavior: a concrete fixed-k monotonicity failure and sharp finite transition for an exceptional 1324 triple, with complete dual-checkable data and two reusable shift embeddings. The record appropriately limits its antitonicity claim to the computed window.

## Source identity / limits
Blobs: RESULT `2a80084126f2de0720da663615e94cd0c76401b6`; METADATA `6b2215317dc9ce56237df0cc077d40d6d1110bb4`; prior AUDIT `3ecb35d45971a4a4fb53eb377eb86880c21667dc`; prior VERIFICATION `83b03a7f246da30fad50fa39962dbb6d7f0519f0`. Inventory snapshot `e9ed144c13b7834896a844cc4f9cac3c25a168a6`. Indexed-literature search is targeted, not a proof of absolute absence.
