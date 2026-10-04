# Review
## Correctness
**PASS.** After normalization, every zero is an equilateral cancellation of three unit complex numbers, so it belongs to one of exactly two orientations. The character-pair map has kernel of size \(g\), which fixes every nonempty fiber size. The proof then reduces the possibility of seeing both orientations to one explicit image-membership problem and solves it by elementary congruences, yielding precisely the modulo-\(3\) criterion. The explicit phase choice realizes the nonzero alternative, while finiteness of the bad phase pairs supplies a zero-free choice. The exact checker independently confirms the residue criterion and zero counts for all normalized supports through \(N=180\). Risk: the computational range is finite, but the all-\(N\) conclusion does not rely on it.

## Originality
**PASS.** Tao's prime-cyclic theorem permits arbitrary coefficients and yields the sharp unrestricted two-zero ceiling for a three-term polynomial; it does not imply the stronger one-zero ceiling under equal magnitudes. Delvaux--Van Barel treat rank-deficient Fourier submatrices with unrestricted null vectors, so their results likewise do not enforce unimodular coordinates. The closest own results concern unrestricted amplitude-tuned three-sparse uncertainty, all-ones spectral triples, or phase minimax objectives, none of which implies this exact phase-only zero classification. Targeted semantic searches under unimodular, phase-only, roots-of-unity, uncertainty, and exact-zero formulations found no covering statement. Risk: an equivalent elementary fact may exist in unindexed older sequence-design literature.

## Value
**PASS.** Equal magnitudes are a natural phase-only restriction in sparse Fourier analysis. The result is a complete all-modulus classification, not a small-table computation, and it identifies an exact arithmetic mechanism: paired cancellation occurs precisely when the reduced three-point geometry is complete modulo \(3\). The prime corollary gives a strict structural improvement over the sharp unrestricted uncertainty ceiling within this natural subclass. Risk: the theorem is intentionally narrow and does not by itself address larger supports.

## Closest literature and limitations
The main comparison sources are Tao's prime-cyclic uncertainty theorem, the Delvaux--Van Barel rank-deficient Fourier-matrix framework, and Gilbert--Rzeszotnik's finite-Abelian Fourier norm work. None of the inspected statements imposes the same equal-magnitude three-sparse hypothesis while classifying the exact Fourier zero count. The claim is limited to cyclic groups and exactly three nonzero coefficients.

Same-model review: passed. Independent audit: not yet performed.
