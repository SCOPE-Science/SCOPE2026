# Independent audit — Exact fixed-order degree-spread minima for trees

Audited at: 2026-10-01T18:04:30Z

Disposition: **passed**

## Correctness

**PASS** — For \(k\ge1\), \(\sum_v(d(v)-1)=n-2\) bounds the number of vertices of degree at least \(k+2\), and the displayed degree multiset has total degree \(2n-2\), hence is realized by a tree via a Prüfer sequence. Competing width-\(k\) windows have no more vertices than the principal \(1,\ldots,k+1\) window. For \(k=0\), the leaf identity gives \(n\le3R-2\), and the three residue-class degree profiles attain equality. An independent re-enumeration of tree degree multisets through order 25 agreed with both formulas; the repository verifier through order 40 was inspected but was not used as the infinite proof.

## Originality

**PASS** — Caro--Lauri--Zarb prove the relevant tree lower bound for \(k\ge1\) and display a two-degree sharpness construction on compatible residue classes, while Caro--West gives the earlier repetition-number framework. The inspected sources do not state the fixed-order minimum for every \(n\); the one-intermediate-degree residue repair and the sharper \(k=0\) exact formula close that gap.

### equivalent_formulations

Searches: Resultary: tree degree spread exact fixed-order minima all residue classes repetition number Caro Lauri Zarb; arXiv:1806.08303.
Evidence: Resultary returned the audited record as the only exact all-order tree-minimum match; the primary 2019 paper uses the same \(\operatorname{sp}(G,k)\) parameter.
Reasoning: The audited \(	au_k(n)\) is exactly the fixed-order extremal reformulation of the established spread parameter, so aliases were compared directly rather than by title.

### broader_coverage

Searches: arXiv:1806.08303; arXiv:2609.19762.
Evidence: Caro--Lauri--Zarb Theorem 3.1 supplies the tree lower bound and a sharpness example, while the 2026 paper addresses broader graph classes and degree-spread questions.
Reasoning: The broader prior results do not state all-order attainment for every residue class, which is the final claim here.

### exact_database_or_table

Searches: Resultary published findings search; tree-degree-sequence literature terms.
Evidence: No exact all-\(n\) table/formula duplicating the two displayed extremal functions was located.
Reasoning: This is a symbolic extremal formula rather than a finite census; the finite verifier only checks small orders and is not novelty evidence.

### claim_vs_prior_implication

Searches: Caro--Lauri--Zarb 2019 Theorem 3.1; Caro--West 2009.
Evidence: The 2019 lower bound rounds to the same numerical lower target for \(k\ge1\), but its displayed two-degree attainment requires a residue compatibility. The audited proof supplies a realizable one-intermediate-degree sequence for every remaining residue.
Reasoning: The prior inequality alone does not imply existence of an attaining tree for every order; the residue-complete construction is the missing implication step. The \(k=0\) formula also improves the previously quoted \(\lceil n/3ceil\) lower statement.

### Source inspections

- **Notes on Spreads of Degrees in Graphs** (arXiv:1806.08303): PARTIAL_COVERAGE: lower bound and congruence-compatible two-degree sharpness, not the all-order formulas. Material read: Full theorem/proof section for the tree bound and sharpness construction. Trigger: Primary source for the exact parameter and tree lower bound. Evidence: Theorem 3.1 gives \(\operatorname{sp}(T,k)\ge(nk+2)/(k+1)\) for \(k\ge1\) and a two-degree construction.
- **Repetition Number of Graphs** (DOI:10.37236/96): BACKGROUND; gives the repetition framework and tree sharpness context, not the audited exact all-order formula. Material read: Publisher abstract/statement available in search. Trigger: Primary source for \(k=0\) repetition number. Evidence: The source describes general repetition lower bounds and approximate/asymptotic tree sharpness.
- **Spreads of degrees in graphs** (arXiv:2609.19762): NOT_COVERING in inspected material; focus is broader bounds and maximal outerplanar graphs. Material read: Abstract and theorem summary. Trigger: Recent paper on the same parameter. Evidence: No all-order tree formula appears in the inspected statement.

Checked sources: arXiv:1806.08303; DOI:10.37236/96; arXiv:2609.19762; Resultary published findings search.
Residual risks: Older degree-sequence literature under different extremal notation remains a best-of-knowledge risk..

## Scientific value

**PASS** — This is a natural complete fixed-order extremal function for a standard degree-spread parameter on trees. It closes every residue class, includes the classical repetition-number case, and supplies uniform extremal degree sequences. The finite checks are ancillary; the value lies in the exact symbolic classification.

## Limitations

- The theorem determines extremal values, not every extremal tree.
- Finite enumeration is supplementary and not an infinite proof.
- Older degree-sequence literature under different terminology remains a residual originality risk.

This file records a scientific assessment only; it does not claim formal verification or expert attestation.
