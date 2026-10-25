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

The standalone checker `verify_hypercube.py` runs using Python 3 and its standard library. Run `python3 verify_hypercube.py` beside this file. It computes exact rational Walsh-kernel entries for dimensions 3 through 12 and compares the complete two-edge automorphism-orbit list with the incident-edge optimum. It independently forms and inverts grounded Laplacians over fractions in dimensions 3, 4, and 5, confirming the predicted changes for adjacent and nearest-parallel failures, and enumerates the full 66, 496 and 3160 edge pairs, respectively. It checks the exact rational separator at dimension 8. All listed finite checks passed.

The finite program is not an exhaustive check for dimensions greater than 12 and cannot establish the infinite statement. The proof uses the integral heat-kernel representation, strict monotone likelihood-ratio ordering of two integral families, and a five-dimensional exact rational base comparison. The 1992 shortest-path leverage source was accessible only at abstract level. Independent audit has not been performed.
