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

# Exact verification

Execute `python3 verify.py` with Python 3.10 or newer and no third-party dependencies. The deterministic code writes `coverage_depth_spectrum.csv` alongside the program and prints `verification_output.txt`-compatible output. All expectation arithmetic uses exact rational fractions.

The program enumerates all \(3432\) unordered seven-column multiset profiles over the eight vectors of \(\mathbb F_2^3\), filters the \(2696\) rank-three profiles, and compares a subspace-Möbius expectation with an independently calculated information-subset expectation on every profile. It then enumerates all \(2097152\) ordered seven-column matrices and verifies that their code-value histogram agrees with multinomial profile weighting. It checks the \(42\) value levels, \(11811\) labeled codes, exact mean and variance, the simplex and second-tier populations, the missing/duplicated-point classification, and the relevant \(168\)-element group action. The replay terminates with `VERIFY_OK`.

The complete output-value census is a finite proof for this precise parameter instance, not a proof of analogues for arbitrary dimension or alphabet. The check of group action and probability formula is implemented directly in the included source. No external independent validation is claimed.
