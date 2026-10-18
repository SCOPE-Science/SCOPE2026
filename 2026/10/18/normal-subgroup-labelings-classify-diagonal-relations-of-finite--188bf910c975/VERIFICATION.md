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

# Reproducibility

Run `python3 verify.py` with Python 3 and the standard library. No external packages or network access are required. The verifier was executed using the file accompanying this result and completed with `VERIFY_OK`.

It enumerates every diagonal support on chains through size five using two independent prefix codes, computes all intersections with the ambient grid downsets, and obtains the exact counts \(2,17,337,12152,696076\). Independently, it tests all \(4096\) reflexive binary relations on the four-element semigroup \(C_2\times C_2\), retaining exactly \(17\). It then tests direct multiplication for all subgroup-fiber assignments over \(C_3\times C_2\), retaining exactly \(337\).

A separate test finds all subgroups of \(S_3\times S_3\) containing its diagonal, with orders \(6,18,36\). Assigning them independently to the cells of every diagonal support over the two-chain and testing compatibility produces exactly \(46\) valid relations, matching the three-level normal-subgroup lattice. Direct restricted-growth-string partition enumeration verifies the congruence formulas for \(C_n\times C_p\) at \((n,p)=(1,2),(2,2),(2,3),(3,2)\) and for the four-element diamond meet-semilattice times \(C_2\).

These experiments establish only the finite cases actually enumerated. The general result for every finite group and finite meet-semilattice with top is proved in `RESULT.md` by the group-fiber and congruence arguments. This is not external or independent mathematical validation.
