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

`verify.py` performs exact finite replay independent of the symbolic counting proof. For each \(q\in\{2,3,4,5\}\), each \(1\le n\le4\), and every center weight \(1\le w\le n\), it:

1. enumerates all projective points using a canonical scalar normalization;
2. computes \(\delta([u],[v])\) directly by minimizing Hamming distance over every nonzero scalar;
3. independently evaluates the multinomial shell formula;
4. compares the complete shell dictionaries coefficient by coefficient;
5. checks that shell totals equal \((q^n-1)/(q-1)\), that the zero-distance shell has one point, and that the radius-one and distance-\(n\) formulas agree with their closed forms.

The \(q=4\) branch implements \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) explicitly, so the finite replay is not restricted to prime fields.

The replay output is:

`VERIFY_OK`

The exhaustive computation is a finite cross-check, not the proof of the all-parameter theorem. The general statement rests on the support-composition counting argument in `RESULT.md`. No claim is made about untested large instances beyond what follows from that proof.
