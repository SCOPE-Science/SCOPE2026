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

# Reproducibility and limits

Run `python3 verify.py` in this directory. The program uses only the Python standard library and exact integers.

It constructs the analytical joint support–proponent histogram by summing circular-run compositions. Separately, it directly evaluates the local majority at every vertex for every bit pattern at cycle sizes 3 through 18, compares every coefficient, and checks the total \(2^n\). It then recomputes the passage threshold and boundary multiplicities for each odd size up to 101 from the exact joint enumerator, comparing the closed forms. Both kinds of finite checks have passed.

The infinite correctness claim relies on the run-marking bijection, the singleton-flip rule, and the complete critical-case enumeration in `RESULT.md`. Finite enumeration is neither an infinite proof nor a certificate that no equivalent formula already exists. No independent audit or validation has been performed.
