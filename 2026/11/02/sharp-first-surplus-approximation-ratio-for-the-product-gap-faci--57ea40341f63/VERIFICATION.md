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

# Verification of the first-surplus Product-Gap law

The proof uses the exact normalization and costs of every omitted-agent outcome; its main theorem is analytical for every real gap vector and does not depend on any finite test. The supplied `verify_gap_product.py` is reproducible with standard-library Python 3 and performs independent exact arithmetic.

Run `python3 verify_gap_product.py` from the extracted files. It enumerates all 1,089 positive integer gap vectors with lengths two through six and entries one through three, an additional 2,000 seeded rational vectors, and 30 limiting-family members; 3,119 inputs in total. Each test constructs every possible retained-report subset, independently multiplies its selected spacings, computes the exact cost of the omitted report, and verifies identity (1) and the proposed upper bound. It also verifies the explicit limiting-family rational ratio. A successful run does not certify unrestricted novelty or provide an independent scientific audit.

Boundary treatment: repeated reports imply zero optimum and zero mechanism cost, so no positive-denominator ratio exists. For positive gaps and at least two facilities, the supremum is strict at every finite report configuration.
