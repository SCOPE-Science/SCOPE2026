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

# Exact finite verification

Run `python3 verify.py` in a directory containing that file. It uses only Python standard-library types and exact integer bit operations. The first enumerator constructs all \(4096\) reflexive binary relations on the fixed four-world diamond and tests every applicable transitivity and confluence obligation. The second enumerates every four-point preorder independently by generating the equivalence classes and quotient partial order; it returns \(355\) preorders. The two paths must produce the identical set of \(135\) admissible relations. The checker also verifies \((76,29,29,1)\) by endpoint flags, exactly \(27\) side-swap fixed relations, and \(81\) side-swap orbits. Successful output terminates in `DIAMOND_IS4_CENSUS_VERIFY_OK`.

The exhaustive computation is valid as a finite mathematical certificate because the claimed domain is explicitly fixed at four points and every off-diagonal bit pattern is considered. It does not constitute a proof for larger carriers or a claim about independent historical priority.
