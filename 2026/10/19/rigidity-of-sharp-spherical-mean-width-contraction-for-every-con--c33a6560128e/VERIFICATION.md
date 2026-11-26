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

The proof was reconstructed from RESULT.md §§1–6. In the half-width formula the constant kernel contribution is linear in the output direction and averages to zero. Equality in the ordered Stieltjes integrals gives both rearrangement equality and cap optimality at a common radius, outside a set of zero decrease-measure. At that radius one can use the maximizing physical caps themselves as selectors in the transposed bathtub argument. Strict concavity of the cap moment (extended continuously to the endpoints) forces the transposed masses to equal s in (0,1); positivity then forces unit norm and uniqueness of the transposed selector. The cap pullback and uniformity conclusions follow by Fubini and harmonic completeness: the normalized zonal polynomial tends to 1 at the cap pole, so its analytic moment has nonzero small-cap ratio; in n=2 the direct Fourier formula gives the same conclusion. Nonatomic decrease puts zero mass on the countable exceptional set. The fixed-radius geometric step was independently checked: on the planar circle slices, arcs of length L have symmetric difference of angular length 2 min(theta,L,2 pi-L) for center separation theta in [0,pi]. A positive-measure family of slices has lengths bounded away from 0 and 2 pi (in n=2 use the circle itself). Thus symmetric difference separates centers and is strictly increasing locally; pulling back caps preserves this modulus and hence small distances. The center map extends from the dense full-measure set, Gram matrices give an orthogonal map on each small ball, and connectedness and Fubini give the claimed almost-everywhere identity. The constant case and orthogonal converse follow directly. For the hemisphere step, the sign sets of the normalized linear map are physical hemispheres, which attain the directional upper bound; averaging gives exactly the degree-one cap moment. The frozen numerical script was inspected as corroboration only; the decisive checks are analytic.

## originality

PASS

Credit Zhong–Kalaj for the sharp inequality and the strictly decreasing equality case. The supported distinction is rigidity under arbitrary nonzero continuous monotone decrease, particularly when the decrease measure lacks full support and may be singular; the proof through one generic radius replaces their all-radii argument.

## value

PASS

This resolves the remaining equality regime of a known sharp inequality. Extending from the full-support proof to plateau and singular non-full-support kernels requires a spectral and geometric argument. The step-kernel witness shows that dropping continuity indiscriminately would change the answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
