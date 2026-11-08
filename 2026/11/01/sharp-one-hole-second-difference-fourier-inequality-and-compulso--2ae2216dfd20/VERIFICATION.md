---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Parseval converts |1−e^{it}|⁴ weighted L² of analytic coefficients to ∑|Δ²a|² and Toeplitz Gram entries 6,−4,+1. Removing a single internal coefficient at L+1 leaves H_L,H_R with exactly one +1 bridge, flipped to −1 by negating right block. Sign conjugation yields K_n=E H_n E = B_nᵀ B_n for B_n=(I+S)² rectangular; total nonnegative minors plus a strictly positive complement minor establishes H_n⁻¹ entrywise positive. Explicit quartic U_n=H_n⁻¹1 and cubic V_n=H_n⁻¹ e_n provide 1ᵀG1=binom(n+4,5)/6, boundary mass n(n+1)/12 and p_n=n(n+1)/[(n+2)(n+3)]. The one-entry Schur bridge yields C²=S_L+S_R+(p_R t_L²+p_L t_R²+2t_L t_R)/(1−p_Lp_R). Because the flipped M⁻¹ is strictly positive, phasewise Cauchy–Schwarz forces all flipped coefficients to share one phase and the original right block to be π out of phase; equality ray unique. Independent exact SymPy matrix computations recovered C²=2/5 for (1,1), 19/7 for (2,2), 643/34 for (3,4) and 6937/146 for (4,5), with positive inverse/optimizer. Analytic cofactor and Schur arguments, not finite checks, give all L,R≥1 and arbitrary complex coefficients.

## originality

PASS

Hindov–Nitzan–Olsen–Rydhe October 2026 study unrestricted sharp discrete Sobolev/left inverses of higher differences and discrete Landau extremizers. Their accessible abstract describes no pinned internal coefficient or compulsory between-block phase; the unrestricted sharp value at total length d is not enough to determine the one-hole Schur bridge or optimizer. Yamagishi–Nagai 2022 consider discrete bending/Dirichlet pointwise best constants, a different functional and constraint. Resultary query finds other Fourier phase/Toeplitz extrema, not one-hole second difference. Primary full text of highly relevant Hindov et al. inaccessible through OA and authorized institutional access (VPN disconnected); it could contain a more general Green framework and remains explicitly risk. No unsupported whole-document NOT_COVERING claim.

## value

PASS

A missing internal Fourier coefficient is a canonical sparse spectral constraint. It changes the sharp discrete Sobolev embedding constant and forces the exact opposite phases of both remaining coefficient blocks, with a closed formula for arbitrary block lengths, not just one small example. This is a mathematically motivated exact finite-dimensional family with a nontrivial positivity/Schur proof, useful as constrained coefficient/control benchmark independently of any downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
