---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Inspected the 16-state transfer matrix enforcing both local best-response equations per rung; trace(T(z)^n) bijects with labeled cyclic equilibrium profiles n>=3, including n=3 simple triangle. The source Bareiss code establishes det(I-tT)=(1-tz)^2(1-z^6t^4)(1-t-z^4t^4) by exact 17-by-33 interpolation grid with rigorous degree caps 16,32. Independently constructed its 16-state matrix and computed exact SymPy characteristic polynomials at z=0,1,2,3, matching all factors; independently enumerated every 2^(2n) action profile for n=3..8 and matched full producer histograms. Formal trace/log-derivative gives every binomial coefficient; primitive quartic companion controls exponential growth. Finite n enumeration and four specializations do not alone prove infinite formula; interpolated determinant and algebraic proof do.

## originality

PASS

Best of knowledge after current primary-source reading and searches: Parity response is an affine GF(2) condition and has bounded equilibrium counts, while exact-two response is nonlinear and has exponential counts. Factorization of the precise 16-state matrix yields quartic recurrence, not a generic consequence of equilibrium existence hardness.

## value

PASS

Natural exhaustive census of pure equilibria by endogenous aggregate production on infinite cubic prism networks; explicit binomial law and Perron growth distinguish nonlinear exact-two response from affine parity response on the same graph. Producer-count refinement can be used for welfare/combinatorial benchmarks without requiring a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
