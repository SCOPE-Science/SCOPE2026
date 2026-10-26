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

# Verification and reproducibility

The proof in RESULT.md is the basis for the universal assertions. The attached `verification.py` is a standard-library Python 3 program that supplements the proof with reproducible floating-point diagnostics. Run `python3 verification.py` with no arguments. Its deterministic seed is `20261023`.

On the actual embedded program, 1,500 parameter configurations were sampled across the below-local-threshold, between-thresholds and above-global-threshold regimes. At each, 401 feasible allocations were checked against the theorem's endpoint/center candidates, for 601,500 comparisons. Off-center minima were reconstructed from the hyperbolic stationarity equation and checked by first derivatives. Additional checks covered all three exact quadratic global optima, the two off-center minima and their barrier, onset scaling for seven Hill exponents and three small perturbations, and 2,093 strictly increasing hyperbolic-budget comparisons.

All diagnostics passed. The quadratic example was checked against exact radical formulas. The tests are finite and use floating-point arithmetic; they neither exhaust all real parameters nor certify the analytic inequalities. Analytical proofs of the count, monotonicity, equality boundaries, and asymptotic statement are in RESULT.md. No external independent audit has been performed.
