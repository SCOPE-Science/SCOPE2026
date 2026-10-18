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

# Verification procedures and limits

The theorem is supported by the exact conjugacy \(W=\gamma DSD^{-1}\) for a bounded, invertible, periodic diagonal \(D\), the explicit orbit-norm formula for every vector, and the weak convergence \(S^n x\rightharpoonup0\). These steps justify the period-product trichotomy and the syndetic-return criterion at equality, including every boundary \(\delta\ge0\) and every \(q\ge1\).

The midpoint calculations for the two-period example are exact: the two squared radius tests equal \((107+2\sqrt{14})/100\) and \((67+4\sqrt{14})/80\), both strictly greater than one. The example vectors meet one separate ellipse equality each. The operator is a bounded diagonal conjugate of the unilateral shift, and its powers have norm at most two.

Execute `python3 verify.py` from the folder containing this document to replay the exact rational certificate checks and 240 phase-orbit diagnostic comparisons (all using Python's standard library). These checks do not test infinitely supported inputs exhaustively, and numerical output does not replace the analytic proof.

No independent validation or external certification has been performed. Possible prior equivalent formulations in the weighted-shift literature remain a publication-priority risk.
