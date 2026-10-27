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

# Reproducibility and limits

Execute `python verify.py` using Python 3 and SymPy. This computes grounded-Laplacian solutions with exact rational arithmetic for all tested graph edge columns, verifies the Laplacian source equations, and checks the predicted norms against the maximum column sums. Additional symbolic rational-identity checks cover the paired-cross currents, matched-edge comparison, and equality of the two formulas at the branch boundary.

Observed result: `MATCHING_SATURATION_HODGE_EXACT_OK graphs=333 checked_edge_columns=17298 symbolic_identities=PASS`.

The program tests finite parameter ranges, not all integers. The unrestricted proof, including positivity and every case split, is in RESULT.md. No external independent audit has been performed.
