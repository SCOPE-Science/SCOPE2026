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
# Verification

The analytic proof is the primary evidence.

`artifacts/verify.py` checks properness and the odd condition directly from neighborhood color multiplicities. It verifies the cyclic \(n\)-color construction for every \(1\le m<n\le20\), and the balanced \(n+2\)-color construction for every \(2\le n\le50\).

For \(2\le n\le4\), it additionally exhausts every proper coloring of \(K_n\square K_n\) with \(n\) or \(n+1\) colors after fixing the first row by global color symmetry. It finds no odd coloring in either forbidden palette size.

Replay output:

`ALL CHECKS PASSED; unbalanced_constructions=190; balanced_constructions=49; balanced_exhaustive_n=2..4; proper_completions_checked=4994`

The exhaustive finite search does not prove the arbitrary-\(n\) lower bound. That lower bound follows from the row/column missing-color argument in `RESULT.md`.
