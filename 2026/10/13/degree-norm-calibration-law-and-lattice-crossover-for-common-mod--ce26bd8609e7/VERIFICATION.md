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

The universal statements are analytic. For independent fair binary vertex configurations \(X,Y\), direct computation of ideal and perturbed graph-state amplitudes gives
\[
F_G(\sigma)=\mathbb E_{X,Y}\exp\bigl[-\sigma^2(H_G(X)-H_G(Y))^2/2\bigr].
\]
The centered edge-indicator decomposition yields
\[
\operatorname{Var}(H_G(X)-H_G(Y))=(\sum_v\deg(v)^2+|E|)/8.
\]
Under the stated degree regularity, the normalized linear component converges to \(N(0,1/8)\) by Lindeberg and the quadratic remainder vanishes in mean square. The complete-graph proof uses exact binomial/Vandermonde identities and local central binomial tail control. The star proof uses its hub Bernoulli indicator and leaf count. Neither an enumeration nor a numerical fit is used to establish infinite-size assertions.

The bundled standard-library `artifacts/verify.py` reconstructs computational-basis amplitudes, independently compares small exact graph formulas, checks the variance identity, and numerically illustrates the critical, Jacobi-theta, fixed-noise, and star limits. Execute with Python 3; expected final output is `VERIFY_OK`.

The exact finite identities hold under the model's single Gaussian angle shared by all edge gates. The asymptotic crossover is conditional on the displayed scaling hypotheses. No independent audit or hardware certification is asserted.
