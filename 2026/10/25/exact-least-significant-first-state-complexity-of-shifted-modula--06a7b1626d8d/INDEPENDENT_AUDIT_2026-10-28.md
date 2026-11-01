# Independent mathematical audit

## correctness

PASS

Reading k digits with integer u gives residual n -> nu_b(c+1+u+b^k n) mod m. If b^k does not divide t=c+1+u, the output is constant nu_b(t) mod m; otherwise the unique residue u modulo b^k gives nonconstant V_{ceil((c+1)/b^k),k mod m}. The shift decreases strictly through depths 0..L-1 then equals one and phases cycle modulo m. The other digits land in m constant states. Distinct nonconstant shifts can be separated with suffix inputs b^r-s and b^(r+1)-s using nu_b(t-s) fixed, valid for any composite b too; phase variants and constants are pairwise different. This proves exactly L+2m states, all-word conventions included. My independent Moore minimizer constructed and minimized reachable automata for 700 parameter triples and matched the formula, corroborating—not substituting for—the residual proof.

## originality

PASS

Best-of-knowledge PASS, bounded. Zantema–Bosma (Information and Computation 2022) gives general digit-order state-complexity theory, tail bounds and arithmetic subsequence bounds, but not the exact minimal state count and chain/cycle structure for this shifted valuation family. Moradi–Rampersad–Shallit (arXiv:2512.10017) addresses linear subsequences with general bounds; Moradi–Popoli–Shallit–Vukusic (arXiv:2603.18858) treats shifts of Fibonacci words in Zeckendorf numeration, a different representation and sequence. Other Resultary period-doubling records concern string attractors, not DFAO minimality. A previously unnoticed direct period-doubling kernel computation remains possible.

## value

PASS

PASS: fully solves a natural three-parameter DFAO minimal-state problem with exact preperiod length, phase cycle and constant-state structure, rather than a generic polynomial upper bound. Sharp power-of-b jumps after each shift threshold and applicability to composite b make the explicit law useful for automata complexity and exact algorithm design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
