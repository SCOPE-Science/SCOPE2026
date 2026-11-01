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

# Reproducibility

Run `python3 verify.py` from the directory containing `verify.py`; only Python's standard library is needed. On successful execution the program prints `BASE_OK`, `UNIVERSAL_FIBERS_OK`, `LOW_BOUND_OK` for the five values 2 through 6, and `VERIFY_OK`.

The verifier begins with the original bidirected graph, enumerates all nonempty multipaths in six probe columns, and constructs the complete Hasse digraph with matched cover edges reversed. Its topological sort proves that there is no directed cycle, while its critical-face count is one vertex and 169 tetrahedra.

Next, it enumerates all 312 valid nonempty external configurations on four symbolic columns. Since every multipath contains at most four arrows, any external configuration for any number of extra columns relabels to one of these cases. The program checks acyclicity for each fiber and exactly the residual profile asserted in the proof. This establishes an all-parameter finite certificate for the combinatorial matching step, subject to the mathematical argument that those symbolic patterns exhaust every external fiber.

Finally the checker performs independent mod-two boundary-rank calculations for small right class sizes 2 through 6. Those small cases establish the sharp threshold, but no assertion is made that finite parameter testing alone proves infinite statements. The all-parameter proof additionally uses the standard poset patchwork and discrete Morse CW theorems and an explicit face-number count.

Independent mathematical audit and external proof-assistant verification have not been performed. An earlier unindexed equivalent result remains a possible scientific limitation.
