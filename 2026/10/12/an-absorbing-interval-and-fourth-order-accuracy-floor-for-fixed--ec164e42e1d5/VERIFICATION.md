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

Pinned scalar CARS Algorithm 1: d_r(x)=(f(x+r)-f(x-r))/(2r), positive centered curvature h_r, proposal y=x-d_r/(Lhat h_r), and safeguard argmin of x,y,x±r. Global strong convexity gives d_r increasing with derivative at least mu and unique zero. C^3 Taylor gives z_r-x*= -f_three(x*) r²/(6 f_two(x*))+o(r²); objective defect f_three(x*)² r^4/(72f_two(x*))+o(r^4). Between minimizer and displaced zero fprime and d_r have opposite signs; proposal moves outward and hence worsens f; probes ±r worsen by positive 1/2 f_two(x*)r²+o(r²), uniformly for |x-x*|=O(r²). At minimizer candidate also worsens, at displaced root candidate is incumbent; thus whole closed interval is fixed under every Rademacher sign and every Lhat>0. For f=x²/2+(sin x-x)/2, f_two=1-sin x/2>=1/2, d_r=x-1/2+(sin r)/(2r)cos x, root 0<z<=r²/6<=r/6 for 0<r<=1; f(x±r)>=25r²/144>r²/48>=f(x) throughout [0,z]. Independent exact SymPy expansion solved z=r²/12-7r^4/2880+O(r^6), f(z)=r^4/288-13r^6/51840+O(r^8). No step requires finite experiments for infinite quantifiers.

## originality

PASS

Best-of-knowledge surviving original contribution; compare mathematical implication rather than titles/parameters. Source CARS Algorithm 1 and Theorem 2.6 give sufficient target-dependent r=O(epsilon^1/4) under Lipschitz Hessian, not an example attaining r^4 or an absorbing continuum. Prior STP safeguard without curvature-aware candidate cannot imply the four-choice obstruction. The 2023 thesis abstract mentions inspection strategies, but its full body was not available for a decisive comparison.

## value

PASS

A sharp fixed-radius failure mode of a published derivative-free method is motivated by its asserted target accuracy guarantee: an entire continuum of nonoptimal starts cannot improve, and attained fourth-order objective gap proves the sufficiency exponent cannot be uniformly weakened on the class. The universal local mechanism and all-radius analytic witness add substantive algorithmic information beyond generic truncation error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
