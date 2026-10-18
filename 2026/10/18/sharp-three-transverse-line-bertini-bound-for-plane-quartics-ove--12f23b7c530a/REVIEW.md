# Scientific review: sharp three-transverse-line Bertini bound

## Correctness (PASS)

The enumeration treats every scalar-normalized ternary quartic and every rational line. Restricting to the line and checking the binary quartic's squarefreeness (including the point at infinity) is equivalent to geometric transversality. The five generators span the full linear group, so the listed 92 orbits exhaust the \(t\le3\) locus. Exact Jacobian-ideal Gröbner tests on all three charts isolate exactly two smooth orbits, each of size 312, and their defining equations and rational-point counts are checked by a second symbolic implementation. Table generation was replayed from source and compared entry-by-entry with the C++ constants. Critical proofs are finite exhaustive algebraic tests with complete included programs; finite tests are not confused with an infinite-field conclusion.

## Originality (PASS, with residual uncertainty)

The closest primary source, Asgarli's 2018 sharp Bertini paper (Theorem 1.2, Corollary 2.2), proves existence of at least one transverse line at degree four over \(\mathbf F_3\), not the lower bound three or extremal classification. Asgarli–Freidin 2020 provides asymptotic proportions rather than exact fixed-degree extrema. The incidence-probability work of Makhul–Schicho–Gallet concerns limiting extension fields. Relevant finite-field rational-flex, bitangent, and binary-quartic transversality records have distinct hypotheses or conclusions and do not imply this ternary exact classification. Targeted published-record searches returned no covering theorem; negative results cannot prove global novelty. Unindexed finite computations and incomplete coverage of inaccessible literature remain risks.

## Mathematical value (PASS)

The sharp quantitative minimum at the natural finite-field Bertini threshold \(d=q+1\) is geometrically motivated by the dual-plane discriminant: thirteen rational lines are available, and at least three avoid it for every smooth quartic. Equality is rigid enough to force exactly two arithmetic isomorphism classes, yet those extremizers sit at radically different rational-point counts (one and ten). This is a complete structural finite cutoff, not merely a new example or an arbitrary refinement. It differs substantially from the binary-field zero-transverse-line phenomenon.

## Scientific limits

Only the base field with three elements, degree four, and the defined rational-line invariant are classified. The exhaustive scheme does not claim formal verification or certify publication priority. The diagrams and code are original finite calculations; no journal or unrelated theorem is claimed as proved. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
