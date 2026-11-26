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

A conjugate power-base partition has distinct row widths that are powers of m and cumulative multiplicities at those widths that are powers of q. If the largest width has multiplicity greater than one, all cumulative multiplicities are divisible by q and the last operation is uniquely inverted by dividing the multiplicities by q. If the top multiplicity is one and its width is greater than one, shrink that row by a factor m, merging it with the next group if needed; this uniquely inverts migration. The sole terminal shape is one cell. Each inverse reduces area. These operations give a word encoding, with migration count k fixed by the largest width m^k and raise count t by the number q^t of rows. Area at most X implies k <= K and t <= T. Two applications of the hockey-stick identity to the sum of binom(k+t,k) over that box give the asserted bound, including equality of the envelope with the box word count but not with the area-restricted shape count. For L=log X, Stirling with arguments aL+O(1) and bL+O(1) gives alpha L minus (log L)/2 plus O(1) in the logarithm, including when alpha=1. Alpha is strictly increasing in a and b, hence decreasing in the respective bases; alpha(4,4)=1 exactly, alpha(2,11) is about 0.989797 and alpha(3,6) about 0.975146. The strict inequalities can be bounded with the positive atanh series for log and a geometric tail bound. At X=1 the sole shape has one cell. The named prior statements are correct, but in the inspected published text the locators are Theorem 2.7, Corollary 2.9 and Question 4.9, not the numbering used in the frozen record.

## originality

PASS

Credit the word bijection and symbol counts to Dietz–Flowers–Lockard and the equal-base congruence and special-class results to Flowers–Lockard. The supported addition is the area-induced counting envelope with its Stirling prefactor, giving a zero-density region for the whole represented support rather than just a sparse residue class. No equivalent or stronger support-count result for that region was verified.

## value

PASS

This partly answers a stated support-density question with a uniform fixed-base criterion and resolves the critical symmetric pair (4,4), where a plain X^alpha bound would not decide density. The result concerns distinct represented integers, not just multiplicities or a congruence obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
