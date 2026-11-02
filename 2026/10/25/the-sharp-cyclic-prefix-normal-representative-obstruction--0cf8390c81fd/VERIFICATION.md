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

The source uses exactly the defining equality between prefix one-counts and maximal linear-factor counts for every length and every cut. My independently written enumerator tested all 2^n rooted words and all rotations for each n=1..11, with 0 bad necklaces through n=10 and precisely the stated three at n=11; 33 rooted words. Read the source gap-composition proof: a shortest span of k+1 consecutive ones is determined by k adjacent gaps and its prefix competitor; the last circular gap is excluded after the cut. The included witness CSV contains 33 explicit prefix/factor comparisons. The all-n witness is proved separately: zero-start cuts fail at length 1, starts at positions 3,5,7 fail due to later 11, start 9 fails by 10101 against 11000, and start 10 fails by 101 against 100. Extra n=1000 check is corroborative, not an unbounded proof.

## originality

PASS

The exact boundary at n=11 and the three first-exception rotation classes concern existence of a prefix-normal rotation of the original necklace, not uniqueness or existence of a canonical prefix-normal form in the larger jumbled-equivalence class. Author-version Fici–Lipták Theorem 1 and Burcsi et al. gap Lemma 2 provide existing linear theory and method, not this cyclic threshold; targeted Resultary search found no direct covering record. Best-of-knowledge only.

## value

PASS

The question is naturally forced by prefix-normal canonicalization of strings without a designated starting point. Exact smallest failure, complete three-necklace obstruction census and an explicit obstruction at all longer lengths establish a sharp genuine transition with reusable counterexamples, rather than an arbitrary fixed-size bit-string count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
