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

`artifacts/verify.py` checks the Gauss--Bonnet preservation and the noncritical area ODE with exact rational arithmetic after treating \(4\pi\) as an independent constant. It also tests the three elementary antiderivatives against \((\lambda^2+c)^{-2}\), checks the critical hyperbolic ODE and integrated volume loss, and compares the general Euclidean formula with the direct two-ball cap-area formula at several nondegenerate parameter choices. Replay from the packaged artifact returns `VERIFY_OK`.

The script does not prove the geometric Gauss--Bonnet theorem, the inner-parallel variation theorem, or literature originality. Those are supplied by the cited sources and the mathematical comparison. The claim concerns lenses before extinction and does not extend to arbitrary polyhedra.
