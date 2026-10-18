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

PASS: Complete frozen result defines p=|U|, q=|D|, m=p+q and arc alternating matching vertices with k +1 entries on U and k -1 on D, zero elsewhere. Direct expansion of squared distance from c_i=q/m on U, -p/m on D gives exactly pq/m regardless of k. The general projection lemma is valid for ANY finite equal-radius vertices: projection y of c onto P yields squared maximum distance R0²-|c-y|² by the normal cone inequality; exposed-face convex coefficients of y give matching lower bound for every other center and uniqueness. Every prefix of c is (q u_j-p d_j)/m. The complete source sign/rise/fall facet system then gives c in P iff each prefix belongs to [0,1]; boundary p,q>=1 and monotone word U^pD^q criterion pq<=p+q follow. Translating by 1_D yields active 0/1 base vertices of rank q and c+1_D=(q/m)1; apply published matroid uniform-density characterization after excluding ambient loops. Independently checked 255 U/D words of length 2–9 via exact Fraction cosphericity and LP hull-membership; the 57 balanced cases match the prefix condition. The finite check is corroboration, not the universal proof.

## originality

PASS

PASS best-of-knowledge: Padrol–Pilaud–Ritter created the shard polytope and determined its alternating-matching vertices and inequalities; Devriendt–Mulas proved general uniform-density equivalence. These ingredients were explicitly credited. The present exact Euclidean sphere, projection center/radius for all arcs and balanced-prefix optimality are a new specific metric invariant. Resultary exact same-object diameter work and general matroid radius results do not imply it. Access to Padrol–Pilaud–Ritter complete primary original was unsuccessful, retaining a real priority risk rather than inferring absence.

## value

PASS

PASS: Minimum enclosing sphere is a canonical geometric invariant for a natural family of shard polytopes used in quotientopes and matroid bases. Their vertices share a sphere despite varying matching size, yet its minimality depends nontrivially on arc balance; the sharp prefix strip and uniform-density equivalence give a usable combinatorial classification. Unknown projection distance in unbalanced cases is expressly not claimed to be a closed formula and does not erase the new exact criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
