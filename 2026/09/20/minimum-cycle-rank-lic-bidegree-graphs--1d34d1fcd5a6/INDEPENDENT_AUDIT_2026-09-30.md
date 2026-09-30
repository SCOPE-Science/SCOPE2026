# Independent Audit — 2026/09/20/minimum-cycle-rank-lic-bidegree-graphs--1d34d1fcd5a6

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c886f23d208660c5f95b98020ccbf31e1875d99c`
- Disposition: **PASSED**

## Correctness

**PASS** — The cycle-rank formula and extremal classification follow correctly from the bidegree counts. If x vertices have degree b and y have degree a, LIC means the irregular bipartite spanning graph between the two degree classes is connected, so x+y>=b+1 and mu=((b-2)x+(a-2)y)/2+1. For a>=3 this lower bound is increasing in x. A one-high-vertex extremizer exists exactly when b(a-1) is even, giving b(a-1)/2; otherwise x>=2 and the universal-two-high-vertex construction gives a(b-1)/2. The a=1 and a=2 cases are handled separately, and for a=2,b odd, x=2 is forced at equality; connectedness of the irregular subgraph forces at least one common neighbor, while the remaining private degree-2 vertices necessarily form a perfect matching and degree balance gives equal private counts. Independent enumeration of all connected Graph Atlas graphs through seven vertices reproduced the formula for every LIC bidegree pair present, including {2,3}, {2,4}, {2,5}, {3,4}, {4,5}, and others.

## Originality

**PASS** — Chartrand--Zhang (May 2026) determine LIC graphs of cycle rank at most 2 and the minimum order for prescribed degree sets. Their closing Problem 1 explicitly asks for conditions and minimum order at prescribed cycle rank r>=3. The audited all-parameter bidegree formula answers the first attainable cycle rank and recovers their rank-2 cases exactly. Older degree-set papers address unrestricted least order/size, not LIC cycle rank. Searches for the exact formulas with locally irregular-connected terminology found no matching theorem.

## Scientific value

**PASS** — The theorem completely resolves the first-cycle-rank threshold for every two-element positive degree set and classifies all minimizers, including the flexible {2,b} odd family. It gives a concrete exact answer in the first nontrivial subclass of a problem explicitly left open in the defining 2026 LIC paper.

## Sources

- **Locally Irregular-Connected Graphs** — Gary Chartrand; Ping Zhang. https://doi.org/10.3390/math14111827 — Introduces the LIC degree-set framework, classifies cycle rank at most 2, determines minimum order, and explicitly poses the r>=3 problem.
- **On the least size of a graph with a given degree set** — A. Tripathi; S. Vijay. https://doi.org/10.1016/j.dam.2006.04.003 — Prior unrestricted least-size degree-set result; a different optimization problem from LIC cycle rank.

## Limitations

- Only two-element positive degree sets are treated.
- The theorem determines the minimum attainable cycle rank, not the full set of attainable larger ranks.
- Very recent follow-up work after the May 2026 introduction of LIC graphs remains a residual originality risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "graph_atlas_exhaustive_check_through_7_vertices": true,
  "source_open_problem_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
