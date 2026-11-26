---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Balance gives q=E p, with uniform empirical averaging, and the oppositely ordered pairwise products give (E p)(E p⁻²)≥E p⁻¹, strict for nonconstant spectra. The upper bound can be checked without the variational argument: after scaling to p∈[1,κ], fix the mean of X=1/p. Both x↦1/x and x↦x² are strictly convex. Their secants on [1/κ,1] bound their expectations by those of the same endpoint law with that mean, strictly if the spectrum has any interior mass. Both moments are positive and the denominator E X is fixed. With κ=t²>1 and smaller-p endpoint mass u, the endpoint objective is F=1+C u(1−u)/D, where D=1+(t²−1)u and C=(t²−1)²(t²+1)/t². The identity D−(t+1)²u(1−u)=[1−(t+1)u]² proves the sharp formula and unique optimizer u=1/(t+1). This u is realizable by an equal-weight finite multiset exactly if t is rational; otherwise approximate u by rational frequencies with both endpoints present to keep κ exact. At κ=1 the ratio is identically one. The stationary update identity holds with c=1/γ and α>0 for the unregularized frozen model; it establishes no stochastic trajectory claim.

## originality

PASS

Credit the sharp quantitative upper loss and its optimal finite-spectrum frequencies for the balanced trace surrogate. The lower ordering, the notion of a Lehmer mean, and the method of using secants for convex moments are standard. The inspected sharp Kantorovich inequalities bound different moment expressions and the original adaptive-method analysis does not supply this upper bound. Watson's broad method is the closest remaining full-text risk; its available abstract does not establish an exact specialization, so the pass is limited to the statements compared.

## value

PASS

Perfect balance is a natural model because it is the frozen fixed-point relation of the unregularized adaptive preconditioner, not a slice chosen merely to fit a calculation. In this regime an input to a learning-rate sufficient condition can underestimate its allowable ratio by a factor growing linearly with κ; exact sharpness shows this is not an artifact of a loose auxiliary estimate. The optimizer describes the balance of spectral extremes responsible for the loss. This quantifies headroom in a sufficient bound, not a practical recommendation to multiply an optimizer's step size by that factor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
