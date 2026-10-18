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

# Reproduction

Run `python verify_unitary_density.py` with Python 3.10+ and NumPy installed. The checker employs exact rational atanh enclosures and exact `uint64` integer mass convolution, with explicit overflow safety checks. The required result is `lower_mass 772112456436` and the exact rational bound `384705031419237/498500000000000`, finishing with `VERIFY_OK`. A separate upper-envelope diagnostic may appear, but no originality claim is made for that diagnostic. The infinite-domain step is the analytic squarefree-tail union bound, not a numerical enumeration. Independent mathematical audit is not performed.
