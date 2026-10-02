# Independent audit — 2026-10-01

## Final claim

For every odd prime \(p\equiv3\pmod4\) and every \(k\ge1\), the cyclotomic polynomial \(\Phi_{2p^k}\) has exactly one relative tau-number, namely \(1\); the same uniqueness holds for every positive power of that polynomial.

## Correctness — PASS

If \(\tau(n)\) divides \(\Phi_{2p^k}(n)\), parity makes \(\tau(n)\) odd and hence \(n\) a square. A common prime divisor of \(n\) and \(\tau(n)\) is impossible because the cyclotomic value is one modulo that prime. If the parameter prime \(p\) divided \(\tau(n)\), the cyclotomic reduction modulo \(p\) would force \(n\equiv-1\pmod p\), contradicting that \(n\) is a square when \(p\equiv3\pmod4\). Every other prime \(\ell\mid\tau(n)\) gives exact order \(2p^k\) for \(n\) modulo \(\ell\). This makes every exponent in \(n\) divisible by \(2p^k\); iterating the order-of-a-power formula forces divisibility by arbitrarily high powers and hence \(n=1\). The same prime-divisor argument applies to positive powers of the cyclotomic polynomial. A fresh bounded search over representative prime powers found no nontrivial counterexample.

Checked sources:
- M. Abel, H. Lauer, E. Redi, About the number of tau-numbers relative to polynomials with integer coefficients, ACUTM 25 (2021), full text inspected.
- E.-M. Muttika, Results about tau-numbers relative to polynomials, University of Tartu thesis (2023), full text inspected.
- Published-record semantic search for relative tau-numbers of cyclotomic polynomials and the polynomial \(x^2-x+1\).

Residual risks:
- The finite search is only a consistency check; the infinite statement follows from the order bootstrap.

## Originality — PASS

Best-of-knowledge originality passes. Abel--Lauer--Redi explicitly report only a computation through one hundred million for \(x^2-x+1\) and leave the type-II behavior open. Muttika's later thesis still describes the general problem as unresolved, while flagging an unidentified article then in preparation. No identified indexed source covering the present cyclotomic family was found.

### Equivalent formulations

Searches:
- Resultary semantic query: tau numbers relative to cyclotomic Phi doubled odd prime power unique n equals one
- Searches for the specialization \(\tau(n)\mid n^2-n+1\)

Evidence:
- The exact published-record hit was the assigned finding.
- The 2021 paper records the quadratic specialization only as a finite computation.

Reasoning: The quadratic divisibility problem is exactly the \(p=3,k=1\) member, so any prior proof there would cover a special case; no such proof was located.

### Broader coverage

Searches:
- Abel--Lauer--Redi 2021 type-II classification discussion
- Muttika 2023 thesis

Evidence:
- The 2021 theorem gives infinitely many relative tau-numbers when \(|Q(0)Q(1)|\ne1\), whereas the current family lies in the complementary type-II regime.
- The thesis continues to treat type-II behavior as unresolved.

Reasoning: The known general theorem applies to the opposite constant-term regime and therefore does not dominate this uniqueness theorem.

### Exact database or table

Searches:
- Abel--Lauer--Redi computational table through one hundred million
- Package consistency search through one million for several parameter pairs

Evidence:
- The older table found no nontrivial solution for the quadratic example but did not prove impossibility.
- The package computation similarly supplies only bounded corroboration.

Reasoning: Finite nonexistence tables cannot imply the universal uniqueness statement.

### Claim versus prior implication

Searches:
- 2021 finite computation versus multiplicative-order bootstrap
- 2023 thesis open-problem discussion

Evidence:
- Neither source supplies the infinite order-bootstrap argument.
- The unnamed in-preparation article is too unspecified to establish actual mathematical coverage.

Reasoning: The final claim is not mechanically implied by the identified literature; the unidentified source remains an explicit residual risk rather than fabricated coverage or noncoverage.

### Source inspections

- **About the number of tau-numbers relative to polynomials with integer coefficients** — Does not cover the theorem; the quadratic case is computational only. Material read: Full primary article, including the type-II computation and open-problem discussion. Evidence: The article reports no nontrivial relative tau-number for \(x^2-x+1\) up to one hundred million and does not prove uniqueness.
- **Results about tau-numbers relative to polynomials** — Confirms continued open status but introduces a material unidentified-source risk. Material read: Full thesis, including its introductory literature note. Evidence: The thesis says an article in preparation described some class with only the relative tau-number one, without identifying the class or publication.

Checked sources:
- M. Abel, H. Lauer, E. Redi, About the number of tau-numbers relative to polynomials with integer coefficients, ACUTM 25 (2021), full text inspected.
- E.-M. Muttika, Results about tau-numbers relative to polynomials, University of Tartu thesis (2023), full text inspected.
- Published-record semantic search for relative tau-numbers of cyclotomic polynomials and the polynomial \(x^2-x+1\).

Residual risks:
- The 2023 thesis mentions, without title, authors, identifier, or class description, an article then in preparation about a class of polynomials having only the relative tau-number one; possible overlap cannot be excluded.
- No claim is made for primes congruent to one modulo four.

## Scientific value — PASS

The theorem upgrades a prominently reported finite computation for \(x^2-x+1\) to a proof and embeds it in an infinite cyclotomic family. The multiplicative-order bootstrap is a structural mechanism that can guide further type-II classification.

Checked sources:
- M. Abel, H. Lauer, E. Redi, About the number of tau-numbers relative to polynomials with integer coefficients, ACUTM 25 (2021), full text inspected.
- E.-M. Muttika, Results about tau-numbers relative to polynomials, University of Tartu thesis (2023), full text inspected.
- Published-record semantic search for relative tau-numbers of cyclotomic polynomials and the polynomial \(x^2-x+1\).

Residual risks:
- The 2023 thesis mentions, without title, authors, identifier, or class description, an article then in preparation about a class of polynomials having only the relative tau-number one; possible overlap cannot be excluded.
- No claim is made for primes congruent to one modulo four.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
