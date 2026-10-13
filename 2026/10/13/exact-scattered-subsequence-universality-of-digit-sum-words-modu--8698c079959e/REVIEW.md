# Scientific review: digit-sum scattered-subsequence universality

**Correctness — PASS.** The proof derives each aligned block as a cyclic run omitting one symbol, establishes the exact base-digit carry identity, and proves by induction the complete sequence of greedy-arch completion positions for both base parities. The all-prefix formula and discrepancy bounds follow by counting those positions. The standalone checker verifies 91,029 finite prefixes, 58,000 carry instances and 155 brute-force short-word cases, but the infinite conclusion depends on the symbolic proof.

**Originality — PASS, subject to residual bibliographic risk.** Classical generalized Thue–Morse work supplies the digit-sum word, and Schnoebelen–Veron credit Barker et al. for the greedy-arch characterization and develop general universality algorithms. Their inspected full results do not state these exact digit-sum block endpoints, parity transition, or valuation correction. Related binomial-complexity results count subsequences in fixed factors rather than require all words as scattered subsequences. Searches of relevant mathematical records and accessible primary texts disclosed no logically covering theorem. An unindexed or inaccessible equivalent computation remains possible; a negative search is not a novelty proof.

**Value — PASS.** The result completely determines a natural formal-language invariant across all prefixes of a classical automatic-word family. Its sharp even/odd dichotomy and carry-controlled exceptional arch endpoints go beyond a generic finite-word algorithm and provide an exact parameter-uniform asymptotic rate with no primality assumptions.

Closest literature: Schnoebelen–Veron, arXiv:2304.11932 (general greedy arches and universality algorithms); Starosta, arXiv:1104.2476 (classical digit-sum words); Lü–Chen–Wen–Wu, arXiv:2112.05347, and Golafshan–Rigo–Whiteland, arXiv:2412.18425 (distinct binomial-complexity invariants). Scope excludes moduli other than base plus one. The computational checks are corroboration, not an infinite proof. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
