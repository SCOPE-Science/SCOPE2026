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

For a word of length m, reflection j->c-j mod m with 0<=c<m reverses both the prefix of length c+1 and the complementary suffix. Conversely a split into two palindromes gives that reflection, and rotating conjugates the reflecting index map. In sigma(w), even positions are 0 and odd positions are complemented letters of w. A reflection with even c fixes the two parity classes and acts on odd positions as j->c/2-j-1 mod m; one with odd c could occur only when sigma(w) is entirely zero, in which case w is constant. Hence desubstitution preserves and reflects the predicate. An odd-aligned factor of even length drops the initial zero from the aligned block and appends the zero from the next block, precisely a cyclic rotation. This proves length-doubling equivalence. The length-3 language follows from the length-2 language {00,01,10} and the two alignments, and length 5 follows in the same way from length 2 and 3, yielding exactly the listed words; the four non-palindromes at length 5 split as 00|010, 010|00, 00|101, 101|00. The two cited length-7 factors occur at zero-based positions 1 and 7, and the unequal circular gaps 1,2,4 between the three ones forbid a reflection. The published periodicity count is a count of distinct factors of the complemented fixed point, which leaves both predicates invariant. Its four interval differences from total complexity are 2r, 2r-2^(k-1), 2r-2^k and 2r-3*2^(k-1), respectively. Thus for every odd n>=9 some factor is not even a palindromic periodicity, whereas equality alone cannot prove any positive case. The explicit small lengths and length doubling complete the proof. Fresh reproduction matched complete factor languages by exact complexity and the split test through length 128; split/reflection equivalence and substitution preservation were also checked on all binary words through length 8.

## originality

PASS

The reviewed contribution is the exact palindrome-pair spectrum, not the factor-complexity or palindromic-periodicity counts. The closest earlier exact result reaches a broader word predicate and leaves the decisive odd-part-7 case unresolved for palindrome pairs. A distinct later Resultary record gives precisely the same palindrome-pair spectrum; no earlier exact coverage was established, and this date comparison does not certify priority.

## value

PASS

The result answers the stronger exact-length version of a natural palindrome-pair question for a canonical automatic word. It identifies an entire dyadic family where all factors are palindromic periodicities but some are not pairs, and the exact doubling argument makes that distinction structural rather than a small-length artifact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
