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
# Verification

Run `python3 check_avalanche.py` in a Python 3 environment (standard library only). The checker reconstructs the parallel-firing support sets from the actual initial configuration, checks containment of later firing sets, enumerates the first-period intersection nerve, compares to the explicit complement-of-edge nerve, and performs reduced mod-two simplicial homology calculations. All 108 two-hole configurations and all 996 generic-motif configurations recorded in the program passed. Its stable digest of the two-hole case records is `35432691bbad8b43c8e8863a3431c9f7354afa8f13982896828eda9dc8c078a6`.

For the unrestricted claim, verify the symbolic path firing formula, the inclusion of later firing sets, the existence of the second-block intersection witness, the graph component count for residue increment \(h\), the cycle-independence suspension recurrence, and the exact integral Alexander-duality index shift. Finite mod-two tests alone neither establish torsion-freeness nor prove all positive integer parameters. The algebraic-topological proof is given in RESULT.md. No independent audit or formal certification has been performed.
