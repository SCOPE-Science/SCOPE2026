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

Each unit observation projector has isotropic half-trace and doubled-angle anisotropy s_t ζ^(−t), where ζ=exp(iπ/N). Thus the information eigenvalues are (N±|P_s(ζ)|)/(2σ²). At fixed trace the lower eigenvalue and determinant are maximized at zero anisotropy, while the trace of the positive-isotropic-prior posterior covariance is minimized there. Direct telescoping gives (1−ζ)P_s(ζ)=s_0+s_(N−1)+2Σ_switch s_t ζ^t, using ζ^N=−1. At a zero this gives k+1 roots for even k and k for odd k; the distinct exponents modulo N prohibit antipodes after absorbing each sign. Lam–Leung's prime-polygon classification and asymmetric support lower bound imply no such nonempty relation for power-of-two N, and otherwise at least p terms with equality only for a rotated p-gon. Independently, this short-relation lemma follows by residue splitting at repeated prime factors (the corresponding cyclotomic extension has degree that prime). At square-free even order, splitting over the largest odd prime q makes its coefficient sums all equal by the q-th cyclotomic polynomial over the coprime-order subfield. If q>p, an empty class forces all the sums to vanish and one reduces the order; with only 2 and p left, each nonempty class contains roots with the same sign, so ≤p terms require one per class, all of the same sign. Order two alone permits no nonzero antipode-free relation. Consequently k≥p−1. Equality requires a p-gon containing s_0; modulo N its nonzero locations are M,2M,…,(p−1)M with M=N/p. These switches force alternating equal blocks, and the block factor Σ_j(−ζ^M)^j indeed vanishes. For N=2^a p^b this same alternating block polynomial is monic of degree φ(2N) and vanishes at ζ, hence equals Φ_(2N). Divisibility and the nonoverlap of its p shifted quotient blocks force and suffice for an arbitrary ±1 first block of length M, giving exactly 2^M schedules.

## originality

PASS

The fixed-trace information comparison, cyclotomic divisibility, and the minimal vanishing-sum ingredient are classical. The supported distinct content is the specific binary rotating-sensor problem's exact least-switch law and equality rigidity for arbitrary horizons with odd factors, together with its all-isotropic-schedule classification in the one-odd-prime family.

## value

PASS

The switch budget is a natural extra constraint on attaining the best information matrix. The theorem provides a sharp, all-horizon prime-factor rule and a rigidity result that identifies the only least-switch realizations. The separate exact family census shows that uniqueness at the switch optimum need not imply uniqueness of isotropy. This gives structural information not supplied by a numerical optimum or an optimization formulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
