# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-80664f4dba18`

## Correctness — PASS

The fixed-order bound follows from the independent inequalities \(\operatorname{diss}(G)\le n-1\) for connected graphs of order at least three and \(\alpha(G)\ge\lceil n/2\rceil\) for bipartite graphs. Equality forces both constituent bounds to be equalities. Removing the unique vertex outside an \((n-1)\)-vertex maximum dissociation set leaves only isolated vertices and edges; connectivity plus bipartiteness forces the removed vertex to meet each component in exactly one vertex. This gives the tree \(H(q,r)\), and its exact independence number \(q+\max\{r,1\}\) yields the parity classification. The finite verifier was inspected and correctly checks small graphs and trees, but the symbolic proof establishes the theorem for all orders.

### Correctness sources

- assigned RESULT.md
- Bock–Pardey–Penso–Rautenbach 2023 full primary text
- artifacts/verify_bipartite_gap.py

### Correctness risks

- The theorem assumes finite simple connected bipartite graphs.

## Originality — PASS

The closest primary paper was inspected in full. Its connected-bipartite results give degree-sensitive inequalities relating independence and dissociation numbers and discuss tree extremals, but they do not state the fixed-order maximum of \(\operatorname{diss}-\alpha\) or the parity-sensitive complete equality classification. Searches in the equivalent 3-path vertex-cover language likewise found no covering theorem.

### equivalent_formulations

Searches:
- Resultary: dissociation number independence number bipartite graph sharp maximum difference extremal construction
- Bock et al. arXiv:2205.03404 full text
- 3-path vertex cover dissociation fixed order gap

Evidence:
- The 2023 paper's relevant proposition is degree-sensitive rather than fixed-order.
- No returned current finding except the audited one gives the exact \(\lfloor(n-2)/2\rfloor\) gap and complete equality list.

Reasoning:
The dissociation and 3-path-cover formulations were both checked because their complements make the two gap statements equivalent.

### broader_coverage

Searches:
- Bock et al. 2023
- Bock et al. 2022
- Yannakakis node-deletion literature

Evidence:
- The broader prior literature studies bounds among the parameters and computation, not this exact order-extremal classification.

Reasoning:
General inequalities do not mechanically force the equality structure \(H(q,r)\); that requires simultaneous tightness and a structural argument.

### exact_database_or_table

Searches:
- current Resultary graph-theory findings
- 3-path vertex-cover terminology searches

Evidence:
- No exact fixed-order table/database theorem was found.

Reasoning:
The theorem is uniform in \(n\), not a finite census, even though a finite atlas is used as corroboration.

### claim_vs_prior_implication

Searches:
- claim-versus-prior implication comparison

Evidence:
- The prior degree-sensitive inequalities neither imply the exact fixed-\(n\) maximum for all degrees nor classify equality by parity.
- The audited proof derives equality graphs directly from the simultaneous constituent equalities.

Reasoning:
The fixed-order extremal theorem is not a restatement of the prior parameter inequalities.

### source_inspections

- **Relating the independence number and the dissociation number** — https://arxiv.org/abs/2205.03404. Trigger: Closest primary source on connected bipartite independence/dissociation inequalities. Material read: Complete accessible full text, including the connected-bipartite proposition and its proof/equality discussion. Method: Primary theorem-and-proof comparison. Assessment: NOT COVERING. Evidence: Its bound depends on maximum degree and does not give the audited fixed-order gap or parity classification.
- **Assigned finite verifier** — artifacts/verify_bipartite_gap.py. Trigger: Supporting finite checks. Material read: Complete source. Method: Line-by-line inspection. Assessment: Correct corroboration. Evidence: It exhausts connected bipartite graph-atlas cases through order seven and nonisomorphic trees through order seventeen.

### checked_sources

- https://arxiv.org/abs/2205.03404
- https://arxiv.org/abs/2202.01004
- 3-path vertex-cover literature
- current Resultary search
- assigned verifier

### residual_risks

- The proof is elementary enough that an equivalent statement could exist in poorly indexed 3-path-cover literature.

## Scientific value — PASS

The theorem gives a natural exact extremal gap at every order and classifies every equality graph, including the parity transition. It also answers the equivalent ordinary-versus-3-path vertex-cover spread. That complete structural classification is worthwhile despite the short proof.

### Value sources

- closest independence/dissociation literature
- assigned equality classification

### Value risks

- No claim is made beyond connected bipartite graphs.

## Limitations

- Finite simple connected bipartite graphs only.
- Finite enumeration is corroboration, not the proof.
- Originality is best-of-knowledge with a specific dual-terminology risk.

## Disposition

**PASSED**
