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

The universal proof uses binomial translation parity, the monic gradient cubic, two- and three-value multiplicity reduction, and a Hessian-rank calculation. The source file `verify.py` runs with Python 3 standard library only. It performs exact computations in \(\mathbb F_4\), enumerating all value-multiplicity patterns for \(n=11,19\), verifying the claimed singularity patterns, enumerating partitions, checking transverse Hessian ranks, and computing plane intersections for \(n=11\). Expected output ends with `VERIFY_OK`.

Finite-field enumeration does not certify equality of algebraic varieties over every algebraically closed field; that conclusion follows from the general symbolic proof. In particular, the package does not establish global radicality of the Jacobian ideal or the local structure at the common diagonal point. The generic Hessian calculation only determines the transverse quadratic part at generic points of the planes.
