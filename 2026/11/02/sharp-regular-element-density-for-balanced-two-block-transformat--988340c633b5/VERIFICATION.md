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

# Reproduction and limits

Run `python3 verify_regular_bipartition.py` with a standard Python 3 interpreter. It exhausts all candidate maps and allowed inner inverses for sizes \(m=1,2,3\), checking the exact counts \(4/4,60/64,2400/2916\). The separate Stirling recurrence evaluates the known count without floating-point subtraction of one half. Bisection evaluates the saddle numerically and reports the prefactor \(C=1/\sqrt{xy-(y-1)^2}\) for the regular-element proportion itself. Ratios of the finite correction to \(C\rho^m\) are checked at \(m=40,80\). A successful run prints `VERIFY_OK`.

The computations verify only finite consistency. The sharp limit depends on the analytic occupancy tilt, full-lattice local limit and negligible equal-image contribution proved in `RESULT.md`. The verifier does not establish priority or formal verification.
