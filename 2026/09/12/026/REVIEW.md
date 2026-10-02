# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. All 37 graph6 records were decoded independently. Each has no K4 and no independent set of size six. For every graph, all independent five-sets were independently enumerated and an exhaustive fail-first search over triangle-free hitting sets was run. All 37 searches proved that no such hitting set exists; the independent-five-set counts exactly match the archived certificate table, ranging from 742 to 818. The reduction is exact: a new vertex creates a K4 precisely when its neighborhood contains a triangle, and creates an independent six-set precisely when its non-neighborhood contains an independent five-set. Hence none of the 37 graphs admits a valid one-vertex extension.

Originality: PASS. Exoo's 2012 paper supplies the 37 K35 witnesses but does not state their one-vertex maximality. Lehavi's 2024 one-vertex-extension paper is the closest primary overlap: it reports that no 36-vertex counterexample has at least seven vertex-deleted subgraphs among the 37 known examples. That is strictly weaker and differently quantified than proving that each of the 37 individual graphs has no one-vertex extension, because a hypothetical extension of one known graph need not have seven deletions in the known subset. Thus the audited theorem is not implied by Lehavi's result.

Scientific value: PASS. R(4,6) remains open, and these 37 graphs are the classical witnesses behind the lower bound. Proving that every known extremal witness is individually maximal under the simplest extension operation removes a natural route to a 36-vertex witness while explicitly not claiming nonexistence of a de novo witness. This is a motivated exact obstruction directly tied to an open Ramsey problem.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
