---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Since p congruent 7 mod36, exponent a=4 always gives 9|p-16, and for a in {0,1,2,3,5}, 4 or 9 cannot divide the remainder. Any nonsquarefree positive remainder has a prime-square divisor q^2 with q>=5 and q<=floor(sqrt(10^9)); gcd(36,q^2)=1 yields a unique progression index k mod q^2 by inverse 36. The checker marks only positive remainders >=q^2 and scans every k=0,...,27,777,777 (27,777,778 integers), all prime q<=31623. Independent newly executed full exact mask sieve reproduced precisely nine integer five-obstruction candidates and precisely two prime survivors; complete deterministic trial division and factorization confirmed exponent 6 for both. Their lower exponent obstructions are explicit and the all-k range is exhaustive within <=10^9; this does not depend on a heuristic cutoff or primality assumptions.

## originality

PASS

Best-of-knowledge original for the precise quantified final claim after comparing same-object and broader primary literature; the prior components/techniques are explicitly credited and residual historical-priority risk is retained.

## value

PASS

The prior same-congruence investigation established the classification below 10^8 and explicitly proposed locating the next first-exponent threshold. The first least-exponent-six prime is a concrete natural invariant of the prime-restricted squarefree-plus-power-of-two problem; the complete nine-candidate and two-prime range certificate is an independently usable sharp finite answer, not an arbitrary unmotivated window. No general conjecture is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
