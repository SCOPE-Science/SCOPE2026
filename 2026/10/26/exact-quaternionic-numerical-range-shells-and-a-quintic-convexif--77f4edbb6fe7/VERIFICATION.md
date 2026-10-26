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

The main proof is analytic for every \(a\ge b>0\) and \(c>0\): exact five-coordinate image, constrained quadratic extrema, rotational convexification, integration and a convergent asymptotic expansion. The upstream five-coordinate ball-filling lemma is attributed to the 2026 primary paper.

Run the included standard-library checker with `python verify.py`. In the packaged check it produced `PASS 50396 finite checks; volume profile and shell bounds`. The checker samples unit quaternionic vectors in five qualitatively different parameter regimes and checks the claimed shell membership, tests an exact-rational quadratic identity on further parameters, and compares the closed volume profile to independent midpoint integration. The separately reconstructed elementary sine-power integrals and the substitution \(\sin\theta=rt\) establish the universal closed formula and quintic coefficient. No finite experiment is offered as a proof of universal validity.

The parameter normalization requires \(d=a-b\ge0\), \(s=a+b>0\), \(r=d/s\in[0,1)\); the radius \(c>0\) is not the anisotropy. The degenerate case \(a=b\) is included, with zero missing volume. Singular limit \(b=0\) is excluded. No independent audit or publication-priority certification is asserted.
