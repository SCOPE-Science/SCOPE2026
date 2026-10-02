# Independent scientific audit — SCOPE-20260919-6d59c47d25e7

Audited at: 2026-10-01T17:15:19.026518Z

Disposition: **passed**

## Correctness — PASS

The source counter-machine model uses positive counters, so the conditional branch 'counter greater than one' can be expressed by two positive witnesses rather than a negated exact-rank predicate. Exact positive rank and exact-one increment are \(\Sigma_2\); zero rank, equality, and successor are \(\Pi_1\); representative membership is quantifier-free in the arbitrary-permutation, selected-permutation with quantifier-free selector, and LRS-function encodings. A finite one-step disjunction is therefore \(\Sigma_2\). Endpoint formulas are at worst \(\Sigma_3\), and the universally closed local transition formula is \(\Pi_3\). Standard prenexing of the existential sequence parameters, endpoints, and local clause gives an effective \(\exists^*\forall^*\exists^*\forall^*\) halting sentence. The package script verifies only the alternation bookkeeping; the semantic correctness comes from reconstructing the source encoding.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/prefix_audit.py
- Karimov-Nieuwveld-Ouaknine arXiv:2609.20415 full text, Sections 3-5 and 8

### Correctness risks

- The theorem gives an upper bound on alternation complexity, not optimality; \(\Sigma_3\) undecidability may still hold by another encoding.
- The selected-permutation extension requires a quantifier-free selector exactly as stated.

## Originality — PASS

The full primary paper proves unrestricted first-order undecidability and gives the explicit counter-machine formulas, but the inspected text does not assign a bounded prenex class to those new one-function structures. It separately relies on earlier two-power-predicate work, which concerns a different structure. Resultary and web searches found no prior \(\Sigma_4\) refinement for the totient, sum-of-divisors, least-prime-factor, or two-dominant-root LRS-function examples.

### Equivalent formulations

No equivalent bounded-prefix theorem was located.

### Broader coverage

Broader semantic undecidability does not imply undecidability of a fixed finite quantifier fragment.

### Exact database or table

Quantifier-prefix complexity is not a tabulated invariant; the full-text syntactic comparison is the substantive evidence.

### Claim versus prior implication

The four-block consequence requires a genuine syntactic normalization argument beyond the source's unrestricted undecidability statement.

### Sources inspected

- Rich Sequences and Decidability of Arithmetic Theories — https://arxiv.org/abs/2609.20415. NOT_COVERING: The source proves full first-order undecidability and exposes the formulas, but the inspected text does not state the audited four-block prenex bound.
- A strong version of Cobham's theorem — https://arxiv.org/abs/2110.11858. NOT_COVERING: It addresses a different structure with two recognizable predicates and does not imply the one-function \(\Sigma_4\) statements.

### Checked sources

- https://arxiv.org/abs/2609.20415
- https://arxiv.org/abs/2110.11858
- Resultary semantic search

### Residual risks

- The motivating preprint is extremely recent, so near-simultaneous quantifier-complexity refinements may be unindexed.
- The four-block upper bound is not claimed optimal.

## Value — PASS

Localizing new natural-structure undecidability results from unrestricted first-order logic to the fixed prefix \(\exists^*\forall^*\exists^*\forall^*\) materially sharpens their logical complexity. It also isolates a concrete lower-fragment boundary for future work, without claiming optimality.

### Value sources

- https://arxiv.org/abs/2609.20415
- https://arxiv.org/abs/2110.11858

### Value risks

- A future \(\Sigma_3\) reduction would supersede the quantitative bound but would not make the current four-block theorem false.

## Limitations

- The \(\Sigma_4\) bound is not claimed optimal.
- The selected-permutation extension requires a quantifier-free selector.
- Predicate-valued LRS and square-free-number constructions are outside the stated four-block theorem.
