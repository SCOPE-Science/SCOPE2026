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

The proof in `RESULT.md` closes under two moments of the squared-radial CIR process. Substitution into \(\operatorname{Var}(Y)=\mathbb EY^2-(\mathbb EY)^2\) gives the completed-square identity exactly; the coefficient of the mean-squared-reset displacement is \(4\beta^2r/[(2\beta+r)^2(4\beta+r)]>0\), while the reset-law variance penalty is \(r/(4\beta+r)>0\). The strict inequalities and the requirement \(\mathbb ER^2>0\) establish the equality and boundary cases.

Run the accompanying code using `python3 verify.py` with NumPy installed. It samples the *stationary renewal law* by selecting the age since the last Poisson reset, then using the exact noncentral chi-square transition law of the CIR diffusion. The code compares mean and variance against the closed moment equations in six regimes and checks the algebraic penalty identities over additional parameter values. Sampling uncertainty is finite and is not a substitute for the analytic moment proof.

For the exact stationarity sampler, conditional on a reset squared location \(z\) and elapsed age \(t>0\), set \(q=e^{-2\beta t}\). Then \(Y_t\) equals \([D(1-q)/\beta]V\), where \(V\) has a noncentral chi-square distribution with degrees of freedom \((\alpha+D)/D\) and noncentrality \(\beta q z/[D(1-q)]\). The stationary age is exponential with rate \(r\).

The proof assumes the canonical nonnegative extension at an accessible origin. No external independent scientific verification is reported.
