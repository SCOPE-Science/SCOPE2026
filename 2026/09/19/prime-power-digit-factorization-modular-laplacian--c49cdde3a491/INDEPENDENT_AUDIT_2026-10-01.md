# Independent mathematical audit — 2026-10-01

## Final claim assessed

Prime-power digit factorization in modular Laplacian dynamics

## Correctness — PASS

PASS. The proof is an infinite algebraic argument, not an extrapolation from the saved experiments. If \(A\equiv B\pmod{p^k}\), then factorization of \(A^p-B^p\) shows one additional factor of \(p\) in the quotient sum, so \(A^p\equiv B^p\pmod{p^{k+1}}\). Starting from Frobenius modulo \(p\) and iterating this lift exactly \(r-1\) times gives the special-time dilation modulo \(p^r\). Writing an arbitrary time in base \(p\) above the low block \(p^{r-1}\) then gives the stated digit product, and multiplication by the residual evolution gives the epoch identity. The repository verifier was inspected and agrees on several masks and moduli, but it is only corroborative evidence.

## Originality — PASS

PASS to the best of current knowledge, with a substantial classical-literature risk recorded. The motivating 2026 modular-Laplacian paper reports prime-modulus replication and computational prime-power signatures; its accessible statement does not give the all-mask prime-power factorization. The 2025 source proves only prime-field Frobenius revivals. Bés's 1997 paper gives a prime-power generalization of Lucas theory, Meštrović gives Lucas-type congruences modulo prime powers, and Dow develops additive cellular automata over finite commutative rings, but the inspected statements do not state the Laurent-polynomial dilation/digit/epoch theorem. Resultary search returned the audited record as the exact match. Because the lifting congruence is elementary and broad finite-ring CA literature is large, possible equivalent older formulations remain the principal originality risk.

### equivalent_formulations

Searches: prime power additive cellular automata Frobenius dilation polynomial modulo p^r; Laurent polynomial p-power congruence digit factorization

Evidence: Searches found general prime-power binomial/Lucas theory and additive-CA algebra but no identical dilation theorem.

Reasoning: Coefficient-wise Lucas congruences could encode related information, but no inspected source was shown to imply the complete operator-level digit and epoch factorization.

### broader_coverage

Searches: Additive cellular automata finite commutative rings Dow 1997; Pascal triangles modulo a prime power Bés 1997; Lucas Type Theorem Modulo Prime Powers

Evidence: These sources cover finite-ring CA structure or prime-power binomial congruences at a broader level.

Reasoning: The inspected accessible statements do not provide a theorem dominating the claimed spatial-dilation identity for arbitrary Laurent masks.

### exact_database_or_table

Searches: Resultary semantic search prime-power modular Laplacian factorization

Evidence: The exact record search returned the audited finding; no numerical database is relevant.

Reasoning: The claim is an algebraic identity, not a table value.

### claim_vs_prior_implication

Searches: arXiv:2609.20416 prime-power signatures; arXiv:2511.17389 Frobenius revivals

Evidence: The 2026 source reports computational prime-power behavior, while the 2025 source proves prime-modulus Frobenius replication.

Reasoning: Neither inspected source mechanically supplies the prime-power lift or arbitrary-time factorization.

## Scientific value — PASS

PASS. Despite the short proof, the theorem addresses a specific motivated gap: the source paper observed binary-like and ternary-like prime-power clocks computationally, while the result converts those observations into exact all-mask, all-seed, all-time algebraic laws. The arbitrary-time digit factorization is structurally stronger than a finite replication experiment and is useful for separating genuine changing-modulus phenomena from constant-modulus effects.

## Source inspections

- **Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics** — https://arxiv.org/abs/2609.20416. Material read: Primary abstract/indexed statement; full-text retrieval did not produce a verified PDF in this run. Assessment: MOTIVATING_COMPUTATIONAL_SOURCE_WITH_ACCESS_LIMITATION. Evidence: The accessible statement explicitly describes computational prime-modulus replication hierarchy and time-dependent modular effects, but not the audited prime-power theorem.
- **Frobenius Revivals in Laplacian Cellular Automata: Chaos, Replication, and Reversible Encoding** — https://arxiv.org/abs/2511.17389. Material read: Primary abstract/indexed statement. Assessment: PRIME_FIELD_PRIOR_NOT_PRIME_POWER_COVERAGE. Evidence: It derives exact returns from finite-field Frobenius at prime modulus.
- **On Pascal triangles modulo a prime power** — https://doi.org/10.1016/S0168-0072(97)85376-6. Material read: Bibliographic record and abstract describing a generalization of Lucas's theorem. Assessment: BROAD_RELATED_PRIOR. Evidence: The accessible material does not state the claimed Laurent-polynomial dilation and epoch identities.

## Limitations and residual risks

The theorem is for constant prime-power modulus. Geometric disjoint-copy conclusions additionally require support separation, and no density or entropy asymptotics are proved.

- The elementary lifting identity may occur under another name in older \(p\)-adic or finite-ring polynomial literature not retrieved here.
- The result is restricted to constant-modulus linear dynamics and does not resolve the source's changing-modulus asymptotics.

## Disposition

**passed**
