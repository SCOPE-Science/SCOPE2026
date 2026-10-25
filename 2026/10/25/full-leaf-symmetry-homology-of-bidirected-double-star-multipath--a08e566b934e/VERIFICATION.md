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

Run `python3 verify_double_star_equivariance.py` with Python 3 from the directory containing this document. The script enumerates every allowable directed-arc face without using the source's cone formula. For the complete balanced group at (3,3), all 72 signed reduced Lefschetz traces matched the stated full-group characters. At (3,4), all 144 leaf-permutation signed traces matched. Independent mod-two boundary ranks gave degree-(2,3) reduced Betti ranks (8,1) and (12,5), respectively. Last output is `VERIFY_OK`.

The checks are finite. The universal conclusion, including integral lattices and the full balanced coset, rests on the displayed equivariant pair exact sequence and sign of join-factor interchange. The computation supplies no independent research audit and does not establish universal novelty.
