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

# Verification instructions and limits

Execute `python verify_parametric_trust.py` with Python 3.9 or later. The program requires only the Python standard library and performs exact rational evaluations of the characteristic function and all pertinent coalition inequalities. It checks all directed zero-or-one-weight support graphs with one through four vertices at five mixing values, plus seeded directed graphs with weights from \(\{0,1/5,2/5,3/5,4/5,1\}\) on two through five vertices at seven mixing values. Total parameterized graph cases: 22,085. The program verifies the co-singleton upper-bound identity, the negative-phase impossibility certificate, the explicit core allocation, the exact tightness pattern and component equations, core certificates for every restricted coalition game, and the two-agent critical interval. On successful completion its first output line begins with `PASS 22085`.

The proof for arbitrary finite order and arbitrary real nonnegative weights is in `RESULT.md`; no finite enumeration implies the universal statement. In particular the affine-dimension assertion follows from an analytic strict-feasibility argument in the component-sum affine space, not from rank extrapolation. No external certification or independent audit has been performed.
