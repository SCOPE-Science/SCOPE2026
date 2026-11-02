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

# Verification

Run `python3 verify.py` using the Python standard library. The program returns a nonzero exit status if an assertion fails. The verified execution returned:

`PASS: 499367 exact checks; n <= 100 exact sign/identity tests; independent set-partition enumeration n <= 9 and uniform-box allocations n <= 6`

These checks cover the exact moment formula, positivity and sign patterns of every feasible conditional size, strict increase of the normalized covariance for at least three blocks, exact weighted covariance cancellation, the special two-block case, and the zero example at \((n,k,s)=(6,3,3)\). Exhaustive restricted-growth enumeration checks every labeled set partition through nine elements. Exhaustive box assignments independently establish small-case occupancy consistency.

Finite verification does not prove the theorem for unbounded \(n\); that conclusion follows from the strict coefficient log-concavity lemma, marked-block counting, and excess-balance identity reconstructed in `RESULT.md`. The source comparison is not an exhaustive historical priority guarantee.
