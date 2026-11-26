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

The uniform density has M(1)=0 and is fixed by doubling; the p-dependent neighborhood makes both inverse branches expanding. Taylor expansion of their Jacobians has a C¹ error O(M²); composing the perturbation with the displaced inverse branches costs O(|M|‖η‖C²) in C¹. This gives the claimed strong-to-weaker expansion and the bounded operator P−(Pg_p)'M, not differentiability of the C¹ self-map. On the doubled cosine chain the observable picks out e₀, and the exact normalization gives (Pg_p)'=Σ c_j e_{j−1}. Thus the shift with replaced first column has characteristic polynomial p. The quotient by this invariant finite block has powers bounded by those of P, which are O(2^(−n)) on mean-zero C¹ by differentiation and the mean-zero oscillation estimate. The exterior resolvent and all exterior generalized eigenspaces therefore reduce to the companion block. Unforced arbitrarily high dyadic modes retained for n steps attain norm ratios bounded below by a constant times 2^(−n); this proves the floor even when all roots are small or zero. Independently computed all nine strong-response matrix pairings for a triple root at 3/4 (python3 /workspace/audit-work/independent_checks.py 3). Repeated/complex modes and exterior multiplicities are covered analytically; checks are corroborative only. The frozen checker was inspected, not run.

## originality

PASS

Pass for arbitrary real-polynomial exterior spectral assignment in this fixed microscopic model, not for discovering the self-consistent differential, companion-matrix algebra, or single-harmonic resonance. The strongest indexed predecessor was read in the mirror: its one harmonic supplies a binomial block and exact radius, whereas this proof assembles a shared multiharmonic shift chain and identifies the entire outside spectral multiset.

## value

PASS

Keeping the microscopic equilibrium dynamics and Lyapunov exponent fixed while choosing the macroscopic modes, including oscillations, repeated unstable roots or fast decay, is a precise separation useful for interpreting collective stability. The radius floor and exclusion of spurious outer modes make this a usable test family rather than a finite matrix illustration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
