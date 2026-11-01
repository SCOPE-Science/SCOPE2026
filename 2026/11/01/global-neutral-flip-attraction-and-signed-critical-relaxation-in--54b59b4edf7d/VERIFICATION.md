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

# Reproducibility and mathematical limits

Run `python verification.py` in a Python environment with SymPy. The code tests independently derived truncated power series of the *exact* logarithmic-odds map, including fifth-order second-iterate coefficients. It checks the positivity argument's elementary curvature identity, exact rational values of the symmetric logarithmic constant, 20 parameterized two-cycle identities, 10 small-bifurcation amplitude comparisons and 15 high-iteration critical-rate comparisons (160000 iterations each).

The run completed successfully with the reported PASS banner. These checks test necessary algebra and representative finite trajectories. They do **not** substitute for the strict integral monotonicity proof, the one-dimensional no-two-cycle convergence theorem, the summation of asymptotic recurrences, or an independent mathematical audit.

For independent inspection, the proof is contained in `RESULT.md`; neither source texts nor external data files are required to execute the checker. The only nonstandard Python dependency is SymPy. The checker uses standard double-precision arithmetic for sample trajectories and exact symbolic arithmetic for formal coefficients.
