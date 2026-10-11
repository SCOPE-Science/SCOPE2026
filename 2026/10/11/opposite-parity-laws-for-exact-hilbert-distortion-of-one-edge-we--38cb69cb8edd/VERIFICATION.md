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

# Verification details

The exact proof is in `RESULT.md`, including the graph quotient identification, the symmetrization argument over every Euclidean pullback, the cube-section vertex exhaustion, the branch comparison, and the derivative signs. The accompanying `verify.py` checks the key formula by independently constructing cube-section vertices, projecting edge generators, and evaluating primal and polar quadratic forms with exact rational arithmetic.

Command: `python verify.py` (Python 3 standard library). On the checked build, the script printed `Exact rational instances checked: 56 ALL_PASS`. All represented dimensions \(3\le n\le10\) and rational edge lengths in the test set passed. A finite test cannot certify the theorem for all real parameters; the algebraic proof supplies that quantification. Real Banach--Mazur distance and only one shortened edge are covered. No external or independent audit has been performed.
