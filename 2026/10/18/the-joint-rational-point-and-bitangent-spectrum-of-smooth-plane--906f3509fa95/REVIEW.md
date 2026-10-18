# Scientific review

## Correctness — PASS

The exact test \(\operatorname{rank}\Phi_F=66\) is proved equivalent to geometric smoothness via a three-quartic complete-intersection Hilbert-function bound; no finite extension smoothness heuristic is used. For each rational line, the restriction is a square exactly when the two odd-degree mixed coefficients vanish in characteristic two. Both conditions are evaluated for every one of the \(32,767\) nonzero binary quartic equations. The independent orbit and affine-chart Gröbner-basis implementation finds 78 smooth projective-coordinate orbits with total weight 10,920, reproducing every cell of the joint table and the specified line configurations. The exact mathematical object, enumeration domain, and hyperflex convention are specified. Reproduction requires C++17 and Python with SymPy. Source programs and actual output records are included.

## Originality — PASS, qualified

The closest primary literature is Nart–Ritzenthaler, arXiv:math/0312366, which supplies a complete classifying system of characteristic-two nonhyperelliptic genus-three curves, explains possible geometric bitangent counts and Fano incidence, and tabulates rational points of Newton-polygon moduli *strata*. Those prior classification and geometry statements are excluded from the new claim. The presently asserted invariant is the exact weighted joint distribution of *individual-curve* rational point counts and rational even-contact lines over \(\mathbf F_2\), including exact per-subconfiguration multiplicities, which is not stated or already numerically implied by the published aggregate class-count formulas. A derivation from complete normal forms is possible in principle with additional computations; priority could be affected by unpublished or unindexed tables. Markwig–Payne–Shaw (arXiv:2207.01305) study arithmetic bitangents only with residue characteristic different from two. Asgarli–Ghioca–Yip (arXiv:2208.13299) study rational point incidence but not its joint distribution with even-contact lines. Müller–Ritzenthaler (arXiv:math/0405052) concern ordinary quartic invariants. Targeted research-record searches and accessible earlier findings supplied no covering joint spectrum, but absence of search results is not proof of novelty.

## Value — PASS

Arithmetic rationality of theta characteristics/bitangent lines and rational point existence are two natural invariants of genus-three curves. Their exact dependence is not captured by the 2-rank alone, a geometric-bitangent total alone, or a count of isomorphism classes. The table supplies an exact arithmetic incidence statistic with sharp forbidden combinations; the Fano-plane multiplicities specify which rational configurations are realizable and how frequently. This is a complete exact finite-degree refinement at the smallest field, useful as a test case and boundary datum for arithmetic enumeration and descent methods. Its scope is deliberately finite and does not assert a general-field theorem or new curve classification.

## Limitations and closest literature

This is a coordinate-equation-weighted finite-field census, not a reclassification of genus-three curves. It relies on executable exact combinatorics and standard commutative-algebra lemmas, and needs independent mathematical audit for additional assurance. In particular, Nart and Ritzenthaler's complete earlier classification is strong background coverage; equivalent unpublished tabulations and consequences requiring straightforward but nontrivial case arithmetic remain the principal priority risks.

Self-review: passed. Independent audit: not yet performed.
