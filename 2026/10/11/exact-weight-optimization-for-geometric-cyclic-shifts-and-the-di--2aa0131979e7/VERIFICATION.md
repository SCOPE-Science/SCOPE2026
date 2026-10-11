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

# Reproducibility and verification

The proof in `RESULT.md` applies for all integer dimensions \(n\ge2\), all real ratios \(a>1\), all real exponents \(r\ge1\), and all \(\theta\in[0,1]\). It reconstructs the norm and numerical-radius terms as maxima of positive diagonal entries, determines the unique switching weight from a strictly decreasing function, and classifies global minimizers by monotonic derivatives.

Run `python3 verify_geometric_cycle.py` with a standard Python 3 installation. The script checks the scalar maxima against independently enumerated diagonal entries for selected points and verifies integer-rational power bounds for the explicit smooth case. It also tests monotone-root bracketing and the three-dimensional quartic. These computations are reproducibility checks, not an exhaustive search over arbitrary dimensions or a substitute for the proof.

The first public source date for the motivating weighted inequality is 4 February 2026. No independent audit has been performed.
