---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The classical Pfaffian multiplicity formula gives D_{n,s}=∏_{1≤i≤j≤s}(n-s-1+i+j)/(i+j), with extended ambient endpoints. Factorial cancellation yields the adjacent ratio D_{n,s}/D_{n,s-2}=∏_{k=-(s-1)}^{s-1}(n+k)/[(2s)! C_{s-1}]; its quotient at s+2 gives exact second ratio [(n²-s²)(n²-(s+1)²)]/[16(2s-1)(2s+1)²(2s+3)]. Independent Sympy factored Q_n(s+2)-Q_n(s) = -4(2s+3)(n²+255s²+765s+701), strictly negative for admissible positive n,s, forcing at most one sign change from log-convex to log-concave. Dividing numerator/denominator by n⁴ yields (1-theta²)²/(256theta⁴), crossing one at 1/sqrt(17). Independent exact fractional degree and curvature comparisons checked 324 cases for 4≤n≤40; symbolic proof covers all.

## originality

PASS

PASS at best-of-knowledge level: same-input primary exact degree formula credited, but no printed Pfaffian adjacent-curvature/one-transition result was found, and the closely related published symmetric and generic results do not cover skew-symmetric rank loci. Algebraic simplification may have been independently noticed in unindexed older work.

## value

PASS

Pfaffian skew-symmetric rank loci form a natural canonical nested family of projective varieties; their enumerative degrees admit a coherent exact curvature phase portrait. One-transition behavior and sharp asymptotic threshold reveal cross-rank geometric structure, not a one-number substitution or recomputation of known multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
