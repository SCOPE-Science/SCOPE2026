---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Read actual Git RESULT.md blob fc0c9cf0c83b786855bea7878220839a2a5c59fd and exact rational verify.py. For each ρij≥0, bivariate Gaussian conditional monotonicity gives Cov(T_i(X_i),T_j(X_j))≥0. For ρij<0, Hermite orthogonality and Cauchy–Schwarz yield Cov≥ρij s_i s_j for centered square-integrable increasing transforms. Negative edges are vertex-disjoint, so disjoint 2×2 quadratic blocks have smallest eigenvalue 1+ρij≥1+ρ*. Choosing linear increasing transforms on the most negative pair (other coordinates zero, permitted in Sei T_cw*) attains β=1+ρ*. Sending other positive weights to zero proves α=1+ρ*; if no negative edges both infima equal 1. Explicit singular rank-two correlation constructed from U,V has ρ*=-sinθ, β=α=1−sinθ>0 for 0<θ<π/2. Finite verify.py cases are algebraic checks, not the proof.

## originality

PASS

Best-of-knowledge PASS: Sei’s primary full text formulates strict Gaussian copositivity in the singular case as Conjecture 4 and a coefficient-equality question. Matching negative edges yield the full exact β=α=1+ρ*, including explicit singular positive examples; the proof is not just a positive-definite spectral bound.

## value

PASS

Sharp β=α for a structural class containing genuinely singular Gaussian measures resolves a motivated special case of Sei’s open Gaussian copositivity/equality questions exactly where the older minimum-eigenvalue bound is zero. It gives a reusable precise coefficient from only the signed-correlation graph and the worst negative pair, without implying the unrestricted conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
