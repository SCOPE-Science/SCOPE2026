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

# Reproducibility and proof checks

- Read the normalization: every facet normal has Euclidean length one, so the clearance gradient has absolute value one on a uniquely nearest-facet region.
- Check density identity by coarea: the shell \(\{T=t,J=i\}\) has cross-sectional facet area \(A_i(t)\), and its probability density equals \(A_i(t)/\mathrm{Vol}(P)\).
- Check one-shell implication: common ratios imply positive area proportionality, Minkowski surface-area uniqueness gives \(P_t=w+sP\), and positive-depth inclusion gives \(0<s<1\); all original facet supports then yield a common tangent ball of radius \(t/(1-s)\).
- Check inradius maximality using the positive equilibrium \(\sum_i A_i(0)u_i=0\).
- Check sparse implication: the difference of conditional facet probability vectors lies in the kernel of the augmented normal matrix. If all untested columns are independent, that kernel intersection is trivial.
- Run `python CHECK.py` to reproduce six planar polygon checks and three spatial box checks. The expected last line is `PASS: all polygon and 3D-box shell checks`.
- The numerical checks do not establish a novel theorem, and no machine proof or outside scientific audit is claimed.
