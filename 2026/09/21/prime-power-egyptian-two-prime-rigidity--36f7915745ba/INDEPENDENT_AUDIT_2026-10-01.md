# Independent mathematical audit — Two-prime rigidity for prime-power pseudoperfect and prime-power Giuga numbers

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — The two classifications follow directly from the defining Egyptian-fraction identities after controlling the smaller prime. If both primes are odd, the geometric-series bounds force the pseudoperfect sum below one and force a positive integral Giuga sum below one. With smaller prime \(2\), the pseudoperfect equation factors as \((1-q^{-b})((q-1)^{-1}-2^{-a})=0\), giving \(q=2^a+1\) with arbitrary positive \(b\). On the Giuga side, integrality forces the value to one; after clearing denominators and setting \(c=2^a-q+1\), one gets \(c(1+q+\cdots+q^{b-1})=2\), so \(c=2\), \(b=1\), and \(q=2^a-1\). An independent exact-rational replay for primes through 60 and exponents through four found zero mismatches.

Checked sources: Assigned RESULT.md and inspected verifier source; Machacek 2018 full paper; Published 20 September 2026 local-congruence result; OEIS A283423 and A286497; Independent exact-rational replay.

Residual correctness risks: The bounded replay is corroborative only; the infinite theorem is established by the displayed algebraic proof..

## Originality

**PASS** — Machacek introduced the two notions and explicitly supplied the Fermat/Mersenne constructions as sufficient families, but the inspected paper and current OEIS entries do not state their exhaustiveness on exactly two prime supports. A published 20 September 2026 result gives a broader local integrality congruence for prime-power pseudoperfect numbers and a separate three-support theorem, but it does not classify the two-support pseudoperfect slice and does not treat prime-power Giuga numbers. No earlier exact converse was located.

### Equivalent formulations

Searches/sources: Resultary query: prime-power pseudoperfect Giuga two distinct prime factors Fermat Mersenne converse; Machacek, Egyptian Fractions and Prime Power Divisors, JIS 21 (2018); OEIS A283423/A286497.

Evidence: The Resultary search returned this record as the exact two-support classification. Machacek's Proposition 5 and surrounding discussion give sufficient closure rules and the Fermat/Mersenne examples, not the two-support converse. OEIS A286497 records that \(2^a(2^a-1)\) is a prime-power Giuga family but does not assert uniqueness on two-prime support.

No equivalent complete two-support classification was found under the primary terminology or sequence terminology.

### Broader coverage

Searches/sources: Published 20 September 2026 local congruence criterion for prime-power pseudoperfect numbers; Machacek 2018 factorization conditions; mu-Sondow literature.

Evidence: The prior local-congruence theorem is broader as an integrality test, but solving its support-two congruences still requires the additional size/factorization argument and it has no Giuga analogue. The mu-Sondow reciprocal condition ranges over distinct prime divisors rather than all prime-power divisors.

No inspected broader theorem directly implies both halves of the final two-support classification.

### Exact database or table

Searches/sources: OEIS A283423 prime-power pseudoperfect numbers; OEIS A286497 prime-power Giuga numbers; Resultary exact theorem search.

Evidence: The sequence entries contain examples and sufficient families but no two-support converse. The exact published finding matched only the audited record.

The theorem is not a table recomputation; it proves the classification for unbounded exponents.

### Claim versus prior implication

Searches/sources: Compare Machacek Proposition 5 with the support-two converse; Compare the 20 September local congruence criterion with the two-support equations.

Evidence: Machacek's closure construction proves that the Fermat/Mersenne families work, but it does not exclude other two-support solutions. The local congruence theorem does not by itself state the support-two classification and does not cover the Giuga equation.

The converse exclusions are additional mathematical content rather than a special case explicitly covered by the inspected prior statements.

### Source inspections

- **Egyptian Fractions and Prime Power Divisors** — PARTIAL_PRIOR.
  Identifier: https://cs.uwaterloo.ca/journals/JIS/VOL21/Machacek/mach4.pdf
  Trigger: Original paper defining both objects and the Fermat/Mersenne constructions.
  Material read: Complete paper, including Proposition 5 and the later Fermat/Mersenne discussion.
  Method: lawful open-access full text
  Evidence: The paper proves sufficient constructions and sequence inclusions but does not state the two-prime-support converse.
- **Local congruence criterion and three-support rigidity for prime power pseudoperfect numbers** — BROADER_INGREDIENT_NOT_COVERING.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-prime-power-pseudoperfect-local-rigidity--e2b81fad1a6a
  Trigger: Potential stronger published SCOPE coverage one day earlier.
  Material read: Complete published RESULT.md.
  Method: public full text
  Evidence: It gives a local integrality criterion for prime-power pseudoperfect numbers and a three-support slice, but no support-two classification and no prime-power Giuga theorem.
- **OEIS A286497** — DATABASE_CONTEXT.
  Identifier: https://oeis.org/A286497
  Trigger: Current database for prime-power Giuga numbers.
  Material read: Complete public sequence entry and comments.
  Method: public database
  Evidence: The Mersenne family is recorded as sufficient; no support-two converse is stated.

Residual originality risks:
- The final argument is elementary enough that an equivalent support-two observation could exist in poorly indexed problem or sequence commentary.

## Scientific value

**PASS** — Exactly two distinct prime factors is the first nontrivial support size for these Egyptian-fraction classes. The result converts previously sufficient Fermat/Mersenne constructions into complete converses, identifies the asymmetric freedom of the odd-prime exponent, and locates the first possible support size for counterexamples to Machacek's A073935 inclusion.

Residual value risks: The theorem does not address support size at least three..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier review evidence remains separately identified and is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
