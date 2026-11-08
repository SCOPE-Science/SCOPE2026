---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Under the explicitly unweighted companion the Krylov space spans e0..e_(m-1); the (m+1)-by-m lower-bidiagonal residual matrix has rank m and null-left vector w=(1,1/s,(1+as)/s^2,...,(1+as)/s^m). Orthogonal projection yields lifted R_m^2=1/||w||^2 and r=w/||w||^2. First two residual equations and L0 inverse row (1,-a,0...) give signed physical 1-(1+as)x=(1-a/s)/||w||^2. No positive W_m can vanish. Rational matrix least squares independently checked m=1..7 and representative a,s; geometric series proves all regimes, while finite tests do not prove m->infinity.

## originality

PASS

Gao–Jiang 2026 furnish the right-preconditioned companion, general recovery formula and lower bounds for the lifted residual outside the unit disk, not a universal lower bound for the physical residual. The all-m affine scalar resonance E_m=|1-a/s|R_m^2 is not a direct statement of the accessible original abstract or checked related GMRES literature, though it is an exact specialization of basic least-squares algebra; unexplored full Gao–Jiang text may contain an implication. Original full text was unavailable on arXiv/mirrors and Oxford VPN disconnected.

## value

PASS

The scalar resonant witness distinguishes an algorithmic lifted residual floor from accuracy of the recovered physical solution even for s>1, while the full m-dependent formulas identify exponential/polynomial/nonzero-floor transitions. As a tightly motivated counterexample to an extrapolation of residual bounds it has standalone numerical-analysis significance, though it does not address generic matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
