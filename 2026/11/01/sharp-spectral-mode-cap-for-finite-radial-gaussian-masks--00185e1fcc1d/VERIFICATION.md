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
The proof is self-contained and does not rely on the finite checks to infer the all-\(K\) assertion. The point requiring the most care is the sharpness induction: old endpoint powers are bounded by \(O(B^{M+1})\) while the far-ring endpoint differences have nonzero \(1/M\) asymptotic coefficients relative to \(e^{-M}M^M\) or \(e^{-M}M^{M+1}\). This justifies retaining all previous peaks and adding the new one. The exponential-polynomial zero bound follows by a fully stated induction using Rolle's theorem.

Execute `python verify_modes.py` using Python 3.11 or later. The script needs only the standard library. It computes, at 90-decimal precision, all natural-degree adjacent-difference signs up through 100 levels beyond each example's largest ring and checks the sharp \(2K-1\) variation count and the selected peaks for \(K=1,2,3,4\). It additionally checks 32 numerical comparisons of the Poisson finite-sum eigenvalue differences with the boundary exponential-polynomial formula, to tolerance \(10^{-70}\). These are reproducibility illustrations, not substitutes for the all-\(K\) argument. No independent mathematical audit has been performed.
