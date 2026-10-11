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

The exact one-step coefficient ratios are
\[
\frac{\mu_{i,k-i}}{\mu_{i+1,k-i}}=\frac{\omega_k}{\omega_{k+1}}\sqrt{\frac{i+1}{k+1}},
\qquad
\frac{\mu_{i,k-i}}{\mu_{i,k+1-i}}=\frac{\omega_k}{\omega_{k+1}}\sqrt{\frac{k+1-i}{k+1}}.
\]
Hence \(T_k=(\omega_k/\omega_{k+1})(a_1+a_2)/\sqrt{k+1}\). The unitary Hadamard rotation sends \(a_1+a_2\) to \(\sqrt2\,a_u\) and preserves \(v\)-degree. For the channel with output \(u\)-degree \(s\), the \(n\)-step coefficient is
\[
\left|\frac{\omega_q}{\omega_{q+n}}\right|2^{n/2}\sqrt{\frac{q!(n+s)!}{(q+n)!s!}}.
\]
The channels are orthogonal, so these are the singular values. Their successive ratio is \(\sqrt{(n+s+1)/(s+1)}>1\), proving the extrema. The \(n=1\) maximum gives the exact boundedness criterion and norm.

The focal source arXiv:2609.34308v1 was checked at its radial Hilbert theorem, radial hypercyclic/mixing corollary and examples, and its further question on non-radial weights. The earlier same-graph paper arXiv:2312.13934 was checked for broader growth criteria. No finite experiment is used as proof.

No claim is made for arbitrary non-radial weights, a complete \(\mathcal F\)-transitivity classification, or perturbative stability.
