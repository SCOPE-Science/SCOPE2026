---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

H(s,t)=ζ^{h(st)} with h(u)=au+bu². Subtraction of zero row/column reduces determinant to (ζ^{h(st)}−1) on Fp×. Multiplicative-character Fourier basis maps χ(t) to χ^{-1}(s) with factor Lχ; inversion contributes (−1)^((p−3)/2). For a≠0 the phase has a nonzero singleton nonzero fiber: linear bijection if b=0, or quadratic critical value h(−a/(2b))=−a²/(4b) if b≠0. For nontrivial χ, cyclotomic disjointness Q(ζ_p)∩Q(ζ_{p−1})=Q implies vanishing would give all phase-fiber weighted counts equal; zero character sum then makes all zero, contradicting singleton χ(u0). Trivial-character factor has negative real part. For a=0,b≠0, rows/columns indexed by square values reduce to a (p+1)/2 square prime-Fourier minor, nonzero by Chebotarev. a=b=0 all ones. Independent numerical SVD checked all 373 coefficient pairs for primes 3,5,7,11,13.

## originality

PASS

The proof credits the known prime Fourier minor theorem and general finite-field extension framework. The exact nonlinear full-rank branch for these parabola-correlated p×p frequencies and the trichotomy are not explicit consequences of the inspected prior results.

## value

PASS

Determines exact invertibility of a natural square self-sampling finite-field parabola operator for all parameters and odd primes, including exceptional rank strata; singleton fiber yields reusable nonvanishing criterion. Not merely a numerical rank table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
