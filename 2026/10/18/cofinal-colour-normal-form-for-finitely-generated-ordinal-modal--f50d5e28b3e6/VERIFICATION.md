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

# Reproducibility
Execute `python3 ordinal_modal_verify.py` using a standard Python 3 installation. Expected output: `ORDINAL_MODAL_COFINAL_LAYER_NORMAL_FORM_OK 6554`.

The script tests 6,554 exhaustive color-words with one, two, or three Boolean generators on finite ordinal frames, comparing iterative normal-form atom counts with modal closure under Boolean operations and the reflexive ordinal diamond. It confirms all finite instances in those ranges. The transfinite theorem relies on the self-contained ordinal-descent proof and is not certified by the finite script. No independent audit has been performed.
