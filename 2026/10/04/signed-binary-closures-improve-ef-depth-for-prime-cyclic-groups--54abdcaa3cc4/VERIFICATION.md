---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The signed-binary construction is correct. The selected doubling chain and partial-sum relations force every response to be the corresponding integer multiple of the first response, and either closing relation forces p times that response to be zero. In a distinct prime-order target this forces the first response to the identity, contradicting preservation of its source inequality. The popcount identity s2(a)+s2(2^n-a)=n-v2(a)+1 yields h(p)<=ceil(n/2). Gomaa's Theorem 3.3 independently supplies the n+1 lower bound for every prime p<q with 2^n<p<2^{n+1}. The package verifier was inspected and an independent finite replay confirmed the combinatorial inequality; the all-prime conclusion rests on the symbolic proof.

## originality

PASS

The corrected final text narrows originality to the actual new part. Gomaa's dissertation gives the n+1 lower bound, the 2n upper bound, and explicitly asks whether the gap can be improved. It also already proves the Mersenne exact case in Theorem 3.5, and Theorem 3.6 covers the Fermat form p=2^n+1 as 2^n+2-1. Those endpoint exact cases are therefore treated as prior coverage, not novelty. No inspected primary, Resultary, or web source states the general n+h(p) signed-binary bound or its uniform n+ceil(n/2) consequence.

## value

PASS

The surviving contribution directly improves the upper side of a named open quantitative gap for prime cyclic groups from 2n to at most n+ceil(n/2), using a reusable signed-binary closure choice. This is a substantive structural improvement even though the endpoint exact cases themselves were already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
