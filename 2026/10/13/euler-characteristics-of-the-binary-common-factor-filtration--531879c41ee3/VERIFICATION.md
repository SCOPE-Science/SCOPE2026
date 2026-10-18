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

For projective pairs ([f],[g]) of nonzero binary forms with 1<=m<=n, torus scaling x yields unique monomial fixed points indexed by 0<=i<=m,0<=j<=n. The gcd degree is min(i,j)+min(m-i,n-j); inequality >=k is equivalent to k-m<=j-i<=n-k. Two triangular corners with k(k+1)/2 lattice points each are removed, yielding (m+1)(n+1)-k(k+1). Euler fixed-point localization on the closed projective locus and additivity on exact-degree locally closed strata give χ_c(G0)=2, χ_c(Gk)=2(k+1) for 1<=k<m, χ_c(Gm)=(m+1)(n-m+1). Boundaries k=0,m and m=n explicitly agree. An independent pair enumeration checked 68 (m,n) combinations 1<=m<=8,m<=n<=12, every threshold; proof is the unrestricted lattice-strip identity.

## originality

PASS

The classical resultant vanishes when homogeneous binary forms share a projective root; Sylvester/subresultant theory characterizes the deeper common-factor closed strata. The inspected D’Andrea–Dickenstein paper develops resultant complexes, minors and formulas, not projective-space Euler characteristics for the complete gcd filtration. No stronger primary Euler formula for the exact same two-form filtration appeared in targeted Resultary and web comparisons. Algebraic equations and a degree condition alone do not determine topological Euler profiles. Relevant independently inspected published SCOPE comparison: The source conditions prescribed repeated roots within ONE binary form; the current problem studies gcd degree of a PAIR of binary forms. The subset-sum function of multiplicity partition does not supply the strip enumeration of pairs.

## value

PASS

The resultant and higher subresultant varieties form a natural singular stratification in elimination theory. The closed quadratic Euler law, exact linear staircase and degree-independent χ_c=2 coprime stratum determine a natural complete topological invariant for all bidegrees, not isolated instances or mere restatement of resultant vanishing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
