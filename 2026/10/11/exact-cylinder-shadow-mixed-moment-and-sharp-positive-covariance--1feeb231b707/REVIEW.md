# Review of the cylinder shadow covariance theorem

## Correctness: PASS

The cylinder is an ellipse-plus-segment Minkowski sum after planar projection. The exact expressions for area and perimeter follow by additivity and Cauchy's perimeter formula. Every expectation used in the mixed moment is derived directly, including the elliptic integral. Exact rational comparisons from the 144-term hypergeometric series, a proved tail bound and alternating arctangent enclosures show the covariance quadratic has strictly negative discriminant and positive leading coefficient. Its unique positive vertex and minimum then follow. The standalone verifier passes its exact rational certificate and independent finite geometric checks. Computational sampling alone is not used as an infinite proof.

## Originality: PASS, with residual risk

Finch (arXiv:1203.2464v1) explicitly computes or reports shadow-area/perimeter moments for three-dimensional regular polyhedra and four-dimensional analogues. His Section 5 also contains the same weighted complete-elliptic integral as a component of the cube perimeter-second-moment calculation; this previously known integral is not claimed novel. No cylinder mixed-area/perimeter calculation or universal right-cylinder covariance inequality is among his results. Kim--Yaskin--Zvavitch (arXiv:1512.07289v1) investigate one-dimensional distributions of projection volumes and comparison/uniqueness questions, not this joint statistic or its shape optimization. A related four-dimensional orthotope calculation has a different geometric object and ambient dimension; its formulas do not imply the right-cylinder theorem. Other candidate records concern unrelated cylinder approximation, lens mean width and finite polytopes. An unlocated equivalent historical elliptic-integral calculation or a stronger universal correlation theorem remains a residual risk; record-search failure is not treated as novelty proof.

## Value: PASS

Random-shadow area/perimeter dependence can change sign across natural solids, making its sign for a full continuous family a genuinely motivated question. The exact mixed moment yields both a nontrivial all-aspect positivity result and a sharp, interior shape optimizer with an explicit constant. It is not merely a recomputation of a mean or a parameter substitution; the negative mixed covariance contributions must be dominated by a certified global discriminant bound. The result supplies a reproducible continuous-body benchmark for projection statistics.

## Limitations and access

The proof is restricted to isotropic planar shadows of solid right circular cylinders. It does not establish any general positive-dependence theorem for other convex bodies. Both relevant arXiv primary texts were read in full-text HTML format; no comparison rests on abstracts alone. Historical overlap cannot be ruled out absolutely. The rational certificate proves the strict sign, while finite hull checks test implementation and normalization.

Same-model review: passed. Independent audit: not yet performed.
