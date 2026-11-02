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

# Verification of the facet transition classification

Reproduce finite corroboration with `python3 verify.py` (Python standard library only). The script performs independent exact-Fraction vertex enumeration, de-duplicates coincident cube-section vertices, checks the three-class count, the closed chamber formulas, the number of fully saturated vertices, and maxima for n=4,...,11 over a fixed grid of 408 parameter/dimension pairs. Output: `VERIFY_OK exact_rational_grid_cases=408 dimensions=4..11; independent vertex enumeration, sign-count formula, closed binomial formula, maxima`.

The rigorous dimension-uniform steps are elementary: (i) all dual constraints form exactly the zero-sum box, (ii) two slack coordinates imply a feasible perturbation, (iii) one slack coordinate forces a unique vertex, (iv) fully saturated signs require an integer parity resonance, and (v) binomial differences are negative or zero as stated. The proof separately treats t=n-1 and greater, where a coordinate inequality becomes redundant. No finite sample is presented as an infinite proof. No independent audit is asserted.
