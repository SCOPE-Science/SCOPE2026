# Independent Audit — 2026/09/12/026

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `7761bb0d4d399601ad0127df742ab5fb157600d3`  
**Disposition:** **PASSED**

## Correctness

I independently decoded all 37 graph6 witnesses, verified each is K4-free and has no independent set of size 6, enumerated every independent 5-set (742–818 per graph, matching the stored summary), and ran a separate exhaustive branch search for a triangle-free vertex set hitting all independent 5-sets. No such set exists for any of the 37 graphs. The reduction is exact: adding a new vertex with neighborhood S preserves K4-freeness iff S is triangle-free and preserves alpha<=5 iff S hits every independent 5-set. Thus none of the 37 known Ramsey(4,6;35) graphs admits a one-vertex extension to a Ramsey(4,6;36) graph.

## Originality

Exoo (2012) supplies the 37 Ramsey(4,6;35) witnesses, not their one-vertex maximality. Lehavi (arXiv:2411.04267) explicitly notes that Exoo did not state a proof that no R(4,6,36) graph can be generated from the 37 examples; Lehavi’s own reported R(4,6,36) check excludes candidates containing at least seven of the known 35-vertex subgraphs, and its extension method explores candidates with at least two known subgraphs when run on a subset. That is strictly weaker than proving that each individual known graph has no extension, i.e. excluding candidates containing even one of the 37 as an induced 35-vertex subgraph.

## Scientific value

The theorem eliminates the entire known lower-bound corpus as one-vertex seeds for an R(4,6)>=37 search and supplies short reproducible certificates for each graph. This is an exact obstruction at the current Ramsey frontier: any 36-vertex witness, if one exists, must avoid all 37 known witnesses as induced 35-vertex subgraphs. That is a useful search-space fact independent of whether the known 35-vertex list is exhaustive.

## Limitations

- The 37-graph corpus is not known to exhaust all Ramsey(4,6;35) graphs.
- The result does not prove R(4,6)=36 and does not exclude a de novo 36-vertex witness.
- The exhaustive no-extension proof is computational, though independently reimplemented in this audit.

## Evidence

- [Geoffrey Exoo, On the Ramsey Number R(4,6)](https://doi.org/10.37236/2102): Introduces the 37 known 35-vertex witnesses and improves the lower bound to 36; it does not state their one-vertex maximality.
- [Adam M. Lehavi, Ramsey Number Counterexample Checking and One Vertex Extension Linearly Bound by s and t](https://arxiv.org/abs/2411.04267): States that Exoo did not explicitly prove non-generability of R(4,6,36) from the 37 examples; its reported test excludes 36-vertex candidates with at least seven known 35-vertex subgraphs and discusses subset extension methods requiring at least two, not one.
- [Brendan McKay, Ramsey Graphs](https://users.cecs.anu.edu.au/~bdm/data/ramsey.html): Hosts the 37 known Ramsey(4,6,35) graphs and explicitly notes that more 35-vertex graphs, and possibly 36–40 vertex graphs, may exist.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `7761bb0d4d399601ad0127df742ab5fb157600d3`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
