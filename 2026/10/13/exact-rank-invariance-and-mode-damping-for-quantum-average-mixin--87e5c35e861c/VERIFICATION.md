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

For A any finite real symmetric n×n and g>0, each distinct eigenvalue theta gives 2×2 block [[theta,g],[g,0]] with lambda_(theta,±)=(theta±sqrt(theta²+4g²))/2. Both eigenvalue branches are strictly increasing, of opposite signs, hence no cross-theta collisions and full projectors E_theta ⊗ P_(theta,±). Cesàro phase averaging gives Mhat(H)=sum projectors Schur squared. Adding the two layer Schur squares yields one-half block [[S+Tg,S−Tg],[S−Tg,S+Tg]], S=sum E_theta∘E_theta and Tg=sum theta²/(theta²+4g²)(E_theta∘E_theta). Orthogonal layer transform gives S⊕Tg. Each Schur-square matrix is PSD, so ker Tg is intersection of ker Q_theta, theta!=0, invariant for all g>0; Tg decreases Loewner in g. H_g nonsingular, enabling iterated doubling. Path sine-square profiles independent up to reflection give path-comb rank m; clique projectors J/n,I−J/n give sharp min eigenvalue (n−2)/(n(1+4g²)) for n>=3. Independently diagonalized H_g for 4 matrices including singular bases at 3 couplings each, reproducing Schur block, rank and Loewner statements numerically to 1e−10. The analytic spectral derivation carries the unrestricted quantifiers.

## originality

PASS

Best-of-knowledge: prior full corona projector formulas and general Cesàro mixing identity are explicitly credited. Their combination allows a nontrivial graph-independent positive-coupling rank/kernel and Loewner damping theorem plus sharp infinite-family corollaries that were not presented as such in inspected primary literature; implicit-corollary priority risk expressly noted.

## value

PASS

Uniform pendant coupling is a canonical graph transformation and long-time quantum average mixing rank is a natural transport invariant. A universal exact block decomposition, monotone mode damping without rank loss, infinite iterated doubling, half-rank path combs and sharp positive clique gap give reusable structure beyond tabulating a toy spectrum. Physical/graph significance is explicit and the result is not merely an evaluation of one parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
