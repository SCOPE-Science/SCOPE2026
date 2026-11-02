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

# Verification of central-section law

Analytical checks: the strip variable has cumulative distribution \(F_q(a)=a/\sqrt{q^2+a^2}\), the five projected vertex magnitudes have the strict order proved in `RESULT.md`, and \(G_q'(t)=F_q(\cos t)\) for \(t\in[0,\pi/2]\). The six probabilities telescope to one and each is strictly positive for \(q>0\).

Computational reproducibility: run `python3 pentagonal_prism_checker.py` using Python's standard library. On the reviewed package copy, for \(q=0.23\), \(q=\sin(\pi/5)\), and \(q=1.7\), every direction was classified by independently checking sign changes across the fifteen actual three-dimensional edges. Each case used 180,000 directions. At each aspect ratio, midpoint quadrature separately integrated 20,000 azimuth slices using the six threshold intervals. Largest absolute quadrature discrepancy was \(1.13\times10^{-10}\) across all cases; largest Monte Carlo discrepancy was less than \(0.00145\). All assertions passed.

Limitations: numerical sampling is not an exhaustive proof for continuum-valued directions. The proof covers that continuum using exact geometry and elementary integration. The historical-priority comparison with some old full texts is unresolved. Independent audit status: not performed.
