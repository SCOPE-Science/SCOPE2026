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

# Verification instructions and limits

Execute `python3 verify.py` from the extracted package root. The verifier needs only the Python standard library. Its `EXPECTED` table contains the 13 finite equality-pattern coefficients used in the proof; the script *independently recomputes* these coefficients from all four-letter outputs with zero or one fixed outside symbol, and refuses to pass if a coefficient disagrees. It also verifies the exact symbolic affine-over-alphabet identity at several distinct alphabet sizes for each pattern, then exhaustively compares every pair of centers for each integer alphabet size from two through six. Successful completion prints `VERIFY_OK`.

The full-domain theorem does not rely on induction from those sample alphabet sizes. The argument that at most one outside symbol can appear in any common output proves the symbolic reduction for every alphabet size. There are exactly 13 distinct-center equality patterns, and their coefficients require only finitely many direct sums (alphabet sizes at most five, for the one-outsider tests). The checker does not independently establish originality, importance, or an external scientific audit. The claims apply only to exact-two-insertion multisets with distinct insertion vectors and do not address the non-multiset channel model.
