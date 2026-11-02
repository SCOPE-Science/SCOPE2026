# Review: Exact periodic image law for elementary cellular automaton Rule 30

## Correctness — PASS

The theorem concerns indexed binary rings of every length \(n\ge1\), with simultaneous Rule 30 local update \(x_{i-1}\oplus(x_i\lor x_{i+1})\). Each output symbol induces a deterministic inverse step on the four adjacent-input pairs; an output has a same-period predecessor precisely if the resulting transformation has a fixed point. This also handles the one-cell and two-cell rings. The two inverse maps generate a completely enumerated monoid of 41 transformations, 30 of which accept. The exact polynomial identity follows from the verified first 49 rational-series coefficients because the unfactored 41-state adjugate numerator difference has degree at most 48. The formal coefficient identity then yields the stated recurrence, and root moduli yield the asymptotic law. `verify.py` regenerates `certificate.json` and returns `VERIFY_OK`; independently brute-forced images through length 17, and the implied missing-state values match the published Faulkenberry census for every length through 27. These finite checks do not replace the rational-series proof.

## Originality — PASS (historical priority qualified)

The central object is **same-period cyclic image cardinality**, not open-boundary block preimage count. Jen (1989), *Enumeration of Preimages in Cellular Automata*, relevant inspected full-text pages, gives four finite-window preimages for Rule 30 with boundary freedom: that does not cover one-step image counts of indexed rings for all lengths. Wolfram's 2019 primary discussion shows individual finite-ring graphs but not the displayed rational all-length image series. Faulkenberry (2016), Appendix A Table 6, supplies a genuine 27-length cyclic Rule 30 Garden-of-Eden census; all 27 entries are exactly consistent with the formula, but the inspected thesis sections provide finite data, not an all-length derivation, recurrence or asymptotic. The Elementary CA Zoo provides selected finite checks. Targeted published-result searches for the exact sequence, dominant root, generating-function factor, image-cardinality aliases and the broader transformation-monoid formulation did not identify an equivalent or stronger all-length theorem. The original 1983 Wolfram manuscript was not read in full and unindexed exact literature remains a residual historical-priority risk. There is no claim that the underlying finite-state enumerator, the finite counts, or left permutivity is new.

## Value — PASS

The one-step finite-ring image size is a natural invariant quantifying how far a fundamental left-permutive cellular automaton is from surjectivity **at the same finite period**. The explicit all-length formula distinguishes exact-period realizability from bi-infinite surjectivity and turns previously published 27-term numerical observations into a proved rational series, recurrence, and sharp exponential missing-output rate. It answers a meaningful family-wide reachability-count question without requiring a downstream dynamical theorem.

## Scientific scope and risk

Only the indexed one-step Rule 30 image is counted. Individual predecessor multiplicities, multistep images, period distribution of dynamics, noise, and global questions about Rule 30 are not established. Historiographic precedence is provisional pending independent literature auditing; self-review is not external mathematical certification.

Self-review: passed. Independent audit: not yet performed.
