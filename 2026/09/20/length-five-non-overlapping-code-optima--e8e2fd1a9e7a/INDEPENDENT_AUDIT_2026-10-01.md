# Independent audit — 2026-10-01

## Final claim

Maximum length-five non-overlapping codes have the stated exact sizes for all alphabet sizes, the unique Blackburn split from alphabet size four onward, and the stated complete enumeration.

## Correctness — PASS

The published SQN formulation specializes to the variables used in the proof. Optimizing the final split and then the next split reduces the problem to the two displayed quadratic branches. The universal inequalities exclude non-Blackburn optima for alphabet size at least four, with the isolated threshold case checked directly; the two smaller alphabets are solved separately. Equality conditions plus Proposition 11 give the enumeration. An independent exact replay for alphabet sizes two through eight reproduced all claimed optima, and the package verifier extends the finite check through twelve.

Checked sources:
- Stanovnik, Moskon, and Mraz, In search of maximum non-overlapping codes, Designs, Codes and Cryptography 92 (2024), full open-access article.
- Blackburn, Non-Overlapping Codes, IEEE Transactions on Information Theory 61 (2015).
- Repository verifier verify_length5.py and verification_output.txt; SQN was independently replayed through alphabet size eight.
- Published Resultary semantic search under non-overlapping, cross-bifix-free, mutually uncorrelated, and strong comma-free terminology.

Residual risks:
- A near-identical published finding dated 2026-09-21 postdates this 2026-09-20 record; it is not prior coverage but indicates near-simultaneous overlap.
- The theorem is specific to block length five and relies on the published SQN characterization.

## Originality — PASS

Best-of-knowledge originality passes at the record date. The 2024 primary paper states that no simple formula was available for larger codeword length and reports finite SQN computations rather than an all-alphabet length-five theorem. No earlier exact Resultary record was found; the close 2026-09-21 finding is later.

### Equivalent formulations

Searches:
- Resultary query: length five non-overlapping code exact S(q,5) maximum cross-bifix-free Blackburn k=4 enumeration
- Stanovnik--Moskon--Mraz 2024 under all four standard aliases

Evidence:
- The assigned 2026-09-20 finding is the earliest exact-topic Resultary hit; the next close hit is dated 2026-09-21.
- The 2024 paper explicitly lists the equivalent code terminology.

Reasoning: All standard aliases were searched and compared at the statement level.

### Broader coverage

Searches:
- Stanovnik--Moskon--Mraz 2024, Proposition 11 and Section 6
- Blackburn 2015 construction and conjecture

Evidence:
- The 2024 article supplies SQN and the counting theorem but says no simple formula is available for larger lengths.
- Blackburn supplies the construction but not all-q optimality at length five.

Reasoning: The prior framework does not mechanically determine the symbolic length-five optimum or its equality cases.

### Exact database or table

Searches:
- Stanovnik--Moskon--Mraz finite tables
- Resultary exact-topic search

Evidence:
- Finite length-five values are tabulated for small alphabets.
- No earlier all-alphabet formula or complete maximum-code count was located.

Reasoning: Finite tabulation cannot imply the infinite symbolic classification.

### Claim versus prior implication

Searches:
- Proposition 11 versus the audited equality classification
- Blackburn construction versus the audited SQN bound

Evidence:
- Proposition 11 counts codes only once the complete set of optimal SQN solutions is known.
- The audited inequalities establish precisely that missing optimizer classification.

Reasoning: The final theorem requires a nontrivial optimization argument rather than a parameter substitution.

### Source inspections

- **In search of maximum non-overlapping codes** — Framework and finite data are prior; the all-alphabet length-five formula is not. Material read: Full open-access article, including SQN, Proposition 11, the reduction section, Section 6, and finite tables. Method: Primary full-text inspection. Evidence: Section 6 says no simple formula was then available for larger codeword length.

Checked sources:
- Stanovnik, Moskon, and Mraz, In search of maximum non-overlapping codes, Designs, Codes and Cryptography 92 (2024), full open-access article.
- Blackburn, Non-Overlapping Codes, IEEE Transactions on Information Theory 61 (2015).
- Repository verifier verify_length5.py and verification_output.txt; SQN was independently replayed through alphabet size eight.
- Published Resultary semantic search under non-overlapping, cross-bifix-free, mutually uncorrelated, and strong comma-free terminology.

Residual risks:
- A near-identical published finding dated 2026-09-21 postdates this 2026-09-20 record; it is not prior coverage but indicates near-simultaneous overlap.
- The theorem is specific to block length five and relies on the published SQN characterization.

## Scientific value — PASS

Length five is the first length beyond the published exact symbolic classifications. The theorem gives the complete all-alphabet optimum, the exact optimizer structure, the small-alphabet exceptions, and the count of all maximum codes.

Checked sources:
- Stanovnik, Moskon, and Mraz, In search of maximum non-overlapping codes, Designs, Codes and Cryptography 92 (2024), full open-access article.
- Blackburn, Non-Overlapping Codes, IEEE Transactions on Information Theory 61 (2015).
- Repository verifier verify_length5.py and verification_output.txt; SQN was independently replayed through alphabet size eight.
- Published Resultary semantic search under non-overlapping, cross-bifix-free, mutually uncorrelated, and strong comma-free terminology.

Residual risks:
- A near-identical published finding dated 2026-09-21 postdates this 2026-09-20 record; it is not prior coverage but indicates near-simultaneous overlap.
- The theorem is specific to block length five and relies on the published SQN characterization.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
