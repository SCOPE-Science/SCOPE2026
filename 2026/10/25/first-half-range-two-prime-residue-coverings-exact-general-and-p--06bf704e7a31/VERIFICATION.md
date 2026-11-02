---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The definition reduces E2(q;t) to a finite multiplication table of primes coprime to q. Submitted coverings.json lists a valid prime pair for each of 32 unit classes at 96 and 128 unit classes at 256; obstructions.json gives missing unit classes for each q<96 and each prime power q<256 (129 distinct lower candidates), plus failure at q=96 with max prime43 and q=256 with max prime113. Source verify.py checks each upper witness by primality and modular product, and independently tests all missing residues with modular inverses and complete pair-product enumeration. I separately implemented a sieve-and-image enumerator for every modulus q=2,...,256; its first success is 96, first prime-power success 256, it confirmed 129 distinct excluded candidates, and the exact upper images have cardinalities 30/32 at bound43, 32/32 at47, 127/128 at113 (missing81), and 128/128 at127. Prime gaps make the two bounds minimal. The result is purely finite; the computations are exhaustive over precisely the claimed range, not a sample from an unbounded statement.

## originality

PASS

Compared equivalent mathematical formulations, stronger coverage, exact-data overlap, and logical prior implication using primary material and actual Resultary searches. No materially inspected theorem was found to imply the complete final claim; this is a best-of-knowledge, not an exhaustive novelty certificate. All unread relevant material and other risks are recorded.

## value

PASS

A two-prime product set covering all reduced residues is a central finite benchmark for the Erdős–Odlyzko–Sárközy problem. The simple stronger half-modulus factor bound makes first success and the difference between unrestricted moduli and prime powers well-motivated exact invariants. Explicit minimal moduli, least prime cutoffs, and full reusable witness/obstruction certificates provide a complete natural initial classification even without a general asymptotic theorem; not a claimed solution of the infinite conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
