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
# Reproducibility and limits

The complete analytical proof is in `RESULT.md`. Run `python verify.py` to perform exact rational checks independent of the displayed hypergeometric derivation. It enumerates each labeled-subset sample in the finite tested domain and computes rooted branch-union length directly from detected tips. The program reported: `PASS 72 exact profile-depth or boundary checks`, including the \(N=5\), \(m=3\), \(H=1\), \(\varepsilon=1/16\) covariance \(-3/200\). The all-size endpoint/nonendpoint statement depends on the analytical proof, not on extrapolating these checks. Full bibliographic equivalence cannot be certified by searches. Independent scientific audit is not performed.
