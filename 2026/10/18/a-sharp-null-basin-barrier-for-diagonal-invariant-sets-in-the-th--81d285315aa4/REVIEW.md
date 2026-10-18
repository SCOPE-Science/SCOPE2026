# Scientific review: a sharp null-basin barrier for the three-dimensional Lozi diagonal

## Correctness — PASS

The map is specified for nonzero real parameters with the original zero-sign convention. The exact same-sign fiber equation follows from elementary absolute-value identities. A convergent orbit near a compact diagonal set avoiding the origin cannot visit opposite assigned sign sectors infinitely often: such visits would force its center, fiber, and middle coordinate to zero, contradicting compactness. Once signs agree permanently, the fiber multiplier has modulus at least one, so convergence forces finite entrance into the invariant diagonal. Each of the four affine branches has determinant \(-2ab\ne0\); preimages of the diagonal form a countable union of null sets, giving the asserted global basin conclusion. A smooth positive diagonal fixed point is explicitly shown to attract a neighborhood when \(0<|a|<1\) with sufficiently small positive \(b\), establishing uniform sharpness in \(|a|\). The Lyapunov-spectrum and finite-time formulas are verified with their stated restrictions.

The standalone script performs 4,050 symbolic/rational finite checks. The null-basin theorem rests on the preceding analytical proof, not extrapolation from those checks. The proof carefully includes points on one switching plane through the sign convention and does not assume continuity at those planes.

## Originality — PASS, with priority risk

The primary 2023 Lozi source already defines the model, its diagonal reduction, its Jacobian and specific diagonal fixed-point multipliers. Those are acknowledged as prior work. The principal new claim is a **global, three-dimensional, zero-volume basin theorem** for every nonempty compact invariant diagonal set excluding the origin, including the neutral parameter boundary and possible switching-line crossings away from the origin. This does not follow solely from one exhibited unstable fixed point or from positivity of the normal Lyapunov exponent; the nonlinear sign-discontinuity argument and preimage-nullity step are essential. A constructive attracting example proves the parameter barrier cannot be strengthened uniformly. Standard blowout/riddled-basin papers establish the wider conceptual mechanism in different coupled maps, but did not supply the model-specific all-compact-set result in the inspected sources.

Searches of the source model, invariant diagonal, transverse exponents, basin measure, and synonymous attractor concepts found no explicit matching theorem. This is limited evidence, not a mathematical proof of historical uniqueness. Priority risk remains from broad general theorems or uncatalogued analyses; independent assessment is needed.

## Value — PASS

The originating paper's principal visual theme is simultaneous thread-like and sheet-like chaotic invariant behavior in a three-dimensional Lozi extension. Whether a set attracts a positive volume of **ambient** initial conditions, rather than points deliberately restricted to an invariant two-dimensional plane, is a fundamental dynamical distinction. The theorem provides an exact all-parameter obstruction; the neutral case is stronger than merely identifying a positive transverse exponent. It also handles transversal sign jumps near the switching planes and proves the parameter condition is genuinely sharp in the natural family. These are structural properties of a motivated object, not arbitrary finite tabulations or a renaming of a known fixed-point eigenvalue.

## Limits and priority comparisons

The full author-posted text of Lozi (2023, DOI `10.20944/preprints202305.0775.v1`) was consulted in the sections defining the map, Jacobian, invariant plane, reported fixed-point eigenvalues, examples and conclusion. Maistrenko et al. (1998, DOI `10.1103/PhysRevE.57.2713`) provide conceptual transverse-instability precedents for a different system. Kucharski (2023, DOI `10.1063/5.0139893`) concerns two-dimensional Lozi attractors; only its abstract was available in this review. The theorem does not classify compact diagonal sets containing the origin, all basin structures, or invariant measures supported on derivative switching points. The sharpness construction is existential in the coupling parameter rather than a classification for each coupling.

Self-review: passed. Independent audit: not yet performed.
