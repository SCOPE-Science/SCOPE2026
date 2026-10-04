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

The exact distributional step is checked analytically: for unequal positive scales \(a>b\), partial fractions give the density as a signed combination of two centered Laplace densities, so integrating above a positive threshold yields
\[
\Pr\{aX_1+bX_2>z\}=\frac{a^2e^{-z/a}-b^2e^{-z/b}}{2(a^2-b^2)}.
\]
The equal-scale limit agrees with the convolution tail \((u+2)e^{-u}/4\) for \(u\ge0\).

The sparse expansion was recomputed from the exact ratio-coordinate formula. Its first nonconstant algebraic coefficient is \(1-t/\sqrt2\). The exponentially small term \(r^2e^{-c/r}\) is flat at \(r=0\), so it cannot alter that sign away from \(t=\sqrt2\).

For the equal-weight endpoint, the squared-weight representation was differentiated directly. The cubic derivative entering the even Taylor expansion is proportional to
\[
4t^2-6t-3,
\]
whose only positive zero is \((3+\sqrt{21})/4\).

The endpoint-height ratio is \((1+t)e^{-(2-\sqrt2)t}\). Its logarithmic derivative changes sign only once, so after its initial equality at \(t=0\) there is at most one positive crossing. Sign checks at \(\sqrt2\) and \((3+\sqrt{21})/4\) place that crossing strictly between the two local-bifurcation thresholds. `verify.py` reproduces the numerical value \(1.687952825208936\ldots\) by bisection and checks the endpoint formulas and local perturbation signs.

The verifier samples only finite points as a stress test. Those samples are not used to infer the analytic local classifications, the uniqueness of the positive crossover, or the existence of the interior minimizer.
