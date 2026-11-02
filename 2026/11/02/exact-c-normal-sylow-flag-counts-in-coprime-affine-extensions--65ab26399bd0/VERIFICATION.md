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

# Reproducibility and verification

Execute `python3 verify.py` using Python 3.10 or newer. The script uses only the standard library. Successful execution prints `VERIFY_OK` and `MULTI_VERIFY_OK`. It independently enumerates all vector subspaces and maximal flags for nine cyclic actions and three noncyclic complement actions. For three small cyclic groups it also enumerates the complete subgroup lattice, normal subgroups, and all conjugations of the semidirect product, checking c-normality directly against its defining normal-supplement condition.

The cyclic field/dimension cases include \((p,n)=(2,2),(2,3),(3,2),(3,3),(5,3)\), both diagonal and irreducible actions. Noncyclic checks include independent involutions over \(\mathbb F_3\) and two independent order-four diagonal generators over \(\mathbb F_5\). For the two moving characters in \(\mathbb F_5^3\), the checker obtains \(62\) qualifying flags among \(186\) full flags. In contrast, a repeated moving character yields \(186\), and the irreducible \(C_3\)-action on \(\mathbb F_2^2\) yields zero.

The general proof, not the finite enumerations, establishes the classification for all prime fields, dimensions, and finite coprime complements. No independence from the mathematical review is asserted.
