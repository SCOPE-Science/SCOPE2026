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

Independently reconstructed the bijection. For two nonzero digits (a,c), ac divides ab+c only if a divides c. Writing c=ak gives the equivalent condition ak | b+k, which forces k | b and then a | (b/k+1). Conversely these conditions imply divisibility. With d=b/k, c<b is equivalent to a<d, and for d>=2 the proper divisors of d+1 are all at most (d+1)/2<d. Recovery of k=c/a and d=b/k makes the correspondence injective. The bound is equality exactly when every nontrivial d|b has d+1 prime. An odd divisor d>=3 rules that out, as does 8|b; among b>=3 only b=4 remains and works. At b=2 the formula gives the sole pair (1,1); at a prime base the only summand is d=b. The all-base proof supplies correctness; the supplied finite checker was inspected, not executed.

## originality

PASS

The closest inspected primary work gives the digit-product condition, exact-length enumeration algorithms, and small-base counts, but not the explicit divisor-lattice classification. The classification follows by a short reduction from the definition itself, not by specializing an identified theorem that already classifies the layer or gives the divisor formula. Pass is restricted to the explicit all-base bijection/formula and its consequences, not the predicate, general enumeration or tabulated values.

## value

PASS

The full first nontrivial digit-length stratum of an existing enumeration problem is natural, with no arbitrary cutoff. The explicit correspondence both generates every valid digit pair from divisors of the base and explains variation of the counts with shifted divisors, including exactly when the universal lower bound is tight. The usefulness is in the complete structural classification, not in the difficulty of the cancellation or recomputation of known table entries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
