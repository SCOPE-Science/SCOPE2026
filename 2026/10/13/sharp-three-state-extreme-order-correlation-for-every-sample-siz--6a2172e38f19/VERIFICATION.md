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

# Reproducibility and verification

Run `python verify.py` with `requirements.txt` available. The script verifies seven nontrivial symbolic identities using exact polynomial arithmetic, enumerates the full \(3^n\) outcome spaces for four finite sample sizes with rational support points, and checks exact parameter inequalities at 36 additional integer sample sizes. The verifier completed with the message `PASS: 7 symbolic identities, 272 exact rational diagnostics`.

The mathematical proof handles all integers \(n\ge4\) and all allowed real support triples by showing that the affine derivative certificate \(H(z)\) has two strictly positive endpoint values. The finite exact checks do not prove an unbounded assertion, and the positivity of its polynomial factor \(B(r,x)\) is established analytically in RESULT.md. No independent audit or outside mathematical certification has been performed.
