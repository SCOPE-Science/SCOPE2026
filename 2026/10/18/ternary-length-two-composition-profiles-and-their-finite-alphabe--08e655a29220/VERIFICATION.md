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

# Reproducibility notes

Run `python3 verify.py` in the same directory as the supplied standalone script. It uses only the Python standard library and assert-based exact integer checks. Successful execution prints `ternary word enumeration PASS: n=1..11`, `independent ternary graph enumeration PASS: n=1..28`, and `four-letter structural lemma PASS: n=1..7`, followed by the coefficient list, the value 282873 at length 28, and the denominator coefficients.

The first checker obtains the factor-composition multiset directly from **every word** of the indicated lengths; the second enumerates **all unordered looped multigraph edge-multiplicity vectors** and applies only connectivity and degree parity; the third changes the alphabet to four symbols. In addition, the numerator and denominator recurrence is evaluated with exact integers. All three checks were executed successfully from the actual script before packaging. The infinite formulas rely on the separate written proof, not on finite extrapolation.

No external mathematical certification or independent audit was conducted.
