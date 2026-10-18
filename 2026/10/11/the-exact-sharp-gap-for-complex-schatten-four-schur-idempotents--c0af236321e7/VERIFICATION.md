---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The Schatten-four identity is (sum squared moduli)^2 minus twice the squared determinant. The adverse complex phase and off-diagonal balancing reduce the triangular mask to a two-real-variable quartic ratio. Eliminating the killed diagonal gives the unique positive stationary t satisfying t^3+4t^2+3t-1=0; independent symbolic differentiation gave -4(3t+2)(t^3+4t^2+3t-1)/[(1+t)^5(t^2+4t+2)^2], so the critical point is the maximum and endpoints give the lower ratio. The sharp norm is 1.037541006105634...; the explicit matrix attains it. An arbitrary 0/1 mask either contains a row-column-permuted triangular 2x2 compression or is disjoint rectangular all-ones blocks; in the latter case block-diagonal conditional expectation is contractive on S4. Finite-to-countable passage uses Schatten finite-section density; neither finite enumeration nor random tests alone establish the general assertion.

## originality

PASS

Banks–Harcharras prove a qualitative p-dependent gap and triangle-free/rectangular classification but explicitly leave the precise norm of the 2x2 triangle mask unknown for 2<p<infinity. The assigned exact p=4 root is not a corollary of the qualitative lower bound. Doust 2000/2001 proceedings is a specifically plausible incompletely read precursor; residual risk is recorded, not used as failure.

## value

PASS

The earliest nontrivial multiplier pattern controls a gap for all zero-one Schur idempotents. An exact algebraic sharp threshold answers the explicit 2004 2x2 norm question at the natural even exponent four and supplies an attained smallest-size extremizer; this is a motivated invariant, not an arbitrary simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
