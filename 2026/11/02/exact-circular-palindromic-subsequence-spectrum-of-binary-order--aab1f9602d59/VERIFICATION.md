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
# Computational verification

The theorem concerns all \(2048\) binary order-five de Bruijn cycles and their \(65536\) linear roots. Running `python3 checker.py` (Python standard library) executes both exhaustive cycle enumerations and both palindromic-subsequence dynamic programs. It prints `VERIFY_OK 2048 65536` only after exact assertions of all tables and full agreement between constructions; it also writes `summary.json`. The included `summary.json` contains the precomputed full joint table and a SHA-256 of the sorted canonical cycle list.

## Independent mathematical controls inside the finite computation

1. Feedback method: iterates every one of \(65536\) possible complementary state-permutation tables and selects full \(32\)-state cycles, exactly covering the mathematical domain.
2. Euler method: enumerates every Euler tour of the order-four de Bruijn graph, fixing the unique zero-labeled length-five edge as the first edge. Exactly \(2048\) tours result, with precisely the same canonical words.
3. LPS method: interval recurrence on all rooted words, checked against LCS with reversal using a separate two-row dynamic program.
4. Structural checks: each cycle has exactly \(32\) different circular length-five windows; all numerical counts sum to the independently determined domain sizes.

## Limits

These checks are exhaustive only for binary order five. The matching algorithms reduce implementation errors but are not a separately conducted human or external independent audit. The complete proof is the finite exhaustiveness argument plus the precise algorithm and its verified output, not the output text alone. Source priorities remain qualified.
