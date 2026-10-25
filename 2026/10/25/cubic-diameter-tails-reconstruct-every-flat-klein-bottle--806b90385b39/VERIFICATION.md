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

Execute `python3 verify.py` with Python 3 and no third-party libraries. The bundled script checks the parity-class shortest-distance reduction against direct minimization over nearby deck transforms using exact rational arithmetic for 3,500 point pairs across five parameter configurations, plus five exact maximizing configurations. It also checks the small-radius disk-law numerical integral and cubic tail coefficient for four aspect ratios; tests the equal-area, equal-diameter nonisometric swapped-period pair exactly; and compares the one-dimensional CDF integral with direct independent point sampling of 180,000 pairs at three thresholds.

The reported checks passed before packaging. Simpson quadrature approximations use explicit finite numerical tolerances; they do not certify the asymptotic statement. Direct deck enumeration is finite and only serves as an exact-rational check for sampled points, not as a proof for arbitrary points. General validity is proved in `RESULT.md` by the complete even/odd deck description, Haar independence, and dominated convergence of the compact scaled terminal region.

Independent scientific audit has not been performed; no external validation is asserted.
