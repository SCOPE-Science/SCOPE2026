---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the intermediate-palette enumeration

Run `python3 verify_intermediate.py` with the Python standard library. It compares the inclusion–exclusion count to an exact union-size dynamic program for labelled blade assignments, tests positivity for every intermediate palette of the selected graphs and vanishing for the first excluded larger palette, and checks the large endpoint \(q=N\) by the closed count \(N!\) of minimum assignments. The selected graphs have \(3\le r\le8\) and \(2\le m\le6\).

The equality for all allowed parameters follows from the proof in `RESULT.md`: the degree bound forbids a leaf force, and inclusion–exclusion counts those all-leaf seeds whose colour union permits the unique hub step. The checker compares counts, not alternative propagation rules or originality.
