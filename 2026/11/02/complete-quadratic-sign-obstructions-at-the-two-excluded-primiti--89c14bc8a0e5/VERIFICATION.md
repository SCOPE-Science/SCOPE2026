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

Verified scalar-projective sign obstruction invariance (square scalar preserves and nonsquare scalar swaps + and -). There are p^2+p+1 normalized projective triples; removing p+1 points of the nondegenerate discriminant conic and the excluded (0,1,0) leaves p^2-1 admissible. Computed all primitive roots by the exact multiplicative-order test and all nonzero square residues; fresh independent exhaustive integer enumeration across all p^2-1 normalized classes agreed exactly with every listed tuple for p19 and p31, 9/360 and 3/960; raw multiplicities follow by free scaling with p-1. The supplied verifier additionally enumerates all p^3 raw triples and normalizes at the end, a complete independent algorithm path; all loops are finite bounded, not an infinite-prime inference.

## originality

PASS

PASS at best knowledge for a tightly bounded exact exception census: Sun’s revised Conjecture 4.9 explicitly isolates 19,31 but gives no projective coefficient classifications in inspected text. Booker–Cohen–Sutherland–Trudgian study primitive values of quadratic polynomials and list stringent exceptional cases, but primitive-value existence is a stronger predicate than square/nonsquare sign variation and does not by itself tabulate these two sign-obstructed sets. Existing finite primitive-root tables could conceivably imply exact tuples: priority risk explicit.

## value

PASS

PASS within the natural finite-cutoff standard: this is not an arbitrary small-prime slice but the complete classification of the exact two primes excluded in a named published quadratic-character conjecture; the normalized exceptional coefficient families and sharp fractions resolve the full finite boundary cases. It does not claim a proof or extension of the conjecture elsewhere, and finite self-contained classification is valuable without a general theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
