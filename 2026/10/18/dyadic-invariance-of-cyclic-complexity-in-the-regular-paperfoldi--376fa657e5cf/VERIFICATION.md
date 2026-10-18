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

The standalone `verify_paperfolding_cyclic.py` reproduces the exact word via two independent recurrence implementations, checks 20 finite pairs of lengths between \(8\) and \(256\), and checks the sharp failed boundary at \(n=4\). It verifies the published factor-count criterion at every tested length to make the factor enumeration exhaustive. The all-length theorem rests on the four-step proof in RESULT.md; the computation is corroborative only.

Execute `python3 verify_paperfolding_cyclic.py` from a directory containing the file. The expected output begins with `VERIFY_OK independent_paperfolding_recursion_32768_positions` and lists each pair of cyclic-complexity values. No independently performed scientific audit or external validation is claimed.
