---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Canonical leftmost subsequence embeddings are in bijection with right-to-left masks deleting a symbol only when different from the nearest retained symbol (or no retained symbol exists). The resulting three-state automaton and its nine-state tensor product give the precise resolvent. Its claimed rational closed form is proved for ALL n by polynomial numerator identity: adjugate u-degree <=8, determinant <=9, claimed numerator <=4 and denominator <=5, so equality through u^13 forces polynomial identity. Independently checked mask versus all deleted-output sets for every binary word n<=8, B3 exact mean and variance n<=11, plus inspected both distinct rational certificate scripts. Endpoints B0=Bn=1 and n=0 included. Finite checks are corroborative only; no biased-letter claim.

## originality

PASS

Known expected distinct-subsequence counts and single-radius/two-deletion variances do not imply correlations between every pair of deletion radii. The nine-state rational joint enumerator and its three-deletion/total-count variance consequences survive best-of-knowledge comparison. Historical full text from Mercier et al could contain unindexed stronger transfer identities; access limitation is not claimed as proof of novelty.

## value

PASS

A joint all-radii covariance kernel is a natural exact statistic in deletion-channel combinatorics: unlike a mean or deterministic radius bound it determines the fluctuation and covariance of every pair of sphere sizes and the total distinct-output variance; the polynomial certificate also turns an infinite family into a finite algebraic identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
