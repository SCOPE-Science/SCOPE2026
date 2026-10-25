---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The domain is all h>=1 with X=16^h, B=4^h, q=2^h; n ranges are integer half-open and the palindrome counts exclude zero in both bases. Reconstructed each boundary count using base-b length formulas, and the first-region digit-pair reversal, two- versus one-event middle blocks, and the last-region base-four bit-swap involution. Its first-nonzero-signed-digit domination gives T_h=2*16^(h-1)+2*T_(h-1) and T_h=(B^2-q)/7. The four interval win/loss/tie formulas sum to the displayed shell totals, with P+N+Z=15B^2. Summing geometric shells gives distinct initial-segment positive proportions 13/280,3/35,3/140. Independently counted every integer and palindrome event on all h=1..4 shells and reproduced (12,94,134),(179,1665,1996),(2853,27235,31352),(45641,438087,499312). The finite check corroborates but does not prove unbounded h.

## originality

PASS

The same race can be written as a signed average of digit-reversal event offsets; digitwise point evaluations do not state exact sign frequencies over all 16-adic shells or the three conflicting density limits.

Older broader-in-base results are weaker in quantified sign-frequency strength; infinitely many sign changes do not imply failure of natural density, and pointwise inequalities do not compute shell census.

The theorem enumerates infinitely many integer inputs in an aligned arithmetic progression of growing shells; finite tables or single-n formulas do not already record the exact distribution.

The new claim implies quantitative frequency information not forced by the 2023 inequality; prior result does not imply any of the rational frequencies. The 2019 algorithm could be used in a separate proof but its statement is not the distribution theorem.

## value

PASS

The base-2/base-4 palindrome-counting race is a motivated prior mathematical problem; exact infinite-shell win/loss/tie distributions and demonstrated nonexistence of positive-race natural density go beyond a small table, reveal a structural base-alignment oscillation, and are useful to study digit-statistic races. The result is exact and self-contained within explicit h>=1 scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
