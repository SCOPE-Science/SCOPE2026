# Scientific review

## Correctness — PASS

All 32,767 nonzero ternary quartic masks are partitioned exhaustively: a separate finite-field evaluator validates an explicit Jacobian-zero witness for each of 21,847 excluded equations, while symbolic unit-ideal Gröbner bases on three projective charts establish geometric smoothness for representatives of all 78 orbits comprising the other 10,920 masks. These complementary certificates close the geometric-smoothness issue without presuming a finite-degree bound on arbitrary singular points. Direct seven-line binary-quartic restriction and independent SymPy substitution give matching three-category contact splitting for each representative; the orbit calculation accounts for every counted equation, and the 40-cell table sums exactly to 10,920 equations and 78 classes. The executable source, full exclusion witnesses and all arithmetic tables are embedded. Finite calculations are used only for a finite parameter space, not as infinite proof.

## Originality — PASS, qualified

The 78 plane-quartic projective classes and characteristic-two normal forms are already classified in Nart--Ritzenthaler (arXiv:math/0312366); the invariant septuple of rational bitangents is already described by Duursma (arXiv:math/0302154). These prior claims are excluded from the claimed contribution. Pacini--Testa (arXiv:2004.00955v1, 2020-04-02) develops the geometric theta-hyperplane framework, without an exact binary-field joint arithmetic contact table. The original candidate is the *40-cell joint multiplicity profile of* \(N,n_0,n_1,n_2\) *among equations and projective classes*, including both zero/one/two rational contact support types. Source text inspected includes Nart--Ritzenthaler's theorem and normal-model setup, Duursma's rational-bitangent analysis and Pacini--Testa's theta-hyperplane discussion. Targeted source/database semantic checks did not reveal equivalent simultaneous incidence tables. Existing normal forms could be used to reconstruct them and an unindexed table may exist: publication priority is not certified. The marginal point and bitangent totals by themselves would not imply the full 40-cell joint distribution.

## Value — PASS

The joint rational theta-contact splitting of the seven rational line sections is a natural arithmetic refinement of the finite-field theta-characteristic geometry. It distinguishes rational bitangents with conjugate degree-two contacts, double rational contact and two rational contacts, recorded jointly with curve rational-point counts, whereas a single bitangent count or an unrefined genus-three moduli count loses these distinctions. The classification is complete at the smallest even-characteristic field, supplies directly checkable finite-field benchmark data with explicit orbit representatives, and respects the known geometric classification instead of presenting its routine totals as new. No downstream theorem is required for the meaningful complete arithmetic classification.

## Residual risk and scope

The previously published normal-model families may imply this arithmetic information after individual computation, and not every unindexed computational appendix or publication was examined. The result is the exact joint table, not the previously known smooth-curve isomorphism count or exceptional quartic; extension fields are outside the theorem.

Self-review: passed. Independent audit: not yet performed.
