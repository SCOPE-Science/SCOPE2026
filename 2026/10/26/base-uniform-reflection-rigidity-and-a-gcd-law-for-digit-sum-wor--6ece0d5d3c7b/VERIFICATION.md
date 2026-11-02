---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Reconstructed base-b carry identity t(bq+j)=t(q)+j and exact adjacent-pair relation c−a≡1 mod gcd(b−1,m), including a constructive realization using trailing (b−1) digits. Every four-window at b≥3 crosses at most one substitution-block boundary, hence two of its three adjacent increments equal +1; its reversal would require two −1 increments, impossible in one four-window for m≥3. Length-three reverse companions must be palindromes. Explicit three- and four-factor families have sizes 2m²/d−m and 3m²/d−2m by inclusion-exclusion; reversal of length-two pairs occurs exactly for d|2, giving displayed gcd trichotomy. Independent direct-prefix tests across 20 base/modulus combinations and three lengths were honest subset checks; 48/60 prefix counts were complete, 12 were not because prefixes do not necessarily realize the full infinite language. All 60 avoided contradictory reversals. Infinite result rests on constructive adjacency and substitution boundary proof.

## originality

PASS

PASS qualified: Allouche–Campbell–Li–Shallit–Stipulanti (2024) Question62 explicitly raises generalized reflection complexity and gives a base2/modulus3 instance; Starosta (2011) establishes ordinary factor complexity and short factor sets for generalized Thue–Morse, and Allouche–Shallit (2000) treats ordinary palindromes. Factor complexity and palindrome absence alone cannot determine the number of distinct reversal-orbit classes. The new short +1 increment argument covers every b,m≥3, including periodic ones.

## value

PASS

PASS: A published reflection-complexity question motivates precisely these digit-sum words. The complete base≥3 all-modulus classification includes a nontrivial gcd(b−1,m) trichotomy for short factors and an all-length ordinary-reversal obstruction; it distinguishes periodic from aperiodic families. The +1-increment argument is elementary but solves a substantive natural family-wide invariant, not an arbitrary tiny example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
