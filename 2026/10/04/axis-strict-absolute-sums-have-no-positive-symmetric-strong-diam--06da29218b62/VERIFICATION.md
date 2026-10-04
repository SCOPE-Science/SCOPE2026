---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was checked directly against the published definition of \(\mathrm{SSD}(d)\mathrm P\). For \(s=d/2>0\), two coordinate slices are sufficient. The axis-clearance functions \(\rho_1(\delta)\) and \(\rho_2(\delta)\) tend to zero by compactness and continuity; no differentiability or strict convexity is used. Membership of both signed perturbations in the first slice bounds the second component of the common direction, while the second slice bounds the first component. Monotonicity of an absolute norm combines the two bounds and contradicts the required lower norm bound.

For \(1\le p<\infty\), the axis-strict premise was checked from \(\|(1,t)\|_p=(1+t^p)^{1/p}>1\) for every \(t>0\). An arbitrary \(\ell_p\)-sum with at least two nonzero summands can be regrouped isometrically into two nonzero \(\ell_p\)-summands, so no cardinality or separability assumption enters.

No finite experiment, enumeration, numerical optimization, or external certificate is used. The result does not classify partially flat absolute norms, does not cover \(p=\infty\), and makes no claim about the nonsymmetric diameter properties.
