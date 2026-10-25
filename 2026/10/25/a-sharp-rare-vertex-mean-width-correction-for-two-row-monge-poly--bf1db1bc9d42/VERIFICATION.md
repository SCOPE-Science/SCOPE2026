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

The main theorem is analytical. A vertex-support identity reduces Gaussian support over the two-row Monge polytope to maxima of normalized Gaussian prefixes, suffixes, and iid two-row column averages. Exponential tail bounds show that all averages of two or more row entries are negligible on the claimed scale. Removing two correlated columns costs a smaller order, and a one-dimensional Laplace calculation supplies the exact rare-vertex constant. Conversion to intrinsic mean width uses Gaussian polar decomposition. Finite experiments are supporting comparisons only.

`verify_monge_width.py` implements 300 independently optimized support-function linear programs over dimensions three through twelve. It additionally integrates the analytic single-boundary proxy integral for five values from one thousand through ten million, printing its rescaled values and the predicted limiting constant. Dependencies are `numpy` and `scipy` (`requirements.txt`). Run `python verify_monge_width.py`.

Observed message: `VERIFY_OK supports 300 LP comparisons` followed by numerical proxy ratios increasing from approximately 0.467762 to 0.566606 as the sample size parameter increases, against limiting single-boundary constant approximately 0.665668. This slow convergence is compatible with logarithmic second-order terms; the numerical values alone do not establish the limit or originality.
