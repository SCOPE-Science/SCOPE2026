---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

If \(G\) is connected with cyclomatic number \(r\ge2\), then \(\operatorname{avm}(G)\ge2-1/[r(n-3)+1]\); for \(n\ge r+2\) this is the exact minimum at fixed \((n,r)\), attained uniquely by the \(r\)-page triangle book with every extra leaf attached to one endpoint of the common edge.

## Correctness — PASS

If a maximal matching of size one exists, its unique edge \(uv\) dominates every edge. Every other vertex is therefore private to \(u\), private to \(v\), or common to both; the edge/vertex count makes the number of common neighbors exactly the cyclomatic number \(r\). For \(r\ge2\), \(uv\) is the unique size-one maximal matching, all other maximal matchings have size two, and their number is \(ab+r(n-3)\). The average is therefore \(2-1/[ab+r(n-3)+1]\), minimized exactly when \(ab=0\). If no size-one maximal matching exists, the average is at least two. The Graph-Atlas verifier exhaustively confirms all relevant connected graphs through order seven but is not used for the infinite proof.

**Checked sources.** Assigned RESULT.md and artifacts/verify.py at the frozen source tree; Kai Zhang, arXiv:2604.28033, full HTML text; Engbers--Erey 2023 bibliographic/abstract material; Hertz--Bonte--Devillez--Mélot 2024

**Residual risks.** No correctness defect was found.

## Originality — PASS

Zhang's full 2026 paper explicitly says the Engbers--Erey extension question asks for \(k\)-cyclic graphs, solves only the bicyclic case, and proves the \(r=2\) member of the audited formula by separate core analysis. The all-cyclomatic dominating-edge reduction and exact count were not found in the older or current literature searched.

### Equivalent formulations

The line-graph independent-domination translation and dominating-edge formulation were included in the comparison.

### Broader coverage

The all-\(r\) theorem strictly extends the known bicyclic minimum rather than specializing a stronger prior statement.

### Exact database or table

Finite graph databases can corroborate small orders but do not determine the infinite theorem.

### Claim versus prior implication

The all-parameter conclusion is not mechanically implied by the bicyclic theorem.

**Checked sources.** https://arxiv.org/abs/2604.28033; https://doi.org/10.1016/j.dam.2023.08.022; Hertz et al. 2024; published mathematical corpus search

**Residual risks.** The inaccessible full 2023 Engbers--Erey article is the principal residual literature risk.

## Value — PASS

The theorem directly advances an explicit cyclic-extension problem, replaces bicyclic core casework by a general cyclomatic identity, and gives a unique exact extremal graph for every \(r\ge2\) in the attainable range.

**Checked sources.** Engbers--Erey extremal program; Zhang 2026 bicyclic theorem; Hertz et al. average-maximal-matching context

**Residual risks.** The denser range \(n<r+2\) and the maximum problem remain open here.

## Limitations

- The exact fixed-parameter minimum is asserted only for \(n\ge r+2\); the denser range is not classified.
- The maximum side of the cyclic extremal problem is not addressed.
- The complete 2023 Engbers--Erey paper was unavailable through available lawful full-text access.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
