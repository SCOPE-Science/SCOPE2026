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

# Reproduction

Execute `python verify.py > verification_certificate.json` with Python 3, using the standard library only, from the directory containing the extracted files. Exact fractions are used for all test values. The output must byte-match the supplied `verification_certificate.json`.

The script performs 51,980 comparisons between the direct sitewise probability sum and the geometric-sum formula, 5,980 constrained-separation centering tests, 460 full-versus-centered optimizer checks, 15 exact polynomial identities for small lengths, and 20 seven-site optimality/phase checks. It provides finite, independent consistency checks. The universal centering result, exponential large-length bounds, and uniform limiting product-distance argument are analytical proofs in RESULT.md, not claims inferred from finite tests.

The original assumptions include conditionally independent detections, integer path distance, exactly two distinct traps, geometric distance decay, and a uniform single target site. Independent audit remains unperformed.
