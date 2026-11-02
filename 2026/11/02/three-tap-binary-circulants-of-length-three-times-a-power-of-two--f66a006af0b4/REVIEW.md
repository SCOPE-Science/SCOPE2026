# Review of three-tap binary circulants

## Correctness — PASS
The rank formula uses the standard principal-ideal description in \(\mathbb F_2[x]/(x^{3\cdot2^k}-1)\). The cubic root condition exactly characterizes singular triples, Frobenius extracts their root multiplicity, and Chinese remaindering counts all strata with no uncounted cases. The polynomial kernel generator gives literal repeated even-parity triples; projecting subcodes proves the full higher-support hierarchy. `verify.py` exhaustively checks the gcd and rank predictions on 19,561 supports and the exact weights of 66,112 codewords. These experiments supplement the infinite argument, not substitute for it.

## Originality — PASS (qualified)
Choi and Hur's 2026 finite-field invertibility manuscript supplies general polynomial methods but not the exact fixed-weight-three rank census at lengths \(3\cdot2^k\). Wei and Zou's rank census includes arbitrary support coefficients and does not distinguish the three-tap shell or describe its kernel codes. The weight-three cyclic-code study of Charpin, Tietäväinen, and Zinoviev focuses on another length regime. Search comparisons also considered recent three-tap convolution classifications on nonabelian groups, which have different fields/groups and cannot imply the repeated-root binary formulas directly. The classical rank and coding lemmas are credited. Residual risk: an older repeated-root code classification could subsume the coding part or provide the full census in disguised form.

## Mathematical value — PASS
A fixed-sparsity singularity spectrum is relevant to sparse cyclic convolution and binary cyclic codes: rank-only results leave unresolved which three-tap operators are singular and how frequently each nullity occurs. This theorem resolves the complete spectrum at an infinite family of sizes, reduces its many singular kernels to a strict chain of \(k+1\) explicit codes, and supplies every support invariant. The classification is materially more informative than either an invertibility criterion or a single parameter example.

## Scientific boundaries
Scope is exactly three taps over \(\mathbb F_2\) with order \(3\cdot2^k\); generalized weights are for the kernel, not the image. The review does not claim independent validation or exhaustive historical priority.

Self-review: passed. Independent audit: not yet performed.
