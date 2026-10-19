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
# Reproducible mathematical checks

Invoke `python verify_two_cluster.py` from the directory containing this file. Requires Python 3 with SymPy, mpmath and SciPy. The program performs exact symbolic simplifications of the convolution-derived ODE, the barycenter and the critical-ratio derivatives; checks the calculated shape constants and representative fold/escape levels; checks asymptotic square-root splitting numerically; and integrates the original point-mass characteristic equations independently of the reduced scalar equation.

The global level-crossing theorem rests on the explicitly proved monotonicity of \(F\) and \(R\) in RESULT.md, not on numerical root searches. ODE integrations are finitely many examples, not a proof of all parameter cases. All population proportions in the computation are within \((0,1)\), \(0\le b\le2\), and all initial separations are strictly positive. The supporting model has zero diffusion, and neither a continuum population nor positive diffusion is experimentally verified here.

Independent audit has not been performed. No independent external validation is claimed.
