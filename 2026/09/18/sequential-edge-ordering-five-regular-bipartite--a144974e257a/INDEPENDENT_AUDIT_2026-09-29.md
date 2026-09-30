# Independent audit — 2026-09-29

**Record:** `2026/09/18/sequential-edge-ordering-five-regular-bipartite--a144974e257a`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The Lovasz-local-lemma argument is correct. A uniform random order of X induces a block order of E in which every x-sequence is the increasing palette. At y, properness and simplicity make its d incident colors and X-neighbors distinct, so the bad event is exactly one relative order of N(y), with probability 1/d!. Relative orders on disjoint vertex subsets of a uniform permutation are jointly independent of the order on N(y), so the neighborhood-overlap graph is a valid dependency graph. Avoiding all bad events distinguishes every edge by either palette inequality or, for equal palettes, non-increasing order at the Y endpoint. In a d-regular bipartite graph Delta(J)<=d(d-1), and the factorial condition starts at d=5 and persists.

## Originality

**PASS** — The current arXiv version of Gorzkowska--Kwasny still states the general regular result only for degree at least six; its arXiv listing was last updated 11 September 2026. Searches for the source identifier together with 5-regular bipartite, sequentially orderable, neighborhood overlap, and local lemma did not locate this degree-five bipartite theorem or the stated D-parameter criterion. The result therefore passes to the best of the accessible literature, with the normal recency risk for a problem introduced only days earlier.

## Scientific value

**PASS** — The corollary closes an entire natural infinite degree-five bipartite subcase left outside the source's degree-at-least-six theorem, and the D-parameter theorem is a reusable structural criterion rather than a one-off construction. The proof is short but yields a genuine boundary improvement.

## Independent checks

- Reconstructed the induced edge order and verified that B_y fixes exactly one of d! relative orders of the distinct neighbors of y.
- Checked the dependency-graph requirement at the sigma-field level: the relative order on N(y) is independent of the collection of relative-order events supported on subsets disjoint from N(y).
- Verified Delta(J)<=d(d-1), the d=5 inequality 120>21e, and monotone persistence of the factorial inequality for all d>=5.

## Findings

- The local-lemma criterion and degree-five bipartite corollary are correct as stated.
- The directly relevant source currently advertises degree at least six rather than covering this d=5 bipartite case.
- The result does not solve arbitrary 5-regular graphs or degrees 3 and 4, as the record correctly states.

## Literature evidence

- https://arxiv.org/abs/2609.11832 — Gorzkowska and Kwasny (2026), directly motivating sequential-edge-ordering preprint; current abstract gives regular degree at least six.
- https://arxiv-troller.com/paper/3295810/ — Version metadata checked during the audit: submitted 10 September and last updated 11 September 2026.
- https://doi.org/10.1007/BF02579182 — Classical Lovasz local lemma background; the audit independently checked the application rather than relying on novelty of the lemma.

## Limitations

- The result is only a sufficient criterion and is not claimed sharp.
- Arbitrary non-bipartite 5-regular graphs and the general 3- and 4-regular cases remain outside the theorem.
- Because the motivating problem is extremely recent, unindexed parallel work remains a residual originality risk.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
