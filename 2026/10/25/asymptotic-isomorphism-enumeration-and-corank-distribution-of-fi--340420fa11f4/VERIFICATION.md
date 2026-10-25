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

The proof is self-contained in `RESULT.md`, Steps 1–5. It establishes a uniform absolute error in each corank after normalization by \(q^{n^2}/(n!(q-1)^n)\); it does not claim a relative error for corank growing with dimension.

The exact, dependency-free script `verify_small.py` enumerates all matrices and all admissible natural-basis changes. `python verify_small.py` returned `VERIFY_OK` after exact runs at \((n,q)=(2,2),(2,3)\). An extended exact run covering \((3,2)\) also returned `VERIFY_OK` with 104 monomial orbits and 85 genuine algebra-isomorphism classes. These finite checks verify the necessity of distinguishing monomial orbits from algebra isomorphism; they are not an infinite proof. The fixed-point estimates and corank limits are proved algebraically.

Limits: independently validated mathematical correctness and novelty have not been established; this record reflects self-review only.
