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

# Verification and scope
The exact algebraic parametrization and exhaustive elementary case analysis in `RESULT.md` prove the theorem. The reproducible standard-library checker `verify.py` tests the equivalence of the gcd criteria across all coprime \(2\le a,b\le120\) and every \(2\le k\le15\) (\(119448\) cases). It also enumerates the full \(17\)-element coefficient-solution set for \((273,55,16)\), confirms every solution is nonprimitive, and checks the stated infinite obstruction family for sample multipliers. The observed output is `VERIFY_OK 119448 all-coefficient witness 17`.

The checker does not prove universality outside the finite tested generator range or prove the infinite-family assertion; those follow from the exact argument. No independent audit or external certification has been performed.
