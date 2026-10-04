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
# Verification

The local analytic proof is in `RESULT.md`. The finite replay checks only exact arithmetic consequences and representation weights.

`verify.py` checks the nontrivial pairwise weight gcds, coordinate-point membership, quotient tangent weights at \(Q_2\) and \(Q_3\), the order-four lift at \(P_x\), the combined order-\(21\) action at \(P_t\), the equivalence to \(\frac1{21}(1,8)\), the continued fraction \(21/8=[3,3,3]^-\), the local canonical index \(7\), the discrepancy vector \((-4/7,-5/7,-4/7)\), and the total exceptional-curve count \(9\).

The replay output stored in `verification_output.txt` must end in `VERIFY_OK`.

Unproved limits: the verifier does not certify analytic convergence of coordinate changes, deformation theory, or literature novelty. Those are handled respectively by the mathematical argument and the documented literature comparison.
