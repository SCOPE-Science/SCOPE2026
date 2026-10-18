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
# Reproducible finite checks

Run `python3 artifacts/verify.py` with a standard Python 3 installation. The script uses no external packages and prints `VALUE_SENSITIVE_MODAL_CERTIFICATES_VERIFY_OK` after checking exact down-set meets, claimed boundary witnesses, equivalence with finite hypergraph transversals, and sharpness of constructions across four representative posets. The checks include a classical three-hyperedge reduction example.

The proof for all finite algebras and arbitrary formula collections is the written Birkhoff-representation argument. The computations do not test all algebras, and the NP-hardness statement is proved by the written many-one reduction, not by execution logs. The direct model-size minimization problem is not considered. Independent audit has not been performed.
