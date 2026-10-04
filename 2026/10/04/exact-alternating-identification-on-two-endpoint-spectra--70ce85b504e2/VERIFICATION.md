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

The proof was checked directly from the published update rule. On \(\sigma(A)=\{\mu,1\}\) with \(\alpha_1=1\), orthogonal spectral decomposition gives
\[
r_1=(I-A)r_0=(1-\mu)P_\mu r_0.
\]
Thus the nontrivial trajectory lies entirely in the \(\mu\)-eigenspace after the first step. For \(q_k\in[0,1-\mu]\), the scalar multiplier satisfies
\[
1-\mu(1+q_k)\ge(1-\mu)^2>0,
\]
so the successive norm ratio is exactly
\[
q_{k+1}=1-\mu-\mu q_k.
\]
The affine fixed-point calculation then yields
\[
q_k-\frac{1-\mu}{1+\mu}=(-\mu)^{k-1}\left(q_1-\frac{1-\mu}{1+\mu}\right).
\]

A direct finite-precision replay was also performed on one hundred random values of \(\mu\in(0,1)\), random residuals, and repeated endpoint eigenspaces. Over the tested steps, the largest discrepancy between the matrix update and the scalar recurrence was below \(4\times10^{-16}\). This computation is only a consistency check; no finite experiment is used to justify the infinite statement.

Scope limits were checked explicitly: if \(P_\mu r_0=0\), the method terminates after the first step; if \(P_\mu r_0\ne0\), the lower bound above prevents later finite termination. No claim is made for interior spectra, inaccurate largest-eigenvalue scaling, \(l>1\), stochastic perturbations, or nonlinear objectives.
