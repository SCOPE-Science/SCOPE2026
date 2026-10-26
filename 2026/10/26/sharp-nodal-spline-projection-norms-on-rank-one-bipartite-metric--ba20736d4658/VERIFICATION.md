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

# Reproduction and exact checks

The complete proof is in `RESULT.md`. The standalone `verify.py` requires only Python's standard library and can be run using `python verify.py`. It independently assembles the exact edgewise nodal Gram matrix, inverts it using rational Gauss–Jordan elimination, integrates the absolute value of the affine projection kernel exactly, and compares every vertex row against the closed formula. Its test cases cover \(2\le a,b\le5\) with three positive integer-factor profiles on each side, i.e. 144 ordered configurations (some may be duplicates for small sizes); no floating-point comparisons are needed. The output from actual execution was: `exact weighted bipartite graph families checked: 144`.

The algebraic proof separately verifies the inverse matrix by multiplication and reduces the norm to an exact elementary integral for *all* positive real factors and graph sizes. These computer experiments cannot establish a universal statement or prove priority. The integer-weight test profiles cover only a finite set. There is no independent audit or external certification.
