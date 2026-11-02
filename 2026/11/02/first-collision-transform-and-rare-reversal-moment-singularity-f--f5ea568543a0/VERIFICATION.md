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

# Reproducible mathematical verification

The accompanying `verification.py` checks the generator residuals of the exact Laplace functions for all three velocity states, the absorbing first-contact condition, the antipodal-folding condition, and a symbolic derivative yielding the exact mean. It checks the first nine moment coefficients (orders \(2\) to \(10\)) against the rare-reversal expansion. It then runs event-driven, orientation-flip simulations (38,000 trajectories for each of three positive-rate parameter cases) independently of the backward-equation evaluator, comparing six Laplace values and three means within seven empirical standard errors. Six additional high-precision tests compare the natural scaled-Laplace expansion at positive reversal rates. **All 30 checks passed.**

Run `python verification.py`, requiring only standard Python plus the publicly available packages `sympy` and `mpmath`.

The proof itself is in `RESULT.md`: generator elimination and boundary conditions establish the exact transform; fixed-rate Taylor differentiation gives the mean; an independent first-flip argument establishes typical ballistic convergence and a conditional exponential law; and a locally uniform holomorphic expansion justifies differentiation for every fixed integer order. Finite simulations are diagnostics rather than proofs of infinitely many moment identities, and a failed run would not establish a theorem's negation.

The model excludes asymmetric flip rates, finite tumble duration, post-contact jamming residence, arbitrary initial velocity states, and thermodynamic limiting regimes. No independent scientific audit has been performed.
