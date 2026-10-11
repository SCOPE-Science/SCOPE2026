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

The proof is analytic. `verify.py` is a reproducibility check that independently constructs the sampled kernel
\[
D_{4,N}(j)=\sum_{k=0}^3e^{2\pi i kj/N}
\]
and compares its normalized \(L^1\) sum with the closed formula for every \(4\le N\le500\). It also checks the simplified formulas in the even residue classes and evaluates the scaled second-order defects on large meshes.

The finite computation does **not** certify the theorem for all \(N\). The all-\(N\) statement rests on the explicit cosine-sum proof in `RESULT.md`; the large-mesh checks only test the algebra and asymptotic coefficients numerically.
