# Self-review

## Correctness
PASS. Translation invariance is exactly the pair of block equations \(au+bu/2=0\) and \(b^Tu/2+cu=0\). Substitution into \(\Delta=4b^{-1}ab^{-T}c-I_4\) gives \(\Delta u=0\), and the converse reverses the same calculation using invertibility of \(a\) and \(b\). The cited factorization implies \(\operatorname{rank}(Q)=4+\operatorname{rank}(\Delta)\). Under distinct eigenvalues, the forced zero is simple, so the rank is exactly \(7\) and the kernel is exactly the translation line. The explicit example is checked by exact arithmetic in `verify.py`.

Risk: none of the finite checks is used as a proof of the general statement; the general result rests on the displayed algebra.

## Originality
PASS. The closest recent source, arXiv:2610.01091v1, defines pan-genericity, records the block factorization, states only that pan-genericity implies rank at least \(7\), and then introduces translation invariance. Full-text inspection found no statement that translation invariance forces \(\Delta u=0\), no explicit incompatibility with Green's older zero-excluding hypothesis, and no exact kernel classification. Green's open-access 2025 paper explicitly excludes eigenvalue \(0\) and explains its connection with nonsingularity, but does not treat the translation-invariant singular regime. Targeted searches of the published-finding corpus and primary literature for the source, zero-eigenvalue formulation, rank-seven formulation, and all-ones kernel found no covering result.

Residual risk: because the deduction is short, an unindexed note may contain it; no such source was located. The statement is intentionally restricted to the fixed \(4+4\) splitting.

## Value
PASS. The observation identifies the exact structural reason that the 2026 hypothesis must permit eigenvalue \(0\): translation invariance itself forces that eigenvalue. It therefore explains why the new dense-prime result occupies a singular regime excluded by Green's predecessor, upgrades the source's rank lower bound to an exact rank/kernel statement, and supplies a concrete indefinite integral example. This is a natural structural lemma tied directly to the new theorem's hypothesis class.

Self-review: passed. Independent audit: not yet performed.
