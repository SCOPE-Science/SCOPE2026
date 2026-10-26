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

## Reproduction
Run `python3 check.py` in this package with standard Python 3. It enumerates every binary-field rank-\(s\) idempotent in each listed finite case through frame--coframe representations, deduplicates the actual \(n\times n\) matrices and verifies idempotence by direct multiplication. It obtains ranks of both ordered products directly from those matrices; its separately enumerated uniform rectangular-matrix reference distribution is not derived from the claimed probability bound. The printed total-variation fraction is compared with the derived full-row-rank-event upper bound. The recorded output is in `check_output.txt`.

## Logical scope
These finite checks confirm sample identities through \(n=5\) only. The proof uses an exact conditional-distribution argument and finite-field rank enumeration for every fixed prime power and prescribed ranks. No external/independent audit has occurred.
