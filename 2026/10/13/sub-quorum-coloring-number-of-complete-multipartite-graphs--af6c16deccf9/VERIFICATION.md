---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For a partial quorum coloring with q≥3 of induced colored H⊂K_{n1,...,nr}, choose ANY largest occupied part P of size L_H; let M be number of colored vertices outside P and h=ceil((M+1)/2). Every color meeting P uses ≥h−1 outside P, because any colored v in P sees itself plus M outside; any color disjoint from P uses ≥h of its own colored vertices because every other part has size ≤L_H and hence its closed colored neighborhood has size ≥M+1. If w≥1 missing classes, u=q−w≥1 present classes imply M≥u(h−1)+wh, impossible for q≥3 and M≥2 (check M even/odd). If M=1, a disjoint singleton class would have only one own color in ≥L_H+1 colored neighbors and forces L_H≤1, hence q≤2. Therefore all classes meet P and q≤L_H≤L. With ≤2 classes q≤max(L,2). Lower bound: color each of L vertices of largest independent part distinctly; for L=1 complete graph pick two colored vertices with distinct colors (each exactly half). Concludes ψ_sq=max(L,2) for r≥2 nonempty parts. Independent checker enumerated 23 complete-multipartite unlabeled order profiles through N=6 and 10208 partial color partitions, checking quorum and structural property; finite experiment supplements unrestricted argument.

## originality

PASS

Sahbi–Belkina–Bennadji Sep2026 caterpillar preprint introduces targeted natural-family calculations; older 2013 paper defines sub-quorum. An especially relevant earlier 2026 arXiv:2609.25128 (latest v4 Oct2026) proves general degree bounds and classical-family cases. Its degree bound already implies ψ_sq(K_{a,b})=max(a,b) for complete bipartite graphs with minimum part ≥2 via floor[b(a+b)/(a+b−1)]=b; that bipartite special case receives NO novelty credit. The present claim covers arbitrary r≥3 and proves stronger all-largest-occupied-part intersection property, not obtained from that degree inequality (e.g. K2,2,2 gives bound 24/7>2). Full arXiv paper could not be acquired/read and authorized institutional tool returned vpn_disconnected; potential general matching theorem remains explicit significant residual risk. Best-of-knowledge original for ≥3-part sharp classification and structural statement.

## value

PASS

Exact all-part-profile ψ_sq of connected complete multipartite graphs and a rigidity statement for every ≥3-color partial coloring fill a natural newly defined invariant; distinction from ordinary quorum coloring and the transition at L=1 are mathematical structure. The bipartite slice is prior-implied and not counted as independent novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
