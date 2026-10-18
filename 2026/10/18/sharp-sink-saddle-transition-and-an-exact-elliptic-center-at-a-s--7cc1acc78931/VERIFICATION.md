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

# Verification

Run `python3 verify.py` in this directory. It uses only Python's standard library. The program checks 320 parameter pairs with exact rational arithmetic, including 1,600 characteristic-polynomial evaluations, exact determinant identities, orbit/quadrant tests, and one exact attracting example. At the algebraic neutral parameter \((a,b)=(-5/\sqrt{29},1/5)\), it checks the center projector, rotation-form identity and 64 successive two-step quadrant visits for three tiny perturbations with floating-point diagnostic tolerance.

The formal proof in `RESULT.md` is necessary for the infinite-parameter claims. Exact finite tests cannot prove the existence/uniqueness for all real parameters or the complete continuum of invariant ellipses. The center-plane construction is rigorously verified there by matrix factorization and preservation of a strictly positive quadratic form. The theorem is local to the strict itinerary. Independent audit: not performed.
