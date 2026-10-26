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

Run `python verify_gauss.py` with Python 3 and SymPy. The supplied deterministic output file records 24 rational incidence bijections, jet ranks, exact geometrically smooth counts 24/0/3048, the sole singular sextic lift at the fixed assignment, and 19 orbit representatives. Geometric smoothness follows from exact Gröbner bases on the three affine charts, not point search over bounded extensions. Binary linear algebra performs exhaustive preimage and kernel enumeration; the projective generators enumerate full orbit closures. No result beyond the three tested degrees is inferred.

The source and output files here are the artifacts actually used for this result. Program output is corroborating reproducibility evidence; the accompanying written proof explains why these finite checks exhaust the entire stated domain. No independent external audit has been performed.
