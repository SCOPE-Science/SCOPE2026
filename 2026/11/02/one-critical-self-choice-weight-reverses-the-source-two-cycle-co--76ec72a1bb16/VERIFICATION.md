---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Each independent image has mass 1/(n-1+w) off diagonal and w/(n-1+w) on itself. For a marked vertex, q=(n-1)/a*((a-1)/a)^(n-1), a=n-1+w. A fixed r-cycle has probability a^-r; a vertex on it cannot have indegree zero, while an outside vertex gains avoidance conditional factor (a/(a-1))^r. Consequently Cov(Z,C_r)=(n)_r/(r a^r)*q*((n-r)(a/(a-1))^r-n). All prefactors are positive. The bracket decreases with cycle length and w; at w=0 its r=3 value is -(2n-3)/(n-2)^3<0. For r=2, the bracket numerator is -(2w²+2(n-2)w-(n-2)), so exactly one positive zero. Fixed-r Taylor expansion gives n Cov→e^-1((3-r)/2-w); w=1/2+t/n yields n²Cov(Z,C2)→-(t+1/4)/e. Independently enumerated all n^n maps for n=3,4,5 and five rational weights, confirming 45 exact covariance identities. Finite tests corroborate but do not prove the parameter-uniform claim.

## originality

PASS

PASS on distinct full-parameter theorem, not on w=0 or w=1 endpoint statistics; exact mixed covariance and parameter sign boundary are not supplied by inspected endpoint random-mapping results. Algebraically elementary overlap permits historical rediscovery, retained as residual risk.

## value

PASS

The loopless and ordinary mapping models have opposite source/two-cycle correlation signs. A natural diagonal self-choice interpolation gives an exact unique threshold and microscopic scaling window while all longer cycles remain negative. This is a structural phase diagram of natural statistics, not a change of notation or finite example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
