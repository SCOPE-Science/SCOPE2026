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

# Verification instructions and mathematical scope

Run `python3 verify.py` in any Python 3 environment. The script uses the Python standard library only. It tests finite convex polygons against direct clipped intersection areas for 128 directions per polygon, independently approximates the directional integral from 8,000 samples, checks the variance lower bound on regular and asymmetric examples, and numerically compares the even-sided sharpness ratio with \(1/(24\pi^2)\). The expected terminal line is `VERIFY_OK`.

These checks inspect the exact directional quadratic coefficient and the shape of the sharpness example, but no finite numerical test certifies a universal mathematical statement. The proof in `RESULT.md` establishes fan persistence, the angular integrals, strict convexity of the angle function, and optimality over all side counts. No independent audit or external verification has been performed.
