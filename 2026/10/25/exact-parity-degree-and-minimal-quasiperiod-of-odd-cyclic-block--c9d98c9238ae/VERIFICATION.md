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

# Reproducible checks
Run `python3 checker.py` with SymPy. The checker performs exact integer transfer-matrix cyclic trace counts; direct original-coordinate enumeration for small cases; rational polynomial interpolation for both parities; and an independent Taylor-series calculation of the signed cone formula. It checks \(m=3,5,7\) when \(a=1\), \(m=3,5\) when \(a=2\), and \(m=3\) when \(a=3\). It verifies equality of the two computed parity differences, their exact degrees, and their rational leading coefficients; the expected terminal token is `ODD_CYCLIC_BLOCK_PERIOD_CERTIFIED`.

The finite tests validate these instances only. The proof covers arbitrary odd \(m\ge3\) and all \(a\ge1\) by a parity image-lattice computation, Brion localization, and a nonzero leading Taylor coefficient. The relevant 2026 manuscript was not accessible in full; historical-priority claims are accordingly provisional. No independent audit has been performed.
