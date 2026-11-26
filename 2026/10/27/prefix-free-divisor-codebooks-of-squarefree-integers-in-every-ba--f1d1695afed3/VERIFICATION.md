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

Finite zero/one base-ℓ subset sums are distinct and strictly between zero and one. A nonempty sum with last nonzero digit at j has reduced denominator ℓ^j; choosing ℓ not to divide the gcd of the exponents of b makes its b-power irrational by an integer-valuation contradiction. The finitely many mantissas therefore lie in interiors of distinct sufficiently fine base-b cylinders. A common positive radius preserves every subset product within its cylinder, including singletons, and can make the prime intervals disjoint. Scaling by b^{L|S|} gives the same leading K digits for the divisor as for its assigned mantissa, and every divisor has at least K digits; different first K digits rule out a prefix relation. The prime number theorem in fixed proportional intervals supplies ≫ b^L/L primes per interval, and unique factorization gives distinct squarefree products bounded by Cb^{rL}. Taking L=floor(log_b(X/C)/r) gives b^{rL}>X/(Cb^r) and L comparable to log X, proving the bound for every sufficiently large real X at each fixed b,r. This works for perfect power bases and r=1. The OEIS existence conclusions use ω=Ω=r, not an identification of minima. The original verifier was inspected, not executed; python3 reproductions/frozen_math_checks.py independently confirmed primality and 127 distinct binary 13-bit prefixes for the seven-prime witness by integer division and shifts. This is only a finite witness.

## originality

PASS

The inspected binary entries pose all-index existence; the proof supplies a construction in every integer base and a uniform-in-X lower bound for each fixed pair (b,r). Neither the finite OEIS tables nor literature using other prefix relations implies this construction or rate. This is a bounded assessment, not proof of historical priority.

## value

PASS

It settles two explicit binary existence conjectures, and its stable digit-cylinder argument explains how to enforce all divisor constraints at once in any base. The stated exponent is not sharp by this method: for r>1 one can fix r−1 primes in their stable mantissa windows at an initial scale and vary the last prime at a growing scale, as the first K digits of each divisor still depend only on the product of mantissas. That observation does not diminish the constructive solution of the all-index existence question or the valid lower bound actually asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
