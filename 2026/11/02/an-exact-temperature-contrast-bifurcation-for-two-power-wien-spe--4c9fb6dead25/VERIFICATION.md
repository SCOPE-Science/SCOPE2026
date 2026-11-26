---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The unchanged `verify.py` can be run with Python 3, SymPy, NumPy and SciPy. It checks the derivative and background cubic resultant and samples the leading window-opening law. The recorded 85 diagnostic groups pertain to those checks, not to a numerical bound on the remainder. In particular, finite numerical samples do not justify an asymptotic error order. The proof of the remainder in `RESULT.md` uses analyticity and the exact reflection symmetry in the scaled coordinates. To reproduce the leading coefficient, solve \(H_r(x)=\partial_x H_r(x)=0\) near \((r,x)=(2.15664,5.63959)\), and use \(k=-\partial_r H_r(x)\), \(h_2=\partial_x^2 H_r(x)\) at that point in \(K=(4k/3)\sqrt{2k/h_2}\).

This package gives an analytic result for an ideal Wien spectrum, not an observation, laboratory experiment or formal proof certificate.
