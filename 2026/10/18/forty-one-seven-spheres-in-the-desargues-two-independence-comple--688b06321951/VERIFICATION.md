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

# Reproducible exact checks

Execute `python3 verify_desargues_ind2.py` and `python3 verify_mod2.py` using Python 3. The programs have no network access or third-party dependencies. Their expected stdout is included separately. `verify_desargues_ind2.py` independently enumerates all \(2^{20}-1\) possible nonempty subsets, checks the exact local degree condition, compares with inductive face generation, forms the entire sequential matching, enumerates all nonempty face-poset covers and performs a full acyclicity topological sort. Recorded values: \(62{,}048\) faces, \(31{,}003\) matched pairs, \(42\) critical cells (one zero-cell and forty-one seven-cells), and \(400{,}760\) directed covers; the topological sort visits every face.

`verify_mod2.py` independently enumerates all faces and computes the entire collection of simplicial boundary ranks over \(\mathbf F_2\): for dimensions one through eleven they are \(19,171,909,3076,6708,9202,7398,2951,509,55,5\). The only nonzero reduced mod-two Betti number is forty-one in dimension seven. This is a finite consistency check; the integral homotopy theorem follows from the acyclic matching, not from mod-two ranks. The programs verify this finite graph, not an unbounded graph family. Independent external validation has not been performed.
