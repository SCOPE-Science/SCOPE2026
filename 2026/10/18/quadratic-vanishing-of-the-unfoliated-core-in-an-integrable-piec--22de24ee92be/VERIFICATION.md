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

# Reproducibility and scope

The archived `verify.py` checks exact polynomial identities over the relation \(s^2=t-t^2\), the determinant-one and quadratic-form conservation identities of the source corner map, and the signed-area determinant identity. It then reconstructs the actual fourfold polygon vertices from the corner matrix and checks the direct shoelace calculation at \(K=3,4,8,12\), with additional high-precision numerical asymptotic tests at \(K=100,300,1000\). Executing the actual package file returned `VERIFY_OK`.

The infinitely quantified result is established by the independent algebraic and asymptotic argument in `RESULT.md`, not by finite test coverage. The polygon is simple and encloses a region, and the outer annulus is foliated, by Ostrovski's original theorems. No statement about the dynamics in the remaining core is verified.
