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

The universal classification is established by a basepoint-free supporting divisor, explicit effective-divisor decompositions on the big side, and sharp negative-intersection multiplicity bounds at the zero wall. All coordinate-grid positions are covered; no genericity assumption is used.

Reproduction: execute `python3 check_grid.py` in the same directory. The checker uses exact rational arithmetic, scans all \(784\) integer pairs \(3\le r,s\le30\), compares the hyperbolic sign to explicit integer multiplicity witnesses at low degree, and verifies the boundary generator degrees and multiplicity inequalities. It prints `VERIFY_OK` when the finite identities hold.

Finite verification does not substitute for the all-parameter proof. Source comparisons include the complete 2026 initiating preprint and relevant sections of the 2022 preprint on the special \(4\times4\) configuration. A prior special-case bi-anticanonical rigidity theorem is acknowledged; no independent audit has been performed.
