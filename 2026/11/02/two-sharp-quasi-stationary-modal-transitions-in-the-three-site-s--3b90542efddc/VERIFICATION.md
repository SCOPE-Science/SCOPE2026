---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the homogeneous continuous-time absorbing SIS chain on path P3 with per-vertex recovery 1 and per-edge infection lambda>0, all seven transient states communicate, giving unique positive left-Perron quasi-stationary vector. Endpoint symmetry reduces to five probabilities a,b,c,d,e satisfying 5x5 balance matrix M. Its determinant, adjugate cofactors and two resultants establish a>b>c before lambda=3/4, c>b>a afterward; at 3/4 five labelled configurations tie at 1/6 while d=1/24,e=1/8, and extinction rate is 1/2. A third eliminant F(lambda)=18lambda^5-140lambda^4+77lambda^3+92lambda^2-50lambda+4, Sturm variation counts and Perron range bounds show the only admissible pair/full crossing lambda*=1.0092470826...; d<c globally. Independently evaluated full seven-state QSD at rates on both sides and inspected source exact SymPy verification.py. The theorem concerns asymptotic conditional modes, not finite-time epidemic modes.

## originality

PASS

Comparing mathematical statements rather than titles, full primary text and domain distinctions indicate the exact final all-parameter claim is not covered by the inspected prior theorems. Earlier frameworks explicitly acknowledged; historical priority is best-of-knowledge, not independently certified. Gives general finite-network QSD algorithm, but not analytic modal ordering and five-state tie for homogeneous 3-node path Approximation of aggregate survival/prevalence on graphs, not exact 3-site labelled-configuration mode transitions

## value

PASS

The three-site path is the smallest noncomplete connected network with unequal infection-position roles; exact quasi-stationary labelled-state modes and a five-way tie are a meaningful finite-state benchmark against general approximate epidemic methods, despite no claim of large-network phase transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
