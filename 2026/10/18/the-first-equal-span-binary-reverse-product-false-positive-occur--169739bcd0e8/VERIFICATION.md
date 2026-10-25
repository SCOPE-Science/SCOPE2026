---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For endpoint-anchored binary words, P(z)P(z^-1) is exactly the two-sided autocorrelation generating Laurent polynomial, and D=2^(L-1)P(2)P(1/2) is just one evaluation. Direct bit arithmetic gives A=1100125 and B=1269125, reverse integers 1528417 and 1324889 and common product 1681449752125; populations 10 and 11 differ. Independently reconstructed the COMPLETE exact enumeration over all 2^(L-2) anchored words modulo reversal for each 2<=L<=21; no deficient product fiber until L=21 and exactly one exceptional product fiber (with two reversal classes) at L=21 among 262231 distinct products. Reversal preserves D and correlation, so enumeration does not omit candidate collisions. The theorem is only a finite equal-span statement, not a higher-length or unequal-span classification.

## originality

PASS

The exact converse posed in the older point-distance generating-function note is refuted by the explicit twenty-one-bit example; the complete first equal-span failure at L=21 supplies a sharp finite boundary beyond that source’s observations below span sixteen. Full Fourier phase-retrieval homometry theorems require equality of the entire autocorrelation polynomial and do not imply equality from one off-unit-circle evaluation.

## value

PASS

The object is a natural finite point-set/phase-retrieval encoding and the invariant is the aperiodic autocorrelation/power spectrum. Numerical reverse-product equality has been used as a possible proxy for homometry; a first explicit false-positive witness plus a complete minimum-length uniqueness certificate pinpoints precisely where the proxy becomes unsound. This is a motivated finite boundary, not an arbitrary bit length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
