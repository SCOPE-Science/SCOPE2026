---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For p<q, phi(pq)=(p-1)(q-1), so gcd(pq,phi(pq))>1 is equivalent exactly to p|(q-1). For fixed p, PNT in reduced residue class 1 mod p gives pi(x/p;p,1)~x/[p(p-1)log x]. With z fixed, the range z<p<=x^(1/3) is O(x/log x * sum_(p>z)1/[p(p-1)]) by Brun--Titchmarsh and log(x/p^2)>=log(x)/3. For x^(1/3)<p<sqrt x, writing q=kp+1, k<=x/p^2 gives O(x^(2/3)). Let z increase to infinity to obtain E(x)~A x/log x. Divide by Landau squarefree-semiprime count ~x loglog x/log x. The exact local condition and finite computations do not alone prove the asymptotic.

## originality

PASS

The local group-order criterion is explicitly classical; only the semiprime-conditioned first-order count and its convergent constant are assessed. Pollack proves a global asymptotic series at the different x/logloglog x scale, while Kanungo treats classification of groups of given pq order without a semiprime counting asymptotic. No searched source proved the specialized distribution law, but a short earlier note or exercise is a concrete priority risk.

## value

PASS

An explicit sharp first-order law for noncyclic group orders within squarefree semiprimes contrasts with their near-universality in this stratum and with scarcity of cyclic group orders globally. The convergent prime constant supplies a quantitative baseline for higher fixed-prime-factor strata, where obstructions interact; more than a restatement of the elementary pq criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
