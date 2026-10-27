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

The proof is independent of numerical enumeration. It reduces the continuous-time occupied-subset chain to the exact two-class first-step equations, solves them by summation of a first-difference identity, and separately compares the complete-graph death rates under **the same per-walker activity normalization**.

The standalone `verify.py` program, requiring only Python 3 standard-library modules, constructs all occupied-subset states of cardinality at least two for \(m=1,\ldots,6\). It writes the complete first-passage linear system with exact rational rates, solves it by fraction-preserving Gaussian elimination, and compares every state's exact expectation with the displayed harmonic formulas. Result: **219/219 checks pass**, including all-occupied states. The all-occupied means at graph orders 2–7 are respectively \(1/2,4/3,15/8,34/15,185/72,197/70\).

The sample program also checks the equality/strict-improvement boundary against the fully occupied complete graph. It is not claimed to exhaust arbitrary graph order, prove bibliographic uniqueness, or supply independent audit evidence.

To reproduce: `python verify.py`. No external data or libraries are required.
