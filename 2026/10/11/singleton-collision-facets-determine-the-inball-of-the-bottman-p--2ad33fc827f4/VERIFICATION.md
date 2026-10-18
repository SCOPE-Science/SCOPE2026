---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Verified the full BP facet classification and affine hyperplane Σz_i=C from actual source. Set H=n−1,K=m−1,d=H+K, C=choose(n,2)choose(m,2)+choose(n,2)+choose(m,2); translate w=z−1. For interval runs the mixed facet lower constant obeys h−t=(U−R)+(V−Q)+UV≤F(R,Q), with F=choose(R,2)+choose(Q,2)+choose(R+1,2)choose(Q+1,2). Direct rational simplification checks G(R+1,Q)−G(R,Q)>0 for R,Q≥1. Pure facets G(R,0)=1/2; H,K≥2 gives all proper nonsingleton h−t < [t(t−1)/(d(d−1))](C−d). Intrinsic projected subset normal norm √[t(d−t)/d] implies every nonsingleton facet farther than (C−d)/√[d(d−1)] from μ1. Every z_i=1 singleton has exactly that distance. Summing singleton constraints for any center in Σz_i=C gives matching upper bound and uniqueness. Finite independent exact rational checks m,n=3..6 corroborated >3500 support comparisons; these are not infinite proof.

## originality

PASS

The result is a metric optimization on the specific BP realization, not a restatement of the known face poset or shuffle realization. Original 2022 primary paper gives support equations only; exact Euclidean incenter, radius, and exhaustive tangencies require newly verified strict collision density gap. Best-of-knowledge PASS subject to broader general Chebyshev folklore risk.

## value

PASS

Constrainahedra have richly structured, exponentially many collision facets; the exact intrinsic inball and complete active-facet classification are natural, nontrivial global metric invariants of the explicit realization and expose a universal singleton-dominance phenomenon. The result gives reusable facet-density bounds beyond a tiny instance, without asserting arbitrary-affine invariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
