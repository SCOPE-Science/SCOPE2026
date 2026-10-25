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

# Verification

Execute `python verify.py` with the dependencies in `requirements.txt`. The program checks the exact coefficient recursion for all four orientation states and all mixed incoming boundary conditions, verifies the first three averaged coefficients by symbolic integration, and checks the threshold identity. Independent matrix-exponential boundary-value calculations match the second-order expansion at six distinct speed ratios. Three independent seeded event-driven simulations agree with the four-state boundary-value solution within their stated Monte Carlo tolerances. All executable checks passed in the present calculation.

The proof requires the exact assumptions \(\ell>0\), \(v_1>v_2>0\), and equal independent Poisson reversal rates. Symbolic finite-order expansions are not an infinite-order proof: analyticity follows from the noncharacteristic finite-dimensional boundary map at zero rate. Numerical tests do not prove the strong-reversal limit, which instead follows from the compensated-jump martingale maximal bound. The work does not establish uniqueness of the positive optimum or ballistic global optimality below the threshold. Independent audit has not been performed.
