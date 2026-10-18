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
Run the included `verify.py` with Python 3 and no third-party packages. It compares two separately implemented finite procedures: literal enumeration of words and pair observations, and a closed run-composition enumeration of each feasible pair-spectrum fiber. Every binary word at lengths \(2\) through \(17\) is included, and each class cardinality and collision second moment is compared exactly; aggregate integer mass is verified at \(25,50,100,200,400,800\). The observed scaled collision probabilities approach \(3/(4\pi)\), but finite tests cannot certify a real-number asymptotic limit.

The mathematical verification of the unbounded-length assertion is the transfer-matrix Fourier identity, proof that exactly two spectral maxima exist on the torus, positive-definite Hessian calculation, and Gaussian integral. The potentially overlooked scientific issue is earlier derivation of the same constant from published exact ambiguity-class formulas; those formulas are acknowledged explicitly and no external independent validation is claimed.
