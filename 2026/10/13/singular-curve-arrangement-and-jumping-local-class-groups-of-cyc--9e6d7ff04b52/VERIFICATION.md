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

# Reproducibility and proof limitations

The mathematical verification is a symbolic proof with bounded computational regression checks. Run from the directory containing this file with an environment providing Python 3, SciPy, and SymPy:

```shell
python3 -m pip install -r checks/requirements.txt
python3 checks/check_cycle_cut.py
```

Compare the resulting JSON object with `checks/check_output.json`, which records the output from the stated checker. For \(3\le n\le7\), the edge tests compare the Hamming-distance-two condition against pair-exposing linear programs over all even-parity vertices; the counts are \(6,24,80,240,672\). For \(3\le n\le7\), exact bounded integer degree-sequence enumeration tests the multigraph description. For \(4\le n\le8\), finite-field modular Jacobian calculations verify that nonzero rank-one determinantal matrices are smooth. For \(4\le n\le10\), the integer Smith forms of the \(2n\times n\) primitive-facet map exhibit unit invariant factors.

Linear-programming edge detection is a finite numerical check, not an exact certificate of all face adjacencies. The modular Jacobian runs are finite-field spot checks, not assertions for arbitrary fields or all matrix entries. Finite tests do not prove statements for unbounded \(n\). The infinite theorem instead rests on the semigroup, determinantal chart, singular-axis, and class-group arguments in `RESULT.md`. No independent audit or external validation has been performed.
