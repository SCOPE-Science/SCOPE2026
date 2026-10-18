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

The target masses are (1-p)(1-q),p+q-2pq,pq. Direct mass subtraction yields errors pq for Bin(1,p+q-pq) and (sqrt(p)-sqrt(q))^2 for Bin(2,sqrt(pq)). If pq>=1/4, ordering p>=q implies q>=1/4 and the second error <=1/4, with equality only p=1,q=1/4. At that pair, for every m>=2 the largest possible Bin(m,r) probability at 1 is (1-1/m)^(m-1)<=1/2 whereas target P(1)=3/4; for m=1 mass at 2 is 0 vs 1/4. This proves the unrestricted lower bound and unique extremizers, not pointwise best m for all pairs.

## originality

PASS

Roos (2000/01), Ehm (1991), Choi and Xia (2002) study same-trial-count or constrained binomial approximation. Jaramillo and Melbourne (2022) provide same-size relative-log-concavity TV bounds and explicitly discuss optimizing binomial size, but do not provide the sharp unrestricted two-coin covering radius, based on inspected source.

## value

PASS

The exact minimax approximation radius for a natural two-summand Poisson-binomial family, unique extremizers and two explicit universal approximants settle a basic sharply defined approximation question beyond same-size comparison, albeit with narrow n=2 scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
