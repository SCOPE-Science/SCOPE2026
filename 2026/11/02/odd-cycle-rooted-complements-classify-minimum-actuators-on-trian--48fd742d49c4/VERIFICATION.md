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

Unsigned incidence C on K_n satisfies CC^T=(n−2)I+11^T and Lap(J)=(2n−2)I−C^TC, with eigenmultiplicities 1,n−1,N−n. PBH gives minimum |U|>=N−n. For |U|=N−n, F=E(K_n) minus U has n edges and must give nonsingular unsigned C_F for largest eigenspace; each connected component must therefore contain an odd cycle and, by edge count, is odd-unicyclic. Second eigenvalue n is obstructed iff the complement U supports a zero-sum alternating a. The U edge density excludes bipartite connected graphs except n=6 and U=K_{3,3}, whose complement is two triangles; disconnected U gives one isolate and a triangle-bearing component with zero constrained a. Explicit star-plus-{2,3} complement proves attainment but U is not zero forcing. Rooted-tree EGF T=ze^T with odd-cycle factor (artanh T−T)/2 and exponential formula gives exact A_n, subtracting 10 for n=6. Independent finite-field PBH enumeration exhaustively checked all 252 n=5 and all 5005 n=6 candidate complements, yielding (162,2520) controllable vs (162,2530) odd-unicyclic candidates. All-size statement follows from the spectral and combinatorial proof, not finite enumeration.

## originality

PASS

The scalar minimum follows already from classical maximum eigenvalue multiplicity, and the odd-cycle nonsingular signless-incidence lemma is classical; neither is claimed novel. The new statement classifies every sharp coordinate-actuator placement for this fixed triangular graph Laplacian, identifies the unique six-label obstruction, counts them exactly and constructs a non-zero-forcing optimum. Zero forcing literature concerns all weights/qualitative classes and is not an equivalent fixed-Laplacian criterion; no located prior triangular-graph statement implies the complete classification.

## value

PASS

A sharp complete leader/actuator placement classification for a standard strongly regular line-graph family is a motivated controllability invariant. The solitary K3,3 exception and explicit non-zero-forcing optimal set delimit fixed-parameter controllability versus robust zero forcing and provide exact enumerative statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
