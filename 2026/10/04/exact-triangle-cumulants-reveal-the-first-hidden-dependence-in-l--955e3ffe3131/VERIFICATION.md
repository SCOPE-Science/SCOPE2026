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

The theorem is verified analytically. For a \(3\times3\) correlation block, direct expansion gives
\[
\det(R)=(1-x^2)(1-y^2)-(z-xy)^2,
\]
so the conditional LKJ density of \(z\) is symmetric about \(xy\). This establishes \(\mathbb E[z\mid x,y]=xy\) for every positive LKJ shape parameter, including the integrable endpoint-singular regime below shape one.

The published LKJ pairwise-independence theorem and marginal variance then give
\[
\mathbb E[xyz]=\mathbb E[x^2y^2]=(n+2\eta-1)^{-2}.
\]
For a nontriangle triple of distinct edges, diagonal-sign conjugation at an odd-degree vertex reverses the product and preserves the law, proving expectation zero. The cubic trace identity follows because \(C-I_n\) has zero diagonal and therefore only ordered triples of distinct vertices contribute.

The asymptotic check uses only
\[
\frac{(n-1)(n-2)}{(n+2\eta_n-1)^2}\longrightarrow(1+2\theta)^{-2},
\]
and the first three Marchenko--Pastur raw moments. No computational certificate, simulation, or unproved limiting interchange is required. Numerical Gaussian-Gram experiments were used only as a non-evidentiary stress check.
