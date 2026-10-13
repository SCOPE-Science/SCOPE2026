# Scientific review of the three-way last-place ordering result

## Correctness

**PASS.** The three-player dynamics can be coupled to independent gamma completion times by Poisson thinning. Exact Laplace transforms and the Erlang finite-sum identity yield both last-place formulas without asymptotic approximation. Subtraction gives exact expressions for both consecutive ordering gaps. The program `check.py` verifies the entire finite range \(2\le n\le499\) in rational arithmetic and cross-checks the closed forms against independent integral expansions for \(2\le n\le32\). For all \(n\ge500\), transparent Taylor bounds and logarithmic estimates yield lower margins strictly exceeding \(1/200\) and \(1/100\), respectively. The finite and infinite pieces exhaust the quantifiers. The code was executed with no failed assertions. No interpretation of a numerical experiment as an infinite proof is needed.

## Originality

**PASS, subject to residual priority uncertainty.** Leobacher and Steinicke, arXiv:2605.21424v1, Proposition 30 and Section 6, are the nearest full-text source. They establish a general probability representation, report a numerical ordering at goals \((1,2,3)\), and exhibit counterexamples to general monotonicity, but do not prove uniform gaps for the full \((1,2,n)\) family. Their asymptotic results do not settle each finite integer. Published mathematical-record searches using gamma-rank, Erlang, last-player, and equivalent dice-race terms found no directly covering theorem. A 2026 submitted dice-game manuscript cited in the lead paper was not available for full comparison; a more general unindexed gamma-rank result remains possible.

## Value

**PASS.** For three strictly ordered goals the middle player need not be middle-ranked by last-place probability, so goal ordering is a genuine question rather than a consequence of shape ordering. The first nontrivial fixed pair \((1,2)\) is a natural infinite subfamily of the source's open-ended last-place comparison problem. The theorem resolves the entire third-goal range, identifies the exact tie boundary, and proves parameter-independent quantitative separations. The result does not extend to arbitrary triples, and its certified margins are not claimed optimal.

Self-review: passed. Independent audit: not yet performed.
