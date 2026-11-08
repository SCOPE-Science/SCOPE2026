---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For kappa(n)=1+sum_{d|n,d<n} kappa(d), kappa depends only on prime exponent tuple. Replacing distinct odd primes with (3,5,7) weakly lowers n while preserving kappa, so any smaller odd three-support ample n yields a smaller canonical ample triple. The rational exponent generating function 1/[2(1-x)(1-y)(1-z)-1] gives an exact seven-neighbor recurrence. A separately implemented multidimensional prefix recurrence independently exhausts ALL 4650 positive canonical triples with 3^a5^b7^c<=801204488268064453125: all 4649 strictly smaller have kappa<=n and the sole boundary triple (20,9,6) yields kappa=841632661765951062016>n. Odd numbers with <=2 prime supports have sigma(n)/n<=15/8<2, are deficient, and by proper-divisor induction cannot be ample. Uniqueness at minimum follows strict increase of the product under larger primes.

## originality

PASS

Fink introduced recursive-divisor ample numbers and recorded the least odd ample integer without support constraint, on five prime supports; that does not determine the minimum at exactly three supports. The published finite-prime-support theorem proves existential infinitely many ample numbers if Euler product>2 but expressly has no effective least-witness bound. The explicit threshold and uniqueness are strictly finer than existence.

## value

PASS

Exact first witness at the minimal possible odd prime-support cardinality is a natural extremal invariant of the recursive divisor function. The exhaustive, reproducible finite cutoff is not an arbitrary slice: canonical-prime reduction proves it covers every possible smaller candidate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
