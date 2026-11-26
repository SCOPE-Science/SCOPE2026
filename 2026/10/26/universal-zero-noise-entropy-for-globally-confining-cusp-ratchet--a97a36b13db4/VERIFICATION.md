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

At fixed D>0, elliptic diffusion on the compact circle with bounded drift and the irreducible two-state chain has a unique positive stationary law; orientation balance gives mass 1/2 each. For the piecewise distance r used in the proof the generator of cosh(ηr/D) has negative drift of order V/D beyond r=KD for small η. The derivative matches at the minimum and jumps down at the repeller, so the local-time correction cannot spoil the bound. This gives uniformly integrable rescaled moments. I checked the abbreviated boundary-layer passage without assuming that weak convergence alone passes a discontinuous drift. Stationary j_s'=γ(p_{−s}−p_s) gives total variation at most γ; the spatial mean of j_s is bounded uniformly by bounded drift, hence sup|j_s| is bounded. On any fixed rescaled interval the density u_{s,D}(y)=D p_s(Dy mod L) satisfies u'=b_s u−D j_s. Its mass is bounded, so there is a bounded starting value in a neighboring fixed interval; Grönwall gives a uniform local bound and then a uniform Lipschitz bound. Local uniform limits are continuous at zero, obey the stated frozen first-order equation on both open half-lines, and have mass 1/2 by localization. Their normalized law is q_s with mean 1/A_s−1/B_s. For the entropy convention, integration by parts using j_s' cancels the log-density term against the flip contribution; the integral of U' against the constant total current is zero by periodicity. A smooth periodic cutoff of the signed coordinate yields LJ exponentially small and E[σ b_σ]=2γ E[σψ]+exponentially small. Hence the limit is γv times the difference of the two conditional rescaled means, which simplifies to the stated sum with factor 2γv². At slopes 2 and 3 with f=0 and v=γ=1 this gives 11/12 exactly. The inspected checker covers three D values per unloaded example; the additional fourth value in RESULT.md was not independently reproduced and is not proof evidence.

## originality

PASS

The distinct result supported here is the shape-invariant local-slope coefficient and moment-convergent boundary-layer law on the entire strictly inward nonlinear cusp class. The exact linear solution, known confined zero-noise finiteness, and stationary entropy-flux identity are prior coverage, not this record's new contribution.

## value

PASS

Even non-solvable force profiles in the specified class give the same singular finite entropy coefficient if their local slopes agree. The localization and first-moment reduction explain how to get a finite entropy limit from a flux with prefactor 1/D, while the conditional asymmetry supplies observable stationary information beyond mere confinement. This fills a precise gap left by the explicit linear solution and its partial small-noise evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
