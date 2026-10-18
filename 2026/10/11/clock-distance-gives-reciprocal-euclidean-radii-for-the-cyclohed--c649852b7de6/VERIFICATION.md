---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

PASS: The source-defined directed clock quasi-metric ρ_d=d(n²−n+1)/n−d(d+1)/2 has ρ1=(n−1)²/n and discrete increment ρ_{d+1}−ρ_d=n−d−2+1/n≥1/n for 1≤d≤n−2. Jevtić–Jelić–Živaljević prove strict quasi-metric irredundancy/cyclohedral polar, giving all n(n−1) distinct ordered-pair inequalities as genuine facets of L_n and all normalized roots as polar vertices. Norm(e_i−e_j)=sqrt2 in zero-sum H0, so exactly n facets at distance ρ_d/sqrt2 for each d, and n polar vertices at norm sqrt2/ρ_d. For any inscribed center c∈H0, add the n clockwise-nearest constraints c_i−c_{i+1}≤ρ1−r sqrt2: telescoping yields r≤ρ1/sqrt2; equality forces c=0. For polar outer roots v_i=(e_i−e_{i+1})/ρ1, Σv_i=0 and averaging ||v_i−y||² yields R²+||y||², so minimum enclosing radius sqrt2/ρ1 has unique center y=0. Contact orbit and reciprocal identity follow. Our independent exact rational checker verified monotonic shells for n=3,…,15, only corroborating the symbolic proof.

## originality

PASS

PASS best-of-knowledge. Jevtić–Jelić–Živaljević (2018) already construct the explicit strict clock quasi-metric and establish the cyclohedral Lipschitz/KR polar realization, so neither source metric nor cyclohedron construction is claimed original. Gordon–Petrov establish general Lipschitz/KR face combinatorics and vertices under strictness. The audited Euclidean full distance/norm shell spectrum and proofs of globally optimal unique insphere/circumsphere centers are not stated in the inspected primary papers. A standard reciprocal polarity identity alone is NOT claimed as new; novelty resides in the exact directed-cost shell classification and unique contact orbit. Resultary unavailable; an unindexed general cyclic-cost theorem remains risk.

## value

PASS

PASS: The explicit clock quasi-metric is the canonical transport-geometric cyclohedron realization selected by the source. The exact n−1 strict shells, each with multiplicity n, together with both unique global Euclidean centers and contact orbits, furnish natural realization-sensitive metric invariants for all n. The result is a complete exact metric description of specified facet and vertex radii, not merely a one-off small-n value or the generic polar reciprocal observation; no claim for arbitrary cyclohedra/affine realizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
