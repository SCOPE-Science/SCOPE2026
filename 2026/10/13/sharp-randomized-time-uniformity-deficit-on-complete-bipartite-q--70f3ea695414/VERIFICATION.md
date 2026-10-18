---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

From A^3=ab A the continuous-time unitary has only the A and A^2 spectral terms, yielding exactly five probability blocks depending on u=E cos(sqrt(ab)T) and v=E cos^2(sqrt(ab)T). The feasible moment region is -1<=u<=1, u^2<=v<=1, realizable by nonnegative observation times. The exact positive Hessian for n>=3 reduces the a,b>=2 case to v=u^2, and monotonicity of the cubic n^2 x^3+Kx+C yields the unique minimizing cosine or boundary x=-1. For star K_{1,m}, the global supporting-plane inequality and Hessian certify x=-(m-1)/(m+1). K_{1,2} uniquely needs u=0,v=1/3 and genuine time mixing; K_{1,1} is deterministic. The balanced H=r^2(r^2-6r+4) changes sign at integer r=6 and gives the stated cross-part-zero optimum. The independent exact matrix/gradient program was inspected but not independently executed; no finite test is substituted for these analytical inequalities.

## originality

PASS

The literature defines arbitrary randomized observation-time average mixing and recognizes exact uniformity exceptions, but does not establish the unrestricted Frobenius-optimal approximation across all complete bipartite graphs, its unique moment minimizers or the r=6 nontransport phase. New here is the quantitative global optimization, not the known K_{1,2} mixing existence or general A^3 relation.

## value

PASS

Optimizing a physically natural global uniform-mixing fidelity over arbitrary time distributions gives a sharp exact benchmark and proves randomization helps only at the exceptional three-vertex path; the balanced transition to zero cross-part transport is a structural, non-obvious consequence of the chosen loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
