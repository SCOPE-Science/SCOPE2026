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
For the published complete-sample modified-Muth likelihood, write \(\eta=1/\theta\). The reciprocal-scale score is
\[
U(\eta)=\frac n\eta+\sum_i x_i\left(\frac{2e^{\eta x_i}}{e^{\eta x_i}-1}+1-e^{\eta x_i}\right).
\]
Its derivative is exactly
\[
U'(\eta)=-\frac n{\eta^2}-\sum_i x_i^2e^{\eta x_i}-2\sum_i\frac{x_i^2e^{\eta x_i}}{(e^{\eta x_i}-1)^2}<0.
\]
Hence the score is strictly decreasing.

As \(\eta\downarrow0\), the log-likelihood equals
\[
3n\log\eta+2\sum_i\log x_i-n\log2+o(1),
\]
so it tends to \(-\infty\) and the score tends to \(+\infty\). As \(\eta\to\infty\), the term \(-e^{\eta x_i}\) dominates each observation's linear terms, so the log-likelihood tends to \(-\infty\) and the score tends to \(-\infty\). There is therefore exactly one positive score root and exactly one global maximum.

For the original scale coordinate, \(e^{x_i/\theta}-1=x_i/\theta+O(\theta^{-2})\) gives
\[
\ell(\theta)=-3n\log\theta+2\sum_i\log x_i-n\log2+o(1),
\]
and the exact derivative expansion yields
\[
\ell''(\theta)=3n\theta^{-2}+o(\theta^{-2})>0
\]
for sufficiently large \(\theta\). Thus global concavity in the original scale is not part of the claim and is in fact false.

The proof is analytic. No finite search, plot, simulation, or numerical optimizer is used to infer the global statements. The result assumes all observations are strictly positive, matching the model's stated support.
