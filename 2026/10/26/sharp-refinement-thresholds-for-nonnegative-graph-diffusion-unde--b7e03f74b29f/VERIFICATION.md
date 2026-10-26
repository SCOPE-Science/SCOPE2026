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

# Reproduction and limits

Run `python verify.py` in the extracted package after installing dependencies from `requirements.txt`. The script checks exact binomial and rational coefficient identities for each integer refinement from two to eighteen, proves the sign changes by direct exact arithmetic, constructs the stated 13-vertex unweighted graph, and checks its diameter, geodesic and Laplacian fourth-power data. It also evaluates representative full extrapolated diffusion matrices.

The proof of the infinite-family claim is the geodesic leading-term identity together with coefficient signs in RESULT.md. Small finite matrix checks are corroboration only, and rounded floating-point near-zero entries are not used as infinite proofs.

Public-status note: self-review passed; independent audit not performed. No independently issued mathematical certification is asserted.
