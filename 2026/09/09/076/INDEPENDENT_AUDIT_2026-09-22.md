# Independent audit — 2026/09/09/076

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

The space of degree-136 affine polynomials has binom(138,2)=9453 columns, and ten multiplicity-43 points impose 10·binom(44,2)=9460 derivative rows. Thus virtual projective dimension is −8. I fetched and independently compiled the original C kernel, then reran the 9460×9453 matrix over F₂₅₁ at the ten listed distinct rational points. It returned **9453 pivots of 9453 columns**; inspection of the code confirmed its entries are the appropriate falling-factorial derivatives and its elimination performs invertible field row operations. A nonzero maximal minor modulo 251 is nonzero over Q. Upper semicontinuity therefore implies vanishing for general ten-tuples over characteristic zero. The degree ratio 136/43 lies strictly between sqrt(10) and 174/55, and D·C=7e+43 for a (−1)-curve follows from Σcᵢ=3e−1. The shifted kernel has a one-past-allocation write in its factorial-table initialization; the independent base-kernel result suffices and that secondary log is not used as proof.

## Originality — PASS

Ciliberto–Miranda, arXiv:0812.0032, prove expected dimension for d/m≥174/55, leaving this lower-ratio cell outside their theorem. The explicit finite-field full-rank specialization is a new certificate for this one cell in the consulted primary work. It uses standard semicontinuity rather than a new general degeneration; an exhaustive priority claim is not established.

## Scientific value — PASS

The certificate settles a precisely identified first low-multiplicity cell just below the known slope, with a reproducible exact rank witness. It does not establish Nagata or SHGH throughout the remaining strip.

Sources: https://arxiv.org/pdf/0812.0032 ; https://arxiv.org/pdf/1211.6380 . Open preprints sufficed.
