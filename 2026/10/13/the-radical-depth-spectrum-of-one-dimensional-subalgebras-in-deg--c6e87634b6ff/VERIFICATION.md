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

# Reproduction and scope

Run `python3 checker.py` alongside the provided report. The program has no third-party dependencies; it forms an actual exterior basis, handles antisymmetric wedge signs, discards products of degree greater than four, and checks exactly the coefficient-wise cardinalities for the listed finite fields.

Reported computational results: `AB_OK` for \((n,q)=(4,2),(4,3),(3,3),(3,5)\); `FULL_OK` for \((2,3),(3,2),(3,3),(4,2)\); terminal line `VERIFY_OK`. The `FULL_OK` cases enumerate **every** radical element at the listed parameters. The `AB_OK` cases enumerate **every** degree-one/degree-two coefficient pair and use the independently proved free choices of degrees three and four. Lower-dimensional tests check boundary implementation, not an enlargement of the theorem's stated domain.

Exact symbolic checks: the normal form for alternating bivectors (valid in odd characteristic), the decomposition of exterior squares into degree three and four, Gaussian point counts, and the \(q-1\) generators of each nonzero line. These facts form an infinite proof for all prime powers; the executable checks are finite consistency checks only. The theorem does not cover subalgebra dimensions greater than one or exterior quotients with top degree greater than four. Independent audit has not been performed.
