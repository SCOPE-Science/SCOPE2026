# Self-review

## Correctness — PASS
The gradient calculation proves smoothness. The cubic contact multiplicity and Bézout reconstruct the precise tangent divisor. The fixed-point reduction to the separable polynomial \(u^{28}+u^{21}+1\) is reversible using the division by \(u^{91}-1\). The attached standard-library polynomial checker verifies all four degree-six/one degree-three/one degree-one irreducible factors by the finite-field GCD criterion, and it verifies the cycle counts. A finite extension census is used only as a consistency check, never in place of the all-degree argument. The assertion is restricted to the reduced configurations.

## Originality — PASS, qualified
Oyono–Ritzenthaler establish the classical geometric count of \(28\) hyperflexes and the characteristic-three exceptional isomorphism. Meagher–Top identify the Klein form as a Fermat twist in characteristic three but explicitly restrict the detailed Klein Frobenius classification to characteristics other than \(2,3,7\). Elkies discusses a different arithmetic model and its characteristic-three geometry. The new comparison target is the arithmetic Frobenius cycle type \(1^1 3^1 6^4\) for the *fixed cyclic model*, not the already-known number \(28\). Targeted mathematical-record searches for the exact tangent map, factor polynomial, bitangent orbits and aliases returned no stronger covering result. Historical specialized tables remain a risk; this is not a proof of uniqueness.

## Value — PASS
Bitangents correspond to odd theta characteristics for smooth plane quartics in odd characteristic, making their fields of definition intrinsic and useful arithmetic data. The nonclassical tangent map is geometrically meaningful and the finite-field splitting degrees of the complete natural \(28\)-object configuration are exact for every extension, not an arbitrary computation or selected numerical instance. In particular, only one bitangent descends to \(\mathbb F_3\) although all are defined over \(\mathbb F_{3^6}\).

## Sources and limitations
See Oyono–Ritzenthaler (2010) Sections 2–3, Meagher–Top (2010) Sections 4 and 8, and Elkies (1999). Scope is the cyclic \(\mathbb F_3\) model and reduced configurations. Nearby literature may hide an equivalent orbit computation; no independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
