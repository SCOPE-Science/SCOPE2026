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

For every nonempty X with identical first/last symbol a and no adjacent aa, and fresh z∉X, T=XzXXzX^- contains exactly two z's. The maximal aligned repeated factor containing z is B=XzX^- at starts 0 and 2m+1; each z-free run X, XX, X^- contains complete X copies only at 0,m+1,2m+1 because the join XX uniquely creates aa. The middle X has unique left/right extensions, hence a net occurrence; proper factors of these three marked repeated occurrences have at least one repeated one-symbol extension and cannot be net. Any repeated factor containing z aligns the two z's and is contained in a B; any repeated z-free factor either cannot cross unique aa or is contained in a complete X. Thus exactly (0,2m),(m+1,m),(2m+1,2m) net position-length pairs. The Zimin recursion Z_{j+1}=Z_j j Z_j, no '00', gives W_d=Z_d, W_{d+1}=Z_{d-1}(d−1)Z_{d-1}Z_{d-1}(d−1)Z_{d-1}^-, and earlier iterates have exactly two repeated maximal Z-block occurrences. Reconstructed this induction; independent all-factor extension enumeration checked 379 admissible marked words, corroboration not infinite proof. k=0,1 zero, 2≤k≤d two, k=d+1 three (d≥3). No assertion for higher k.

## originality

PASS

Guo–Kishi 2025 proves the special Fibonacci and Thue–Morse net-occurrence counts; the marked-square lemma is a different structural criterion, not a restatement of a Fibonacci count. Faro–Pavone 2026 addresses period-aligned regular epistandard morphic approximants; its full paper was inaccessible, so its abstract does not justify blanket noncoverage. The particular first post-Zimin initial d-bonacci iterate W_{d+1} is not the period-aligned iterate described by the accessible abstract. The all-alphabet marked-square theorem has not been shown to follow from the inspected literature, but possible implicit general string combinatorics and the inaccessible plausible paper are material risks.

## value

PASS

This is a structural classification of repeated factors with unique extensions, giving an exact and unexpectedly stable three-occurrence mechanism across arbitrary alphabets/word lengths; it also identifies the earliest natural d-bonacci transition beyond the Zimin prefix. It resolves a motivated boundary of net-occurrence enumeration rather than an arbitrary one-off numeral. Finite experiments are corroboration of the general factor argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
