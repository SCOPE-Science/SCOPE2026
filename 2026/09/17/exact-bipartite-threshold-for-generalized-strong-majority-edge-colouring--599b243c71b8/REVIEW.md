# same-model review

## Run identity

- Source run ID: `SCOPE-20260917T090104Z-R01`
- Research start: `2026-09-17T09:01:04Z`
- Finalized run end reported in conversation: `2026-09-17T09:17:15Z`
- Source artifact end timestamp: `2026-09-17T09:15:36Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Result type: substantive target

The timestamp discrepancy above is preserved rather than normalized away; the original source note is archived verbatim in compressed form under `artifacts/research_note.md.gz`, with decompression/hash instructions in `artifacts/research_note.md`.

## Correctness

**PASS (same-model assessment).**

The upper bound uses de Werra's published balanced edge-colouring theorem plus an elementary ceiling inequality. The lower bound converts the strong-majority condition into a local degree inequality for each colour class in `K_{k^2,k^2+1}` and proves a uniform colour-class capacity bound. The `k=2` boundary case reproduces the known `K_{4,5}` obstruction, and the source verification script checked the arithmetic/algebra and independently solved the `k=2` colour-class MILP.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The source run searched the new generalized strong-majority literature, equivalent terminology, the complete-bipartite family, de Werra connections, and follow-up citations. It found no indexed statement of the exact bipartite threshold. The strongest concrete originality threat is D. S. McNeil's inaccessible August 2026 personal communication, which the closest paper says contains `K_{4,5}` and “various other examples.” A very recent unindexed follow-up is also possible.

## Value

**PASS (same-model assessment).**

The result is an exact all-`k` theorem for a natural infinite graph class, with a matching obstruction family. It sharpens the known sufficient scale on bipartite graphs and is not an isolated numerical extension.

## Independence

The source run first discarded a prior-covered 5-regular target, then restarted on the generalized problem. As the first accessible run in this sequence, no earlier SCOPE result was used as a starting point.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
