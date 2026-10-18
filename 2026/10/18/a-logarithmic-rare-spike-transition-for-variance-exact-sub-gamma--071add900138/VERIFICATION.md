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
# Verification record

The proof in RESULT.md was reconstructed from the jump cumulant identity and an explicit \(\operatorname{Beta}(1,2)\) integral. Equation (1) is exact, not an approximation. For any \(\varepsilon\in(0,1)\), the small-argument upper bound is uniformly bounded because \(h_B/\log B\to\infty\), while the complementary \(1/t\) bound gives a global upper scale. The lower scale follows from the spike term at \(t=(1+\varepsilon)h_B/B\). Only after these steps is the limit \(\varepsilon\downarrow0\) taken.

The bundled verify.py provides finite diagnostics of the exact Beta-moment coefficients, selected profile values, and local curvature. It is not an infinite certificate. It can be run with Python 3 and uses only the Python standard library. The source comparison distinguishes the pre-existing variational formula from the new moving-spike asymptotic. Scientific priority and generalizations remain unverified independently.
