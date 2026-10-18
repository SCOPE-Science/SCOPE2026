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

# Computational verification

Execute `python3 verify.py` using a standard Python 3 interpreter. All arithmetic is exact, and the script reads no external data or packages.

The script independently constructs the overcubic one-tuple generating series by (1) formal inversion of a signed theta-series product and (2) a direct finite Euler-product expansion; agreement is asserted through degree 191. It derives the integral fourth-power correction, tests even support of the quadratic correction modulo 2, and checks the special coefficients needed for sharpness. It then tests the universal odd-index lifting formula for 20 parameter pairs \((i,k)\) with \(3\le i\le7\), \(0\le k\le3\), at every odd degree \(1\le n\le191\): exactly 1920 comparisons. All required progression congruences through the same degree and sharpness at degrees 5 and 7 are also checked.

Recorded execution result: `VERIFY_OK exact_integer_checks=1920 i=3..7 k=0..3 N=191 sharp_both=True`.

The finite tests do not prove the theorems for unbounded indices or parameters; that conclusion follows from the formal-series identities and the cited published triple congruences.
