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

# Reproduction and limits

Run `python verify.py certificate.json` from the directory containing this document. The included `certificate.json` is the deterministic expected output, generated from the included `verify.py`; the checker uses no nonstandard Python packages. It recomputes the six shape/clade polynomials and every adjacent coefficient difference, tests the two depth-matched shapes, directly sums exact probabilities for all 64 extinction states for six shapes across four rational marginal extinction probabilities and three rational catastrophe weights, and verifies the expectation identities. Its certificate records 4,926 rational and structural checks.

The general positive-polynomial factorization, the exhaustive six-shape argument, and the arbitrary-size graft are proved directly in `RESULT.md`. Finite tests do not certify untested parameter values or all host-tree sizes. No external independent audit or validation has been performed.
