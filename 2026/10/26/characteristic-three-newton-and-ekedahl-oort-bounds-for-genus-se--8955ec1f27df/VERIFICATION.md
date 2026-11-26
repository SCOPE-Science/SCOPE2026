---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` in this directory with Python 3. It checks squarefreeness and stable Cartier ranks of the two prime-field quintics in the attainment proof, and tests the required order \(M^{(3)}M\) over the exact field \(\mathbb F_3[\alpha]/(\alpha^3-\alpha-1)\), where reversing the product can change the rank. In particular, the branch set \(\{\infty,0,1,\alpha,1-\alpha^2,1-\alpha-\alpha^2\}\) gives stable rank one, not zero. The expected final line is `CARTIER_WITNESSES_OK`.

The proof in `RESULT.md` establishes the all-field theorem and gives a geometric attainment argument for the other profiles. The certificate is not a finite-field census, a formal proof, or expert attestation.
