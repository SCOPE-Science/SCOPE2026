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

Read frozen RESULT.md and METADATA.json, independently reconstructed the divisor identity a(2^k m)=((2^(k+1)-3)σ(m)-λ(m))/4 for k>=1, m odd and the bound 0<=λ(m)<=τ(m). For k>=2, m=1 attains 2^(k-1)-1; among m>1, m=3 attains 2^(k+1)-3, and m>3 gives strict inequality because σ(m)-τ(m)>=m-1>=4 and C_k>1. For odd m, prime, higher-prime-power and two-prime-factor cases rigorously exclude all further a(m)<5; doubling a(2m)=a(m), and dyadic bounds limit k>=2 to 4,8. Independently computed signed q-series and divisor sums for n<=100 and checked fibers; no finite test used to infer the global theorem.

## originality

PASS

The structural dyadic identity and positivity/zero set are already in Merca (2026); only the sharp layer minima, equality cases and complete pre-five fibers are assessed. The newer Merca dyadic source is abstract-accessible, with full text uninspected because open arXiv attempts failed and authorized institutional access returned VPN disconnected; this is residual risk, not proof of novelty. No equivalent family theorem was identified in accessible primary results or the semantic records.

## value

PASS

The exact sharp minima on each dyadic layer and the entire sub-five fiber classification are natural arithmetic information about an introduced signed partition statistic. The cutoff is motivated rather than arbitrary: 5 is the first non-pure-power-of-two value possible on layer k=2. The classification does not pretend to solve higher fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
