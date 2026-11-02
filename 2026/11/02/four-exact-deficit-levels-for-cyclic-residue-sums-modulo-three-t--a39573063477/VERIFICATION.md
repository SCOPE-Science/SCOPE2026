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

# Verification details

Run `python3 verify.py` using Python 3 and standard library only. The verifier checks the explicit CRT lift subgroups for each allowed order with exponents from four through twelve, including group closure, exact sizes, and the four expected deficits. It independently generates every cyclic subgroup in the full multiplicative unit group for each exponent from four through nine, confirms that there are four at each order at least four, and that the unique centered subgroup has two elements and contains minus one. Its output is deterministic: `VERIFY_OK symbolic_CRT_order_cells= 45  independent_full_unit_group_subgroups= 132  a=4..9  modulo3_character_and_sums=PASS  finite_only=YES`.

The unbounded proof is supplied in RESULT.md; this finite computation is a cross-check, not exhaustive evidence for all parameters. A separate independent audit has not been carried out.
