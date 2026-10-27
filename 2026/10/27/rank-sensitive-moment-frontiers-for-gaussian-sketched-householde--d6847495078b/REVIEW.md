# Self-review

## Correctness — PASS
For the fixed orthonormal input, the reconstructed basis norm is exactly the reciprocal least singular value of the block sketch. The proof explicitly diagonalizes the retained deterministic Gram block, separates an independent rectangular Gaussian null block, proves two-sided comparisons of reciprocal singular values, derives the sharp chi-diagonal negative-moment threshold, and transfers its square to the Euclidean Gram defect. The analytic proof handles every positive real moment order and critical equality; `verify.py` passed 3,937 finite checks but numerical tests do not establish the infinite-moment claims.

## Originality — PASS, with publication-priority risk
The originating Grigori–Timsit arXiv:2405.10923 Theorem 3.7/Section 3.3 constructs the block sketch and reconstructed QR factor; the source analyzes high-probability embeddings and stability rather than the rank-sensitive unconditional all-moment frontier. Balabanov–Grigori arXiv:2011.05090 supplies the earlier sketched Gram–Schmidt framework, while Jang–Grigori doi:10.1002/nla.70029 handles a reorthogonalized output. Standard Bartlett chi-variable and pure Gaussian inverse singular-value results are known proof ingredients and are not claimed new. Targeted published mathematical comparisons did not find a covering statement; this is not proof of publication priority. A more general partially deterministic inverse-Wishart theorem could subsume the result, and the Anderson–Wells Gaussian condition-number paper was inspected only by abstract.

## Value — PASS
The sharp threshold distinguishes high-probability stability from existence of unconditional Euclidean Gram-defect moments for a directly motivated block-preserving QR construction. With minimal oversampling the change from zero to rank-one retained deterministic information changes the expected Gram defect from infinite to finite, even though the original input is exactly orthonormal. The precise cutoff gives a meaningful numerical-method design diagnostic while respecting the restricted real-Gaussian exact-arithmetic model.

## Closest literature and limitations
See `RESULT.md` for assumptions, exact formulas, proof, reproducibility, and full scientific limitations. The primary reference is Grigori and Timsit, *Randomized Householder QR*, HAL hal-04156310 (authors report first public version 2023-07-07), arXiv:2405.10923. All comparisons are self-review; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
