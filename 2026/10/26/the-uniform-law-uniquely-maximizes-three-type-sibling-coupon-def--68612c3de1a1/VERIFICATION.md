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
Run `python verify.py` with Python 3 and SymPy. The script computes the formula independently from the stated rational form, factors \(7/12-\operatorname{Var}(U)\), checks the exact 140 nonzero positive coefficients and the displayed denominator, and checks seven exact-rational finite-state recursions that use occupancy status truncated at two. `CERTIFICATE.txt` prints every nonzero numerator coefficient. `verification-output.txt` records the actual completed run. These exact symbolic checks establish an elementary polynomial identity and show strict positivity, not an independent audit of the proof or novelty. Full-text inspection of one relevant cited paper was unavailable.
