# Scientific review: finite Kleene-cube modal-operator spectra

## Correctness — PASS
The direct-product structure makes the axioms coordinatewise; for each output coordinate, finite meet preservation produces nested principal upper filters for the \(0\)- and \(1\)-thresholds. Positivity makes the lower generator lie in \(\{-1,0\}^n\); consistency is equivalent to the explicit implication \(x\vee t\ge b\Rightarrow x\ge b\) for all \(t\in\{-1,0\}^n\), exactly forcing the upper generator (when present) into \(\{-1,1\}^n\). The three allowed coordinate pairs and the absence-of-upper-filter alternative give the counts. The normality and asymptotic steps follow by evaluation at the top and elementary expansion. `checker.py` exhaustively agrees on the exact truth-table **sets** for \(n=1,2\); larger \(n\) is proved symbolically rather than inferred from experiments.

## Originality — PASS, with stated priority risks
The closest motivating preprint (Celani, Menchón and Miguelez, arXiv:2608.10937v1) develops general modal Kleene algebras, triple representations and dualities, whereas the new claim is a complete explicit normal form and the labelled operation spectrum on all finite non-chain powers of \(\mathbf K_3\). The earlier finite-chain classification only intersects at the single factor \(\mathbf K_3\). Targeted searches for Kleene cubes, meet-preserving modal operators, ternary matrices and the exact exponents did not locate a result establishing the same counts. A general representation theorem can encode these operators abstractly, but the needed positivity/consistency reduction and three-state enumeration are additional, quantified statements. Residual priority risk remains from older finite many-valued-operator or contact-algebra classifications and from any uninspected portions of the cited preprint; lack of a match is not uniqueness proof.

## Value — PASS
Finite products of the basic three-valued Kleene algebra are canonical finite non-Boolean models, and the new normal form turns the modal operator into independent, explicitly specified two-threshold data. Exact counts for both normal and non-normal operations across every dimension give a natural algebraic spectrum. The asymptotic near-certainty of normality on large cubes is a substantial contrast with behavior on growing finite chains, so it is not merely a small finite table or a change of notation.

## Source and verification boundaries
The verified motivating primary source is arXiv:2608.10937v1, first submitted on 2026-08-11, particularly its Definitions and representation statements in Sections 2–3. The checker's exhaustive range is \(n\in\{1,2\}\); the argument for all positive integers is a separate proof. Searches and a targeted reading cannot rule out unpublished or differently phrased predecessors. The scholarly claim is limited to the operation spectrum on labelled products.

Self-review: passed. Independent audit: not yet performed.
