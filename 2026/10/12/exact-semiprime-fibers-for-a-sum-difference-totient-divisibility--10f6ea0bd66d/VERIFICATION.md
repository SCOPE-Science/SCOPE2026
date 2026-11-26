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

For Ω(n)=2 the only possibilities are p² and p<q. For the square, multiplying 2p²+1 by two reduces it to 3 modulo 2p+1≥5. For a distinct pair the quotient is (pq+1)/(p+q), and the remainder test gives p+q | p²−1; p=2 cannot satisfy it. Divisors d>2p generate exactly the prime companions q=d−p. The quotient on a solution is strictly between 1 and p since (p−1)(q−1)>0 and p²>1. Multiplying out gives (p−k)(q−k)=k²−1, and expanding the positive factor-pair construction proves its converse; p<q and the quotient force uniqueness. An independent bounded Python check (/tmp/opencode/frozen_audit_small.py) computed σ by divisor accumulation and φ from the divisor recurrence, and compared both generators against the literal divisibility for all 23,378 semiprimes up to 100,000. There were 158 hits, with the stated first ten. The frozen verify.py was inspected, not executed. It checks the fiber identity on hits, not as a separately generated predicate on every pair as the verification prose suggests. Neither finite check establishes the unbounded claim; the algebra does.

## originality

PASS

The exact underlying sequence and the tabulated terms are public. The supported distinct content is the complete multiplicity-two criterion and the two finite parametrizations, not the initial integer list or either component function. No inspected source supplies that structural classification; this is a bounded assessment.

## value

PASS

This is the first composite multiplicity layer of an established arithmetic sequence. The new information is not that a finite list can be tested: at fixed p or fixed k one can generate all eligible candidates from a finite divisor set without a search over unbounded prime companions or all composites. The proof is elementary, but the two complete search directions and exact image and uniqueness statements determine a natural layer rather than an arbitrary slice. No infinitude or result on Ω(n)≥3 follows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
