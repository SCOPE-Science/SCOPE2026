# Independent mathematical audit

## correctness

PASS

Averaging signed-isometric conjugates preserves the fixed range and identity on it. The endpoint-swap stabilizer forces any intertwiner from a complete-graph oriented edge module to the vertex module to be a multiple of incidence; tensoring with the two-dimensional commutant on the other vertex module gives precisely the four potential coefficients, and identity on gradients leaves one free parameter. For the circulation projection, the complement factors through divergence, and the dual intertwiner argument restricts its right inverse to the two gradient copies of the mixed block and the single copies of the pure blocks. I rederived the horizontal absolute column sums: the gradient of an endpoint difference has norm 2(m−1), its diagonal entry is 2w_c, and the other edges in that fiber contribute 2(m−2)|w_c|. This gives the displayed cut and circulation expressions; swapping factors gives the other columns. Replacing each absolute value by its interior sign gives affine lower bounds globally, with opposite strictly signed slopes and their unique crossings in [0,1]. This proves the minima and equivariant uniqueness, not unrestricted uniqueness. The orthogonal parameter m/(m+n) and factorizations give exactly the stated exceptions; complementarity would prescribe the orthogonal pair since C and Z are orthogonal complements. The four-cycle gives cut 3/2 and circulation 1, and (2,3) gives 7/4 and 64/39. RESULT.md §§1–4 suffice for replay. The supplied check.py and VERIFICATION.md were inspected, not executed: the recorded exact calculations check finite columns and selected generators, not universal optimality.

## originality

PASS

Pass is for the complete rectangular classification, principally the unequal two-factor case with both factors at least 3. The equal-factor results, the two-vertex-factor results, and the (2,4) exception on its own are already covered and are not credited as distinct findings. No compared source establishes the full unequal-factor optima or the exclusion of further orthogonal exceptions.

## value

PASS

The real edge cut and circulation spaces are natural fixed subspaces with intrinsic projection constants in the graph ℓ1 model. Distinct edge orbits expose two different optimal balances and show that no complementary pair simultaneously attains the two separate minima off the diagonal. The full classification closes the gap between previously analyzed symmetric and thin rectangles; its value does not rely on the already-known (2,4) case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
