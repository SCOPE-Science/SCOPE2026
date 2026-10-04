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

The finite certificate consists of `artifacts/codes.json` and `artifacts/verify.py`.

The verifier checks, for each of the two displayed codes, that every word has length four over the nine-symbol alphabet, all codewords are distinct, and each ordered pair in the alphabet square occurs in exactly one distinct two-deletion descendant set. It also checks that the sum of the descendant-set sizes is exactly 81. These checks prove perfectness for the two explicit codes.

The surrounding spectrum bounds and previously known sizes are literature inputs and are not re-proved by the verifier. The result does not decide sizes 14 or 15 and does not classify all codes of sizes 16 or 17.
