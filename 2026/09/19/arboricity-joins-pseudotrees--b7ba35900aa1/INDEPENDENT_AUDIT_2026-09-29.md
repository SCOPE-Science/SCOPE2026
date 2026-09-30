# Independent Audit — 2026/09/19/arboricity-joins-pseudotrees--b7ba35900aa1

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `5e85a9bb332bb692d4f41dfa3f6092a5394f7cd1`
- Disposition: **PASSED**

## Correctness

**PASS** — The Nash-Williams density proof is correct. For S=X union Y, the induced join has xy plus the internal edges, and the pseudotree bounds yield phi_d(x,y). Its discrete coordinate increments have numerators y^2-y+1-d and x^2-x+1-d, so monotonicity handles d<=1. In the d=2 unicyclic-unicyclic case, the only nonmonotone boundary x=1 or y=1 has actual density at most 2, strictly below the full-join density for orders at least three. Subgraphs inside one factor are also smaller. The independent-set extension has exact differences y^2-epsilon and (x-1)^2-epsilon with the same boundary repair. An independent brute-force enumeration of all connected tree/unicyclic graph pairs of order at most four (64 join instances) found the full vertex set maximal in every case and matched the displayed formula exactly.

## Originality

**PASS** — Kuanyshov-Yeginbay's September 2026 preprint states an exact wedge formula but only general lower and upper bounds for joins, with computations for selected families. The older Hobbs-Kannan-Lai-Lai-Weng paper develops 1-balanced generalized Cartesian constructions, not arbitrary graph joins of unequal-order pseudotrees. The audited theorem gives a shape-independent exact formula for all tree/unicyclic joins and a pseudotree-independent-set extension. Targeted searches using graph join/sum, pseudotree, unicyclic, arboricity, uniformly dense and 1-balanced terminology found no statement covering these formulas.

## Scientific value

**PASS** — The result converts a bounded regime in a very recent join-arboricity paper into a complete exact classification for a broad natural class, and shows that only orders and cyclomatic indicators matter. The accompanying 1-balancedness statement and independent-set extension unify fans, wheels and many further examples. The proof is elementary but the classification is reusable and nontrivial.

## Sources

- Arboricity and Simplicial Geometric Category of Wedges and Joins of Graphs (Nursultan Kuanyshov; Islam Yeginbay): https://arxiv.org/abs/2609.20606 — Primary 2026 source; its abstract states exact wedge formulas and only general bounds for joins.
- Balanced and 1-balanced graph constructions (Arthur M. Hobbs; Lavanya Kannan; Hong-Jian Lai; Hongyuan Lai; Guoqing Weng): https://doi.org/10.1016/j.dam.2010.05.004 — Older 1-balanced generalized-Cartesian construction paper, not an exact arbitrary-order pseudotree join theorem.

## Limitations

- The theorem is limited to connected pseudoforests and one-sided independent-set joins.
- Some equal-order special cases may be derivable from older 1-balanced construction machinery even though the explicit arbitrary-order formulas were not located.
- No optimal decomposition algorithm beyond the density formula is claimed.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "networkx_independent_cases": 64,
  "networkx_mismatches": 0
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository write was performed. Open-access and preprint sources were checked first. No current assigned record required Oxford Download.
