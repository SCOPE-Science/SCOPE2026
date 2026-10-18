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

The finite certificates use only `verify.py` and the Python standard library. Execute `python3 verify.py`; its final line is `VERIFY_OK`. The script explicitly lists every odd-prime covering witness and checks all affine coordinates on the two shifted conics, verifies the required line count, and confirms a vertical line covers the unique shared point at infinity. For fields of orders 4, 8, 16, and 32, it constructs the characteristic-two Artin–Schreier-image intercept set and verifies the proposed half-size parallel-line cover over all affine points. Order two is verified directly by its two vertical lines. The mathematical proof of the all-field lower and upper statements is self-contained in `RESULT.md` and is not inferred from these test cases.

No independent audit, expert check, external formal certification, or undisclosed computation is claimed. Unproved limits: optimal odd-field covers outside the listed eight prime fields, and optimal even-field covers in the large binary-span case.
