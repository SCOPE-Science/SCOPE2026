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

The no-flux balance gives ∫Qr=0, and r≡0 iff m/P is constant (test the homogeneous weighted Neumann equation by m/P). With v=Qw the operator is self-adjoint in L²(Q dx). The trial w=1+εr has a positive linear term 2ε∫Qr² against a quadratic diffusion cost, so the eigenvalue is strictly positive for each finite d. A constant positive principal eigenfunction would force r constant; the Rayleigh upper bound is therefore strict and the derivative is the strictly negative normalized Dirichlet energy. Interior bumps arbitrarily close to a maximizer give the d↓0 endpoint even for a boundary maximum. Normalize w=1+u with weighted mean u zero. On the mean-zero subspace the Neumann operator B=−Q⁻¹ div(a∇) has a bounded inverse; projecting the eigen-equation gives dBu=r+(I−Π)ru−Λu. The bounded potential and bounded Λ imply u=h/d+O(d⁻²) in weighted L². The mean equation gives Λ=∫Qru/∫Q=C/d+O(d⁻²), with C=∫a|∇h|²/∫Q>0. Constant c shifts the eigenvalue by −c exactly; strict monotonicity and the limits give the stated unique cutoff and cd_c→C. Direct cosine moments in the witness give potential, energy and norm squared per π equal to 1/16, 1/32 and 35/32; capacity minima are 5/12 and 61/150, and C=1/32.

## originality

PASS

Equal-capacity invasion substantially overlaps a distinct indexed result and is explicitly an open question in the cited primary paper, not a new general spectral principle. The supported distinction is the entire additive-loss/mobility frontier for the prescribed resident target, including its Neumann corrector and inverse scaling; neither that primary paper's advantage theorem nor the indexed fixed-mobility proportional-loss threshold establishes it.

## value

PASS

The theorem answers a model-specific linear-invasion question for an explicit prescribed dispersal target and quantifies the tradeoff between a uniform ecological disadvantage and movement, rather than merely showing existence of some favorable strategy. The corrector predicts the mobility cutoff for small losses and the exact positive-disadvantage witness rules out an interpretation confined to equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
