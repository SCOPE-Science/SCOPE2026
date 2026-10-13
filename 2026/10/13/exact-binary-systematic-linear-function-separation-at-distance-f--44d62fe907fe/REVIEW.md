# Scientific review

## Correctness — PASS
The proof handles every binary linear function, including zero columns, repeated images, and functions with nontrivial kernels. Single-position differences force parity row weight at least three; two-position differences with distinct nonzero images force pairwise distance at least two. The fixed-coordinate hypercube matching excludes exactly \(r\) adjacent pairs, giving a sharp bound. Odd-weight parity labels realize every allowed number of image types, and an exhaustive case analysis over input differences of weights one, two and three verifies separation four. `verify.py` independently checks 84 small functions and four full-projective families. Computation supports, but does not replace, the proof.

## Originality — PASS, with residual risk
The primary full text explicitly states that exact systematic linear redundancy at prescribed separation four is left open (Ho, arXiv:2608.29389v1, Remark 5.13), while its proved distance-three formula has a different projective threshold. Classical extended Hamming codes already determine the identity-function special case and are credited. The additional result that *every* binary linear function is classified by its distinct nonzero function-column count is not present in the inspected primary source or discovered published comparisons. The 1990 parity-check literature may contain an implicit equivalent; the full article was unavailable, so that residual risk is disclosed.

## Value — PASS
This settles the complete binary case at the first prescribed separation beyond the classification in Ho's paper, replacing an apparently complicated triple-row constraint by a sharp constructive invariant of the protected function. It applies with arbitrary kernel, zero columns, and multiplicities and quantifies the redundancy cost of protecting a function rather than the whole message. It is a natural all-function exact classification rather than an arbitrary finite example or mere reproduction of the extended-Hamming special case.

## Scope and limitations
Only binary fields, linear systematic encoders and prescribed separation four are established. Neither nonbinary nor nonlinear analogues are asserted, and an earlier equivalent in uninspected UEP literature remains possible.

Self-review: passed. Independent audit: not yet performed.
