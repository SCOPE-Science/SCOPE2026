# Scientific review

## Correctness — PASS
The proof fixes the Gaussian and inner-product conventions, derives the scalar kernel formula from the orthogonal splitting, and treats all radius and angular endpoints explicitly. The logarithmic threshold follows from a sharp harmonic-circle minimum; first-zero simplicity and monotonicity use exhaustive parameter cases and sign analysis, not numerical scans. The two asymptotic expansions follow from a nondegenerate analytic square-root equation and exponential control of the far-field root. The included standard-library checker passed fifteen supporting parameter and asymptotic tests. A finite numerical sample is not the proof.

## Originality — PASS (best-known evidence)
Looi (arXiv:2608.13550, Sections 2 and 6) and Fulsche (arXiv:1901.02644) record the pluriharmonic Fock kernel/splitting; these premises are not claimed as new. Their inspected results do not give the sharp first orthogonality radius, the strictly decreasing first angular zero, or its two asymptotic laws. Fulsche and Hagger (2024) study different, polyanalytic Laguerre kernels, whose displacement-dependent zeros do not imply this result. Semantic published-record searches and targeted literature searches did not find equivalent quantitative statements. Unindexed earlier coverage remains a risk, particularly because the scalar kernel formula is known.

## Value — PASS
The first-orthogonality boundary is a natural exact geometric invariant, with a sharp local onset and an unexpectedly collapsing far-field Euclidean separation. The contrast with the holomorphic coherent-kernel geometry motivates its use as a benchmark for interpolation and sampling conditioning. No global sampling inequality is asserted.

## Limitations
One-dimensional equal-radius angular geometry is classified only at the least zero; later oscillatory zeros and unequal-radius pairs are not classified. The full-ball threshold holds in all complex dimensions. Independent expert validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
