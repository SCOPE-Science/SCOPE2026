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

Conditioning on K=k touched cards, the final deck is a uniformly random k-element prefix followed by the increasing untouched suffix. Lehmer digits yield mu_D=(k-1)/2+(n-k)/(n-k+1), mu_I=k(2n-k-1)/4, and conditional covariance C=(k-1)/4+(n-k)/(2(n-k+1)). Chebyshev covariance of nondecreasing mu_D/mu_I plus C>0 proves all-n,r strict positivity. For r=floor(cn), c>0, occupancy variance K/n tends to t=b-(1+c)b^2 (b=e^-c), while conditional CLTs for random-permutation descents, inverse-rank projection and finite-population sample sum give independent Gaussian noise with variances a/12 and (1-b^3)/36. Delta-method K effects add (H/2,bH/2), giving matrix [(a/12+t/4,bt/4),(bt/4,(1-b^3)/36+b^2*t/4)]. A fourth-moment bound justifies covariance convergence separately. Independent rational enumeration verifies conditional formulas at n<=5, not the infinite CLT.

## originality

PASS

PASS qualified: Clay proves the occupancy/prefix law and marginal asymptotic CLTs, but marginal limits do not determine the joint limiting cross covariance. Dörr–Heiny treat uniform permutations, which lack the finite-c occupancy shared randomness. Earlier multivariate shuffle-statistic limits remain priority risk.

## value

PASS

Exact strictly positive finite-time covariance and an explicit nonzero bivariate Gaussian limiting correlation explain how mixing-time occupancy fluctuations couple two classical shuffle statistics even though their uniform-permutation limits decouple.

The dated certificate retains the supplied scientific assessment, sources and limitations.
