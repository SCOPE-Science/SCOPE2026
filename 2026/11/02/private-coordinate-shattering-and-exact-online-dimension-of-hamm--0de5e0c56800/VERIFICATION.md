---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For the all-shortest-path geodesic convexity in products of finite complete graphs, geodesic intervals independently change coordinate values, hence every nonempty convex set is exactly a product of coordinate subsets; the concept count is 1+∏_i(2^{n_i}-1). A support S is shattered iff each point has a coordinate value unique within S: this is necessary from the leave-one-out trace and sufficient since coordinate-projection hulls exclude every omitted point. Thus VCdim k when at least two factors are nontrivial and k+1 otherwise, k=∑(n_i−1). Littlestone upper bound k+1 follows from the positive first-query version space having 2^k boxes, while induction on k gives a depth-(k+1) complete mistake tree, exploiting a second nontrivial coordinate after a negative answer. For two factors private-value support graphs are star forests; exact max-support counts mn (m,n>=3), 2^max (one side two), 6 (2x2). Independent direct concept and online-dimension recursion verified (2,2): concepts 10, Ldim3; (2,3):22,Ldim4; (2,2,2):28,Ldim4, agreeing with proof.

## originality

PASS

Cartesian-product geodesic convexity is old (Jiang–Pelayo–Pritikin) and general online graph convex-set complexity is prior (Thiessen–Gärtner). The specific private-coordinate shattering iff, exact VC/Littlestone dimensions across arbitrary finite Hamming factors, sharp gap one and maximal-support star-forest counts are not directly stated by those inspected results. However signed-literal conjunction and combinatorial-rectangle terminology are important aliases; broader learning-theory coverage remains a priority risk.

## value

PASS

The all-alphabet exact classification relates graph convexity, static VC dimension and online Littlestone dimension, including an every-shape sharp one-unit gap and exact counts of extremal shattered supports in two factors. It resolves a natural parameter-uniform combinatorial dimension problem, useful independently of larger graph-learning bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
