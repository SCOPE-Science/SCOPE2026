---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For n>=9 any connected K_{2,5}-free cograph must have a singleton root join factor, hence a universal vertex: otherwise a minimum root factor of size>=2 has complement >=5 and creates K2,5. After removing v, K1∨H avoids K2,5 iff Δ(H)<=4 and H avoids K2,4. The published K2,4 cograph structural lemma then forces every connected H-component to have <=6 vertices; its local optimal edge counts for orders 1..6 are (0,1,3,6,10,11), with the unique admissible 6-vertex 11-edge block B6=(K2⊔K1)∨(K2⊔K1). I independently enumerated all simple graphs through 6 vertices, filtered induced P4, K2,4 common-neighbor counts and Δ<=4; optimum counts agree, with 90 labeled order-6 optima (single B6 isomorphism class). The exact unbounded integer knapsack has deficits 2d-w(d)=(2,3,3,2,0,1); its residue-optimal partitions yield δ=(0,1,2,3,2), including the 3B6 alternative for residue 3; independently verified optimal deficits AND complete partition types for m=8..200, not treated as proof. The analytic deficit argument proves all m. Small n7=17, n8=20 by cotree root cases; disconnected upper 3n-6 cannot attain claimed connected bound even in δ3 residue by modular component orders. Thus formula and complete n>=9 extremizers hold.

## originality

PASS

Zimmermann’s cograph bipartite Turan paper proves eventual linear-periodic structure with slope 3 for (s,t)=(2,5) and gives a dynamic programming method, not in its inspected theorem the explicit all-order period-five δ, exact small thresholds or full extremizer structures. The prior published K2,4 result gives the essential local B6 lemma but has DIFFERENT forbidden K2,4 and period-four global optimization; it does not imply the new target exact K2,5 classification without the universal-vertex remainder and new knapsack step. Narrow all-order classification is best-knowledge original; unexamined companion tables could overlap finite values.

## value

PASS

Exact natural restricted Turán number and complete structural description for a standard forbidden bipartite graph. It resolves the constant and residue classification beyond an asymptotic pumping theorem, exhibits a new role for an exceptional six-vertex block and non-uniqueness in one residue. Independent future extremal work can use the precise period-five threshold and extremal decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
