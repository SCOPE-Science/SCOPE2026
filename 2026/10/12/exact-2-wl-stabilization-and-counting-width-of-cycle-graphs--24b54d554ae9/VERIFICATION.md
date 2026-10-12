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

The theorem has a uniform proof; computation is used only as an independent finite consistency check.

`artifacts/verify.py` directly implements standard ordered-pair 2-WL refinement from the atomic coloring. It checks every cycle from order \(3\) through \(60\), verifies the complete distance-color profile at every round, and compares the observed stabilization round with the closed form. A separate arithmetic sweep checks the equivalent stopping criterion through order \(4096\). It also instantiates the 2-regular lower-bound competitor \(C_3\dot\cup C_{{n-3}}\) throughout the direct-test range.

Expected output:

`VERIFY_OK full_2WL_cycles_3_60 formula_cycles_3_4096 width_witnesses_6_60`

The finite checks do not prove the theorem for unbounded \(n\); that role is played by the distance-doubling induction in `RESULT.md`. The script uses only the Python standard library.
