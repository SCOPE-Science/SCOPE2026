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

The analytical proof in `RESULT.md` derives the latent covariance and third-order identities, gives a unique inverse, and constructs an arbitrarily near three-season observational alias. Those are the unrestricted claims. The standard-library-only `verification.py` independently enumerates complete hidden and observed histories with exact rational arithmetic. Running it writes `certificate.json` to the current directory.

Four rational parameter cases are checked, including negative temporal memory and stationary occupancy one half. Each of the four 16-atom observed laws is inverted exactly, and one eight-atom three-season observed law is shown identical for two distinct strict parameter vectors. The generated certificate has been compared with the packaged certificate exactly. Finite enumeration is not the proof for every real-valued parameter vector and does not establish novelty. Population-law identifiability does not guarantee finite-sample precision, especially for weak temporal dependence or low detection contrast.
