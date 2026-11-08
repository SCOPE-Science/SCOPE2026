# Self-review: cyclotomic second-order binomid classification

## Correctness — PASS

The characteristic roots are distinct and the three periodic weights \((1,t,-(t+1))\) sum to zero; the recurrence solution is exact for all indices. The generalized coefficient factors as \(q^{k(n-k)}t^{E_2}(-(t+1))^{E_0}\). The zero-class count is never negative, while the two-class count can be negative only by one unit, and only when \(k\ge2\) and \(n-k\ge2\). Hence every possible denominator \(t\) is canceled if and only if \(t\mid q^4\), as \({4\brack2}_f\) witnesses. Index divisibility reduces to the residue class of the divisor index, with \(f_2\mid f_4\) forcing precisely \(t\mid q^2\). The finite checker executes independently using full integer-product arithmetic; no finite experiment is used to prove infinite integrality.

## Originality — PASS within inspected evidence

Shapiro's primary 2023 text, Section 4.4 Question 27, poses the second-order binomid-versus-divisibility implication explicitly. Its proved Lucas/zero-initial and divisible-sequence cases cannot imply this construction, whose initial term is nonzero and divisibility fails. Caalim and Tanaka 2024/2025 characterize binomid *indices* and lexicographically minimal extensions for positive sequences; their stated results do not provide this signed order-two counterexample or the sharp constraints on the cyclotomic parameters. Koshkin 2022 concerns *divisibility* recurrences and likewise cannot imply binomid nondivisibility. Related accessible recurrence claims cover repeated-root, exactly eventually periodic, or companion Lucas cases, and a nonrecurrent binomid example; their hypotheses exclude this growing, distinct-root, order-two family. Searches of the mathematical index, related expressions, and publicly indexed mathematical records found no explicit equivalent claim. Residual risk: unindexed equivalent work and generic valuation principles may provide a shorter proof; absence from searches is not a proof of novelty.

## Mathematical value — PASS

A published order-two recurrence question asks whether binomid integrality forces index divisibility. This result gives a negative answer through infinitely many explicit recurrences, and classifies a natural two-parameter cyclotomic slice exactly. The thresholds are sharp and distinct: a fourth-degree cancellation makes the generalized coefficients integral even though the second-degree test for divisibility fails. The result does not claim pyramid-level binomid integrality, positivity of all terms, or a complete classification of every order-two recurrence.

Self-review: passed. Independent audit: not yet performed.
