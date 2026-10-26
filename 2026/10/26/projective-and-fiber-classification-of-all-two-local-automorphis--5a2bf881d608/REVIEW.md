# Scientific review: projective-and-fiber two-local Heisenberg classification

## Correctness — PASS

The algebraic normal form of an ordinary automorphism follows from the characteristic derived line and the determinant action on the alternating bracket. Necessity reconstructs all parameters from pair witnesses: scalar homogeneity, a single central multiplier, a quotient map constant on each central fiber, injective projective direction map, injective fiber maps, and compatibility under scalar multiplication. Sufficiency explicitly constructs a witnessing matrix and central shear for each of four exhaustive configurations of two projected vectors: independent, dependent nonzero, one zero, or both zero. The dependent case uses injectivity to prove simultaneous vanishing of the residuals, which permits the required nonzero determinant. The finite-field formula counts independent, uniquely recoverable choices without hidden stabilizer overcounting.

The package's checker independently enumerates actual automorphism orbits on ordered pairs. It exhaustively tests all \(40320\) bijections of \(H(\mathbb F_2)\), finding exactly \(48\) two-local maps, precisely matching all \(48\) parameterized ones. It tests all ordered pairs for randomized parameterized maps over \(\mathbb F_3\) and \(\mathbb F_4\). The infinite-field and general finite-field cases rest on the complete proof, not finite enumeration. No characteristic restriction is used.

## Originality — PASS, subject to identified access risk

Ayupov–Kudaybergenov (arXiv:1602.05187v1, Section 3, Theorems 3.1–3.2) constructs nonlinear two-local automorphisms on broad classes of nilpotent Lie algebras using homogeneous central perturbations; the full inspected text contains neither the converse projective/fiber characterization nor the count of all maps. An exact finite-field enumeration is also not implied by merely knowing existence of a nonautomorphism. The 2024 model-filiform study and the 2024/2025 Heisenberg study advertise local and **linear** two-local classifications; the latter's full text was inaccessible, so any unadvertised related result remains a residual risk. Independent mathematical priority is not certified.

Equivalent-formulation, broader-coverage, exact-table, and claim-versus-prior implications were checked against the relevant published primary sources, direct phrase/alias searches, mathematical research index, and available local claim history. No source checked establishes this all-map classification and exact count. The closest index entries concern ordinary Heisenberg automorphisms or unrelated subalgebra invariants. The 2025 comparison is not declared definitively noncovering based on its abstract alone.

## Value — PASS

The previously motivated distinction between automorphisms and two-local automorphisms in nilpotent Lie algebras is upgraded to an unrestricted structural classification for a canonical nonabelian example. It identifies two independent sources of nonlinear freedom—an arbitrary projective-line injection and arbitrary injective central-fiber functions—and measures their dramatic finite-field growth by an exact formula. The ratio to the ordinary automorphism group already equals \(2\) over \(\mathbb F_2\) and \(2304\) over \(\mathbb F_3\). These are not arbitrary finite test cases: the statement classifies a natural local-symmetry class over every field and quantifies it over every finite field.

## Limitations and literature

The count is restricted to the three-dimensional Heisenberg algebra, although the characterization allows arbitrary fields. The exact formula is proved symbolically, not inferred from a finite test. Full-text access to DOI:10.1007/s11464-023-0061-6 was unavailable, and future comparison may change the assessment of priority. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
