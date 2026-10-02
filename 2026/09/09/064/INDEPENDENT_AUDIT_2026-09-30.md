# Independent audit — SCOPE-20260909-064

Date: 2026-09-30 UTC

## Final claim

There are exactly 352 shifted 3-uniform hypergraphs on seven labelled vertices, exactly 68 are tight-\(C_5^{(3)}\)-free, those 68 are pairwise nonisomorphic under all vertex permutations, and the unique shifted-free extremal has 16 edges.

## Correctness

**PASS.** A fresh independent enumerator, not the package scripts, generated predecessor-closed subsets of the 35 triples and found exactly 352 ideals. Independently generated tight-cycle edge sets gave 252 forbidden masks, leaving exactly 68 free ideals with the stated edge-count distribution. Canonicalization over all 5040 vertex permutations produced 68 distinct canonical forms. The unique 16-edge extremal is exactly all 15 triples through vertex 0 together with \(\{1,2,3\}\). These values agree with the package census and verifier source.

Residual risk: The classification is a finite computational proof rather than a structural hand classification, though the state space is small enough to be exhaustively regenerated.

## Originality

**PASS.** A semantic published-results search for the exact seven-vertex shifted tight-cycle census found only this record. Kamčev–Letzter–Pokrovskiy concerns asymptotic Turán density and leaves the tight 5-cycle case open; it does not contain this finite shifted classification. A later published result found by semantic search gives the unrestricted six-vertex census, not this seven-vertex shifted table.

Equivalent formulations: Searched seven-vertex shifted/left-compressed 3-graphs, tight \(C_5^{(3)}\), the counts 352 and 68, and the 16-edge extremal; no external equivalent statement was found.

Broader coverage: Asymptotic tight-cycle Turán results and the unrestricted six-vertex exact census do not imply the seven-vertex shifted isomorphism classification.

Exact database or table: No external exact table of the 352 ideals or 68 shifted-free classes was located.

Claim versus prior implication: The known lower-bound construction and large-cycle Turán theorem do not determine these finite shifted counts or the unique 16-edge member.

Residual risk: A small unpublished computational table could have circulated outside indexed literature.

## Value

**PASS.** The tight 5-cycle is a named open extremal configuration, and shifted families form a natural finite order-ideal slice. An exact seven-vertex classification and unique shifted extremal provide reusable small-order reference data, even though ordinary shifting is not asserted to preserve tight-\(C_5\)-freeness.

Residual risk: Because the forbidden property is not preserved by naive shifting, the census alone does not reduce or solve the unrestricted Turán problem.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/064/RESULT.md — Full claim and limitations inspected from the source blob.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/064/artifacts/shifted_census_n7.py — Generation and forbidden-mask source inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/09/064/artifacts/verify_census.py — Independent package verifier source inspected; fresh audit used a separately written enumeration instead.
- https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE064 — Exact semantic search; this record was the direct match.
- https://github.com/Resultary/2026/tree/main/2026/9/9/SCOPE086 — Related unrestricted six-vertex tight-\(C_5^{(3)}\)-free census inspected as a neighboring but non-covering result.
- https://arxiv.org/abs/2209.08134 — Kamčev–Letzter–Pokrovskiy abstract inspected; it states the \(C_5^{(3)}\) lower bound/conjecture and proves the density for sufficiently large cycle lengths not divisible by three, not this finite census.

## Disposition

**PASS.** Correctness, originality and value all pass the review bar.
