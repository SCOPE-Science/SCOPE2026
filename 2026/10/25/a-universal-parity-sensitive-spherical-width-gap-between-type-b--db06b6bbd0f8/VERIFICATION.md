---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For all n>=4 and strictly increasing a_i>0, B_n(a) is full signed-permutation orbit hull and D_n(a) is its even-negative-sign suborbit. Rearrangement yields h_B(u)=sum a_i|u|_(i). For odd negative-coordinate parity, at least one mismatched sign in D costs >=2 a1 min_i|u_i| and equality is attained using an optimal assignment pairing a1 with the smallest |u_i|; even parity gives equal support and zeros can correct parity free. Therefore h_B−h_D=2a1 min|u| times odd-parity indicator, and d_H(B,D)=2a1/sqrt n. Under u->−u parity changes iff n odd, so width loss is 2a1 min|u| for odd n, and 4a1 min|u| times odd-parity indicator for even n. Gaussian sphere sampling U=G/||G|| yields n min|G_i| => Exp(sqrt(2/pi)), ||G||/sqrt n->1, signs independent of magnitudes, giving stated parity-mixed scaled laws and all fixed positive moments by uniform exponential tails/Hölder inverse-chi moments. Variances normalize to 2pi odd and 6pi even. Independent brute 4D signed-permutation maximum for a=(1,1.8,3.3,4.2) and u=(-.4,.2,-.8,-1.2) found support loss .4 as predicted.

## originality

PASS

Elementary rearrangement and Gaussian minimum-order-statistic theory are classical, as are Coxeter B/D orbit-polytope descriptions. Ardila–Castillo–Eur–Postnikov 2020 covers type B/D generalized permutahedra/deformations, while Godland–Kabluchko 2023 gives projected face counts and angle sums; neither supplies the coupled same-weight B-versus-D support-loss law with Hausdorff extremum and parity-dependent random-width limit. Published SCOPE B/D Fourier norms and spin-weight John ellipsoids are different quantities. Best-of-knowledge priority limited to this combined coupled invariant, not basic rearrangement.

## value

PASS

A motivated, exact metric/probabilistic contrast of natural hyperoctahedral versus even-sign Coxeter orbit polytopes: despite halving vertices, maximal support loss is controlled by the smallest weight and min coordinate, while odd/even ranks have sharply different zero-loss angles and fluctuations. This structural parity law and its exponential/Bernoulli scaling is a reusable quantitative geometry invariant, not an arbitrary computational slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
