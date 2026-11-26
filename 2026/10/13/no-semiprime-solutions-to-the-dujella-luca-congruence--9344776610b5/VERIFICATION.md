---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Modulo 1 is vacuous; at a prime p the difference is (p+1)(p−2). For p², p³≡1 modulo D=p²+p+1, so the condition is D|p−3; the strict bound |p−3|<D gives p=3, and 9 satisfies the congruence. For 2q with q odd, reduction modulo q+1 gives a difference congruent to 2 and hence an impossibility. For two distinct odd primes there is even a direct check: 4 divides both nφ(n) and σ(n), since each p−1, q−1, p+1, q+1 is even. Thus nφ(n)−2 cannot be divisible by σ(n). The frozen proof's more detailed valuations are also correct. This exhausts Ω≤2 including the unit, without relying on the attached finite checker, which was inspected but not run. Mixed powers at higher Ω are outside the claim.

## originality

PASS

Primes and the prime-square part are prior art. The supported distinct part is exclusion of every squarefree semiprime with both primes variable. The closest primary texts establish fixed-prime-support results, and the closest indexed multiplicity classifications concern a different divisor or remainder; no inspected result gives the global residue-two semiprime exclusion.

## value

PASS

The multiplicity cutoff is the first full layer containing composites and answers the uniform two-distinct-prime case for a studied congruence, rather than testing isolated primes or a numerical range. The elementary parity obstruction removes a whole natural family that fixed-support lists cannot settle. The scope does not include arbitrary products of higher prime powers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
