# Independent mathematical audit — SCOPE-20260916-010

Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Correctness
**PASS** — The finite-field construction was rebuilt for q=3,5,7 from its coordinate definition. Independently constructed graphs had orders 30,90,182; were q-regular, connected, bipartite and C4-free; the local matching sizes were 5,9,13; the cross induced matchings had sizes 9,25,49; and the total-perfect-code ownership condition held. Cardoso et al. Theorem 2.1 then makes the cross matching maximum. Theorem 5 of Fürst--Leichter--Rautenbach gives |M|>=m/q² for locally stable matchings in {C3,C4}-free graphs. Combined with the regular conflict bound nu_s<=m/(2q-1), the exact ratio and integrality force |V|>=2q(2q-1).

## Originality
**PASS** — The two main ingredients are prior: efficient edge dominating sets are maximum induced matchings, and the local-search lower bound holds in triangle/4-cycle-free graphs. Neither inspected theorem constructs this affine two-copy family, the total-perfect-code matching of size 2q-1, or the simultaneous equality/divisibility benchmark. Searches under efficient edge domination, total perfect codes, affine incidence graphs, and local induced matching found no theorem implying the complete construction.

### Equivalent formulations
These standard aliases were searched; prior theory supplies consequences of each certificate but not their coexistence in the displayed affine family.

### Broader coverage
These are the exact general inequalities used in the proof; neither implies existence or minimum order of the audited affine equality family.

### Exact database or table check
The target is a construction theorem; database non-hit is supporting evidence only.

### Claim versus prior implication
The claim uses prior theorems as ingredients but contains a nontrivial existence/equality construction not mechanically implied by them.

## Value
**PASS** — The record supplies an infinite prime-power family attaining a natural extremal equality case for a known local-search bound while simultaneously certifying the global induced-matching optimum. This is a reusable structural benchmark rather than an arbitrary parameter instance.

## Source inspections
- **Efficient edge domination in regular graphs** (https://doi.org/10.1016/j.dam.2008.01.021): INGREDIENT ONLY. Open-access full text, especially Theorem 2.1 and Section 3/Theorem 3.1. Theorem 2.1 proves an EEDS is maximum; for p-regular graphs an EEDS has size |E|/(2p-1).
- **Locally Searching for Large Induced Matchings** (https://arxiv.org/abs/1708.02028): INGREDIENT ONLY. Full arXiv PDF around Theorem 5 and its proof. Theorem 5(ii) states |M|>=m(G)/d² for the relevant locally searched matching in {C3,C4}-free graphs.

## Residual risks
- The fresh coordinate reconstruction explicitly replayed prime fields q=3,5,7; extension-field arithmetic was checked from the package implementation and the symbolic field argument, not independently enumerated for every prime power.
- No exhaustive global classification of all equality graphs is claimed; only minimum order under the stated exact locality ratio is proved.

The accompanying JSON file records the four structured originality checks, source inspections, checked sources, and residual risks.
