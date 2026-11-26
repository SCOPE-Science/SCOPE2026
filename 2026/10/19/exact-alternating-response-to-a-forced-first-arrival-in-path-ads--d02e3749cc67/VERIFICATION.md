---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditioning on the first uniform permutation element leaves the two segments with the same path law, yielding 1+J_(i-2)+J_(n-i-1) with J_(-1)=J_0=0. Averaging gives the frozen recurrence; differentiating the stated generating function verifies it and the zero constant term. With q=e^(-2), subtracting the affine part J_m=(1-q)m/2+(1-3q)/2+e_m cancels it from the response, leaving e_(a-1)+e_(b-1)-e_(a+b+1), a<=b, and e_(-1)=q. Taylor remainders and integration by parts give e_m=(-1)^(m+1) u_m with the stated positive integral. The integral gives u_m<2^(m+1)/(m+2)! and u_(m+1)/u_m<2/(m+1); e^2>7 also gives u_0>u_1. If a,b have the same parity the signs and dominance give sign (-1)^a; for a even and b odd decreasing u gives positivity. For a odd >=3 and b even the two potentially counteracting terms have ratio to u_(a-1) strictly below 2/a+4/[a(a+1)]<=1. For a=1 and b even, u_0=u_1+u_4 gives equality at b=2 and strict negativity thereafter. In the endpoint case a=0, b=0 gives 2q-u_1=0, b=1,3 give equality by q=u_0-u_2=u_2-u_4, even b>=2 give positivity by monotonicity, and odd b>=5 by u_4=(1-7q)/2<q since e^2<9. Together these give exactly the three exceptional sizes. For a>=1, the furthest residual term is strictly smaller in magnitude than u_(a-1), so the triangle inequality gives the stated strict bound below 3u_(a-1) and hence below 3*2^a/(a+1)!.

## originality

PASS

The exact unconditioned path expectation and the formulas that compute each conditional mean are prior; the supported distinct claim is the sign and exception classification and its uniform strict factorial bound. The inspected perturbation results are on other models, graphs or observables. None was shown to mechanically imply the finite-path sign comparisons, including their small cancellations.

## value

PASS

The expected-size sensitivity to selecting one definite vertex first is natural for the random greedy process, with the path isolating boundary effects. The result resolves the full all-size sign profile rather than just computing examples, identifies the small paths with no sensitivity, and quantifies how rapidly interior priority effects vanish. The known mean formula alone does not exhibit any of those qualitative outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
