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

The pure-Python `verify_energy.py` constructs finite fields, enumerates the image of the norm-perturbation map, computes all ordered pair-sum multiplicities and their squared sum, and checks the closed formula. Checked nine prime-power fields (including degrees two over 3 and 5).

Recorded replay: `VERIFY_OK fields= 9 total_image_points= 919 total_energy= 24033255`. Finite replay is corroboration, not a universal proof. The proof uses a full Fourier expansion and standard Gauss-sum identities; no external independent audit was conducted.
