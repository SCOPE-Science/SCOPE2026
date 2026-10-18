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

Run `python3 check_spectrum.py` with Python 3 and its standard library; no network or third-party packages are needed.

The script constructs all zero-divisor–unit incidence entries from the algebraic coordinate-equality characterization, builds the exact integral Gram matrix, calculates its characteristic polynomial with Newton identities, and compares the complete coefficient list against the closed eigenvalue/multiplicity formulas. For products of prime fields it also independently tests the actual condition that the coordinatewise sum has a zero coordinate. Every assertion passed in 13 field-order configurations including \((4,4,4)\). The final program output is `VERIFY_OK: exact Gram characteristic polynomials and nonprime-size combinatorics`.

The exact mathematical proof is in `RESULT.md`; finite tests do not constitute a proof for unbounded numbers of factors or field orders. Tests over nonprime orders use labels of nonzero elements and the observation that additive negation is a bijection; this is sufficient for the incidence relation but does not implement arbitrary extension-field arithmetic. No external independent audit was performed.
