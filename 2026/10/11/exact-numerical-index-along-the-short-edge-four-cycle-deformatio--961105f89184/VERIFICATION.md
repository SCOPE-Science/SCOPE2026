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

# Verification and limits
The proof is analytic and establishes the complete real interval \(0<t\le1\). It identifies the dual polytope, computes every relevant extreme pairing, proves the optimal universal operator inequality, and displays a sharp rank-one witness. These steps should be checked algebraically without relying on a numerical optimizer.

For an independently reproducible finite sanity check, run `python verify.py` from the same directory as this file. The script uses Python's built-in `fractions.Fraction` and explicitly enumerates the finite rational vertex lists for seven rational values of \(t\). It checks the norm and numerical radius of the stated rank-one witness and the dual decomposition. The actual replay output was:

`VERIFY_OK rational_parameters=7 three_dimensional_vertex_profiles=True analytic_family_proof_required=True`

Finite checks do not prove the continuum theorem, and they do not establish originality. Independent audit has not been performed.
