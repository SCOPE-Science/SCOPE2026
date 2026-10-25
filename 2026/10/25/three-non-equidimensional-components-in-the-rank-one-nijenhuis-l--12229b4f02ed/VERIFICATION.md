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

The explicit Lie bracket table, the full fifteen-pair torsion condition, all three linear kernel descriptions, the component argument, and the counting identity are given in `RESULT.md`. The executable `verify_n4.py` forms brackets of \(4\times4\) matrix units, solves the torsion equations over finite fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), and checks all \(63\times63\) nonzero functional/vector pairs over \(\mathbb F_2\). Executed command: `python3 verify_n4.py`. Output terminates with `N4_RANK_ONE_NIJENHUIS_OK` and reports totals \(641\), \(12758\), \(109227\), and \(589844\).

The all-field theorem depends on the symbolic case split proved in `RESULT.md`, not extrapolation from these tests. No independent mathematical audit has been performed; the reduced locus, rather than possible nilpotent scheme structure, is classified.
