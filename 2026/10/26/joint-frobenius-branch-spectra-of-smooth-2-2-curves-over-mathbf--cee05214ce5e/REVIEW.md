# Scientific review

## Correctness (C): PASS

The domain is exactly the 9841 scalar-normalized nonzero bidegree-\((2,2)\) forms over \(\mathbf F_3\). The branch polynomials and infinity convention are explicit; squarefreeness is equivalent to geometric smoothness for the separable finite degree-two projection. Independently, the symbolic program constructs the 41 entire projective orbits and computes the four-chart Jacobian ideals on their representatives, leaving 14 smooth orbits and 5184 equations. A direct all-form finite-field implementation reproduces the same 5184 and every branch-profile count. A separate evaluation/interpolation group implementation checks all 1152 ambient symmetries and all smooth orbit sizes. Proof does not extrapolate from a finite extension test. Remaining risk: reproducibility depends on the stated exact arithmetic and software execution; no external certification was performed.

## Originality (O): PASS, qualified

Fisher–Radičević (arXiv:1703.01940, §2) develops the two binary-quartic branch-cover representations. Fisher–Ho–Park (arXiv:1911.09623, Remark 3.6) already proves the total 5184 smooth equations at \(q=3\); that count and the existence of paired binary quartics are expressly excluded from the originality claim. Examined primary sections do not specify the joint six-type Frobenius distributions or the 14-orbit refinement. Targeted mathematical-record and literature searches found no equivalent statement, including under dual-branch, pair-of-binary-quartics and polarized-model descriptions. These searches do not prove worldwide priority; an unindexed small-field census or an uninspected appendix could subsume these precise numbers.

## Value (V): PASS

Two degree-two maps from an elliptic model encode different degree-two linear systems and branch divisors. Their **joint** arithmetic splitting is a natural finer invariant than a single quartic type, a point count, or the known count of smooth models. The exact six-profile support, frequencies, and rare asymmetric \(((1,1,1,1),(2,2))\) class form a complete finite-field boundary test for paired-branch models; they are neither generic formulas nor an arbitrary coefficient slice. The result is restricted to \(\mathbf F_3\), and no downstream theorem for other fields is asserted.

Self-review: passed. Independent audit: not yet performed.
