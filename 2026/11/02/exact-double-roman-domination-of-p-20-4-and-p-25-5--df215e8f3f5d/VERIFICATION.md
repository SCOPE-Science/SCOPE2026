---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Definition requires every 0-labelled vertex to have a 3-neighbour or at least two 2-neighbours and every 1-labelled vertex to have a 2/3-neighbour. A weight-nonincreasing local replacement eliminates all labels 1. For P(5k,k), indexing outer and inner vertices by k columns and 5 positions makes all inner-zero constraints column-local. The table B(U,D) minimizes inner weights over all 243 five-state vectors for each of 243 outer and 243 demand vectors. With fixed outer vectors U_j, the exact minimum is sum_j(sum U_j+B(U_j,d_j)), with outer adjacency twists t-1 and t+1 at cyclic seams. Monotone lower bound sum_j L(U_j) prunes no feasible function of weight <= C. Independently reimplemented complete C++ exhaustive enumeration using the original graph predicate and rotated seam; for (k,C)=(4,33) visited exactly 1,912,264 surviving complete outer tuples and found 0 feasible, and (5,41) exactly 77,570,086 and found 0. Independent direct graph check of provided upper witnesses gives weights 34 and 42. Thus both equalities follow from finite exhaustive proof, not extrapolation.

## originality

PASS

Best-of-knowledge original sharp lower bounds for the first two parameter choices left between 8k and 8k+2 by the 2022 generalized Petersen theorem; pre-existing upper constructions are explicitly acknowledged, not attributed as new.

## value

PASS

The cases k=4 and k=5 are the first two unresolved boundary instances expressly left by published 2022 bounds. Exact sharp lower bounds resolve two small but mathematically motivated extremal graph parameters, rather than computing arbitrary or known entries. The full finite negative certificate is repeatable and can support future work on the unresolved residue classes; no sweeping general claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
