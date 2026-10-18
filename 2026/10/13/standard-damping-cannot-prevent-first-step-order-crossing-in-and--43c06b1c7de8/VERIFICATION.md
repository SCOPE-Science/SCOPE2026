---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Minimize Q(β)=Σ a_i²e_i²(1−β a_i)². Second derivative 2Σa_i⁴e_i²>0 for nonempty active set, so unique minimizer as claimed. Weighted-average identity τ=Σ(a_i³e_i²)a_i/Σa_i³e_i² gives strict min<τ<max when distinct gaps, and (1−ωa_i)>0 for 0≤ω≤1. In exact two-rate example Λ=(1/2,3/4), x*=1, x0=(36,36), β=36/17, τ=17/36, first output 1−(35/17)(1−ω/2) equals −18/17 at ω0 and −1/34 at ω1, negative on interval. One active dimension reaches exact fixed point, hence two is minimal. Reconstructed full algebra and source Fraction checker; statements concern first damped Anderson step, not later iterations.

## originality

PASS

PASS but narrowly assessed: Walker–Ni 2011 already defines Anderson residual minimization and notes possible negative matrix entries, while a published Resultary Oct4 record gives a two-dimensional positive diagonal contraction with a sign failure at SIXTH iterate and no all-damping claim. Thus the general possibility of loss of positivity and minimal dimension are covered; the retained new precise assertion is mandatory coordinate-side split on the FIRST prediction for arbitrary active diagonal rates, exact weighted-gap classification and damping invariance ∀ω∈[0,1]. This follows by new specialization/weighted-mean analysis rather than a directly stated earlier theorem; residual risk for vector-extrapolation literature and routine-derivation value.

## value

PASS

PASS narrowly for the sharp first-step order-invariance obstruction: there is a substantive question whether underrelaxation can preserve positive orthants and monotone coordinate bounds after acceleration. The theorem proves that ordinary post-prediction damping alone cannot repair ANY multi-rate sign split and gives an exact all-damping two-dimensional counterexample; this is more operationally precise than the already-known possibility of later negativity. Does not claim originality of Anderson, least-squares coefficient per se, or generic positivity loss.

The dated certificate retains the supplied scientific assessment, sources and limitations.
