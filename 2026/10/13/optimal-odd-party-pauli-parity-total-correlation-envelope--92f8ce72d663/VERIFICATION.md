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

The all-\(n\) proof is analytic. The critical identities are: the exact product threshold \(\Gamma_{\mathrm{prod}}(B_w)=\|w\|_\infty\); pairwise anticommutation of \(X^{\otimes n}\), \(Y^{\otimes n}\), and \(Z^{\otimes n}\) for odd \(n\); the resulting exact norm \(\|B_w\|=\|w\|_2\); and the Euclidean distance/support-function duality for the \(\ell_1\) unit ball.

The explicit state family \(\rho_a=2^{-n}(I+aX^{\otimes n}+aY^{\otimes n})\) is positive for \(0\le a\le1/\sqrt2\), since the perturbation has operator norm \(\sqrt2a\). For \(1/2<a\le1/\sqrt2\), its correlation vector is \((a,a,0)\), and the optimized lower bound equals \((2a-1)^2/4\), compared with \((2a-1)^2/6\) for the equal-weight witness.

The packaged checker verifies the Pauli algebra, weighted norms, soft-threshold projection values, and the explicit strict-improvement family for small odd sizes. These finite calculations are not used as proof of the theorem for arbitrary odd \(n\).

Limits: no even-party geometric envelope is claimed, and certificate extinction under depolarization is not identified with extinction of physical total correlation.
