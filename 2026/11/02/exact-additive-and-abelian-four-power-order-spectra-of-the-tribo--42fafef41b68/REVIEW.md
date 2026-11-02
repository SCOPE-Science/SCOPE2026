# Scientific review: exact Tribonacci fourth-power orders through \(1705\)

## Correctness: PASS

The factor-cover lemma is exact: all five length-two factors of the Tribonacci fixed point occur, and each length-\(4d\) factor for \(1\leq d\leq1705\) starts in one \(\mu^{16}\)-image and ends no later than the following image. This is guaranteed by the lower bound \(\min_x|\mu^{16}(x)|=10609>4\cdot1705\). Conversely the five image-pairs really occur, so the finite search can neither omit nor introduce a witness. The arithmetic tests use exact symbol-prefix counts and are equivalent to the additive and Abelian definitions. A separate variable-level scan and verification of every listed witness reproduce the two membership arrays, the cumulative counts and the strict-separation order. The calculation is a finite exhaustive proof because the mathematical coverage lemma applies to the **infinite** fixed point.

## Originality: PASS, subject to bibliographic uncertainty

The closest primary source is Popoli–Shallit–Stipulanti, *Additive word complexity and Walnut* (arXiv:2410.02409v1), Section 6. Its Theorem 37 recognizes orders of cubes, while Problem 38 explicitly asks for orders of higher additive powers and identifies computational difficulty at exponent four. The submitted claim determines both fourth-power order sets up to a specified natural substitution cutoff, rather than asserting an automaton or a global classification. Couvreur et al. (arXiv:2504.13584), Theorems 19–23, obtain generalized Abelian factor-complexity and balance properties, not four consecutive blocks of equal Parikh vector. Turek's Tribonacci factor-class counts and the OEIS cube-order sequences likewise lack the necessary four-block positional correlations. Currie et al. (arXiv:2111.07857) work with a different morphic word that avoids fourth powers. Related exact short-word results on a three-pseudoperiod invariant have a different predicate and no implication for this order spectrum.

Searches for the mathematical aliases, the exact object and parameters, more general automata or tables, and the cited primary results found no covering statement. This is evidence for best-knowledge novelty, not an absolute uniqueness certificate. The remaining risk is an unindexed calculation or a deeper theorem whose unstated corollary yields the same finite table.

## Mathematical value: PASS

The cutoff \(1705=|\mu^{12}(0)|\) is a natural Tribonacci substitution length, not an arbitrary digit range. A complete two-predicate classification supplies \(3410\) exact existence decisions with witnesses or exhaustive negative certificates. It attacks the specific exponent-four computational gap highlighted by Problem 38 and discovers a concrete, reproducible separation: \(117\) orders permit additive fourth powers but no Abelian fourth powers, first at \(d=10\). The data provide test cases for any future structural or automata-theoretic characterization. The value is a motivated finite segment of an open problem, not a claim to resolve that infinite problem.

## Remaining limitations

No conclusion for \(d>1705\), no global regular-language representation, and no assertion of unindexed-literature completeness. Numeric replay requires the included standard-library script and CSVs; no external certification was performed.

Self-review: passed. Independent audit: not yet performed.
