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

The proof first reduces all affine minorants of \(f(x)=a x^2/2\) to tangent minorants at fixed slope. It then derives the exact target-sublevel distance and factors the loss from the optimal tangent as a square. The exact-gap and above-gap cases are treated separately because attainment changes there.

`artifacts/verify_w_certificate_quadratic.py` checks the subgap envelope and W-threshold in exact rational arithmetic using rational \(q\) with \(r=1-q^2\). It also checks the strict finite-slope gap at \(r=1\) and a concrete certificate for a trial modulus strictly above the true modulus.

The finite replay does not prove uniqueness over all real slopes; that follows from the square-factor identity in `RESULT.md`. Higher-dimensional, constrained, and bundle-generation questions are outside scope.
