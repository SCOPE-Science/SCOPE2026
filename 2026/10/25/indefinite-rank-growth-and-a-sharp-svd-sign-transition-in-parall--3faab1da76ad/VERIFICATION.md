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

# Reproducibility and verification

The closed-form basis equations in the proof have solutions \(K(h)=L(h)=U_0+\gamma(1-e^{-h})e_3e_1^\top\) and \(B(h)=I_2\). Substitution into the 2023 method's augmentation gives \(H\). Its characteristic polynomial factors as \((\lambda-1)(\lambda^2-\lambda-p^2)\), proving the three eigenvalues. The strict parameter comparisons in the example can be checked with elementary exponential bounds, independently of floating-point output.

Install NumPy according to `requirements.txt` and run `python verify.py` from the directory containing these files. In the current environment the verifier printed `VERIFY_OK 132` and, for the witness, \(d\approx1.132209236674\), \(h\eta=7.5\), a positive exact minimum eigenvalue near \(0.322274939716\), and a negative truncated minimum eigenvalue near \(-1.132209236674\). The routine compares the exact spectrum with symmetric eigensolvers and checks the truncation choice on a finite set of parameters; the symbolic proof is what establishes the all-parameter inertia and the sharp cutoff.

The numerical checks do not constitute an independent scientific audit, prove novelty, or certify the method beyond the stated assumptions. Exact selection at the tied-singular-value boundary remains nonunique and is not tested as a unique-output claim.
