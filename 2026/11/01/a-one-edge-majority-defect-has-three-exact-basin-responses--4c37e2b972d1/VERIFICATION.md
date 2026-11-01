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

Run `python verify_defect.py` with Python 3 and the open-source SymPy library. The included `verification_output.txt` is the actual output of a successful replay. Checks are: nine symbolic side-signature cases compared by exact polynomial expansion; 861,184 concrete class/state compatibility checks over sizes 2–30; 63,504 individual labelled binary state checks over sizes 2–7; and 841 benchmark complete-bipartite checks. All completed successfully.

# Proof boundaries

The general theorem is proved by the exact majority update, finite sign-state partition and symbolic class multiplicity calculation in `RESULT.md`; finitely many checks alone would not establish arbitrarily large graphs. The result does not enumerate individual fixed-point basins. The odd-balanced two-update antecedent is already in Tamuz–Tessler (arXiv:1307.4035, §3.7), and independent external audit has not been performed.
