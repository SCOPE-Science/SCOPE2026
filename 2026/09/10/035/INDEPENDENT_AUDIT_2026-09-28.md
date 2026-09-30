# Independent Audit — 2026/09/10/035

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b77033af041bc6c195d83af151ab5facc8764622`
- Disposition: **PASSED**

## Correctness

**PASS** — An independent implementation of the stated QC base matrix and symmetric lifted-product formulas reproduces 105x238 H_X,H_Z matrices, row weight 8, H_X H_Z^T=0, ranks 97 and 97, and k=44. Exhaustive enumeration of the 16-dimensional kernel of B reproduces minimum weight 6 and the full deposited distribution. The explicit support {0,4,10,18,21,24} has zero H_Z syndrome and raises rank(H_X) from 97 to 98, proving it is a non-stabilizer X logical. Independent exhaustive neighborhood enumeration also reproduces 84 failing 4-subsets and none of sizes 1-3.

## Originality

**PASS** — Searches for the exact N=238, 3x5, L=7 instance, the rank-97/97 parameters, and the explicit support did not locate an indexed prior table or paper. The finite-length LP distance paper gives general constraints but not this instance or witness.

## Scientific value

**PASS** — The explicit logical operator is a complete certificate falsifying the proposed d>=9 bound for a named finite LP instance, and the exact rank/base-distance/expansion diagnostics make the failure reproducible and diagnostically useful. Exact quantum distance need not be determined to establish this negative result.

## Limitations

- The audit proves only d(Q*) <= 6; a lower-weight mixed-block or Z logical could exist.
- The conclusion is tied to the stated LP construction up to row/column permutation.

## Sources

- On the Minimum Distances of Finite-Length Lifted Product Quantum LDPC Codes: https://arxiv.org/abs/2503.07567 — Nearest finite-length LP distance literature; no exact N=238 witness located.
- Quantum LDPC Codes With Almost Linear Minimum Distance: https://doi.org/10.1109/TIT.2021.3119384 — Broader lifted-product/QLDPC context.

This audit is independent of the record's pre-existing AUDIT.json. GitHub was read only as evidence; no repository mutation was performed in this audit chat.
