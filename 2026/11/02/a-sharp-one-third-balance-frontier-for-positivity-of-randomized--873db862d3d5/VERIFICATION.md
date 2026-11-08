---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The frozen RESULT.md reduces the matrix M_x exactly to Π+r_x(z)(I−Π) with r_x(z)=[1+(2x−1)z+(x²−2x+1/2)z²]/(1+xz)². The diagonal entry test reduces to r_x(z)≥−m/(1−m) and the off-diagonals are positive. The calculated ∂_x r=z³(2x−1)/(1+xz)³≥0 and ∂_z r=[−1+(1−3x)z]/(1+xz)³<0 give the unique success cutoff x*(z,m), whose uniform interval measure yields the exact P branches, endpoint values, and one-third stiff frontier. Taylor expansion at z0 gives the square-root onset. Because −1<r_x(z)<1 for every x in the parameter interval and finite z, the product projector representation has multiplier bounded by q(z)^n for q(z)<1; it eventually lies strictly above the diagonal nonnegativity threshold even for nonstochastic individual factors. Independently derived symbolic derivatives and exact rational endpoint tests in independent_checks.py gave CASE1_OK. Tests only support sampled boundaries; infinite conclusion is the algebraic argument. No proof claims 3-state, stagewise, nonlinear or finite-precision positivity.

## originality

PASS

Best-of-knowledge: the original randomized SDIRK tableau, scalar amplification, A-stability and convergence analysis in Eisenmann–Jans–Kruse–Podhaisky 2026 are fully acknowledged; stochastic matrix positivity probability for imbalanced two-state generators is a different property, because its threshold r≥−m/(1−m), not r≥0. Resultary records on SSP-SDIRK2(2) and Crank–Nicolson concern different rational functions. Exact same primary preprint full text could not be obtained from arXiv/open author OA, and authorized Oxford reported vpn_disconnected, so an undiscovered direct corollary is explicitly a priority risk; this limitation alone does not entail scientific falsity or known coverage.

## value

PASS

The fixed two-state chain is the smallest nontrivial probability-preservation testbed and the distinction between stochastic one-step matrices and eventually strictly positive products has direct meaning for probabilistic numerical integration. The sharp balance m=1/3, exact full probability law, and non-Lipschitz square-root onset are not routine stability-radius paraphrases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
