# Independent audit — 2026-09-29

Record: `2026/09/19/exact-rank-one-masking-maximal-correlation--eb153aa9e688`  
Assigned and audited source tree: `d33df47c239c22bfd2f385dc4a16a7ccecfb0e59`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `92ff732da9686b15ac2af9db323bfd9965f5d2cd`  
Disposition: **passed**

## Correctness

**independently_supported**. The rank-one shell calculation is correct. Every nonzero rank-one matrix has exactly q-1 factorizations uv^T with u,v nonzero, so that sampling is uniform on the shell. For a character matrix H of rank s, counting v in ker H and using character orthogonality gives lambda_s=(q^(2n-s)-2q^n+1)/(q^n-1)^2. Additive-noise maximal correlation is the largest absolute nontrivial Fourier coefficient. The lambda_s decrease with s and lambda_n=-1/(q^n-1); for n≥3, lambda_1≥|lambda_n|, so the claimed value follows. A fresh complete enumeration for q=2,n=3 found 49 shell matrices and character averages 17/49, 1/49, and -1/7 at ranks 1,2,3, exactly matching the formula. The source converse at r=1 gives the same finite-n lower bound for the admissible input-independent rank-at-most-one class with secret invertible transforms, so the shell is minimax. For two independent uploads, product-channel singular values make the joint maximal correlation equal to the single-channel value, and Z=XY is deterministic from the uploads.

## Originality

**qualified_exact_rank_one_completion**. Cohen–D'Oliveira–Sprintson's September 2026 source introduces the masking model, two q^-r achievability schemes, and the universal/asymptotic converse even with secret invertible transformations. Classical bilinear-forms association-scheme spectra are also prior. The current public source summary does not claim an exact finite-length minimax theorem for r=1 or the nonzero rank-one shell sampler, and targeted searches found no such completion. Originality is therefore supported narrowly for matching the converse exactly at r=1 and identifying the shell as the optimizer.

## Scientific value

**meaningful_exact_finite_length_completion**. The theorem closes the factor-of-constant finite-length gap at the first nontrivial rank budget, supplies an equally simple O(n^2) sampler, and proves a strict finite-n improvement over both source constructions. The asymptotic exponent is unchanged, so the principal value is exact minimax characterization rather than a new asymptotic privacy rate.

## Literature and evidence checked

- https://arxiv.org/abs/2609.18876
- https://doi.org/10.1016/0097-3165(78)90015-8

## Limitations

- Exact optimality is proved only for rank budget r=1 and n≥3.
- The source model assumptions of uniform inputs and input-independent rank-constrained masks are retained.
- The finite-length improvement over q^-1 vanishes exponentially with n.
- The rank-metric Fourier spectrum itself is classical and is not claimed as new.
