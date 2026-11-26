---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The numerical and equality statements are unchanged in the repaired RESULT.md. Centering the affine basis gives coefficient 12 on the second moment; integrating the primitive of f=g' against it yields the real kernel 1_{t<=x}+t-1-(6x-3)t(1-t), with zero signed integral and antisymmetry under (x,t)->(1-x,1-t). On 0<=x<=1/3 put c=1/(3-6x), u=c-x>0. Twice the negative mass is u^2(1-c+2u/3)/c. On 1/3<=x<=1/2 it is 2 times the integral of t(1-a+at) over [0,x], for a=6x-3, giving 4x^2(1-x)^2. An independently evaluated exact symbolic integration/differentiation in SymPy verified these masses, the derivative factorization and the junction and endpoint values; the uploaded checker was inspected, not run. On the first branch the two other quadratic factors are positive and the denominator is negative, so the derivative changes from negative to positive only at (3-sqrt(3))/6; the second branch ends at 1/4. Comparing 8/27, 16/81, and 1/4 and reflecting gives strict global rigidity. Equality in the integral bound requires saturation of the derivative magnitude and a common complex phase times the kernel sign almost everywhere, giving exactly the two specified kink profiles up to scaling and constants. This covers every Lipschitz input, including the separate zero-seminorm case.

## originality

PASS

The frozen comparison omitted a same-day exact endpoint overlap. The repaired RESULT.md explicitly credits that comparison and makes the contribution the strict global comparison over all evaluations and resulting full uniform-norm equality classification, not the already covered numerical endpoint calculation. Reassessed PASS for this scope; no chronological priority inferred from a shared date.

## value

PASS

Endpoint error alone permits worse interior error and does not classify equality for the sup-norm residual over the whole interval. Deciding that comparison and exhaustively identifying worst-case profiles is useful for sharp Lipschitz-to-uniform distortion of affine detrending, even without claiming the endpoint computation as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
