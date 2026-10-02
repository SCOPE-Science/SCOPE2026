# Independent audit — 2026-10-01

## Final claim

Maximality of the 37 known Ramsey(4,6;35) witnesses under single-vertex extension

## Correctness — PASS

PASS. All 37 graph6 records were decoded independently. Each has no K4 and no independent set of size six. For every graph, all independent five-sets were independently enumerated and an exhaustive fail-first search over triangle-free hitting sets was run. All 37 searches proved that no such hitting set exists; the independent-five-set counts exactly match the archived certificate table, ranging from 742 to 818. The reduction is exact: a new vertex creates a K4 precisely when its neighborhood contains a triangle, and creates an independent six-set precisely when its non-neighborhood contains an independent five-set. Hence none of the 37 graphs admits a valid one-vertex extension.

## Originality — PASS

PASS. Exoo's 2012 paper supplies the 37 K35 witnesses but does not state their one-vertex maximality. Lehavi's 2024 one-vertex-extension paper is the closest primary overlap: it reports that no 36-vertex counterexample has at least seven vertex-deleted subgraphs among the 37 known examples. That is strictly weaker and differently quantified than proving that each of the 37 individual graphs has no one-vertex extension, because a hypothetical extension of one known graph need not have seven deletions in the known subset. Thus the audited theorem is not implied by Lehavi's result.

## Scientific value — PASS

PASS. R(4,6) remains open, and these 37 graphs are the classical witnesses behind the lower bound. Proving that every known extremal witness is individually maximal under the simplest extension operation removes a natural route to a 36-vertex witness while explicitly not claiming nonexistence of a de novo witness. This is a motivated exact obstruction directly tied to an open Ramsey problem.

## Sources inspected

- Geoffrey Exoo, On the Ramsey Number R(4,6) — https://doi.org/10.37236/2102: OBJECT_SOURCE_NOT_PROPERTY_COVERAGE. Publishes the 37 K35 colorings and the lower bound R(4,6)>=36, but not their individual single-vertex maximality.
- Adam M. Lehavi, Ramsey Number Counterexample Checking and One Vertex Extension Linearly Bound by s and t — https://arxiv.org/abs/2411.04267: RELATED_BUT_NOT_COVERING. Section 5.1 proves no 36-vertex counterexample with at least seven subgraphs strictly within the known 37; it does not prove zero extensions from each individual member.

## Residual risks

- The 37-graph corpus is not known to exhaust all Ramsey(4,6;35) graphs.
- The theorem rules out only single-vertex extensions of these named witnesses; it does not rule out a de novo 36-vertex witness.

## Disposition

**passed**
