# Independent mathematical audit — 2026-10-01

## Final claim assessed

Positive characteristic collapses the two-call passive register frontier

## Correctness — PASS

PASS. With one work register and a passive output, call-free work updates are constants. In any nonlinear two-call clean program the two nonzero work-register accesses must cancel. Collecting output updates before and after the active interval gives \(H(\tau+ax)-H(\tau)=f(x)-f(0)\), so after rescaling \(f-f(0)\) is additive. Conversely, any constant plus additive polynomial is computed by the displayed two-access finite-difference transcript. Over characteristic \(p>0\), polynomial additivity is exactly the standard \(p\)-linearized form \(\sum_j a_jX^{p^j}\), so arbitrarily high formal degree is attained already by Frobenius powers.

## Originality — PASS

PASS to the best of current knowledge. The complete inspected portion of Vinciguerra's primary preprint explicitly assumes characteristic zero throughout the call-lower-bound section and states \(D^{\mathrm{pass}}_{r,K}(2)=1\) only there. Its positive-characteristic statements concern four-call constructions under a large-characteristic restriction, not a two-call classification. Published-record and targeted searches found no earlier theorem identifying the two-call class with additive polynomials. Standard linearized-polynomial theory supplies the algebraic classification after additivity is proved, but not the register-program necessity argument.

### equivalent_formulations

Searches: Resultary: passive two-call register programs positive characteristic additive polynomials Frobenius; web search: passive-output register program additive polynomial characteristic p two calls

Evidence: No earlier exact record was found; standard linearized-polynomial references describe additive polynomials but not this register-program characterization.

Reasoning: The equivalent finite-difference formulation still requires proving that every clean two-call program has a translation-independent finite difference.

### broader_coverage

Searches: arXiv:2609.18692 Sections 2--3 full text; MFCS 2025 register-program paper

Evidence: The primary 2026 source states the two-call frontier only in characteristic zero; its positive-characteristic constructions use four accesses.

Reasoning: No inspected broader register-program theorem covers the positive-characteristic two-call class.

### exact_database_or_table

Searches: Published-record semantic search for two-call additive/Frobenius register programs

Evidence: The assigned record was the only exact match in the inspected results.

Reasoning: This is a structural classification rather than a tabulated invariant.

### claim_vs_prior_implication

Searches: Vinciguerra Theorem 3.2 and Theorem 3.5; standard \(p\)-linearized polynomial classification

Evidence: The source's proof is characteristic-zero and does not imply the positive-characteristic frontier. Linearized-polynomial theory applies only after the new register-program finite-difference necessity is established.

Reasoning: The final theorem is not a parameter substitution into an existing positive-characteristic register-program result.

## Scientific value — PASS

PASS. The theorem identifies a sharp structural boundary in a newly active register-program model: the characteristic-zero two-call degree frontier collapses completely in positive characteristic, and the exact mechanism is additive finite difference. This is a natural diagnostic for how characteristic assumptions enter catalytic algebraic lower bounds.

## Source inspections

- **An Operator Approach to Register Programs for Catalytic Computing** — https://arxiv.org/abs/2609.18692. Material read: Primary full-text pages 1--12 of the 31-page preprint, including definitions, Theorems 3.2 and 3.5, and the explicit statement that Section 3 works in characteristic zero. Assessment: CHARACTERISTIC_ZERO_SOURCE_NOT_COVERING_POSITIVE_CHARACTERISTIC_CLASSIFICATION. Evidence: The source proves the two-call degree-one frontier under characteristic zero and gives separate four-call constructions in characteristic zero or sufficiently large characteristic.
- **Linearized-polynomial background** — https://doi.org/10.1017/CBO9780511525926. Material read: Standard finite-field theorem context and corroborating modern references to \(p\)-linearized polynomials. Assessment: STANDARD_ALGEBRAIC_INGREDIENT. Evidence: It explains the \(p\)-power form of additive polynomials but does not address register programs.

## Limitations and residual risks

The exact classification is for one work register, one passive output, and at most two input accesses. It is univariate and commutative. Formal polynomial degree, rather than degree of a polynomial function on a finite field, is the relevant notion.

- A later revision of the very recent primary preprint could contain new positive-characteristic remarks that were not available in the inspected full text. A separate attempt to inspect a later revision was blocked and was not retried.
- The classification concerns formal polynomial identities; over a finite field, distinct formal polynomials can induce the same function.

## Disposition

**passed**
