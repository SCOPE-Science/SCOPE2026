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

The all-parameter proof is symbolic. Its critical steps are: (i) nondegeneracy of the finite-field trace pairing makes the column-coordinate map injective; (ii) the appended constant coordinate equals \(1\), so distinct columns cannot be proportional; and (iii) when \(y=-\alpha^{-1}\), the defining equation is independent of \(x\), producing a full affine line and hence a three-column dependence with coefficients \(1,-2,1\).

`verify.py` independently checks the primary source's displayed ternary \(m=2\) generator matrix. It verifies rank \(5\), absence of zero or proportional columns, existence of dependent triples, and computes the first three dual MacWilliams coefficients from the displayed primal weight enumerator. The expected terminal line is `VERIFY_OK`.

The computation is a finite stress test of the displayed example, not the proof of the all-parameter statement. The general claim rests on the symbolic column argument above.
