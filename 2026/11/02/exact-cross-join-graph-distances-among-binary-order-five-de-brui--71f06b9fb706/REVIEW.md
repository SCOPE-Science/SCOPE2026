# Scientific review — exact order-five cross-join distances

## Correctness — PASS

The feedback encoding is bijective: each four-bit suffix chooses opposite outgoing bits for its two conjugate five-bit predecessors, and a single 32-state orbit is equivalent to an order-five de Bruijn cycle. Two flips are exactly one cross-join if and only if they rejoin the two cycles after the first flip; the interleaving test and an independent direct validity test agree for every proposed pair. The standalone certificate enumerates all 65536 candidates, all 120 possible two-flips at each of 2048 valid cycles, and all 2048 BFS sources. This is exhaustive finite reasoning. All distances and eccentricties are determined with integer operations and no extrapolation. The recovered degree distribution exactly matches Alhakim's previously printed table.

## Originality — PASS, with historical limits

The closest full texts are Mykkeltveit–Szmidt (2013), Sections 2–4, proving cross-join connectivity, and Alhakim (2018), Sections 2, 4–6, proving generalized connectivity/Hamiltonicity and tabulating the order-five degree distribution. Alhakim's prefix-based distance is expressly different from graph shortest-path distance, and a degree histogram does not imply the distance histogram. The earlier available internal claim on this exact graph concerns maximal cliques, not shortest paths. The search of available mathematical records found no implication of the stated diameter, eccentricities, and complete all-pairs counts. Jiang–Lin (2020) uses “diameter” for positions in a cross-join pair, but only its publisher preview and accessible portions were available; full text checking remains a residual historical-priority risk. The 2026 generation article was inspected only via available extracts. Novelty is best-knowledge, not independently certified.

## Value — PASS

The metric answers the natural operational question posed by cross-join connectivity: how many elementary, validity-preserving feedback edits are sufficient and sometimes necessary to reach another full-period order-five shift register? The exact seven-step worst-case answer, all-pairs path statistics and 48 central cycles give a complete and reusable quantitative complement to earlier connectivity and degree information. This is a complete natural finite classification at a nontrivial 2048-vertex benchmark rather than an arbitrary slice or merely new sample counts. It does not imply a corresponding bound for higher orders.

## Scientific limitations and sources

The theorem is finite and order-five only; it makes no claim about cryptographic strength, arbitrary order or random-walk mixing. Key sources: Mykkeltveit–Szmidt, IACR ePrint 2013/760; Alhakim, arXiv:1805.12059, especially Table 1; Jiang–Lin, DOI 10.1007/s10623-020-00759-2; Dąbrowski–Rachwalik–Szmidt, DOI 10.3390/math14091424. Missing full-text access for the latter two is disclosed rather than treated as proof of noncoverage.

Self-review: passed. Independent audit: not yet performed.
