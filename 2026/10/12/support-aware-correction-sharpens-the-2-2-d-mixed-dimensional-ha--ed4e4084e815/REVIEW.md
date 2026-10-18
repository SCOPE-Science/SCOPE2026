# Independent mathematical audit

## correctness

PASS

In C^2⊗C^2⊗C^d, d>=5, dimensional weight of a support is the product of local dimensions; hence every error of weight ≤4 is supported entirely in A=C^2⊗C^2 (including double-qubit support), and any E_a†E_b of this set also lies in End(A)⊗I_d, weight ≤4< D=5. The exact distance-definition detection property on each product gives Knill–Laflamme correction of the full A operator algebra. Its orthogonal error basis has 4^2=16 elements (one identity, six one-qubit and nine two-qubit); if nondegenerate, 16 orthogonal K-dimensional error spaces in ambient dimension 4d force 16K≤4d, K≤floor(d/4). The originating paper instead uses the merely sufficient T²<D cutoff T=2, counts seven errors and gives K≤floor(4d/7). Its separate pure Singleton ceiling floor(d/4) coincides with the stronger Hamming upper bound, so the particular numerical upper-bound gap does not force impurity. These are conditional upper bounds, not a construction/existence claim. Independent support-check code evaluated d=5,6,11,17; analytic closure applies to all d≥5.

## originality

PASS

The source itself computes only seven correctable basis errors and claims T=2 is maximal; primary pages 16–18 show the example and downstream impurity claim. An earlier Ball–Zhang theorem explicitly states that all errors on a known support of dimensional weight below D can be corrected, and ordinary Knill–Laflamme is older. The abstract support lemma and 16=4² alone are not new. The new claim is a concrete correction to the later published example: its full threshold, strengthened nondegenerate Hamming count and invalidity of the specific forced-impurity inference from the displayed upper bounds. No inspected source gives this exact paper-specific correction, but the mathematics is a straightforward consequence of the older principle, so priority/value depend on this independently motivated error identification rather than rediscovery of the general theorem.

## value

PASS

The correction identifies a material error in a recent published worked quantum coding bound and removes a claimed forced-impurity implication, changing interpretation of an explicit architecture. This is a motivated, consequential source correction, not an unmotivated support-check exercise. The basic support theorem receives full credit as antecedent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
