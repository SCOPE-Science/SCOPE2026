---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Let B=im D^T and Z=ker D. A vertex stabilizer fixes only zero cycle flow: all edges among other parts change sign under swap, and remaining two orbits of flows are forced zero by divergences at the distinguished vertex and an external vertex (p>=2). Hence Hom_Gamma(B,Z)=Hom_Gamma(Z,B)=0, so averaging any projection onto either invariant subspace yields its Euclidean projector and cannot increase any ℓq norm. Exact transfer-current Q=D^T(DD^T)^+D has two-part potentials U=(rp−1)/(r(r−1)p²), V=1/((r−1)p²)−1/(rp²). Summing six edge-type multiplicities yields sharp endpoint cut constant 2+2/r−4(rp−1)/(r(r−1)p²), cycle constant 3+2/r−8(rp−1)/(r(r−1)p²); real symmetry gives ℓ∞. Direct rational graph Laplacian and projection-column checks for (r,p)=(3,2),(3,4),(4,3),(6,2) agree. Finite checks do not establish all (r,p,q), which follow from the averaging proof. Finite difference sign yields transitions at p=5,6,7.

## originality

PASS

General group-averaging minimal-projection principle was known in Dilworth–Kutzarova–Ostrovskii (2023/2024), including Hamming graphs/tori, and Laakso graphs supply bipartite precedents. Inspected full text did not contain balanced complete r-partite family with r>=3,p>=2, exact cut AND cycle constants and r-transition. New stabilizer calculation and transfer-current formula are not merely renamings of a recorded Hamming projection constant.

## value

PASS

A natural symmetric family (complete multipartite graphs) has simultaneous minimizers for complementary cycle/cut spaces across the entire Banach ℓq scale, explicit sharp endpoint projection constants and a genuine part-count monotonicity phase transition. This fills a motivated quantitative gap in transportation-cost and graph-flow projections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
