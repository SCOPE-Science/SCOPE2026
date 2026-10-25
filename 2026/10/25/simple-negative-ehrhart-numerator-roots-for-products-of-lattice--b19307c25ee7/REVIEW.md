# Scientific review: polygon-product Ehrhart roots

## Correctness — PASS

Pick's formula fixes both quadratic Ehrhart polynomials. The explicitly displayed four coefficients of the degree-at-most-four numerator are independently reproduced by the exact finite-difference transform of the product lattice counts. The critical nonstandard step is positivity of seven finite polynomial expansions. `coefficient_certificate.json` stores all monomials, and `verify.py` regenerates and compares them exactly: 784 for the full quartic discriminant; 36 each for its two root witnesses; 75 and 25 for the two cubic discriminants; and 6 and 3 for quadratic boundary cases. Positivity plus a strictly negative evaluation at \(-2/p\) proves four real quartic roots, while positive cubic discriminants prove three real cubic roots. Strictly positive numerator coefficients then force all roots to be negative. The cases with zero interior lattice points are treated separately rather than incorrectly counted as quartics.

## Originality — PASS under inspected evidence

The nearest published general statement is the Cartesian-product real-rootedness preservation theorem quoted in Feihu Liu, arXiv:2610.06338, Section 2: it assumes both factor numerators are already real-rooted. A lattice polygon has non-real-rooted numerator exactly when it is a three-boundary-point triangle with one, two, or three interior lattice points. The present theorem resolves precisely these exceptional inputs for every polygon counterpart, and establishes simplicity of all resulting roots. Yanxin Liu–Jianxi Mao, arXiv:2609.11589, yields log-concavity, strictly weaker than real-rootedness. The 2024 Brändén–Ferroni–Jochemko inequalities paper does not directly cover the exceptional non-real-rooted factor case. Nill's large-width condition is not universal for primitive-edge triangles. Exact title/parameter and semantic searches of related published records revealed a lattice-segment log-concavity result but no all-polygon real-rootedness implication. These searches do not certify historical uniqueness; an unindexed Segre-product result remains a priority risk.

## Mathematical value — PASS

The real-rootedness of a Cartesian product is not generally implied by log-concavity of its factors, and the simplest exceptional triangle has numerator \(1+t+t^2\) with nonreal zeros. Its Cartesian square has four distinct negative roots, and the proof extends this phenomenon to *every* product of two lattice polygons. This fills the exact naturally occurring exception to the published product-preservation mechanism and produces a complete, dimension-four structural theorem, not a single numerical calculation or arbitrary slice. The exact simplicity refinement also determines the absence of repeated nonzero roots.

## Sources and limitations

Primary sources inspected: Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, Introduction and entire Cartesian-product section; Yanxin Liu and Jianxi Mao, *Preservation of log-concavity under Hadamard products*, arXiv:2609.11589, Sections 1–3 and its main theorem; Brändén, Ferroni and Jochemko, *Preservation of inequalities under Hadamard products*, arXiv:2408.12386, main theorems and Hadamard-product implications; Benjamin Nill, arXiv:2608.03635, theorem statement and introductory scope. Historical priority is not independently certified. The computational positivity certificate is complete exact algebra, but its 784-term expansion has not been replaced by a short conceptual identity.

Self-review: passed. Independent audit: not yet performed.
