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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. No external dependencies are needed. The script constructs the fields \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11}\) by prime residues and \(\mathbb F_9\) by the quadratic irreducible relation \(u^2=-1\) over \(\mathbb F_3\). It independently computes determinants by elimination using the exact field tables, with independent predicted counts from modular orbits and square classes.

Complete enumerated orders are \(1\)–\(11\) for \(q=3\), \(1\)–\(10\) for \(q=5\), \(1\)–\(8\) for \(q=7\), \(1\)–\(7\) for \(q=11\), and \(1\)–\(8\) for \(q=9\). There are 44 cases, 19,740 actual matrices, 5,456 singular matrices and eight cases in which the field characteristic divides the order. Every determinant fiber and total count matched.

Observed exact replay:

`VERIFY_OK fields=5 cases=44 matrices=19740 zero_determinants=5456 characteristic_divides_order_cases=8`

The tests cover a finite grid only. Correctness of the universal statement rests on the invariant-algebra decomposition, norm surjectivity, correct multiplicities, and lift-count proof in `RESULT.md`. No external or independent mathematical validation was performed.
