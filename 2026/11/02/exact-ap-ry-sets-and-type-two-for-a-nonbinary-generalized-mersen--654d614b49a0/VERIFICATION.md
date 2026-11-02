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

## Reproducibility

Execute `python3 checker.py` using Python 3 and the standard library. It constructs weighted coin-change minima independently of the greedy formula and calculates least semigroup representatives for each residue by Dijkstra shortest paths. Direct Apéry computations supply the Frobenius number, genus, and pseudo-Frobenius set without using the claimed formula to generate them. All finite checks passed: 6,342 weighted-change comparisons, 271,591 Apéry-residue comparisons, and 242 independent full-family checks.

## Limits

These are exhaustive tests only over the finite parameters encoded in the checker, not over all admissible integers. The unrestricted assertion follows from the algebraic exchanges, Apéry minimization, and maximal-residue proof in RESULT.md. This record is not independent scientific certification.
