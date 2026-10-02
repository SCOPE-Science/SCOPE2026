# Independent scientific audit — Exact Sylvester--Gallai dimension of K_{2,n}

Audit date: 2026-10-01 (UTC) UTC.

Disposition: **PASSED**.

## Correctness

**PASS** — The incidence-graph proof reconstructs cleanly. Off the x-y spine, each B-vertex defines one edge between its x-line and y-line; this graph is simple and every line-vertex has degree at least two because each graph edge must lie on a special line with a third configuration point. Hence every incidence component contains at least four edges. Adjacency propagates all points of a component into one affine plane through the common spine, so c components span dimension at most c+1 and 4c<=|B*|. The four-intersection page gadget attains one new independent direction per block of four, with leftover vertices placed on the spine. All small-n boundary cases follow.

## Originality

**PASS** — Dvir introduces SGdim and explicitly treats complete bipartite graphs only at asymptotic/order level in Observation 2.5: for K_{m,s} it records an Omega(m/s) lower bound from the book construction and an asymptotically matching upper bound from the quantitative Sylvester--Gallai theorem. Resultary search for the exact formula and K_{n,2} alias returned only this record. No inspected stronger theorem implies the exact floor term.

### Equivalent formulations

Both bipartition orientations and complete-bipartite aliases were searched.

Searches: Resultary: exact Sylvester Gallai dimension K_{2,n}; Resultary: SGdim K_{n,2} complete bipartite.

Evidence: Only the audited exact formula was returned as a direct match.

### Broader coverage

No inspected broader result fixes the exact coefficient and floor term for the fixed side of size two.

Searches: Dvir arXiv:2608.15967, Observation 2.5.

Evidence: The primary full text states only an Omega(m/s) lower bound and an asymptotically matching upper bound for complete bipartite K_{m,s}.

### Exact database or table

No exact database or table mechanically covers the family.

Searches: Resultary semantic search; arXiv search for SGdim complete bipartite.

Evidence: The claim is a symbolic all-n theorem for a newly defined parameter, not a finite catalog value.

### Claim versus prior implication

The exact formula requires the min-degree-two incidence graph argument and is not a direct numerical substitution into a prior exact theorem.

Searches: Dvir arXiv:2608.15967, Observation 2.5.

Evidence: The source gives asymptotic complete-bipartite bounds rather than an exact K_{2,n} statement or the incidence-component equality proof.

### Source inspections

- **The Sylvester--Gallai dimension of graphs** (https://arxiv.org/abs/2608.15967): Assessment: the source gives only asymptotic complete-bipartite bounds and does not state 1+floor(n/4). Material read: complete primary full text pages 1--12, especially Observation 2.5 and the Section 2 book constructions. Evidence: Observation 2.5 says Lemma 2.3 gives SG-dim(K_{m,s})=Omega(m/s) while Theorem 1.2 gives an asymptotically matching upper bound.

Checked sources: Dvir arXiv:2608.15967 full text, Observation 2.5; Resultary semantic searches for K_{2,n} and K_{n,2} exact SGdim.

Residual risks: The parameter is only weeks old; an unindexed follow-up could overlap, so originality remains explicitly best-of-knowledge.

## Scientific value

**PASS** — K_{2,n} is a canonical first complete-bipartite family for a newly introduced graph parameter. Replacing asymptotic bounds by an exact all-n formula with a transparent incidence-page mechanism is a natural structural result, not an arbitrary finite computation.

## Final claim

For every integer n>=1, the Sylvester--Gallai dimension of K_{2,n} is exactly 1+floor(n/4).

This audit is a scientific assessment of the claim and supplied evidence. It is not peer review, formal verification, or a guarantee of first discovery.
