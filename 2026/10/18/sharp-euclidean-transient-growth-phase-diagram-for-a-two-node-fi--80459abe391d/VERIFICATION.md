---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independently assembled the consistent mass and stiffness blocks and formed H=−(A+Aᵀ)/2 using MHM=(KM+MK)/2. Both matrices M and K are positive definite by their element quadratic forms and the zero boundary data; physical dissipation follows from d(cᵀMc)/dt=−2cᵀKc. H has positive diagonals and determinant equal to the stated positive factor times Δ, so Δ=0 is included in contractivity. Differentiating the squared Euclidean norm gives necessity and sufficiency over all times. When det H<0, −H has one positive eigenvalue and a positive off-diagonal, so a maximizing unit eigenvector has strictly positive coordinates. The symbolic replay gave Δ(1,r)=−P(r) and the four exact endpoint signs (+,−,−,+). Descartes' two sign changes and the two distinct brackets prove that both positive roots are simple and exhaust the positive roots; P(1)<0 determines the interior sign. The limiting scaled H and the mass eigenvalues reproduce the claimed coefficient and conditioning bound. The radical-to-trace ratio decreases for 0<r≤1, giving the stated supremum via r→0, not an attained maximum. The bound by √κ₂(M) distinguishes divergence of the initial rate from any divergence of finite-time amplification. With one degree of freedom A is a negative scalar. The two exact positive witnesses were also verified.

## originality

PASS

The supported distinction is the exact mesh-dependent polynomial region in pure heat flow, its sharp cutoffs and the explicit divergent rate despite bounded mass conditioning. Mass-energy decay, the logarithmic norm criterion, and the possibility of a rightward coefficient numerical range for an FEM operator are not new.

## value

PASS

A concrete smallest-dimension example is useful because stability in the physical energy and good mass conditioning do not certify monotonic nodal Euclidean decay. The full two-parameter criterion and the simple grading family with failure at both ends give exact benchmarks, and the thin-element calculation distinguishes arbitrarily steep initial growth from bounded amplification. These features are not supplied by just quoting dissipativity or exhibiting an arbitrary stable matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
