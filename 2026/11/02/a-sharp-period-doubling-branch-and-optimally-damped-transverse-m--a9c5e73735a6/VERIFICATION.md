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

The frozen Finding's open interval is exact for hyperbolic attraction but false for local asymptotic attraction. It conflicts with its own limitation excluding nonlinear endpoint stability. In the repair the interval is 1/2<h<=pi/4, with a nonhyperbolic upper endpoint. On the alternating invariant line g(x)=x-4h sin(x); H(a)=a/(2 sin a) strictly increases from 1/2 to infinity, and a in (0,pi) gives two distinct phase configurations. Both quotient Jacobians are I-h cos(a)L; the spectrum and repulsion above pi/4 follow. At h=pi/4 in edge displacements the two steps are u+Q(u) and u-Q(u) with quadratic part Q2=(h/2)L(s*u^2), componentwise. Both returns have cubic increment -DQ2(u)Q2(u). For W=u^T L_E^(-1)u/2, the leading difference is -(h^2/2)(s*u^2)^T L(s*u^2). The only constant vector of the form s*u^2 is zero, because the signs alternate. Hence the quartic decrease is uniformly definite on the mean-zero unit sphere; a small sublevel is invariant and summability of ||u||^4 gives u->0. This is a full-quotient stability proof, not an inference from an invariant line. Convexity of |1-t lambda| in lambda puts the worst spectral factor at lambda_min and 4; balancing them gives the unique t*=1/[2(1+b_n)]. The neutral endpoint cannot minimize. For local uniqueness at the flip, the w derivative of F^2-I on the complement of the alternating eigenspace is invertible and invariance makes w=0 its unique solution. On the line the divided second return has leading terms 8(h-1/2)-(2/3)x^2, giving a unique positive squared-amplitude branch and the stated onset scaling. Expanding a cot(a) and H(a) gives the large-n constants. The supporting finite checker was inspected only; it does not test the neutral endpoint.

## originality

PASS

The genuinely distinct repaired claim is nonlinear asymptotic attraction at the upper endpoint in the full common-phase quotient. The local flip overlays earlier weighted bipartite results; the scalar branch has indexed overlap; the spectrum and optimizer are covered by a later general theorem with the same cycle specialization. Those parts provide context and a self-contained classification, not separate novelty credit. The closest endpoint treatment proves a cubic scalar return and explicitly does not infer transverse attraction. The quartic decrease proved here supplies the missing implication when every multiplier is 1.

## value

PASS

At the physically and mathematically distinguished upper bifurcation parameter, the derivative is the identity on the entire phase quotient and Floquet stability is inconclusive. Showing full nonlinear attraction decides the actual parameter interval and explains why it is closed at that end even though spectral contraction is lost. A scalar attraction result cannot answer the transverse question. The ring minimax formulas retain their role as a quantitative comparison in the interior but are not the basis of the repaired claim's value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
