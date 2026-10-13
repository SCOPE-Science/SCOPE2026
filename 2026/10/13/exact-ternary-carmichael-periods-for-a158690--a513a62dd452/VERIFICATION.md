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

# Arithmetic verification

The coefficient identity \(n![t^n](e^{-t}-1)^k=(-1)^n k!S(n,k)\), the inclusion–exclusion identity, and the binomial congruence for \(k^{2\cdot3^{r-2}}\) are proved in `RESULT.md`. The finite contributions \(H_m\) for \(1\le m\le4\) have at most sixteen subsets each. For \(m\ge5\), pair subsets using the addend nine, proving a universal cancellation rather than extrapolating from a bounded enumeration.

`verify_ternary.py` computes the first 111 coefficients by two independent exact-integer modular algorithms, verifies their agreement modulo \(243\), confirms the known OEIS initial coefficients, and tests 764 shifts for \(r\le5\). It also recomputes the finite derivative-residue table. To replay, run `python3 verify_ternary.py`; the actual output from the package run is in `replay.txt`.

These tests do not constitute exhaustive verification of all \(r\) or \(n\); the displayed proof provides those quantifiers. The prime-two and other odd-prime cases, as well as optimal preperiods, remain outside scope.

