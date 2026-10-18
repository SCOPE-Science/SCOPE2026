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

# Reproducibility and verification

The statement is a theorem about the minimum operator norm of arbitrary real linear projections from the weighted wheel edge space onto the wheel circulation subspace. For any integer rim count \(m\ge6\), on \(1/2\le t\le(1+\sqrt{17})/4\), the value is \(F(t)=(1+2t)^2/(1+2t+2t^2)\). The same rational expression is strictly smaller than the true optimum on \( (1+\sqrt{17})/4<t<3/2\). The analytic proof in RESULT.md includes the full cyclic-kernel reduction, exact input-column calculations and five-coordinate dual norm certificate.

`python check_wheel_exact.py` completed with the output `EXACT_OK 520 rational weighted-wheel cases; 30 smaller-wheel comparison cases`. It checks the explicit kernel, upper bound and sharp dual inequality in exact rational arithmetic, plus explicit smaller-wheel projections. These checks sample finite parameter sets and do not establish the all-real-parameter theorem on their own.

`python check_wheel_unrestricted_lp.py` completed with `UNRESTRICTED_LP_OK 20 full-projection optimizations`, using NumPy and SciPy. Each LP imposes the complete linear projection identity and optimizes the full operator matrix with no dihedral symmetry restriction, checking the analytic optimum against numerical optimization in sample cases. The LP solver has finite precision and is corroboration only.

The sharpness argument after the radical threshold uses equality conditions in a convex-dual lower bound; it does not compute the continued optimum for those parameters. The separate smaller-wheel trial projections give strict upper bounds, not a closed formula for the smaller-wheel optima.

No independent audit or external validation has been performed. The primary mathematical references appear in RESULT.md.
