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

Run, in a Python 3 environment with SymPy installed, `python3 verify_affine.py`, `python3 verify_smith.py`, `python3 verify_quotients_directed.py`, and `python3 verify_quotients_sorted.py`. The captured exact outputs are stored in `verification_output.json`. The verifiers reconstruct all eleven-vertex transitive subtournaments without external datasets, identify all affine face orbits under the three explicitly named groups, and test \(\partial_{k-1}\partial_k=0\) for each quotient complex. Two independent quotient verifiers use different simplex orientations and check the same integer Smith factors. Their checks are exhaustive for this finite instance.

The full-quotient CW matrices and degree-one two-cell elimination in `RESULT.md` promote exact homology to the displayed Moore homotopy equivalence. The subgroup conclusions intentionally assert homology only. The nonequivariant calculation is reproduced by code but is credited as known to Govc. These programs are computational verification, not independent mathematical peer review or certification, and neither their execution nor an unrelated homology census establishes originality.
