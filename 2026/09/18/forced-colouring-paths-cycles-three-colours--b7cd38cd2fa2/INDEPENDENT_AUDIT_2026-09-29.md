# Independent Audit — 2026/09/18/forced-colouring-paths-cycles-three-colours--b7cd38cd2fa2

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `16b26d8e2bdc0deb574f10968f6ad73a35bade85`
- Disposition: **PASSED**

## Correctness

**PASS** — The path and cycle coefficient formulas follow from the stated tight-vertex description. For a fixed proper 3-colouring of a path, the omitted initially-uncoloured set is exactly an independent set of internal vertices whose two neighbour colours differ; in ±1 increment coordinates this is the local equality delta_{i-1}=delta_i. The analogous cyclic condition gives the cycle transfer count. As an independent check, I reimplemented the forcing process directly from its definition and exhaustively enumerated all partial 3-colourings for P_n through n=6 and C_n through n=6; every coefficient matched the closed formulas exactly. The all-colour classification is also correct: for lambda>=4 no vertex of a degree-at-most-two graph can ever see lambda-1 distinct neighbour colours, while the lambda=2 connected bipartite case reduces to the standard two proper colourings.

## Originality

**PASS** — Farr's September 2026 paper develops the general forced-colouring polynomial, its basic properties and complexity, while the earlier Farr-Morgan work introduces the model and small examples. Targeted searches for path/cycle closed forms, the three-colour tight-vertex reduction, and equivalent independence-polynomial formulations did not locate these infinite-family formulas. The result therefore appears to be a genuine family-level computation beyond the available general theory.

## Scientific value

**PASS** — Paths and cycles are the first canonical infinite families on which a new graph polynomial should be made explicit. The formulas give exact coefficient distributions rather than just evaluations, isolate the three-colour forcing mechanism as a weighted independent-set problem, and provide tractable test cases for recurrences, asymptotics and future structural conjectures about the forced-colouring function.

## Sources

- The forced colouring function of a graph (G. E. Farr): https://arxiv.org/abs/2609.17108 — Current general theory of the forced-colouring polynomial; the indexed abstract states fundamental properties and #P-hardness, not the submitted path/cycle formulas.
- Forcing proper colourings of graphs (G. E. Farr; K. Morgan): https://arxiv.org/abs/2406.15746 — Open-access precursor introducing the forcing model and examples.

## Limitations

- The originality search cannot rule out an equivalent formula hidden under different terminology in an unindexed note.
- The independent exhaustive check covers small n; the all-n statement rests on the submitted tight-vertex/transfer argument, which was checked symbolically.
- No analogous closed form is claimed for graphs of maximum degree greater than two.

## Independent exact check

```json
{
  "method": "fresh exhaustive enumeration from the forcing definition",
  "paths_checked": "P_n for 2<=n<=6",
  "cycles_checked": "C_n for 3<=n<=6",
  "all_coefficients_match": true
}
```

GitHub was read only as evidence; no repository mutation was performed. The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. Open-access/preprint material was checked before other sources; no Oxford Download was needed for this record.
