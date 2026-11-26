---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Expanding Eq. (22) with y=e^(−κℓ) and s=sin(2μ) gives the exact normalized Q term 4Qκ(1+κ²)(y−y³)/s and the Q-independent coefficients F, −2(1+κ²)², B at y powers 0, 2, 4. Independently, F=(1+κ²)² sin(2μ−4 arctan κ)/s, so the only positive roots are t,u and their slopes are −4(1+t²)/s and +4(1+u²)/s. On a fixed small neighborhood of each positive root r the perturbation tends to zero in C¹ uniformly in Q. To sharpen the root estimate, bracket it at r±K e^(−rℓ) with fixed sufficiently large K; on that bracket y=e^(−rℓ)+O(ℓe^(−2rℓ)), uniformly. Taylor expansion yields the stated shifts +tQe^(−tℓ) and −uQe^(−uℓ). The exact ∂Q term is positive, so implicit differentiation fixes the signs of the energy slopes and the endpoints are Q=±2. Squaring and subtracting gives both leading constants 8r². For completeness, in each Bloch fiber the vertex boundary condition is equivalent to an inward-edge derivative equal to minus the Hermitian matrix of phase half-angle tangents times the endpoint vector. At the fixed interior phase no Cayley eigenphase is singular, and exactly two tangents are positive. The metric-graph quadratic form is nonnegative on the kernel of the corresponding two endpoint coordinates, so a fiber has at most two negative eigenvalues. The two continuous root images are disjoint for large ℓ, hence there are no further negative bands. For fixed nonzero Q the normalized Eq. (26) error is already order e^(−κℓ), not merely a failure of uniformity across Q; at Q=0 the leading term cancels. No endpoint-phase uniformity is inferred. The packaged floating-point checker was inspected, not executed; its single-phase finite checks are not the proof.

## originality

PASS

Credit the exact secular equation, centers, and qualitative shrinking to Exner–Tater. The supported distinct claim is the corrected leading quasimomentum term, the oppositely signed uniform dispersions, and the two explicit leading widths at fixed interior phase. The printed leading-order asymptotic neglects the term that produces these widths; the closest inspected literature and indexed records do not supply the splitting for this graph and regime. This is a best-of-knowledge decision, not an absolute novelty claim.

## value

PASS

The resolved splitting is a natural quantitative invariant of the two distinct localized vertex levels, not another presentation of their already-known centers. It determines which fiber extrema occur at Q=±2, gives two physically distinct tunnelling scales and their coefficients, and corrects an error that would otherwise suppress the leading band dispersion. This is a substantive refinement even though it starts from an exact known secular equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
