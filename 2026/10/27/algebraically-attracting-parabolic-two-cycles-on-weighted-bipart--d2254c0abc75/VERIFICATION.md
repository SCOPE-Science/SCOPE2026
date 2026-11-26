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

Using the signed edge incidence B with columns oriented from A to B, the real-lift force is B diag(w) sin(Bᵀθ). The mean is conserved; the class-constant difference map is d↦d+hΛ sin d. The two distinct points exchange since 2δ/sin δ is strictly increasing from 2 to infinity. The positive vector taking values d_A and d_B on the two classes is Perron for the signless Laplacian, similar to L, so the positive quotient spectrum is bounded by Λ. The two Jacobians are I−h cos(δ)L; squaring gives the claimed trichotomy using 0<2δ cot δ<2 on (0,π/2). At criticality the centered component maps are I+Q and I−Q through cubic order, with Q=(h/2)B diag(w)(Bᵀu)^2 (entrywise square). Their composition retains −DQ·Q=−∇W at cubic order because DQ is symmetric. One color's components are positive sums of squares, so Q=0 forces equality across every edge, hence u=0 in the mean-zero slice. Homogeneity gives the stated decrease of squared radius and two-sided positive bounds on each increment of its reciprocal; local invertibility excludes finite-time landing. This proves the rate near the chosen p_+ (near p_- the even subsequence instead limits to p_-). On the scalar circle Q is π ε²/2, yielding cubic coefficient −π²/2 and reciprocal-square increment tending to π². The analytic reconstruction covers every graph in scope; the frozen finite diagnostics were inspected, not used as an infinite proof or executed.

## originality

PASS

Credit substantial overlap for branch existence, spectral stability window and the scalar endpoint constant. The supported distinct contribution is the positive-definite quartic mechanism and all-direction local attraction and rate on the full quotient for the stated graph class. The strongest matched catalogue comparison explicitly leaves transverse nonlinear dynamics unproved. The verdict does not assert historical priority of the overlapping components.

## value

PASS

The sharp stability boundary is genuinely neutral at linear order in every quotient direction. A positive-definite quartic return giving attraction and sharp orbitwise rate without restricting initial perturbations to the two-color manifold settles a distinct qualitative and quantitative dynamical question. The scope is local and excludes non-biregular graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
