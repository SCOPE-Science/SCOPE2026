# Independent audit — 2026-10-01

## Final claim

Prime-square local rigidity holds for the stated 31 residual exponents of the Lebesgue--Nagell equation: every integer solution has the locally trivial y residue and the corresponding x residue modulo the prime square.

## Correctness — PASS

The Thue polynomial reduces modulo p to one affine residue line, and every first partial derivative is divisible by p, so its value modulo p squared is constant on residue classes modulo p. An independent exact replay over all 84 residual primes reproduced exactly the stated 31 unique classes. The Katz--Pratt normalization and congruence theorems then convert that unique class into the claimed congruences for x and y, including the prime-square upgrade for x.

Checked sources:
- Katz and Pratt, On the Lebesgue--Nagell equation x^2-2=y^p, Ramanujan Journal 69 (2026), arXiv:2507.12397v3.
- Chen, On the equations a^2-2b^6=c^p and a^2-2=c^p, LMS Journal of Computation and Mathematics 15 (2012).
- Repository verifier verify.py and verification.txt; the 84 residual exponents were also independently replayed with exact quadratic-ring arithmetic.
- Published Resultary semantic search for Lebesgue--Nagell local triviality, prime-square congruences, and the Katz--Pratt Thue equation.

Residual risks:
- The Katz--Pratt source was revised recently, so near-simultaneous follow-up work remains possible.
- The theorem is local and covers 31 residual exponents; it does not rule out nontrivial global solutions.

## Originality — PASS

Best-of-knowledge originality passes. Katz--Pratt explicitly formulate local triviality as Conjecture 8.1 and prove only weaker general restrictions; their current full text does not identify the 31 unique prime-square branches. The published-record search returned no earlier exact statement.

### Equivalent formulations

Searches:
- Resultary query: Lebesgue Nagell x^2-2=y^p local triviality p^2 Katz Pratt Thue 31 primes
- Katz--Pratt arXiv:2507.12397v3, Sections 5, 7, 8, and 10

Evidence:
- The exact Resultary match is the assigned finding.
- Conjecture 8.1 remains a conjecture in the residual range; Proposition 8.2 gives only nonvanishing modulo p.

Reasoning: Equivalent formulations through the Thue residue class, local triviality, and the prime-square x congruence were compared.

### Broader coverage

Searches:
- Katz--Pratt Theorems 2.3, 5.3, 7.7, and 10.1
- Chen 2012

Evidence:
- These theorems supply normalization and downstream congruence implications but do not supply the 31-prime residue collapse.
- Chen resolves different congruence classes globally.

Reasoning: No inspected broader theorem mechanically implies the finite local classification.

### Exact database or table

Searches:
- Katz--Pratt computations and local-count theorem
- Resultary exact-topic search

Evidence:
- No prior exact table of the 31 unique prime-square branches was located.
- The package enumeration was independently reproduced but is correctness evidence, not novelty evidence.

Reasoning: The finite certificate is attached to a proved reduction, not inferred from search absence.

### Claim versus prior implication

Searches:
- Katz--Pratt Conjecture 8.1 versus the prime-square rigidity lemma
- Katz--Pratt Theorem 2.3

Evidence:
- The prime-square theorem upgrades x only after the local y congruence is known.
- The new modulo-p-squared Thue test supplies that missing implication on 31 exponents.

Reasoning: The final claim is not a corollary of the cited source without the new residue-class argument.

### Source inspections

- **On the Lebesgue--Nagell equation x^2-2=y^p** — Highly relevant but not covering the 31-prime classification. Material read: Current full arXiv v3 sections containing Theorems 2.3, 5.3, 7.7, Conjecture 8.1, Proposition 8.2, and Theorem 10.1. Method: Primary full-text inspection. Evidence: The paper leaves local triviality conjectural in the residual range.

Checked sources:
- Katz and Pratt, On the Lebesgue--Nagell equation x^2-2=y^p, Ramanujan Journal 69 (2026), arXiv:2507.12397v3.
- Chen, On the equations a^2-2b^6=c^p and a^2-2=c^p, LMS Journal of Computation and Mathematics 15 (2012).
- Repository verifier verify.py and verification.txt; the 84 residual exponents were also independently replayed with exact quadratic-ring arithmetic.
- Published Resultary semantic search for Lebesgue--Nagell local triviality, prime-square congruences, and the Katz--Pratt Thue equation.

Residual risks:
- The Katz--Pratt source was revised recently, so near-simultaneous follow-up work remains possible.
- The theorem is local and covers 31 residual exponents; it does not rule out nontrivial global solutions.

## Scientific value — PASS

The result resolves a named local-triviality conjecture for 31 of the 84 exponents left by the global reductions and gives a reusable exact prime-square criterion. The finite list is mathematically motivated by the residual problem rather than an arbitrary census.

Checked sources:
- Katz and Pratt, On the Lebesgue--Nagell equation x^2-2=y^p, Ramanujan Journal 69 (2026), arXiv:2507.12397v3.
- Chen, On the equations a^2-2b^6=c^p and a^2-2=c^p, LMS Journal of Computation and Mathematics 15 (2012).
- Repository verifier verify.py and verification.txt; the 84 residual exponents were also independently replayed with exact quadratic-ring arithmetic.
- Published Resultary semantic search for Lebesgue--Nagell local triviality, prime-square congruences, and the Katz--Pratt Thue equation.

Residual risks:
- The Katz--Pratt source was revised recently, so near-simultaneous follow-up work remains possible.
- The theorem is local and covers 31 residual exponents; it does not rule out nontrivial global solutions.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
