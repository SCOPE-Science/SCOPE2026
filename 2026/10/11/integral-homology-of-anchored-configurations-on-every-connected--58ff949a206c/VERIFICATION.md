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

PASS. Examined exact RESULT.md blob 9e20270deb1b3b6a6ee67c3c7348c6488a3f66ae and verify_anchored.py a288d1169c3bdc2a9dfc1d57be2d05b78a4c4639. Graph G finite connected CW, K nonempty anchor vertices, labels and collisions allowed, n>=r=|K|, b=E−V+1. Choose spanning tree T and anchor a; replace non-tree edges by loops at a to obtain W. Explicit edge-path maps G↔W and backtrack homotopies relative to T (therefore every anchor) give equivalence of anchored product subspaces. Cellular product chain complex on W splits integrally by the exact subset j of coordinates sitting on loop one-cells and which of b loops: loop cellular boundary is zero, leaving a copy of degree-j shift C_*(Sigma(T,K,n-j)) for each of C(n,j)b^j choices, j<=n-r. Kozlov's Stirling complexes tree theorem gives wedge^{f(r,t)} S^{t-r}, and r=1 tree case contractible; at n=r, precisely r! isolated vertex configurations. Free integral chain splitting and free tree homology prove no torsion and exact top and low Betti ranks, including loop/multi-edge and b=0 boundary. Independent arithmetic K4,b=3,r=2,n=4 gives Betti (1,12,121) as displayed; 14-case bundled checker mod2 source inspected not independently run, and could not by itself prove torsion-freeness.

## originality

PASS

PASS best knowledge with unusually explicit access risk: Kozlov 2023 computes anchored configurations for trees/contractible complexes, his 2024 paper computes Euler characteristic for all graphs and full homology for circle, not all connected positive cycle rank. Mamun–Nalikka–Ramos Sept2026 preprint is highly relevant; only abstract/indexed discussions were accessible. Its full arXiv/OA text failed; lawful Oxford retrieval returned vpn_disconnected; no bypass was attempted. No available established theorem strongly implies the all-graph integral splitting. Literature inaccessibility alone does not force O FAIL; actual best-knowledge PASS retains specific uninspected manuscript risk. Resultary self-hit and unrelated graph configuration findings do not supply coverage.

## value

PASS

PASS. Completes a natural open structural problem of additive integral homology of anchored configurations over every connected finite graph (including arbitrary cycle rank and loops/multiple edges), exhibiting unexpected torsion-freeness and full Betti polynomial dependence only on (b,r,n). The integral loop-cell decomposition is a reusable mechanism beyond an Euler characteristic or an arbitrary small-parameter computation; prior tree and circle cases are explicitly subsumed and attributed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
