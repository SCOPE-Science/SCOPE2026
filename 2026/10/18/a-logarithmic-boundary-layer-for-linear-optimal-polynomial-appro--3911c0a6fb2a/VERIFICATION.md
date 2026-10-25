---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For complex degree≤1 q and real p>1, map q to residual r=1−(1−z)q with r(1)=1. Strict convexity/coercivity and conjugation/reversal invariance force unique r=a+(1−2a)z+az², a real. Boundary absolute value |1−2a(1−cos θ)| reduces to strictly convex F_p(a) under arcsine measure. Derivative signs at a=1/4 and 1/2 give unique a_p in (1/4,1/2). Splitting derivative-balance integrals near s=0 and s=2, endpoint Laplace gives P~(2√(2π))^{-1}(bp)^{-3/2}, N~√(2/π)L^{p−1/2}/√(bp), b=2a, L=2b−1, hence L^{p−1/2}~1/(4bp), 4p(1/2−a_p)=log(4p)+o(1). Root w=1−1/a_p=−1−log(4p)/p+o(1/p); optimal p-th residual moment dominated by s=0 and ~1/√(2πp). Independently integrated 8192 arcsine nodes, solved 6 finite p roots through p=600, recovered published p=2,4 coefficients and p-th-moment asymptotic ratio→1. The o(1/p) constants derive analytically, not from finite quadrature.

## originality

PASS

Extends same-object finite-even-exponent examples of Centner to exact uniform all-real-p sharp asymptotics and an additional optimal residual moment constant. A simultaneously assigned narrower high-exponent record has exactly the same root-asymptotic but is implied by this stronger theorem; only THIS record contains the extra sharp p-th residual moment. Do not count the narrower record as independent supporting novelty.

## value

PASS

A named open boundary-zero convergence phenomenon for the canonical Hardy optimal inverse is resolved quantitatively with logarithmic layer and exact constant; comparing the optimal residual to its limiting polynomial exposes noncommuting limits and a factor-two moment gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
