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

# Reproducibility

Run `python3 verify_fiber.py` with Python 3 standard library. It directly enumerates every valid cyclic binary word for lengths 2 through 18, groups words by full six-coordinate cyclic three-gram multiplicity vectors, and independently computes each predicted fiber size from the stated binomial formula. It asserts agreement for every vector and every maximum; the observed terminal output is `EXHAUSTIVE_OK n=2..18`.

The checked range is finite. The all-length proof is the excursion double count and fixed-slice binomial inequality in RESULT.md. No external formal proof certificate or independent validation is claimed.
