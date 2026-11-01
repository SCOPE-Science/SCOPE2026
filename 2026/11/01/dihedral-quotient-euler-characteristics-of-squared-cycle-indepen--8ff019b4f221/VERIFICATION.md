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

The standalone `verify.py` enumerates all admissible vertex orbits for each rotation and reflection of the squared cycle, evaluates signed alternating sums, compares those to the recurrence expressions, and checks quotient integrality for lengths 6 through 500. The direct enumeration covers every one of the 2n dihedral actions at n=6,...,22. Run `python3 verify.py`. The last line is `CHECKS_OK`.

These finite computations do not by themselves prove any assertion for unbounded n. The written proof establishes the orbit-graph reductions, recurrence identities, and asymptotic nonvanishing argument. Ordinary quotient homology is only addressed rationally; integral torsion, individual Betti numbers, and equivariant homotopy are not determined.
