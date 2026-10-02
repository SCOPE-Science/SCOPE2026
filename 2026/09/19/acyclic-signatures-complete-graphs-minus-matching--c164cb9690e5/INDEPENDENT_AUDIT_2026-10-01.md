# Scientific audit — 2026-10-01

## Final claim

For a complete graph with \(r\) disjoint matching edges deleted, the acyclic signature has the stated factorial closed form; in particular every cocktail-party graph \(K_{2r}-M_r\) with \(r\ge2\) has a non-Hamiltonian graph of acyclic orientations.

## Correctness — PASS

The signed orientation algebra is well defined because adjacent incomparable vertices in a linear extension lie in one multipartite part and commute. Sink-set inclusion-exclusion gives \(FC=1\). Splitting the independent-set series into even central terms and odd anticommuting terms yields the stated rational identity; coefficient extraction reduces to ordered perfect matchings and gives \((-1)^k(2k)!\) on every selected \(2k\)-set. This produces the factorial formula in all s cases. An independent brute-force implementation, separate from the committed verifier, reproduced all 23 parameter pairs with \(2\le n\le8\), including signature 24 for \(K_8\) minus a perfect matching.

## Originality — PASS

No equivalent or stronger signed evaluation was found. The closest sources give either the general parity obstruction or unsigned complete-multipartite enumeration, neither of which implies the factorial signature.

The structured originality comparison records equivalent formulations, broader coverage, exact database/table checks, claim-versus-prior implication, source inspections, checked sources and residual risks in the accompanying JSON file.

## Scientific value — PASS

The formula gives an exact infinite family of large parity imbalances and converts them into explicit non-Hamiltonicity results for cocktail-party and near-cocktail acyclic-orientation graphs. It is a natural structural evaluation, not an arbitrary finite census.

## Disposition

PASSED. This is a mathematical assessment of the stated claim, not a formal-proof certificate.
