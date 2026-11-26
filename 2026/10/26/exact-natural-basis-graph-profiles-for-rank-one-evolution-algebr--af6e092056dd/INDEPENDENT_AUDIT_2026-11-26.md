# Independent mathematical audit

## correctness

PASS

The frozen probability theorem and three feasible exceptions survive. Two assertions in the frozen text needed correction: RESULT.md:64 says A_n(c)=|G_n(c)| only in the three listed regimes, but A_2(0)=|G_2(0)|=q−1 for every odd q (the sign giving cancellation makes T=0); RESULT.md:77 wrongly says uniform weighting of rescaling-and-reordering classes changes the law. The monomial action on ordered bases is free with constant orbit size n!(q−1)^n and preserves K. The complete replacement /workspace/repairs/3/RESULT.md proves the feasible-cancellation classification by exact parity-specific base cases and an increase-by-two inequality and corrects the class-weighting assertion. I checked the replacement: natural bases are orthogonal bases, and each diagonal of determinant class δ has |O(B)| presentations, with constant fibers for nonzero coordinates of fixed norm by Witt extension (including norm zero). On a proper support the residual entries supply exactly half the tuples in the specified determinant class; on full support the restriction is (1+δχ(product a_i))/2. Additive character orthogonality gives A and, with the quadratic Gauss-square identity, the four cases of G, including the χ(−c) factor in odd dimension. T counts nonzero vectors of norm c in any of the diagonal models. The three feasible cancellations and generator-rescaling invariance were also checked. Replay: python /workspace/checks/3-4.py directly enumerates unordered sets of orthogonal nonisotropic lines and verifies all three exceptional F3 histograms and additional F5 and F9 cases. This corroborates, but does not replace, the all-field proof. Frozen verify.py and supporting notes were read, not executed.

## originality

PASS

The supported distinct claim is the all-dimensional finite odd-field graph-support law with discriminant correction and complete feasible exception list. Bilinear classification, Witt transitivity and quadratic Gauss sums are credited ingredients. The repair supplies the missing boundary reasoning and corrects a weighting remark; it does not rely on a new priority claim about quotienting.

## value

PASS

Graph type can change under natural-basis changes, even for a fixed rank-one algebra. The repaired theorem gives a basis-independent probability profile of that variability, exact counts and a complete list of actual small-field failures of full support. The determinant constraint appearing only at full support and the three exceptional regimes matter for graph realizability; the result is not just a restatement of form classification or a fixed small-dimensional calculation. It does not classify all evolution-algebra graphs or automorphism-orbit weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
