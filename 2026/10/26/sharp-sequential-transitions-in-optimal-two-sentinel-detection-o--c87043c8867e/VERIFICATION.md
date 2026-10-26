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

# Reproduction and limits

Run `python3 verify.py` in this package and compare its canonical one-line JSON output with `verification_certificate.json` (the certificate includes the terminal newline). The checker uses exact rational arithmetic, enumerates all percolated edge subsets for 483 small placement cases, evaluates all 26,946 placements over the specified parameters, checks 2,430 neighboring-distance difference formulas, and verifies rational threshold-order brackets for path sizes 4 through 99.

This is a finite consistency check, not a computer proof for arbitrary path size or real transmission probability. The complete analytical proof is in `RESULT.md`; assumptions exclude transmission retries, correlated edges, finite-time detection, and other surveillance objectives. Independent audit is not performed.
