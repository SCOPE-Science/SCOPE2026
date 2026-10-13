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

Run `python3 verify.py` after extracting the associated complete package. Only Python 3 standard-library rational arithmetic is used. Four pressure checkpoints \(0\), \(1/50\), \(1/20\), and \(1/5\) are tested for alternating strict signs of the analytic incidence derivative \(Q\), positive prevalence \(I\), and the effective susceptibility exceeding \(4/5\). The sign computations involve enclosures of exponentials using a positive Taylor polynomial and an explicit rational geometric tail bound, not decimal evidence. The terminal marker is `VERIFY_OK: exact rational four-point sign certificate and increasing prevalence`.

# Proof linkage and scope

The exact finite sign certificate is joined to an explicit symbolic identity \(\dot C=IQ\). Because the pressure increases while \(I>0\), strict alternating signs at the four pressure values imply three distinct strict intervening extrema. The derived monotonicity \(H_x<0\), together with \(H(1/5)>4/5\), proves \(I_x>0\) throughout the relevant entire interval; no numerical integration is required. The certificate does not show exactly two peaks over the whole epidemic, does not establish stochastic peak probabilities, and does not constitute an independent audit. Scientific originality and possible coverage by further heterogeneous-epidemic theory remain subject to independent assessment.
