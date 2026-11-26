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

The two-state semigroup gives off-diagonals u and v and output probability z=u+(1-u-v)q. The entropy chain rule and conditional variance decomposition prove the objective and its strict concavity; positivity of the channel gives an interior optimizer. The gradient of the homogeneous conditional entropy in positive input weights is the vector of point-mass mismatch costs, and the point-mass maximum and KL data processing give the minimax equality. In the fixed gap regime, at q=c/L the term h'(q)−h'(z) is asymptotic to atL/c, the extra factor (1−k)h'(z) is O(t log L), and h(v)−h(u) contributes −ΔtL. Thus concavity brackets q* at a/(ΔL). On that bracket the entropy Taylor error is O(t²/q)=o(t). The term −Δq*log(1/t) cancels the constant +a, while −a log(1/q*) converts a log(1/t)−a log a to a(L−log L). At equal rates the symmetric optimizer is exactly 1/2. In the varying-rate family the compact-interior first-order objective and derivative limits give the stated g_η; its strictly negative second derivative and derivative sign brackets localize the finite-time maximizer away from either endpoint before evaluating the value. The large-η slope equation has leading term κ/Q_η, as claimed. The varying-rate expansion is pointwise at fixed κ>0, η≥0, not uniform near a moving boundary. Inspected but did not execute verification/minimax_verifier.py; its recorded 76 checks are finite diagnostics, not the proof.

## originality

PASS

The minimax identity and the leading law and qualitative concentration for fixed rates are established prior results. The supported refinement is the sharp two-state rate/cost expansion and, particularly, the explicit crossover between fixed imbalance and symmetry. There is a verified exact match to the fixed-unequal and balanced formulas in a separate archive entry dated Nov. 8; it has no varying-rate theorem. That entry's relationship to the frozen work is not established by date alone and no priority is inferred from it. The full stated result, including the crossover, is distinct from the inspected matches.

## value

PASS

The maximization is singular at fixed asymmetry and regular at symmetry. The optimizer scale and the negative log-log term quantify the singularity, and the varying-rate theorem identifies the transition window in which neither fixed-rate formula can be used uniformly. Resolving the order-t value and the optimizer in that window is useful beyond recomputing a binary-channel leading coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
