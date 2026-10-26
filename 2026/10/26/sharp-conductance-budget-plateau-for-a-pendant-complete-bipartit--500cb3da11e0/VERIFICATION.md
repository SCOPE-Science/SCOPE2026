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

# Verification notes

Run `python checks/verify.py` with Python 3, SymPy, and NumPy. An execution of this bundled program returned PASS for the symbolic equitable-quotient characteristic polynomial, the symbolic dual trace/edge-distance identities, 57 exact rational assembled-matrix cases, 189 independently assembled finite spectral cases, and the six-vertex rational boundary counterexample. Its exact identities use the graph and ordering specified in `RESULT.md`.

The Gram construction \(X=vv^{\mathsf T}+\sigma^2E\) and the complementary-slackness/averaging step yield the all-parameter upper bound and necessity analytically. Numerical spectra are checks, not proof for arbitrary graph size. The script does not optimize arbitrary nonsymmetric designs; universal optimality follows from the Gram certificate. No independent audit has been performed, and specialized literature overlap remains a stated risk.
