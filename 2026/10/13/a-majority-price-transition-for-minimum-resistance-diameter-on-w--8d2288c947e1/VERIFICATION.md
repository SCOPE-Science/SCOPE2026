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

Tree path resistances add; all-pairs maximum equals max_{i<j}(1/w_i+1/w_j), never the edge-only maximum. Let D this maximum and u_i=(1/w_i)/D. Then u_i>0, pair constraints u_i+u_j≤1, and D=sum c_i/u_i. Conversely F(u) with pair constraints gives a feasible allocation; a strict-inequality point can be scaled and improved. If all u_i≤1/2, F≥2C sharply only at u_i=1/2. Otherwise one unique u_j=t>1/2 forces other u_i≤1−t, yielding sharp strictly convex envelope c_j/t+(C−c_j)/(1−t). Its unique interior minimum exists exactly at 2c_j>C, gives t=sqrt(c_j)/(sqrt(c_j)+sqrt(C−c_j)), and all other u_i=1−t. For no-majority all t>1/2 produce >2C. These strict equality conditions establish global uniqueness including m=2/boundary. Independently generated 1,000 positive integer price vectors with 10,000 other normalized resistance samples verified bounds and exact budget/diameter; full-domain proof analytic.

## originality

PASS

Ghosh–Boyd–Saberi 2006/2008 explicitly formulates maximum *all-vertex-pair* effective resistance as a convex/SDP objective but optimizes total resistance in primary analysis; general tractability is credited. Suliman–Weinstein targets maximum resistance over graph EDGES, different on a star. No examined source states the arbitrary-positive-price explicit star majority bifurcation and uniqueness formula. Its optimization is elementary but a nontrivial exact all-parameter answer; residual minimax design folklore risk.

## value

PASS

Worst-case all-vertex-pair effective resistance is an independently motivated network-design objective. This complete pricing sensitivity classification resolves arbitrary star size and arbitrary positive prices; it reveals uniform unique optimum even under heterogeneous costs until a sharp majority-price bifurcation. The exact allocation formulas and threshold can guide star network budgets, not extrapolated to general graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
