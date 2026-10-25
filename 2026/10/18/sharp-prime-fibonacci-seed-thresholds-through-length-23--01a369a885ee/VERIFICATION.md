---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The recurrence starts at ordered distinct odd primes (p,q), stops when their sum is a power of two, otherwise appends its least odd prime factor. Each newly appended odd prime r divides p+q with r<= (p+q)/2 < max(p,q), so max of the ordered pair decreases after at most two transitions and trajectories terminate. Independently enumerated all 656 odd primes <=4919 and all 656*655=429680 distinct ordered seeds, using a separate prime sieve, smallest-odd-prime-factor transition and memoized depth, and reproduced 22 optimal ceiling entries M(l) for 2<=l<=23, unique depth-23 pair (4007,4919), and upper bound 22 for every preceding ceiling. This IS exhaustive for the finite seed ceiling, since any seed ceiling lower than a witnessed minimum lies within the enumerated set. It does not claim any value M(l) for l>=24 or all-prime asymptotics.

## originality

PASS

No exact prior implication was located after source-specific comparison of definitions and named parameters; best-of-knowledge, with explicit residual risks. The searches and source inspections below are not a novelty certificate.

## value

PASS

The first exact 22 values of the natural minimal-seed ceiling needed to achieve trajectory depth l quantify prime-Fibonacci length-resource growth beyond the foundational existence/termination theorem; uniqueness of a length-23 extremal seed is a useful precise finite cutoff on a motivated recurrence, rather than arbitrary small sample statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
