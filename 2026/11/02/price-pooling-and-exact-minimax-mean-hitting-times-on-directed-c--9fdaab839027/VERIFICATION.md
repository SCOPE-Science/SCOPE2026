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

`verify.py` is the complete standalone check; run with `python3 verify.py`. All formulas are derived for every positive price and budget in `RESULT.md`; the finite tests here do not substitute for the proof.

The performed run passed **6,393 deterministic checks** covering root equations, budget saturation, primal-dual equality, exact radical examples and 12 independently generated competitor allocations for each of 372 price-and-budget cases. An optional SciPy SLSQP block achieved successful independent constrained minimization on **33 of 36** trials, with objective values agreeing to its tolerance. Three trials reported optimizer non-success flags; these were neither counted as successful optimizations nor interpreted as infeasibility. The code reports this distinction itself.

To reproduce the mathematical conclusion without numerical black boxes, evaluate the exact inequalities and equality cases in the proof, particularly the weights \(\lambda_i=(1-p_i/c)_+\) and the scalar Cauchy–Schwarz identity. The proof covers every integer \(n\ge3\), every positive price vector, every positive budget and all threshold ties. Verification is self-review only; independent mathematical audit remains unperformed.
