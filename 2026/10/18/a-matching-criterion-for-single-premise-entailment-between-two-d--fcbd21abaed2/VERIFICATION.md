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

The proof establishes all unbounded statements. Reproduce finite witness checks with `python3 checker.py` in an ordinary Python 3 installation. The checker constructs 131 nonmatching 2-by-2 FD entailment tests on 3 attributes with triple-symbol grid coordinates; verifies source satisfaction and the respective maximal satisfying subteam size bounds by direct determinant-fiber counting. Its expected output is `FD_MATCHING_WITNESSES_OK 131`. These checks concern finite sampled instances, not a machine certification of the general theorem. Independent audit has not been performed.
