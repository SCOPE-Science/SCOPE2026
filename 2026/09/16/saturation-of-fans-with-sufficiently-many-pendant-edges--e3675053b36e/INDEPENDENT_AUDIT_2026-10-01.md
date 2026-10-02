# Independent mathematical audit — SCOPE-20260916-011

Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Correctness
**PASS** — The proof was reconstructed in three stages. The displayed cone is H_{t,q}-free and saturation follows by using a new cross-component edge plus one edge from each of t-1 triangles. For any saturated graph with at most n+3t-4 edges, the degree budget forces a leaf and then forces its neighbor to be universal when q>=4t. Deleting that universal vertex yields a tK2-saturated graph with at most 3t-3 edges and an isolated vertex; Tutte--Berge forces a disjoint union of odd cliques, whose edge minimum is t-1 triangles. Fresh finite checks independently verified the claimed construction and saturation at (t,q,n)=(3,12,19),(3,13,20),(4,16,25).

## Originality
**PASS** — Hua--Peng's 2026 paper explicitly treats K2 plus isolates and 2K2 plus isolates, not tK2 plus isolates for t>=3, and motivates the isolated-vertex join problem. Cameron--Puleo gives the cone upper bound but not equality/uniqueness here. Searches of later fan/friendship and matching-saturation work did not locate a theorem implying the q>=4t result. A 2025 Discrete Applied Mathematics paper on generalized friendship saturation remains a concrete access risk; authorized retrieval was interrupted by human-verification expiry, so no NOT_COVERING claim is made for that paper.

### Equivalent formulations
Both formulations were searched because isolated vertices below a join become pendant vertices above it.

### Broader coverage
The accessible stronger/general sources do not cover t>=3; the inaccessible 2025 paper is disclosed as residual risk rather than treated as negative evidence.

### Exact database or table check
The result is theorem-level; non-hit is not used by itself to establish novelty.

### Claim versus prior implication
The audited theorem strictly extends the known petal count in an infinite parameter range and supplies new structure needed for the lower bound.

## Value
**PASS** — The theorem gives an exact saturation number and unique extremal graph on an infinite large-pendant range of a natural friendship/fan family, addressing a published extension problem. The universal-vertex forcing lemma is structural and the result is not a finite census.

## Source inspections
- **Saturation numbers for joins of graphs and characterization of extremal graphs** (https://arxiv.org/abs/2606.22011): NOT COVERING THE t>=3 CLAIM. Primary arXiv abstract and bibliographic record; exact families treated were compared. The abstract gives exact results for F=K2 union qK1 and F=2K2 union qK1 for every q, but no tK2 result for t>=3.
- **A lower bound on the saturation number, and graphs for which it is sharp** (https://arxiv.org/abs/2004.05410): INGREDIENT ONLY. Relevant theorem descriptions and implications as cited in the package were checked against the accessible preprint record. Gives the general cone upper bound, not the exact large-q equality and uniqueness here.
- **Some results on the saturation number of graphs** (https://doi.org/10.1016/j.dam.2025.04.038): ACCESS LIMITATION. Bibliographic/abstract-level material only; full-text institutional retrieval was interrupted by an expired human-verification step. Potentially relevant generalized friendship results; operative singleton-clique hypotheses could not be verified.

## Residual risks
- The 2025 Hu--Ji--Zhang paper is a plausible covering source whose full text was not obtained; this is the main residual originality risk.
- The threshold q>=4t is sufficient, not claimed sharp; the proof does not settle smaller q.

The accompanying JSON file records the four structured originality checks, source inspections, checked sources, and residual risks.
