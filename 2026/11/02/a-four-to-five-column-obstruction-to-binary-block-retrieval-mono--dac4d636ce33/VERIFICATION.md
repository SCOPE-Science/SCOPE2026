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

# Reproducibility and boundaries

Run `python3 verify.py` in a directory containing the supplied file. It uses only the Python standard library and computes rational retrieval expectations independently via the sampled-subset formula and via the finite-state span process. It verifies the four-column witness and exhausts all rank-three five-column binary generator multisets including zero columns.

The actual run produced the bundled `verification_output.txt`, beginning with `VERIFY_OK`. The two calculations agree for all 476 rank-three five-column multisets, twelve have \(E_1\le2\), and their minimum \(E_2\) is \(15/2\). The proof in `RESULT.md` establishes the structural dichotomy directly; this finite check does not prove broader field or length statements. Independent audit has not been performed.
