---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Since the zero set V0 is not dominating, some positive vertex x has no zero neighbor. When V0 is nonempty, the universal center cannot play x, so x lies in a blade B_i, forcing center positive and all r blade vertices positive. Weight ≥r+1, and r+1 fails Italian domination on every all-zero other blade (they see center label1 only). A matching construction with center2 and B_i labels1 gives weight r+2. If optimum weight r+2 had center1, at most one further positive unit outside the forced blade is available; m≥3 guarantees at least one totally zero other blade, whose zero vertices have total neighbor weight1, contradiction. Thus center2 and exactly one full blade1 are forced, giving m distinct functions for every r≥1. Independently enumerated all 3^(1+mr) labels for (3,1),(3,2),(3,3),(4,1),(4,2),(5,1), reproducing minima r+2 and multiplicity m; finite checks only corroborate arbitrary m,r proof.

## originality

PASS

Cabrera Martínez 2021 establishes the same scalar γ*_I=r+2 via Theorem 4.6 universal-join formula with δ(mK_r)=r-1, but the theorem does not list every minimum starred Italian function or multiplicity. Full original PDF inspected, notably universal-join theorem and family results. Searches for windmill/friendship and starred Italian equality families (also Resultary) did not reveal an equivalent optimizer census. Unindexed equality-characterization risk remains.

## value

PASS

The minimum-weight value already existed, but this identifies *every* minimizing labeling and the exact optimizer multiplicity on the whole natural generalized-windmill family, with a genuine transition at m=2. Structural rigidity describes the combinatorial mechanism of extremality, not merely an arbitrary small parameter substitution or re-derivation of the known scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
