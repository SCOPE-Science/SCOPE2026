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

# Verification of the exact biomass-only theorem

Run the standalone Python 3 program `verify_klausmeier.py` with SymPy available:

```text
python verify_klausmeier.py
VERIFY_OK input_output=1 derivative_identity=1 no_constant_B_transients=1 two_jet_nonidentifiability=1 regular_three_jet_points=3 singular_nonstationary=1 positive_equilibrium_family=1
```

The executable independently derives \(\dot u,\ddot u,u^{(3)}\) by polynomial Lie differentiation. It checks the input–output equation and derivative identity symbolically, the cubic obstruction under a hypothetical constant \(B\), the explicit one-parameter second-jet ambiguity, and the formula for the third-derivative change. Three nonsingular rational initial states recover both parameters exactly. The singular witness at \((a,m,u,w)=(6,1,2,1)\) verifies \(\dot u=2\), \(\dot B=0\) and \(\ddot B=20\). Exact symbolic assertions, not floating-point tolerances, are used.

The unrestricted quantifiers are justified in the mathematical proof: nonconstancy of a real polynomial on any interval, ODE solution uniqueness, and the isolated-zero property of analytic functions. The checker does not exhaust infinitely many trajectories. No independent or external certification has been performed. No noisy-data inverse estimate is claimed.
