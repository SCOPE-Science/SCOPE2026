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

# Verification of the support-stratum enumerator

Run `python checker.py` with Python 3 and no third-party modules. It independently constructs each allowable partial bijection on \([n]\), computes both partial compositions as literal tuples of image values, and checks all three ranks. A separate exact-fraction formal-series recurrence computes the claimed coefficient polynomial and compares **all** its coefficients with the direct enumeration.

The checked prescribed-power families are \((1,1),(1,3),(2,2),(2,3)\) through \(n=5\), and \((3,3),(2,4)\) through \(n=4\). A finite subgroup-closure algorithm, independent of Hermite normal form, verifies subgroup index multiplicities for \(C_2\times C_2\), \(C_2\times C_3\), \(C_3\times C_3\), \(C_4\times C_4\), \(C_2\times C_6\), and \(C_4\times C_6\). Brute force checks triples of commuting involutions for \(n\le3\). All tests must report `ALL_EXACT_CHECKS_PASSED`.

The proof of the unlimited parameter range is the structural bijection, orbit counting, and Hermite normal form argument in RESULT.md. Exhaustive finite tests cannot alone prove the general formula. Neither an independent mathematical audit nor a formal proof-assistant certification has been performed.
