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

# Reproducible checks

Run `python3 verify.py` in the same directory as this file. The program uses only standard-library integer arithmetic. It directly computes the base-\(b\) and base-\(b^k\) representations of integers in each feasible exact-length interval, tests ordinary digit reversal, and separately applies the asserted block-array criterion. It then checks the exact count against the closed formula and verifies entire-base-power cumulative cutoffs whenever their full finite range is affordable.

A successful execution returned:

`VERIFY_OK: 134 exact length bins and 1148558 direct integer tests`

This includes bases \(2,3,4\), exponents from \(2\) through \(5\), block lengths from \(1\) through \(5\), with only bins whose upper endpoint does not exceed \(250000\) directly enumerated. The program tests no assertion about infinitely many indices. The general result depends on the digit-reversal identities and exact combinatorial summation supplied in the proof; the exhaustive *finite* comparisons do not certify them externally. In particular, no independent mathematical audit has yet been performed.
