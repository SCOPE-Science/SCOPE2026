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
# Verification

The proof is analytic for every \(n\ge2\). The finite checker is supplementary.

`checker.py` exhaustively enumerates every permutation for \(2\le n\le9\). With exact rational arithmetic it verifies each conditional mean \(\mathbb E[\rho\mid\Pi(i)=i]\), every coordinate covariance \(\operatorname{Cov}(I_i,\rho)\), the aggregate covariance \(\operatorname{Cov}(F,\rho)\), the null means and variances, and the orthogonality
\[
\operatorname{Cov}(F-1-\rho,\rho)=0.
\]

The exhaustive replay covers \(409112\) permutations. It does not prove the infinite family; the all-\(n\) proof is the conditional-permutation calculation in `RESULT.md`.
