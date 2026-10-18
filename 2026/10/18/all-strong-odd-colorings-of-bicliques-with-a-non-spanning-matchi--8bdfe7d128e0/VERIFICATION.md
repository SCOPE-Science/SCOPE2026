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

Run `python3 verification/verify.py` with Python 3 (standard library only). The script constructs adjacency directly and enumerates all proper canonical set partitions for every \(2\le a\le b\le5\) and \(0\le t<a\), then tests the strong odd condition at every vertex for every color class. It checks the exact coefficient histogram, the minimum number of classes, the number of optimal partitions and several finite palette evaluations of the polynomial. Additional arithmetic-only profiles test larger parameters.

The recorded run returned `VERIFICATION_OK exhaustive_profile_cases=30 canonical_partitions_tested=22259`. Its full output is `verification/output.txt`. These checks do **not** prove the claim for unbounded parameters. The universal mathematical proof is in `RESULT.md`.

No independent audit has been performed.
