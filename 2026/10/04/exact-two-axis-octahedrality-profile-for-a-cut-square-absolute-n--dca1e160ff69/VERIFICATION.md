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
The analytic proof in `RESULT.md` is the primary verification.

The companion `verify_two_axis_profile.py` uses only the Python standard library and exact `Fraction` arithmetic. For a deterministic collection of rational parameters \(t\in[0,1]\), it enumerates rational points on each of the three positive-sphere boundary segments, verifies the exact scalar objective, confirms that every sampled value is bounded by \(\max\{(3+t)/2,(2+t)/(1+t)\}\), and confirms that the diagonal sphere point attains the formula exactly. It also checks the two endpoint values and the sign change of the branch comparison around \(\sqrt2-1\).

The finite grid is not an exhaustive proof of the continuous optimization. Its role is to replay the algebra, boundary parametrizations, and branch logic; the continuous statement is established by the inequalities in `RESULT.md`.
