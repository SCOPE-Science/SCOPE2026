---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

The Euler-trail existence criterion is proved and applied in RESULT.md. The generating functions for fixed signed net flows are valid as formal power series for each finite transition total. Their sum partitions every realizable matrix according to its nonloop support size and divergence and therefore proves the unrestricted \(n\ge1\) result. Enumeration is supplemental.

The provided `verify_words.py` calculates transition-count profiles from every word over the labeled ternary alphabet for lengths one through eleven, compares unique profiles to rational-function coefficient extraction, and records all equalities in `verify_words.out`.

The provided `verify_matrices.py` independently enumerates every nonnegative nine-entry matrix of edge total at most fourteen; compares weak connectivity and degree divergence with explicit integer-flow counts; and records the checks in `verify_matrices.out`. The matrix criterion concerns graph-theoretic existence rather than enumerated word occurrences.

Replay in the directory containing these four files using standard Python 3: `python3 verify_words.py` and `python3 verify_matrices.py`. No third-party libraries or external network access are required. The tested lengths are finite and do not independently certify the asymptotic statement or the all-length theorem. The exact proof, not this enumeration, establishes both.
