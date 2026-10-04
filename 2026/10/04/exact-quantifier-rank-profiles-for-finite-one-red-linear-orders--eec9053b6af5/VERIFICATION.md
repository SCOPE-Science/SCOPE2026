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
The symbolic proof is the controlling verification. It uses the character recursion for coloured linear orders, the exact monochromatic finite-order threshold, and the elementary split lemma stated and proved in `RESULT.md`.

`verify.py` independently constructs character sets recursively and checks the proposed closed form for ranks 1 through 4 on finite rectangles extending past all predicted truncation thresholds. The latest replay completed with:

- `VERIFY 1 True canons 2`
- `VERIFY 2 True canons 11`
- `VERIFY 3 True canons 51`
- `VERIFY 4 True canons 227`
- `VERIFY_OK`

The computation does not prove the infinite family of ranks. It is a regression check for the induction, boundary cases, and off-by-one thresholds.
