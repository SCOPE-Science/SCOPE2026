# Independent audit — 2026-10-01

## Final claim

In the two-iid-block Rademacher class the exact bounded-stopping bias is the ordinary simple-walk maximum, systematic linear-code constructions attain it under high wise-independence, and fixed positive independence fractions below one half still permit square-root worst-case stopping bias.

## Correctness — PASS

The two-block envelope is pathwise: any chosen second-block partial sum lies between that path's minimum and maximum, so the expected stopped sum is bounded by the ordinary simple-walk maximum even for a non-stopping random index. The linear-character construction makes the second block iid while measurable from the first, and the least linear relation weight is exactly the claimed wise-independence threshold. The random injective-map estimate yields linear independence order below one half, while Narayanan's four-wise maximal second-moment theorem gives the matching square-root upper order. Independent exact checks reproduced the walk-maximum formula through length eight and the simplex relation distance sixteen at total length thirty-one.

Checked sources:
- Narayanan, Three-wise independent random walks can be slightly unbounded, Random Structures and Algorithms 61 (2022), arXiv:1807.04910, full arXiv text.
- Benjamini, Kozma, and Romik, Random walks with k-wise independent increments, Electronic Communications in Probability 11 (2006).
- Repository verifier verify_stopping_bias.py and VERIFICATION.txt; the walk-maximum formula and a simplex relation distance were independently checked.
- Published Resultary semantic search for k-wise independent Rademacher stopping bias, linear codes, and bounded stopping.

Residual risks:
- Equivalent older formulations may exist in orthogonal-array, resilient-function, pseudorandom-stopping, or older optimal-stopping terminology.
- The exact constant is for the two-iid-block subclass; the unrestricted fixed-fraction theorem is only order-sharp.

## Originality — PASS

Best-of-knowledge originality passes. Narayanan's full paper gives the maximal-displacement upper theorem used here, but it does not state the exact two-iid-block stopped-sum envelope, the predictable-tail systematic-code extremizers, or the fixed-positive-fraction bounded-stopping theorem. Resultary returned only the assigned exact-topic record.

### Equivalent formulations

Searches:
- Resultary query: k-wise independent Rademacher stopping time bounded stopping bias sqrt N linear codes
- Search under pairwise-independent stopping, orthogonal arrays, and random-walk maximal inequalities

Evidence:
- The assigned record is the only exact published-result hit.
- The nearest primary literature studies maxima of partial sums, not expected stopped sums selected after a revealing block.

Reasoning: Equivalent formulations through linear characters, predictable tails, and bounded stopping were compared.

### Broader coverage

Searches:
- Narayanan arXiv:1807.04910 full text
- Benjamini--Kozma--Romik 2006

Evidence:
- Narayanan proves strong maximal inequalities under four-wise independence and larger lower behavior at lower independence.
- Those results do not characterize the audited two-block information structure.

Reasoning: The broader random-walk theorem supplies one upper-bound ingredient but does not dominate the exact envelope or lower construction.

### Exact database or table

Searches:
- Resultary exact-topic query
- Repository finite checks

Evidence:
- No prior exact table/formula for the two-block stopping envelope was found.
- Finite checks confirm examples but are not used as novelty proof.

Reasoning: The central theorem is structural and infinite, so a finite table is not decisive.

### Claim versus prior implication

Searches:
- Narayanan four-wise maximal theorem versus the stopped-sum functional
- Standard linear-code k-wise-independent sample spaces

Evidence:
- The known maximal theorem yields the global upper order once the independence level is at least four.
- Standard code constructions alone do not show a fully predictable iid future block that attains the exact envelope.

Reasoning: The final result requires combining the information-structure bound with a specific systematic-code construction.

### Source inspections

- **Three-wise independent random walks can be slightly unbounded** — Provides an upper-bound ingredient but not the stopped-sum theorem. Material read: Full arXiv text, including the main-results and generalized four-wise maximal inequality sections. Method: Primary full-text inspection. Evidence: The paper studies the supremum of partial sums rather than the two-block stopped expectation.

Checked sources:
- Narayanan, Three-wise independent random walks can be slightly unbounded, Random Structures and Algorithms 61 (2022), arXiv:1807.04910, full arXiv text.
- Benjamini, Kozma, and Romik, Random walks with k-wise independent increments, Electronic Communications in Probability 11 (2006).
- Repository verifier verify_stopping_bias.py and VERIFICATION.txt; the walk-maximum formula and a simplex relation distance were independently checked.
- Published Resultary semantic search for k-wise independent Rademacher stopping bias, linear codes, and bounded stopping.

Residual risks:
- Equivalent older formulations may exist in orthogonal-array, resilient-function, pseudorandom-stopping, or older optimal-stopping terminology.
- The exact constant is for the two-iid-block subclass; the unrestricted fixed-fraction theorem is only order-sharp.

## Scientific value — PASS

The result demonstrates that even linear-order limited independence can retain square-root stopping bias and identifies an exact extremal constant in a natural two-block class. It gives a clean quantitative boundary between wise independence and the conditional-mean hypothesis needed by optional stopping.

Checked sources:
- Narayanan, Three-wise independent random walks can be slightly unbounded, Random Structures and Algorithms 61 (2022), arXiv:1807.04910, full arXiv text.
- Benjamini, Kozma, and Romik, Random walks with k-wise independent increments, Electronic Communications in Probability 11 (2006).
- Repository verifier verify_stopping_bias.py and VERIFICATION.txt; the walk-maximum formula and a simplex relation distance were independently checked.
- Published Resultary semantic search for k-wise independent Rademacher stopping bias, linear codes, and bounded stopping.

Residual risks:
- Equivalent older formulations may exist in orthogonal-array, resilient-function, pseudorandom-stopping, or older optimal-stopping terminology.
- The exact constant is for the two-iid-block subclass; the unrestricted fixed-fraction theorem is only order-sharp.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
