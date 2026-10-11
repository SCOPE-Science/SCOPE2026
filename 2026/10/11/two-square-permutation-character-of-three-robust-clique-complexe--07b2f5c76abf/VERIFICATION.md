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

Execute `python3 verify_grid_reflections.py` using Python 3 and its standard library. The program independently enumerates all accepted faces from the no-independent-triple rule, checks the matching criterion on every four-face in its six homology test cases, computes exact mod-two boundary ranks, evaluates fifteen signed augmented simplicial traces, and compares forty-eight nonidentity orbit-trace instances against the uniform formulas.

Completed replay reported:

```text
HOMOLOGY_OK 2 2 [0, 0, 0, 0]
HOMOLOGY_OK 2 3 [0, 0, 0, 1]
HOMOLOGY_OK 2 4 [0, 0, 0, 3]
HOMOLOGY_OK 3 3 [0, 0, 0, 6]
HOMOLOGY_OK 3 4 [0, 0, 0, 15]
HOMOLOGY_OK 4 4 [0, 0, 0, 36]
VERIFY_OK reflection_characters 48 tetrahedra 387 direct_signed_trace_cases 15 independent_mod2_homology_cases 6
```

The computations cover only the displayed finite parameter ranges and verify mod-two ranks, not integral or rational module decompositions directly. The infinite assertion follows from the analytic character proof and the independently established nonequivariant homotopy theorem in arXiv:2602.11365. An abstract rational character isomorphism does not supply an integral isomorphism or canonical basis.
