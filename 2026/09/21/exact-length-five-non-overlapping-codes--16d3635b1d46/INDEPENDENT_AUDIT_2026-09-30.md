# Independent audit — 2026-09-30

**Record:** `2026/09/21/exact-length-five-non-overlapping-codes--16d3635b1d46`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `b5e277cfa4393012d3593348b9dcbbb7d6d51ac6`  
**Disposition:** **PASSED**

## Correctness

**PASS.** Starting from the published SQN characterization, the n=5 elimination was recomputed: after maximizing the affine e-variable, Φ=a^3b^2+2ab^2c−ac^2+d(b^2−2c), so d is forced to an endpoint and the two stated quadratic branches follow. The unbalanced and balanced bounds are consistent with the stated threshold argument. The supplied verifier was inspected and its finite checks are consistent with the proof: full endpoint-reduced SQN enumeration for q≤7, the reduced optimum and unique orientation through q=60, and the integer maximizer of t(q−t)^4 through q=1000. The all-q conclusion itself rests on the analytic inequalities, not these finite checks.

## Originality

**PASS (literature-bounded).** The 2024 open-access Stanovnik–Moškon–Mraz paper gives the exact SQN optimization and computational exact values for n≥5 only over bounded small alphabets; it explicitly says no simple formula was then available for larger codeword length. Thus the q≤6 numerical values are prior art, while the all-q n=5 formula, q=4 structural threshold, and classification/count of all maximum codes are not stated there. Searches under non-overlapping/cross-bifix-free/mutually-uncorrelated terminology did not locate the all-q theorem; priority remains literature-bounded.

## Scientific value

**PASS.** The theorem converts a finite computational pattern into a closed formula for every alphabet size at length five and classifies/counts every maximum code for q≥4, resolving Blackburn's simple-construction behavior at this fixed length.

## Literature and evidence

- Stanovnik, Moškon and Mraz, In search of maximum non-overlapping codes: https://doi.org/10.1007/s10623-023-01344-z
- Blackburn, Non-overlapping codes: https://arxiv.org/abs/1303.1026

## Limitations

- The theorem is specific to length five and does not classify the exceptional q=2,3 maximum-code structures.
- The proof relies on the earlier SQN structural characterization.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
