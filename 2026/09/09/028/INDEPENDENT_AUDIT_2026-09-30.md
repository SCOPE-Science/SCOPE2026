# Independent mathematical audit — 2026-09-30

## Final claim
No residue class modulo 343, and no residue class modulo 49, vanishes identically modulo 49 for the assigned d_4 series; in particular the known step-343 modulo-7 residues 39, 235, and 284 do not uniformly lift modulo 49.

## Correctness — PASS
A fresh exact integer-series computation of f2^4/f1^13 through index 1000 reproduced the initial coefficients 1,13,100,585,2862 and the key residues: d4(39)=14, d4(235)=21, d4(284)=0, d4(627)=0, d4(970)=14 modulo 49. Scanning the exact coefficients found a nonzero modulo-49 witness in every residue class modulo 343 by 970 and in every residue class modulo 49 by 72; the three stated diagonal witnesses are minimal in their classes.
Checked sources: Fresh exact Euler-product/series-division computation; Assigned RESULT.md and artifact definitions at 92c7f26b45ce94be6cda0eafed44298c598d7b47
Residual risks: The conclusion is only about the stated step sizes; finer progressions such as modulus 2401 remain open.

## Originality — PASS
Best-of-knowledge originality passes. The prior theorem gives only modulo-7 progressions for d4 at step 343; the checked later 7-power tower paper concerns d3 and d5, not a modulo-49 d4 lift. The explicit universal non-lift certificate is therefore not covered by those sources.

### Equivalent formulations
Searches: d4 elongated plane partition diamonds mod 49 343 residues lift congruence; d4 343n+39 235 284 mod 49
Evidence: Resultary's exact-topic hit is this record; no equivalent d4 modulo-49 non-lift result was returned.
Reasoning: The search compared failure of uniform congruences, not only the individual witness numbers.

### Broader coverage
Searches: Baruah–Das–Talukdar arXiv:2207.06264 Theorem 6.1; Chen–Xu–Yin arXiv:2508.09723
Evidence: Baruah–Das–Talukdar equation (6.8) gives d4 modulo 7 for residues 39,235,284 at step 343; its neighboring modulo-49 statement is for d3. Chen–Xu–Yin's 7-power towers are for d3 and d5.
Reasoning: Neither broader source implies the negative d4 modulo-49 certificate.

### Exact database or table
Searches: d4 elongated plane partition diamonds mod 49 343 residues lift congruence; d4 elongated partition diamonds coefficients modulo 49
Evidence: No checked coefficient/congruence table supplied all 343 minimal residue-class witnesses.
Reasoning: Search absence is best-of-knowledge evidence only.

### Claim versus prior implication
Searches: Baruah–Das–Talukdar theorem 6.1(6.8); 7-power tower literature
Evidence: A modulo-7 zero progression does not imply either a modulo-49 lift or failure of that lift; the latter needs an explicit nonzero modulo-49 term in each target class.
Reasoning: The fresh witnesses decisively answer a natural next lifting question not fixed by the prior theorem.

### Source inspections
- **Congruences for k-elongated plane partition diamonds** (https://arxiv.org/abs/2207.06264): Confirms d4 step-343 congruences only modulo 7; the adjacent modulo-49 formula applies to d3. Material read: Full-text Theorem 6.1 around equations (6.7)–(6.8). Evidence: Equation (6.8) lists residues 39,235,284 for d4 modulo 7.
- **Congruences modulo powers of 7 for k-elongated plane partitions** (https://arxiv.org/abs/2508.09723): The advertised infinite towers concern d3 and d5, not d4. Material read: Abstract/result summary identifying tower families. Evidence: No d4 modulo-49 tower is stated in the inspected result summary.

Checked sources: Resultary published-record search; Baruah–Das–Talukdar arXiv:2207.06264; Chen–Xu–Yin arXiv:2508.09723; da Silva–Hirschhorn–Sellers arXiv:2112.06328
Residual risks: An unindexed d4 modulo-49 computation could exist. The result does not address non-diagonal or finer-step lifts.

## Scientific value — PASS
The non-lift directly tests the next prime-power strengthening of a published modulo-7 family. Universal minimal witnesses at the same natural step eliminate the most immediate tower mechanism and give concrete boundary data for future 7-adic work.
Checked sources: Baruah–Das–Talukdar arXiv:2207.06264; Chen–Xu–Yin arXiv:2508.09723
Residual risks: It is a sharp negative at one step, not an infinite nonexistence theorem.

## Limitations
- Only the stated step sizes and modulus 49 are excluded.
- Finer or non-diagonal progressions remain open.
- Originality is best-of-knowledge after targeted primary-literature and Resultary checks.

## Disposition
passed
