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

# Verification record

The proof in `RESULT.md` gives the infinite-domain theorem; the accompanying numerical checker is supplementary. To replay, place `verify.py` and `requirements.txt` together, install NumPy, and run `python verify.py`. Expected output: `VERIFY_OK: exact_example=4/3, random_energy_comparisons=210000, sharp_upper_lower_examples=46`.

The calculation evaluates the exact rational normalized stiffness example, many random nodal transforms on isotropic and constant anisotropic triangles, and analytical equality configurations. Finitely many evaluated cases do not certify the universal inequality or originality. This research has not undergone an independent audit.
