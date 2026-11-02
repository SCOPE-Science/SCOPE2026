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

# Verification record

The direct finite verifier is `verify.py` and requires only Python 3 standard libraries. Invocation:

```sh
python3 verify.py
```

The executed run reported `VERIFY_OK cases 102 distinct_pattern_cases 364 start_checks 465`. It generated one-positions by direct base-digit membership and also by the independent binary-to-base map; exhaustive window scans at each sampled first-attainment length agreed with the explicit residue-pattern classification. At the same lengths, the preceding length had a maximum weight one smaller. This verifies examples but cannot alone establish the theorem for all bases or all \(k\); those follow from the proof's binary-carry identity and gap-injectivity step.

Scientific originality assessment is based on accessible published texts and expressly identified source-access limitations; it is not an independent scientific audit.
