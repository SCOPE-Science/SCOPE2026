# Review: Exact two-deletion circular traces for a single elongated run

## Correctness — PASS

The input, deletion operation, and rotation equivalence are defined explicitly. The proof exhaustively separates deletions by the number of deleted ones and by their positions relative to the unique zero run of length at least three. The decisive nontrivial step counts two equal distinguished run lengths under cyclic rotation only when the initial run has length three; the proof derives the two resulting duplication terms. Independent canonical-rotation and run-cycle implementations agree for all 120 parameter pairs with integers \(3\le a\le8\) and \(3\le k\le22\); they do not establish the unbounded claim themselves.

## Originality — PASS (with residual risk)

Narayanan and Ren (arXiv:2009.01346) introduce circular trace reconstruction and focus on probabilistic reconstruction rather than this exact rotation-quotient output spectrum. Bar-Lev, Etzion and Yaakobi (arXiv:2206.07995) study linear deletion spheres and fixed-length Levenshtein balls, which retain or restore linear starting positions. The related ITCS 2026 article gives general circular-trace probabilities but does not explicitly evaluate this polynomial for the displayed family. Targeted mathematical-record queries found deletion variance, inverse-ball and multi-trace comparison results, not this all-parameter composition-refined claim. The possibility of an equivalent prior enumeration under another name is a substantive residual risk; no priority certification is asserted.

## Mathematical value — PASS

The number of distinguishable observations under cyclically unidentified two-position deletions is a natural support-size statistic in circular trace reconstruction. For the first nonalternating family with a single elongated zero run, exact output deduplication is nontrivial because changing deletion positions can produce the same necklace. The theorem classifies every outcome by composition and captures a sharp stable boundary between an elongated run of length three and runs of length at least four; the formula holds for an infinite two-parameter family and gives a finite-block benchmark without relying on empirical extrapolation.

## Scientific limitations

The proof does not count probabilities or multiplicities of individual traces; it does not address more than two deletions, arbitrary circular sources, or linear observation classes. Literature indexing and alternative formulations cannot be exhaustively excluded. External independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
