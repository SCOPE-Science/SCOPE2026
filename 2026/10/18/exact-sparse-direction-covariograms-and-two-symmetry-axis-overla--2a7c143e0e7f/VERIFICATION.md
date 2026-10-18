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
# Verification and limits

Running `python verify_octahedral.py` in a Python environment with SymPy, NumPy and SciPy produces `OCTAHEDRAL_COVARIOGRAM_OK`; it symbolically evaluates the exact three-dimensional slice integrals and checks dimensions 3–12, constructs 18 independent three-dimensional polyhedral intersections, and verifies both comparison roots. The written proof, not finite computation, justifies every integer dimension and all real parameter values. The derivation and finite checks are self-reviewed only; independent audit has not been performed.
