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

For a reproducible check, put `verify.py` and `certificates.json` together and run `python3 verify.py certificates.json`; compare stdout against `checks.txt`.

The verifier recomputes all pairwise-OR outcome supports for the displayed column bases, exhausts the 17,902 canonical five-query bases with zero to four additional nonunit columns, validates the complete adaptive-query tree paths and all 62 witness leaves, and independently recomputes all eleven finite adaptive dimensions by a memoized exact recurrence. The required static and adaptive upper bounds also have independent written combinatorial arguments in `RESULT.md` (obligatory columns, triple-counting, cardinality, and binomial root-branch obstruction); numerical experimentation does not replace those proofs.

The finite census goes no further than twelve input coordinates. The unbounded-dimension column criterion is a definition-level equivalence, not an assertion of exact dimensions beyond the recorded range. No third-party independent mathematical audit is represented by this report.
