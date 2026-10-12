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

The mathematical claim is the universal sharp bound \(0\le Q(X|B)\le1-p_{\mathrm{guess}}(X|B)\) for every finite commuting conditional ensemble. Its proof, not the verifier script, establishes it for all finite dimensions, zeros, repeated eigenvalues, and the full parameter range.

The standalone `verify_subentropy.py` uses Python's standard-library `decimal` arithmetic at precision 85 and exact-rational normalized inputs. It calculates \(Q\) independently through the divided-difference definition for nonrepeated positive eigenvalues. The script checks 48 reproducible two-observation, three-label joint distributions, including a case with zero entries, against the spectral-marginal inequality and the Bayes-error bound. Three binary near-deterministic samples check the sign and expected first-order sharpness. The actual script replay produced:

`VERIFY_OK tables=48 binary_edges=3 precision=85 analytic_proof_required=yes`

The checker does not attempt to numerically resolve repeated nonzero eigenvalues, test an infinite continuum, or establish independent validation. Those cases are addressed by the analytic proof and its continuity argument; the publication comparison is limited to the inspected cited literature.
