---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For n=1 there is one matching. For n=2 with two stable matchings, the men must both prefer the same one: if they disagreed they would both prefer the same woman, who would need to prefer each of her two partners to the other to prevent blocking in both matchings. When both men prefer one matching, stability of the other forces both women to prefer that other matching. Both profiles are then (2,2), with regret 2. For n=3 I reproduced the exact census by fixing man 0's preference list to the identity, a free normalization under women's label permutations, and weighting each normalized input by 6. For each perfect matching I independently compared the sets of pairs preferred by their male and female endpoints to their assigned partners; disjointness is exactly stability. Both partners' ranks contribute to the lexicographic objective and the maximum rank. Exact set comparisons give 37716 equal, 6984 strict P subsets, 1956 disjoint and no other cases. The stable counts are 34080, 11484, 1092. Among the disjoint profiles the counts by (stable count, |P|, |G|) are (2,1,1): 1728, (3,1,1): 144, (3,2,1): 84. After expanding the disjoint normalized profiles, orbit traversal by adjacent label transpositions on both shores and side-swap gives 26 size-72, 2 size-36 and 1 size-12 orbits. The witness has just the specified two stable matchings with profiles (2,4,0), (4,0,2) and regrets 2, 3; the incidence fraction reduces to 163/3888.

## originality

PASS

The objectives and underlying profile space are established. Very close Resultary records compute other pairs of fairness objectives, or the objective-free symmetry quotient of the same market. The checked sources do not supply the rank-maximal/minimum-regret optimizer relations or the objective-specific quotient. This is a best-of-knowledge assessment of the specific boundary and census, not priority for the objectives or enumeration technique.

## value

PASS

Lexicographically maximizing the number of high ranks and optimizing the worst individual rank express two natural, established goals. The result determines the smallest market where enforcing one can preclude the other and describes all optimizer-set relations there. Exact counts and symmetry types quantify and classify the first obstruction, rather than presenting a cherry-picked example or recomputing the known unlabelled compatibility-free census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
