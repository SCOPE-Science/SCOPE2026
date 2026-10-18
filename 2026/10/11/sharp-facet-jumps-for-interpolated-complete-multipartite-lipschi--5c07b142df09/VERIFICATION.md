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

PASS. The k≥3 real complete-multipartite metric is valid for 1≤t≤2, dual dimension N−1. Connected tight-edge graph ⇔ dual vertex by incidence rank. For 1<t<2, with no tight internal edges, connectedness gives integer-valued binary potentials. In ≥3 parts, disconnected nonconstant binary cuts occur exactly when a single mixed part has all other parts monochromatic: exclude 2∑(2^m_i−2) orientations. With a tight internal edge in part i, all outside vertices lie in [t−1,1], a band narrower than 1, so no outside tight edge; connectedness forces the unique saturated part's values {0,t} and every external value t−1 or1. This gives (2^m_i−2)2^(N−m_i) for each unique i; summing yields 2^N−2+∑(2^m_i−2)(2^(N−m_i)−2). Endpoint t=1 equilateral and t=2 previously known 2^N−2−∑(2^m_i−2), also follows directly. Singleton-only profile remains equilateral. Independently enumerated all half-integer connected tight potentials for 4 profiles and all three t=1,3/2,2 (12 exact cases), including (2,2,2): 62,146,56; inspected actual check_facets.py finite algorithm without executing it. Analytic classification, not finite enumeration, proves the infinite family.

## originality

PASS

Best-of-knowledge PASS for the k≥3 strict-interior expression and its two-type tight-potential classification; pre-existing complete multipartite graph t=2 formula is not credited as new. The distinct k=2 related theorem does not cover k≥3. No inspected published source covers weighted strict t between 1 and 2.

## value

PASS

PASS. This is a natural exact facial invariant and complete extreme-potential classification for every k≥3 and arbitrary block sizes, with a structural difference from two-part tight-cut connectivity and a strict phase jump under metric interpolation. The precise count is reusable in polyhedral metric geometry; no downstream theorem/paper-size test is demanded. The endpoint table is credited as known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
