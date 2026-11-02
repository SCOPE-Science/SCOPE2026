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

# Reproduction and scope

Run `python3 verify_closed_four_runs.py` with Python 3.9 or newer and only its standard library. The expected completion marker is `VERIFY_OK`. The program enumerates all positive four-run compositions through length \(16\), uses both an occurrence-count border test and a separate prefix-function border test, and compares the resulting distinct-factor sets with the five explicit classes in the proof. It additionally compares the exact maximizing counts, tests longer deterministic samples, and checks the bivariate generating-function identity coefficientwise through length \(20\).

The all-length theorem is proved analytically in RESULT.md, and finite checks do not certify all infinite parameter choices. The public package contains the program source, proof and review, with no dependencies on external artifacts. Historical priority and independent mathematical validation are not certified.
