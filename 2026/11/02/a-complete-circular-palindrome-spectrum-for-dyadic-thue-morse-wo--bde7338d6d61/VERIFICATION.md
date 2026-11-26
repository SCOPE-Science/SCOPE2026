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

Check the argument on periodic extensions, only counting strings of length at most one period. At rank j≥1 each length-three window contains a full complementary substitution pair, hence there is no constant triple even across the boundary. A length-five palindrome at either alignment forces a constant triple in the preceding periodic extension. Both 010 and 101 occur in T_3 as ordinary factors and persist since each T_j is a prefix of T_{j+1}; odd antipalindromes are impossible. For length 2t, the even- and odd-aligned maps are μ(v) from t input symbols and G(u)=complement(u_1) μ(u_2...u_t) u_{t+1} from t+1 input symbols. Both are injective and reversal of either output is its map applied to the reverse-complemented input. Thus a palindrome comes from an antipalindrome, forcing one of the two alignments according to t parity, whereas antipalindromes come from palindromes in both alignments. An output G(u) also in the even-aligned image must have complementary pairs at positions (1,2),(3,4),..., forcing consecutive u symbols equal. This is impossible for t≥2 by the triple prohibition. At t=1, both 01 and 10 occur in both images: the preceding iterate contains 00 and 11 cyclically from rank 2 onward (visible at rank 2, and both occur internally in rank 3 and persist). At t=2^{k−1} the only over-one-period input relevant to the antipalindrome count would be an odd palindrome of length at least 5, excluded even in the periodic extension. For k=3 that exclusion uses the no-triple fact already at rank 1 to rule out length 5 in periodic T_2. Direct enumeration of the rotations and short factors of 0110 gives the base p_2=6, a_2=4. Summation counts each even input length twice in the palindrome recurrence and loses two unit palindromes plus the two overlaps in the antipalindrome recurrence. Hence p_k=4+2a_{k−1} and a_k=2p_{k−1}−4, so p_3=12 and p_{k+2}=4p_k−4 for k≥2. Solving on parity classes yields the two displayed totals and their distinct density limits.

## originality

PASS

The supported distinct claim is the exact finite-dyadic one-period circular palindrome and antipalindrome spectra, and in particular the parity-split palindrome total. Neither general infinite-word complexity nor exact circular classifications for other sequences were found to cover it; full-text access to two relevant comparators remained limited.

## value

PASS

Dyadic substitution iterates of Thue–Morse are canonical finite objects. The exact one-period spectra resolve wraparound without overcounting aligned occurrences and show that even the aggregate normalized palindrome count does not converge across ranks. The two-map count and sole overlap are useful structural controls beyond the infinite-language complexity bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
