---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

If \(G\) and \(H\) are connected finite nontrivial graphs of girth at least five, then \(\mu_c(G\square H)=3\); the maximum connected mutual-visibility sets are exactly the Cartesian corners, and there are \(4|E(G)||E(H)|\) of them.

## Correctness — PASS

At a selected vertex, two selected neighbours in the same factor direction would have that vertex as the unique internal point of their length-two geodesic because girth at least five forbids both triangles and a second common neighbour. Hence the selected induced graph has degree at most two. Four consecutive vertices of a selected path/cycle must alternate factor directions; for endpoints separated by two forced steps in one factor and one edge in the other, every shortest shuffle passes through at least one of the two selected internal vertices. A Cartesian four-cycle fails similarly for opposite corners. Thus no connected mutual-visibility set has size four, while every three-vertex Cartesian corner works via the unused fourth corner. The centre is unique, and summing \(d_G(g)d_H(h)\) gives \(4|E(G)||E(H)|\). The definition-level verification script was inspected and correctly checks all small atlas factors, but the finite enumeration is only corroboration.

**Sources.** current RESULT.md and verification script at archived record; Tonny K B--Shikhi M, arXiv:2609.18877; Cicerone--Di Stefano--Klavžar product visibility literature

**Residual risks.** No correctness defect was found.

## Originality — PASS

The paper introducing connected mutual visibility gives general structural, block, and complexity results but its public primary description does not state a Cartesian-product theorem. Earlier Cartesian-product literature concerns ordinary, total, lower, or related mutual-visibility parameters. published-result corpus searches for connected mutual visibility in high-girth Cartesian products returned this record as the first exact theorem; nearby rook/line-graph records are later or concern low-girth factors.

### Equivalent formulations

Connected mutual visibility is a distinct maximum parameter because the selected set must induce a connected graph.

### Broader coverage

No checked broader theorem mechanically implies the sharp upper bound or maximizer classification.

### Exact database or table

No earlier exact database theorem was located.

### Claim versus prior implication

The alternating-direction geodesic obstruction and complete corner classification are additional structural work.

**Checked sources.** arXiv:2609.18877; arXiv:2112.13024; Di Stefano 2022; Korže--Vesel 2024; published-result corpus search

**Residual risks.** The invariant is extremely recent, so parallel unindexed work is a material residual originality risk. The full arXiv body of the introducing paper was not retrievable, but its abstract and published-result corpus coverage checks did not reveal a product theorem.

## Value — PASS

The theorem gives a complete, shape-independent product law, classifies every maximizer, and exhibits an unbounded separation from ordinary mutual visibility on grids. This is a natural exact theorem for a newly introduced graph invariant, not an arbitrary finite slice.

**Sources.** connected-mutual-visibility source problem context; ordinary Cartesian-product visibility literature

**Residual risks.** The scope is restricted to high-girth factors and does not address the richer low-girth product regime.

## Limitations

- The theorem treats exactly two factors and assumes both have girth at least five.
- It does not classify mixed low-girth factors or higher Cartesian powers.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
