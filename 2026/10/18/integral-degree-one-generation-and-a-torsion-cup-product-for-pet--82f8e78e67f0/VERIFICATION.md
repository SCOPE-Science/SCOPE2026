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
# Exact verification

Run `python3 verify.py` with Python 3. The script reconstructs all cells and boundaries, checks that \(\partial_1\partial_2=0\), verifies the configuration one-skeleton is connected and the graph chord basis has parking vertices, constructs six disjoint-pentagon product tori and confirms their rational rank five, then certifies a determinant-\(-2\) minor of \(\partial_2^{\mathsf T}\), its rank sixty-nine modulo two, and a determinant-\(-1\) minor of \([\partial_2^{\mathsf T}\mid C]\), where \(C\) is the integral cup-product matrix. Finally it checks that the displayed torsion combination annihilates each torus and is nonzero modulo boundaries over \(\mathbb F_2\).

Expected terminal output: `VERIFY_OK cells (45, 120, 75) minor_D -2 mod2_coboundary_rank 69 torus_rank 5 unimodular_cup_minor -1 tau_order 2`.

All checks use exact signed integers and finite enumerations. The validity of the product cochain formula follows from the geometric particle-sum map into the six-torus; the script verifies its cellular values and the resulting algebraic certificates. The computation does not independently establish historical priority, determine every alternative ring presentation, or constitute external validation.
