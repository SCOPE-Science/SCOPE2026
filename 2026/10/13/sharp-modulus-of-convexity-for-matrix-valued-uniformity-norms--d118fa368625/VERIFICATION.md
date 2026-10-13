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

The analytic verification has two independent parts. First, for a constant matrix-valued function \(F_A\), repeated application of the defining multiplicative derivative gives \((AA^*)^{2^{k-1}}\). With normalized trace this is exactly the normalized Schatten \(2^k\)-norm. Second, the explicit diagonal pair with coordinates \(a=(1-(\varepsilon/2)^{2^k})^{1/2^k}\) and \(b=\varepsilon/2\) has unit norm, separation \(\varepsilon\), and midpoint norm \(a\). This proves the matching upper bound.

The lower bound is Theorem 4.1 plus Corollary 4.2 of arXiv:2606.16862v2. Combining the two directions yields equality. The bundled `artifacts/verify.py` checks the exponent recursion and several numerical instances of all three witness identities. Those finite checks are only corroborative and are not used to infer the all-parameter theorem.

The statement is limited to the ambient matrix-valued uniformity space. No exact-modulus claim is made for the Weyl-orbit quantum subspace.
