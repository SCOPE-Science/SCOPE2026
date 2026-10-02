# Independent audit — Degree-sensitive separation for integer linear forms in square roots

Audit date: 2026-10-01 (UTC) UTC

## Final claim

The product lower bound for an integer linear form in square roots can be written in terms of the actual multiquadratic field degree rather than the full formal sign cube. On a complete multiquadratic basis the coefficient exponent becomes K minus 1, and that exponent is optimal for fixed radicands.

## Correctness — PASS

The norm argument is valid. The active negative squareclasses define distinct nontrivial characters of the multiquadratic Galois group, and character orthogonality gives the exact average squared conjugate size. The identity embedding and complex conjugation contribute the two copies of the target linear form; the nonzero algebraic-integer norm and AM-GM on the remaining conjugates give the claimed degree-sensitive lower bound. The field degree is the power of two determined by the binary rank of the negative squareclasses. On a complete multiquadratic basis the degree is twice the basis size, and Dirichlet approximation gives the matching coefficient exponent. The committed degree-eight example was independently checked from its minimal polynomial and exact norm.

## Originality — PASS

The current full HTML of Aymone, Figueredo, Iyer and Táfula, arXiv:2609.14161v2, was inspected. Its product and AM-GM bounds use the full formal sign orbit and retain the exponent based on the number of sign choices; it does not state an actual-field-degree or squareclass-rank refinement. Resultary returned no earlier equivalent published record. Older radical-separation literature was searched, but one plausible Dubickas source could not be obtained in full text after open-access attempts and an institutional retrieval attempt was interrupted. That specific access risk is recorded rather than treated as proof of novelty.

### Equivalent formulations

Searches: Resultary semantic search for degree-sensitive square-root separation and squareclass rank; full-text inspection of arXiv:2609.14161v2; targeted search for multiquadratic degree lower bounds for square-root linear forms

Evidence: Aymone et al. Proposition 2.2 isolates all (2^K) signed factors and obtains exponent (2^{K-1}-1), with no quotient by the actual Galois degree.

Reasoning: Replacing the formal sign orbit by the actual Galois orbit changes the theorem substantially when radicands have squareclass relations.

### Broader coverage

Searches: Searches for Burnikel–Fleischer–Mehlhorn–Schirra radical separation; searches for Dubickas square-root separation and multiquadratic degree

Evidence: Located older general radical-separation and equal-coefficient results, but no accessible theorem with the exact (D/2-1) coefficient exponent or the binary-rank formula.

Reasoning: No inspected broader theorem was found that mechanically implies the final degree-sensitive bound.

### Exact database or table

Searches: No finite invariant database or table governs the general multiquadratic separation bound.

Evidence: The binary rank is computed from the input squareclasses and is part of the theorem, not a database lookup.

Reasoning: Database comparison is inapplicable.

### Claim versus prior implication

Searches: Compared the final norm argument directly with Aymone et al. Lemma 2.1 and Proposition 2.2.

Evidence: Prior proof multiplies all formal sign conjugates; final proof uses only the actual (D) Galois conjugates and the character second moment.

Reasoning: The prior published inequality does not imply the stronger degree-sensitive exponent in low-degree configurations.

## Value — PASS

The refinement is mathematically motivated because squareclass relations can make the actual multiquadratic degree exponentially smaller than the formal sign cube. On a natural complete multiquadratic basis, the coefficient exponent collapses to the optimal linear value K minus 1. This is a structural sharpening controlled by an exact field invariant, not merely a change of notation.

## Source inspections

- **Marco Aymone, Samuel Figueredo, Siddharth Iyer, Christian Táfula, Quantitative linear independence for square roots, arXiv:2609.14161v2** — Material read: full arXiv HTML through the introduction, Lemma 2.1, Proposition 2.2, and surrounding discussion. Finding: Uses the full sign product and gives exponent (2^{K-1}-1); no actual-degree refinement is stated.
- **Older Dubickas square-root separation literature** — Material read: bibliographic/abstract-level material located by targeted search; full text was not obtained. Finding: Potentially relevant older source remains an access risk; no accessible statement matched the audited degree-sensitive theorem.
- **Committed verification artifacts for the audited record** — Material read: complete verifier source and saved output. Finding: Checks binary ranks, a degree-eight example, and 2,400 small coefficient vectors; these finite checks corroborate but do not prove the theorem.

## Residual risks

- A plausible older Dubickas source could not be inspected in full. Open-access retrieval did not provide the paper, and a later institutional retrieval attempt was interrupted before text was available. The originality verdict is therefore qualified by this concrete access risk.

The assessment applies to the single final claim above. Computational artifacts are corroborative evidence only; they are not used as a substitute for the mathematical proof.
