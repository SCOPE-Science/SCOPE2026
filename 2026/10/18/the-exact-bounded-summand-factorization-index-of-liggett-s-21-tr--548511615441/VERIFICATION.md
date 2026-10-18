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

# Verification and reproducibility

Run `python p5_checker.py` using Python 3's standard library. The checker rebuilds the thirteen integer coefficients from exact binomial counts and verifies their sum is \(2^{21}\). It then verifies a strict rational Taylor/Rouché inequality in eight root-centered disks, plus disjointness of their twelve real/conjugate disks. It certifies nonnegative (in fact positive) coefficients for the explicit degree-2/5/5 grouping by rational interval arithmetic. Finally, it enumerates all permitted real-root/conjugate-pair groupings of degree at most four, discards only groups with certified negative coefficients, and verifies that even the resulting optimistic candidate groups cannot partition all twelve roots.

This is a finite exact certificate of the stated algebraic factorization and its minimal degree; numerical root-finding is not used as evidence. An external independent audit remains unperformed. No claim concerning other binomial parameters is checked.
