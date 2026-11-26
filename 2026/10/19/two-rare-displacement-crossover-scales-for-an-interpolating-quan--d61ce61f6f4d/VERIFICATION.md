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

The primary Theorem 1 fixes q=1-p and the variance scale r=|a|²/|b|². Conditioning on the variance gives the stated angular ratio, with amplitude A and phase B; subtracting cos(theta) from B gives the displayed q-order numerator over a denominator ≥(1-q)². Together with |log A|≤artanh(q) this gives the 8q(1+eta) envelope for all x, including x=0. For the uniform endpoint argument set y=1-cos(theta); the exact phase loss is B(1)-B(1-y)=b_q y/(1-2qy/(1+q)²), where b_q=(1-q)/(1+q)³ is bounded below on [0,1/4]. Uniformly on a small fixed y interval, replacement by b_q y incurs a relative integral error O(eta^-1): the amplitude error is O(y) and the exponential error is bounded by a constant times eta*y²*exp(-c*eta*y), integrated against y^-1/2. Outside this interval the positive phase gap is uniform and the endpoint weight remains integrable. The prefactor A(1)/sqrt(b_q)=1+q and the comparison at q=0 give the (1+q)exp(-q*eta/(1+q)) correction to I_0, hence the e^-z limit. For any fixed q<1 the same positive endpoint slope holds, giving the stated |x|^-1 density prefactor. Integrating and doubling uses the Gaussian tail integral with weight 1/x and yields the stated x^-2 survival prefactor, including the factor U_q. This is a statement about a fixed-parameter infinite-time law, not a finite-time rare-event or simultaneous time limit. The frozen quadrature checker was inspected but is not needed for the analytic result.

## originality

PASS

Best-of-knowledge pass for the explicit envelope, the uniform q-small endpoint estimate and the two rare-displacement profiles. The walk, mixing law and ordinary Gaussian limit are prior. The fixed-q sharp tails are standard endpoint-Laplace consequences of the known mixing law, not a standalone originality basis. The inspected prior symmetry/crossover results concern different laws, and the mixture theorem and general mixture sources inspected do not state or uniformly control the second displacement regime.

## value

PASS

Weak convergence to a Gaussian does not detect how the tails change. The natural eta scale first gives an I_0 enhancement, and an explicit uniform estimate then identifies precisely where that approximation itself breaks down and what replaces it. The density and survival prefactors anchor the estimates in the far tail. The numerical constant in the global bound and the fixed-q calculation alone are not the value basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
