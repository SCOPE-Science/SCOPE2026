# Mathematical audit — 2026-10-01

Record: `SCOPE-20260930-3d968bf6d9b9`

## Correctness — PASS

The all-set characterization follows from exact distance-difference cells. Two omitted vertices in one non-singleton part are twins relative to every selected vertex, forcing selection of all but at most one vertex there. For vertices in distinct parts, selected witnesses give only the three values \(+1\), \(-1\), and \(0\), and the pair is doubly resolved exactly when two of those cells are met. Exhausting support sizes at least three, two, and one gives precisely the stated support conditions. Maximizing omissions under those conditions reproduces every branch of \(\psi(G)\), and counting the extremal omission profiles gives the displayed basis counts. The actual package verifier exhausts all 58 complete-multipartite isomorphism types through order eight and all 8,084 vertex subsets; its logic was inspected and independently checked against the proof structure.

### Correctness sources

- assigned RESULT.md at tree 0b4c4ad18590f5f7e35c1498382e6befcdb2ef29
- assigned verify.py and VERIFY_OUTPUT.txt
- Jannesari 2021, arXiv:2106.03080v2

### Correctness risks

- Finite enumeration only corroborates the uniform proof.
- The result is for ordinary vertex doubly resolving sets in connected complete multipartite graphs.

## Originality — PASS

Jannesari's primary paper was inspected at the complete-bipartite theorem: it gives \(\psi(K_{r,s})=n-1\) for the smaller part of size at most two and \(n-2\) otherwise, but it does not classify arbitrary complete multipartite graphs or count all minimum doubly resolving sets. A 2025 lexicographic-product paper is a plausible overlap source for balanced product-structured subclasses, but its accessible abstract concerns lexicographic products rather than an arbitrary unequal complete-multipartite all-set classification. Fresh Resultary searches returned only the audited record as an exact match; nearby complete-multipartite results concern different resolving parameters.

### equivalent_formulations

Searches:
- Resultary: doubly resolving sets complete multipartite graphs exact formula basis count all subsets singleton parts
- arXiv:2106.03080v2 complete bipartite theorem
- DOI:10.1142/S1793830925500892 lexicographic product

Evidence:
- Jannesari 2021 Lemma 2.3 supplies only the complete-bipartite values.
- No searched source gives the arbitrary part-size support characterization or exact basis count.

Reasoning:
The complete-bipartite specialization and possible balanced lexicographic-product subclasses were separated from the arbitrary multipartite theorem.

### broader_coverage

Searches:
- Jannesari 2021 full HTML
- Jannesari 2025 lexicographic-product abstract
- current Resultary complete-multipartite resolving findings

Evidence:
- The strongest inspected exact prior statement is bipartite; the product paper is broader in construction type but not shown to imply arbitrary unequal multipartite instances.

Reasoning:
Neither source mechanically implies the all-set criterion across arbitrary singleton and non-singleton profiles.

### exact_database_or_table

Searches:
- current Resultary corpus for complete multipartite doubly resolving
- web searches for complete multipartite double metric dimension

Evidence:
- No exact database/table or stronger formula was found.

Reasoning:
This is a uniform structural theorem, not a finite table claim.

### claim_vs_prior_implication

Searches:
- statement-by-statement comparison with Jannesari Lemma 2.3

Evidence:
- The audited formula specializes correctly to the known bipartite cases, which are treated as prior work.
- The new support-size cases with three or more parts and the basis enumeration are not consequences of the printed bipartite theorem alone.

Reasoning:
Known special cases are excluded from the novelty basis.

### source_inspections

- **On doubly resolving sets in graphs** — https://arxiv.org/html/2106.03080v2. Trigger: Primary source containing the closest exact complete-bipartite theorem. Material read: Full relevant Section 2, including Proposition 2.2 and Lemma 2.3 with proof. Method: Primary theorem and implication comparison. Assessment: PARTIAL COVERAGE only. Evidence: Lemma 2.3 gives exact complete-bipartite values but no arbitrary multipartite all-set classification or basis count.
- **The doubly resolving number of the lexicographic product of graphs** — https://doi.org/10.1142/S1793830925500892. Trigger: Plausible broader product theorem overlapping balanced subclasses. Material read: Published abstract and bibliographic scope available through the searched lawful source. Method: Scope comparison. Assessment: Residual overlap risk for product-structured subclasses; no decisive coverage of the arbitrary theorem. Evidence: The abstract states computations for lexicographic products, not a complete classification of arbitrary complete multipartite graphs.
- **Assigned verifier** — verify.py. Trigger: All-set and basis-count finite cross-check. Material read: Complete source and recorded output. Method: Line-by-line logic inspection. Assessment: Correct corroboration. Evidence: It compares the definition with the stated characterization and formulas on every complete-multipartite type through order eight.

### checked_sources

- https://arxiv.org/html/2106.03080v2
- https://doi.org/10.1142/S1793830925500892
- current Resultary semantic search
- assigned RESULT.md and verify.py

### residual_risks

- The 2025 lexicographic-product full text was not available in the searched open route, so exact overlap for some balanced subclasses remains possible.
- Older terminology such as double metric dimension could conceal an equivalent theorem.

## Scientific value — PASS

The finding gives a complete structural description of every feasible set, not just a minimum cardinality, and turns it into closed formulas for both the invariant and the number of bases. The sharp dependence on singleton parts and part size two is mathematically natural and extends a known bipartite calculation to the full complete-multipartite class.

### Value sources

- Jannesari's complete-bipartite theorem
- assigned all-set classification and basis enumerator

### Value risks

- Value rests on the arbitrary multipartite classification and enumeration, not on the already-known bipartite values.

## Limitations

- Connected finite simple complete multipartite graphs only.
- Ordinary vertex doubly resolving sets only.
- Complete-bipartite values are prior work.
- Possible overlap with balanced lexicographic-product subclasses is recorded as a residual risk.

## Disposition

**PASSED**
