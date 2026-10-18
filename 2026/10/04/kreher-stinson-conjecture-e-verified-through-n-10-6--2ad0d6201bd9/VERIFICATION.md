---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For every n≥1 the binary representation 2^n is 10...0 and is not a palindrome; thus b(2^n)=3 iff the ternary expansion of 2^n is palindromic. The actual C++17 source stores 2^n as little-endian base 3^39 chunks using exact 128-bit carry arithmetic, including leading zeroes within non-leading chunks; it scans all exponents through one million. For length≥24 it uses only the necessary condition that the first 12 digits equal the reverse of the last 12, with exact cross-chunk leading-digit extraction, then full symmetric-digit comparison on every survivor; length<24 receives full comparison. A separately compiled independent equivalent C++17 integer implementation fully ran all 1,000,000 exponents and returned hits 1,2,3,4 and exactly seven long-number filter survivors 41298,41299,41300,62318,377166,877495,918265; all seven were rejected by complete comparison. Finite proof only through the specified cutoff; it is not an infinite Diophantine proof.

## originality

PASS

The primary 2024 paper explicitly conjectures only four ternary-palindromic powers of two and computes all palindromic representations for n<64. OEIS A369233's linked table is described through n=10000. Current Resultary query found the candidate and unrelated digit combinatorics, not a stronger published exact scan. This best-of-knowledge result extends the documented public cutoff, but inaccessible private computations could exist.

## value

PASS

Kreher--Stinson's explicit conjecture makes the finite cutoff mathematically motivated. A million-exponent exact census extends the closest stated public OEIS table by factor 100, with a transparent necessary-digit filter and a fully replayable integer scan. Its scope is limited but nontrivial as a rigorous computational benchmark for a live digit-conjecture, not an arbitrary isolated small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
