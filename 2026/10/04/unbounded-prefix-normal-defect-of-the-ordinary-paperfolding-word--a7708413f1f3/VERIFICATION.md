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

Run `python3 verify.py`.

The verifier reconstructs the ordinary paperfolding word from the odd part of each positive index. It checks the two prefix-sum recurrences for \(1\le N\le199999\), then verifies for \(2\le m\le21\) the identities used in the proof, the length of the displayed factor, and the exact excess \(m-1\). It also checks the corresponding finite-prepending witness for \(0\le c\le17\).

The quantified theorem is not inferred from these finite ranges. Its infinite validity follows from the symbolic recurrences and the two inductions in `RESULT.md`. The computation is a reproducibility and transcription check.

The result is limited to the ordinary paperfolding convention stated in the package and does not claim an exact formula for the global maximum prefix-normal defect.
