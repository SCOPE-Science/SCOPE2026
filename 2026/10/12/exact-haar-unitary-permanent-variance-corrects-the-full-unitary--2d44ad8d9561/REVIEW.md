# Self-review

## Correctness
PASS. The proof realizes the full Haar permanent as a unit-vector matrix coefficient in the irreducible representation \(\operatorname{Sym}^n(\mathbb C^n)\). Schur orthogonality gives \(\mathbb E|\operatorname{perm}(U)|^2=\binom{2n-1}{n}^{-1}\) exactly. Stirling's formula and Markov's inequality then give the stated asymptotic and anti-concentration consequences. The bundled arithmetic checker passed.

## Originality
PASS. The exact second-moment identity itself is classical and is explicitly not claimed as new. The finding is the correction of the current 2026 paper's full-Haar normalization and the quantified consequences for its RMS and anti-concentration scales. The direct source was inspected in full at the relevant sections, the cited 2021 representation-theory paper was compared at abstract/metadata level, and targeted formula, alias, ensemble, and correction searches found no published correction of the 2026 source.

Residual risk: an unindexed public comment may already have noticed the same error, and the inaccessible full text of the 2021 paper may state the \(d=k=n\) specialization explicitly. Neither risk affects correctness; the claim is not priority for the classical identity.

## Value
PASS. Replacing \(n!/n^n\) by \(\binom{2n-1}{n}^{-1}\) changes the variance by the exponential factor \(2^{-1/2}(4/e)^n(1+o(1))\). This changes the quantitative interpretation of the paper's principal Haar-unitary distribution observation and rules out its full-Haar anti-concentration conclusion at the printed Gaussian-entry scale. The distinction is directly relevant to boson-sampling, where Gaussian behavior arises for suitable submatrices rather than from the full \(U(n)\) matrix.

## Closest literature and limitations
The closest prior work is Nezami, arXiv:2104.06423, which develops representation-theoretic moment formulas for Gaussian permanents and Haar-unitary submatrix permanents. It supplies the appropriate broader context and may contain the classical specialization, but it does not constitute a correction of the 2026 source. No central-limit theorem, corrected fourth moment, or anti-concentration theorem at the true Haar scale is claimed here.

Self-review: passed. Independent audit: not yet performed.
