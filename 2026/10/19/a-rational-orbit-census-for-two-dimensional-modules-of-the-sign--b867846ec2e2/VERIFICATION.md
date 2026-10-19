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

Run `python3 verify.py` with a standard Python 3 interpreter, without installing packages. The program enumerates all pairs of \(2\)-by-\(2\) matrices over the prime fields \(\mathbb F_3\) and \(\mathbb F_5\), checks the defining equation independently of the orbit proof, and exhausts each orbit under elementary unipotent, diagonal, and permutation generators of the full general linear group. For \(q=3\), it finds \(417\) solutions in \(37\) orbits; for \(q=5\), \(4705\) solutions in \(103\) orbits. The count of solutions alone is known from earlier work and is used only as a check. Successful execution ends with `VERIFY_OK`.

The general proof is algebraic: rational canonical forms, an explicit solution of the matrix anticommutator equation, centralizer actions, and the norm-one torus in the quadratic extension. Enumeration over two prime fields cannot certify the odd-prime-power result without that proof. Independent audit remains unperformed.
