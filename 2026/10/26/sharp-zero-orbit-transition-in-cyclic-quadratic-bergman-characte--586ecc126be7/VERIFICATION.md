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

The beta integral gives the reciprocal squared monomial norms binomial(n+3,3). Extracting the progression yields t^r P(t^q)/(6(1-t^q)^4); expansion confirms P(1)=6q^3 and the factored P(-1). The numerator recurrence gives alternating signs at old roots, a sign change before zero, and an extra root on the left when degree increases. Its degrees through m=0,1,2,3 are nondecreasing with unit increments or plateaus, including q-r-1=0,1,2 by the explicit coefficients. Thus all residual roots are simple and negative. Except at (2,1) the quadratic factor of P(-1) is positive. Endpoint-sign parity combined with the product of the root moduli rules out three interior s-roots below q=2r+4 and zero above it. At equality the reciprocal pair straddles -1 and the remaining root is -1. At (2,1) P(s)=24(1+s). Every s in (-1,0) lifts to one attainable orbit of q simple nonzero products; the boundary s=-1 does not lift to attainable products, and the forced t=0 zero is separate, including in the exception. The frozen script and output were inspected, not executed; the reported Sturm sweep to q=60 is corroboration only.

## originality

PASS

Prior work directly covers cyclic averaging and simple negative Veronese roots; the supported distinct claim is the exact count in the open unit disk with its boundary case and exception, not the averaging or sign-of-roots result. No inspected source established that count.

## value

PASS

The exact magnitude cutoff distinguishes genuine zeros of a projected disk kernel from formal numerator roots. It locates the first two-orbit sector at each residue and separates both boundary escape and the exceptional sector. That information is usable for deciding which projections of the zero-free full-space kernel acquire nonzero zeros, and is not provided by negative real-rootedness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
