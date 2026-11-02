# Scientific review

## Correctness — PASS

The paperfolding convention matches the cited definition. An explicit lower-bound lemma turns rational factor weights with per-position load at most one into a valid integer lower bound for **every** possible attractor. For each finite word the packed factor occurrences, load inequalities, and sums are reconstructed exactly by `verify.py`. Separately, all \(6479,25775,102767,410351\) distinct factors are exhaustively checked to cross a listed upper-witness position at least once. The resulting lower ceilings and upper witness sizes agree. The result is a finite proof by complete enumeration, not an extrapolation to an infinite word.

## Originality — PASS, subject to residual search risk

The closest public exact-same-object record, [2], was read in full at its RESULT.md and reports only interval bounds for lengths \(128\), \(256\), \(512\), \(1024\); it gives exact minima only through \(64\). Its paperfolding bounds at the four lengths are respectively \([4,7]\), \([4,8]\), \([4,10]\), \([4,9]\). The new minima \(5,6,6,7\) are **not implied** by any of those intervals. The 2026 Banbara et al. paper, whose relevant introduction and theorem sections were inspected, concerns Fibonacci and period-doubling words; the October 2026 extended version adds Thue–Morse, not paperfolding. Schaeffer–Shallit is broader automatic-sequence context; the accessible abstract does not establish these explicit finite values. Searches for equivalent phrasing, exact parameters, the same factor-packing or hitting-set formulation, and dominating tables found no covering record. Publication priority beyond indexed and accessible sources cannot be certified.

## Value — PASS

These four powers of two are precisely the first four unresolved natural checkpoints following the earlier exact dyadic cutoff \(64\), not arbitrarily sliced parameters. The old bounds at length \(512\) were as wide as \([4,10]\); the new rational dual certificate closes that gap and uncovers a nontrivial plateau between \(256\) and \(512\) followed by a jump at \(1024\). The explicit finite lower certificates provide reusable tools for quantitative attractor investigations of automatic words. The modest finite scope is stated, not enlarged by an unsupported infinite conjecture.

## Closest literature and limitations

[1] M. Banbara et al., arXiv:2602.16152, DOI 10.4230/LIPIcs.CPM.2026.33 (word-family characterization, distinct objects).

[2] https://github.com/Resultary/2026/blob/main/2026/9/8/SCOPE079/RESULT.md (same paperfolding prefixes, only bounds beyond length 64).

[3] L. Schaeffer and J. Shallit, arXiv:2012.06840 (general framework, abstract-level inspection only).

Limits: no all-prefix formula or infinite boundedness decision; unpublished or unindexed exact computations may exist. Verification is a finite exhaustive certificate replay, not a proof by an external mathematical expert.

Self-review: passed. Independent audit: not yet performed.
