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
# Reproducibility and limits

The standalone `verify_lp_chords.py` executes deterministic Sobol integration with \(2^{19}\) planar affine-line parameter pairs for each test and computes **actual** Euclidean intersections with \(B_p^2\) by Newton iteration with checked boundary residuals. At fixed \(\varepsilon=10^{-8}\), the normalized asymptotic ratios for \(p=1.25,1.5,1.75\) are approximately \(1.0000314,1.0013043,1.0391284\). The checker verifies the local determinant \(2^{-q}\) in transverse dimensions \(q=1,\ldots,5\), two Dirichlet moment predictions and the distinct Euclidean-ball endpoint formula. The slower convergence as \(p\) increases toward two follows the relative correction order \(\varepsilon^{(2-p)/p}\); no uniform-in-\(p\) error control is asserted.

The infinite-dimensional-range assertions over all integers \(d\ge2\) and real \(1<p<2\) follow only from the analytic argument in `RESULT.md`. Finite experiments are supporting reproducibility checks, not a substitute for that proof or an independently performed audit. The priority question remains open for inaccessible historical papers.
