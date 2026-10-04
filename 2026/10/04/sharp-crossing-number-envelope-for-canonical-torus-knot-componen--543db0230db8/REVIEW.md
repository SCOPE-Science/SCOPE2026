# Scientific review

## Correctness
PASS. The determinant-one component tree converts a fixed component-size fiber into the depth-\(u\) additive tree on \((a,b)\). The row sums give \(P=a+b\) and \(Q=(v-u)P+b\), so the torus-knot crossing number is exactly \(P((v-u)P+b-1)\). The lower and upper bounds follow from sharp depth bounds on the additive tree, including uniqueness. The fixed-total-size comparison is an exact Fibonacci calculation. The supplied script reconstructs the canonical split and verifies representative finite ranges independently.

## Originality
PASS. The closest published-finding corpus record proves the exact number \(2^u\) of knots in each component-size fiber but does not bound their crossing numbers. Lin--Spreer give the canonical split, examples, and qualitative linear/Fibonacci growth families, while the earlier link-diagram literature gives a Fibonacci family showing exponential crossing growth from small triangulations. Targeted searches for fixed-component crossing extrema, equivalent formulations, and stronger envelope statements found no statement implying the sharp two-sided formulas and unique extremizers proved here. Residual risk remains because the motivating preprint is recent.

## Value
PASS. The result turns the qualitative crossing-versus-canonical-size phenomenon into an exact sharp envelope on every canonical component-size fiber, identifies both extremal knot types, and then solves the natural fixed-total-size maximum. It directly refines the source paper's comparison of crossing number with canonical triangulation size rather than introducing an arbitrary slice.

## Closest literature and limitations
The closest prior mathematical statement is the exact component-size census in the published-finding corpus record `2026/9/18/SCOPE-exact-canonical-torus-knot-triangulation-census--831655b0b665`; it supplies the fiber parametrization but not the crossing extremum. The theorem is about canonical layered size and does not settle minimal triangulation complexity.

Same-model review: passed. Independent audit: not yet performed.
