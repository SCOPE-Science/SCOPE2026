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

For equal-length binary blocks, 2-binomial equivalence is exactly equality of number of ones k and position-weighted ones sum S (since scattered 01 count is S-choose(k,2)). Every starting index has unique i=128j+r and its 72-letter window is a subword of μ^7(t_j t_{j+1}), so exactly four possible adjacent source pairs times 128 offsets cover every index; a complete 512-case enumeration is thus an infinite-word proof, not finite prefix extrapolation. Independently rebuilt all 512 templates from the morphism and scanned all 1≤m≤36 for equal (k,S); recovered source-pair histograms, all nine densities, six worst templates, and witness i=19. Weighted pair frequencies are (1/6,1/3,1/3,1/6), obtained by primitive-substitution invariance. Compared against the entire frozen templates.csv and verified code logic, which uses a separate direct scattered-subsequence counter.

## originality

PASS

All four comparisons are grounded in actual primary or published-record searches; best-of-knowledge only. Checked possible equivalence between local least-root laws, recurrence of binomial squares, and global factor-complexity/avoidability results. Existing statements inspect different quantifiers: number of factor classes or existence of pattern-free words, not minimum root for each fixed i.

## value

PASS

The least adjacent 2-binomial-square root at every starting position is a natural recurrence/avoidance invariant of the canonical Thue–Morse automatic word. A sharp universal radius, complete possible-root spectrum, all exact densities and precise extremizers provide a full local classification rather than a single finite test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
