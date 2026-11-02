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

Run `python3 dodeca_exact.py` to reproduce the exact quadratic-field certificate. Output file `dodeca_exact_output.txt` records 92 complete sign chambers (6-sided section: 20, 8-sided: 60, 10-sided: 12) and exact angle cosine multisets. Each chamber is defined by strict signs of twenty vertex height functionals. The program checks the 120 nonzero determinants of triples of the ten antipodal vertex normals and constructs all chamber rays as exact cross products. Each facet is enumerated independently from supporting icosahedral normals. Run `python3 dodeca_law.py` for an independent numerical reconstruction and spherical area computation; this is corroboration only, not an infinite proof. The theorem rests on the exact finite enumeration plus spherical Girard excess. External independent audit has not been performed.
