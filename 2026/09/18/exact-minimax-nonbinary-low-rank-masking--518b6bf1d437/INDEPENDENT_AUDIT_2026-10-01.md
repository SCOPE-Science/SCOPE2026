# Independent mathematical audit — SCOPE-20260918-518b6bf1d437

Final disposition: **PASS**.

## Correctness
**PASS.** The kernel-count covariance was reconstructed from the two-vector dependence split, giving the stated universal correlation lower bound for every input-independent rank-at-most-r mask even after invertible left/right transforms. For the exact-rank shell, character diagonalization reduces maximal correlation to normalized bilinear-forms eigenvalues. Cioabă–Gupta Theorems 4.3 and 4.6 were read in full text and give strict magnitude decrease away from rank one for q>=3 and for q=2 with e>=d+1; the rank-one coefficient evaluates exactly to the displayed Lambda. A separate exact-integer reconstruction on representative parameters reproduced this identity and the excluded binary-square behavior. The complete-view matrix-multiplication corollary follows because the extra independently masked upload is independent and the product is a deterministic function of the uploads.

## Originality
**PASS.** The recent masking paper establishes q^{-r} achievability for rank-ball/factor masks and only asymptotic optimality in its public primary abstract, while the older bilinear-forms work supplies the spectrum but not a masking minimax theorem. No inspected source states the exact-rank-shell optimizer or rectangular minimax conclusion. This is a best-of-knowledge judgment because the 2026 masking paper could not be read in full through the available lawful routes.

### Equivalent formulations
This equivalence supplies the achievability proof but is not itself an earlier masking theorem.

### Broader coverage
Neither inspected result alone dominates the final masking theorem; their combination requires the exact-shell choice and identification of the rank-one coefficient with the converse.

### Exact database or table
Search failure is not used as novelty proof; originality rests on the mathematical mismatch between the prior masking theorem and the audited exact finite theorem.

### Claim versus prior implication
The final theorem is not a special case of a stronger inspected masking result.

## Value
**PASS.** The claim closes a newly posed finite-parameter achievability/converse gap exactly over all nonbinary fields, extends the converse/optimizer to rectangles, and identifies a standard-samplable optimal mask. This is a natural optimization problem rather than an arbitrary parameter slice.

## Source inspections
- **Low-Rank Masking for Single-Server Matrix Multiplication** (arXiv:2609.18876): primary arXiv abstract; full-text retrieval was attempted but unavailable Assessment: ABSTRACT_NOT_DECISIVE_FOR_WHOLE_DOCUMENT; abstract gives q^{-r} methods and asymptotic optimality, not the exact shell theorem. Evidence: The abstract explicitly describes rank-ball/factor masks and asymptotic matching for r=o(n).
- **On the eigenvalues of Grassmann graphs, Bilinear forms graphs and Hermitian forms graphs** (arXiv:2102.10155): full PDF pages 1-12, including Section 4 and Theorems 4.3, 4.6, 4.7 Assessment: SUPPORTING_INPUT_NOT_COVERING_FINAL_MASKING_CLAIM. Evidence: Theorems 4.3 and 4.6 give strict |B_j(i)| decrease in exactly the stated q/e regimes.

## Residual risks
- The highly relevant September 2026 masking preprint was not available in full text through the routes tried, so hidden exact-shell discussion or simultaneous work remains possible.
- The independent finite spectral reconstruction is supporting evidence only; the all-parameter correctness relies on the read analytic eigenvalue theorems.

The JSON companion records the structured four-part originality comparison and the same limitations.
