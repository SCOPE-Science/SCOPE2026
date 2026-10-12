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

Run `python3 verify.py` from the package directory (Python 3 standard library; no downloads or third-party packages).

Observed run result:

`VERIFY_OK algebraic_spectrum=10 nontrivial_Fourier_modes=9 torus_points=1024 offsets=10 cesaro_profiles=10`

The exact enumeration for frequency differences \((a_j-a_{j-k},b_j-b_{j-k})\) gives the following counts for the three relevant frequencies \((0,0)\), \((1,-2)\), and \((-1,2)\):

| Shift \(k\) | Zero | Positive target | Negative target |
| --- | ---: | ---: | ---: |
| 1 | 0 | 0 | 0 |
| 2 | 2 | 2 | 2 |
| 3 | 0 | 0 | 0 |
| 4 | 2 | 2 | 2 |
| 5 | 0 | 0 | 0 |
| 6 | 2 | 2 | 2 |
| 7 | 0 | 0 | 0 |
| 8 | 2 | 2 | 2 |
| 9 | 0 | 0 | 0 |

These finite counts exhaust all Fourier shifts on the **fixed ten-vertex graph** and, together with the exact character moments, constitute the algebraic cancellation certificate. The independent \(32\times32\) torus quadrature checks all ten displacement probabilities to floating-point tolerance, but numerical quadrature does not prove exact time realizability. That relies on the separate full-support convex-geometric argument and irrational Kronecker density. The six-time existence assertion is exact, not a displayed numerical witness. Neither optimality of six times nor any higher-order cycle classification is asserted.
