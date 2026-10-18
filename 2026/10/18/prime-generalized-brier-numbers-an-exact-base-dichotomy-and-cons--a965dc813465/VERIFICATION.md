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

# Verification details and limits

The proof reduces the new assertion to (i) a complete local gcd obstruction, (ii) independent unit coefficient congruences in Virbalas's published two-sided covering construction, and (iii) the classical prime-distribution and consecutive-prime theorems for reduced residue classes.

The standalone file `verify.py` was executed with Python and returned:

```
VERIFY_OK exact_local_bases=511 analytic_condition_bases=199488 crt_unit_instances=100
```

The first check exhaustively tests all possible residues modulo \(b-1\) for every \(2\le b\le512\) and verifies that a unit residue avoiding both adjacent forbidden classes exists exactly when \(b\) is even and \(3\nmid b-1\). The second verifies the explicit gcd formula for \(513\le b\le200000\). The third constructs sample CRT systems whose coverage-prime conditions are abstracted to independent unit residues, combines them with the base-power condition and the new residue \(2\pmod{b-1}\), and verifies the resulting full modulus is coprime to its residue.

**Limits.** These finite tests are not an exhaustive verification of Virbalas's covering systems and do not prove any infinitude or prime-density theorem. Those infinite statements follow from the stated covering-system proof and the published prime theorems. No numerical search for an actual generalized Brier prime or minimal modulus is asserted. Every imported theorem is identified in `RESULT.md`.
