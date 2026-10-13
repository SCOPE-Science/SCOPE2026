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

The counterexample is analytic. For independent exponential components with rate \(\lambda\), direct integration gives the displayed closed form for \(J_\lambda(t)\), and differentiation gives
\[
J_\lambda'(t)=
\frac{\lambda e^{-\lambda t}}{(1-e^{-\lambda t})^3}
\int_0^t(1-e^{-\lambda x})^2dx>0.
\]
Thus the monotonicity premise is satisfied for every positive threshold.

The dilation \(Y_i=2X_i\) satisfies the stated dispersive-order premise because its dilation derivative is \(2\). The defining integral gives exactly \(\mathcal{CJ}^{\mathbf Y}_i(2,2)=2J_{\log2}(1)\) and \(\mathcal{CJ}^{\mathbf X}_i(2,2)=J_{\log2}(2)\). Their difference is
\[
\frac{57-80\log2}{36\log2}>0.
\]
To certify the strict sign without a floating-point premise, use \(e^{7/10}>1+7/10+(7/10)^2/2+(7/10)^3/6>2\), hence \(\log2<7/10<57/80\).

The bundled checker independently evaluates the exact closed forms at high precision and verifies the rational Taylor bound. It is a reproducibility aid only; finite-precision output is not used as an infinite or symbolic proof.

Limits: the verification establishes a counterexample to the stated dispersive-order implication and the general coordinate-dilation identity. It does not establish a corrected necessary-and-sufficient theorem or assess unrelated results in the source.
