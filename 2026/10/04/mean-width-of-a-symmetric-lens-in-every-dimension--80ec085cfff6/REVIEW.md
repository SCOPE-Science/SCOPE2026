# Same-model review
## Correctness
PASS. The support-function maximization is reduced to one scalar variable with all constraints explicit. The two branches meet at \(t=c\), the distribution of \(|U_1|\) on \(S^{n-1}\) is normalized by \(C_n\), and each beta-function reduction is a direct substitution. Differentiation of the integral form gives a strictly negative derivative for \(0<c<1\). The \(n=3\) specialization reproduces Finch's stated three-dimensional formula exactly. The bundled numerical checker independently probes the support maximization and low-dimensional specialization, but those computations are not part of the proof.

## Originality
PASS, with a historical-literature residual risk. The 2013 source explicitly gives higher-dimensional volume and surface-area formulas and says that an analogous mean-width formula was not attempted. Later inspected work on congruent-ball intersections and \(\lambda\)-convex lenses uses first intrinsic volume or lens support functions for extremal inequalities but does not state the explicit incomplete-beta evaluation. Targeted searches for the formula, its support-function form, and arbitrary-dimensional lens mean width produced no covering statement. The main unresolved risk is Hadwiger's 1957 quermassintegral treatment cited by Finch; the source was not available in sufficiently inspectable form to rule out an equivalent formula hidden there.

## Value
PASS. This closes a concrete formula gap identified in the motivating source and supplies more than a numerical value: the support function is explicit in every dimension, the mean width is a closed special-function expression, the scaling law is immediate, and strict monotonicity in center separation is proved. These formulas give direct quantitative input for later arbitrary-dimensional lens extremal problems.

## Closest literature and limitations
Finch (arXiv:1301.5515v1) is the closest source: it gives the three-dimensional lens mean width and explicitly stops before the higher-dimensional analogue. Bezdek (arXiv:1912.05118v1) and Drach–Tatarko (arXiv:2511.11901v1) supply broader intrinsic-volume and mean-width extremal frameworks for ball bodies and \(\lambda\)-convex lenses, but the inspected text does not state this closed formula. The claim is limited to two congruent balls and does not assert novelty over every inaccessible historical source.

Same-model review: passed. Independent audit: not yet performed.
