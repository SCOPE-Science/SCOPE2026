# Independent audit — 2026-10-01

## Final claim

For every positive odd \(v\) and \(A\ge2\), the boundary coefficient of the Thue--Morse power \(m=2+2^A v\) satisfies the stated mod-\(2^{A+2}\) congruence and disagrees in 2-adic valuation with the binomial comparator; consequently Shen's conjectured exact valuation law in the \(r=1\) layer holds for every index only at \(m=2\).

## Correctness — PASS

The boundary proof is internally coherent. The dyadic convolution lemma isolates the linear term because every nonlinear convolution gains at least one extra factor of two; the comparison with \(t_2\) below \(N/2\), the endpoint parity statement, the odd-index recurrence and the paired normalized binomial terms then yield \(t_m(N-1)\equiv N(v-1)\pmod{4N}\). The comparator valuation follows from the binary digit-sum identity. I independently recomputed coefficients from \(T(x)^m=(1-x)^mT(x^2)^m\) for representative cases \((A,v)=(2,1),(2,3),(3,1),(3,3),(4,5),(5,7)\); every congruence and valuation mismatch agreed. The inspected repository verifier checks 112 \((A,v)\) pairs and all 127 odd \(u\) from 3 through 255, but the proof rather than that finite grid establishes the infinite claim.

Checked sources:
- Zhao Shen, Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts, arXiv:2609.16966v1 (2026)
- Maciej Gawron, Piotr Miska, Maciej Ulas, Arithmetic properties of coefficients of powers of the Thue--Morse product, Monatsh. Math. 185 (2018)
- Resultary record SCOPE-exact-tenth-power-thue-morse-valuations--2cde9accbbd3 (2026-09-17)
- Assigned exact-integer verifier and an independent recurrence replay on representative \((A,v)\) values

Residual risks:
- The finite verifier is auxiliary and does not certify the general theorem; the infinite conclusion rests on the displayed 2-adic proof.

## Originality — PASS

Best-of-knowledge originality passes for the uniform all-twice-odd obstruction and complete \(r=1\) slice. The earlier SCOPE tenth-power theorem covers the single exponent \(m=10\), hence is a special case rather than broader coverage. Shen's abstract states exact valuations for powers of two, for \(3\cdot2^r\) with \(r\ge2\), and a corrected formula for \(m=6\); none of those statements implies the arbitrary odd-\(u\) theorem. No stronger Resultary record was found.

### Equivalent formulations

Searches:
- Resultary query: Thue Morse series twice odd exponent boundary coefficient valuation Conjecture 6.2
- Resultary query: Thue Morse valuations powers m equals 2u odd u r=1 exact binomial valuation

Evidence:
- The assigned record was the exact hit; the strongest earlier close hit is the 2026-09-17 exact \(m=10\) valuation theorem.

Reasoning: The current theorem is equivalently a uniform explicit obstruction for every exponent with \(\nu_2(m)=1\) except \(m=2\). The prior \(m=10\) result supplies one member only.

### Broader coverage

Searches:
- Shen arXiv:2609.16966 abstract
- Gawron--Miska--Ulas 2018 power-of-two valuation theorem

Evidence:
- Shen's abstract lists the power-of-two and \(3\cdot2^r\), \(r\ge2\), exact families and a separate \(m=6\) correction; the 2018 theorem covers powers of two.

Reasoning: These families do not dominate arbitrary \(m=2u\) with odd \(u>1\); the audited theorem genuinely moves in a transverse parameter direction.

### Exact database or table

Searches:
- Resultary record SCOPE-exact-tenth-power-thue-morse-valuations--2cde9accbbd3
- Targeted searches for boundary index \(2^A-1\) and all twice-odd exponents

Evidence:
- An exact prior table/formula exists for \(m=10\) only; no database/table covering all odd \(u\) was located.

Reasoning: The known exact tenth-power row is acknowledged as covered; it does not determine the general parameter family.

### Claim versus prior implication

Searches:
- Shen arXiv:2609.16966 abstract
- Earlier exact tenth-power SCOPE finding

Evidence:
- The accessible Shen abstract gives no theorem for all twice-odd exponents, and the tenth-power theorem cannot imply arbitrary odd \(u\).

Reasoning: The uniform congruence requires the additional dyadic boundary argument. Full-text inaccessibility of the recent Shen preprint is retained as a residual risk rather than converted into a noncoverage assertion.

### Source inspections

- **Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts** (https://arxiv.org/abs/2609.16966): trigger — Same coefficients, valuation conjecture and exceptional \(m=6\) case; material read — Primary abstract and bibliographic record; full text was not retrievable in this run; method — Primary-source abstract inspection; assessment — Confirms the known families and \(m=6\) correction; insufficient for whole-document noncoverage, so full-text risk is retained.; evidence — The abstract explicitly states exact valuations for \(m=2^r\), \(m=3\cdot2^r\) with \(r\ge2\), and the corrected \(m=6\) formula.
- **Exact 2-adic valuations for the tenth power of the Thue--Morse generating function** (https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-exact-tenth-power-thue-morse-valuations--2cde9accbbd3): trigger — Earlier published SCOPE special case inside the claimed family; material read — Resultary title and scientific summary; method — Published-record semantic comparison; assessment — Covered special case \(m=10\), not broader coverage.; evidence — It gives a full exact formula only for the tenth power.

Checked sources:
- Zhao Shen, Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts, arXiv:2609.16966v1 (2026)
- Maciej Gawron, Piotr Miska, Maciej Ulas, Arithmetic properties of coefficients of powers of the Thue--Morse product, Monatsh. Math. 185 (2018)
- Resultary record SCOPE-exact-tenth-power-thue-morse-valuations--2cde9accbbd3 (2026-09-17)
- Assigned exact-integer verifier and an independent recurrence replay on representative \((A,v)\) values

Residual risks:
- Shen's full preprint text was not retrievable in this run; the abstract was inspected and confirms the power-of-two, \(3\cdot2^r\), and \(m=6\) cases.
- The source preprint is recent, so unindexed contemporaneous work remains possible.

## Scientific value — PASS

The result closes an entire infinite layer of a newly posed valuation classification and supplies an explicit violating coefficient for every excluded exponent. The uniform mod-\(4N\) congruence explains the obstruction rather than merely extending a finite census.

Checked sources:
- Zhao Shen, Powers of the Thue--Morse Series: 2-Adic Valuations and Automatic Odd Parts, arXiv:2609.16966v1 (2026)
- Maciej Gawron, Piotr Miska, Maciej Ulas, Arithmetic properties of coefficients of powers of the Thue--Morse product, Monatsh. Math. 185 (2018)
- Resultary record SCOPE-exact-tenth-power-thue-morse-valuations--2cde9accbbd3 (2026-09-17)
- Assigned exact-integer verifier and an independent recurrence replay on representative \((A,v)\) values

Residual risks:
- Shen's full preprint text was not retrievable in this run; the abstract was inspected and confirms the power-of-two, \(3\cdot2^r\), and \(m=6\) cases.
- The source preprint is recent, so unindexed contemporaneous work remains possible.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
