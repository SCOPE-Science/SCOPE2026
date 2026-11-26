---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On a line avoiding zero, the norm is a nonzero scalar times an irreducible quadratic. Completing the square reduces its character sum to the sum for x^2-d with d nonzero: the equation y^2=x^2-d has exactly p−1 solutions by factoring (x−y)(x+y)=d. Thus even allowing the norm scalar to reverse signs, at most (p+1)/2<p−1 points have nonsquare norm, a necessary condition for primitivity. A long progression must therefore be on a line through zero; the missing index is −1, so a=b. If b has generator exponent k coprime to p²−1, the scalar coset has exponents k+(p+1)t with t covering p−1 residues. An odd prime divisor of p−1 divides some such exponent, whereas if p−1 is a power of two, all prime divisors of p²−1 divide p+1 and no exponent is disqualified. This proves the count and all-pair rigidity. The same line obstruction or the zero term rules out a full p-term progression. A nonnormal nonzero element satisfies z^p=±z and has order at most 2(p−1), so primitivity implies normality here. The finite enumerations reported in the frozen files are corroboration only; no uploaded code was executed or needed for the universal proof. No exact maximum is asserted for non-Fermat primes.

## originality

PASS

The inspected statements do not cover the Fermat-prime condition for the growing length p−1 together with the classification and count of all ordered pairs in quadratic prime fields. Standard ingredients and fixed-length progression existence are not claimed new.

## value

PASS

At the natural nonrepeating length bound, the theorem identifies an exact arithmetic obstruction and every extremal pair, rather than just producing examples or estimating a count. The link between the Fermat-prime condition and rigidity is useful independently of the unknown shorter maxima.

The dated certificate retains the supplied scientific assessment, sources and limitations.
