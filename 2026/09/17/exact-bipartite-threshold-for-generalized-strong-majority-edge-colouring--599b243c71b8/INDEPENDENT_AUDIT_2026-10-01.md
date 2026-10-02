# Independent scientific audit — Exact bipartite threshold for generalized strong-majority edge colouring

Audit date: 2026-10-01 UTC.

Disposition: **PASSED**.

## Correctness

**PASS** — The upper bound follows correctly from balanced bipartite edge-colouring: d_alpha(v)<=ceil(d(v)/(k+1))<=(d(v)-1)/k for d(v)>=k-squared+1. For the lower bound, the one-colour constraint on K_{k-squared,k-squared+1} implies the stated high-degree structure and the case split gives |E(H)|<=M_k=k-cubed-k-squared+k; multiplying by k+1 yields k-to-the-fourth+k<k-to-the-fourth+k-squared total edges. The case algebra was independently checked for every 2<=k<=1000, including the boundary k=2. The proof is symbolic; the MILP artifact is only supplementary.

## Originality

**PASS** — The inspected Pękała--Przybyło source introduces the generalized strong 1/k notion and proves the general-graph sufficient bound 2k-squared+1; its concluding discussion leaves improved thresholds as an open direction and records the k=2 bipartite obstruction. Resultary search found no independent all-k bipartite k-squared+1 theorem. The inaccessible McNeil personal communication cited by the source remains a real but non-decisive residual risk; no accessible material indicates it contains the all-k result.

### Equivalent formulations

Search included generalized strong-majority, bipartite threshold, and the K_{k-squared,k-squared+1} obstruction formulation.

Searches: Resultary: exact bipartite threshold strong 1/k majority edge colouring k+1 k-squared+1; Pękała--Przybyło arXiv:2608.04122.

Evidence: Only the audited record matched the exact all-k bipartite threshold.

### Broader coverage

The broader general-graph theorem is weaker on bipartite graphs and therefore does not cover the exact k-squared+1 result.

Searches: Pękała--Przybyło Theorem 7; balanced bipartite edge-colouring/de Werra.

Evidence: The primary source gives 2k-squared+1 for all graphs; balanced edge-colouring supplies the upper-bound tool but not the lower obstruction/classification.

### Exact database or table

No exact database/table was found that mechanically supplies the threshold for all k.

Searches: Resultary search; source discussion of computational examples.

Evidence: The theorem is uniform in k; isolated computational examples such as K_{4,5} do not constitute an all-k table covering the claim.

### Claim versus prior implication

No inspected prior theorem gives both directions at k-squared+1, so the final exact threshold is not a mere special case of the cited general theorem.

Searches: Pękała--Przybyło arXiv:2608.04122; de Werra balanced-colouring theorem.

Evidence: The upper half is implied after a new arithmetic observation, but the matching lower obstruction requires the record's one-colour extremal argument.

### Source inspections

- **On Strong Majority Edge Colourings with Few Colours** (https://arxiv.org/abs/2608.04122): Assessment: proves 2k-squared+1 for general graphs and motivates sharper thresholds; does not state the all-k bipartite k-squared+1 theorem. Material read: abstract, Theorem 7 statement/proof text, and concluding/open-problem material in accessible full-text rendering. Evidence: Theorem 7 gives the 2k-squared+1 sufficient bound; the concluding discussion treats improved thresholds as open.

Checked sources: https://arxiv.org/abs/2608.04122; Resultary semantic search for all-k bipartite threshold; record artifacts/verify.py.

Residual risks: The source cites an August 2026 personal communication by D. S. McNeil for K_{4,5} and computational examples; that inaccessible communication could contain overlap, though no accessible evidence indicates an all-k exact theorem.

## Scientific value

**PASS** — The result exactly solves a natural threshold problem in the bipartite subclass for every k, improves the general sufficient bound by essentially a factor of two, and supplies a matching infinite obstruction family. This is a motivated all-parameter theorem, not a finite-table computation.

## Final claim

For every integer k>=2, the least minimum degree forcing a strong 1/k-majority edge-colouring with k+1 colours in every finite simple bipartite graph is k-squared+1; K_{k-squared,k-squared+1} is a sharp obstruction.

This audit is a scientific assessment of the claim and supplied evidence. It is not peer review, formal verification, or a guarantee of first discovery.
