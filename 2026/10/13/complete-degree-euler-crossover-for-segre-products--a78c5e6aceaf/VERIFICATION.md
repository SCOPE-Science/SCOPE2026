---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

At the pinned RESULT.md, the Segre hyperplane class H=sum h_i has intersection number N!/prod(a_i!), while the CW-cell decomposition of each complex projective factor gives chi=prod(a_i+1). Dividing yields the exact coordinate-ratio (N+1)/(a_j+2). For r>=3 every increment strictly raises the quotient; for r=2, (1,b) stays at 1/2, (2,b) gives (b+2)/6, and every pair with both entries >=3 is >=R(3,3)=5/4. With r=3 the base (1,1,1) gives 3/4 and (1,1,2) gives 1; for r>=4 r!/2^r >1. Therefore equality is only (2,4) or (1,1,2), and the stated strict cases exhaust all positive-dimensional factors. Independent exact integer enumeration of sorted tuples r<=5, dimensions 1..6 returned these same equality tuples.

## originality

PASS

The two classical closed invariant formulas are prior knowledge. The assessed final claim is the complete sign/equality partition, not either formula. A targeted Resultary query and primary Segre-geometry comparisons identified secants, dual degrees, hyperdeterminants and identifiability rather than a theorem implying the complete primal degree-versus-topological-Euler phase diagram. This is a best-of-knowledge judgment rather than proof of absolute priority.

## value

PASS

Degree and topological Euler characteristic are independent canonical invariants of the natural Segre product family; identifying precisely when either dominates and classifying two isolated equalities makes the multidimensional parameter comparison complete. The coordinate-growth lemma explains the rigidity, beyond simply listing factorial evaluations. The result is elementary and not a general theorem for arbitrary polarizations, but a natural full invariant comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
