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

# Reproduction and proof boundary

Run the standard-library Python 3 program `verify.py` in this package. It constructs, without using the cyclic-increment characterization, all scattered subsequences of each phase's contiguous length-\(p\) window and independently identifies the absent words whose every one-letter deletion is present. Those full sets are compared against the claimed local classification, with alphabet/window pairs \((q,p)\) given by \(q=2\), \(1\le p\le11\); \(q=3\), \(1\le p\le8\); and \(q=4\), \(1\le p\le6\). There are 25 complete parameter cases. In the binary cases the histogram by word length is also compared with the coefficients of the proposed bivariate rational generating function.

The expected success message is `PASS cyclic-window minimal-absent direct exhaustive vs distance characterization and binary recurrence; cases 25`.

The proof of all-parameter correctness is the separate minimum-span/deletion-cost argument and weighted transfer derivation in `RESULT.md`. The test is a finite independent computational cross-check, not an infinite proof or independent audit. Symbolic simplification of the transfer matrix was separately checked for \(q=2,3,4,5\) using exact rational polynomial arithmetic; that symbolic calculation is a supplementary check, not a dependency needed to run the standalone program. Mathematical originality is compared in `REVIEW.md` and `AUDIT.json` and remains subject to ordinary bibliographic uncertainty.
