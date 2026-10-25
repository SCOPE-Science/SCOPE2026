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

# Reproducibility and limitations

Run `python3 CHECK.py` using Python 3.8 or later. This standard-library script factors the selected small values of \(h\), enumerates exact first-zero depths of \(r\mapsto r+r^{-1}\pmod p\), constructs all local weighted outcomes, and multiplies them by unions of index sets. It checks every residue class modulo \(h\operatorname{rad}(h)\) for the listed \(h\), and separately compares the first seven reduced integer numerator iterates on sample seeds. A successful run prints `VERIFY_OK`, with the explicit \(h=145\) counts. All checks completed successfully in the recorded run.

The argument establishing the result for unbounded \(h\) is in RESULT.md. A finite check cannot independently certify the global theorem or guarantee novelty. The companion preprint cited in the original source was not available for full comparison. Independent audit has not been performed.
