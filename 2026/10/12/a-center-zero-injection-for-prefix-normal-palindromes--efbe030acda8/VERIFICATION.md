---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For factor length k<=m, noncrossing factors survive in w; crossing factors lose an inserted zero, become length k-1 factors in w, and extend to k factors dominated by the original prefix. For k>=m+1, every factor and prefix crosses the center, and deleting the zero compares their respective k-1 factors in w. This is a quantified proof for every m>=1; center deletion is an inverse on images and all-ones word is outside. Independent enumeration of all palindromes for m=1,...,8 checked prefix-normality, image injectivity and strictness; counts (even,odd) through m=8: (2,3),(3,5),(4,8),(7,12),(11,21),(18,36),(31,57),(55,104).

## originality

PASS

The original Fleischmann–Kulczynski–Nowotka paper specifically studies npal(n), tabulates parity behavior and proves distinct two-step recurrences and palindrome constructions. Its examined main text and appendix do not formulate the all-m one-step center-zero injection. The 2021 dissertation is a plausible overlapping source but its full direct PDF was not read during this audit. No indexed Resultary analog was identified; this is a bounded best-of-knowledge assessment, not a priority guarantee.

## value

PASS

An explicit all-length injection proves strict odd-over-even inequalities for a naturally unresolved enumerative sequence, explaining parity asymmetry without extrapolating tables or solving the complete enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
