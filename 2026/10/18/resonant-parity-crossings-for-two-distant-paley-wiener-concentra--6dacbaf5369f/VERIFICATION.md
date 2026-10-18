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

# Verification of the distant-two-interval crossing theorem

The analytic steps were checked directly against the definitions in the main result: the block reflection transform, the first two terms in the separated sinc kernel, the exact parity matrix elements, and the reduced-resolvent second-order perturbation formula. The strict positivity condition \(4Wa<1\) is used to ensure that the single-interval leading eigenvalue is simple and its eigenfunction positive.

The standalone program `verification/check_sinc_gaps.py` was run with 160 Gauss–Legendre points. For \(a=1/4\) and \(W=1/2\) it returned \(\lambda\approx0.467791059210704\), \(A\approx0.638200786363659\), \(B\approx0.042331329261806\), \(\tau_*\approx0.042226461913684\), \(L\approx0.008599424114337\). Its numerically determined rescaled crossing positions at indices 20, 40, 80 and 120 were approximately 0.0422304172, 0.0422274507, 0.0422267091 and 0.0422265718. Numerical branch slopes, centroid corrections, and a far-off-resonance test converged to the stated expressions.

These finite quadrature checks are diagnostics, not proofs of exact infinite-dimensional crossings. The exact crossings and claimed uniform errors follow from the parity decomposition, parameter-differentiable operator expansion, isolated-eigenvalue perturbation, and intermediate-value argument in the proof.

The external literature comparison distinguishes global rearrangement/stability inequalities and large-bandwidth Fredholm determinant asymptotics from the fixed-bandwidth first-two-eigenvalue splitting derived here. An unindexed equivalent classical calculation remains a priority risk. Independent audit has not been performed.
