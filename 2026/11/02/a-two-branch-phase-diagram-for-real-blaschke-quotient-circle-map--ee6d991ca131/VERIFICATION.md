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

The complete analytic proof in `RESULT.md` derives the angular numerator, exactly factors both endpoint constraints, reduces same-sign failures to a quadratic discriminant, and proves exact turning-point counts. Strict and nonstrict inequalities are treated separately. The classical harmonic-extension step depends on the established Radó–Kneser–Choquet theorem and is explicitly distinguished from the new boundary classification.

Run `python CHECK.py` with Python 3.10 or later. Using only the standard library, this checks the numerator and endpoint identities in exact fractions, the vertex identity, an exact four-fold witness, and deterministic numerical samples against a separate direct polynomial-minimum calculation. The final local replay printed `PASS: 93744 supplementary exact and numerical assertions`. Random sampling is non-exhaustive and is not evidence for universal quantifiers by itself.

Originality is assessed against inspected primary literature and indexed claims rather than asserted as certified. One closely related published result is only available here as a claim summary, and there remains a risk of an earlier equivalent calculation in unindexed literature. Independent audit has not been performed.
