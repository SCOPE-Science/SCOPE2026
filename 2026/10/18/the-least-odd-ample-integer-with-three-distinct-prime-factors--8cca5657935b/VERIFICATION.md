---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

From a(n)=1+Σ_{proper d|n}a(d), strong induction on divisors proves sigma(n)<2n implies a(n)≤n because divisor abundancy is monotone under divisibility. For at most two odd prime factors, the limiting Euler product is <2; for exactly three, supports outside {3,5,7},{3,5,11},{3,5,13} are likewise excluded. On support p,q,r, the recurrence depends only on exponents. Expanding A(X,Y,Z)=1/[2(1-X)(1-Y)(1-Z)-1] gives an exact seven-neighbor integer recurrence with boundary zeros. Independent Python recomputation over the complete exponent box, filtering p^i q^j r^k ≤ N*=3^20·5^9·7^6, confirmed exactly 4650+3718+3459=11827 eligible triples; only (20,9,6) is ample, with a(N*)=841632661765951062016 and N*=801204488268064453125; among strict smaller candidates minimum deficits are79,139,169. The proof establishes the necessary finite cutoff; no infinite conclusion is drawn from an incomplete search.

## originality

PASS

Best-of-knowledge priority assessment distinguishes the actual joint/exact invariant and mathematical implications from stronger but non-covering frameworks; pertinent primary statements were compared and residual risks are explicit. Least odd ample integer with exactly three distinct prime factors

## value

PASS

Determining the first odd ample integer at its minimum possible support size of three primes is a canonical sharp natural invariant of the recursive divisor function, separate from the smaller unrestricted odd minimum. The exact minimizer and complete 11827-triple certificate provide a reusable boundary for the classification and a test of support-local abundance principles. It is not arbitrary exponent slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
