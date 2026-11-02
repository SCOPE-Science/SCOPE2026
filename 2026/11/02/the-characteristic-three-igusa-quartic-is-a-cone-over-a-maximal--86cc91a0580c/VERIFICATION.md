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

# Exact verification record

The standalone script `verify_igusa3.py` uses only integer arithmetic modulo three, an explicit quadratic model of \(\mathbb F_9\), and SymPy Gröbner bases for the four Jacobian ideals. It constructs the quartic polynomial from the six-coordinate equation without importing a precomputed singular locus. Run it with `python verify_igusa3.py` after installing the package in `requirements.txt`.

The checked Jacobian-quotient dimensions on the four affine charts are \(12,12,12,12\). All chart solutions are simple, giving exactly fifteen geometric nodes, each rational over \(\mathbb F_3\). The script checks the correspondence with the fifteen perfect matchings of six letters and the full-rank local Hessians. Exact enumeration returns \(\#Q(\mathbb F_3)=25\) and \(\#Q(\mathbb F_9)=145\), hence the K3 resolution counts \(70\) and \(280\). The saved execution output ends `VERIFY_OK`.

The universal-extension point-count and zeta identities are proved by cohomological Weil-bound equality, not established by finitely many computational samples. The calculation does not certify publication priority or independent validation.
