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

# Verification of the graph logistic recovery theorem

The proof in `RESULT.md` is analytical and applies to all finite connected undirected weighted graphs with positive rates and identical quadratic self-limitation. The principal nonstandard ingredients are the equilibrium Jacobian's exact negative quadratic form, the Rayleigh/RMS inequality with its complete equality case, and the strong-dispersal spectral limit. Those are explicitly derived, with their positivity and connectedness hypotheses, in the proof.

Execute `python verify.py` using Python 3 with NumPy and SciPy. The standalone file checks 6,875 assertions including exact rational equalities over binary-rate complete-graph populations, an exact four-vertex weighted-graph eigenvector/cross-class equality instance, spectral inequalities for numerous positive weighted graphs and coupling values, and a numerical three-distinct-rate gap. It must print `PASS: 6875 independent rational and numerical assertions`.

The exact example has \(r=(1,1,4)\), complete mean-field \(L=I-\mathbf{1}\mathbf{1}^{\mathsf T}/3\), \(d=5/2\), and \(q=\sqrt6\). The exact equilibrium condition \(r_i^2-q^2=2d(Lr)_i\) implies \(x_*=(r+q\mathbf{1})/2\); its Jacobian is exactly \(-qI-dL\). Thus the largest eigenvalue is \(-q\), without trusting a nonlinear solver.

Tests of bounded numbers of graphs, floating-point optimization, and exact arithmetic over finite parameter grids are only corroboration. They are neither a proof over continuous parameter ranges nor independent scientific validation. The proof supplies those infinite conclusions. The claim does not include stochastic resilience or global, state-independent transient rates.
