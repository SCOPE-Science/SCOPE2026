---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The exact block factorization defines the unitary totient without a squarefree hypothesis. For one prime power A, (M−1)(A−1)=2 gives the two pairs for A=2,3. With two distinct-prime blocks A=x+1, B=y+1, the equation is kxy=x+y+2, k=M−1≥1. If x=1 then A=2 and y is positive and even, so (k−1)y=3 is impossible; the symmetric case is identical. If x,y≥2 then 2xy−x−y−2=(x−2)(2y−1)+3y−4>0, so k=1. The factorization (x−1)(y−1)=3 gives A,B=3,5 in either order. Direct substitution confirms all three ordered pairs (N,M). Independently enumerating prime powers and products of powers of different primes through 10^6 gave 367460 unique eligible N and precisely (2,3),(3,2),(15,2), in agreement with the recorded output. Replay: `python3 /tmp/opencode/frozen-independent-checks.py totient`. The classification is proved without this cutoff.

## originality

PASS

The inspected comparisons do not give the unrestricted-exponent, low-support plus-sign classification. In particular Yamada's quoted 2010 result is written N=Mφ*(N)+1, which means Mφ*(N)=N−1, not N+1. Yamada's own ± bounds are related but do not classify these cases.

## value

PASS

Fixing support at one or two is a natural first classification for an explicitly studied arithmetic equation. The theorem identifies the only composite solution in that layer and rules out all nonsquarefree composites there, without a size or exponent cutoff. The sign and the distinct-prime parity obstruction are essential; it is not a recomputation of table entries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
