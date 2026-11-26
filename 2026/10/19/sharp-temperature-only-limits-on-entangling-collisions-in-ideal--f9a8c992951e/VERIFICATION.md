---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

From the two mixed basis states of each gate the reduced target population is q_k=h q_(k-1)+(1-h)x, with x=p for exchange and x=1-p for anti-exchange; tracing removes the sole off-diagonal pair. Thus q_(k-1)=x(1-z), z=h^(k-1). In the ordered computational basis the inert diagonal entries multiply to xr q(1-q) for both gates (r=1-x), while the sole coherence has squared modulus x^2 z^2 h(1-h). Partial transposition places it in the inert block, making negativity equivalent to F(z)=h(1-h)z^2-r(1-z)(r+xz)>0. The leading coefficient is positive and the constant negative; the unique positive root, in (0,1), rationalizes to the stated z(r,h) since (x-r)^2+4rx=1. Strict inequality makes exactly ceil(log(z(r,h))/log(h)) indices eligible, even at an integer boundary: for example h=1/2 and r=(sqrt(2)-1)/2 give exact zero at collision two. For delta=1-h, z(r,h)>=1/(1+delta/r)>h^(1/r) by the square-root bound and strict logarithmic inequality. The log ratio is positive, smaller than 1/r and tends to 1/r from below as h tends to 1, so every sufficiently weak nonzero angle gives the claimed ceiling, integral 1/r included. At fixed h the plus root is a positive constant times p asymptotically, giving the stated logarithm in 1/p; p=0 leaves the minus gate inert and the plus coherence nonzero at each finite collision. The supplied checker was inspected, not executed: its test combines exact rational signs with floating-point matrices and logarithms; the strict-threshold and uniform-angle arguments are analytic.

## originality

PASS

The assessed addition is the exact ground-target, two-gate pre-reset horizon and its sharp temperature-only maxima over all fixed nontrivial angles. The primary literature already supplies the gates, reduced populations and qualitative transient negativity. The strongest indexed horizon and optimization records treat a maximally mixed target, a condition that changes the exact determinant and even whether the first collision entangles. No claim of originality for the model, fixed points, partial transpose, or logarithmic lifetime as a general phenomenon is credited.

## value

PASS

The count is a natural, measurable boundary for use of a fresh ancilla before reset. The distinction between a universal two-collision ceiling and a sharp bath-dependent inverse-excitation ceiling is qualitative, as is the logarithmic fixed-angle versus inverse-excitation optimized low-temperature growth. This is a complete sharp comparison rather than a parameter example. The count measures neither magnitude nor retained entanglement after reset; attaining a cap near the identity can give very small entanglement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
