# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-f728d9010e27`

## Correctness — PASS

Let \(a_p=2-2^{p-1}\). Proposition 23 condition (12) gives \(1/k_1+1/k_2<2a_p\), while AM–HM gives \((k_1+k_2)(1/k_1+1/k_2)\ge4\), hence every admissible pair has size \(2(k_1+k_2)>4/a_p\). Conversely, the source's asymptotic density of Hadamard orders provides an order \(k\) just above \(1/a_p\). For the symmetric choice \(k_1=k_2=k\), all three Proposition 23 inequalities reduce to \(1/a_p<k<2/a_p\), so the construction gives size \(4k=(1+o(1))4/a_p\). Expanding at exponent two yields \(4/a_p\sim2/((2-p)\ln2)\). The lower and upper bounds therefore match, including against asymmetric admissible pairs.

### Correctness sources

- assigned RESULT.md
- Swanepoel–Villa 2013 Proposition 23, Lemma 20, and Theorem 6 proof

### Correctness risks

- Optimality is only within the two-Hadamard construction, not for the true minimum maximal-equilateral cardinality.

## Originality — PASS

The primary 2013 construction already contains both ingredients—Proposition 23 and asymptotic density of Hadamard orders—but its Theorem 6 proof records the weaker leading constant obtained by selecting near the upper admissible endpoint. The audited theorem optimizes the full admissible pair problem, proves a matching lower bound for every pair, and halves that displayed leading constant. Exact semantic and formula searches found no later result stating this construction-optimal asymptotic.

### equivalent_formulations

Searches:
- Resultary query: maximal equilateral Hadamard Proposition 23 optimal asymptotic p to 2 constant Swanepoel Villa
- search for exact leading constant 2 / ((2-p) ln 2)
- Swanepoel–Villa Proposition 23/Theorem 6

Evidence:
- The source proof records the larger leading constant.
- The audited AM–HM lower bound applies to every admissible pair, not only symmetric choices.

Reasoning:
Equivalent formulations via the minimum size over Proposition 23 admissible pairs and the constants in Theorem 6 were compared.

### broader_coverage

Searches:
- Swanepoel–Villa Hadamard construction
- later maximal-equilateral literature in current Resultary

Evidence:
- No stronger theorem optimizing this exact construction was located.
- General bounds for maximal equilateral sets do not imply optimality of the Proposition 23 parameter choice.

Reasoning:
Broader subject literature does not mechanically determine this construction-level constant.

### exact_database_or_table

Searches:
- Hadamard-order tables versus asymptotic density lemma

Evidence:
- Finite tables of Hadamard orders are not needed: the source lemma \(H(t)/t\to1\) supplies the asymptotic upper construction.
- No exact database value establishes the lower bound.

Reasoning:
The theorem is asymptotic and is not a finite Hadamard-order table computation.

### claim_vs_prior_implication

Searches:
- source Theorem 6 bound versus audited optimization

Evidence:
- The source's recorded upper bound alone cannot imply the smaller constant.
- Condition (12), combined with AM–HM, gives a new matching lower bound on every pair, certifying optimality inside the framework.

Reasoning:
The final statement is a genuine optimization of the prior construction rather than a restatement of its existence theorem.

### source_inspections

- **Maximal Equilateral Sets** — https://doi.org/10.1007/s00454-013-9523-z. Trigger: Primary source containing Proposition 23 and Theorem 6. Material read: Accessible article text for the Hadamard construction, Lemma 20, Proposition 23 conditions, and Theorem 6 proof. Method: Primary statement and parameter-range comparison. Assessment: PARTIAL COVERAGE only. Evidence: The source provides the construction and dense Hadamard orders but records a factor-two larger leading constant in the proof of Theorem 6.
- **Current published maximal-equilateral findings** — Resultary semantic search. Trigger: Check for later optimization or stronger coverage. Material read: Ranked theorem summaries returned by the exact construction/asymptotic query. Method: Semantic theorem comparison. Assessment: No covering theorem located. Evidence: The audited result was the only exact match to the Proposition 23 optimal asymptotic.

### checked_sources

- Swanepoel–Villa 2013 primary article
- current Resultary exact semantic search
- assigned RESULT.md

### residual_risks

- A differently phrased optimization could exist in unindexed literature; no specific covering source was identified.

## Scientific value — PASS

The theorem determines the exact leading constant obtainable from a published construction and proves that no asymmetric choice within that construction can improve it. This halves the previously displayed asymptotic constant while giving a matching optimality certificate, which is a natural and reusable quantitative refinement near the Hilbert exponent.

### Value sources

- Swanepoel–Villa Proposition 23 and Theorem 6
- audited universal AM–HM lower bound

### Value risks

- It does not prove a lower bound for the actual invariant outside the two-Hadamard framework.

## Limitations

- The optimality statement is construction-specific.
- The result is asymptotic as the exponent approaches two.
- It does not close the general upper/lower asymptotic gap for maximal equilateral sets.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
