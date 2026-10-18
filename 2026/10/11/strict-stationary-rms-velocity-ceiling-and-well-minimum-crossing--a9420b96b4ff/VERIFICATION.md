---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

At frozen RESULT.md blob dd470992d297fd34a3b2dcc7e1686c2695a6dc95, generator stationarity for antiderivatives of test functions in x and y gives E[y|x]=0 and E[L|y]=δy, L=βx−αx³+f cosθ. Invariant θ rotation gives zero forcing mean and E cos²θ=1/2. Differentiating H=y²/2−βx²/2+αx⁴/4 gives δ E[y²]=f E[y cosθ] and hence E[y²]≤f²/(2δ²). Zero velocity is impossible under f>0 and rotating phase. Equality in Cauchy gives y=(f/δ)cosθ, so x=C+[f/(δω)]sinθ on each support orbit; the y equation then has a nonzero cubic coefficient −α[f/(δω)]³ in a proposed linear identity, contradiction. Similarly E[(dy/dt)²]>0, giving the strictly intermediate load correlation from orthogonal variance. E[x(x²−β/α)]=0 forces positive mass on both sides of the potential minimum ±sqrt(β/α) for any one-well invariant support. All compactly supported invariant measures, all positive α,β,δ,f,ω, and the two-crossings conclusion for each nonconstant one-well periodic orbit are covered. Symbolically recomputed dH/dt and the cubic obstruction; finite checks cannot establish invariant-measure statements.

## originality

PASS

PASS on bounded best-of-knowledge comparison for the jointly quantified conditional regressions, strict all-stationary RMS inequality with equality obstruction, exact load variance and well-crossing constraint. Classical Duffing chaos and power-balance papers do not on inspected material imply these full statements; older statistical work is partly uninspected.

## value

PASS

The forced double-well oscillator is canonical in nonlinear dynamics; any invariant measure (including chaotic and periodic ones) obeys a strict energy-throughput ceiling independent of the potential parameters, plus conditional load regression and a geometrically forced crossing of the unforced well minimum. The one-well crossing/strict rigidity is a motivated nontrivial structural constraint usable to test proposed invariant statistics, rather than treating the elementary energy balance as new. No existence, chaoticity, or optimized sharpness beyond strict universal bound claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
