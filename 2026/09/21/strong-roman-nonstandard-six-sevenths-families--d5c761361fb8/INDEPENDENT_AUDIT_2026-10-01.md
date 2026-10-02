# Independent audit — 2026-10-01

## Final claim

Every connected root-gluing of subdivided-claw and triangularized-claw seven-vertex blocks has strong Roman domination number exactly \(6/7\) of its order, and any construction containing a triangularized block lies outside the subdivided-claw rooted-product equality family proposed in 2017.

## Correctness — PASS

The local lower bound is valid for both seven-vertex blocks even when only the root may have external neighbors: each support-leaf pair forces the stated minimum, and the cases by root label exclude total weight below six. Explicit block labelings have weight six and remain valid after root-to-root gluing because every root is positive. Summing the disjoint local lower bounds gives \(6m\), and the degree-two count separates every construction containing a triangularized block from the standard subdivided-claw rooted product. An independent exhaustive local replay gives minimum six for both blocks; bounded Graph Atlas enumeration corroborates the two order-seven equality examples.

Checked sources:
- Álvarez-Ruiz et al., Discrete Applied Mathematics 231 (2017); tree \(6n/7\) bound and equality rooted products.
- Mahmoodi, Nazari-Moghaddam and Behmaram, Mathematics Interdisciplinary Research 5 (2020), full accessible text; Lemma 4.1 and Theorem 4.2.
- Poureidi et al., Bulletin of the Malaysian Mathematical Sciences Society 45 (2022); abstract: linear-time algorithms for trees and unicyclic graphs; full theorem text unavailable in this run.
- Resultary semantic query for strong Roman \(6/7\) equality families; assigned record was the exact hit.

Residual risks:
- Finite enumeration is corroborative only; the arbitrary-base theorem is proved by the block argument.

## Originality — PASS

Best-of-knowledge originality passes for the exact triangularized block lower bound and the resulting arbitrary mixed equality families. The 2020 paper is important partial prior art: its Lemma 4.1 already shows that adding any edge to a standard equality rooted product cannot increase the strong Roman domination number. That yields the needed upper bound for a triangularized claw but not the matching lower bound or the mixed-family equality theorem.

### Equivalent formulations

Searches:
- Resultary query: strong Roman domination six sevenths equality subdivided claw unicyclic triangularized rooted product
- Mahmoodi--Nazari-Moghaddam--Behmaram 2020 Lemma 4.1

Evidence:
- The Resultary search returned the assigned finding as the exact-topic record.
- Lemma 4.1 proves only \(\gamma_{StR}(G+e)\le \gamma_{StR}(G)\) for an edge added to a standard equality tree.

Reasoning: Equivalent formulations include a second exact seven-vertex equality block and an infinite root-glued equality family outside the proposed class. The prior edge-addition lemma supplies one inequality only.

### Broader coverage

Searches:
- Álvarez-Ruiz et al. 2017 equality characterization for trees
- Mahmoodi et al. 2020 unicyclic bound
- Poureidi et al. 2022 algorithm abstract

Evidence:
- The 2017 theorem is restricted to trees.
- The 2020 theorem gives an upper bound for unicyclic graphs and does not classify all equality cases.
- The 2022 accessible abstract is algorithmic and contains no equality-family statement.

Reasoning: No inspected broader theorem forces exact value six for the triangularized block and arbitrary mixed gluing.

### Exact database or table

Searches:
- Graph Atlas order-seven equality census in the package
- Published literature searches for unicyclic equality cases

Evidence:
- The finite census finds the subdivided claw and triangularized claw as the only connected order-seven equality graphs.
- No prior complete equality table was located.

Reasoning: The census does not prove novelty or the infinite theorem; it only corroborates the naturality of the new block.

### Claim versus prior implication

Searches:
- Mahmoodi et al. Lemma 4.1 versus the audited lower bound

Evidence:
- The prior lemma yields \(\gamma_{StR}(H)\le6\) for the one-edge augmentation, while the audited local case analysis proves \(\gamma_{StR}(H)\ge6\) and survives arbitrary root gluing.

Reasoning: The exact equality and mixed-family conclusion therefore require substantive additional mathematics and are not a corollary of the known upper bound alone.

### Source inspections

- **Some Results on the Strong Roman Domination Number of Graphs** (https://doi.org/10.22052/mir.2020.225635.1205): trigger — Same extremal tree family under edge addition and unicyclic graphs; material read — Accessible full text, including Lemma 4.1 and Theorem 4.2; method — Primary full-text inspection; assessment — Strong partial overlap but not covering the exact new families.; evidence — Lemma 4.1 preserves a weight-six labeling after adding an edge, but proves only a nonincrease; Theorem 4.2 is an upper bound for unicyclic graphs.
- **Computing Strong Roman Domination of Trees and Unicyclic Graphs in Linear Time** (https://doi.org/10.1007/s40840-022-01301-4): trigger — Most plausible later source on exact unicyclic values; material read — Abstract and bibliographic material; full theorem text was unavailable in this run; method — Primary abstract inspection after lawful full-text search; assessment — Residual access risk only; no whole-document noncoverage claim is made.; evidence — The abstract states linear-time computation for trees and unicyclic graphs, not a closed equality classification.

Checked sources:
- Álvarez-Ruiz et al., Discrete Applied Mathematics 231 (2017); tree \(6n/7\) bound and equality rooted products.
- Mahmoodi, Nazari-Moghaddam and Behmaram, Mathematics Interdisciplinary Research 5 (2020), full accessible text; Lemma 4.1 and Theorem 4.2.
- Poureidi et al., Bulletin of the Malaysian Mathematical Sciences Society 45 (2022); abstract: linear-time algorithms for trees and unicyclic graphs; full theorem text unavailable in this run.
- Resultary semantic query for strong Roman \(6/7\) equality families; assigned record was the exact hit.

Residual risks:
- The full 2022 algorithm paper was unavailable after lawful open-web access attempts; it remains a plausible source for an isolated seven-vertex unicyclic example, though its abstract does not state an equality classification.
- The result does not settle the universal connected-graph \(6n/7\) conjecture or classify all equality graphs.

## Scientific value — PASS

The theorem directly falsifies the proposed equality-side classification while preserving the still-open universal bound, and it gives infinitely many exact-ratio examples over arbitrary connected bases. That is a motivated extremal counterfamily rather than an isolated small graph.

Checked sources:
- Álvarez-Ruiz et al., Discrete Applied Mathematics 231 (2017); tree \(6n/7\) bound and equality rooted products.
- Mahmoodi, Nazari-Moghaddam and Behmaram, Mathematics Interdisciplinary Research 5 (2020), full accessible text; Lemma 4.1 and Theorem 4.2.
- Poureidi et al., Bulletin of the Malaysian Mathematical Sciences Society 45 (2022); abstract: linear-time algorithms for trees and unicyclic graphs; full theorem text unavailable in this run.
- Resultary semantic query for strong Roman \(6/7\) equality families; assigned record was the exact hit.

Residual risks:
- The full 2022 algorithm paper was unavailable after lawful open-web access attempts; it remains a plausible source for an isolated seven-vertex unicyclic example, though its abstract does not state an equality classification.
- The result does not settle the universal connected-graph \(6n/7\) conjecture or classify all equality graphs.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
