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

# Reproducibility and verification

`verify.py` is a standalone Python 3 implementation with no third-party packages. Run `python3 verify.py`. The accompanying `verify_output.txt` is the captured output of executing exactly the packaged script.

The checker constructs vertex adjacencies for each labeled circular ladder, generates each two-packing through distance-at-most-two exclusion, and tests the defining induced-edge condition on undominated vertices. For each \(3\le n\le21\), it compares the complete cardinality histogram against \(\frac{2n}{k}\binom{k}{n-2k}\) in its permitted range. For each \(3\le n\le14\), it compares the full family of vertex masks with a separate generator that uses alternating rows and gaps two or three. Over the first 120 circumferences it verifies the formal-series recurrence, with exact integers throughout. On success the program prints `RECURRENCE_120_OK` and `VERIFY_OK`.

This does not establish the infinite claim independently: the unrestricted proof is the local-gap equivalence and the counting argument in `RESULT.md`. No external or independent mathematical audit is represented by this verification file.
