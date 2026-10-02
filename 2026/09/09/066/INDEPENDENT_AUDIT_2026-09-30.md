# Independent audit — SCOPE-20260909-066

Date: 2026-09-30 UTC

## Final claim

For the graph formed by wedging three 5-cycles at one common vertex, over \(\mathbb{Q}\) the induced matching number is 3 while \(\operatorname{reg}(S/I)=4\), so the graph gives a gap-one counterexample to equality on the triple-wedge tricyclic family.

## Correctness

**PASS.** A fresh independent exact computation reproduced the graph with 13 vertices and 15 edges. Exhaustive edge-subset checking gives induced matching number 3 and no induced matching of size 4. Independently rebuilding the full independence complex gives face counts 13, 63, 148, 179, 108, 27 and rational boundary ranks 1, 12, 51, 97, 81, 27, hence one-dimensional reduced third homology and the Hochster lower bound \(\operatorname{reg}(S/I)\ge4\). A separate exact vertex-deletion recursion over all induced vertex subsets gives the matching upper bound 4.

Residual risk: The upper bound invokes the standard edge-ideal vertex-deletion inequality, and the result is only over \(\mathbb{Q}\); characteristic dependence was not assessed.

## Originality

**PASS.** A semantic search for the exact triple-\(C_5\) bouquet regularity/induced-matching gap found this record as the direct match. The inspected bicyclic literature characterizes cyclomatic-two graphs, not this cyclomatic-three bouquet, and no published tricyclic bouquet formula covering the example was found.

Equivalent formulations: Searched triple \(C_5\) wedge/bouquet, edge ideal, Castelnuovo–Mumford regularity 4, induced matching 3 and tricyclic formulations; no prior exact same statement was found.

Broader coverage: The published bicyclic characterization applies to cyclomatic number two and therefore does not cover the cyclomatic-three graph here; unicyclic results are still narrower.

Exact database or table: No exact database/table for edge-ideal regularity of this named 13-vertex bouquet was located.

Claim versus prior implication: General lower bounds by induced matching and unicyclic/bicyclic formulas do not imply \(\operatorname{reg}(S/I)=4\) for this graph; the Hochster witness and deletion upper bound are needed.

Residual risk: There may be an obscure cactus-graph monomial-edge-ideal formula not surfaced by the searches; the closest indexed cactus result encountered concerns binomial edge ideals and is inapplicable.

## Value

**PASS.** The example falsifies a natural equality fallback at the first cyclomatic number beyond established unicyclic/bicyclic classifications. A small exact obstruction with a homological witness is useful for constraining any future tricyclic regularity-versus-induced-matching classification.

Residual risk: It is a single witness; minimality, attached-tree behavior and a full tricyclic characterization remain open.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/066/RESULT.md — Full statement and proof sketch inspected from the source blob.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/066/artifacts/replay_counterexample.py — Actual package computation source inspected; fresh audit used separately written exact code.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/066/artifacts/verify.py — Independent package verifier source inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE066 — Exact semantic search; this record was the direct match.
- https://arxiv.org/abs/1802.07202 — Cid-Ruiz–Jafari–Nemati–Picone abstract inspected; it characterizes regularity for bicyclic edge ideals and selected dumbbell powers, not this tricyclic bouquet.

## Disposition

**PASS.** Correctness, originality and value all pass the review bar.
