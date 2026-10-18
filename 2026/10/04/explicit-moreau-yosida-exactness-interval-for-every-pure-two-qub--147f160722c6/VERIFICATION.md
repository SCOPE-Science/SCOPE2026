---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For Schmidt form psi=a|00>+b|11> with concurrence c=2ab, rho^{T_B} has spectrum (a^2,b^2,ab,-ab) for a,b>0; its sign is swap F. The trace-norm subgradient gives N(sigma)>=Tr[(|Phi+><Phi+|-I/2)sigma] with equality N(rho)=c/2. Since pure-state negativity is C/2, negativity convexity and concurrence's convex roof yield 2N(sigma)<=C(sigma). Wootters f(C) is increasing and convex; differentiating yields f'(c)=(c/(2r))log((1+r)/(1-r)), f''(c)=[log((1+r)/(1-r))-2r]/(2r^3)>0 with f'(1)=1. Hence Lambda=2f'(c)W+[f(c)-cf'(c)]I supports E_F globally at rho and has diameter 2f'(c). Trace-norm duality |Tr Lambda(rho-sigma)|<=(diam Lambda/2)||rho-sigma||_1 proves the sufficient exactness condition 2f'(c)<=1/lambda for the cited norm-penalty convention. The c=1 derivative limit and c=0 separable lower bound are handled separately. The threshold is sufficient, not proved optimal.

## originality

PASS

Prior qualitative existence of global supports for pure entangled two-qubit states is acknowledged. The retained assertion is an explicit negativity-based supporting operator with computed spectral diameter and a concurrence-dependent sufficient lambda interval. No explicit version of the same interval was identified in current accessible abstracts and targeted searches, with material full-text access gaps documented as real residual risks.

## value

PASS

Converts a natural qualitative supporting-functional existence question into a usable, exact state-dependent sufficient parameter window for every pure two-qubit state, including the Bell and separable endpoints. The explicit operator norm diameter makes the certificate independently applicable, not a purely renamed existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
