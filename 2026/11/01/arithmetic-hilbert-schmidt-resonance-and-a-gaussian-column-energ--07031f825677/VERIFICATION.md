---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Row and column sums 1 and 1/t give Hardy boundedness by Schur. The log identity for 1-phi_t holds on the prescribed branch by analyticity and equality at zero, and gives the exact column factor z^k h_tau(z) sum_j A_j(z) B_j(z)^k. For q_j=1-t_j the linear and quadratic terms of log B_j(e^{ix}) are i(q_j/t_j)x and -q_j x^2/(2t_j^2); a Gaussian bound on the whole angular interval follows from the exact denominator t_j^2+2q_j(1-cos x). At x=u/sqrt(k) the weight tends to e^(pi tau) on the positive side and e^(-pi tau) on the negative side. Each diagonal term thus contributes |a_j(t_j^(-i tau)-1)|^2 cosh(pi tau)/(2 sqrt(pi) t_j sqrt(q_j)) to the sqrt(k)-scaled column square norm; the factor 1/2 comes from the normalized Hardy integral of the two half Gaussians. A cross term has a Gaussian-dominated L^1-convergent amplitude times a linear phase of frequency sqrt(k)(q_j/t_j-q_l/t_l), which diverges in modulus; one can replace the amplitude by its limit in L^1 before using Riemann–Lebesgue. This gives o(k^(-1/2)) with no positivity restriction on a_j. Summing multiplies the column coefficient by 2 at scale sqrt(K). If every resonance holds, each A_j vanishes linearly at 1, and the integral is bounded by a constant times the second moment of the Gaussian, O((k+1)^(-3/2)); otherwise the leading coefficient is positive and the column sum diverges. This also covers tau=0 and proves the commensurability assertion. The checker was read, not executed: its quadrature is a finite truncation of a rescaled boundary integral, and none of its shift-commutator diagnostics is a premise.

## originality

PASS

Pass for the combined finite-atomic column-energy law and exact arithmetic ideal characterization, not for the Hardy Hausdorff representation or for generic one- or two-term Hilbert–Schmidt membership criteria. The additive cutoff coefficient is the strongest supported distinction.

## value

PASS

The quantitative law explains exactly how an imaginary-power multiplier probes these distinct boundary maps: at the natural degree cutoff each atom contributes independently even for complex coefficients. The resulting arithmetic classification distinguishes genuine Hilbert–Schmidt cancellation from nonresonant square-root divergence. The specified cutoff is natural for Hardy polynomials and is not advertised as a basis-independent singular-value invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
