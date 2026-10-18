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

Run `python3 verify.py` using only the standard Python library. It generates the full three-particle graph-configuration chain model for \(K_{3,4}\), all \(144\) graph automorphisms and signed action traces, and exact modular matrix ranks. All consecutive differential products are checked zero. Nine transpositions forming a generating set are checked for chain-equivariance; group composition extends this to the entire automorphism group. Independent orbit-series traces agree at every element, and all fifteen irreducible characters are orthogonal with the claimed multiplicities. The script reports `VERIFY_OK` on success.

Finite-field ranks are used solely as lower bounds for rational ranks; the geometric surjective first-homology map establishes the necessary complementary bound. No integral homology torsion statement or independent scientific audit is certified.
