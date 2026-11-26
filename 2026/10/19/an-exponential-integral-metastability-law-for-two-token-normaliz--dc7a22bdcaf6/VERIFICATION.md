---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The orthogonal half-sum and half-difference give equal normalization factors and an exact ratio multiplier 1−αp with 0<1−αp<1. The sum direction is preserved and the half-angle ratio tends to zero (p is bounded below at fixed β). To check the discrete approximation uniformly even near antipodality, use h=atanh c, the negative log of the half-angle ratio. One step is Δh=−log(1−αp)=αp(1+O(p)), with p≤p(c*) before crossing. Along the whole step |d log p/dh|=β(1−p)(1−c²)≤β, so the relative variation is O(βp(c*))=o(1), including on a final overshoot. Thus each full step contributes 1+o(1) to ∫dh/(αp) and the truncated step O(1). The number of steps diverges since the h displacement is bounded below in both regimes and the step upper bound decays exponentially. Changing back to c gives the stated clock integral. Its fixed lower endpoint gives the first limit by Laplace scaling. In the antipodal layer s=β(1+c), the exponential piece is dominated by e^(−s)/[s(1−c*)]; the nonexponential piece after normalization is O(e^(−2β) log β). The limit is E₁(z)/(2α), at fixed z>0, and π−arccos(c₀) is asymptotic to √(2z/β).

## originality

PASS

The discrete map is a known specialization and the clock integral with its E₁ limit is already directly derivable from the published continuous two-token equation, up to time normalization. The supported distinction is the sharp discrete update count, with its exact residual-weight constant and a relative comparison valid over exponentially many updates while the initial point approaches antipodality. Neither a known continuous-flow clock nor the closest discrete equilibrium result establishes that statement.

## value

PASS

The simplest nontrivial symmetric normalized attention model is a natural benchmark for the number of layers needed to leave an almost antipodal state. An exponential order alone misses both the weight-dependent prefactor and the change from a fixed-correlation endpoint to the E₁ angular layer. A quantitative comparison in actual update counts, justified despite the growing time horizon, is useful beyond the equilibrium description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
