# Scientific review of the four-gap covariance phase diagram

## Correctness (C): PASS

The theorem is an all-size rational covariance identity for two prescribed disjoint endpoint-pairs in a uniform perfect matching on a circle, for integers \(n\ge4\). The proof begins with exact single-pair and disjoint-two-pair matching probabilities, removes overlapping potential pairs through \(Q-C\), and factors a completely specified polynomial numerator. Its noncrossing specialization has manifestly nonnegative sign. For crossing chords the squared-opposite-gap-product inequality gives all three signs. The first-positive claim explicitly requires all four gap counts strictly positive; the manuscript supplies a positive counterexample at \(n=4\) when empty gaps are allowed. The strict-positive-gap minimal case is established by finite enumeration of the only positive four-part compositions at \(n=4,5\), together with an explicit \(n=6\) witness. The standalone checker independently enumerates all matching outcomes for 1,710 marked layouts through seven chords and cross-checks 19,149 algebraic compositions, all exactly.

## Originality (O): PASS, with bounded priority risk

Acan, arXiv:1501.01489v1, Section 2 derives one-chord span-conditional degree information, not a two-prescribed-chord covariance classified by all four arc gaps. Flajolet–Noy, INRIA RR3914, Section 2 treats *global* crossing moments; Paguyo, arXiv:2104.01134, Section 2 treats approximation of the *total* crossing count. Focused searches for two-chord joint degrees, fixed-cut crossing counts, and corresponding random perfect-matching covariance did not identify a direct prior statement. A general matching-indicator moment identity is an elementary ingredient and is not itself claimed as new. A broader, older two-cut moment theorem could implicitly contain the new factorization, so human historical review remains prudent.

## Value (V): PASS

Local dependence in random circle graphs is naturally described by joint degrees of prescribed chords, rather than only marginal degree limits or global crossing totals. The result supplies a complete finite-sample sign criterion, shows noncrossing positions cannot have negative covariance, and proves that crossing positions of identical diagram size can have both signs with positive space between all marked endpoints. The balanced negative covariance remains bounded away from zero, whereas an imbalanced positive family has linearly growing covariance, giving a geometrically motivated phase distinction beyond routine first moments.

## Limitations

The result does not treat random selection of two vertices of the realized circle graph and does not infer a full bivariate dependence order. The all-size proof is independent of the finite exact checker. Priority is bounded by inspected literature, not guaranteed absolutely. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
