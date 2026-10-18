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

For H={3,4}, nonnegativity at t=1/2 and 5/14 yields the positive dual certificate sT(1/2)+T(5/14)=1+s-lambda(r+s)>=0, where r=cos(2pi/7), s=cos(pi/7); ratio (1+s)/(r+s)=2r. For lambda=2r, b=(3-10r)/7,c=4(r-1)/7 the Chebyshev quartic factors 32(1-r)(x+1)(x+r)^2(q-x)/7, q=(5+2r-4r^2)/4>1. Equality at x=-1,-r plus interior stationarity determines unique coefficients (determinant 7(2r²-r-1) nonzero). Independently verified factor coefficient-by-coefficient in Q[r]/(8r³+4r²-4r-1) using Sympy polynomial remainders; numerically q≈1.173>1. Global nonnegativity, not finite grid testing.

## originality

PASS

The full problem-defining Kolountzakis–Révész source lists singleton/complement, tails, odd/even supports and duality, none evaluating H={3,4}. Published Resultary corpus shows nearby exact sparse cases and a general doubled-harmonic family, but {3,4} is not {m,2m} and no known frequency equivalence fixing 1 reduces it. Originality accepted best-of-knowledge, with plausible older 1995 dual-cosine source incompletely read.

## value

PASS

A natural concrete sparse prescribed-support extremal constant with a sharp global dual certificate and unique extremizer; determines a specific missing-support value not entailed by common full-degree or parity formulas, and usable as a benchmark in harmonic-analysis support problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
