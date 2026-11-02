---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The final claim specifies d≥2, nonzero zero-sum centralized gradient h, zero initial Adam moments, 0≤β1,β2<1, ε>0, positive learning rate α and no weight decay. Bias-correction exactly gives mhat=h and vhat=h², hence Δw_i=−α h_i/(|h_i|+ε). For d=2, h=(a,−a) and drift is zero. For d≥3, let the positive and negative magnitudes sum to A>0 with p positive and n negative components. φ(x)=x/(x+ε) increases and is strictly concave; Jensen yields ∑positives φ(x_i)≤pφ(A/p), whereas subadditivity yields ∑negatives φ(y_j)≥φ(A). After reversing h to make S≥0, 0≤S≤pφ(A/p)−φ(A)=(p−1)A²/((A+pε)(A+ε))<p−1≤d−2. Thus |Δmean|<α(d−2)/d, and h=(a,…,a,−(d−1)a), a/ε→∞, makes the ratio tend to (d−2)/d. At fixed finite ε the bound is strict and the maximum is not attained; ε=0 is excluded. Projection of final adaptive delta gives zero mean at each step for those blocks on which it is actually applied. An independent exact-rational test covered 4214 cases and boundary families in dimensions 2..64; mathematical proof is analytic, not finite sampling. The seven source blob identities were read and the Git tree hash was reconstructed exactly.

## originality

PASS

Best-of-knowledge originality is confined to the complete dimension-sharp first-step drift envelope and its d=2 dichotomy. The formula for the first Adam-GC update is algebraically present in prior algorithm definitions, and final-delta GC2 mean preservation is prior source-code knowledge. However the quantified sharp supremum over all finite centered gradients at every d≥3 requires an additional global concavity/subadditivity extremal argument; the inspected primary literature and three semantic database searches did not contain it. This is an informed, qualified novelty assessment, not proof from search absence.

## value

PASS

GC’s projected-gradient affine constraint is explicitly offered as a central theoretical mechanism of the original method, and its Adam implementation is prominent. Quantifying precisely how far the actual adaptive update can leave that affine space—zero at d=2, strict but asymptotically near a whole learning rate as d grows—is an intrinsic, dimension-sharp safety/invariance boundary directly relevant to the original mathematical interpretation. It can inform optimizer choice and controlled mean preservation, without needing downstream generalization claims. The proof is short but the extremal object and invariant are independently motivated; neither correctness, novelty nor code reproducibility alone is used to justify value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
