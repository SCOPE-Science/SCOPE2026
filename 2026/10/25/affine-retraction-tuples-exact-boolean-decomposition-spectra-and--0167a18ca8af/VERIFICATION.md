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

The standalone Python 3 script `VERIFY.py` has no external dependencies. Run `python3 VERIFY.py` from the directory containing it.

It constructs all affine maps on the tested finite vector spaces as explicit functions, checks functional idempotence by composition, checks commutation of ordered pairs and triples by explicit composition, and independently evaluates the orbit-stabilizer sum from general-linear-group orders and integer weak compositions. It implements \(\mathbb F_4\) with the irreducible polynomial \(t^2+t+1\); this tests a non-prime finite field.

Observed complete pair counts: \(5233\) for \(\mathbb F_2^3\), \(460\) for \(\mathbb F_3^2\), and \(1249\) for \(\mathbb F_4^2\). The complete triple count for \(\mathbb F_2^2\) is \(617\). All eleven tested parameter triples match exact orbit-stabilizer formulas. The script ends with the literal output `VERIFY_OK: affine idempotent tuple formula; all 11 cases`.

The general proof uses common-fixed-point reduction, simultaneous spectral idempotents, and a dominated-convergence argument for a finite-dimensional Gaussian lattice series. None of the finite computations is used as a substitute for the infinite limiting argument. Conjugacy-orbit classification and all-arity formulas are proved algebraically, not just sampled.
