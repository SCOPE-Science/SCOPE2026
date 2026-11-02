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

# Reproducible checks and scope

The accompanying `checker.py` is standard Python 3 and requires no external dependencies. Running it independently enumerates every integer below \(2^M\) for each \(2\le M\le16\) and evaluates the zero-run predicate directly. It compares exact successive-difference frequency counters to the formula, confirms that the support has \(F_{M+2}\) elements, and checks both the count of gaps and their weighted telescoping sum. The replay completed with `ALL TESTS PASSED`.

Computational evidence is finite; it does not prove the infinite classification, which is established by the lexicographic first-divergence and Fibonacci-summation proof in `RESULT.md`. The limiting power-law claim uses Binet's formula and the explicit geometric-tail calculation, not simulation. Checks have not been performed by an independent external assessor.
