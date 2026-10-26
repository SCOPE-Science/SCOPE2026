---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and checks

Execute `python3 checker.py` with Python 3 and no third-party packages. The actual output from the packaged code is embedded as `checker_output.txt`. The final line of the successful run is:

`ALL_FULL_SUPPORT_RANK_ONE_CHECKS_PASSED cases=15 matrices=5629 Fourier_cases=6`

The checker enumerates the full-support rank-one matrices in 15 small cyclic label-group examples. It verifies exact size, means, covariances, and pairwise independence. It also calculates real Gaussian determinants and discrete Fourier singular-value expressions on six finite cyclic groups. Not every cyclic-group order corresponds to a finite field, and those examples check the group-theoretic proof step only. Finite tests are not proofs of the multinomial central limit theorem, of non-Gaussianity in every field, or of novelty. Those assertions rely on the mathematics and prior-work comparison given in `RESULT.md` and `REVIEW.md`.
