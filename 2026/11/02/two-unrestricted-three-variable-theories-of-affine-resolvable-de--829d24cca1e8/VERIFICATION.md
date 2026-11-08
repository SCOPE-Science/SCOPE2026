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

Under the exact hypotheses of a finite simple 2-(v,k,lambda) design with a resolution into t parallel classes of q blocks and a constant positive cross-class block intersection mu, counting gives k=qmu, v=q²mu, replication t, and t(k-1)=lambda(v-1), whence t>q. For the two-sorted incidence language, nine ordered-pair profiles refine every atomic two-position type: PP equal/different, BB equal/disjoint/intersect, and incident/nonincident PB/BP. The source proof enumerates all support types of an additional point/block relative to two anchors. The only emptiness changes occur with q=2 versus q>=3: outside two disjoint blocks has size (q-2)k, another parallel block exists exactly for q>=3, and q-2 further blocks avoid an outside point. Other counts lambda, t-lambda, mu, k-mu, etc. are strictly positive. The resulting support uniformity allows a three-pebble back-and-forth of arbitrary length for any pair of designs in the same q class. A three-variable rank-three sentence asserting two blocks cover all points distinguishes q=2 from q>=3; two-element atomic patterns agree at rank <=2. Lower bound on total vertices v+qt>=2q²+q is attained by AG(2,2) size 10 and AG(2,3) size 21. The proof uses only axioms, not finite sampled designs; no extension to arbitrary resolvable designs without uniform positive cross-intersections is claimed.

## originality

PASS

The 2-design classification results of Lam and Tonchev, rigidity of affine-resolvable designs by Key and Mackenzie-Fleming, and pairwise-transitive design theory concern isomorphism, automorphisms or coding. Standard pebble-game methods are prior, but the exact two unrestricted counting-free FO³ incidence theories with sharp size representatives appear distinct from those inspected statements. A broader coherent-configuration or Weisfeiler–Leman result could imply it; treat originality as qualified.

## value

PASS

Nonisomorphic affine resolvable designs can nevertheless have identical arbitrarily deep three-variable incidence theories. The exact dichotomy q=2 versus q>=3 and minimal representatives give a natural logical invariant of a broad combinatorial-design family without requiring field coordinatization or automorphism transitivity. The sharp unbounded-depth classification is a structural theorem, not a renamed finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
