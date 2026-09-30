# Independent Audit — 2026/09/17/cover-free-path-cycle-wheel-exact-values--d0cab96518f2

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e8879afb35975087590d169e8dd3e189dc1f5e08`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite certificates and deductions check independently. I reimplemented the submitted bit-mask search logic from scratch and obtained no six-point P_11 family, no six-point C_10 family, and no seven-point W_11 family. I also independently checked every listed seven-point construction for P_13,P_14,P_15,C_13,C_14,C_15 against the graph-CFF definition. The search reductions are complete: a graph-CFF on a graph without isolated vertices is globally an antichain; ground-set permutations are transitive on the fixed first-block size, and for wheels the center stabilizer is transitive on first-rim blocks with fixed size and center-intersection size. The DFS maintains all previous incomparability constraints and both directions of every completed edge-union constraint. The remaining exact values follow from subgraph monotonicity, the source upper bounds, and the published universal-vertex lemma.

## Originality

**PASS** — The May 2026 Parida-Moura source proves exactness only through P_10, C_9 and W_10 and leaves the later entries as upper bounds; its Open Problem 8.6 explicitly asks whether the P_10 construction can be generalized. The present record was deposited on 2026-09-17. The current arXiv v2, submitted 2026-09-24, still states Theorem 8.5 only through P_10/C_9 and Corollary 8.8 only through W_10; its Table 4 continues to label later entries as upper bounds rather than proving them exact. Targeted searches found no pre-2026-09-17 source containing the exact P_11/C_10/W_11 lower bounds or the seven-point n=13,14,15 constructions.

## Scientific value

**PASS** — The result closes the first unresolved lower-bound cases for all three graph families, thereby making the source table exact through n=12, and extends exact path/cycle values through n=15 while improving the prior general upper bound from 8 to 7 at n=13,14,15. The deterministic certificates are small enough to serve as reproducible benchmarks for future graph-CFF constructions and classifications.

## Sources

- Cover-free families on graphs (Prangya Parida; Lucia Moura): https://arxiv.org/abs/2605.12634 — Primary graph-CFF source; current v2 still proves exact path/cycle values only through P10/C9 and wheel values only through W10, while later Table 4 entries are upper bounds.
- Cover-free families on hypergraphs and combinatorial group testing (Thaís Bardini Idalino; Lucia Moura): https://doi.org/10.1007/s10878-026-01429-0 — Neighboring structured group-testing background; no matching exact path/cycle/wheel values were located.

## Limitations

- The nonexistence proofs are exhaustive finite computations rather than a human-only classification.
- Originality searches cannot exclude every differently named superimposed-code or structured group-testing formulation.
- The current arXiv v2 postdates the record; chronology was checked so later source revisions were not treated as prior art.

## Independent exact computation

- Implementation: fresh Python bit-mask search reconstructed from the mathematical definition.
- Negative cases: P11 on 6 points, C10 on 6 points, W11 on 7 points.
- Positive cases: P13 on 7 points, P14 on 7 points, P15 on 7 points, C13 on 7 points, C14 on 7 points, C15 on 7 points.
- Result: ALL CHECKS PASSED.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first. Oxford Download was used only where version-specific or full-text source verification remained unavailable through the open-access retrieval path.
