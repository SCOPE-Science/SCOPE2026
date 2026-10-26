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

# Verification instructions and limits

Run `python3 constructive_check.py` and `python3 independent_check.py` with Python 3. Both terminate by assertion unless a check fails. They build the same graph independently: one from cyclic opposite-edge differences, the other from a two-row ladder with a crossed seam. Recorded outputs are supplied as `constructive_output.txt` and `independent_output.txt`.

The finite obligations are the base words at widths \(n=5,7,8,9,12\), and the validity of the initial four-column duplicate at \(n=7,9,12\). The proof in `RESULT.md` demonstrates that this local operation may be repeated arbitrarily often. Thus successful finite executions are **not** claimed to prove an infinite statement on their own. The residue-four construction is verified algebraically in the proof and additionally sampled by a program; the exception at \(n=8\) has a packing lower bound independent of solver status. All checks use actual standalone files in this package and make no external calls.

Publication priority is uncertain beyond the material explicitly inspected. Independent third-party mathematical audit is not performed.
