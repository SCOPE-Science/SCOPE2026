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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 interpreter. The program enumerates permutation orders by the complete cycle-partition recurrence, enumerates every divisor of the group exponent, computes the forced residual second covering integer in two mathematically different ways (entire order set versus prime-power vertices and edges), checks they agree for every divisor, verifies each optimum and its witness, and prints the complete 38-row table. A successful run ends with `ALL ORDER AND PRIME-POWER GRAPH CROSSCHECKS PASSED`.

At degree 40: 495 distinct element orders, 19 prime powers, 105 compatible graph edges, 36,864 potential first covering exponents. `verification_output.txt` is an actual recorded execution. The graph if-and-only-if theorem for all degrees is proven mathematically in `RESULT.md`; the program checks only the claimed finite range, with no extrapolation or claim of independent certification.
