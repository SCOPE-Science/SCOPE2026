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

With units digit t and leading digit s, the carry recurrence starts at -4 and ends at 0; c_i is in {-1,0,1} for i>=1, and once nonnegative stays so. The outside equations give 3s=4+b c_1-2c_(L-1). A negative c_1 forces t=1, s=b-2, incompatible with the final equation; c_1=0 forces 3s=2 or 4. If c_1=1 and c_(L-1)=0, length two is already impossible and otherwise b=2 mod 3; the next mirrored equations give 3a_1=2b c_2-2-c_(L-2), either negative or nonzero modulo 3. These equations remain valid when the two mirrored positions coincide (length three). Thus both outer carries are 1, giving s=(b+2)/3 and t=(2b+7)/3; the digit bound on t imposes b>=10. At each inward pair integrality forces 2x-1-y=0 mod 3 for x,y in {0,1}, hence x=y=1, and both digits are b-1; a central digit satisfies u+1=b. Direct reversal of the resulting expansion proves existence, including the empty middle block. For primes the equality reduces to q=p-2; odd admissible bases give even digit sum and an even candidate, and the even length-two expansion gives the displayed quadratic pair. Independently enumerated every eligible integer in bases 4 through 17 at lengths 2 through 4 (303,765 inputs), with agreement; replay python3 /workspace/reproductions/independent_finite_checks.py. The frozen verification script was inspected, not executed.

## originality

PASS

Pass for the arbitrary-base and arbitrary-length affine classification and the resulting restrictions for the specified prime subcase, not for the decimal specialization or the already-published base-16 example. The strongest shifted-reversal paper studies commutation with an affine map, not affine reversal of a single input. No inspected covering theorem gives the forced digits and congruence across bases.

## value

PASS

The offset -4 is forced by the arithmetic function for a reversal equal to twice an odd prime, rather than picked from a parameter table. The rigidity theorem replaces a search over every integer of each base and length by one explicit pair of primality tests in eligible bases and none elsewhere. It separates digit rigidity from prime occurrence and yields the odd-base obstruction, without claiming infinitude or solving the general-base prime question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
