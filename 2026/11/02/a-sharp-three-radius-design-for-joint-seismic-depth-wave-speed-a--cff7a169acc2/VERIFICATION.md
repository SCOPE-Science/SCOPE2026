---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Squaring t_i=tau+v^-1 sqrt(|s_i-x|²+h²) gives exact 5-column linear design [2t_i,|s_i|²,s_ix,s_iy,1]. Five distinct circle stations force an affine time relation to have a degree-two trigonometric polynomial with 5 zeros, so its degree-two harmonic vanishes (slope b=0) and the degree-one harmonic forces x=0. For x=0, three distinct squared radii sample a strictly concave sqrt(z+h²), excluding affine rank loss. A circle gauge u→lambda u, x→x/lambda², h²→(R²+|x|²+h²)/lambda²-R²-|x|²/lambda^4 proves all-circle nonidentifiability. Two radii fail centrally. Independently computed rank 5 for central and two off-center positive-depth instances, with minimum singular values 0.01450,0.00771,0.00893; finite samples are supplementary.

## originality

PASS

Classic calibrated-speed linear source localization uses related squaring but does not itself prove global identifiability when both origin and speed are unknown, nor the 5-circle/2-off-radius sufficient design and radial lower bound. Exact general acoustic localization may imply an equivalent construction; this remains a risk.

## value

PASS

Unknown speed, depth and origin time is a natural inverse problem. The exact radial-identifiability obstruction and universally safe seven-station layout are concrete constructive and negative results; no claim of optimal station number among all planar arrays.

The dated certificate retains the supplied scientific assessment, sources and limitations.
