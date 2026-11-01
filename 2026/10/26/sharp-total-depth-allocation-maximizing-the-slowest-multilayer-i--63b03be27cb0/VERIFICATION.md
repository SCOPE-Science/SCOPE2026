---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For N>=2 prescribed positive reduced gravities, H>0 and positive depths summing to H, the rigid-lid generalized Jacobi eigenproblem is exactly K(h)eta=c^-2 D eta. With a_j=1/g_j and alternating v_j=(-1)^(j-1)a_j, v^T D v=S and sum |v_j-v_{j-1}|=2S. The Rayleigh bound and weighted Cauchy–Schwarz show lambda_max>=4S/H, with equality only for h_i=H(a_{i-1}+a_i)/(2S). At those depths K(h*)v=(4S/H)Dv; sign-conjugation produces a positive Perron vector of the tridiagonal matrix, making that eigenvalue the largest and proving attainability. N=2 scalar boundary holds; N=3 trace gives 1:2 slow/fast squared-speed ratio. Fresh generalized-eigenproblem calculations tested 325 randomized depth/gravity choices across N=2..14; universal proof is analytic.

## originality

PASS

The physical multilayer eigenproblem and modal orthogonality are classical, including Shimizu (2011) and de Melo Viríssimo–Milewski (2019), but the inspected fixed-geometry mode theory does not itself state a unique global optimizer for the smallest speed over every fixed-total-depth allocation and arbitrary positive buoyancy jumps. The all-N inverse-gravity adjacent-depth rule is the assessed theorem, not generic Cauchy–Schwarz or two-layer equal-depth folklore. Shimizu publisher full text was not fully accessible and Oxford authorized access returned VPN disconnected; do not infer complete exclusion.

## value

PASS

The output is an exact, unique allocation rule with physically interpretable inverse-buoyancy weights, valid for arbitrary numbers of layers and independent positive jumps. Maximizing the slowest mode under total-depth resource constraint is a natural optimal-stratification question; N=3 half-depth middle-layer law is a nontrivial concrete consequence, not a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
