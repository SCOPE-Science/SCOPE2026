# Scientific review

**Correctness — PASS.** The factorwise abundance bound excludes up to four prime factors and forces each five-prime candidate into the form \(105st\) with \(s\in\{11,13,17,19\}\), and \(t\) in one of four explicit finite intervals. Direct complement-pair parametrization is bijective. The independently implemented meet-in-the-middle and bitset subset-sum tests both reject all \(87\) cases, and the explicit omitted-pair witness for \(937365\) is verified by direct divisor summation. Computation does not replace the proof that these are all possible five-prime inputs.

**Originality — PASS with literature-priority risk.** Wang--Zelinsky (2026, arXiv:2609.36068v1) provide the six-factor example, restrictions, and computational tables but not the sharp rank-exclusion theorem. McCormack--Zelinsky (2023/2024, arXiv:2312.11661) define the property and establish congruence obstructions, not the full five-factor obstruction. OEIS A334405 gives a general exact coefficient test but no unbounded exclusion of five prime factors. Published related findings about at most three total prime factors and about even two-prime families do not imply the five-distinct-prime odd squarefree result. An undiscovered older proof or implicit exhaustive calculation is the remaining priority risk.

**Mathematical value — PASS.** The integer \(937365\) motivates a natural extremal question: how few primes can an odd squarefree example have? The sharp answer six resolves the complete first conceivable support layer, using a structural abundancy reduction and finite, fully reproducible complementary-divisor certificates. This is not a claim that the known six-prime witness or the general subset-sum algorithm was newly discovered.

**Limits:** The theorem is confined to odd squarefree integers; the five-prime exclusion uses exact finite exhaustive checking. Independent scientific auditing and bibliographic priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
