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
# Reproducible checks and their scope

Run `python verify_universal_pheat.py` using Python 3, NumPy, and SciPy. The program checks a weighted three-vertex path at exponent \(3\) using exact rational arithmetic; 78 weighted noncomplete graph/exponent directional witnesses; numerical positive-rate scaling diagnostics; and 132 complete-graph flow-pair/time samples integrated with tight numerical tolerances.

The exact rational test certifies a finite witness only. The finite sampled graphs and exponents do not establish the all-graph statement, and short-time integration does not prove a global semigroup bound. Global existence and the complete-graph bound follow analytically from monotonicity and vertex comparison. The induced-path construction proves the noncomplete converse and unbounded normalized instantaneous rates for every \(1<p<\infty\) other than \(p=2\). All critical proof steps are written out in `RESULT.md`.

No independent audit has been performed.
